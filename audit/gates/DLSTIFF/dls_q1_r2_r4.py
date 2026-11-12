#!/usr/bin/env python3
"""
dls_q1_r2_r4.py — Gate DL-STIFF, Q1 part 2: kill tests for R2 and R4.

R2 (induced Maxwell term from the medium's dipole response): re-derive the card's §7
part-3 statement cold, then ask of the pinned sources whether any term gives chi != 0.

R4 (alpha_0 as the surface/boundary coupling): re-derive sigma_s from
tex/BCT_Appendix_J_SphereAction.tex §J.1.3 (eq:sigma, eq:alpha0, the boxed result at
lines 147-168) with EVERY input named and tiered; reproduce Gate TANH's computed
g = 0.00036975; and test the step R4 needs but does not take, from a sphere-surface
potential sigma_s (dimension 1/length after dividing by J) to a window-link plaquette
coupling beta (dimensionless).
"""
from mpmath import mp, mpf, sqrt, pi, tanh, nstr
import sympy as sp

mp.dps = 30
R_DIG = 10
p = lambda label, v: print(f"{label:<54s} {nstr(v, R_DIG)}")

# --- the pinned geometry (audit/MINIMAL_BCT.md §1.3) ---
r_oct = (sqrt(2) - 1) / 2
r_tet = (sqrt(6) - 2) / 4
alpha0 = r_oct * r_tet / pi
xi = 1 / sqrt(8 * r_oct * r_tet)
Rsph = mpf(1) / 2          # App J: R; "energies of order c/R = 2 m_P c^2" and 4 pi R = 6.2832
beta_geom = 2 * xi ** 2

print("=" * 78)
print("R2 — INDUCED MAXWELL TERM FROM THE MEDIUM'S DIPOLE RESPONSE")
print("=" * 78)
E, P0, chi = sp.symbols('E P0 chi', real=True)
P = P0 + chi * E                       # most general response linear in E
U = -sp.integrate(P, E)                # energy of the medium in the field
coeff_E2 = sp.diff(U, E, 2) / 2
print("P(E) =", P)
print("U(E) = -Int P dE =", sp.expand(U))
print("coefficient of E^2 in U:", sp.simplify(coeff_E2), " -> the induced Maxwell/epsilon term")
print("so the induced shift in beta is  delta_beta ~ -chi/2  (per plaquette, same normalisation)")
print()
print("Does any term in the pinned sources give chi != 0?")
print("  audit/MINIMAL_BCT.md §1.2: S = Int [ J |dPsi|^2 - (J/4xi^2)(|Psi|^2-Psi_0^2)^2 ].")
print("    No gauge field appears. No P, no chi, no epsilon_0, no electric charge.")
print("  audit/gates/STIFF/STIFF_RESULT.md, CN-STIFF-01 [PROVEN]: for a reflection-symmetric")
print("    window the GP ground state is even, so Int z delta_n dz = 0: P = 0 identically,")
print("    'not small, not soft, but identically absent' (SC-STIFF-5).")
print("  CN-STIFF-02 [PROVEN]: the Smoluchowski two-component mechanism needs a second,")
print("    independently-profiled charged distribution; one complex scalar has none.")
print("  CN-STIFF-03 [PROVEN, numeric]: a nonzero window dipole appears only under an")
print("    IMPOSED void-to-void bias, linearly in it, vanishing with it.")
print("  => chi = 0 for the pinned medium. No nonzero chi can be exhibited from the pinned")
print("     sources, which is the condition the card set for keeping the route.")
print("  R2: CLOSED.  (Also closed upstream by the decoupling theorem: with no Psi-a term in")
print("     the action there is nothing to integrate out that knows about a.)")
print("  delta_beta with chi = 0:", sp.simplify(coeff_E2.subs({chi: 0})))

print()
print("=" * 78)
print("R4 — alpha_0 AS THE SURFACE/BOUNDARY COUPLING (App J §J.1.3-1.4)")
print("=" * 78)
print("App J eq:sigma      sigma_s = Delta_V * d  ~  Q d^2 / (4 pi R^2)")
print("App J eq:alpha0     alpha_0 = r_tet r_oct / (4 pi R^2)")
print("App J boxed         sigma_s = alpha_0            [in units J = 1]")
print()
print("Re-derivation with every input named (card §4.2 tiering):")
inputs = [
    ("r_oct = (sqrt2 - 1)/2", "GEOMETRY", "MINIMAL_BCT §1.3 / App D", r_oct),
    ("r_tet = (sqrt6 - 2)/4", "GEOMETRY", "MINIMAL_BCT §1.3 / App D", r_tet),
    ("R = 1/2 (sphere radius, lattice units)", "GEOMETRY", "App J (c/R = 2 m_P; 4 pi R = 6.2832)", Rsph),
    ("Q = 1 (one Planck charge unit)", "ASSERTED", "App J line 161, flagged as an input in App J itself", mpf(1)),
    ("d = sqrt(r_tet r_oct) (shell thickness)", "ASSERTED", "App J line 162, flagged as an input in App J itself", sqrt(r_tet * r_oct)),
    ("J = 1 (stiffness unit)", "CONVENTION", "App J line 166-168", mpf(1)),
    ("l_P = a = 1 (length unit)", "CONVENTION", "needed to equate a 1/length with a pure number", mpf(1)),
]
print(f"{'input':<42s} {'tier':<10s} {'value'}")
print("-" * 78)
for name, tier, src, val in inputs:
    print(f"{name:<42s} {tier:<10s} {nstr(val, R_DIG)}")
print("-" * 78)
for name, tier, src, val in inputs:
    print(f"  {name.split(' =')[0].split(' (')[0]:<12s} source: {src}")

sigma_s = mpf(1) * (sqrt(r_tet * r_oct)) ** 2 / (4 * pi * Rsph ** 2)   # Q=1, d^2 = r_tet r_oct
print()
p("sigma_s = Q d^2/(4 pi R^2) with Q=1, d^2=r_tet r_oct", sigma_s)
p("alpha_0 = r_tet r_oct/(4 pi R^2)", alpha0)
p("difference", abs(sigma_s - alpha0))
print("  -> the App J identity reproduces exactly, AS AN IDENTITY, once Q = 1 and")
print("     d = sqrt(r_tet r_oct) are put in: d^2/(4 pi R^2) IS alpha_0/Q by construction.")
print("     Two asserted inputs do the whole of the work; App J's own summary footnote")
print("     says so ('uses Q=1 and d=sqrt(r_tet r_oct) as inputs').")

print()
print("Gate TANH's computed window/overlap coupling, re-derived cold (App J §J.3.1):")
g_computed = alpha0 * 4 * pi * Rsph * tanh(r_oct / xi) ** 2
p("r_oct/xi", r_oct / xi)
p("tanh^2(r_oct/xi)", tanh(r_oct / xi) ** 2)
p("4 pi R", 4 * pi * Rsph)
p("g = alpha_0 * 4 pi R * tanh^2(r_oct/xi)", g_computed)
p("alpha_0", alpha0)
p("alpha_0 / g", alpha0 / g_computed)
print("  matches App J's printed 0.00036975 and TANH SC-TANH-3 (alpha_0/g = 20.0353):")
print("  the computed coupling is NOT alpha_0. TANH's finding reproduces.")

print()
print("The step R4 must take and does not: sphere surface -> window plaquette.")
print("  sigma_s/J is a RADIAL BOUNDARY CONDITION at r = R: it enters App J only as the")
print("  derivative jump [d_r Psi] = -(sigma_s/J) Psi(R), i.e. in kappa cot(kappa R) =")
print("  -1/xi + sigma_s/J. Its dimension is 1/length (it sits next to 1/xi).")
print("  beta is dimensionless and lives on the PLAQUETTES of the void graph (nodes = oct")
print("  and tet voids, links = triangular windows). The two objects differ in:")
print("    (i)  dimension      : 1/length  vs  dimensionless")
print("    (ii) support        : sphere shells r = R  vs  minimal cycles of the void graph")
print("    (iii) role          : a boundary condition on Psi  vs  the coefficient of")
print("                          (1 - cos Phi_p) for a field Psi is NEUTRAL under")
print("  The third is fatal on its own: sigma_s is a coupling OF THE MEDIUM TO THE SHELL,")
print("  and the added link field does not appear in it. Equating it with beta is not a")
print("  derivation but a renaming, and it needs l_P = a = 1 to be even numerically stated.")
p("if one asserts beta = 1/(4 pi sigma_s/J):", 1 / (4 * pi * sigma_s))
p("beta_geom = 2 xi^2/a^2", beta_geom)
print("  i.e. R4 DOES reach the number - and reaches it because sigma_s was built out of")
print("  r_oct r_tet in the first place. Inputs asserted: Q=1, d=sqrt(r_tet r_oct), and the")
print("  unit identification. R4: CLOSED as a derivation; SC-DLS-4 if one accepts the three.")
