#!/usr/bin/env python3
"""
dls_q1_factorisation.py — Gate DL-STIFF, Q1 part 1: the decoupling theorem that
closes R1/R2/R3/R5 at the level of the pinned action, and the R1 kill test.

Pinned action (card §1, from audit/MINIMAL_BCT.md §1.2 + the Wilson gauge term):

    S[a, Psi] = S_gauge[a] + S_med[Psi]
    S_gauge   = beta * sum_p (1 - cos Phi_p)                        (Wilson, beta = 1/e^2)
    S_med     = int d^4x [ J (d_mu Psi)* (d^mu Psi) - (J/4 xi^2) (|Psi|^2 - Psi_0^2)^2 ]

Option B of the scoping note: the superfluid is NEUTRAL under a_e. That neutrality is
exactly what spares the photon the Meissner mass (Gate DL, CN-DL-02).

Part A. THE DECOUPLING THEOREM. If S_med has no a-dependence, the partition function
factorises and the medium contributes NOTHING to the effective action for a. Shown here
on an exactly-doable toy of the same structure (Gaussian medium, compact link variable
replaced by its quadratic expansion), symbolically, with the a-dependence tracked.

Part B. R1 kill test: minimal coupling (the only way to make S_med depend on a at
zeroth order in derivatives of a) gives the Meissner mass m_A^2 = q^2 rho_s != 0.
Reproduces audit/gates/DL/gate_DL_step1_mass.py cold.

Part C. the operator census: which gauge-invariant Psi-a couplings could evade Part A,
and what each costs.
"""
import sympy as sp

print("=" * 78)
print("PART A — THE DECOUPLING THEOREM (the load-bearing step of this gate)")
print("=" * 78)

# Toy with the SAME structure as the pinned action: one gauge mode a, one medium mode s.
a, s, beta, J, q, rho_s, Lam = sp.symbols('a s beta J q rho_s Lambda', positive=True)
A, S_ = sp.symbols('A s', real=True)

# S_gauge: quadratic expansion of beta*(1 - cos Phi) about Phi = 0, Phi = (lattice curl) ~ k*a
k = sp.symbols('k', positive=True)
Phi = k * A
S_gauge = beta * (1 - sp.cos(Phi))
S_gauge_q = sp.series(S_gauge, A, 0, 4).removeO()
print("S_gauge = beta (1 - cos(k a))            ->  quadratic:", sp.simplify(S_gauge_q))

# S_med for the NEUTRAL medium: no a anywhere (this IS option B's defining property)
S_med_neutral = J * (k * S_) ** 2 / 2 + J / (4) * S_ ** 4
print("S_med (neutral)                          =", S_med_neutral)
print("  d S_med / d a  =", sp.diff(S_med_neutral, A), "   <-- zero: no a-dependence at all")
print("  mixed Hessian block  d^2 S / da ds  =", sp.diff(S_gauge_q + S_med_neutral, A, S_))

# The factorisation, done explicitly as a Gaussian integral over the medium mode.
# Z = Int da Int ds exp(-S_gauge(a) - S_med(s)).  Keep S_med Gaussian so it is exactly doable.
S_med_gauss = J * k ** 2 * S_ ** 2 / 2
Z_med = sp.integrate(sp.exp(-S_med_gauss), (S_, -sp.oo, sp.oo))
print("\nIntegrating the medium out exactly (Gaussian case):")
print("  Z_med = Int ds exp(-S_med) =", sp.simplify(Z_med))
print("  d Z_med / d a =", sp.diff(sp.simplify(Z_med), A))
Gamma_eff = -sp.log(sp.simplify(Z_med))
print("  induced effective action for a:  Gamma_eff = -ln Z_med =", sp.simplify(Gamma_eff))
print("  d Gamma_eff / d a =", sp.diff(Gamma_eff, A),
      "  -> the medium induces NO a-dependent term")
print("\n  => beta_effective = beta_bare EXACTLY. For the pinned action the medium cannot")
print("     renormalise beta, let alone fix it. beta is an input of S_gauge and nothing else.")
print("     This closes R2, R3 and R5-without-added-charged-matter in one step:")
print("       R2: an induced Maxwell term requires a Psi-a coupling; there is none.")
print("       R3: beta and J are independent coefficients of two decoupled terms.")
print("       R5: a matter loop requires matter charged under a; the medium is not.")

print()
print("--- Does the Gauss-law constraint evade the factorisation? ---")
print("The card §1 imposes Gauss's law at the nodes. That constraint reads div E = rho, where rho")
print("is the charge density of whatever is charged under a_e. With the medium NEUTRAL (option B)")
print("the medium contributes rho = 0 identically, so the constraint is a condition on the gauge")
print("sector alone and the factorisation is untouched. The constraint becomes a coupling only")
print("when something carries charge - which is Gate DL-MATTER's separate input, and which for the")
print("medium itself is R1 (Meissner mass, Part B). So the one structural element of the")
print("construction that touches the nodes does not connect the medium to beta either.")

print()
print("=" * 78)
print("PART B — R1 KILL TEST: minimal coupling gives the Meissner mass")
print("=" * 78)
phi0, dth = sp.symbols('phi0 dtheta', real=True)
L_charged = sp.expand(phi0 ** 2 * (dth - q * A) ** 2)
m2_charged = sp.diff(L_charged.subs(dth, 0), A, 2) / 2
print("CHARGED medium  |(d - i q a)Psi|^2  ->  L =", L_charged)
print("  photon mass^2 (unitary gauge) = (1/2) d^2L/da^2 =", sp.simplify(m2_charged))
print("  = q^2 rho_s, NONZERO for q != 0  ->  Meissner/London mass (Gate LINK's fate).")
print("  A charged medium is not the neutral medium of option B: R1 CONTRADICTS the")
print("  construction it is meant to serve. Route closed by the card's own kill test.")
print("\n  Note the structural tension this exposes, which is the finding of the gate:")
print("  q != 0 is the ONLY way to make the medium's action depend on a without adding a")
print("  new coupling, and it is exactly the thing that gaps the photon. Neutrality buys")
print("  masslessness (CN-DL-02) and pays for it with beta.")

print()
print("=" * 78)
print("PART C — OPERATOR CENSUS: what could evade Part A, and what it costs")
print("=" * 78)
chi, c1, c2 = sp.symbols('chi c1 c2', real=True)
rows = [
    ("|(d - i q a)Psi|^2", "q != 0", "R1: Meissner mass q^2 rho_s != 0; not option B's medium"),
    ("-P . E  (dipole, linear)", "P != 0", "STIFF SC-STIFF-5 / CN-STIFF-01: P = 0 by symmetry"),
    ("(chi/2) E^2  (polarisation)", "chi != 0", "R2: chi = dP/dE = 0 when P == 0; and chi is a NEW coupling"),
    ("c1 |Psi|^2 F_{mu nu} F^{mu nu}", "c1 != 0", "absent from the pinned action; c1 is a new input (card 4.5 forbids)"),
    ("c2 |Psi|^4 F^2 , higher dim", "c2 != 0", "same: absent, and a new input"),
]
print(f"{'operator':<32s} {'needs':<10s} {'status'}")
print("-" * 78)
for op, need, st in rows:
    print(f"{op:<32s} {need:<10s} {st}")
print("-" * 78)
print("Every operator that would let the medium talk to a_e is either absent from the")
print("pinned action or carries its own coefficient. A route through one of them is a")
print("CONSTRUCTION, which card 4.5 forbids, and would be SC-DLS-4 at best even if allowed.")
