#!/usr/bin/env python3
"""
Desk-check VOID-Q2 (8 Nov 2026, same-session, CONJECTURE; NOT a gate).

Question 2: Does the void-network quantum liquid of Q1 carry light -- a massless photon with two
polarisations, isotropic, and the FASTEST signal in the medium?

Inputs carried from Q1 (desk_VOID_Q1_output.txt): low-energy sites = octahedral voids (an FCC lattice,
z = 12), hopping t = 2.9e-5 .. 1.5e-4, interaction scale g n0 = 0.1862 (units hbar^2/2m = 1, a = 1),
on-site U = g n0 / nbar, liquid (Mott) needs U/(12 t) > 5.83 at nbar = 1.

Part A  Structure: does the low-energy model carry a U(1) gauge structure (a 'Gauss law' with the
        electric field on links of a bipartite lattice)?
        - is the octahedral-site lattice bipartite? (triangles?)
        - in how many 'constraint units' (tetrahedral voids) does each site sit? (pyrochlore: exactly 2,
          which is what turns a site into a link between two units; here?)
Part B  Speeds: in lattice Coulomb phases the photon comes from ring exchange around the smallest loop,
        J_ring ~ t^L / U^(L-1), while a charge (a rule violation) moves by single hops, ~ t.
        So v_charge / c_photon ~ (U/t)^(L-1). Light must be the fastest signal (electrons and photons
        share one limiting speed to high precision). Q1 needs U/t large. Compute the ratio.
Run: python3 -I desk_VOID_Q2.py
"""
import numpy as np, itertools

A = np.sqrt(2.0)
def hdr(s): print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)

# =============================================================================== A
hdr("A. Structure of the low-energy lattice (octahedral sites)")
oct_b = np.array([[.5, 0, 0], [0, .5, 0], [0, 0, .5], [.5, .5, .5]]) * A
tet_b = np.array([[x, y, z] for x in (.25, .75) for y in (.25, .75) for z in (.25, .75)]) * A
L = 3
O = np.array([p + A * np.array(c) for c in itertools.product(range(L), repeat=3) for p in oct_b])
T = np.array([p + A * np.array(c) for c in itertools.product(range(L), repeat=3) for p in tet_b])
Lbox = L * A
def dmin(u, v):
    d = u - v; d -= Lbox * np.round(d / Lbox); return np.linalg.norm(d)
n = len(O)
adj = [[j for j in range(n) if j != i and abs(dmin(O[i], O[j]) - 1.0) < 1e-9] for i in range(n)]
print(f"  octahedral sites: {n} in a periodic {L}x{L}x{L} cell block; neighbours per site: {len(adj[0])} (FCC, spacing 1 a)")
tri = sum(1 for i in range(n) for j in adj[i] for k in adj[j] if k in adj[i] and i < j < k)
print(f"  triangles among octahedral sites: {tri} ({3 * tri / n:.0f} per site)")
color = [-1] * n; color[0] = 0; stack = [0]; bip = True
while stack:
    i = stack.pop()
    for j in adj[i]:
        if color[j] < 0: color[j] = 1 - color[i]; stack.append(j)
        elif color[j] == color[i]: bip = False
print(f"  two-colourable (bipartite)? {bip}")
units = [sum(1 for t in T if abs(dmin(O[i], t) - A * np.sqrt(3) / 4) < 1e-9) for i in range(4)]
print(f"  tetrahedral voids touching each octahedral site: {units}  (pyrochlore needs exactly 2)")
print("  => Each site belongs to 8 constraint units, not 2. A site variable cannot be read as a flux on a")
print("     link between two units, so no Gauss law follows from the bare model. The bipartite oct-tet")
print("     graph has the right shape, but its links (the windows) carry no low-energy degree of freedom:")
print("     the tetrahedral voids are barriers (Q1). A U(1) Coulomb structure must be ADDED, e.g. by extra")
print("     interactions that impose a rule on every tetrahedral void and make it resonate (new inputs).")

# =============================================================================== B
hdr("B. Speeds: the photon versus the charges (granting a Coulomb phase)")
# max group velocity of a single hopping particle on the FCC octahedral lattice (t = 1, spacing 1)
ks = np.linspace(-np.pi, np.pi, 81) * 2 / A
KX, KY, KZ = np.meshgrid(ks, ks, ks, indexing='ij')
h = A / 2
def vel(kx, ky, kz):
    gx = 4 * h * (np.sin(kx * h) * np.cos(ky * h) + np.sin(kx * h) * np.cos(kz * h))
    gy = 4 * h * (np.sin(ky * h) * np.cos(kx * h) + np.sin(ky * h) * np.cos(kz * h))
    gz = 4 * h * (np.sin(kz * h) * np.cos(kx * h) + np.sin(kz * h) * np.cos(ky * h))
    return np.sqrt(gx ** 2 + gy ** 2 + gz ** 2)
vmax = vel(KX, KY, KZ).max()
print(f"  single-hop band (E = -4t sum cos cos): maximum speed = {vmax:.2f} t a / hbar")
gn0 = 0.1862
t_range = (2.9e-5, 1.5e-4)
print("  photon speed ~ J_ring a / hbar with J_ring ~ t^L / U^(L-1); smallest loops on the octahedral")
print("  lattice: triangles (L = 3); smallest even loops L = 4. Ratio v_charge / c_photon ~ vmax (U/t)^(L-1):")
print("     t        nbar   U/t      L=3            L=4")
for t in t_range:
    for nb in (1, 4):
        Ut = gn0 / nb / t
        r3 = vmax * Ut ** 2; r4 = vmax * Ut ** 3
        print(f"   {t:.1e}    {nb}   {Ut:8.0f}   {r3:10.1e}     {r4:10.1e}")
Ut_min = 12 * 5.83
print(f"  Even at the edge of the liquid (U/t = {Ut_min:.0f}, the least Q1 allows): L=3 ratio = {vmax * Ut_min ** 2:.1e},"
      f" L=4 = {vmax * Ut_min ** 3:.1e}")
print("  For light to be the fastest signal the ratio must be <= 1, i.e. U/t <~ 1 - but then the liquid melts")
print("  into a superfluid (Q1 needs U/t >~ 70). The two requirements exclude each other.")
print("  Observed: photons and electrons share one limiting speed to many decimal places; here charges")
print("  living on the voids would outrun light by 10^4 (edge of the liquid) to 10^12 (BCT values).")

hdr("C. What does pass, granted a Coulomb phase")
print("  - two transverse polarisations: yes (emergent U(1) in 3-D)")
print("  - massless: yes, in the Coulomb phase")
print("  - isotropy: cubic symmetry -> isotropic at long wavelength, corrections ~ (a/lambda)^2 ~ 1e-57 for")
print("    visible light at Planck spacing; far inside the 1e-17..1e-18 limits")

hdr("Q2 SUMMARY")
print("  Structure: NOT supplied. The octahedral sites form a non-bipartite FCC lattice, each site in 8")
print("  tetrahedral units; no Gauss law comes out of the model Q1 found. A Coulomb phase must be added.")
print("  Speed: FAILS even if added. Charges hop at first order (~t), photons only via ring exchange")
print("  (~t^L/U^(L-1)), so matter outruns light by (U/t)^(L-1) >= ~10^4, while the liquid needs U/t >= 70.")
print("  Score (desk): FAIL. Polarisations, masslessness and isotropy would be fine; the speed ordering is not.")
