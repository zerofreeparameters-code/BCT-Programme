#!/usr/bin/env python3
"""
dlb_deskcheck.py — Gate DL-BETA card-thread desk check. 12 Nov 2026.

What it establishes before the card is registered, and nothing more:

  PART A  The FCC void network as a cell complex (a = 1, periodic box of L conventional cells):
          its minimal loops are exactly the rhombic faces of the FCC Voronoi tessellation (one per
          nearest-neighbour bond); they span every contractible cycle; Euler characteristic 0.
  PART B  The product with time (L_t steps): counts, incidences, and the exact rank of the
          plaquette boundary map, which fixes the weak-coupling target of the simulator.
  PART C  The classical continuum normalisation 1/e^2 = k beta with every smallest loop at the
          same beta (beta_t = beta_s). Method validated on Z4 (k = 1) and D4 (k = 2, the value
          CRIT2's card states) before it is applied to the void complex.
  PART D  A reference heat-bath simulator on a general complex: gauge invariance, local-vs-global
          action, strong-coupling and weak-coupling limits on the void complex and on Z4.
  PART E  Timing, to size the run's budget.

BLINDNESS RULE. Monte Carlo is run ONLY at beta = 0.1 and beta = 20. Nothing is simulated in
[0.2, 5] on any lattice. The card's author has seen no data near any transition.

Every check is an assertion; the script halts on the first failure.
Run:  python3 dlb_deskcheck.py            (all parts)
      python3 dlb_deskcheck.py --no-timing (A-D only)
"""
import argparse
import itertools
import json
import os
import sys
import time

import numpy as np

OK = []


def check(cond, msg):
    if not cond:
        raise SystemExit(f"FAIL: {msg}")
    OK.append(msg)
    print(f"  ok  {msg}")


# ========================================================================================
# 1. GEOMETRY BUILDERS (integer coordinates in units of a/4; box side 4L)
# ========================================================================================
FCC = [(0, 0, 0), (2, 2, 0), (2, 0, 2), (0, 2, 2)]
BONDS = [(2, 2, 0), (2, -2, 0), (2, 0, 2), (2, 0, -2), (0, 2, 2), (0, 2, -2)]
AXIS = [np.array(v) for v in [(2, 0, 0), (-2, 0, 0), (0, 2, 0), (0, -2, 0), (0, 0, 2), (0, 0, -2)]]
DIAG = [np.array(d) for d in itertools.product((-1, 1), repeat=3)]


def build_void(L):
    """Nodes: octs (FCC + (2,2,2)) then tets (FCC + (1,1,1), FCC + (3,3,3)).
    Links: oct -> tet at offset (+-1,+-1,+-1) (distance sqrt3/4 a).
    Rhombi: per FCC bond A -> A+b, the 2 octs and 2 tets adjacent to both atoms, cyclic O-T-O-T."""
    S = 4 * L
    wrap = lambda p: tuple(int(c) % S for c in p)
    atoms, octs, tets = set(), set(), set()
    for i, j, k in itertools.product(range(L), repeat=3):
        o = np.array([4 * i, 4 * j, 4 * k])
        for f in FCC:
            f = np.array(f)
            atoms.add(wrap(o + f)); octs.add(wrap(o + f + 2))
            tets.add(wrap(o + f + 1)); tets.add(wrap(o + f + 3))
    octs, tets, atoms = sorted(octs), sorted(tets), sorted(atoms)
    nodes = octs + tets
    idx = {p: n for n, p in enumerate(nodes)}
    n_oct = len(octs)
    is_oct = np.arange(len(nodes)) < n_oct
    links, lidx = [], {}
    for o in octs:
        for d in DIAG:
            t = wrap(np.array(o) + d)
            if t in idx and not is_oct[idx[t]]:
                key = (idx[o], idx[t])
                if key not in lidx:
                    lidx[key] = len(links); links.append(key)
    rhombi, rgeom = [], []
    for A in atoms:
        A = np.array(A)
        for b in BONDS:
            b = np.array(b)
            O = [A + o for o in AXIS if np.sum((o - b) ** 2) == 4]
            T = [A + t for t in DIAG if np.sum((t - b) ** 2) == 3]
            assert len(O) == 2 and len(T) == 2
            (o1, o2), (t1, t2) = O, T
            rhombi.append((idx[wrap(o1)], idx[wrap(t1)], idx[wrap(o2)], idx[wrap(t2)]))
            rgeom.append((o1, t1, o2, t2, b))
    return dict(L=L, nodes=nodes, n_oct=n_oct, is_oct=is_oct, links=links, lidx=lidx,
                rhombi=rhombi, rgeom=rgeom, atoms=atoms)


def rhombus_links(G):
    """Each rhombus O1-T1-O2-T2 as 4 (link, sign); links are stored oct -> tet."""
    li = G['lidx']
    return [[(li[(o1, t1)], +1), (li[(o2, t1)], -1), (li[(o2, t2)], +1), (li[(o1, t2)], -1)]
            for (o1, t1, o2, t2) in G['rhombi']]


def build_product(L, Lt):
    """(3+1)D complex: spatial links per slice, then temporal links (v,t)->(v,t+1).
    Loops: rhombi in each slice (kind 0), then temporal squares on each spatial link (kind 1)."""
    G = build_void(L)
    V0, E0 = len(G['nodes']), len(G['links'])
    node = lambda v, t: v + V0 * (t % Lt)
    links = [(node(u, t), node(w, t)) for t in range(Lt) for (u, w) in G['links']]
    nsp = len(links)
    links += [(node(v, t), node(v, t + 1)) for t in range(Lt) for v in range(V0)]
    sl = lambda e, t: e + E0 * (t % Lt)
    tl = lambda v, t: nsp + v + V0 * (t % Lt)
    plaqs, kind = [], []
    sp = rhombus_links(G)
    for t in range(Lt):
        for p in sp:
            plaqs.append([(sl(l, t), s) for l, s in p]); kind.append(0)
    for t in range(Lt):
        for e, (u, w) in enumerate(G['links']):
            plaqs.append([(sl(e, t), +1), (tl(w, t), +1), (sl(e, t + 1), -1), (tl(u, t), -1)])
            kind.append(1)
    return dict(G=G, V=V0 * Lt, links=links, nsp=nsp, plaqs=plaqs, kind=np.array(kind), L=L, Lt=Lt)


def boundary_rank(n_links, plaqs):
    M = np.zeros((len(plaqs), n_links))
    for r, pl in enumerate(plaqs):
        for l, s in pl:
            M[r, l] += s
    return np.linalg.matrix_rank(M)


# ========================================================================================
# 2. CONTINUUM NORMALISATION HELPERS
# ========================================================================================
PAIRS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]     # index 3 = time
EL, MAG = [2, 4, 5], [0, 1, 3]


def bivec(Pts):
    """Oriented area bivector sigma^{mu nu} (mu < nu) of a closed planar polygon of 4-vectors."""
    s = np.zeros((4, 4))
    for i in range(len(Pts)):
        x, y = Pts[i], Pts[(i + 1) % len(Pts)]
        s += 0.5 * (np.outer(x, y) - np.outer(y, x))
    return np.array([s[m, v] for m, v in PAIRS])


def normalisation(name, bivecs, vol, k_expected=None):
    Q = sum(np.outer(b, b) for b in bivecs) / vol
    off = np.max(np.abs(Q - np.diag(np.diag(Q))))
    cE, cB = np.diag(Q)[EL], np.diag(Q)[MAG]
    check(off < 1e-12, f"C6 {name}: flux quadratic form is diagonal (max off-diagonal {off:.1e})")
    check(np.ptp(cE) < 1e-12 and np.ptp(cB) < 1e-12, f"C6 {name}: spatially isotropic (3 equal c_E, 3 equal c_B)")
    cE, cB = cE[0], cB[0]
    a_t, k = np.sqrt(cB / cE), np.sqrt(cE * cB)
    print(f"      {name}: c_E(a_t=1) = {cE:.10f}, c_B(a_t=1) = {cB:.10f}  ->  a_t = {a_t:.10f}, k = {k:.10f}")
    if k_expected is not None:
        check(abs(k - k_expected) < 1e-12, f"C6 {name}: k = {k_expected:g}, as expected")
    return a_t, k


# ========================================================================================
# 3. REFERENCE SIMULATOR (sequential single-link heat bath, storage order; LATT §2)
# ========================================================================================
def arrays_from_plaqs(n_links, plaqs, kind):
    pl = np.array([[l for l, s in p] for p in plaqs], dtype=np.int64)
    ps = np.array([[s for l, s in p] for p in plaqs], dtype=np.int64)
    cnt = np.bincount(pl.ravel(), minlength=n_links)
    ptr = np.zeros(n_links + 1, np.int64); ptr[1:] = np.cumsum(cnt)
    order = np.argsort(pl.ravel(), kind='stable')
    lp_p = (order // pl.shape[1]).astype(np.int64)
    lp_j = (order % pl.shape[1]).astype(np.int64)
    return dict(pl=pl, ps=ps, ptr=ptr, lp_p=lp_p, lp_j=lp_j, kind=np.asarray(kind, np.int64), n_links=n_links)


def void_time(L, Lt):
    P = build_product(L, Lt)
    A = arrays_from_plaqs(len(P['links']), P['plaqs'], P['kind'])
    A['links'] = np.array(P['links'], np.int64); A['n_nodes'] = P['V']
    return A


def hypercubic(L):
    N = L ** 4
    site = lambda x: (((x[0] % L) * L + (x[1] % L)) * L + (x[2] % L)) * L + (x[3] % L)
    lk = lambda x, mu: 4 * site(x) + mu
    plaqs, links = [], []
    for x in itertools.product(range(L), repeat=4):
        for mu in range(4):
            y = list(x); y[mu] += 1
            links.append((site(x), site(y)))
        for mu, nu in itertools.combinations(range(4), 2):
            xm = list(x); xm[mu] += 1
            xn = list(x); xn[nu] += 1
            plaqs.append([(lk(x, mu), 1), (lk(xm, nu), 1), (lk(xn, mu), -1), (lk(x, nu), -1)])
    A = arrays_from_plaqs(4 * N, plaqs, np.zeros(len(plaqs), np.int64))
    A['links'] = np.array(links, np.int64); A['n_nodes'] = N
    return A


def _kernels():
    import numba as nb

    @nb.njit(cache=True)
    def seed_rng(s):
        np.random.seed(s)

    @nb.njit(cache=True)
    def plaq_angles(theta, pl, ps):
        P, K = pl.shape
        out = np.empty(P)
        for p in range(P):
            a = 0.0
            for j in range(K):
                a += ps[p, j] * theta[pl[p, j]]
            out[p] = a
        return out

    @nb.njit(cache=True)
    def sweep(theta, beta, pl, ps, ptr, lp_p, lp_j):
        K = pl.shape[1]
        twopi = 2.0 * np.pi
        for l in range(theta.shape[0]):
            re = 0.0
            im = 0.0
            for m in range(ptr[l], ptr[l + 1]):
                p = lp_p[m]
                jj = lp_j[m]
                rest = 0.0
                for j in range(K):
                    if j != jj:
                        rest += ps[p, j] * theta[pl[p, j]]
                a = ps[p, jj] * rest
                re += np.cos(a)
                im += np.sin(a)
            kappa = beta * np.sqrt(re * re + im * im)
            phi = np.arctan2(im, re)
            x = np.random.vonmises(0.0, kappa) if kappa > 1e-12 else np.random.uniform(-np.pi, np.pi)
            theta[l] = (-phi + x) % twopi

    @nb.njit(cache=True)
    def run(theta, beta, n_therm, n_meas, pl, ps, ptr, lp_p, lp_j, kind):
        E = np.empty(n_meas); Es = np.empty(n_meas); Et = np.empty(n_meas); Cs = np.empty(n_meas)
        for i in range(n_therm):
            sweep(theta, beta, pl, ps, ptr, lp_p, lp_j)
        for i in range(n_meas):
            sweep(theta, beta, pl, ps, ptr, lp_p, lp_j)
            ang = plaq_angles(theta, pl, ps)
            ea = 0.0; es = 0.0; et = 0.0; ns = 0; nt = 0; cs = 0.0
            for p in range(ang.shape[0]):
                c = np.cos(ang[p])
                ea += 1.0 - c; cs += c
                if kind[p] == 0:
                    es += 1.0 - c; ns += 1
                else:
                    et += 1.0 - c; nt += 1
            E[i] = ea / ang.shape[0]; Cs[i] = cs / ang.shape[0]
            Es[i] = es / max(ns, 1); Et[i] = et / max(nt, 1)
        return E, Es, Et, Cs

    return seed_rng, plaq_angles, sweep, run


def blocked(x, nblk=20):
    m = np.array([v.mean() for v in np.array_split(x, nblk)])
    return x.mean(), m.std(ddof=1) / np.sqrt(nblk)


# ========================================================================================
# PARTS
# ========================================================================================
def part_A():
    print("=" * 80)
    print("PART A — the spatial void complex")
    print("=" * 80)
    for L in (2, 3):
        G = build_void(L)
        N = 4 * L ** 3
        V, E, F = len(G['nodes']), len(G['links']), len(G['rhombi'])
        print(f"\nL = {L}: N = {N} primitive cells; V = {V}, E = {E}, rhombi = {F}, atoms = {len(G['atoms'])}")
        check(V == 3 * N and E == 8 * N and F == 6 * N and len(G['atoms']) == N,
              f"C1 L={L}: per primitive cell V = 3, E = 8, rhombi = 6, 3-cells = 1")
        deg = np.bincount(np.array(G['links']).ravel(), minlength=V)
        check(set(deg[G['is_oct']]) == {8} and set(deg[~G['is_oct']]) == {4}, f"C1 L={L}: degree oct 8, tet 4")
        check(all(G['is_oct'][u] and not G['is_oct'][w] for u, w in G['links']), f"C1 L={L}: every link oct-tet (bipartite)")
        areas, pdev, nok = [], 0.0, True
        for (o1, t1, o2, t2, b) in G['rgeom']:
            P = [np.array(x, float) / 4 for x in (o1, t1, o2, t2)]
            av = 0.5 * sum(np.cross(P[i], P[(i + 1) % 4]) for i in range(4))
            n = av / np.linalg.norm(av)
            areas.append(np.linalg.norm(av))
            pdev = max(pdev, max(abs(np.dot(p - P[0], n)) for p in P))
            nok &= abs(abs(np.dot(n, b / np.linalg.norm(b))) - 1) < 1e-12
        pl = rhombus_links(G)
        check(len(pl) == F, f"C2 L={L}: every rhombus edge is an existing window link")
        check(pdev < 1e-12, f"C2 L={L}: every rhombus planar")
        check(np.allclose(areas, 1 / (4 * np.sqrt(2))), f"C2 L={L}: rhombus area = a^2/(4 sqrt2)")
        check(nok, f"C2 L={L}: rhombus normal along its FCC bond (<110>)")
        nbr = {v: set() for v in range(V)}
        for u, w in G['links']:
            nbr[u].add(w); nbr[w].add(u)
        cyc = set()
        octs = [v for v in range(V) if G['is_oct'][v]]
        for a_, b_ in itertools.combinations(octs, 2):
            for t1, t2 in itertools.combinations(sorted(nbr[a_] & nbr[b_]), 2):
                cyc.add(frozenset([a_, b_, t1, t2]))
        rh = set(frozenset(r) for r in G['rhombi'])
        check(len(rh) == F, f"C3 L={L}: no duplicate rhombi")
        check(cyc == rh, f"C3 L={L}: the 4-cycles of the void graph are exactly the rhombi ({len(cyc)})")
        cnt = np.bincount([l for p in pl for l, s in p], minlength=E)
        check(set(cnt) == {3}, f"C3 L={L}: every window link lies in exactly 3 rhombi")
        r = boundary_rank(E, pl)
        check(r == E - V - 2 == 5 * N - 2, f"C4 L={L}: rank d2 = {r} = E - V - 2 = 5N - 2 (rhombi span all contractible cycles)")
        check(V - E + F - N == 0, f"C4 L={L}: Euler characteristic V - E + F - C3 = 0 (a cellulation of T^3)")


def part_B():
    print()
    print("=" * 80)
    print("PART B — product with time")
    print("=" * 80)
    L, Lt = 2, 6
    P = build_product(L, Lt)
    N = 4 * L ** 3
    Nl, Np, Nv = len(P['links']), len(P['plaqs']), P['V']
    print(f"\nL = {L}, L_t = {Lt}: N_v = {Nv}, N_l = {Nl}, N_p = {Np}")
    check(Nl == 11 * N * Lt and Np == 14 * N * Lt and Nv == 3 * N * Lt, "C5: per cell per slice N_v = 3, N_l = 11, N_p = 14")
    inc = np.bincount([l for p in P['plaqs'] for l, s in p], minlength=Nl)
    check(set(inc[:P['nsp']]) == {5}, "C5: every spatial link in 5 loops (3 rhombi + 2 temporal squares)")
    G = P['G']; V0 = len(G['nodes'])
    tinc = inc[P['nsp']:].reshape(Lt, V0)
    check(set(tinc[:, G['is_oct']].ravel()) == {8} and set(tinc[:, ~G['is_oct']].ravel()) == {4},
          "C5: temporal links in 8 (oct) or 4 (tet) squares")
    r = boundary_rank(Nl, P['plaqs'])
    check(r == Nl - Nv - 3, f"C5: rank d2 = {r} = N_l - N_v - 3 = N_l - (N_v - 1) - b1(T^4)")
    print(f"      mean loops per link = 4 N_p / N_l = {4*Np/Nl:.6f} (= 56/11; Z4: 6; D4: 8)")
    print(f"      weak-coupling target E -> rank/(2 beta N_p); infinite volume 8/(28 beta) = 2/(7 beta) = 0.285714/beta")
    # C7: zero-momentum mode count. Classes of links modulo lattice translations (space and time):
    # 8 spatial classes (oct -> tet offset d in {+-1}^3) and 3 temporal classes (node sublattice).
    fccmod = {(0, 0, 0), (2, 2, 0), (2, 0, 2), (0, 2, 2)}
    S4 = 4 * L
    cls = np.empty(Nl, np.int64)
    dirs = [tuple(d) for d in DIAG]
    for li, (a_, b_) in enumerate(P['links']):
        u, w = a_ % V0, b_ % V0
        if li < P['nsp']:
            pu, pw = np.array(G['nodes'][u]), np.array(G['nodes'][w])
            d = tuple(int(x) for x in ((pw - pu + S4 // 2) % S4 - S4 // 2))
            cls[li] = dirs.index(d)
        else:
            if G['is_oct'][u]:
                cls[li] = 8
            else:
                q = tuple(int(x) % 4 for x in (np.array(G['nodes'][u]) - 1))
                cls[li] = 9 if q in fccmod else 10
    check(np.all(np.bincount(cls, minlength=11) == Nl // 11), "C7: 11 link classes per cell per slice, equally populated")
    M = np.zeros((Np, 11))
    for r_, pl_ in enumerate(P['plaqs']):
        for l, s in pl_:
            M[r_, cls[l]] += s
    r0 = np.linalg.matrix_rank(M)
    check(r0 == 5, f"C7: at zero crystal momentum the loop map has rank {r0} = 5 per cell")
    print("      => of the 8 action-carrying link modes per cell (rank d2 per cell), 5 cost action already at")
    print("         k = 0: optical branches, gapped at the lattice scale at tree level. The remaining 3 are")
    print("         acoustic (constant A_mu mod gauge: 4 holonomies + 2 sublattice gauge = 6 = 11 - 5 at k = 0)")
    print("         and form the photon. This is the tree-level content of CN-DL-05 (DL left it CONJECTURE).")


def part_C():
    print()
    print("=" * 80)
    print("PART C — classical continuum normalisation 1/e^2 = k beta (all smallest loops at one beta)")
    print("=" * 80)
    print("A constant F gives each loop theta_p = sum_{mu<nu} F_{mu nu} sigma_p^{mu nu}. (beta/2) sum_p theta_p^2")
    print("per unit 4-volume must equal (1/2e^2) sum_{mu<nu} F_{mu nu}^2. c_E ~ a_t and c_B ~ 1/a_t, so")
    print("light speed 1 fixes a_t = sqrt(c_B/c_E) and then k = sqrt(c_E c_B), both at a_t = 1.")
    e = np.eye(4)
    print("\n  Z4 (method validation):")
    normalisation("Z4", [bivec([0 * e[0], e[m], e[m] + e[v], e[v]]) for m, v in PAIRS], 1.0, k_expected=1.0)
    nbv = [s1 * e[i] + s2 * e[j] for i, j in itertools.combinations(range(4), 2) for s1 in (1, -1) for s2 in (1, -1)]
    nbset = set(tuple(v.astype(int)) for v in nbv)
    tri = set()
    for r1 in nbv:
        for r2 in nbv:
            q = r1 + r2
            if tuple(q.astype(int)) in nbset:
                vs = sorted(tuple(v.astype(int)) for v in (np.zeros(4), r1, q))
                base = np.array(vs[0])
                tri.add(tuple(sorted(tuple((np.array(v) - base).astype(int)) for v in vs)))
    print(f"\n  D4 (method validation): triangle translation classes per site = {len(tri)}")
    check(len(tri) == 32, "C6 D4: 32 triangles per site (CRIT2 card §3)")
    normalisation("D4", [bivec([np.array(v, float) for v in t]) for t in tri], 2.0, k_expected=2.0)
    G = build_void(2)
    bv = []
    for (o1, t1, o2, t2, b) in G['rgeom']:
        bv.append(bivec([np.append(np.array(x, float) / 4, 0.0) for x in (o1, t1, o2, t2)]))
    for (u, w) in G['links']:
        dv = (np.array(G['nodes'][w], float) - np.array(G['nodes'][u], float)) / 4
        dv = (dv + G['L'] / 2) % G['L'] - G['L'] / 2
        assert abs(np.linalg.norm(dv) - np.sqrt(3) / 4) < 1e-12
        x1 = np.append(dv, 0.0)
        bv.append(bivec([np.zeros(4), x1, x1 + e[3], e[3].copy()]))
    print("\n  void network x time (beta_t = beta_s):")
    a_t, k = normalisation("void", bv, 4 * 2 ** 3 * 0.25)
    check(abs(a_t - 1 / (2 * np.sqrt(2))) < 1e-12, f"C6 void: a_t = a/(2 sqrt2) = {a_t:.10f} exactly")
    check(abs(k - 1 / np.sqrt(2)) < 1e-12, f"C6 void: k = 1/sqrt2 = {k:.10f} exactly, i.e. 1/e^2 = beta/sqrt2")
    print("      a/(2 sqrt2) is numerically the radius of the touching FCC spheres. No physical weight is")
    print("      attached to that; it is recorded so that nobody later 'discovers' it.")
    return a_t, k


def part_D(out):
    from scipy.special import i0, i1
    seed_rng, plaq_angles, sweep, run = _kernels()
    print()
    print("=" * 80)
    print("PART D — reference simulator checks (beta = 0.1 and beta = 20 ONLY)")
    print("=" * 80)
    rng = np.random.default_rng(12345)
    for name, A in (("void L=2 Lt=6", void_time(2, 6)), ("Z4 L=4", hypercubic(4))):
        print(f"\n{name}: N_l = {A['n_links']}, N_p = {len(A['pl'])}, N_v = {A['n_nodes']}")
        th = rng.uniform(0, 2 * np.pi, A['n_links'])
        lam = rng.uniform(0, 2 * np.pi, A['n_nodes'])
        th2 = th + lam[A['links'][:, 0]] - lam[A['links'][:, 1]]
        dev = np.max(np.abs(np.cos(plaq_angles(th, A['pl'], A['ps'])) - np.cos(plaq_angles(th2, A['pl'], A['ps']))))
        check(dev < 1e-10, f"D1 {name}: gauge invariance, max |change in cos theta_p| = {dev:.1e}")
        S = lambda t: np.sum(1 - np.cos(plaq_angles(t, A['pl'], A['ps'])))
        worst = 0.0
        for l in rng.choice(A['n_links'], 25, replace=False):
            new = th.copy(); new[l] = rng.uniform(0, 2 * np.pi)
            re = im = 0.0
            for m in range(A['ptr'][l], A['ptr'][l + 1]):
                p, jj = A['lp_p'][m], A['lp_j'][m]
                rest = sum(A['ps'][p, j] * th[A['pl'][p, j]] for j in range(A['pl'].shape[1]) if j != jj)
                re += np.cos(A['ps'][p, jj] * rest); im += np.sin(A['ps'][p, jj] * rest)
            R, phi = np.hypot(re, im), np.arctan2(im, re)
            worst = max(worst, abs((S(new) - S(th)) + R * (np.cos(new[l] + phi) - np.cos(th[l] + phi))))
        check(worst < 1e-9, f"D2 {name}: local staple dS equals global recompute (max diff {worst:.1e})")
        seed_rng(7919)
        th = np.random.default_rng(1).uniform(0, 2 * np.pi, A['n_links'])
        _, _, _, C = run(th, 0.1, 1000, 10000, A['pl'], A['ps'], A['ptr'], A['lp_p'], A['lp_j'], A['kind'])
        m, s = blocked(C)
        u = i1(0.1) / i0(0.1)
        check(abs(m - u) / u < 0.02, f"D3 {name}: beta=0.1 hot, <cos> = {m:.6f} +- {s:.6f} vs I1/I0 = {u:.6f} "
                                       f"({(m-u)/u*100:+.2f}%, {(m-u)/s:+.1f} sigma)")
        out[f"{name}|beta=0.1|<cos>"] = [m, s, u]
        seed_rng(7920)
        th = np.zeros(A['n_links'])
        E, Es, Et, _ = run(th, 20.0, 1000, 10000, A['pl'], A['ps'], A['ptr'], A['lp_p'], A['lp_j'], A['kind'])
        m, s = blocked(E)
        tgt = (A['n_links'] - (A['n_nodes'] - 1) - 4) / (2 * 20.0 * len(A['pl']))
        check(abs(m - tgt) / tgt < 0.02, f"D4 {name}: beta=20 cold, E = {m:.6f} +- {s:.6f} vs rank/(2 beta N_p) = "
                                           f"{tgt:.6f} ({(m-tgt)/tgt*100:+.2f}%)")
        out[f"{name}|beta=20|E"] = [m, s, tgt]
        if name.startswith("void"):
            ms, ss = blocked(Es); mt, st = blocked(Et)
            print(f"      beta = 20: rhombi E_s = {ms:.6f} +- {ss:.6f}; temporal squares E_t = {mt:.6f} +- {st:.6f}"
                  f"; E_t/E_s = {mt/ms:.4f}")
            out[f"{name}|beta=20|E_s,E_t"] = [ms, ss, mt, st]


def part_E(out):
    seed_rng, plaq_angles, sweep, run = _kernels()
    print()
    print("=" * 80)
    print("PART E — timing at beta = 20 (sweep cost is beta-independent to within the sampler's branch)")
    print("=" * 80)
    timing = {}
    for name, ctor in (("void L=2 Lt=6", lambda: void_time(2, 6)),
                       ("void L=4 Lt=12", lambda: void_time(4, 12)),
                       ("void L=6 Lt=18", lambda: void_time(6, 18)),
                       ("void L=8 Lt=24", lambda: void_time(8, 24)),
                       ("Z4 L=8", lambda: hypercubic(8)),
                       ("Z4 L=12", lambda: hypercubic(12))):
        t0 = time.time(); A = ctor(); tb = time.time() - t0
        th = np.zeros(A['n_links']); seed_rng(1)
        run(th, 20.0, 1, 1, A['pl'], A['ps'], A['ptr'], A['lp_p'], A['lp_j'], A['kind'])
        n = 20
        t0 = time.time()
        run(th, 20.0, 0, n, A['pl'], A['ps'], A['ptr'], A['lp_p'], A['lp_j'], A['kind'])
        dt = (time.time() - t0) / n
        timing[name] = dict(n_links=int(A['n_links']), n_loops=int(len(A['pl'])), sec_per_sweep=dt, build_s=tb)
        print(f"  {name:<16s} N_l = {A['n_links']:>7d}  N_p = {len(A['pl']):>7d}  build {tb:6.1f} s  "
              f"{dt*1e3:8.2f} ms/sweep")
    out['timing'] = timing


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-timing", action="store_true")
    args = ap.parse_args()
    out = {}
    part_A(); part_B()
    a_t, k = part_C()
    out['a_t'] = a_t; out['k'] = k
    part_D(out)
    if not args.no_timing:
        part_E(out)
    with open(os.path.join(os.getcwd(), "dlb_deskcheck_results.json"), "w") as f:   # cwd, never the repo dir
        json.dump(out, f, indent=1, default=float)
    print()
    print("=" * 80)
    print(f"ALL {len(OK)} ASSERTIONS PASSED")
    print("=" * 80)
