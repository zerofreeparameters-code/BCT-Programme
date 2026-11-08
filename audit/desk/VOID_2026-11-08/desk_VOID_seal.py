#!/usr/bin/env python3
"""
Desk-check VOID-SEAL (8 Nov 2026, same-session, CONJECTURE; NOT a gate).
Can anything in BCT make the sphere shells strong walls for the network fluid (the 'sealed spheres'
input of VOID-Q1)? And if not, what is the cheapest physical mechanism that would?

Units as VOID-Q1: hbar^2/2m = 1, a = l_P = 1; g n0 = 1/xi^2 = 0.1862; lowest void state E0 ~ 130.
'Sealed' benchmark: barrier >~ 10 E0 (decay length into a sphere 1/sqrt(V - E0) ~ 0.03 a, below the
0.077 a windows; VOID-Q1 used walls of 23 E0 and 77 E0 and both gave the liquid regime).
Run: python3 -I desk_VOID_seal.py
"""
import numpy as np
ROCT = (np.sqrt(2) - 1) / 2; RTET = (np.sqrt(6) - 2) / 4
ALPHA0 = ROCT * RTET / np.pi; XI = 1 / np.sqrt(8 * np.pi * ALPHA0); R = 0.5
gn0 = 1 / XI ** 2; E0 = 130.0; Vneed = 10 * E0
def hdr(s): print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)
print(f"xi = {XI:.4f} a, g n0 = {gn0:.4f}, void ground state E0 ~ {E0:.0f}, sealing needs a barrier >~ {Vneed:.0f}")

hdr("1. The corpus shell term (alpha0 hbar^2/2mR) oint |Psi|^2 dA  -> delta shell of strength alpha0/R")
lam = ALPHA0 / R; k = np.sqrt(E0)
T = 1 / (1 + lam ** 2 / (4 * k ** 2))
lam_need = 2 * k * np.sqrt(999)
print(f"  strength {lam:.4f}/a; transmission of a void state through it: {T:.7f}")
print(f"  0.1% transmission needs {lam_need:.0f}/a = {lam_need / lam:.1e} x the corpus value  -> does not seal")

hdr("2. The corpus double layer (App J: charge Q = 1 q_P on the shell, thickness d = sqrt(r_tet r_oct))")
d = np.sqrt(RTET * ROCT)
step_P = 1.0 * d / R ** 2            # q_P * dphi in units of E_P  (q_P^2/4 pi eps0 = hbar c)
step_e = step_P * np.sqrt(1 / 137.036)
print(f"  potential step across the layer, for a Planck charge: {step_P:.3f} E_P; for charge e: {step_e:.3f} E_P")
print("  a neutral network fluid feels nothing. For a charged one, the barrier needed is 10 E0 = 650 E_P (m_P/m),")
print(f"  so sealing needs particle mass m >~ {650 / step_P:.0f} m_P (Planck charge) or {650 / step_e:.0f} m_P (charge e).")
print("  -> does not seal: it needs a charged network fluid (not in the medium) AND a mass scale (free), and the")
print("     double layer itself is an asserted input (Gate TWIST Q4(i)).")

hdr("3. A dense sphere interior (same fluid, density contrast n_in/n0)")
ratio = Vneed / gn0
print(f"  a network particle entering a sphere of density n_in pays g n_in; sealing needs n_in/n0 >~ {ratio:.0f}")
print(f"  the interior then out-pushes the voids by (n_in/n0)^2 ~ {ratio ** 2:.0e} in pressure; the corpus shell term")
print("  (a density penalty) holds no pressure: Gate TWIST found it changes the density by ~0.5%.")
print("  -> does not seal: the dense interior would simply spill into the voids.")

hdr("4. Cheapest physical mechanism found: two immiscible components (A1's C^2, with g12 != g)")
g12 = ratio                    # in units of g, with both components at density ~ n0
width = XI / np.sqrt(g12 - 1)
print("  Interior = component 1, network = component 2, mutual repulsion g12. Pressures balance when both")
print("  densities are ~ n0, so no shell strength is needed; the interface itself is the wall.")
print(f"  sealing: a network particle pays g12 n1 >~ {Vneed:.0f}  ->  g12/g >~ {g12:.0f}")
print(f"  interface width (strong segregation) ~ xi / sqrt(g12/g - 1) = {width:.3f} a"
      f"  (windows 0.077 a, sphere radius 0.5 a): thin enough")
print("  V0 as fixed for TWIST has g12 = g exactly (SU(2)-symmetric): the marginal point, where nothing")
print("  separates. Sealing therefore costs ONE coupling, g12/g >~ 7e3, motivated by A1 rather than ad hoc.")
print("  Caveat: phase separation alone coarsens - droplets merge to cut interface area. Something must fix")
print("  the sphere size and the FCC arrangement (e.g. a fixed content per sphere); that is not supplied.")

hdr("SUMMARY")
print("  Nothing already in BCT seals the spheres: shell term 5e4 too weak; double layer needs charge + mass;")
print("  a dense interior bursts. One mechanism does it cleanly: strongly immiscible components (g12/g >~ 7e3),")
print("  interface ~0.03 a, pressures balanced. It replaces 'sealed spheres' (an assumption) with one number,")
print("  and adds a new open question: what fixes each sphere's size against coarsening.")
print("  It does not touch VOID-Q2: light is still outrun.")
