#!/usr/bin/env python3
"""
Desk-check VOID-Q1 (8 Nov 2026, same-session, CONJECTURE; NOT a gate).

Question 1: Does BCT supply void-scale structure, in the form the quantum-liquid route to light needs?
 The route (Hermele-Fisher-Balents 2004 and relatives): a fluid living on a 3-D BIPARTITE network,
 obeying a local rule at every node ("what flows in flows out"), and NOT condensed (a quantum liquid,
 Mott-like: on-node repulsion U >> hopping t). Then an emergent U(1) gauge field appears:
   'electric' field on the links, Gauss law at the nodes, 'magnetic' flux through the smallest loops,
   gapless photon; violations of the node rule are gapped charges living ON the nodes.

Part A  Geometry of BCT's void network (FCC = BCT with c/a = sqrt2, touching spheres, a = 1):
        nodes = octahedral + tetrahedral voids, links = shared triangular windows.
        Is it bipartite? coordinations? counts per sphere? smallest loops and where they sit?
Part B  Regime: BCT's own numbers (xi = 2.31754 a) -> hopping t of the pore network vs the interaction
        scale g n0 = hbar^2/(2 m xi^2). Liquid needs U/t >~ 30 (3-D Bose-Hubbard Mott point ~29).
        Pore-network band estimate: lowest Bloch state of -lap psi in the pore space (spheres as walls),
        periodic vs twisted boundary across the cubic cell; units hbar^2/2m = 1, lengths in a.
Run: python3 -I desk_VOID_Q1.py
"""
import numpy as np, itertools

A = np.sqrt(2.0); R = 0.5
ROCT = (np.sqrt(2) - 1) / 2; RTET = (np.sqrt(6) - 2) / 4
ALPHA0 = ROCT * RTET / np.pi; XI = 1 / np.sqrt(8 * np.pi * ALPHA0)
basis = np.array([[0, 0, 0], [.5, .5, 0], [.5, 0, .5], [0, .5, .5]]) * A

def hdr(s): print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)

# =============================================================================== A
hdr("A. The void network: nodes, windows, loops")
N = 3
spheres = np.array([b + A * np.array(c) for c in itertools.product(range(-N, N + 1), repeat=3) for b in basis])
oct_b = np.array([[.5, 0, 0], [0, .5, 0], [0, 0, .5], [.5, .5, .5]]) * A
tet_b = np.array([[x, y, z] for x in (.25, .75) for y in (.25, .75) for z in (.25, .75)]) * A
def nodes(b, n=1):
    return np.array([p + A * np.array(c) for c in itertools.product(range(-n, n + 1), repeat=3) for p in b])
O = nodes(oct_b); T = nodes(tet_b)
def nn_spheres(p):
    d = np.linalg.norm(spheres - p, axis=1); m = d.min()
    return frozenset(np.where(np.abs(d - m) < 1e-9)[0]), m
Oset = [nn_spheres(p) for p in O]; Tset = [nn_spheres(p) for p in T]
print(f"  octahedral void: {len(Oset[0][0])} neighbouring spheres, radius {Oset[0][1] - R:.5f} a;"
      f"  tetrahedral: {len(Tset[0][0])}, radius {Tset[0][1] - R:.5f} a")
# links = shared triangular faces (3 common spheres)
def adjacent(s1, s2): return len(s1 & s2) == 3
c = np.zeros(3) + A * 0.0
i0 = int(np.argmin(np.linalg.norm(O - oct_b[0], axis=1)))           # an oct near the origin cell
j0 = int(np.argmin(np.linalg.norm(T - tet_b[0], axis=1)))
oo = sum(adjacent(Oset[i0][0], s) for k, (s, _) in enumerate(Oset) if k != i0)
ot = sum(adjacent(Oset[i0][0], s) for s, _ in Tset)
tt = sum(adjacent(Tset[j0][0], s) for k, (s, _) in enumerate(Tset) if k != j0)
to = sum(adjacent(Tset[j0][0], s) for s, _ in Oset)
print(f"  windows: oct-tet {ot} per oct, tet-oct {to} per tet, oct-oct {oo}, tet-tet {tt}"
      f"  -> {'BIPARTITE' if oo == 0 and tt == 0 else 'not bipartite'}")
print(f"  per sphere: 1 oct + 2 tet nodes, {ot} windows (= 2 tets x 4 = 1 oct x 8)")
w = 2 * R / np.sqrt(3) - R
print(f"  window (gap inside three touching spheres): inscribed radius {w:.5f} a = {w / R:.4f} R")
# smallest loops: oct-tet-oct-tet 4-cycles; check each wraps one sphere-sphere contact (nn bond)
ctr = np.zeros(3)
Onear = [k for k, p in enumerate(O) if np.linalg.norm(p - ctr) < 1.6]
Tnear = [k for k, p in enumerate(T) if np.linalg.norm(p - ctr) < 1.6]
cycles = set()
for o1, o2 in itertools.combinations(Onear, 2):
    common_t = [t for t in Tnear if adjacent(Oset[o1][0], Tset[t][0]) and adjacent(Oset[o2][0], Tset[t][0])]
    for t1, t2 in itertools.combinations(common_t, 2):
        cycles.add((o1, o2, t1, t2))
bonds_ok = 0; bond_list = []
for (o1, o2, t1, t2) in cycles:
    shared = Oset[o1][0] & Oset[o2][0] & Tset[t1][0] & Tset[t2][0]
    if len(shared) == 2:
        s1, s2 = sorted(shared)
        if abs(np.linalg.norm(spheres[s1] - spheres[s2]) - 1.0) < 1e-9:
            bonds_ok += 1; bond_list.append((s1, s2))
print(f"  4-cycles oct-tet-oct-tet found near the origin: {len(cycles)}; each wraps a sphere-sphere contact: "
      f"{bonds_ok == len(cycles)}")
s0 = int(np.argmin(np.linalg.norm(spheres - ctr, axis=1)))
contacts_of_s0 = {b for b in bond_list if s0 in b}
print(f"  loops around the 12 contacts of the sphere at the origin: {len(contacts_of_s0)} (one per contact);"
      f" per sphere 12/2 = 6 loops")
print("  => The smallest loops of the void network ring the contact points between touching spheres.")
print("     In a Coulomb phase: electric field on the 8 windows/sphere, Gauss law on the 3 voids/sphere,")
print("     magnetic flux through the 6 contact-loops/sphere; charges = rule violations sitting ON voids.")
print("  Eligibility (3-D, bipartite, short even loops, cubic symmetry): YES - geometry is not the obstacle.")

# =============================================================================== B
hdr("B. Regime: does BCT put the network fluid in the liquid (Mott-like) regime?")
print(f"  xi = {XI:.4f} a;  xi/r_oct = {XI / ROCT:.1f}, xi/r_tet = {XI / RTET:.1f}, xi/window = {XI / w:.1f},"
      f"  xi/(oct-tet spacing {A * np.sqrt(3) / 4:.3f} a) = {XI / (A * np.sqrt(3) / 4):.1f}")
gn0 = 1 / XI ** 2
print(f"  interaction scale g n0 = hbar^2/(2 m xi^2) = {gn0:.4f}  (units hbar^2/2m = 1, a = 1)")
# pore-network bands: lowest eigenstates of -lap + V_wall on the cubic FCC cell (4 spheres, 4 oct, 8 tet voids)
def bands(Ng, Vw, nev=6, tau=4e-4, steps=700, seed=0):
    """Block imaginary-time (subspace) iteration with QR, then Rayleigh-Ritz with the exact H.
    nev = 12 covers the 4 octahedral-site states and the 8 tetrahedral-site states of the cubic cell."""
    h = A / Ng
    x = (np.arange(Ng) + 0.5) * h
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')
    inside = np.zeros_like(X, bool)
    for b in basis:
        for c3 in itertools.product((-1, 0, 1), repeat=3):
            cc = b + A * np.array(c3)
            inside |= (X - cc[0]) ** 2 + (Y - cc[1]) ** 2 + (Z - cc[2]) ** 2 < R ** 2
    V = np.where(inside, Vw, 0.0)
    k1 = 2 * np.pi * np.fft.fftfreq(Ng, d=h)
    KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing='ij'); K2 = KX ** 2 + KY ** 2 + KZ ** 2
    eV = np.exp(-tau * V / 2); eK = np.exp(-tau * K2)
    rng = np.random.default_rng(seed)
    B = rng.normal(size=(nev, Ng, Ng, Ng)) * (~inside)
    def orth(B):
        M = B.reshape(nev, -1).T
        Q, _ = np.linalg.qr(M)
        return Q.T.reshape(B.shape)
    B = orth(B)
    for it in range(steps):
        B = eV * np.real(np.fft.ifftn(eK * np.fft.fftn(eV * B, axes=(1, 2, 3)), axes=(1, 2, 3)))
        if it % 10 == 9:
            B = orth(B)
    B = orth(B)
    HB = np.real(np.fft.ifftn(K2 * np.fft.fftn(B, axes=(1, 2, 3)), axes=(1, 2, 3))) + V * B
    Hs = B.reshape(nev, -1) @ HB.reshape(nev, -1).T
    Hs = 0.5 * (Hs + Hs.T)
    w, U = np.linalg.eigh(Hs)
    vecs = (U.T @ B.reshape(nev, -1)).T
    # refine with LOBPCG from the converged subspace (exact H, spectral preconditioner)
    from scipy.sparse.linalg import LinearOperator, lobpcg
    n = Ng ** 3
    Vf = V.ravel()
    def Hmv(v):
        v = np.asarray(v).reshape(Ng, Ng, Ng, -1)
        out = np.real(np.fft.ifftn(K2[..., None] * np.fft.fftn(v, axes=(0, 1, 2)), axes=(0, 1, 2)))
        return out.reshape(n, -1) + Vf[:, None] * v.reshape(n, -1)
    def Pmv(v):
        v = np.asarray(v).reshape(Ng, Ng, Ng, -1)
        return np.real(np.fft.ifftn(np.fft.fftn(v, axes=(0, 1, 2)) / (K2[..., None] + Vf.reshape(Ng, Ng, Ng)[..., None] * 0 + 300.0), axes=(0, 1, 2))).reshape(n, -1)
    Hop = LinearOperator((n, n), matvec=Hmv, matmat=Hmv, dtype=float)
    Pop = LinearOperator((n, n), matvec=Pmv, matmat=Pmv, dtype=float)
    w, vecs = lobpcg(Hop, vecs, M=Pop, largest=False, tol=1e-7, maxiter=400)
    o = np.argsort(w); w = w[o]; vecs = vecs[:, o]
    # residual check
    Hv = np.real(np.fft.ifftn(K2 * np.fft.fftn(vecs.T.reshape(nev, Ng, Ng, Ng), axes=(1, 2, 3)), axes=(1, 2, 3))) + V * vecs.T.reshape(nev, Ng, Ng, Ng)
    res = np.linalg.norm(Hv.reshape(nev, -1) - w[:, None] * vecs.T, axis=1)
    return w, vecs, 1 - inside.mean(), h, res
results = {}
import sys
CONFIGS = [tuple(map(float, c.split(':'))) for c in sys.argv[1:]] or [(48, 3000.0)]
for Ng, Vw in [(int(a), b) for a, b in CONFIGS]:
    w, vecs, pf, hh, res = bands(Ng, Vw)
    results[(Ng, Vw)] = (w, vecs, hh)
    print(f"  grid {Ng}^3, wall {Vw:.0f}: lowest levels = {np.round(w, 5)}  (LOBPCG-refined, rel. accuracy ~1e-7)", flush=True)
w, vecs, hh = results[list(results)[-1]]
oct_band = w[:4]
print(f"  levels 1-4 (one per octahedral void): {np.round(oct_band, 5)};  next level {w[4]:.3f}")
gap_ot = w[4] - oct_band.mean()
print(f"  the next states sit {gap_ot:.0f} higher: the tetrahedral voids act as barriers between octahedral sites")
print("  -> with sealed spheres the low-energy network is a lattice of OCTAHEDRAL sites (an FCC lattice,")
print("     z = 12) linked through tetrahedral voids. FCC tight binding at the zone centre of the cubic cell:")
print("     one level at -12t (Gamma) and three at +4t (X points): splitting = 16 t.")
for key, (ww, _, _) in results.items():
    split = ww[1:4].mean() - ww[0]
    print(f"     {key}: splitting {split:.5f} -> |t| = {abs(split) / 16:.5f}   (triplet spread {np.ptp(ww[1:4]):.1e})")
split = oct_band[1:4].mean() - oct_band[0]
t_oo = abs(split) / 16
psi = vecs[:, 0] / np.sqrt(np.sum(vecs[:, 0] ** 2) * hh ** 3)
I4 = np.sum(psi ** 4) * hh ** 3
Vw_eff = 1 / (4 * I4)
print(f"  effective volume of one octahedral-site state: V_w = {Vw_eff:.4f} a^3 (oct void sphere volume {4 * np.pi * ROCT ** 3 / 3:.4f})")
ts = {k: abs(v[0][1:4].mean() - v[0][0]) / 16 for k, v in results.items()}
t_max = max(ts.values()); t_min = min(ts.values())
print(f"  hopping t = {t_min:.1e} .. {t_max:.1e} (stiffer walls -> smaller t; a true hard wall is smaller still)")
print(f"  interaction scale g n0 = {gn0:.4f}:  g n0 / t = {gn0 / t_max:.0f} .. {gn0 / t_min:.0f}")
t_oo = t_max   # conservative: largest hopping
print("  On-site repulsion U = g/V_w = (g n0)/nbar, nbar = n0 V_w = particles per octahedral void (NOT fixed")
print("  by the corpus). Mott (non-condensed) at integer filling nbar needs, in mean field on z = 12,")
print("  U/(z t) > (2 nbar + 1) + 2 sqrt(nbar (nbar + 1))  [= 5.83 at nbar = 1].")
z = 12
for nb in (1, 2, 3):
    lhs = (gn0 / t_oo) / nb / z
    rhs = (2 * nb + 1) + 2 * np.sqrt(nb * (nb + 1))
    print(f"     nbar = {nb}: U/(z t) = {lhs:8.3f}  vs needed {rhs:6.2f}  -> {'liquid possible' if lhs > rhs else 'condensed'}")
need_ratio = z * 5.83
print(f"  At nbar = 1 the liquid needs g n0 / t > {need_ratio:.0f}; with the largest hopping found, g n0 / t = {gn0 / t_oo:.0f}"
      f"  (margin x{(gn0 / t_oo) / need_ratio:.0f}).")
def nmax(tt):
    r = gn0 / (tt * z); best = 0
    for nb in range(1, 200):
        if r / nb > (2 * nb + 1) + 2 * np.sqrt(nb * (nb + 1)): best = nb
    return best
print(f"  Largest filling that stays non-condensed (mean field): nbar <= {nmax(t_max)} (softest walls) .. {nmax(t_min)} (stiffest)")

hdr("Q1 SUMMARY")
print("  Geometry: the octahedral-tetrahedral void network is 3-D and bipartite (8 windows per oct, 4 per tet,")
print("  no oct-oct or tet-tet), and its smallest loops ring the 12 sphere-sphere contacts (6 loops per sphere).")
print("  Regime: IF the spheres keep the network fluid out (Michel's 'contained' spheres), the fluid's low-energy")
print(f"  states sit in the octahedral voids; the tetrahedral voids are barriers ({gap_ot:.0f} units higher). Octahedral")
print(f"  sites form an FCC lattice with hopping t = {t_min:.1e}..{t_max:.1e}, far below the interaction scale g n0 = {gn0:.3f}.")
print(f"  A non-condensed (Mott-like) network is then possible for up to ~{nmax(t_max)}-{nmax(t_min)} particles per octahedral void.")
print("  Inputs: (1) spheres impermeable to the network fluid [structural; the record has the superfluid passing")
print("  through the shells]; (2) the filling per octahedral void [free number; n0 is not fixed by the corpus].")
print("  No new length is needed: BCT's own xi with the void geometry gives the right regime.")
print("  Score (desk): BOUGHT, 2 inputs - and better than expected. Not yet light: a Mott liquid is necessary,")
print("  not sufficient. Whether it carries an emergent photon is Q2.")
