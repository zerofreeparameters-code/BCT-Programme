#!/usr/bin/env python3
"""
Gate TWIST — Q4.  Does a current-carrying shell follow from the medium?  Items (i)–(iv) are scored
against the corpus in the RESULT; this script supplies the numbers for (iii):

 (iii) Insulating contacts.  If the 12 touching contacts per sphere conduct, the shells form a connected
       conducting network at Planck spacing.  Pendry, Holden, Stewart & Youngs, PRL 76, 4773 (1996):
       a thin-wire lattice of spacing a and wire radius r has an effective plasma frequency
           ω_p² = 2π c² / ( a² ln(a/r) ).
       Order of magnitude for the BCT shell network: a = ℓ_P, r ~ shell thickness.  Any connected
       conducting network with spacing a has ω_p ~ c/a up to the logarithm; below ω_p it is opaque
       (ε_eff = 1 − ω_p²/ω² < 0, evanescent).
       Contrast: INSULATED conducting spheres (Maxwell–Garnett, perfect conductor, filling fraction f)
           ε_eff = (1 + 2f)/(1 − f)   — a transparent dielectric with no cutoff.
       So the insulating-contact requirement is real: it is what separates "opaque Planck metal" from
       "transparent dielectric" — and the corpus must supply it, not assume it.
 (iv) Grip term — topological statement only (no number): on a ball B³ with FREE boundary values of n,
       maps B³ → S² are all homotopic (B³ is contractible); the Hopf invariant is defined and protected only
       when n is fixed on ∂B³ (then B³/∂B³ ≅ S³ and π₃(S²) = ℤ applies).  The corpus shell term is a function
       of |Ψ|² only (U(2)-symmetric, App J eq. deltashell / App JH eq. free-energy): it does not see n.
"""
import mpmath as mp
mp.mp.dps = 40

a = mp.mpf(1)
r_tet = (mp.sqrt(6) - 2) / 4 * a; r_oct = (mp.sqrt(2) - 1) / 2 * a
R = a / 2
f_fcc = mp.pi / (3 * mp.sqrt(2))               # FCC packing fraction 0.74048

print("Gate TWIST Q4(iii) — wire-medium (Pendry 1996) estimate for connected conducting shells at Planck spacing")
print("  ω_p² = 2π c²/(a² ln(a/r)),  in units of (c/a):  ω_p/(c/a) = √(2π/ln(a/r))")
for label, r in [("r = shell thickness d = √(r_tet r_oct) a (App J's asserted d)", mp.sqrt(r_tet * r_oct) * a),
                 ("r = r_tet", r_tet), ("r = window radius (2/√3−1)R", (2 / mp.sqrt(3) - 1) * R),
                 ("r = 1e-3 a (very thin)", mp.mpf('1e-3') * a), ("r = 1e-10 a (absurdly thin)", mp.mpf('1e-10') * a)]:
    wp = mp.sqrt(2 * mp.pi / mp.log(a / r))
    print(f"   {label:58s} r/a = {mp.nstr(r,5):>9}   ω_p = {mp.nstr(wp,5)} × (c/a)")
c_over_lP_Hz = mp.mpf('2.99792458e8') / mp.mpf('1.616255e-35')      # c/ℓ_P in rad/s (CODATA ℓ_P, scale only)
print("  Scale: c/ℓ_P =", mp.nstr(c_over_lP_Hz, 4), "rad/s  →  ω_p ~ 10^43 rad/s for every reasonable r (the log is weak).")
print("  Highest-energy photons observed are ~PeV (ω ~ 10^30 rad/s): ω/ω_p ~ 1e-13 → deep in the evanescent regime.")
print("  → If the contacts conduct, the medium is opaque to ALL observed light. The wire-medium argument HOLDS")
print("    (order of magnitude; the log and the network topology only move ω_p by O(1)).")
print()
print("  Contrast — INSULATED perfectly conducting spheres (Maxwell–Garnett, f = π/(3√2) =", mp.nstr(f_fcc, 8), "):")
eps_eff = (1 + 2 * f_fcc) / (1 - f_fcc)
print("    ε_eff = (1+2f)/(1−f) =", mp.nstr(eps_eff, 8), " → n_eff = √ε_eff =", mp.nstr(mp.sqrt(eps_eff), 8),
      " — transparent, no cutoff (long-wavelength limit; MG is approximate at f = 0.74 but the qualitative point stands).")
print("  So the entire difference between 'opaque Planck metal' and 'transparent medium' rides on the 12 contacts")
print("  per sphere being insulating — nothing in App J / App JH / Letter 36 says anything about the contacts.")
print()
print("Q4(iv) — topology (no number): Hopf number on a ball with free boundary is NOT protected; it needs n pinned on ∂B³.")
print("  The corpus shell term depends on |Ψ|² only (U(2)-symmetric) → it does not pin n → grip term ABSENT.")
