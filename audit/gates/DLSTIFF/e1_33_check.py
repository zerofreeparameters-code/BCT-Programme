#!/usr/bin/env python3
"""
e1_33_check.py — POST-GATE desk check of App E.1 §3.3 (NOT part of Gate DL-STIFF).

Gate DL-STIFF is sealed; App E.1 is not among its §4.1 pinned sources and was not read
during the run. This script checks the arithmetic of the section the gate recorded as
CN-DLS-09 / R6d, now that it has been read. Nothing here can move the gate's verdict.

Source text (App E.1 §3.3, from BCT_Appendices_Volume1_2026_compressed_Part1.pdf, p.54-55):
    S_monopole = (2pi/e)^2 x (rho_s/2) x a = 4 pi^2 rho_s a
    In BCT units where a = l_P and rho_s = J/l_P:   S_monopole = 4 pi^2 J
    Taking J = 1/g0^2 where g0^2 = 4 pi alpha_0:    J = 1/(4 pi alpha_0) ~= 10.74
    S_monopole = 4 pi^2/(alpha 4 pi alpha_0) = pi/(4 alpha_0 alpha) ~= 34
    P_monopole ~ exp(-34) ~= 2 x 10^-15
and §3.4:  "the Wilson plaquette action ... giving the Maxwell action with coupling
            1/e^2 = J"; "1/e^2_ren = 1/(4 pi alpha) where alpha = alpha_0(1-3alpha_0)/(1-alpha_0)"
"""
from mpmath import mp, mpf, sqrt, pi, exp, log, nstr

mp.dps = 30
p = lambda label, v: print(f"{label:<50s} {nstr(v, 10)}")

r_oct = (sqrt(2) - 1) / 2
r_tet = (sqrt(6) - 2) / 4
alpha0 = r_oct * r_tet / pi
alpha = mpf("0.0072973525643")
J = 1 / (4 * pi * alpha0)

print("=" * 76)
print("1. THE PARAMETER ITSELF")
print("=" * 76)
p("alpha_0 = r_oct r_tet / pi", alpha0)
p("J = 1/(4 pi alpha_0)  [E.1's 'Taking ...']", J)
print("E.1's words: 'The lattice stiffness J must be LARGE for the BCT medium to be")
print("physically rigid ... TAKING J = 1/g0^2 where g0^2 = 4 pi alpha_0'.")
print("=> the only ARGUMENT offered is that J be large; the VALUE is introduced by")
print("   'Taking'. No derivation of J = 1/(4 pi alpha_0) appears in §3.1-3.4.")

print()
print("=" * 76)
print("2. S_monopole: FIVE VALUES FOR ONE QUANTITY")
print("=" * 76)
e2 = 1 / J                                   # from §3.4's own  1/e^2 = J
v_a = (2 * pi) ** 2 / e2 * (J / 2)           # (2pi/e)^2 (rho_s/2) a  with rho_s a = J
v_b = 4 * pi ** 2 * J                        # the printed 4 pi^2 rho_s a = 4 pi^2 J
v_c = 4 * pi ** 2 / (alpha * 4 * pi * alpha0)  # literal reading of the printed form
v_d = pi / (4 * alpha0 * alpha)              # the printed second form
v_e = pi * J                                 # what the printed number 34 actually equals
p("(a) (2pi/e)^2 (rho_s/2) a, using 1/e^2 = J", v_a)
p("(b) 4 pi^2 J          [E.1's own next line]", v_b)
p("(c) 4 pi^2/(alpha 4 pi alpha_0) = pi/(alpha alpha_0)", v_c)
p("(d) pi/(4 alpha_0 alpha)  [printed]", v_d)
p("(e) pi J                 [= the printed '34']", v_e)
print()
print("E.1 prints (a) = (b) and (b) = (c) = (d) ~= 34. Every one of those equalities fails:")
p("  (a)/(b)", v_a / v_b)
p("  (c)/(b)", v_c / v_b)
p("  (d)/(b)", v_d / v_b)
p("  (b)/(e)  [= 4 pi, the factor the printed answer is short by]", v_b / v_e)
p("  4 pi", 4 * pi)
print("  The printed '~= 34' is pi J = 33.75: the correct 4 pi^2 J divided by 4 pi.")
print("  (a) = (b) would need e^2 = 1/2, contradicting §3.4's own 1/e^2 = J.")

print()
print("=" * 76)
print("3. THE SUPPRESSION FACTOR")
print("=" * 76)
p("P ~ exp(-34)   [printed]", exp(-34))
print("   printed as '~= 2 x 10^-15' -- consistent with 34, so the error is upstream")
p("P ~ exp(-pi J) = exp(-33.747)", exp(-v_e))
p("P ~ exp(-4 pi^2 J) = exp(-424.078)", exp(-v_b))
p("  log10 of that", -v_b / log(10))
print("=> the TRUE suppression on E.1's own J is ~10^-184, not ~10^-15.")
print("   The error runs AGAINST the corpus's rhetoric and FOR its conclusion:")
print("   monopoles are far more suppressed than claimed. Direction unchanged.")

print()
print("=" * 76)
print("4. THE CORRECTION MAP E.1 §3.4 WRITES DOWN")
print("=" * 76)
alpha_map = alpha0 * (1 - 3 * alpha0) / (1 - alpha0)
p("alpha_0", alpha0)
p("1/alpha_0", 1 / alpha0)
p("alpha_map = alpha_0(1-3 alpha_0)/(1-alpha_0)", alpha_map)
p("1/alpha_map", 1 / alpha_map)
p("1/alpha CODATA", 1 / alpha)
p("relative error of the map vs CODATA", abs(alpha_map - alpha) / alpha)
p("beta_bare = 1/(4 pi alpha_0)", J)
p("beta_ren  = 1/(4 pi alpha_map)", 1 / (4 * pi * alpha_map))
p("beta at CODATA alpha", 1 / (4 * pi * alpha))
print("So E.1 treats 10.74 as the BARE coupling and reaches the measured alpha through")
print("this algebraic map -- which is exactly the object FWD/STAT closed as a SELECTED")
print("correction map. The map's accuracy (2e-5) is not evidence it is a derivation;")
print("that is the question those gates settled, and this gate does not reopen it.")
print("Note for DL-STIFF's CN-DLS-10: the bare/renormalised reading is why that notice")
print("says the 1.5 % gap is what FWD/STAT closed, rather than calling it a bare error.")

print()
print("=" * 76)
print("5. CN-LINK-09 CROSS-CHECK: the corpus's OTHER bare U(1) coupling")
print("=" * 76)
g2_jh4 = pi ** 5 / 6
p("JH4's g^2 = pi^5/6", g2_jh4)
p("  as a Wilson beta = 1/g^2", 1 / g2_jh4)
p("E.1's beta = 1/e^2 = J", J)
p("  ratio", J * g2_jh4)
print("beta_c (hypercubic) = 1.0111: E.1's 10.74 is deep Coulomb, JH4's 0.0194 is deep")
print("CONFINED. The corpus asserts two incompatible values for the same bare coupling.")
