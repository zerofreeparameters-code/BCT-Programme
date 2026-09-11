#!/usr/bin/env python3
"""
Two questions, from Appendix KA4 and Appendix JH S3.4.

Q1. Can |H| <= n be proved?  KA4's own proof is vacuous (alpha_0 cancels).
    Is there a route that works, and what are the genuine bounds?

Q2. "Changing the Hopf charge requires a nodal surface, which costs infinite
    energy in the superfluid."  Is that true?  If not, what does it cost?

All numbers in Planck units: hbar = c = m = l_P = 1, rho_0 = 1.
"""
from mpmath import mp, mpf, sqrt, pi, log, tanh, nstr, exp

mp.dps = 30
P = lambda x, n=8: nstr(x, n)

r_oct = (sqrt(2) - 1) / 2
r_tet = (sqrt(6) - 2) / 4
a0 = r_oct * r_tet / pi
R = mpf(1) / 2
xi = 1 / sqrt(8 * pi * a0)
rho0 = mpf(1)

print("=" * 74)
print("PART A -- geometry, for reference")
print("=" * 74)
print(f"  alpha_0 = {P(a0,10)}   R = {P(R)}   xi = {P(xi,10)}   xi/R = {P(xi/R,8)}")
print(f"""
  NOTE, and it matters for Q2: xi > R.  The healing length is {P(xi/R,5)} times
  the sphere radius.  A vortex core in this medium is {P(2*xi/(2*R),5)}x wider than
  the whole sphere.  There is no room inside a BCT sphere for a localised
  nodal structure: the sphere fits inside a single core.
""")

print("=" * 74)
print("PART B -- Q1: is |H| <= n provable?")
print("=" * 74)
print("""
B1. What KA4 actually argues, restated:
      a Hopf excitation of charge H "requires phase winding" H * 2*pi*alpha_0
      the n-th mode "can sustain phase winding up to"   n * 2*pi*alpha_0
      therefore H <= n.

    alpha_0 and 2*pi appear identically on both sides and cancel.  The
    argument is  (H * k) <= (n * k)  =>  H <= n,  for ANY k != 0.  It is
    true for k = alpha_0 and equally true for k = 1, k = 137, k = pi^5/6.
    No property of alpha_0, of the Josephson coupling, or of the Bessel
    spectrum enters.  Whatever the theorem rests on, it is not this.

B2. Both premises are unsourced, and the second is the load-bearing one.
    "The mode can sustain phase winding up to 2*pi*n*alpha_0 without
    exceeding the Josephson energy barrier" is stated, not derived.  Note
    its FORM: it is an ENERGETIC statement (a barrier is exceeded), but
    KA4 S4 then insists the constraint is TOPOLOGICAL and therefore
    admits no exceptions.  A barrier argument cannot deliver a homotopy
    obstruction.  The two halves of KA4 contradict each other in kind.

B3. Is there a genuine bound of this shape anywhere?  The nearest true
    statement is the Vakulenko-Kapitanskii bound for the Faddeev-Skyrme
    model:
""")
print("      E  >=  c * |H|^(3/4)      =>      |H|  <=  (E/c)^(4/3)")
print("""
    Three differences from KA4's claim, each fatal to it as stated:
      (i)   it is ENERGETIC, not topological -- it bounds H at fixed
            energy, and says nothing about what is reachable by smooth
            deformation;
      (ii)  the exponent is 3/4, so H grows as E^(4/3), NOT linearly in a
            mode index;
      (iii) it requires the quartic Faddeev-Skyrme term, which the BCT
            corpus does not contain anywhere (established separately).

B4. Does the Bessel index even constrain H?  KA4 indexes modes by
    j_n(kappa_0 r/R), i.e. by ANGULAR MOMENTUM n, not by radial node count.
    The Hopf charge of a two-component field is fixed by the phase/angular
    structure of the map to S^2, not by its radial profile.  Standard
    axially symmetric hopfions carry H = m * p with m the toroidal and p
    the poloidal winding.

    A field whose angular content is bounded by l <= n has azimuthal
    quantum numbers |m| <= n, so the RELATIVE azimuthal winding between
    the two components can reach |m_+ - m_-| = 2n.  With poloidal winding
    p that gives H up to 2*n*p, not n.

    So even the most sympathetic reading of "n-th mode" gives a bound of
    the wrong FORM.  |H| <= n is not recovered.
""")
print("  Candidate counterexample to |H| <= n at n = 1 (sketch, NOT verified):")
print("     psi_+ ~ Y(1,+1) ~ sin(theta) e^{+i phi},  psi_- ~ Y(1,-1) ~ sin(theta) e^{-i phi}")
print("     relative azimuthal winding = 2; with poloidal winding 1 this is H = 2")
print("     inside an l = 1 mode.  If that configuration is smooth and")
print("     normalisable, |H| <= n is FALSE at n = 1.")
print("     -> flagged for proper verification; NOT claimed here.")

print()
print("=" * 74)
print("PART C -- Q2: what does changing the Hopf charge actually cost?")
print("=" * 74)
print("""
C1. "Nodal surface" is the wrong object.
    Zeros of a single complex field in 3D are generically LINES
    (codimension 2: Re = 0 and Im = 0).  Surfaces of zeros are
    non-generic and unstable to perturbation.
    For a TWO-component field (App JH's Psi_int : B^3 -> C^2), |Psi|^2 = 0
    needs FOUR real conditions in three dimensions -- codimension 4,
    generically EMPTY.  And App JH S3.1 fixes |Psi_int|^2 = rho_0 exactly,
    so its own field can never have a node anywhere, of any dimension.
    The mechanism S3.4 invokes cannot occur in the theory S3.1 defines.

C2. Even for a genuine GP vortex, the energy is finite.
    Energy per unit length of a singly quantised vortex line:
        E/L = pi * rho_0 * (hbar^2/m) * ln(b/xi)
""")
for b, lbl in [(R, "b = R (sphere)"), (2 * R, "b = 2R (unit cell)"), (10 * R, "b = 10R")]:
    EL = pi * rho0 * log(b / xi)
    print(f"     {lbl:20s} ln(b/xi) = {P(log(b/xi),6):>12}   E/L = {P(EL,6):>12} m_P c^2 / l_P")
print("""
     All finite.  Note the first two are NEGATIVE, which is the formula
     telling us b < xi: the core is larger than the region.  The physical
     reading is that a vortex cannot be localised inside a BCT sphere at
     all, and the relevant energy scale is set by the core, not by a
     logarithm.  Core energy over the sphere:
""")
E_core = pi * rho0 * (2 * R)
print(f"     E_core ~ pi * rho_0 * (2R) = {P(E_core,6)} m_P c^2   -- Planck scale, FINITE")

print("""
C3. The decisive point, and it comes from App JH's own free energy.
    With |Psi_int|^2 = rho_0 fixed and the surface term constant, the only
    configuration-dependent term is the sigma-model gradient energy.  For a
    texture of linear size a:  E_2(a) ~ a.
""")
for a in [mpf('0.5'), mpf('0.1'), mpf('0.01'), mpf('0.001')]:
    print(f"     texture size a = {P(a,4):>8}   E_2 proportional to a = {P(a,4):>8}")
print("""     E_2(a) -> 0 as a -> 0.  The H = 1 texture SHRINKS TO A POINT and
     the charge is lost at the singular point, at energy tending to ZERO.

     So the barrier to changing the Hopf charge in App JH's written free
     energy is not infinite.  It is zero.  This is Derrick's theorem, and
     it is the exact opposite of what S3.4 claims.

C4. Where a finite barrier WOULD come from.
     Adding the Faddeev-Skyrme quartic E_4 ~ 1/a stabilises the size at
     a* = sqrt(kappa_FS / c_2) and makes hopfion transitions cost a FINITE
     barrier -- which is what is seen numerically in Faddeev-Skyrme
     simulations.  Finite, not infinite.  And kappa_FS is a new coupling
     the corpus does not have.
""")

print("=" * 74)
print("SUMMARY")
print("=" * 74)
print("""
  Q1  |H| <= n :  NOT PROVED, and not provable by KA4's argument, which is
      an identity in disguise.  The nearest genuine bound (VK) is energetic,
      has exponent 3/4, and needs a term the corpus lacks.  A sympathetic
      reading of the Bessel index gives a bound of the form 2*n*p, not n.
      Status: OPEN, leaning FALSE.  A counterexample at n = 1 is sketched
      and needs verification before the claim can be retired.

  Q2  "infinite energy" :  FALSE, three times over.
      (a) the nodal object invoked cannot exist in the field App JH defines
          (|Psi| is fixed and nonzero everywhere);
      (b) real GP vortices cost finite energy, and in this geometry cannot
          be localised inside a sphere at all, since xi > R;
      (c) in App JH's OWN free energy the barrier is not infinite but ZERO,
          by Derrick collapse.
      The claim is not merely unsupported; the document that makes it
      contains its own refutation two sections earlier.
""")
