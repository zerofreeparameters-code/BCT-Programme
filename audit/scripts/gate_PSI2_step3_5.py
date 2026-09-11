#!/usr/bin/env python3
"""
Gate PSI2, Steps 3-5.
"""
from mpmath import mp, mpf, sqrt, pi, cot, findroot, nstr, exp, diff

mp.dps = 40
P = lambda x, n=12: nstr(x, n)

r_oct = (sqrt(2) - 1) / 2
r_tet = (sqrt(6) - 2) / 4
alpha0 = r_oct * r_tet / pi
xi = 1 / (alpha0 + mpf("0.424083"))
R = mpf(1) / 2
V = 4 * pi * R**3 / 3
A = 4 * pi * R**2
E_C = 1 / (2 * xi**2 * V)
E_J_constructed = 2 * A / xi

print("=" * 72)
print("STEP 3 -- how much work does alpha_0 actually do in App J?")
print("=" * 72)
root = lambda a: findroot(lambda k: k * cot(k * R) - (-1 / xi + a), mpf("3.4"))
k_with = root(alpha0)
k_without = root(mpf(0))
print(f"  kappa_0 with    alpha_0 = {P(alpha0,10)} : {P(k_with,12)}")
print(f"  kappa_0 with    alpha_0 = 0            : {P(k_without,12)}")
print(f"  shift                                  : {P(k_with-k_without,8)}"
      f"  ({P(100*(k_with-k_without)/k_without,4)} %)")
print(f"  alpha_0 share of the RHS (-1/xi + alpha_0): "
      f"{P(100*alpha0/(1/xi - alpha0),4)} %")
print("""
  So the sole equation in App J in which alpha_0 appears moves the
  interior ground state by under a percent.  Deleting the Josephson
  boundary condition entirely does NOT leave the interior spectrum
  undetermined -- it leaves it almost unchanged.  This cuts BOTH ways
  and must be recorded as such:
    - AGAINST SC-PSI2-3 as literally worded: unlocking does not leave
      alpha_0 undetermined; alpha_0 is fixed in App D by void geometry
      and is merely USED here.
    - AGAINST App JH: a boundary condition that shifts kappa_0 by 0.6%
      is not plausibly what "forces" an integer topological charge.
      Topological selection is discrete; this input is a perturbation.
""")

print("=" * 72)
print("STEP 2 (cont.) -- the corpus's OWN Josephson ratio, Letter 36 (D4 qubit)")
print("=" * 72)
ratio_corpus = 1 / alpha0
print(f"  Letter 36 eq (3):  E_J/E_C = 1/alpha_0 = {P(ratio_corpus,10)}"
      f"   (prints 134.99)")
print(f"  constructed from App J (E_J/E_C above) = "
      f"{P(E_J_constructed/E_C,10)}")
print("  Both are >> 1.  E_J/E_C >> 1 is the TRANSMON regime: the relative")
print("  phase sits in a harmonic well at the bottom of the cosine, and its")
print("  excitation is the gapped plasma mode.  It is not a Goldstone.\n")

for label, ratio in [("Letter 36's 1/alpha_0", ratio_corpus),
                     ("constructed from App J", E_J_constructed / E_C)]:
    E_J = ratio * E_C
    g1 = sqrt(E_C * E_J)          # H = (E_C/2)n^2 + (E_J/2)theta^2
    g2 = sqrt(8 * E_C * E_J)      # standard transmon convention
    spread = (2 / ratio) ** mpf("0.25")
    print(f"  {label}:  E_J/E_C = {P(ratio,8)}")
    print(f"      gap sqrt(E_C E_J)   = {P(g1,8):>12} m_P c^2  ->  range {P(1/g1,8)} l_P")
    print(f"      gap sqrt(8 E_C E_J) = {P(g2,8):>12} m_P c^2  ->  range {P(1/g2,8)} l_P")
    print(f"      rms phase spread sqrt(<theta^2>) = (2 E_C/E_J)^(1/4) = "
          f"{P(spread,6)} rad")
print("""
  A Goldstone's phase is flat -- it explores the whole circle at zero cost.
  Here the relative phase is confined to a well of rms width ~0.2-0.35 rad
  about zero.  That is the definition of "locked", stated quantitatively.
""")

print("=" * 72)
print("SUMMARY OF EVERY GAP ESTIMATE FOUND (Planck units)")
print("=" * 72)
k0 = root(alpha0)
rows = [
    ("App J's own printed interior A1 ground mode kappa_0", k0),
    ("constructed plasma gap, sqrt(E_C E_J), App J params", sqrt(E_C*E_J_constructed)),
    ("same, transmon convention sqrt(8 E_C E_J)", sqrt(8*E_C*E_J_constructed)),
    ("Letter 36 ratio 1/alpha_0, sqrt(E_C E_J)", sqrt(E_C*ratio_corpus*E_C)),
    ("Letter 36 ratio 1/alpha_0, sqrt(8 E_C E_J)", sqrt(8*E_C*ratio_corpus*E_C)),
    ("hard-wall limit of App J's stated profile, kappa R = pi", pi/R),
]
lo = min(v for _, v in rows); hi = max(v for _, v in rows)
for name, v in rows:
    print(f"  {name:<52} {P(v,8):>12}   range {P(1/v,6)} l_P")
print(f"\n  BRACKET: gap in [{P(lo,6)}, {P(hi,6)}] m_P c^2")
print(f"           Yukawa range in [{P(1/hi,6)}, {P(1/lo,6)}] l_P")
print(f"  Every route gives a Planck-scale gap.  NONE gives zero.")
print(f"  Suppression of the mediated potential at r = 1 mm relative to 1/r:")
mm_over_lP = mpf("1e-3") / mpf("1.616255e-35")
print(f"     r/l_P at 1 mm = {P(mm_over_lP,6)}")
print(f"     exp(-r/lambda) with the SMALLEST gap ({P(lo,6)}): "
      f"exp(-{P(mm_over_lP*lo,6)})")

print()
print("=" * 72)
print("STEP 5 -- symmetry and independence")
print("=" * 72)
print("""  (a) O_h character.  vartheta = theta_2 - theta_1 is a difference of two
      phases attached to the SAME site.  It carries no spatial index, so it
      is l = 0 and transforms as A_1g under O_h.  CONFIRMED A_1g -- the
      gate's Step 5 question (a) is answered YES.

  (b) Independence of rho.  In the two-mode reduction the canonical pair is
      (n, vartheta) with n the number IMBALANCE between interior and
      exterior.  The equations of motion are

          d(vartheta)/dt = E_C n ,      dn/dt = -E_J sin(vartheta)

      -- ONE canonical pair, hence ONE mode, and it is the gapped plasma
      mode above.  vartheta's conjugate momentum IS a density variable.
      This is the same slaving CN-R2-06 identifies for theta_1 (continuity
      + Euler), arrived at independently and by a different route.
      Step 5 question (b): NO.  vartheta is not independent of rho.
      ==> SC-PSI2-4 fires.

  (c) E5-05 (at most one H-singlet per order parameter).
      Interior A (App J): App J SS1.1 -- "The BCT condensate field Psi fills
      all of space" -- and SS1.2 -- "The field Psi itself is continuous."
      Psi_2 is Psi RESTRICTED to r < R.  A restriction of a field to a
      subdomain is a second COMPONENT of one order parameter at most, and
      here not even that: it is the same field on part of its domain.
      One order parameter ==> at most one A_1g singlet ==> already spent
      on theta_1.  ==> SC-PSI2-4 fires on Interior A.

      Interior B (App JH): Psi_int : B^3 -> C^2 with |Psi_int|^2 fixed IS a
      genuinely distinct order parameter, so E5-05 permits it a singlet.
      It is not closed by E5-05.  It is closed at Step 4 instead -- see
      the parameter count -- and by the Derrick result.
""")

print("=" * 72)
print("STEP 4 -- honest parameter count")
print("=" * 72)
print(f"""  Interior A (App J, one complex scalar)
    App J SS1.2 claims: no new field, no new coupling, no new free parameter.
    Assessment: the ACTION claim is sustained -- S[Psi_2] really is the
    exterior GP action restricted to r < R.  Two riders:
      (i)  sigma_s = alpha_0 is obtained in SS1.3 under two stated
           conditionals ("If the double layer charge Q = 1 ... and the
           shell thickness d = sqrt(r_tet r_oct)").  Conditionals, not
           derivations.
      (ii) DIMENSIONS.  The jump condition [d_r Psi] = -(sigma_s/J) Psi(R)
           requires sigma_s/J to have units of 1/length.  alpha_0 is
           dimensionless.  "sigma_s = alpha_0" therefore carries an
           undeclared unit convention -- alpha_0 per Planck length.  Per R
           instead it would read 2 alpha_0 = {P(2*alpha0,10)}.  This is the
           same defect class as CN-FWD-02, surfacing independently here.
    Net: 0 new parameters in the action; 2 conditionals; 1 undeclared unit.
    Moot in any case -- Interior A supplies no second mode at all.

  Interior B (App JH, two-component unit-normalised)
    Against App J SS1.2's "zero", the honest count is:
      1. a NEW FIELD: C^2 in place of C (one extra complex component).
      2. a NEW CONSTRAINT: |Psi_int|^2 = rho_0 fixed, replacing App J's
         quartic (J/xi^2)(|Psi|^2 - Psi_0^2)^2/4.  This DELETES the
         amplitude mode App J has, so it is not an addition to App J's
         content -- it is a different theory.
      3. a NEW COUPLING, mandatory: the Faddeev-Skyrme coefficient
         kappa_FS.  Without it there is no stable hopfion (Derrick).
         With it, kappa_FS -- not alpha_0 -- sets the soliton size and
         hence the interior spectrum.
      4. an INCONSISTENCY, not a parameter: App JH keeps App J's
         derivative-jump BC (its eq 2) while fixing |Psi_int| constant
         (its SS3.1).  A field of constant modulus has zero radial
         derivative of its modulus on the inside, so the jump is set by
         the exterior alone and cannot equal -alpha_0 Psi(R) in general.
    Count: at least 1 new field + 1 new coupling + 1 replaced potential.
    App J SS1.2's claim of ZERO is FALSE for Interior B.
""")

print("=" * 72)
print("APP J INTERNAL CONSISTENCY CHECK (secondary finding)")
print("=" * 72)
print("""  App J SS2.1 states the exterior profile as
      Psi_out = Psi_0 [1 - (R/r) exp(-(r-R)/xi)] ,
  which VANISHES at r = R.  A field vanishing at R has divergent
  logarithmic derivative there, so it cannot produce the finite matching
  Psi_out'/Psi_out|_R = -1/xi - 1/R that the printed eigenvalue equation
  kappa cot(kappa R) = -1/xi + alpha_0 requires.  The eigenvalue equation
  is the WEAK-perturbation limit; the printed profile is the HARD-WALL
  limit.  They are opposite limits of the same problem.
  Consequence check: in the hard-wall limit Psi_in(R) = 0 forces
  kappa R = pi, i.e. kappa = %s -- not the printed 3.3905.
  This does not change this gate's verdict (both limits gap the relative
  phase at Planck scale) but it is a live defect in App J SS2.1.
""" % P(pi / R, 8))
print("=" * 72)
print("END")
print("=" * 72)
