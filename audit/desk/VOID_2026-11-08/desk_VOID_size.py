#!/usr/bin/env python3
"""
Desk-check VOID-SIZE (8 Nov 2026, same-session, CONJECTURE; NOT a gate).
If the spheres are droplets of one component sealed off by immiscibility (desk_VOID_seal.py), what fixes
their size and holds them in BCT's arrangement: an FCC lattice of TOUCHING spheres, filling fraction
phi = pi/(3 sqrt2) = 0.7405, with the other component in a connected void network (25.95%)?

M1  Interface tension alone.
M2  Interface tension + a long-range repulsion between like regions (Coulomb-frustrated phase
    separation; e.g. a net charge per sphere with a neutralising background). This is the textbook
    size-fixing mechanism (nuclear 'pasta', block copolymers, colloids). In the Wigner-Seitz treatment
    (Ravenhall, Pethick & Wilson, PRL 50, 2066 (1983)) the minimised energy density is
        E_min = (3/2) (4 pi sigma^2 rho^2)^(1/3) * g_d(u),   g_d(u) = u (d^2 f_d(u))^(1/3)
    for spheres (d=3), rods (d=2), slabs (d=1) of volume fraction u, and with u -> 1-u for the inverted
    phases (bubbles, tubes). g_d does not depend on sigma or rho, so the morphology comparison at fixed
    u needs NO couplings.
M3  A fixed content per sphere (a 'bag': N particles held by an outside pressure).
Run: python3 -I desk_VOID_size.py
"""
import numpy as np

phi = np.pi / (3 * np.sqrt(2))
R = 0.5; XI = 2.31754; g12 = 6982
w = XI / np.sqrt(g12 - 1)
def hdr(s): print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)

hdr("M1. Interface tension alone")
print("  Energy = sigma x total interface area. At fixed volume fraction the area per volume is 3 phi / R,")
print("  so the energy falls as 1/R: bigger spheres always win. Merging two spheres cuts their interface by")
print(f"  {100 * (1 - 2 ** (-1 / 3)):.0f}%. -> no size is fixed; the lattice coarsens.")
neck = np.sqrt(2 * w * R)
print(f"  Worse, BCT's spheres TOUCH. With interface width w = {w:.3f} a (from the sealing check), the two")
print(f"  interfaces overlap within rho ~ sqrt(2 w R) = {neck:.3f} a of each contact, so the interiors join")
print("  through a neck at all 12 contacts: the 'spheres' form one connected domain, which can only coarsen.")

hdr("M2. Long-range repulsion (frustrated phase separation): which shape wins at BCT's filling?")
def f(d, u):
    if d == 2:
        return 0.25 * (np.log(1 / u) - 1 + u)
    return (1 / (d + 2)) * ((2 / (d - 2)) * (1 - 0.5 * d * u ** (1 - 2 / d)) + u)
def g(d, u): return u * (d * d * f(d, u)) ** (1 / 3)
rows = [("spheres of the interior fluid (BCT's picture)", 3, phi),
        ("rods of the interior fluid", 2, phi),
        ("slabs", 1, phi),
        ("tubes: rods of the NETWORK fluid in an interior-fluid matrix", 2, 1 - phi),
        ("bubbles: spheres of the NETWORK fluid in an interior-fluid matrix", 3, 1 - phi)]
vals = [(name, g(d, u)) for name, d, u in rows]
best = min(v for _, v in vals)
for name, v in vals:
    print(f"  {name:64s} g = {v:.4f}  ({100 * (v / best - 1):+5.1f}% vs best)")
print(f"  at phi = {phi:.4f}: the touching-sphere arrangement is the HIGHEST-energy shape of the five.")
print("  The winners are the inverted shapes: the network fluid would form isolated tubes or bubbles inside")
print("  a continuous interior fluid. That is the opposite of BCT: no separate spheres, no connected network.")
print("  (Same sequence as nuclear 'pasta': spheres only at low filling; bubbles and tubes near 3/4 filling.)")
# filling at which spheres would win
us = np.linspace(0.01, 0.99, 981)
win = [u for u in us if g(3, u) <= min(g(2, u), g(1, u), g(2, 1 - u), g(3, 1 - u))]
print(f"  Spheres win only for interior filling u <~ {max(win):.2f} (separated spheres, not touching ones).")

hdr("M3. Fixed content per sphere (a 'bag')")
print("  N particles confined in a sphere carry kinetic energy ~ N pi^2 hbar^2/(2 m R^2); an outside pressure P")
print("  squeezes it. Minimising N pi^2/R^2 + P (4 pi/3) R^3 (units hbar^2/2m) gives R^5 = N pi/(2 P).")
print("  -> the size is set by N and P: two free numbers, and soft: dlnR/dlnP = -1/5.")
print("  -> touching happens at one pressure only; below it the spheres separate, above it they press into")
print("     flat facets (as compressed emulsions do) and the voids shrink and close. And at the contacts")
print("     the M1 neck problem still merges neighbours unless something keeps the boundaries apart.")

hdr("SUMMARY")
print("  If the spheres are emerging droplets, nothing tested fixes their size AND gives touching FCC spheres:")
print("   M1 tension alone: no size; touching spheres neck together and coarsen.")
print("   M2 long-range repulsion: fixes a size, but at 74% filling it prefers tubes/bubbles of the network")
print("      fluid; spheres are the worst shape (they win only below ~%.0f%% filling)." % (100 * max(win)))
print("   M3 fixed content: size set by two free numbers; touching only at one pressure; deformable.")
print("  What would work: a boundary with its own identity - a membrane that does not merge at contact and")
print("  has a fixed area (e.g. a fixed number of shell units). That is App J's double layer promoted to a")
print("  physical membrane, which is an input, not a result.")
print("  The alternative is to keep the lattice as BCT's starting postulate (size fixed by fiat, a = l_P); then")
print("  sealing must also be a property of that postulated cell wall, and the immiscibility mechanism is not")
print("  needed.")
