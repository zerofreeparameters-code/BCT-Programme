#!/usr/bin/env python3
"""
Desk-check VOID-MEMBRANE (8 Nov 2026, same-session, CONJECTURE; NOT a gate).
Combined picture: each sphere is bounded by a membrane of FIXED AREA (4 pi R^2, R = a/2) with bending
stiffness kappa; the void network holds the Q1 liquid (nbar particles per octahedral void, ground-state
energy E0 ~ 130 each). How stiff must the membrane be to keep the spheres round and the voids open?

Units as VOID-Q1: hbar^2/2m = 1 (energy unit hbar^2/(2 m a^2)), a = l_P = 1.
Run: python3 -I desk_VOID_membrane.py
"""
import numpy as np

R = 0.5; E0 = 130.0
def hdr(s): print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)

# ---------------------------------------------------------------- void volumes (FCC Delaunay cells)
V_cell = 1 / np.sqrt(2)                         # volume per sphere
V_oct_cell = np.sqrt(2) / 3; V_tet_cell = 1 / (6 * np.sqrt(2))
# sphere volume inside each cell from solid angles at the vertices
om_tet = np.arccos(23 / 27); om_oct = 4 * np.arcsin(1 / 3)
sph_tet = 4 * om_tet / (4 * np.pi) * (4 * np.pi / 3) * R ** 3
sph_oct = 6 * om_oct / (4 * np.pi) * (4 * np.pi / 3) * R ** 3
void_oct = V_oct_cell - sph_oct; void_tet = V_tet_cell - sph_tet
hdr("1. The void the network particles sit in")
print(f"  octahedral void volume {void_oct:.4f} a^3, tetrahedral {void_tet:.4f} a^3 (x2 per sphere);"
      f" total void per sphere {void_oct + 2 * void_tet:.4f} (check {V_cell * (1 - np.pi / (3 * np.sqrt(2))):.4f})")

# ---------------------------------------------------------------- outward push of the network liquid
p_net = (2 / 3) * E0 / void_oct        # per particle in the void: E0 ~ size^-2 ~ V^-2/3
hdr("2. Pressure of the network liquid on the sphere walls")
print(f"  confinement energy ~ size^-2, so p = (2/3) E / V = {p_net:.0f} x nbar   (energy/a^3)")

# ---------------------------------------------------------------- critical pressure of a fixed-area membrane
hdr("3. Fixed-area membrane: pressure at which the round shape gives way (numerical check)")
print("  A fixed-area membrane already prefers the sphere (least bending energy, 8 pi kappa, and most volume).")
print("  Under an outside pressure p it can only lose volume by changing shape. Lowest mode: l = 2.")
th = np.linspace(0, np.pi, 40001)
def shape_props(eps):
    r = 1 + eps * 0.5 * (3 * np.cos(th) ** 2 - 1)
    rho = r * np.sin(th); z = r * np.cos(th)
    drho = np.gradient(rho, th); dz = np.gradient(z, th)
    ds = np.sqrt(drho ** 2 + dz ** 2)
    psi = np.unwrap(np.arctan2(-dz, drho))
    c1 = np.gradient(psi, th) / ds
    with np.errstate(divide='ignore', invalid='ignore'):
        c2 = np.where(rho > 1e-9, np.sin(psi) / rho, c1)
    c2[0] = c1[0]; c2[-1] = c1[-1]
    dA = 2 * np.pi * rho * ds
    A = np.trapezoid(dA, th)
    V = np.trapezoid(np.pi * rho ** 2 * (-dz), th)
    F = 0.5 * np.trapezoid((c1 + c2) ** 2 * dA, th)        # kappa = 1
    return A, V, F
A0, V0, F0 = shape_props(0.0)
print(f"  sphere check: area {A0 / (4 * np.pi):.6f} x 4pi, volume {V0 / (4 * np.pi / 3):.6f} x 4pi/3, bending {F0 / (8 * np.pi):.6f} x 8 pi kappa")
coefs = []
for eps in (0.01, 0.02, 0.04):
    A, V, F = shape_props(eps)
    s = np.sqrt(A0 / A)                                 # rescale to keep the area fixed
    dV = V0 - V * s ** 3; dF = F - F0                   # bending energy is scale-free
    coefs.append(dF / dV)
    print(f"  eps = {eps}: volume lost {dV / V0:.2e}, bending gained {dF / (8 * np.pi):.2e} x 8 pi kappa,"
          f"  dF/dV = {dF / dV:.3f} kappa / R^3")
pc_coef = coefs[0]
print(f"  small-deformation limit: dF/dV -> {pc_coef:.2f} kappa/R^3 (my pencil estimate said 6; the numbers say 12)")
pc = pc_coef / R ** 3
print(f"  -> the round shape holds while p < {pc_coef:.1f} kappa / R^3 = {pc:.0f} kappa (R = a/2)")

# ---------------------------------------------------------------- requirement
hdr("4. How stiff must the membrane be?")
for nb in (1, 4, 11):
    print(f"  nbar = {nb:2d}: network pushes with {p_net * nb:6.0f};  need kappa > {p_net * nb / pc:6.1f}  (units hbar^2/2m)")
k1 = p_net / pc
print(f"  For scale: at nbar = 1, kappa = {k1:.1f} gives a closed-sphere bending energy 8 pi kappa = {8 * np.pi * k1:.0f},")
print(f"  about {8 * np.pi * k1 / E0:.1f} times the confinement energy of one network particle (E0 ~ {E0:.0f}).")

hdr("5. Or let the inside push back")
E_in = (np.pi / R) ** 2                                   # one particle in the sphere's ground state
p_in_per = (2 / 3) * E_in / (4 * np.pi / 3 * R ** 3)
print(f"  one particle in a sphere's ground state: {E_in:.1f}; it pushes outward with {p_in_per:.1f} per particle")
print(f"  balancing the network needs ~{p_net / p_in_per:.0f} particles inside each sphere per particle per void.")
print("  Then a floppy membrane suffices, but the inside/outside ratio becomes one more number to fix.")

hdr("SUMMARY")
print(f"  The network liquid pushes on the spheres with p ~ {p_net:.0f} nbar. A fixed-area membrane stays round while")
print(f"  p < {pc_coef:.0f} kappa/R^3 (computed), so it needs bending stiffness kappa >~ {p_net / pc:.0f} nbar (hbar^2/2m units):")
print("  a genuinely stiff skin, whose bending energy is comparable to a network particle's own confinement")
print("  energy. Alternatively ~13 interior particles per network particle balance the push.")
print("  Either way the membrane picture adds one number (kappa, or the inside/outside ratio) on top of the")
print("  membrane itself and the filling. Touching contacts: with these pressures balanced, the spheres meet")
print("  without pressing, so no facets form; the open question left is the FCC-versus-HCP tie-breaker.")
