"""Gate DL-BETA -- simulator (written in the run thread from card section 4.2).

Compact U(1), Wilson action S = beta * sum_loops (1 - cos theta_loop) on a general complex given as
(loop_links[n_loops,4], loop_signs[n_loops,4], loop_type[n_loops]) with link incidence in CSR form.

Update: sequential single-link heat bath.  For link l, with Z = sum_{p ∋ l} exp(i s_{p,l} theta_p),
the conditional law of theta_l is exp(beta |Z| cos(theta_l + phi)), phi = arg Z - theta_l
(derivation: theta_p = s theta_l + rest_p, cos(s theta + rest) = cos(theta + s rest), and
s rest_p = s theta_p - theta_l).  theta_l + phi is drawn exactly from von Mises(0, beta |Z|) by
the Best-Fisher (1979) rejection algorithm in a cancellation-free form (vm_sample).

SWEEP ORDER (fixed before the first run): one sweep = one update of every link in storage order
l = 0, 1, ..., n_links - 1, the storage order of dlb_complex.py (void: slice-major, inside a slice
the 8N spatial links (oct-major, offset order) then the 3N temporal links; Z4: site-major, mu = 0..3).
No overrelaxation.

RNG: numba's internal generator, seeded inside compiled code with the run's seed; the starting
configuration is drawn from it.  Hot start: uniform in [0, 2pi); cold: all zero; mixed: links with
cold_mask set to zero, all others uniform (drawn in storage order).

Observables after EVERY sweep (thermalisation sweeps included, so mixed-start readings at sweeps
50, 100, ... are available): E = mean (1 - cos theta_p) over all loops, E_s over type-0 loops
(rhombi / Z4 space-space), E_t over type-1 loops (temporal squares / Z4 plaquettes with mu = 0).
"""
import os, sys, time
import numpy as np
import numba as nb

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dlb_complex import VoidST, Z4, incidence_csr

TWOPI = 2.0 * np.pi


@nb.njit(cache=True)
def seed_rng(s):
    np.random.seed(s)


@nb.njit(cache=True)
def vm_sample(kappa):
    """Exact draw from von Mises(0, kappa) on (-pi, pi]; Best & Fisher (1979), cancellation-free.
    b = (a - sqrt(2a))/(2 kappa), a = 1 + sqrt(1 + 4 kappa^2), written as 2 kappa / D with
    D = 1 + s + sqrt(2 + 2 s), s = sqrt(1 + 4 kappa^2); 1 - b = (1 + 1/(s + 2 kappa) + sqrt(2+2s))/D.
    r = (1 + b^2)/(2b).  With z = cos(pi u1): f = (1 + r z)/(r + z),
    c = kappa (r - f) = kappa (r^2 - 1)/(r + z) = kappa (1 - b^2)^2 / (4 b^2 (r + z)),
    arccos f = 2 atan( (1 - b)/(1 + b) * tan(pi u1 / 2) )."""
    if kappa < 1e-12:
        return (2.0 * np.random.random() - 1.0) * np.pi
    s = np.sqrt(1.0 + 4.0 * kappa * kappa)
    sq = np.sqrt(2.0 + 2.0 * s)
    D = 1.0 + s + sq
    b = 2.0 * kappa / D
    omb = (1.0 + 1.0 / (s + 2.0 * kappa) + sq) / D
    r = (1.0 + b * b) / (2.0 * b)
    w = omb * (1.0 + b)                    # 1 - b^2
    cfac = kappa * w * w / (4.0 * b * b)
    rho = omb / (1.0 + b)
    while True:
        u1 = np.random.random()
        u2 = np.random.random()
        z = np.cos(np.pi * u1)
        c = cfac / (r + z)
        if c * (2.0 - c) - u2 > 0.0:
            break
        if u2 > 0.0 and np.log(c / u2) + 1.0 - c >= 0.0:
            break
    th = 2.0 * np.arctan(rho * np.tan(0.5 * np.pi * u1))
    if np.random.random() < 0.5:
        th = -th
    return th


@nb.njit(cache=True)
def vm_many(kappa, n, seed):
    np.random.seed(seed)
    out = np.empty(n)
    for i in range(n):
        out[i] = vm_sample(kappa)
    return out


@nb.njit(cache=True)
def staple(theta, l, LL, LS, ptr, inc_loop, inc_sign):
    """R, phi with sum_{p ∋ l} cos(theta_p) = R cos(theta_l + phi)."""
    zr = 0.0
    zi = 0.0
    for m in range(ptr[l], ptr[l + 1]):
        p = inc_loop[m]
        a = LS[p, 0] * theta[LL[p, 0]] + LS[p, 1] * theta[LL[p, 1]] \
            + LS[p, 2] * theta[LL[p, 2]] + LS[p, 3] * theta[LL[p, 3]]
        a = inc_sign[m] * a
        zr += np.cos(a)
        zi += np.sin(a)
    R = np.sqrt(zr * zr + zi * zi)
    phi = np.arctan2(zi, zr) - theta[l]
    return R, phi


@nb.njit(cache=True)
def sweep(theta, beta, LL, LS, ptr, inc_loop, inc_sign):
    for l in range(theta.shape[0]):
        R, phi = staple(theta, l, LL, LS, ptr, inc_loop, inc_sign)
        x = vm_sample(beta * R)
        t = (x - phi) % TWOPI
        theta[l] = t


@nb.njit(cache=True)
def loop_cos(theta, LL, LS):
    n = LL.shape[0]
    out = np.empty(n)
    for p in range(n):
        a = LS[p, 0] * theta[LL[p, 0]] + LS[p, 1] * theta[LL[p, 1]] \
            + LS[p, 2] * theta[LL[p, 2]] + LS[p, 3] * theta[LL[p, 3]]
        out[p] = np.cos(a)
    return out


@nb.njit(cache=True)
def measure(theta, LL, LS, LT):
    es = 0.0
    et = 0.0
    ns = 0
    nt = 0
    for p in range(LL.shape[0]):
        a = LS[p, 0] * theta[LL[p, 0]] + LS[p, 1] * theta[LL[p, 1]] \
            + LS[p, 2] * theta[LL[p, 2]] + LS[p, 3] * theta[LL[p, 3]]
        e = 1.0 - np.cos(a)
        if LT[p] == 0:
            es += e
            ns += 1
        else:
            et += e
            nt += 1
    E = (es + et) / (ns + nt)
    return E, es / max(ns, 1), et / max(nt, 1)


@nb.njit(cache=True)
def simulate(seed, start, cold_mask, beta, n_sweeps, LL, LS, LT, ptr, inc_loop, inc_sign, n_links):
    """start: 0 hot, 1 cold, 2 mixed (cold_mask links zero, others uniform)."""
    np.random.seed(seed)
    theta = np.zeros(n_links)
    if start == 0:
        for l in range(n_links):
            theta[l] = TWOPI * np.random.random()
    elif start == 2:
        for l in range(n_links):
            if not cold_mask[l]:
                theta[l] = TWOPI * np.random.random()
    E0, Es0, Et0 = measure(theta, LL, LS, LT)
    E = np.empty(n_sweeps)
    Es = np.empty(n_sweeps)
    Et = np.empty(n_sweeps)
    for i in range(n_sweeps):
        sweep(theta, beta, LL, LS, ptr, inc_loop, inc_sign)
        E[i], Es[i], Et[i] = measure(theta, LL, LS, LT)
    return E, Es, Et, E0, theta


# ------------------------------------------------------------------------------------------
_CACHE = {}


def get_complex(lattice, L, Lt=None):
    key = (lattice, L, Lt)
    if key not in _CACHE:
        if lattice == "void":
            cx = VoidST(L, Lt)
            # mixed start (card 4.4 step 4): links whose origin node has time t < Lt/2 set to 0;
            # a link's origin node is in its storage slice (spatial: the oct at t; temporal: (v,t)).
            org_slice = cx.link_org // (3 * cx.N)
            assert (org_slice == cx.link_slice).all()
            cold = org_slice < (Lt / 2.0)
        else:
            cx = Z4(L)
            # CRIT2 5.4: links starting at a site with x1 < L/2 (x1 = first coordinate)
            cold = cx.x[cx.link_org][:, 0] < (L / 2.0)
        ptr, il, isg = incidence_csr(cx.n_links, cx.loop_links, cx.loop_signs)
        arrs = dict(LL=cx.loop_links.astype(np.int64), LS=cx.loop_signs.astype(np.float64),
                    LT=cx.loop_type.astype(np.int64), ptr=ptr, il=il, isg=isg,
                    n_links=int(cx.n_links), n_loops=int(cx.n_loops), n_nodes=int(cx.n_nodes),
                    cold=cold.astype(np.bool_), org=cx.link_org, tgt=cx.link_tgt,
                    n_s=int((cx.loop_type == 0).sum()), n_t=int((cx.loop_type == 1).sum()))
        _CACHE[key] = arrs
    return _CACHE[key]


START = {"hot": 0, "cold": 1, "mixed": 2}


def run_job(spec):
    """spec: lattice, L, Lt, beta, start, seed, n_sweeps.  Returns (record, series dict)."""
    a = get_complex(spec["lattice"], spec["L"], spec.get("Lt"))
    t0 = time.time()
    E, Es, Et, E0, theta = simulate(int(spec["seed"]), START[spec["start"]], a["cold"],
                                   float(spec["beta"]), int(spec["n_sweeps"]), a["LL"], a["LS"],
                                   a["LT"], a["ptr"], a["il"], a["isg"], a["n_links"])
    dt = time.time() - t0
    rec = dict(spec)
    rec.update(n_links=a["n_links"], n_loops=a["n_loops"], n_rhombi_or_ss=a["n_s"],
               n_temporal=a["n_t"], E_start=float(E0), E_final=float(E[-1]),
               wall_s=dt, ms_per_sweep=1e3 * dt / spec["n_sweeps"])
    return rec, dict(E=E, Es=Es, Et=Et)
