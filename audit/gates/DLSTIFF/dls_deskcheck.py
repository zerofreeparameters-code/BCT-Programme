#!/usr/bin/env python3
"""
dls_deskcheck.py — Gate DL-STIFF card-thread validation (card §7). 12 Nov 2026.

What it checks, and nothing more:
  1. The identity 1/(4 pi alpha_0) = 1/(4 r_oct r_tet) = 2 xi^2 / a^2, to 30 digits, from the
     MINIMAL_BCT §1.3 definitions. This is the number a "beta fixed by geometry" claim would have
     to produce, and it is the same statement as alpha = alpha_0 for the added field, because the
     Wilson action S = beta * sum_p (1 - cos Phi_p) has beta = 1/e^2 = 1/(4 pi alpha).
  2. That number against the critical couplings already on the ledger (hypercubic 1.0111;
     D4 0.615 card convention / 1.230 Katz–Nogradi convention). Orientation only: the void-network
     beta_c is Gate DL-BETA's job.
  3. Symbolic (sympy): the form of a Maxwell coefficient induced by a medium that couples to the
     field only through a dipole density P (DL's neutral coupling). The induced coefficient is the
     susceptibility chi = dP/dE; if P is identically zero (STIFF: P = 0 by symmetry for the written
     medium) the induced coefficient is zero. This is route R2's kill test, written down so the run
     can re-derive rather than inherit it.
Nothing here derives beta. The run does Q1–Q5.
"""
from mpmath import mp, mpf, sqrt, pi, nstr
import sympy as sp

mp.dps = 30
R = 10
p = lambda label, v: print(f"{label:<56s} {nstr(v, R)}")

print("# 1. The geometric number a 'beta from geometry' claim must produce")
r_oct = (sqrt(2) - 1) / 2
r_tet = (sqrt(mpf(3) / 2) - 1) / 2
alpha0 = r_oct * r_tet / pi
xi = 1 / sqrt(8 * r_oct * r_tet)
p("r_oct", r_oct)
p("r_tet", r_tet)
p("alpha_0 = r_oct r_tet / pi", alpha0)
p("1/alpha_0", 1 / alpha0)
p("xi/a = 1/sqrt(8 r_oct r_tet)", xi)
p("beta_geom = 1/(4 pi alpha_0)", 1 / (4 * pi * alpha0))
p("           = 1/(4 r_oct r_tet)", 1 / (4 * r_oct * r_tet))
p("           = 2 xi^2 / a^2", 2 * xi ** 2)
p("difference of the three forms", abs(1 / (4 * pi * alpha0) - 2 * xi ** 2))
p("for comparison 1/(4 pi alpha_CODATA)", 1 / (4 * pi * mpf("0.0072973525643")))

print("\n# 2. Against critical couplings already on the ledger (orientation; void network = DL-BETA)")
for name, bc in (("hypercubic Z4 (Wilson, standard)", mpf("1.0111")),
                 ("D4, CRIT2 card convention", mpf("0.6150")),
                 ("D4, CRIT2 Katz-Nogradi convention", mpf("1.2300"))):
    p(f"beta_geom / beta_c [{name}]", 2 * xi ** 2 / bc)
print("A beta of ~10.7 sits an order of magnitude inside the Coulomb phase on every lattice known so far;")
print("the question of this gate is whether anything makes beta equal to that number, not whether it suffices.")

print("\n# 3. Route R2 kill test, symbolic: Maxwell coefficient induced by a dipole-coupled medium")
E, P0, chi = sp.symbols('E P0 chi', real=True)
# Most general dipole response linear in E: P = P0 + chi*E  (P0 = spontaneous, chi = susceptibility)
P = P0 + chi * E
# Energy of the medium in the field: -int P dE  = -(P0 E + chi E^2/2)
U = -sp.integrate(P, E)
coeff_E2 = sp.diff(U, E, 2) / 2       # coefficient of E^2 -> induced (1/2)(-chi) E^2 : renormalises eps
print("P(E) =", P, "   U(E) = -int P dE =", sp.expand(U))
print("coefficient of E^2 in U:", sp.simplify(coeff_E2), "  (this is the induced Maxwell/epsilon term)")
print("with P identically zero (STIFF, SC-STIFF-5: P0 = 0 and no polarisable charge => chi = 0):",
      sp.simplify(coeff_E2.subs({chi: 0})))
print("=> a neutral medium with no dipole response induces no Maxwell term; beta cannot come from R2")
print("   unless the run exhibits a nonzero chi from the pinned sources.")

print("\n# 4. Route R3 reminder (Josephson-junction array analogue; no computation, a statement)")
print("link coupling E_J = phase stiffness;  plaquette (loop) coupling = Phi_0^2/(2 L_loop), set by the loop")
print("inductance L_loop, an independent scale. Identifying beta with the phase stiffness needs a derivation")
print("that the added field inherits J; the analogue says it need not.")
