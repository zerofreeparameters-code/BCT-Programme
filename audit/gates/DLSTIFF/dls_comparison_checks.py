#!/usr/bin/env python3
"""
dls_comparison_checks.py -- Gate DL-STIFF, three-run comparison (original d67f5ca, REP2 4a1a83d,
REP3 a2d47c9). Checks the claims the comparison record relies on that sit in only one or two runs,
or that two runs state in different conventions. Not a gate; nothing here can move a verdict.

mpmath 30 digits working, 10 reported; sympy for the two symbolic checks.
Run:  python3 -I dls_comparison_checks.py
"""
from mpmath import mp, mpf, sqrt, pi, log, tanh, nstr
import sympy as sp

mp.dps = 30
N = lambda v: nstr(v, 10)


def row(label, v):
    print(f"  {label:<64s} {v if isinstance(v, str) else N(v)}")


r_oct = (sqrt(2) - 1) / 2            # MINIMAL_BCT §1.3, in units of the sphere diameter d_nn
r_tet = (sqrt(6) - 2) / 4
alpha0 = r_oct * r_tet / pi
xi = 1 / sqrt(8 * r_oct * r_tet)     # xi / d_nn
beta_geom = 1 / (4 * r_oct * r_tet)  # unit-free form

print("1. Numbers all three runs report (must agree)")
row("beta_geom = 1/(4 r_oct r_tet) = 1/(4 pi alpha_0)", beta_geom)
g = alpha0 * 4 * pi * (mpf(1) / 2) * tanh(r_oct / xi) ** 2
row("App J g = alpha_0 4 pi R tanh^2(r_oct/xi), R = 1/2", g)
row("alpha_0 / g", alpha0 / g)
row("R5 ln(Lambda/m), card coefficient 1/(12 pi^2)", beta_geom * 12 * pi ** 2)
row("R5 ln(Lambda/m), Dirac 1/(6 pi^2)", beta_geom * 6 * pi ** 2)
row("R5 ln(Lambda/m), complex scalar 1/(24 pi^2)", beta_geom * 24 * pi ** 2)
row("ICE E_J/E_C = 2 nbar^2 xi^2/a^2 at nbar = 1, a = d_nn", 2 * xi ** 2)
row("  ... at nbar = 2", 8 * xi ** 2)

print("\n2. Card R5 coefficient (REP2's note): Dirac one-loop in two log conventions")
L = sp.symbols("L", positive=True)        # L = ln(Lambda/m)
print("  (1/(6 pi^2)) ln(Lambda/m) - (1/(12 pi^2)) ln(Lambda^2/m^2) =",
      sp.simplify(L / (6 * sp.pi ** 2) - (2 * L) / (12 * sp.pi ** 2)))

print("\n3. Duality: REP2 '2-form coefficient 1/(8 pi^2 K)' vs REP3 'beta_dual = 1/(4 pi^2 K)'")
K, beta = sp.symbols("K beta", positive=True)
# REP3 writes S = (beta/2) sum H^2; REP2 writes S = c sum H^2. Same action iff c = beta/2.
print("  c = beta/2 with beta = 1/(4 pi^2 K):  c =", sp.simplify((1 / (4 * sp.pi ** 2 * K)) / 2),
      " -> identical action")

print("\n4. REP2 CN-DLS-08 (units): 2 xi^2 / a^2 for each length a = 1 could mean")
a_c = sqrt(2)                          # Gate DL's cubic edge, in d_nn (d_nn = a_c/sqrt2)
link = sqrt(3) / 4 * a_c               # oct-tet window link (DL step 0: d = sqrt3/4 a_c)
cell = (a_c ** 3 / 12) ** (mpf(1) / 3) # volume per void: 12 voids per conventional cell
for lab, a in (("a = d_nn (sphere diameter; MINIMAL / App J R = a/2)", mpf(1)),
               ("a = Gate DL cubic edge", a_c), ("a = oct-tet link length", link),
               ("a = per-void cell size", cell)):
    row(lab, 2 * xi ** 2 / a ** 2)
row("REP2: classical coupling sqrt(E_J/E_C) at nbar = 1, a = d_nn", sqrt(2 * xi ** 2))

print("\n5. Original CN-DLS-03/04: beta = c/(r_oct r_tet); minimum c for beta > beta_c")
for lab, bc in (("hypercubic 1.0111", mpf("1.0111")), ("D4 card 0.6150", mpf("0.6150")),
                ("D4 Katz-Nogradi 1.2300", mpf("1.2300"))):
    row(f"c_min ({lab})", bc * r_oct * r_tet)
row("candidate c", beta_geom * r_oct * r_tet)
row("Original CN-DLS-10: 1/alpha a derived beta would predict (1/alpha_0)", 1 / alpha0)

print("\n6. MINIMAL §1.4 amplitude gap (REP2 CN-DLS-10; REP3 saw it, did not record it)")
J, xs, P0, d = sp.symbols("J xi Psi0 delta", positive=True)
# L = J|dPsi|^2 - (J/4 xi^2)(|Psi|^2 - Psi0^2)^2 ; Psi = Psi0 + delta (real fluctuation)
V = J / (4 * xs ** 2) * ((P0 + d) ** 2 - P0 ** 2) ** 2
m2 = sp.simplify(sp.diff(V, d, 2).subs(d, 0) / (2 * J))    # kinetic J (d delta)^2 -> m^2 = V''/(2J)
print("  m^2 =", m2, "  -> m =", sp.sqrt(m2), " ; MINIMAL §1.4 prints 2/xi, which needs Psi0 =",
      sp.solve(sp.Eq(sp.sqrt(m2), 2 / xs), P0))
row("  2/xi (as printed in §1.4)", 2 / xi)
