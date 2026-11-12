"""
Gate DL-BETA REP1 -- simulator (written in the run thread from gate_DLBETA_prompt.md section 4.2;
the original run's code was not opened).

Compact U(1), Wilson action S = beta * sum_loops (1 - cos theta_loop) on
  * the FCC void network x time ("void"), loops = rhombi + temporal squares, and
  * Z4 (calibration), loops = square plaquettes.
Every loop of both complexes is a 4-cycle, so one generic kernel serves both.

FIXED BEFORE THE FIRST RUN (card REP1 section 4.2):

Storage order
  Void, space: atom a = ((i*L + j)*L + k)*4 + m, position 4*(i,j,k) + basis[m],
      basis = (0,0,0), (2,2,0), (2,0,2), (0,2,2)  (units a/4, periodic side 4L).
      Node v = 3*a + {0: oct at atom+(2,2,2), 1: tet at atom+(1,1,1), 2: tet at atom+(3,3,3)}.
      Spatial link j = 8*a + o, from the oct of atom a to the tet at oct + OFFSETS[o]
      (oriented oct -> tet), OFFSETS in the order (+,+,+),(+,+,-),(+,-,+),(+,-,-),(-,+,+),...,(-,-,-).
  Void, space x time: slice-major. Block size B = 8N + 3N = 11N per slice.
      link(t, j)  = t*B + j            for spatial link j at slice t,
      temp(t, v)  = t*B + 8N + v       for the temporal link (v,t) -> (v,t+1).
      Loops per slice t, in this order: the 6N rhombi (atom-major, b in card order), then the 8N
      temporal squares (spatial-link order). Loop type 0 = rhombus, 1 = temporal square.
  Z4: site = ((x1*L + x2)*L + x3)*L + x4; link = 4*site + mu (mu = 0..3 <-> x1..x4);
      plaquettes 6 per site, (mu,nu) in order (0,1),(0,2),(0,3),(1,2),(1,3),(2,3).
Sweep order
  link index 0, 1, ..., N_l - 1 (storage order), one heat-bath update of each. No overrelaxation.
Sampler
  Best & Fisher (1979) rejection sampler for von Mises(0, kappa), with
  rho = 2 kappa / (tau + sqrt(2 tau)) (algebraically equal to (tau - sqrt(2 tau))/(2 kappa),
  free of cancellation); kappa < 1e-8 -> uniform. New angle = x - arg(staple sum), wrapped to [0, 2pi).
RNG
  numba's internal Mersenne Twister, seeded with np.random.seed(seed) inside compiled code at the start
  of each chain; the initial configuration is drawn from that stream. Each chain is fixed by its seed.
Starts
  hot = uniform on [0, 2pi); cold = all 0; mixed = links whose mask is 1 set to 0, others uniform
  (the uniform draw is made for every link in storage order, then masked links are zeroed).
Observables (every sweep, after the update of all links)
  E = mean over all loops of (1 - cos theta_loop); E_s over type-0 loops; E_t over type-1 loops.
"""
import numpy as np
from numba import njit

TWO_PI = 2.0 * np.pi

BASIS = [(0, 0, 0), (2, 2, 0), (2, 0, 2), (0, 2, 2)]
OFFSETS = [(sx, sy, sz) for sx in (1, -1) for sy in (1, -1) for sz in (1, -1)]
BVECS = [(2, 2, 0), (2, -2, 0), (2, 0, 2), (2, 0, -2), (0, 2, 2), (0, 2, -2)]
OVECS = [(2, 0, 0), (-2, 0, 0), (0, 2, 0), (0, -2, 0), (0, 0, 2), (0, 0, -2)]


# --------------------------------------------------------------------------------------------
# complexes
# --------------------------------------------------------------------------------------------
def build_void_space(L):
    """Spatial void complex. Returns dict with positions, nodes, links, rhombi (link indices+signs)."""
    S = 4 * L
    N = 4 * L ** 3
    atoms = np.zeros((N, 3), dtype=np.int64)
    for i in range(L):
        for j in range(L):
            for k in range(L):
                for m in range(4):
                    a = ((i * L + j) * L + k) * 4 + m
                    atoms[a] = (4 * i + BASIS[m][0], 4 * j + BASIS[m][1], 4 * k + BASIS[m][2])
    V = 3 * N
    node_pos = np.zeros((V, 3), dtype=np.int64)
    node_type = np.zeros(V, dtype=np.int64)          # 0 oct, 1 tet, 2 tet
    pos2node = {}
    for a in range(N):
        for typ, off in enumerate([(2, 2, 2), (1, 1, 1), (3, 3, 3)]):
            p = tuple(int(x) for x in ((atoms[a] + off) % S))
            v = 3 * a + typ
            assert p not in pos2node, "duplicate node position"
            pos2node[p] = v
            node_pos[v] = p
            node_type[v] = typ
    E = 8 * N
    link_ends = np.zeros((E, 2), dtype=np.int64)
    link_vec = np.zeros((E, 3), dtype=np.int64)       # unwrapped displacement oct -> tet
    pair2link = {}
    for a in range(N):
        o = 3 * a
        for oi, off in enumerate(OFFSETS):
            p = tuple(int(x) for x in ((node_pos[o] + np.array(off)) % S))
            w = pos2node[p]
            assert node_type[w] in (1, 2), "oct-neighbour at (+-1,+-1,+-1) is not a tet"
            j = 8 * a + oi
            link_ends[j] = (o, w)
            link_vec[j] = off
            assert (o, w) not in pair2link, "multi-edge"
            pair2link[(o, w)] = j
    R = 6 * N
    rh_links = np.zeros((R, 4), dtype=np.int64)
    rh_signs = np.zeros((R, 4), dtype=np.int64)
    rh_verts = np.zeros((R, 4, 3), dtype=np.int64)    # unwrapped vertex positions O1,T1,O2,T2
    rh_atom = np.zeros(R, dtype=np.int64)
    rh_b = np.zeros(R, dtype=np.int64)
    r = 0
    for a in range(N):
        A = atoms[a]
        for bi, b in enumerate(BVECS):
            b = np.array(b)
            Os = [np.array(o) for o in OVECS if np.sum((np.array(o) - b) ** 2) == 4]
            Ts = [np.array(t) for t in OFFSETS if np.sum((np.array(t) - b) ** 2) == 3]
            assert len(Os) == 2 and len(Ts) == 2
            O1, O2 = [pos2node[tuple(int(x) for x in ((A + o) % S))] for o in Os]
            T1, T2 = [pos2node[tuple(int(x) for x in ((A + t) % S))] for t in Ts]
            assert node_type[O1] == 0 and node_type[O2] == 0 and node_type[T1] > 0 and node_type[T2] > 0
            # cycle O1 -> T1 -> O2 -> T2 -> O1; links are stored oct -> tet
            rh_links[r] = (pair2link[(O1, T1)], pair2link[(O2, T1)], pair2link[(O2, T2)], pair2link[(O1, T2)])
            rh_signs[r] = (1, -1, 1, -1)
            rh_verts[r] = (A + Os[0], A + Ts[0], A + Os[1], A + Ts[1])
            rh_atom[r] = a
            rh_b[r] = bi
            r += 1
    return dict(L=L, S=S, N=N, atoms=atoms, V=V, node_pos=node_pos, node_type=node_type,
                pos2node=pos2node, E=E, link_ends=link_ends, link_vec=link_vec, pair2link=pair2link,
                R=R, rh_links=rh_links, rh_signs=rh_signs, rh_verts=rh_verts, rh_atom=rh_atom, rh_b=rh_b)


def build_void_spacetime(L, Lt, sp=None):
    """Void network x time. Returns (loops (Np,4), signs (Np,4), ltype (Np,), Nl, meta)."""
    if sp is None:
        sp = build_void_space(L)
    N, V, E, R = sp["N"], sp["V"], sp["E"], sp["R"]
    B = E + V
    Nl = B * Lt
    Np = (R + E) * Lt
    loops = np.zeros((Np, 4), dtype=np.int64)
    signs = np.zeros((Np, 4), dtype=np.int64)
    ltype = np.zeros(Np, dtype=np.int64)
    u = sp["link_ends"][:, 0]
    w = sp["link_ends"][:, 1]
    jj = np.arange(E)
    for t in range(Lt):
        t1 = (t + 1) % Lt
        base = t * (R + E)
        loops[base:base + R] = t * B + sp["rh_links"]
        signs[base:base + R] = sp["rh_signs"]
        ltype[base:base + R] = 0
        q = slice(base + R, base + R + E)
        # u(t) -> w(t) -> w(t+1) -> u(t+1) -> u(t)
        loops[q, 0] = t * B + jj
        loops[q, 1] = t * B + E + w
        loops[q, 2] = t1 * B + jj
        loops[q, 3] = t * B + E + u
        signs[q] = (1, 1, -1, -1)
        ltype[q] = 1
    meta = dict(kind="void", L=L, Lt=Lt, N=N, V=V, Esp=E, R=R, B=B, Nl=Nl, Np=Np, Nv=V * Lt)
    return loops, signs, ltype, Nl, meta, sp


def build_z4(L):
    Ns = L ** 4
    Nl = 4 * Ns
    Np = 6 * Ns
    x = np.array(np.unravel_index(np.arange(Ns), (L, L, L, L))).T   # x[:,0] = x1 (slowest)

    def site(c):
        c = c % L
        return ((c[:, 0] * L + c[:, 1]) * L + c[:, 2]) * L + c[:, 3]

    s0 = site(x)
    assert np.array_equal(s0, np.arange(Ns))
    loops = np.zeros((Np, 4), dtype=np.int64)
    signs = np.zeros((Np, 4), dtype=np.int64)
    k = 0
    pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    e = np.eye(4, dtype=np.int64)
    P = np.zeros((Ns, 6, 4), dtype=np.int64)
    for pi, (mu, nu) in enumerate(pairs):
        P[:, pi, 0] = 4 * s0 + mu
        P[:, pi, 1] = 4 * site(x + e[mu]) + nu
        P[:, pi, 2] = 4 * site(x + e[nu]) + mu
        P[:, pi, 3] = 4 * s0 + nu
    loops = P.reshape(Np, 4)
    signs = np.tile(np.array([1, 1, -1, -1]), (Np, 1))
    ltype = np.zeros(Np, dtype=np.int64)
    meta = dict(kind="z4", L=L, Lt=L, Nl=Nl, Np=Np, Nv=Ns)
    return loops, signs, ltype, Nl, meta, x


def incidence(loops, signs, Nl):
    """CSR: for each link l, rows (other three links, sign_l*sign_j) for every loop containing l."""
    Np = loops.shape[0]
    lk = loops.reshape(-1)
    order = np.argsort(lk, kind="stable")
    counts = np.bincount(lk, minlength=Nl)
    ptr = np.zeros(Nl + 1, dtype=np.int64)
    ptr[1:] = np.cumsum(counts)
    p_idx = order // 4
    k_idx = order % 4
    others = np.zeros((lk.size, 3), dtype=np.int32)
    osgn = np.zeros((lk.size, 3), dtype=np.int8)
    for d in range(1, 4):
        kk = (k_idx + d) % 4
        others[:, d - 1] = loops[p_idx, kk]
        osgn[:, d - 1] = signs[p_idx, k_idx] * signs[p_idx, kk]
    return ptr, others, osgn, counts


# --------------------------------------------------------------------------------------------
# compiled kernels
# --------------------------------------------------------------------------------------------
@njit(cache=True)
def vonmises(kappa):
    if kappa < 1e-8:
        return TWO_PI * np.random.random() - np.pi
    tau = 1.0 + np.sqrt(1.0 + 4.0 * kappa * kappa)
    rho = 2.0 * kappa / (tau + np.sqrt(2.0 * tau))
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
    th = np.arccos(f)
    if np.random.random() < 0.5:
        th = -th
    return th


@njit(cache=True)
def seed_rng(seed):
    np.random.seed(seed)


@njit(cache=True)
def vm_draws(seed, kappa, n):
    np.random.seed(seed)
    out = np.empty(n)
    for i in range(n):
        out[i] = vonmises(kappa)
    return out


@njit(cache=True)
def staple(theta, ptr, oth, osg, l):
    re = 0.0
    im = 0.0
    for q in range(ptr[l], ptr[l + 1]):
        a = osg[q, 0] * theta[oth[q, 0]] + osg[q, 1] * theta[oth[q, 1]] + osg[q, 2] * theta[oth[q, 2]]
        re += np.cos(a)
        im += np.sin(a)
    return re, im


@njit(cache=True)
def sweep(theta, ptr, oth, osg, beta):
    nl = theta.shape[0]
    for l in range(nl):
        re, im = staple(theta, ptr, oth, osg, l)
        R = np.sqrt(re * re + im * im)
        phi = np.arctan2(im, re)
        x = vonmises(beta * R)
        th = (x - phi) % TWO_PI
        theta[l] = th


@njit(cache=True)
def loop_cos(theta, loops, signs):
    Np = loops.shape[0]
    out = np.empty(Np)
    for p in range(Np):
        a = 0.0
        for k in range(4):
            a += signs[p, k] * theta[loops[p, k]]
        out[p] = np.cos(a)
    return out


@njit(cache=True)
def measure(theta, loops, signs, ltype):
    Np = loops.shape[0]
    s_all = 0.0
    s0 = 0.0
    s1 = 0.0
    n0 = 0
    n1 = 0
    for p in range(Np):
        a = signs[p, 0] * theta[loops[p, 0]] + signs[p, 1] * theta[loops[p, 1]] \
            + signs[p, 2] * theta[loops[p, 2]] + signs[p, 3] * theta[loops[p, 3]]
        c = np.cos(a)
        s_all += c
        if ltype[p] == 0:
            s0 += c
            n0 += 1
        else:
            s1 += c
            n1 += 1
    E = 1.0 - s_all / Np
    Es = 1.0 - s0 / n0 if n0 > 0 else np.nan
    Et = 1.0 - s1 / n1 if n1 > 0 else np.nan
    return E, Es, Et


@njit(cache=True)
def run_chain(seed, start, mask, beta, n_sweeps, ptr, oth, osg, loops, signs, ltype):
    """start: 0 hot, 1 cold, 2 mixed (mask==1 -> 0). Returns series[n_sweeps+1, 3] (row 0 = start)."""
    np.random.seed(seed)
    nl = ptr.shape[0] - 1
    theta = np.empty(nl)
    for l in range(nl):
        theta[l] = TWO_PI * np.random.random()
    if start == 1:
        for l in range(nl):
            theta[l] = 0.0
    elif start == 2:
        for l in range(nl):
            if mask[l] == 1:
                theta[l] = 0.0
    out = np.empty((n_sweeps + 1, 3))
    E, Es, Et = measure(theta, loops, signs, ltype)
    out[0, 0] = E
    out[0, 1] = Es
    out[0, 2] = Et
    for s in range(1, n_sweeps + 1):
        sweep(theta, ptr, oth, osg, beta)
        E, Es, Et = measure(theta, loops, signs, ltype)
        out[s, 0] = E
        out[s, 1] = Es
        out[s, 2] = Et
    return out


# --------------------------------------------------------------------------------------------
# lattice cache + one-run entry point
# --------------------------------------------------------------------------------------------
_CACHE = {}


def get_lattice(kind, L):
    key = (kind, L)
    if key not in _CACHE:
        if kind == "void":
            loops, signs, ltype, Nl, meta, sp = build_void_spacetime(L, 3 * L)
            # mixed mask: origin node at time t < Lt/2  <=> link index < (Lt/2)*B (slice-major storage)
            Lt = 3 * L
            mask = np.zeros(Nl, dtype=np.int8)
            idx = np.arange(Nl)
            t_of = idx // meta["B"]
            mask[t_of < Lt / 2.0] = 1
        elif kind == "z4":
            loops, signs, ltype, Nl, meta, x = build_z4(L)
            mask = np.zeros(Nl, dtype=np.int8)
            site = np.arange(Nl) // 4
            x1 = x[site, 0]
            mask[x1 < L / 2.0] = 1
        else:
            raise ValueError(kind)
        ptr, oth, osg, counts = incidence(loops, signs, Nl)
        _CACHE[key] = dict(loops=loops.astype(np.int32), signs=signs.astype(np.int8),
                           ltype=ltype.astype(np.int8), Nl=Nl, meta=meta, mask=mask,
                           ptr=ptr, oth=oth, osg=osg, counts=counts)
    return _CACHE[key]


def seed_for(kind, L, beta, s):
    off = 300000 if kind == "z4" else 700000
    return 7919 * L + round(1e4 * beta) + s + off


def do_run(kind, L, beta, start, n_sweeps):
    """start in {'hot','cold','mixed','hist'}; seed s = 0,1,2,3; hist uses the mixed initial state."""
    import time
    lat = get_lattice(kind, L)
    s = {"hot": 0, "cold": 1, "mixed": 2, "hist": 3}[start]
    st = {"hot": 0, "cold": 1, "mixed": 2, "hist": 2}[start]
    seed = seed_for(kind, L, beta, s)
    t0 = time.time()
    ser = run_chain(seed, st, lat["mask"], float(beta), int(n_sweeps), lat["ptr"], lat["oth"], lat["osg"],
                    lat["loops"], lat["signs"], lat["ltype"])
    dt = time.time() - t0
    return dict(kind=kind, L=L, Lt=lat["meta"]["Lt"], beta=beta, start=start, seed=seed,
                n_sweeps=int(n_sweeps), Np=int(lat["meta"]["Np"]), Nl=int(lat["Nl"]),
                seconds=dt, ms_per_sweep=1e3 * dt / n_sweeps), ser
