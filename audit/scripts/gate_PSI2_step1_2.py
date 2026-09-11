#!/usr/bin/env python3
"""
Gate PSI2, Steps 1-2.  Everything is recomputed from App J's own stated
numbers.  No value is imported from any other gate or session.

App J primary text (Appendices Vol.1, App J SS1.1-3.1):
  GP eq          -xi^2 grad^2 Psi + g|Psi|^2 Psi / J = Psi     (everywhere)
  shell          V(r) = sigma_s delta(r-R),  sigma_s = alpha_0 J
  jump condition [d_r Psi]_{R-}^{R+} = -(sigma_s/J) Psi(R)
                 "The field Psi itself is continuous."
  eigenvalue eq  kappa cot(kappa R) = -1/xi + alpha_0 = -0.424083
  printed roots  kappa_n = 3.3905, 9.5139, 15.762   (all labelled A1, s-wave)
  exterior gap   2/xi = 0.8630
  App J action   S[Psi2] = Int [ J (d_mu Psi)^2 + (J/xi^2)(|Psi|^2-Psi0^2)^2/4 ]
"""
from mpmath import mp, mpf, sqrt, pi, cot, tan, findroot, cos, sin, tanh, nstr

mp.dps = 40
P = lambda x, n=12: nstr(x, n)

print("=" * 72)
print("SECTION A -- App J parameters, reconstructed from App J's own text")
print("=" * 72)

r_oct = (sqrt(2) - 1) / 2
r_tet = (sqrt(6) - 2) / 4
alpha0 = r_oct * r_tet / pi
print(f"  r_oct                    = {P(r_oct,16)}")
print(f"  r_tet                    = {P(r_tet,16)}")
print(f"  alpha_0 = r_oct r_tet/pi = {P(alpha0,16)}   (App J prints 0.00740806)")

# App J prints the RHS of its own eigenvalue equation as -0.424083.
# That single printed number fixes xi, because RHS = -1/xi + alpha_0.
rhs_printed = mpf("-0.424083")
inv_xi = alpha0 - rhs_printed
xi = 1 / inv_xi
R = mpf(1) / 2                      # App JH SS2.2: R = (1/2) l_P
print(f"\n  1/xi  (= alpha_0 - RHS)  = {P(inv_xi,12)}")
print(f"  xi                       = {P(xi,12)}")
print(f"  R (App JH SS2.2)         = {P(R,12)}")
print(f"  xi/R                     = {P(xi/R,12)}   (gate SS2 states 4.635)")
print(f"  2/xi  (exterior gap)     = {P(2/xi,12)}   (App J prints 0.8630)")

# Reproduce App J's printed roots to confirm we have the right equation.
f = lambda k: k * cot(k * R) - rhs_printed
print("\n  Roots of  kappa cot(kappa R) = -0.424083   (App J SS2.2 table):")
for guess, printed in [(3.4, "3.3905"), (9.5, "9.5139"), (15.8, "15.762")]:
    k = findroot(f, mpf(guess))
    print(f"     kappa = {P(k,10):>16}   App J prints {printed}")
kappa0 = findroot(f, mpf("3.4"))

print("\n  Consistency: App J's three printed numbers (RHS, 2/xi, kappa_0)")
print("  are mutually consistent to the digits printed. The reconstruction")
print("  of xi is therefore App J's own xi, not an imported value.")

print()
print("=" * 72)
print("SECTION B -- Step 1: is the shell a junction at all?")
print("=" * 72)
# The jump condition is a condition on the LOGARITHMIC derivative of Psi.
# Its natural comparator is the only other inverse length in the problem, 1/xi.
b = alpha0 * xi                     # dimensionless barrier strength sigma_s xi / J
print(f"  logarithmic-derivative jump  sigma_s/J = alpha_0 = {P(alpha0,12)}")
print(f"  condensate's own inverse length   1/xi       = {P(inv_xi,12)}")
print(f"  dimensionless barrier strength    b = alpha_0 xi = {P(b,12)}")
print(f"  ratio (1/xi)/alpha_0                          = {P(inv_xi/alpha0,12)}")
print("""
  A Josephson junction requires b >> 1 (opaque link, two quasi-independent
  phases).  b << 1 is the transparent limit: one condensate, one phase.
  The corpus sits a factor 1/b = %s on the TRANSPARENT side of b = 1.
  Barrier transmission for a delta shell, T = 1/(1 + b^2/4) = %s.
""" % (P(1 / b, 8), P(1 / (1 + b**2 / 4), 12)))
print(f"  Fractional condensate depletion at the shell, O(b) = {P(b*100,4)} %")
print(f"  App J's own overlap factor tanh^2(r_oct/xi)        = "
      f"{P(tanh(r_oct/xi)**2,8)}  (App J prints 0.007944)")

print()
print("=" * 72)
print("SECTION C -- Step 2: constructed relative-phase stiffness and gap")
print("=" * 72)
# Gate SS0.4 permits construction.  Build E_J from App J's own action.
# Phase sector of S[Psi2]:  J rho |grad theta|^2.
# Twist vartheta across the interface, relaxing over length L, area A:
#   E(vartheta) = J rho A vartheta^2 / L   ==>   (E_J/2) vartheta^2
#   ==>  E_J = 2 J rho A / L
J = mpf(1); rho0 = mpf(1)           # App J units: J = 1, Psi0^2 = rho0 = 1
A = 4 * pi * R**2
V = 4 * pi * R**3 / 3
L = xi                              # shortest length over which phase can
                                    # vary without paying condensation energy
E_J = 2 * J * rho0 * A / L
# Charging energy from App J's own quartic (J/xi^2)(|Psi|^2-Psi0^2)^2/4:
#   U = (J/xi^2)(N-N0)^2/(4V)  ==>  E_C = d2U/dN2 = J/(2 xi^2 V)
E_C = J / (2 * xi**2 * V)
gap_plasma = sqrt(E_C * E_J)        # H = (E_C/2)n^2 + (E_J/2)vartheta^2
print(f"  interface area   A = 4 pi R^2   = {P(A,10)}")
print(f"  interior volume  V = 4 pi R^3/3 = {P(V,10)}")
print(f"  twist relaxation length L = xi  = {P(L,10)}")
print(f"\n  E_J = 2 J rho A / L             = {P(E_J,10)}  (Planck units)")
print(f"  E_C = J / (2 xi^2 V)            = {P(E_C,10)}")
print(f"  relative-phase gap sqrt(E_C E_J)= {P(gap_plasma,10)}  m_P c^2")
print(f"\n  App J's own computed interior A1 ground mode kappa_0 = {P(kappa0,10)} m_P c^2")
print(f"  Exterior Higgs gap 2/xi                              = {P(2/xi,10)} m_P c^2")

print()
print("=" * 72)
print("SECTION D -- what a gapped relative phase mediates")
print("=" * 72)
for name, delta in [("constructed plasma gap", gap_plasma),
                    ("App J's kappa_0", kappa0)]:
    lam = 1 / delta
    print(f"  {name:<26} Delta = {P(delta,8):>14} m_P c^2"
          f"   ->  Yukawa range 1/Delta = {P(lam,8)} l_P")
print("""
  A gapped scalar exchanges a Yukawa potential  V(r) ~ -(g^2/4 pi r) e^{-r/lambda},
  not 1/r.  With lambda of order one Planck length the potential is down by
  e^{-r/lambda}; at r = 1 mm that is e^{-6.2e31}.  This fails for a STATED
  reason -- a nonzero gap -- not by analogy with the locked horn.
""")

print("=" * 72)
print("SECTION E -- what the unlocked horn (E_J = 0) would require")
print("=" * 72)
print(f"""  E_J = 0 requires zero transmission across the shell, i.e. b -> infinity.
  The corpus has b = {P(b,8)}.  The unlocked horn is not marginally
  disfavoured; it sits at the opposite end of the barrier axis from where
  App J places the model, by an unbounded factor.  App J's own words --
  "the condensate permeates the object ... a weakly perturbing potential,
  not a hard wall" -- are the statement that b << 1.
""")

print("=" * 72)
print("SECTION F -- App JH SSJH.3.2, eq (14), evaluated")
print("=" * 72)
rhs14 = alpha0 * rho0 * 4 * pi * R**2
print(f"  App JH eq (14):  oint_{{dB^3}} J_Hopf . n dA  =  alpha_0 rho_0 4 pi R^2")
print(f"  RHS = {P(rhs14,12)}   (nonzero)")
print("""  LHS: for ANY stationary configuration the continuity equation gives
  div J = -d(rho)/dt = 0 throughout B^3, so by the divergence theorem
       oint_{dB^3} J . n dA = Int_{B^3} div J d^3r = 0   identically.
  Eq (14) therefore reads  0 = %s.  It has no solutions, and the
  LHS carries no dependence on N_H whatever, so it cannot select N_H = 1
  over N_H = 0.  Separately, LHS and RHS differ dimensionally by one
  power of velocity (hbar/mL).
""" % P(rhs14, 10))

print("=" * 72)
print("SECTION G -- App JH free energy: is the N_H = 1 ground state stable?")
print("=" * 72)
print("""  App JH eq (13):
     F = Int_{B^3} [ (hbar^2/2m)|grad Psi|^2 + (g/2)|Psi|^4 ] d^3r
         + (alpha_0 hbar^2 / 2 m R) oint_{S^2} |Psi|^2 dA

  App JH SS3.1 fixes |Psi_int|^2 = rho_0, constant.  Then:

   (i) the quartic term is (g/2) rho_0^2 V  -- a constant;
  (ii) the surface term is (alpha_0 hbar^2/2mR)(4 pi R^2 rho_0)
       = %s (Planck units, hbar=m=1) -- also a CONSTANT.
       Its variation with respect to the unit field Psi-hat vanishes
       identically, so the term App JH calls "the Josephson coupling"
       has no functional dependence on the configuration it is said to
       select.  It cannot select N_H.
 (iii) the ONLY configuration-dependent term is the sigma-model gradient
       energy E_2 = (hbar^2/2m) Int |grad Psi-hat|^2 rho_0 d^3r.

  Derrick scaling, texture of linear size a inside the fixed ball:
       |grad n-hat|^2 ~ 1/a^2 ,  volume ~ a^3   ==>   E_2(a) ~ a.
  So E_2 -> 0 as a -> 0: the N_H = 1 texture shrinks to a point.  The
  infimum of energy in the N_H = 1 sector is 0 and is not attained.
  There is NO stable hopfion in the free energy App JH actually writes.

  Stabilisation requires a Faddeev-Skyrme quartic-derivative term
       E_4 = kappa_FS Int (d_i n-hat x d_j n-hat)^2 d^3r ,   E_4(a) ~ 1/a,
  balancing at a* = sqrt(kappa_FS / c_2).  kappa_FS is a NEW COUPLING with
  its own dimensions, absent from App J's ingredient list, and it -- not
  alpha_0 -- would set the hopfion size and hence the interior spectrum.
""" % P(alpha0 * 4 * pi * R**2 * rho0 / (2 * R), 10))

print("  Scaling exponents (explicit):")
for term, expo in [("E_2  sigma-model gradient", "+1"),
                   ("E_4  Faddeev-Skyrme quartic", "-1"),
                   ("potential / volume term", "+3")]:
    print(f"     {term:<30} E(a) ~ a^({expo})")
print("""     With E_2 alone the only stationary point is a -> 0.  This is
     Derrick's theorem in the form that applies to a fixed domain.
     Note also: Faddeev-Niemi (cited by App JH as [Hopfion1,Hopfion2] for
     its energy formula) work in the model WITH E_4, and their result is
     the Vakulenko-Kapitanskii scaling E >= c N_H^(3/4), not the linear
     E = N_H eps_0 that App JH asserts.
""")

print("=" * 72)
print("SECTION H -- homotopy: can App J's field carry a Hopf charge?")
print("=" * 72)
print("""  App J's order parameter: one complex scalar with quartic
  (J/xi^2)(|Psi|^2 - Psi0^2)^2/4.  Vacuum manifold M = S^1.
        pi_2(S^1) = 0 ,  pi_3(S^1) = 0.
  Hopf charge is identically zero on App J's field content -- not small,
  zero, for every configuration.  App JH's construction needs a target
  with pi_3 = Z, i.e. S^2, which requires the two-component field.
  The two interiors are therefore not merely different write-ups of one
  object: they are separated by a homotopy invariant.
""")
print("=" * 72)
print("END")
print("=" * 72)
