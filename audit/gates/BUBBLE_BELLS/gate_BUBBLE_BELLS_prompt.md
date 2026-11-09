# Gate BUBBLE_BELLS — construction card

**Programme:** BCT Superfluid Lattice Model, Cold Ledger
**Card written:** 10 November 2026, Claude Fable 5.1, at Michel's request ("think positively and run the BELLS")
**Type:** construction gate — does the bubble-bells reading of the sphere interiors (depleted rigid spheres in a single-component superfluid filling the FCC void network) hold up as a self-consistent, zero-parameter description with definite numbers?
**Depends on:** App J (interior mode κ₀, shell condition), App JH (surface term), Gate TWIST (SC-TWIST-1), Gate C1 (ξ_int = ξ), the 10 Nov 2026 desk-check (`BUBBLE_BELLS_deskcheck.md`: α_∞ ≈ 1.64 by finite differences, bell ladder by inherited Robin constant).
**Protocol disclosure:** written and run in the same thread as Gate TWIST and the desk-check, by the same instance, not blind. Tier cap CONJECTURE whatever the outcome.

## 1. Fixed model
FCC (BCT at c/a = √2), NN distance a = ℓ_P, spheres rigid and depleted, radius R = a/2, touching. Void superfluid: single-component GP, healing length ξ = a/√(8πα₀) = 2.31754 a (CN-C1-04, used as given), sound speed c_s = ħ/(√2 mξ). Sphere–void boundary: App J's δ-shell condition ψ'_out/ψ_out − ψ'_in/ψ_in = −α₀ (in units a = 1), which reproduces κ₀ = 3.3905 for ℓ = 0. Porosity φ = 1 − π/(3√2).

## 2. Questions (scored PASS / PARTIAL / FAIL; "PASS" means the construction holds as stated)

**Q1 — Is the tortuosity reproducible by an independent method?**
Compute α_∞ for the FCC void network by a method that shares no discretisation with the finite-difference solve: off-lattice random walkers with reflecting sphere boundaries, ⟨r²⟩/6t → D₀/α_∞. PASS if the random-walk α_∞ agrees with the FD extrapolation 1.64 ± 0.03 within 3 %; PARTIAL within 10 %; otherwise FAIL. Also check against any literature value located for FCC insulating spheres at close packing.

**Q2 — Where does the 0.78 land in the corpus?**
Grep the repo for every place the sound speed is identified with c or used numerically (c_s = c, "speed of sound", ħ/(√2 mξ), v_ph, 2/ξ gap). Classify each: (a) identification only (no number moves), (b) a printed number that would change by 1/√α_∞ or α_∞, (c) a number that would change but is already recorded as fitted/asserted. PASS if no printed corpus prediction with a quoted error moves outside that error; PARTIAL if one moves but is already in the fitted/asserted class; FAIL if a claimed derived observable moves outside its error.

**Q3 — Is the bell ladder stable under proper matching?**
Redo κ_ℓ for ℓ = 0…3 with the exterior taken as the decaying modified spherical Bessel k_ℓ(r/ξ) (the ℓ-generalisation of App J's e^{−(r−R)/ξ}/r), not the inherited s-wave Robin constant. PASS if κ₀ reproduces App J to 4 figures and E₁/E₀ is within 10 % of the desk-check 2.81; PARTIAL if κ₀ reproduces but E₁/E₀ moves more; FAIL if κ₀ does not reproduce.

**Q4 — Positive statement of what the construction predicts.** Write the list of zero-parameter numbers the bubble-bells reading commits to (α_∞, c_eff/c_s, κ-ladder, bell/zone-edge ratio, rigidity requirement), each with its tier and what would falsify it. Not scored; it is the deliverable's forward-looking part.

## 3. Verdict codes
- **SC-BB-1 (construction holds):** Q1 PASS, Q2 PASS or PARTIAL, Q3 PASS. The bubble-bells reading is recorded as the live CONJECTURE for sphere interiors, with its number list.
- **SC-BB-2 (holds with repairs):** any PARTIAL not covered above, or Q3 PARTIAL. Record which number needs a fresh-thread check.
- **SC-BB-3 (does not hold as stated):** any FAIL. Say which.

## 4. No-fit clause
No input beyond §1. No comparison with α, 137, or measured constants is part of any score. The card is not evidence for or against the void geometry.

## 5. Deliverable
`gate_BUBBLE_BELLS_RESULT.md` with the hash of this card, Q1–Q4, verdict, number list, and a plain-language summary; scripts and outputs alongside.
