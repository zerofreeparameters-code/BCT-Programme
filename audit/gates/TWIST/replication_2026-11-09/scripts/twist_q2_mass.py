#!/usr/bin/env python3
"""
Gate TWIST — Q2.  Granting the minimal Maxwell term (BOUGHT in Q1: coupling e counted, not fitted),
what is the mass of a and how many polarisations does it have (i) in a uniformly condensed medium,
(ii) in a medium condensed in the shells but not in the voids — if the model supplies that?

Units: ħ = c = 1, a = ℓ_P = 1.  Corpus Planck normalisation declared: n0 a³ = 1, m = m_P = 1/a
  ⇒ K := ħ² n0 / (2m) = 1/(2a²)   (stiffness; this is App J's "J = 1").  Kept symbolic as K below
  where it matters; the Planck normalisation is used only to quote numbers.

Energy functional (Euclidean / static):
  E = ∫ [ (1/4e²) f_ij f_ij + K (∇φ + a)² + (K/4)(∇n)² + ... ]  with f = da.
In Fourier space, after the phase φ is eliminated (Q1 Part B) the quadratic form for a is
  a_i [ (k²/e²) P^T_ij + 2K P^T_ij ] a_j / 2   (with (1/4e²) f_ij f_ij = (1/2e²)(curl a)²)
so the transverse propagator pole sits at k² = −2K e²:  m_a² = 2 K e²,  λ_L = 1/√(2 K e²).
"""
import mpmath as mp
mp.mp.dps = 60

a = mp.mpf(1)
alpha0 = (mp.sqrt(2) - 1) / 2 * (mp.sqrt(6) - 2) / 4 / mp.pi
xi = a / mp.sqrt(8 * mp.pi * alpha0)
R = a / 2
r_oct = (mp.sqrt(2) - 1) / 2 * a
r_tet = (mp.sqrt(6) - 2) / 4 * a
K = 1 / (2 * a**2)                       # Planck normalisation (declared)

print("Gate TWIST Q2 — mass and polarisations of a with a granted Maxwell term")
print("Fixed inputs: a = 1, R = a/2, ξ/a =", mp.nstr(xi, 20), ", K a² =", mp.nstr(K * a**2, 5), "(declared Planck normalisation)")
print()
print("(i) UNIFORMLY CONDENSED MEDIUM (App J: same GP condensate inside, outside, in voids; one n0):")
print("    m_a² = 2 K e²  →  m_a = e √(2K) = e/a  (Planck normalisation)   λ_L = a/e")
for e2 in [mp.mpf('0.01'), mp.mpf('0.1'), mp.mpf(1), mp.mpf(10)]:
    e = mp.sqrt(e2)
    m_a = mp.sqrt(2 * K) * e
    lam = 1 / m_a
    print(f"      e² = {mp.nstr(e2,4):>5}:  m_a = {mp.nstr(m_a,6)} /a  (= {mp.nstr(m_a,6)} m_P),  λ_L = {mp.nstr(lam,6)} a,  λ_L/R = {mp.nstr(lam/R,6)}")
print("    For EVERY e ≠ 0: m_a ≠ 0.  The Goldstone φ is eaten (Higgs/Meissner):")
print("    polarisations = 2 transverse + 1 longitudinal = 3 (massive vector).  → FAIL in the uniform medium.")
print("    No corpus number makes m_a = 0; only e → 0 does, which switches the Maxwell term off (1/e² → ∞).")
print()
print("(ii) CONDENSED IN SHELLS, EMPTY VOIDS — does the model supply it?")
print("    App J §1.1–1.2 (primary source): 'The BCT condensate field Ψ fills all of space' … 'the same GP")
print("    action as the exterior condensate (same J, same ξ, same nonlinear coupling)'. App JH §3.1:")
print("    |Ψ_int|² = ρ0 'constant bulk density'. Card A1: 'the interior is exactly the same as the OHC'.")
print("    → The model supplies NO location-dependent condensation. Branch (ii) is NOT REACHED without a new")
print("      input (a confining potential or a second phase). Counted in the cost table, not granted.")
print()
print("    Even if bought, the void network cannot carry a long-wavelength massless mode:")
r_win = (2 / mp.sqrt(3) - 1) * R          # triangular-window inscribed radius between 3 touching spheres (KL desk check)
k_c = mp.mpf('1.8412') / r_win            # TE11 cutoff of a circular aperture of radius r_win (order of magnitude)
omega_P = 1 / a                           # c/a = Planck angular frequency (c = 1)
print("      window radius between touching spheres r_win = (2/√3 − 1) R =", mp.nstr(r_win, 8), "a")
print("      waveguide cutoff through a window  k_c ≈ 1.841/r_win =", mp.nstr(k_c, 6), "/a  →  ω_c ≈", mp.nstr(k_c / omega_P, 5), "× (c/a)")
print("      cavity sizes r_oct =", mp.nstr(r_oct, 6), "a, r_tet =", mp.nstr(r_tet, 6), "a  →  lowest cavity modes k ~ π/r ~",
      mp.nstr(mp.pi / r_oct, 5), "–", mp.nstr(mp.pi / r_tet, 5), "/a")
print("      Everything below ~10 c/a is evanescent in the void network: no propagating massless photon at any")
print("      wavelength longer than the Planck length. Locally two transverse cavity polarisations, but no massless mode.")
print("    → Branch (ii) FAILS as well, on geometry alone (connected sub-Planck cavities, Planck-scale cutoff).")
print()
print("Q2 verdict: FAIL (conditional on Q1 being BOUGHT).  a is massive in the corpus medium; a void-only")
print("massless mode needs a location-dependent condensation the corpus does not supply and is then cut off")
print("at ~10 Planck frequencies by the void geometry.")
