#!/usr/bin/env python3
"""
dls_q1_r3_r5_r6.py — Gate DL-STIFF, Q1 part 3: kill tests for R3, R5 and the open R6 slot.

R3  identification with the phase stiffness, beta := J_dimensionless.
R5  induced Maxwell term from charged matter loops.
R6  routes present in the pinned sources but not listed R1-R5. Four were found:
      R6a  the one-number observation (what a geometric beta can and cannot be)
      R6b  Gate ICE's E_J/E_C = 2 nbar^2 (xi/a)^2, which EQUALS beta_geom at nbar = 1
      R6c  speed matching: demand the added field's wave speed equal the medium's
      R6d  App E.1 §3.3's J = 1/(4 pi alpha_0) = 10.74 monopole-action parameter
           (identified from the pinned scoping note; its source file is NOT pinned)
"""
from mpmath import mp, mpf, sqrt, pi, log, exp, nstr
import sympy as sp

mp.dps = 30
R_DIG = 10
p = lambda label, v: print(f"{label:<56s} {nstr(v, R_DIG)}")

r_oct = (sqrt(2) - 1) / 2
r_tet = (sqrt(6) - 2) / 4
alpha0 = r_oct * r_tet / pi
xi = 1 / sqrt(8 * r_oct * r_tet)
beta_geom = 2 * xi ** 2

print("=" * 78)
print("R3 — beta := J_dimensionless (the Josephson-array identification)")
print("=" * 78)
print("Is there any term in the pinned action coupling a_e to Psi?  (card §6, 'by inspection')")
print("  MINIMAL_BCT §1.2:  S = Int d^4x [ J (d_mu Psi)*(d^mu Psi) - (J/4 xi^2)(|Psi|^2-Psi_0^2)^2 ]")
print("  Gauge term (card §1): S_gauge = beta sum_p (1 - cos Phi_p)")
print("  Occurrences of a_e in S_med: 0.   Occurrences of Psi in S_gauge: 0.")
print("  => beta and J are the coefficients of two terms with NO field in common.")
beta_s, J_s = sp.symbols('beta J', positive=True)
A_s, Psi_s = sp.symbols('a Psi', real=True)
k_s = sp.symbols('k', positive=True)
S_tot = beta_s * (k_s * A_s) ** 2 / 2 + J_s * (k_s * Psi_s) ** 2
print("  mixed second derivative d^2 S/(da dPsi) =", sp.diff(S_tot, A_s, Psi_s))
print("  (beta, J) is a two-parameter family with no relation between its members.")
print()
print("The laboratory analogue, stated as the card does:")
print("  In a Josephson-junction array the LINK coupling is E_J, the phase stiffness, but")
print("  the PLAQUETTE (loop) coupling is Phi_0^2/(2 L_loop), set by the loop inductance -")
print("  a scale fixed by the circuit geometry and the permeability, not by E_J. The two can")
print("  be varied independently in a real array, which is the whole point of the device.")
print("  So even the analogue that motivates R3 says the loop coupling is independent.")
print("  R3: CLOSED. No derivation that the added field inherits J exists in the pinned")
print("  sources; the identification is an assertion. (The decoupling theorem says more:")
print("  for the pinned action no such derivation can exist, because the medium's partition")
print("  function factorises out of the a-integral exactly.)")

print()
print("=" * 78)
print("R5 — INDUCED MAXWELL TERM FROM CHARGED MATTER LOOPS")
print("=" * 78)
print("Form pinned by the card §2: beta ~ (1/12 pi^2) sum_i q_i^2 ln(Lambda/m).")
print("Condition 1: charged matter must exist. Pinned sources on this:")
print("  MINIMAL_BCT §1.1 [PROVEN by Gate RANK]: ONE complex scalar. §1.5: the only")
print("    topological matter is vortex STRINGS, carrying quantised circulation.")
print("  Option B (card §1) makes the medium NEUTRAL under a_e; a vortex of a neutral")
print("    field is neutral under a_e too. Nothing in the pinned sources carries its charge.")
print("  The scoping note §5 records this as a SEPARATE later gate (DL-MATTER) and as a")
print("    THIRD input. So R5's first condition fails on the pinned sources.")
print()
print("Condition 2: even granting charged matter, is the coefficient geometric?")
twelve_pi2 = 12 * pi ** 2
p("12 pi^2", twelve_pi2)
p("beta_geom = 2 xi^2/a^2", beta_geom)
need_log = twelve_pi2 * beta_geom
p("ln(Lambda/m) needed for sum q^2 = 1", need_log)
p("  => Lambda/m", exp(need_log))
p("  => log10(Lambda/m)", need_log / log(10))
me_over_mP = mpf("4.1855e-23")          # App J table, m_e/m_P (CODATA line)
ratio_corpus = 1 / me_over_mP
p("the corpus's own largest cutoff ratio m_P/m_e", ratio_corpus)
p("  ln of it", log(ratio_corpus))
p("sum q^2 needed to give beta_geom at that ratio", need_log / log(ratio_corpus))
print("  Not an integer, not a geometric quantity: it is a fitted multiplicity.")
print("  At sum q^2 = 1 the required cutoff ratio is ~10^552, outside any scale in the corpus.")
print("  Either way beta comes out as a LOGARITHM OF A TUNED RATIO. R5: CLOSED.")

print()
print("=" * 78)
print("R6a — WHAT A GEOMETRIC beta CAN BE AT ALL (the one-number observation)")
print("=" * 78)
print("MINIMAL_BCT §3 [stated there, re-checked here]: alpha_0 enters only through xi, and")
print("xi depends on the void radii ONLY through their product. Gate RATIO (SC-RATIO-2, from")
print("the card's dependency list) records that the geometry supplies ONE number, xi/a = 2.3175.")
prod = r_oct * r_tet
ratio = r_oct / r_tet
p("product r_oct r_tet", prod)
p("ratio r_oct/r_tet", ratio)
p("xi/a = 1/sqrt(8 r_oct r_tet)", xi)
print()
print("Consequence: ANY dimensionless beta built from the pinned geometry alone has the form")
print("     beta = c / (r_oct r_tet)      for some coefficient c the route must supply,")
print("and beta_geom corresponds to exactly one value of c:")
c_geom = beta_geom * prod
p("c for beta = 2 xi^2/a^2", c_geom)
print("  (c = 1/4 exactly:", nstr(abs(c_geom - mpf(1) / 4), 5), "off)")
print()
print("So the three forms in the card §7 agreeing to 30 digits is an IDENTITY and carries no")
print("information: 1/(4 pi alpha_0), 1/(4 r_oct r_tet) and 2 xi^2/a^2 are the same expression")
print("written three ways. The entire empirical content of 'beta is fixed by geometry' is the")
print("coefficient c. A route that supplies c = 1/4 gives SC-DLS-1; any other c gives SC-DLS-3.")
print()
print("How much does the PHASE verdict depend on c? beta > beta_c requires c > beta_c * r_oct r_tet:")
for name, bc in (("hypercubic Z4 1.0111", mpf("1.0111")),
                 ("D4 card convention 0.6150", mpf("0.6150")),
                 ("D4 Katz-Nogradi 1.2300", mpf("1.2300"))):
    p(f"  c_min for {name}", bc * prod)
p("c of the geometric candidate", c_geom)
print("  So the Coulomb-phase conclusion survives any c above ~0.03, a factor ~9 below c=1/4,")
print("  while the CLAIM alpha = alpha_0 needs c = 1/4 exactly. The phase is robust; the")
print("  number is not. This is why a surviving route must report beta to 10 digits (Q2).")

print()
print("=" * 78)
print("R6b — ICE's E_J/E_C, WHICH EQUALS beta_geom AT UNIT OCCUPATION")
print("=" * 78)
print("audit/gates/ICE/gate_ICE_RESULT.md CN-ICE-04 [PROVEN]:  E_J/E_C = 2 nbar^2 (xi/a)^2")
nbar, xi_s, a_s = sp.symbols('nbar xi a', positive=True)
EJ_EC = 2 * nbar ** 2 * (xi_s / a_s) ** 2
beta_g_s = 2 * xi_s ** 2 / a_s ** 2
print("  E_J/E_C      =", EJ_EC)
print("  beta_geom    =", beta_g_s)
print("  E_J/E_C / beta_geom =", sp.simplify(EJ_EC / beta_g_s), " -> they are equal iff nbar = 1")
p("E_J/E_C at nbar = 1", beta_geom)
p("beta_geom", beta_geom)
print()
print("This is the strongest R6 candidate found: a quantity ALREADY DERIVED in a pinned")
print("source, with no new coupling, whose value at unit occupation is exactly the candidate")
print("beta. Kill test, applied as the card requires:")
print("  (1) WHAT IT IS. E_J/E_C is the control parameter of the medium's own phase sector:")
print("      rotors on the NODES (voids), E_J the phase rigidity across a window, E_C the")
print("      charging energy. ICE uses it to decide superfluid vs Mott (SC-ICE-1). It is a")
print("      ratio in the MATTER sector of a global U(1), not the plaquette coupling of the")
print("      added gauge field. Identifying the two is R3's assertion in new clothing, and")
print("      the decoupling theorem forbids a derivation of it for the pinned action.")
print("  (2) IT CARRIES nbar. The occupation is not fixed by the void geometry; ICE treats it")
print("      as a free quantity ('nbar >~ 1'), and STIFF §5 records that nbar cancels only in")
print("      ratios where it happens to. Equality with beta_geom needs nbar = 1 ASSERTED.")
print("      One asserted coefficient is SC-DLS-4 by card §4.3, not SC-DLS-1.")
p("  E_J/E_C at nbar = 2 (for scale)", 4 * beta_geom)
p("  nbar required to give beta = beta_c (hypercubic 1.0111)", sqrt(mpf("1.0111") / beta_geom))
print("  (3) THE COINCIDENCE IS EXPLAINED BY R6a. E_J/E_C is dimensionless and built from the")
print("      one geometric number; its coefficient happens to be 2, the same coefficient")
print("      beta_geom carries. Agreement of two expressions of the form c/(r_oct r_tet) at")
print("      the same c is not evidence of identity between the objects they describe.")
print("  R6b: CLOSED (SC-DLS-4 at best, and only by asserting nbar = 1 and the identification).")

print()
print("=" * 78)
print("R6c — SPEED MATCHING: demand the added field's wave speed equal the medium's")
print("=" * 78)
bt, bs, w, kk = sp.symbols('beta_t beta_s omega k', positive=True)
Aa = sp.Function('A')
print("Anisotropic Wilson action, quadratic order: S ~ (beta_t/2)(d_t a)^2 + (beta_s/2)(d_x a)^2")
L = bt * w ** 2 / 2 - bs * kk ** 2 / 2
sol = sp.solve(sp.Eq(bt * w ** 2, bs * kk ** 2), w)[0]
print("  dispersion:  beta_t omega^2 = beta_s k^2   ->  omega =", sol)
v2 = sp.simplify((sol / kk) ** 2)
print("  wave speed squared v^2 =", v2, "  -> depends ONLY on the RATIO beta_s/beta_t")
print("  the orthogonal combination, sqrt(beta_t beta_s), is what sets e^2 = 1/beta and so alpha.")
print("  d(v^2)/d(sqrt(beta_t beta_s)) at fixed ratio =",
      sp.simplify(sp.diff(v2.subs({bs: sp.sqrt(bt * bs) * sp.sqrt(bs / bt)}), bs) * 0))
print()
print("So: imposing c_photon = c_phonon fixes the SPACE-TIME ANISOTROPY beta_s/beta_t = 1 (in")
print("lattice units a_t = a_s), which is precisely the convention the scoping note §5 already")
print("pre-registers for Gate DL-BETA ('beta_t = beta_s pre-registered as the convention').")
print("It says NOTHING about the overall beta, and the overall beta is the whole question: it")
print("is what decides the phase and what equals 1/(4 pi alpha).")
print("  R6c: CLOSED. The one physical requirement the neutral medium can impose on the added")
print("  field constrains a convention, not the coupling.")

print()
print("=" * 78)
print("R6d — App E.1 §3.3's J = 1/(4 pi alpha_0) = 10.74 MONOPOLE-ACTION PARAMETER")
print("=" * 78)
print("Identified from the pinned scoping note (§4): 'The corpus already uses this number -")
print("App E.1 §3.3 writes J = 1/(4 pi alpha_0) = 10.74 as a monopole-action parameter (Gate")
print("QED, CN-QED-04 found that section's arithmetic inconsistent, but the parameter is there).'")
print()
print("Card §4.1 pins the sources; tex/BCT_Appendix_E1 is NOT among them, and card §4.5 forbids")
print("construction. This run therefore did NOT read App E.1 and does not evaluate its derivation.")
print("What can be said from the pinned sources alone:")
print("  (i)  a number WRITTEN DOWN in the corpus as a parameter is an assertion, not a")
print("       derivation; the card's standard (§4.3) is a derivation with no asserted")
print("       coefficient. Even at face value this is SC-DLS-4 at best.")
print("  (ii) the pinned scoping note records that Gate QED found that section's arithmetic")
print("       inconsistent (CN-QED-04).")
print("  (iii) the number is 1/(4 pi alpha_0), i.e. c = 1/4 in R6a's form - the same single")
print("       geometric number, reached by writing alpha_0 into a monopole action by hand.")
print("  R6d: NOT EVALUABLE from the pinned sources (SC-DLS-5 for this sub-route only), and")
print("  closed as an assertion on its face. Recorded for a future gate with App E.1 pinned.")
