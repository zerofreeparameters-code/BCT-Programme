"""Gate DL-BETA -- K1 (card 4.3): the complex, built and checked in the run thread.
Written and run BEFORE dlb_deskcheck.py was opened.  Output: out/k1_own.txt (+ k1_own.json).
Usage: python3 -I dlb_k1.py OUTDIR
"""
import sys, os, json, time, math
from itertools import product
import numpy as np
import numba as nb

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dlb_complex import VoidSpace, VoidST, Z4, OFFSETS, boundary2_dense

OUT = sys.argv[1]
lines, rec, fails = [], {}, []


def say(s=""):
    print(s, flush=True)
    lines.append(s)


def check(name, cond, detail=""):
    tag = "ok  " if cond else "FAIL"
    say(f"  {tag} {name}" + (f"  [{detail}]" if detail else ""))
    if not cond:
        fails.append(name)


P = 2147483629  # prime < 2^31


@nb.njit(cache=True)
def rank_mod_p(A, p):
    A = A.copy()
    m, n = A.shape
    r = 0
    for c in range(n):
        piv = -1
        for i in range(r, m):
            if A[i, c] % p != 0:
                piv = i
                break
        if piv < 0:
            continue
        for j in range(n):
            tmp = A[r, j]; A[r, j] = A[piv, j]; A[piv, j] = tmp
        # inverse of pivot by Fermat
        a = A[r, c] % p
        inv, e, base = 1, p - 2, a
        while e > 0:
            if e & 1:
                inv = (inv * base) % p
            base = (base * base) % p
            e >>= 1
        for j in range(n):
            A[r, j] = (A[r, j] % p) * inv % p
        for i in range(r + 1, m):
            f = A[i, c] % p
            if f != 0:
                for j in range(c, n):
                    A[i, j] = (A[i, j] - f * A[r, j]) % p
        r += 1
        if r == m:
            break
    return r


def ranks(D, label):
    """exact rank mod p (lower bound of rank over Q) and SVD rank with its gap."""
    Di = np.rint(D).astype(np.int64) % P
    rp = rank_mod_p(Di, P)
    s = np.linalg.svd(D, compute_uv=False)
    tol = s.max() * max(D.shape) * np.finfo(float).eps
    rs = int((s > tol).sum())
    gap = (s[rs - 1], s[rs] if rs < len(s) else 0.0)
    say(f"      rank {label}: mod-p {rp}, SVD {rs} (smallest kept s.v. {gap[0]:.3e}, largest dropped {gap[1]:.1e})")
    return rp, rs


def boundary1_dense(n_nodes, org, tgt):
    D1 = np.zeros((n_nodes, len(org)))
    D1[org, np.arange(len(org))] -= 1
    D1[tgt, np.arange(len(org))] += 1
    return D1


def cycles_3_4(n_nodes, org, tgt):
    adj = [dict() for _ in range(n_nodes)]
    multi = 0
    for e, (u, w) in enumerate(zip(org.tolist(), tgt.tolist())):
        if w in adj[u]:
            multi += 1
        adj[u].setdefault(w, []).append(e)
        adj[w].setdefault(u, []).append(e)
    tri = 0
    for u in range(n_nodes):
        for w in adj[u]:
            if w > u:
                tri += len((set(adj[u]) & set(adj[w])) - {u, w})
    tri //= 3
    cyc = set()
    for u in range(n_nodes):
        nbr = list(adj[u])
        for i in range(len(nbr)):
            for j in range(i + 1, len(nbr)):
                a, b = nbr[i], nbr[j]
                for w in (set(adj[a]) & set(adj[b])) - {u}:
                    cyc.add(frozenset((adj[u][a][0], adj[a][w][0], adj[w][b][0], adj[b][u][0])))
    return multi, tri, cyc


def newell(V):
    """V: (..., 4, 3) polygon vertices -> vector area (normal * area)."""
    n = np.zeros(V.shape[:-2] + (3,))
    for k in range(4):
        n += np.cross(V[..., k, :], V[..., (k + 1) % 4, :])
    return 0.5 * n


def sigma4(V):
    """V: (n, 4, 4) 4D polygon vertices -> (n, 6) oriented projected areas on (01,02,03,12,13,23)."""
    pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    S = np.zeros((V.shape[0], 6))
    for A, (m, v) in enumerate(pairs):
        for k in range(4):
            x, y = V[:, k], V[:, (k + 1) % 4]
            S[:, A] += 0.5 * (x[:, m] * y[:, v] - x[:, v] * y[:, m])
    return S


def cE_cB(Q):
    off = np.abs(Q - np.diag(np.diag(Q))).max()
    cE, cB = np.diag(Q)[:3], np.diag(Q)[3:]
    return off, cE, cB


t0 = time.time()
say("Gate DL-BETA -- K1, run thread's own complex (dlb_complex.py), before reading dlb_deskcheck.py")
say(f"numpy {np.__version__}, numba {nb.__version__}, python {sys.version.split()[0]}")
say("=" * 96)
say("PART 1 -- spatial void complex")
say("=" * 96)
for L in (2, 3):
    sp = VoidSpace(L)
    N = sp.N
    say(f"\nL = {L}: N = {N} primitive cells (atoms); V = {sp.nv}, E = {sp.ne}, rhombi F = {sp.nr}, 3-cells C3 = {N}")
    r = {}
    check(f"L={L}: per cell V = 3, E = 8, F = 6, C3 = 1", (sp.nv, sp.ne, sp.nr) == (3 * N, 8 * N, 6 * N))
    deg = np.bincount(np.concatenate([sp.link_org, sp.link_tgt]), minlength=sp.nv)
    check(f"L={L}: degree oct 8, tet 4 (every node)", (deg[:N] == 8).all() and (deg[N:] == 4).all())
    check(f"L={L}: every link oct -> tet (bipartite)", (sp.link_org < N).all() and (sp.link_tgt >= N).all())
    multi, tri, cyc = cycles_3_4(sp.nv, sp.link_org, sp.link_tgt)
    check(f"L={L}: no multiple links", multi == 0)
    check(f"L={L}: no 3-cycles", tri == 0, f"{tri}")
    rh = set(frozenset(x) for x in sp.rhomb_links.tolist())
    check(f"L={L}: no duplicate rhombi", len(rh) == sp.nr)
    check(f"L={L}: the 4-cycles of the void graph are exactly the rhombi", cyc == rh,
          f"4-cycles {len(cyc)}, rhombi {len(rh)}")
    inc = np.bincount(sp.rhomb_links.ravel(), minlength=sp.ne)
    check(f"L={L}: every link in exactly 3 rhombi", (inc == 3).all())
    V = sp.rhomb_verts / 4.0                         # units of a
    vol = np.einsum('ij,ij->i', V[:, 1] - V[:, 0], np.cross(V[:, 2] - V[:, 0], V[:, 3] - V[:, 0]))
    check(f"L={L}: every rhombus planar", np.abs(vol).max() < 1e-12, f"max |triple product| {np.abs(vol).max():.1e}")
    nvec = newell(V)
    area = np.linalg.norm(nvec, axis=1)
    check(f"L={L}: rhombus area = a^2/(4 sqrt2) = {1/(4*math.sqrt(2)):.10f}",
          np.abs(area - 1 / (4 * math.sqrt(2))).max() < 1e-12)
    from dlb_complex import BONDS
    bvec = BONDS[sp.rhomb_bond].astype(float)
    cosang = np.abs(np.einsum('ij,ij->i', nvec, bvec)) / (area * np.linalg.norm(bvec, axis=1))
    check(f"L={L}: rhombus normal along its FCC bond <110>", np.abs(cosang - 1).max() < 1e-12)
    # sides: every rhombus side is a window link of length sqrt3/4 a
    side = np.linalg.norm(V - np.roll(V, -1, axis=1), axis=2)
    check(f"L={L}: rhombus sides = sqrt3/4 a (window links)", np.abs(side - math.sqrt(3) / 4).max() < 1e-12)
    # boundary maps
    D1 = boundary1_dense(sp.nv, sp.link_org, sp.link_tgt)               # nodes x links
    D2 = boundary2_dense(sp.ne, sp.rhomb_links, sp.rhomb_signs)        # rhombi x links
    check(f"L={L}: d1 d2 = 0", np.abs(D1 @ D2.T).max() == 0)
    # d3: cells (atoms) x faces, sign = outward orientation of the face for that cell
    M = sp.M
    alook = -np.ones((M, M, M), dtype=np.int64)
    alook[tuple(sp.atoms.T)] = np.arange(N)
    A = sp.rhomb_atom
    B = alook[tuple(((sp.atoms[A] + bvec.astype(np.int64)) % M).T)]
    sgn = np.sign(np.einsum('ij,ij->i', nvec, bvec))
    D3 = np.zeros((N, sp.nr))
    np.add.at(D3, (A, np.arange(sp.nr)), sgn)
    np.add.at(D3, (B, np.arange(sp.nr)), -sgn)
    check(f"L={L}: every rhombus bounds exactly 2 cells, each cell has 12 faces",
          (np.abs(D3).sum(0) == 2).all() and (np.abs(D3).sum(1) == 12).all())
    check(f"L={L}: d2 d3 = 0 (closed cells, consistent orientation)", np.abs(D2.T @ D3.T).max() == 0)
    r1 = ranks(D1, "d1")
    r2 = ranks(D2, "d2")
    r3 = ranks(D3, "d3")
    check(f"L={L}: exact and SVD ranks agree", r1[0] == r1[1] and r2[0] == r2[1] and r3[0] == r3[1])
    rk1, rk2, rk3 = r1[0], r2[0], r3[0]
    check(f"L={L}: rank d2 = 5N - 2 = {5*N-2}", rk2 == 5 * N - 2, f"{rk2}")
    b = (sp.nv - rk1, sp.ne - rk1 - rk2, sp.nr - rk2 - rk3, N - rk3)
    check(f"L={L}: Betti numbers (1,3,3,1) = those of T^3", b == (1, 3, 3, 1), f"{b}")
    chi = sp.nv - sp.ne + sp.nr - N
    check(f"L={L}: Euler characteristic V - E + F - C3 = 0", chi == 0, f"{chi}")
    rec[f"space_L{L}"] = dict(N=N, V=sp.nv, E=sp.ne, F=sp.nr, C3=N, four_cycles=len(cyc), rank_d2=rk2,
                             betti=b, chi=chi)

say("")
say("=" * 96)
say("PART 2 -- void network x time, L = 2, L_t = 6")
say("=" * 96)
st = VoidST(2, 6)
N, Lt = st.N, st.Lt
say(f"N = {N}, L_t = {Lt}: N_v = {st.n_nodes}, N_l = {st.n_links}, N_loops = {st.n_loops}")
check("per cell per slice N_v = 3, N_l = 11, N_loops = 14",
      (st.n_nodes, st.n_links, st.n_loops) == (3 * N * Lt, 11 * N * Lt, 14 * N * Lt))
inc = np.bincount(st.loop_links.ravel(), minlength=st.n_links)
isp = np.zeros(st.n_links, bool)
for tt in range(Lt):
    isp[tt * st.blk: tt * st.blk + 8 * N] = True
kind_t = (st.link_cls - 8)
check("every spatial link in 5 loops (3 rhombi + 2 temporal squares)", (inc[isp] == 5).all())
check("temporal links in 8 (oct) or 4 (tet) squares",
      (inc[~isp & (kind_t == 0)] == 8).all() and (inc[~isp & (kind_t > 0)] == 4).all())
inc_r = np.bincount(st.loop_links[st.loop_type == 0].ravel(), minlength=st.n_links)
check("spatial link: exactly 3 rhombi and 2 squares", (inc_r[isp] == 3).all() and ((inc - inc_r)[isp] == 2).all())
mlp = 4 * st.n_loops / st.n_links
check("mean loops per link = 56/11", abs(mlp - 56 / 11) < 1e-12, f"{mlp:.6f}")
check("no loop repeats a link", all(len(set(r)) == 4 for r in st.loop_links.tolist()))
multi, tri, cyc = cycles_3_4(st.n_nodes, st.link_org, st.link_tgt)
loopset = set(frozenset(x) for x in st.loop_links.tolist())
check("space x time graph: no multiple links, no 3-cycles", multi == 0 and tri == 0, f"multi {multi}, tri {tri}")
check("space x time: the 4-cycles are exactly the rhombi and the temporal squares", cyc == loopset,
      f"4-cycles {len(cyc)}, loops {len(loopset)}")
D1 = boundary1_dense(st.n_nodes, st.link_org, st.link_tgt)
D2 = boundary2_dense(st.n_links, st.loop_links, st.loop_signs)
check("d1 d2 = 0 (every loop closed and consistently oriented)", np.abs(D1 @ D2.T).max() == 0)
r2 = ranks(D2, "d2 (space x time)")
check("exact and SVD ranks agree", r2[0] == r2[1])
rk_st = r2[0]
check(f"rank d2 = N_l - N_v - 3 = {st.n_links - st.n_nodes - 3}", rk_st == st.n_links - st.n_nodes - 3, f"{rk_st}")
cnt = np.bincount(st.link_cls, minlength=11)
check("11 link classes per cell per slice, equally populated", (cnt == N * Lt).all(), f"{cnt.tolist()}")
Pm = np.zeros((st.n_links, 11))
Pm[np.arange(st.n_links), st.link_cls] = 1
D20 = D2 @ Pm
r0 = ranks(D20, "d2 at zero crystal momentum (11 link classes)")
check("rank at zero crystal momentum = 5", r0[0] == 5 and r0[1] == 5)
# extra: generic allowed momentum on this torus -> rank 8 = 11 - 3 gauge
sp = st.sp
Rl = np.zeros((st.n_links, 3)); tl = st.link_slice.astype(float)
for tt in range(Lt):
    b = tt * st.blk
    Rl[b:b + 8 * N] = sp.pos[sp.link_org]
    Rl[b + 8 * N:b + st.blk] = sp.pos
for kvec in ([1, 0, 0, 1], [1, 2, 3, 1], [0, 1, 1, 2]):
    k = 2 * np.pi * np.array(kvec[:3]) / sp.M
    w = 2 * np.pi * kvec[3] / Lt
    Bk = np.zeros((st.n_links, 11), complex)
    Bk[np.arange(st.n_links), st.link_cls] = np.exp(1j * (Rl @ k + w * tl))
    s = np.linalg.svd(D2 @ Bk, compute_uv=False)
    rk = int((s > s.max() * 1e-10).sum())
    say(f"      rank d2 at crystal momentum (k M/2pi, w Lt/2pi) = {kvec}: {rk}   (singular values {np.array2string(s, precision=3)})")
    check(f"rank 8 = 11 - 3 gauge at k = {kvec} (extra)", rk == 8)
r_targ = rk_st / (2 * 20 * st.n_loops)
say(f"      weak-coupling target at beta = 20: rank/(2 beta N_loops) = {rk_st}/(40*{st.n_loops}) = {r_targ:.6f}")
rec["st_L2_Lt6"] = dict(N_v=st.n_nodes, N_l=st.n_links, N_loops=st.n_loops, rank_d2=rk_st,
                        rank_k0=r0[0], four_cycles=len(cyc), mean_loops_per_link=mlp, E20_target=r_targ)

say("")
say("=" * 96)
say("PART 3 -- classical continuum normalisation (constant F), 1/e^2 = k beta, beta_t = beta_s")
say("=" * 96)
say("theta_p = sum_{mu<nu} sigma_p^{mu nu} F_{mu nu};  (beta/2) sum_p theta_p^2 / V4 = (beta/2) F^T Q F,")
say("Q = sum_p sigma_p sigma_p^T / V4.  At a_t = 1: Q = diag(c_E x3, c_B x3) required; c_E ~ a_t, c_B ~ 1/a_t,")
say("so light speed 1 needs a_t = sqrt(c_B/c_E), and then 1/e^2 = beta c_E(a_t) = beta sqrt(c_E c_B), k = sqrt(c_E c_B).")


def normalisation(cx, label, a_t=1.0):
    S = sigma4(cx.loop_vertices_4d(a_t))
    Q = S.T @ S / cx.volume4(a_t)
    off, cE, cB = cE_cB(Q)
    return off, cE, cB, Q


z = Z4(4)
off, cE, cB, _ = normalisation(z, "Z4")
check("Z4: Q diagonal", off < 1e-12, f"max off-diag {off:.1e}")
check("Z4: spatially isotropic", np.ptp(cE) < 1e-12 and np.ptp(cB) < 1e-12)
at_z, k_z = math.sqrt(cB[0] / cE[0]), math.sqrt(cE[0] * cB[0])
say(f"      Z4: c_E(a_t=1) = {cE[0]:.10f}, c_B(a_t=1) = {cB[0]:.10f} -> a_t = {at_z:.10f}, k = {k_z:.10f}")
check("Z4: k = 1 (method validation)", abs(k_z - 1) < 1e-12)

# D4 (extra method validation): 32 triangle classes per site, 1 site per 2 units of 4-volume
nbv = [np.array(v) for v in set(tuple(s * np.eye(4, dtype=int)[i] + t * np.eye(4, dtype=int)[j])
                                for i in range(4) for j in range(i + 1, 4) for s in (1, -1) for t in (1, -1))]
nbs = set(tuple(v) for v in nbv)
tris = set()
for r1 in nbv:
    for r2 in nbv:
        if tuple(r1 + r2) in nbs:
            vs = sorted([(0, 0, 0, 0), tuple(r1), tuple(r1 + r2)])
            base = np.array(vs[0])
            tris.add(tuple(tuple(np.array(v) - base) for v in vs))
TV = np.zeros((len(tris), 4, 4))
for i, tr in enumerate(sorted(tris)):
    TV[i, 0], TV[i, 1], TV[i, 2], TV[i, 3] = tr[0], tr[1], tr[2], tr[0]   # triangle as degenerate 4-gon
SD = sigma4(TV)
QD = SD.T @ SD / 2.0
offD, cED, cBD = cE_cB(QD)
check("D4: 32 triangle classes per site (extra)", len(tris) == 32, f"{len(tris)}")
check("D4: Q diagonal and isotropic (extra)", offD < 1e-12 and np.ptp(cED) < 1e-12 and np.ptp(cBD) < 1e-12)
k_d4 = math.sqrt(cED[0] * cBD[0])
say(f"      D4: c_E(a_t=1) = {cED[0]:.10f}, c_B(a_t=1) = {cBD[0]:.10f} -> a_t = {math.sqrt(cBD[0]/cED[0]):.10f}, k = {k_d4:.10f}")
check("D4: k = 2 (extra method validation)", abs(k_d4 - 2) < 1e-12)

off, cE, cB, _ = normalisation(st, "void")
check("void: Q diagonal", off < 1e-12, f"max off-diag {off:.1e}")
check("void: spatially isotropic", np.ptp(cE) < 1e-12 and np.ptp(cB) < 1e-12)
at_v, k_v = math.sqrt(cB[0] / cE[0]), math.sqrt(cE[0] * cB[0])
say(f"      void: c_E(a_t=1) = {cE[0]:.10f}, c_B(a_t=1) = {cB[0]:.10f} -> a_t = {at_v:.10f}, k = {k_v:.10f}")
check("void: a_t = a/(2 sqrt2)", abs(at_v - 1 / (2 * math.sqrt(2))) < 1e-12)
check("void: k = 1/sqrt2", abs(k_v - 1 / math.sqrt(2)) < 1e-12)
off2, cE2, cB2, Q2 = normalisation(st, "void", a_t=1 / (2 * math.sqrt(2)))
say(f"      direct recompute at a_t = a/(2 sqrt2): Q = {np.array2string(np.diag(Q2), precision=10)} (off-diag {off2:.1e})")
check("void: at a_t = a/(2 sqrt2), Q = (1/sqrt2) * identity (Euclidean invariant)",
      off2 < 1e-12 and np.abs(np.diag(Q2) - 1 / math.sqrt(2)).max() < 1e-12)

# Z4 weak-coupling target for K3
D2z = boundary2_dense(z.n_links, z.loop_links, z.loop_signs)
rz = ranks(D2z, "d2 Z4 L=4")
check("Z4 L=4: rank d2 = N_l - N_v - 3", rz[0] == rz[1] == z.n_links - z.n_nodes - 3, f"{rz[0]}")
say(f"      Z4 L=4 weak-coupling target at beta = 20: {rz[0]}/(40*{z.n_loops}) = {rz[0]/(40*z.n_loops):.6f}")
rec["normalisation"] = dict(Z4_k=k_z, D4_k=k_d4, void_cE=cE[0], void_cB=cB[0], void_a_t=at_v, void_k=k_v)
rec["Z4_L4"] = dict(rank_d2=rz[0], E20_target=rz[0] / (40 * z.n_loops))

say("")
say("=" * 96)
say(f"{'ALL K1 CHECKS PASSED' if not fails else 'FAILED: ' + '; '.join(fails)}   ({time.time()-t0:.1f} s)")
say("=" * 96)
with open(os.path.join(OUT, "k1_own.txt"), "w") as f:
    f.write("\n".join(lines) + "\n")
with open(os.path.join(OUT, "k1_own.json"), "w") as f:
    json.dump(dict(rec=rec, fails=fails), f, indent=1, default=lambda o: o if not hasattr(o, 'tolist') else o.tolist())
sys.exit(1 if fails else 0)
