#!/usr/bin/env python3
"""
GATE ICE - Step 2 (soft branch): does the GP stiffness J cancel, and what
dimensionless ratio controls superfluid vs Coulomb? Symbolic, cold.
"""
import sympy as sp

hbar, m, g, a, nbar, xi = sp.symbols('hbar m g a nbar xi', positive=True)

# GP order parameter psi = sqrt(rho) e^{i phi}, rho = nbar/a^3 (occupation per void).
rho = nbar / a**3

# Phase-gradient stiffness coefficient K in E = (1/2) int K (grad phi)^2 d^3r
K = hbar**2 * rho / m                     # [J/m]
# Josephson (phase) energy per window/link (length ~ a, volume ~ a^3):
#   (1/2) K (dphi/a)^2 * a^3  ->  E_J ~ K * a
E_J = K * a                               # phase-coherence scale (favours superfluid)

# On-site charging energy: cost of one extra boson on a void of volume ~ a^3.
#   U ~ g * |psi|^2_overlap ~ g / a^3
E_C = g / a**3                            # number-localisation scale (favours Mott/ice)

ratio_raw = sp.simplify(E_J / E_C)
print("E_J        =", E_J)
print("E_C        =", E_C)
print("E_J/E_C    =", ratio_raw, "   <- note the explicit hbar^2/m (=J-scale) still present")

# Eliminate g via the healing length:  xi^2 = hbar^2 / (2 m g rho)
g_of_xi = sp.solve(sp.Eq(xi**2, hbar**2/(2*m*g*rho)), g)[0]
print("\ng(xi)      =", sp.simplify(g_of_xi))

ratio = sp.simplify(ratio_raw.subs(g, g_of_xi))
print("E_J/E_C    =", ratio, "   <- after substituting xi")

# Does the J-scale hbar^2/m survive?
has_J = ratio.has(hbar) or ratio.has(m)
print("contains hbar or m (i.e. J-scale) ? ->", has_J)
print("controlling dimensionless ratio r = E_J/E_C =", sp.nsimplify(ratio))

# sanity: both energies share hbar^2/m
print("\nE_J  factor of hbar^2/m :", sp.simplify(E_J/(hbar**2/m)))
print("E_C  after xi-subst      :", sp.simplify(E_C.subs(g,g_of_xi)),
      "=", sp.simplify(E_C.subs(g,g_of_xi)/(hbar**2/m)),"* hbar^2/m")
