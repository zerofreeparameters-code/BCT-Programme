"""
Gate CRIT2 -- independent compact U(1) lattice gauge simulator.

Written in the Gate CRIT2 thread (8 Oct 2026) from the card's section 3 specification
only. No code from Gate CRIT was opened.

Lattices
  D4  : sites = points of Z^4 with even coordinate sum, periodic box of side L (L even).
        24 neighbours r in {+-e_i +- e_j, i<j}. One angle per nearest-neighbour pair
        (12 stored "positive" directions per site). Plaquettes = triangles
        (x, x+r1, x+r1+r2) with r1, r2, r1+r2 all neighbour vectors.
        Asserted: 32 triangles per site, every link in exactly 8 triangles.
  HC  : hypercubic Z^4, side L, 4 links per site, 6 square plaquettes per site
        (validation only). Asserted: every link in exactly 6 plaquettes.

Action      S = beta * sum_p (1 - cos theta_p)
Observables E = mean_p (1 - cos theta_p);  C = N_p * var(E)
Update      sequential single-link heat bath (exact von Mises draw, Best-Fisher 1979).
            One sweep = one heat-bath update of every stored link, in storage order.
Seeds       seed = 7919*L + round(1e4*beta) + s, s = 0 hot, 1 cold, 2 mixed.
            The numba RNG is seeded inside the jitted code, and the initial
            configuration is drawn from it, so a run is fixed by its seed.
"""
import itertools
import numpy as np
from numba import njit

TWO_PI = 2.0 * np.pi


# ----------------------------------------------------------------------------------
# Lattice construction (NumPy, vectorised)
# ----------------------------------------------------------------------------------
def _coords(L):
    g = np.indices((L, L, L, L)).reshape(4, -1).T  # (L^4, 4), C order
    return g


def _full_index(c, L):
    c = np.mod(c, L)
    return ((c[..., 0] * L + c[..., 1]) * L + c[..., 2]) * L + c[..., 3]


def d4_roots():
    pos = []
    for i, j in itertools.combinations(range(4), 2):
        v = np.zeros(4, dtype=np.int64); v[i] = 1; v[j] = 1; pos.append(v)
    for i, j in itertools.combinations(range(4), 2):
        v = np.zeros(4, dtype=np.int64); v[i] = 1; v[j] = -1; pos.append(v)
    pos = np.array(pos)                       # 12 positive directions
    allr = np.concatenate([pos, -pos])        # 24 neighbour vectors
    return pos, allr


def d4_triangle_shapes():
    """Translation classes of triangles {0, r1, r1+r2}; returns list of (a, b)."""
    _, allr = d4_roots()
    rset = {tuple(r) for r in allr}
    shapes = set()
    for r1 in allr:
        for r2 in allr:
            s = r1 + r2
            if tuple(s) in rset:
                verts = [np.zeros(4, dtype=np.int64), r1, s]
                m = min(verts, key=lambda v: tuple(v))
                shp = tuple(sorted(tuple(v - m) for v in verts))
                shapes.add(shp)
    out = []
    for shp in sorted(shapes):
        z, a, b = (np.array(v) for v in shp)
        assert tuple(z) == (0, 0, 0, 0)
        out.append((a, b))
    return out


def build_d4(L):
    assert L % 2 == 0 and L >= 4
    pos, allr = d4_roots()
    coords = _coords(L)
    even = (coords.sum(axis=1) % 2) == 0
    sites = coords[even]                       # (Ns, 4)
    Ns = sites.shape[0]
    assert Ns == L ** 4 // 2
    compact = -np.ones(L ** 4, dtype=np.int64)
    compact[_full_index(sites, L)] = np.arange(Ns)
    ndir = 12
    nlinks = Ns * ndir
    posmap = {tuple(v): d for d, v in enumerate(pos)}

    def step(y, r):
        """Link index and sign for the directed step y -> y + r (y: (Ns,4))."""
        rt = tuple(r)
        if rt in posmap:
            d = posmap[rt]
            base = y
            sgn = 1
        else:
            d = posmap[tuple(-np.array(r))]
            base = y + np.array(r)          # y - v_d
            sgn = -1
        ci = compact[_full_index(base, L)]
        assert (ci >= 0).all()
        return ci * ndir + d, sgn

    shapes = d4_triangle_shapes()
    assert len(shapes) == 32, len(shapes)
    pl, ps = [], []
    for a, b in shapes:
        l1, s1 = step(sites, a)
        l2, s2 = step(sites + a, b - a)
        l3, s3 = step(sites + b, -b)
        pl.append(np.stack([l1, l2, l3], axis=1))
        ps.append(np.tile(np.array([s1, s2, s3], dtype=np.int64), (Ns, 1)))
    plaq_links = np.concatenate(pl)
    plaq_signs = np.concatenate(ps)
    P = plaq_links.shape[0]
    assert P == 32 * Ns, (P, Ns)
    cnt = np.bincount(plaq_links.ravel(), minlength=nlinks)
    assert (cnt == 8).all(), (cnt.min(), cnt.max())
    # every triangle distinct (as a set of links)
    srt = np.sort(plaq_links, axis=1)
    assert np.unique(srt, axis=0).shape[0] == P
    # no triangle uses the same link twice
    assert (srt[:, 0] != srt[:, 1]).all() and (srt[:, 1] != srt[:, 2]).all()
    link_origin = np.repeat(sites, ndir, axis=0)   # origin site coords of each link
    link_vec = np.tile(pos, (Ns, 1))
    return dict(name="d4", L=L, Ns=Ns, nlinks=nlinks, plaq_links=plaq_links,
                plaq_signs=plaq_signs, link_origin=link_origin, link_vec=link_vec,
                links_per_site=12, plaq_per_site=32, plaq_per_link=8)


def build_hc(L):
    assert L >= 4
    coords = _coords(L)
    Ns = L ** 4
    e = np.eye(4, dtype=np.int64)

    def lk(y, mu):
        return _full_index(y, L) * 4 + mu

    pl, ps = [], []
    for mu in range(4):
        for nu in range(mu + 1, 4):
            l1 = lk(coords, mu)
            l2 = lk(coords + e[mu], nu)
            l3 = lk(coords + e[nu], mu)
            l4 = lk(coords, nu)
            pl.append(np.stack([l1, l2, l3, l4], axis=1))
            ps.append(np.tile(np.array([1, 1, -1, -1], dtype=np.int64), (Ns, 1)))
    plaq_links = np.concatenate(pl)
    plaq_signs = np.concatenate(ps)
    nlinks = 4 * Ns
    assert plaq_links.shape[0] == 6 * Ns
    cnt = np.bincount(plaq_links.ravel(), minlength=nlinks)
    assert (cnt == 6).all()
    link_origin = np.repeat(coords, 4, axis=0)
    link_vec = np.tile(e, (Ns, 1))
    return dict(name="hc", L=L, Ns=Ns, nlinks=nlinks, plaq_links=plaq_links,
                plaq_signs=plaq_signs, link_origin=link_origin, link_vec=link_vec,
                links_per_site=4, plaq_per_site=6, plaq_per_link=6)


def build_staples(lat):
    """For each link l: the other links of each plaquette containing l, with signs
    such that cos(theta_p) = cos(theta_l + sum_j sgn_j theta_j)."""
    PL, PS = lat["plaq_links"], lat["plaq_signs"]
    P, n = PL.shape
    m = lat["plaq_per_link"]
    nl = lat["nlinks"]
    rows_l, rows_o, rows_s = [], [], []
    for k in range(n):
        others = [j for j in range(n) if j != k]
        rows_l.append(PL[:, k])
        rows_o.append(PL[:, others])
        rows_s.append(PS[:, [k]] * PS[:, others])
    lk = np.concatenate(rows_l)
    ol = np.concatenate(rows_o)
    os_ = np.concatenate(rows_s)
    order = np.argsort(lk, kind="stable")
    lk = lk[order]
    assert (lk.reshape(nl, m) == np.arange(nl)[:, None]).all()
    stp_l = np.ascontiguousarray(ol[order].reshape(nl, m, n - 1)).astype(np.int64)
    stp_s = np.ascontiguousarray(os_[order].reshape(nl, m, n - 1)).astype(np.float64)
    lat["stp_l"] = stp_l
    lat["stp_s"] = stp_s
    lat["PS_f"] = PS.astype(np.float64)
    return lat


def build(name, L):
    lat = build_d4(L) if name == "d4" else build_hc(L)
    return build_staples(lat)


def run_seed(L, beta, s):
    return int(7919 * L + int(round(1e4 * beta)) + s)


# ----------------------------------------------------------------------------------
# Numba kernels
# ----------------------------------------------------------------------------------
@njit(cache=True)
def nb_seed(s):
    np.random.seed(s)


@njit(cache=True)
def vonmises0(kappa):
    """Draw psi in (-pi, pi] with density ~ exp(kappa cos psi) (Best & Fisher 1979),
    written in a cancellation-free form."""
    if kappa < 1e-12:
        return np.pi * (2.0 * np.random.random() - 1.0)
    q = np.sqrt(1.0 + 4.0 * kappa * kappa)
    tau = 1.0 + q
    rho = tau * 2.0 * kappa / ((q + 1.0) * (tau + np.sqrt(2.0 * tau)))
    r = (1.0 + rho * rho) / (2.0 * rho)
    while True:
        u1 = np.random.random()
        u2 = np.random.random()
        z = np.cos(np.pi * u1)
        f = (1.0 + r * z) / (r + z)
        c = kappa * (r - f)
        if c * (2.0 - c) - u2 > 0.0:
            break
        if u2 > 0.0 and np.log(c / u2) + 1.0 - c >= 0.0:
            break
    if f > 1.0:
        f = 1.0
    elif f < -1.0:
        f = -1.0
    psi = np.arccos(f)
    if np.random.random() < 0.5:
        psi = -psi
    return psi


@njit(cache=True)
def init_hot(nl):
    th = np.empty(nl)
    for i in range(nl):
        th[i] = TWO_PI * np.random.random()
    return th


@njit(cache=True)
def init_mixed(cold_mask):
    nl = cold_mask.shape[0]
    th = np.empty(nl)
    for i in range(nl):
        u = np.random.random()          # drawn for every link to keep the stream fixed
        th[i] = 0.0 if cold_mask[i] else TWO_PI * u
    return th


@njit(cache=True)
def plaq_cos(theta, PL, PSf):
    P, n = PL.shape
    out = np.empty(P)
    for p in range(P):
        a = 0.0
        for k in range(n):
            a += PSf[p, k] * theta[PL[p, k]]
        out[p] = np.cos(a)
    return out


@njit(cache=True)
def energy(theta, PL, PSf):
    P, n = PL.shape
    tot = 0.0
    for p in range(P):
        a = 0.0
        for k in range(n):
            a += PSf[p, k] * theta[PL[p, k]]
        tot += 1.0 - np.cos(a)
    return tot / P


@njit(cache=True)
def staple(theta, stp_l, stp_s, l):
    m = stp_l.shape[1]
    k = stp_l.shape[2]
    re = 0.0
    im = 0.0
    for a in range(m):
        phi = 0.0
        for b in range(k):
            phi += stp_s[l, a, b] * theta[stp_l[l, a, b]]
        re += np.cos(phi)
        im += np.sin(phi)
    return re, im


@njit(cache=True)
def sweep(theta, stp_l, stp_s, beta):
    nl = stp_l.shape[0]
    for l in range(nl):
        re, im = staple(theta, stp_l, stp_s, l)
        amp = np.sqrt(re * re + im * im)
        psi = vonmises0(beta * amp)
        t = psi - np.arctan2(im, re)
        t = t % TWO_PI
        theta[l] = t


@njit(cache=True)
def evolve(theta, stp_l, stp_s, PL, PSf, beta, nsweeps, record):
    """nsweeps sweeps; if record, E after every sweep is returned."""
    out = np.empty(nsweeps if record else 0)
    for i in range(nsweeps):
        sweep(theta, stp_l, stp_s, beta)
        if record:
            out[i] = energy(theta, PL, PSf)
    return out


# ----------------------------------------------------------------------------------
# Driver helpers
# ----------------------------------------------------------------------------------
_CACHE = {}


def get_lat(name, L):
    key = (name, L)
    if key not in _CACHE:
        _CACHE[key] = build(name, L)
    return _CACHE[key]


def initial_state(lat, start):
    nl = lat["nlinks"]
    if start == "hot":
        return init_hot(nl)
    if start == "cold":
        return np.zeros(nl)
    if start == "mixed":
        L = lat["L"]
        cold_mask = lat["link_origin"][:, 0] < (L // 2)   # x_1 < L/2 (first coordinate)
        return init_mixed(cold_mask)
    raise ValueError(start)


def blocked_stats(E, nblk=20):
    E = np.asarray(E)
    n = len(E) // nblk * nblk
    Eb = E[:n].reshape(nblk, -1)
    bm = Eb.mean(axis=1)
    mean = E.mean()
    err = bm.std(ddof=1) / np.sqrt(nblk)
    # jackknife over blocks for var(E)
    jk = []
    for i in range(nblk):
        rest = np.delete(Eb, i, axis=0).ravel()
        jk.append(rest.var())
    jk = np.array(jk)
    var_err = np.sqrt((nblk - 1) / nblk * ((jk - jk.mean()) ** 2).sum())
    return mean, err, var_err


def run_scan(name, L, beta, start, n_therm, n_meas):
    """Section 4.3 / 5.1-5.3 style run: E measured every sweep after n_therm."""
    import time
    lat = get_lat(name, L)
    s = {"hot": 0, "cold": 1, "mixed": 2}[start]
    seed = run_seed(L, beta, s)
    nb_seed(seed)
    th = initial_state(lat, start)
    t0 = time.time()
    evolve(th, lat["stp_l"], lat["stp_s"], lat["plaq_links"], lat["PS_f"], beta, n_therm, False)
    E = evolve(th, lat["stp_l"], lat["stp_s"], lat["plaq_links"], lat["PS_f"], beta, n_meas, True)
    dt = time.time() - t0
    P = lat["plaq_links"].shape[0]
    mean, err, var_err = blocked_stats(E)
    C = P * E.var()
    return dict(lattice=name, L=L, beta=beta, start=start, seed=seed, n_therm=n_therm,
                n_meas=n_meas, N_plaq=int(P), E=float(mean), E_err=float(err),
                C=float(C), C_err=float(P * var_err), seconds=round(dt, 2)), E


def run_mixed(name, L, beta, nsweeps, Estar):
    """Section 5.4 run: mixed start, E every sweep (readings every 50 used)."""
    import time
    lat = get_lat(name, L)
    seed = run_seed(L, beta, 2)
    nb_seed(seed)
    th = initial_state(lat, "mixed")
    E0 = energy(th, lat["plaq_links"], lat["PS_f"])
    t0 = time.time()
    E = evolve(th, lat["stp_l"], lat["stp_s"], lat["plaq_links"], lat["PS_f"], beta, nsweeps, True)
    dt = time.time() - t0
    readings = E[49::50]                       # E after sweeps 50, 100, ..., nsweeps
    last = readings[-10:]                      # readings inside the last 500 sweeps
    m = float(last.mean())
    if m < Estar - 0.01:
        outcome = "weak"
    elif m > Estar + 0.01:
        outcome = "strong"
    else:
        outcome = "unresolved"
    return dict(lattice=name, L=L, beta=beta, start="mixed", seed=seed, nsweeps=nsweeps,
                E_initial=float(E0), Estar=float(Estar), E_last500=m,
                E_final=float(E[-1]), readings=[float(x) for x in readings],
                outcome=outcome, seconds=round(dt, 2)), E
