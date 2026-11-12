"""
Gate DL-BETA REP1 -- K1 (the complex), from the run's own construction in dlbr_sim.py.
Run BEFORE dlb_deskcheck.py is opened (card REP1 section 4.3 / original section 4.3).
Usage: python -I dlbr_k1.py OUTDIR
"""
import sys, os, json, itertools
import numpy as np
from numba import njit

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dlbr_sim as S

OUT = []
NUM = {}
FAILS = []


def say(s=""):
    print(s)
    OUT.append(s)


def check(cond, msg):
    say(("  ok    " if cond else "  FAIL  ") + msg)
    if not cond:
        FAILS.append(msg)


@njit(cache=True)
def rank_mod_p(A, p):
    A = A.copy() % p
    nr, nc = A.shape
    r = 0
    for c in range(nc):
        piv = -1
        for i in range(r, nr):
            if A[i, c] != 0:
                piv = i
                break
        if piv < 0:
            continue
        if piv != r:
            for j in range(nc):
                tmp = A[r, j]; A[r, j] = A[piv, j]; A[piv, j] = tmp
        # inverse of pivot mod p (Fermat)
        a = A[r, c]; e = p - 2; inv = 1
        while e > 0:
            if e & 1:
                inv = (inv * a) % p
            a = (a * a) % p
            e >>= 1
        for j in range(nc):
            A[r, j] = (A[r, j] * inv) % p
        for i in range(nr):
            if i != r and A[i, c] != 0:
                f = A[i, c]
                for j in range(c, nc):
                    A[i, j] = (A[i, j] - f * A[r, j]) % p
        r += 1
        if r == nr:
            break
    return r


def boundary_matrix(loops, signs, Nl):
    M = np.zeros((loops.shape[0], Nl), dtype=np.int64)
    for k in range(4):
        np.add.at(M, (np.arange(loops.shape[0]), loops[:, k]), signs[:, k])
    return M


def ranks(M):
    sv = np.linalg.svd(M.astype(float), compute_uv=False)
    tol = sv.max() * max(M.shape) * np.finfo(float).eps
    r_svd = int(np.sum(sv > tol))
    gap = (float(sv[r_svd - 1]), float(sv[r_svd]) if r_svd < len(sv) else 0.0)
    r_p = rank_mod_p(M.astype(np.int64), 1000003)
    return r_svd, r_p, gap


def four_cycles(adj_edges, nnodes):
    """adj_edges: list of (u, v, edge_id). Return set of frozensets of edge ids of all 4-cycles, and #3-cycles."""
    nbr = [dict() for _ in range(nnodes)]
    for (u, v, e) in adj_edges:
        assert v not in nbr[u], "multi-edge"
        nbr[u][v] = e
        nbr[v][u] = e
    cyc = set()
    tri = 0
    for a in range(nnodes):
        na = list(nbr[a].keys())
        for b, d in itertools.combinations(na, 2):
            if d in nbr[b]:
                tri += 1
            common = set(nbr[b].keys()) & set(nbr[d].keys())
            for c in common:
                if c == a:
                    continue
                cyc.add(frozenset((nbr[a][b], nbr[b][c], nbr[c][d], nbr[d][a])))
    return cyc, tri // 3


def min_image(d, S_):
    return (d + S_ // 2) % S_ - S_ // 2


def part_A(L):
    sp = S.build_void_space(L)
    N, V, E, R = sp["N"], sp["V"], sp["E"], sp["R"]
    say(f"L = {L}: N = {N} primitive cells (atoms); V = {V}, E = {E}, rhombi = {R}")
    nt = sp["node_type"]
    # 3-cells = rhombic dodecahedra, one per atom: built and closed below
    deg = np.bincount(sp["link_ends"].ravel(), minlength=V)
    check(V == 3 * N and E == 8 * N and R == 6 * N, f"A{L}: per primitive cell V = {V/N:g}, E = {E/N:g}, rhombi = {R/N:g}")
    check(np.all(deg[nt == 0] == 8) and np.all(deg[nt > 0] == 4), f"A{L}: degree oct {set(deg[nt==0])}, tet {set(deg[nt>0])}")
    check(np.all(nt[sp["link_ends"][:, 0]] == 0) and np.all(nt[sp["link_ends"][:, 1]] > 0), f"A{L}: every link oct -> tet (bipartite)")
    # rhombus geometry
    vs = sp["rh_verts"] / 4.0  # units of a
    closed = True
    for r in range(R):
        # walk the links: O1->T1 (+), T1->O2 (link O2->T1, -), O2->T2 (+), T2->O1 (link O1->T2, -)
        l = sp["rh_links"][r]
        e = sp["link_ends"]
        ok = (e[l[0], 0] == e[l[3], 0]) and (e[l[0], 1] == e[l[1], 1]) and (e[l[1], 0] == e[l[2], 0]) and (e[l[2], 1] == e[l[3], 1])
        # unwrapped vertex steps equal the link vectors
        st = [vs[r, 1] - vs[r, 0], vs[r, 2] - vs[r, 1], vs[r, 3] - vs[r, 2], vs[r, 0] - vs[r, 3]]
        lv = sp["link_vec"] / 4.0
        ok = ok and np.allclose(st[0], lv[l[0]]) and np.allclose(st[1], -lv[l[1]]) and np.allclose(st[2], lv[l[2]]) and np.allclose(st[3], -lv[l[3]])
        closed = closed and ok
    check(closed, f"A{L}: every rhombus is a closed O-T-O-T 4-cycle of existing links (unwrapped steps = link vectors)")
    d1 = vs[:, 1] - vs[:, 0]; d2 = vs[:, 2] - vs[:, 0]; d3 = vs[:, 3] - vs[:, 0]
    vol = np.einsum("ij,ij->i", d1, np.cross(d2, d3))
    check(np.max(np.abs(vol)) < 1e-12, f"A{L}: every rhombus planar (max |triple product| {np.max(np.abs(vol)):.1e})")
    area_vec = 0.5 * np.cross(vs[:, 2] - vs[:, 0], vs[:, 3] - vs[:, 1])
    area = np.linalg.norm(area_vec, axis=1)
    check(np.allclose(area, 1 / (4 * np.sqrt(2)), atol=1e-13), f"A{L}: rhombus area = a^2/(4 sqrt2) = {1/(4*np.sqrt(2)):.10f} (found {area.min():.10f}..{area.max():.10f})")
    bv = np.array(S.BVECS, dtype=float)[sp["rh_b"]]
    cr = np.linalg.norm(np.cross(area_vec, bv), axis=1)
    check(np.max(cr) < 1e-12, f"A{L}: rhombus normal along its FCC bond <110>")
    keys = [frozenset(x) for x in sp["rh_links"].tolist()]
    check(len(set(keys)) == R, f"A{L}: no duplicate rhombi")
    edges = [(int(sp["link_ends"][j, 0]), int(sp["link_ends"][j, 1]), j) for j in range(E)]
    cyc, tri = four_cycles(edges, V)
    check(tri == 0, f"A{L}: no 3-cycles")
    check(cyc == set(keys), f"A{L}: the 4-cycles of the void graph are exactly the rhombi ({len(cyc)} 4-cycles, {R} rhombi)")
    per_link = np.bincount(sp["rh_links"].ravel(), minlength=E)
    check(np.all(per_link == 3), f"A{L}: every link lies in exactly 3 rhombi")
    M = boundary_matrix(sp["rh_links"], sp["rh_signs"], E)
    r_svd, r_p, gap = ranks(M)
    check(r_svd == r_p == 5 * N - 2 == E - V - 2, f"A{L}: rank d2 = {r_svd} (SVD; mod-p {r_p}) = 5N - 2 = {5*N-2} = E - V - 2   [sv gap {gap[0]:.3e} | {gap[1]:.1e}]")
    # 3-cells: rhombic dodecahedron of each atom = rhombi of its 12 bonds; closed surface
    Sbox = sp["S"]
    pos2atom = {tuple(int(c) for c in sp["atoms"][a]): a for a in range(N)}
    rh_index = {(int(sp["rh_atom"][r]), int(sp["rh_b"][r])): r for r in range(R)}
    cell_ok = True
    faces_per_rh = np.zeros(R, dtype=int)
    for a in range(N):
        A = sp["atoms"][a]
        chain = np.zeros(E, dtype=int)
        nf = 0
        for bi, b in enumerate(S.BVECS):
            for sgn in (1, -1):
                if sgn == 1:
                    r = rh_index[(a, bi)]
                else:
                    a2 = pos2atom[tuple(int(c) for c in ((A - np.array(b)) % Sbox))]
                    r = rh_index[(a2, bi)]
                faces_per_rh[r] += 1
                nf += 1
                centre = sp["rh_verts"][r].mean(axis=0) + 0.0
                # centre relative to A, minimum image (units a/4)
                rel = (centre - A + Sbox / 2.0) % Sbox - Sbox / 2.0
                o = np.sign(np.dot(area_vec[r], rel))
                if o == 0:
                    cell_ok = False
                for k in range(4):
                    chain[sp["rh_links"][r, k]] += int(o) * sp["rh_signs"][r, k]
        cell_ok = cell_ok and nf == 12 and not np.any(chain)
    cell_ok = cell_ok and np.all(faces_per_rh == 2)
    C3 = N
    check(cell_ok, f"A{L}: 3-cells = {C3} = N rhombic dodecahedra (12 rhombi each, outward-oriented boundary closes; each rhombus on exactly 2 cells)")
    chi = V - E + R - C3
    check(chi == 0, f"A{L}: Euler characteristic V - E + F - C3 = {chi}")
    NUM[f"A_L{L}"] = dict(N=N, V=V, E=E, rhombi=R, cells3=C3, four_cycles=len(cyc), rank_d2=r_svd, chi=chi)
    say()
    return sp


def bivectors_void(L, Lt, sp):
    """Oriented area bivectors (a_t = 1; space in units of a) of every loop of the void x time complex."""
    loops, signs, ltype, Nl, meta, _ = S.build_void_spacetime(L, Lt, sp)
    R, E = sp["R"], sp["E"]
    pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]   # index 0 = time
    sig = np.zeros((meta["Np"], 6))
    vs3 = sp["rh_verts"] / 4.0
    lv = sp["link_vec"] / 4.0
    up = sp["node_pos"][sp["link_ends"][:, 0]] / 4.0
    for t in range(Lt):
        base = t * (R + E)
        X = np.zeros((R, 4, 4)); X[:, :, 0] = t; X[:, :, 1:] = vs3
        Y = np.zeros((E, 4, 4))
        Y[:, 0, 0] = t; Y[:, 0, 1:] = up
        Y[:, 1, 0] = t; Y[:, 1, 1:] = up + lv
        Y[:, 2, 0] = t + 1; Y[:, 2, 1:] = up + lv
        Y[:, 3, 0] = t + 1; Y[:, 3, 1:] = up
        for blk, P in ((slice(base, base + R), X), (slice(base + R, base + R + E), Y)):
            for pi, (m, n) in enumerate(pairs):
                s = 0.0
                for i in range(4):
                    j = (i + 1) % 4
                    s = s + P[:, i, m] * P[:, j, n] - P[:, i, n] * P[:, j, m]
                sig[blk, pi] = 0.5 * s
    vol = (L ** 3) * Lt   # 4-volume at a = 1, a_t = 1
    return sig, vol


def bivectors_z4(L):
    loops, signs, ltype, Nl, meta, x = S.build_z4(L)
    pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    sig = np.zeros((meta["Np"], 6))
    Ns = L ** 4
    for pi, (mu, nu) in enumerate(pairs):
        sig[pi::6, pi] = 1.0
    return sig, float(Ns)


def cE_cB(sig, vol, label):
    Q = sig.T @ sig / vol
    off = Q - np.diag(np.diag(Q))
    d = np.diag(Q)
    cE = d[:3]; cB = d[3:]
    check(np.max(np.abs(off)) < 1e-12, f"C {label}: flux quadratic form diagonal (max off-diagonal {np.max(np.abs(off)):.1e})")
    check(np.allclose(cE, cE[0]) and np.allclose(cB, cB[0]), f"C {label}: spatially isotropic (3 equal c_E, 3 equal c_B)")
    cEv, cBv = cE[0], cB[0]
    a_t = np.sqrt(cBv / cEv)
    k = np.sqrt(cEv * cBv)
    say(f"      {label}: c_E(a_t=1) = {cEv:.10f}, c_B(a_t=1) = {cBv:.10f}  ->  a_t = {a_t:.10f}, k = {k:.10f}")
    return cEv, cBv, a_t, k


def part_B(L, Lt, sp):
    loops, signs, ltype, Nl, meta, _ = S.build_void_spacetime(L, Lt, sp)
    N, V, E, R, B = sp["N"], sp["V"], sp["E"], sp["R"], meta["B"]
    Nv, Np = meta["Nv"], meta["Np"]
    say(f"L = {L}, L_t = {Lt}: N_v = {Nv}, N_l = {Nl}, N_loops = {Np}")
    check(Nv == 3 * N * Lt and Nl == 11 * N * Lt and Np == 14 * N * Lt, f"B: per cell per slice N_v = {Nv/(N*Lt):g}, N_l = {Nl/(N*Lt):g}, N_loops = {Np/(N*Lt):g}")
    inc = np.bincount(loops.ravel(), minlength=Nl)
    idx = np.arange(Nl)
    is_sp = (idx % B) < E
    rh_inc = np.bincount(loops[ltype == 0].ravel(), minlength=Nl)
    sq_inc = np.bincount(loops[ltype == 1].ravel(), minlength=Nl)
    check(np.all(inc[is_sp] == 5) and np.all(rh_inc[is_sp] == 3) and np.all(sq_inc[is_sp] == 2), "B: every spatial link in 5 loops (3 rhombi + 2 temporal squares)")
    vtx = (idx % B) - E
    tt = np.where(~is_sp)[0]
    typ = sp["node_type"][vtx[tt]]
    check(np.all(inc[tt][typ == 0] == 8) and np.all(inc[tt][typ > 0] == 4), f"B: temporal links in {set(inc[tt][typ==0])} (oct) / {set(inc[tt][typ>0])} (tet) squares")
    M = boundary_matrix(loops, signs, Nl)
    r_svd, r_p, gap = ranks(M)
    check(r_svd == r_p == Nl - Nv - 3, f"B: rank d2 = {r_svd} (SVD; mod-p {r_p}) = N_l - N_v - 3 = {Nl-Nv-3}   [sv gap {gap[0]:.3e} | {gap[1]:.1e}]")
    say(f"      mean loops per link = 4 N_loops / N_l = {4*Np/Nl:.6f} (56/11 = {56/11:.6f})")
    say(f"      weak-coupling target E -> rank/(2 beta N_loops) = {r_svd/(2*20*Np):.6f} at beta = 20")
    # space-time graph 4-cycles = the loops, nothing else
    def node(v, t):
        return t * V + v
    edges = []
    for t in range(Lt):
        for j in range(E):
            edges.append((node(sp["link_ends"][j, 0], t), node(sp["link_ends"][j, 1], t), t * B + j))
        for v in range(V):
            edges.append((node(v, t), node(v, (t + 1) % Lt), t * B + E + v))
    cyc, tri = four_cycles(edges, Nv)
    lkeys = set(frozenset(x) for x in loops.tolist())
    check(tri == 0 and cyc == lkeys, f"B: the 4-cycles of the space-time graph are exactly the rhombi + temporal squares ({len(cyc)} cycles, {Np} loops; 3-cycles {tri})")
    # link classes (11) and zero-momentum rank
    lcls = np.where(is_sp, (idx % B) % 8, 8 + sp["node_type"][np.clip(vtx, 0, V - 1)])
    lcls_counts = np.bincount(lcls, minlength=11)
    check(len(lcls_counts) == 11 and np.all(lcls_counts == N * Lt), f"B: 11 link classes per cell per slice, equally populated ({lcls_counts.tolist()})")
    pcls = np.zeros(Np, dtype=int)
    pidx = np.arange(Np) % (R + E)
    rh = pidx < R
    pcls[rh] = sp["rh_b"][pidx[rh]]
    pcls[~rh] = 6 + ((pidx[~rh] - R) % 8)
    rows = {}
    consistent = True
    for p in range(Np):
        row = np.zeros(11, dtype=int)
        for k in range(4):
            row[lcls[loops[p, k]]] += signs[p, k]
        key = pcls[p]
        if key in rows:
            consistent = consistent and np.array_equal(rows[key], row)
        else:
            rows[key] = row
    M0 = np.array([rows[c] for c in range(14)])
    r0 = np.linalg.matrix_rank(M0)
    check(consistent and r0 == 5, f"B: zero-momentum loop map (14 loop classes x 11 link classes) has rank {r0} = 5 per cell (rows class-consistent: {consistent})")
    NUM["B"] = dict(L=L, Lt=Lt, Nv=Nv, Nl=Nl, Np=Np, rank_d2=r_svd, four_cycles=len(cyc), rank_k0=int(r0),
                    loops_per_link=4 * Np / Nl, E_target_beta20=r_svd / (2 * 20 * Np))
    say()
    return loops, signs, ltype, Nl, meta


def main(outdir):
    say("=" * 96)
    say("Gate DL-BETA REP1 -- K1, the run's own construction (dlbr_sim.py); dlb_deskcheck.py NOT opened")
    say("=" * 96)
    say("PART A -- spatial void complex")
    sp2 = part_A(2)
    sp3 = part_A(3)
    say("PART B -- void network x time")
    part_B(2, 6, sp2)
    say("PART C -- constant-F normalisation (beta/2) sum theta^2 per 4-volume = (1/2e^2) sum F^2")
    sig, vol = bivectors_z4(4)
    cE, cB, at, k = cE_cB(sig, vol, "Z4")
    check(abs(k - 1) < 1e-12 and abs(at - 1) < 1e-12, "C Z4: k = 1, a_t = 1 (method validation)")
    NUM["C_Z4"] = dict(cE=cE, cB=cB, a_t=at, k=k)
    sig, vol = bivectors_void(2, 6, sp2)
    cE, cB, at, k = cE_cB(sig, vol, "void x time")
    check(abs(at - 1 / (2 * np.sqrt(2))) < 1e-12, f"C void: a_t = a/(2 sqrt2) = {1/(2*np.sqrt(2)):.10f}")
    check(abs(k - 1 / np.sqrt(2)) < 1e-12, f"C void: k = 1/sqrt2 = {1/np.sqrt(2):.10f}, i.e. 1/e^2 = beta/sqrt2")
    NUM["C_void"] = dict(cE=cE, cB=cB, a_t=at, k=k)
    say()
    say(f"K1 FAILS: {len(FAILS)}" + ("" if not FAILS else " -> " + "; ".join(FAILS)))
    NUM["fails"] = FAILS
    with open(os.path.join(outdir, "k1_own.txt"), "w") as f:
        f.write("\n".join(OUT) + "\n")
    with open(os.path.join(outdir, "k1_own.json"), "w") as f:
        json.dump(NUM, f, indent=1, default=float)


if __name__ == "__main__":
    main(sys.argv[1])
