# Gate BB-ALPHA — pre-registration card

**Programme:** BCT Superfluid Lattice Model, Cold Ledger
**Card written:** 10 November 2026, Claude Fable 5.1, at Michel's request (next step after Gate BUBBLE_BELLS)
**Status:** PRE-REGISTERED, NOT RUN.
**Type:** verification gate — promote one number, the tortuosity of the FCC void network, from in-house CONJECTURE to an independently anchored value.
**Depends on:** Gate BUBBLE_BELLS (SC-BB-2; `audit/gates/BUBBLE_BELLS/`), which found α_∞ = 1.64 ± 0.03 by two in-house methods (finite-difference conductivity, N = 64–224; off-lattice random walk, two step sizes).

## 1. The claim under test

For rigid, mutually touching, insulating spheres on FCC (radius R = a/2, porosity φ = 1 − π/(3√2) = 0.259520), the electrical tortuosity of the pore space is
  **α_∞ = φ · F = 1.64 ± 0.03**,  F = σ₀/σ_eff the formation factor,  equivalently  σ_eff/σ₀ = 0.158 ± 0.003.
Consequence used downstream (Johnson, Koplik & Dashen, J. Fluid Mech. 176, 379 (1987)): fourth-sound speed of a superfluid filling the pores, c₄ = c_s/√α_∞ = 0.781 ± 0.007 c_s.

## 2. Blinding

Switch off "Search and reference past chats" and "Generate memory from chats" before the thread; on after. Do **not** open `audit/gates/BUBBLE_BELLS/` scripts or outputs, or the desk-check note, until Step 2 is written down. The number 1.64 ± 0.03 in §1 is the only in-house input and is the thing being tested.

## 3. Steps, in order

**Step 1 — literature.** Locate a published value for the effective conductivity of an FCC array of *insulating* (zero-conductivity) spheres at or extrapolated to the close-packed fraction f = 0.74048. Candidate sources: Sangani & Acrivos, Proc. R. Soc. A 386, 263 (1983) (multipole expansion, cubic arrays, both conducting limits); Cheng & Torquato, Proc. R. Soc. A 453, 145 (1997) (FCC, wide f-range); McPhedran & McKenzie, Proc. R. Soc. A 359, 45 (1978); Kim & Yoon, J. Compos. Mater. 33 (1999) (BEM, FCC). Record the value, its f, and how it was obtained. If only a near-touching value is available, record it and the extrapolation used.

**Step 2 — independent computation.** Compute σ_eff/σ₀ for the same geometry by a method that is neither a Cartesian finite-difference grid nor a random walk: a multipole (Rayleigh) expansion, a boundary-element/Nyström solve, or a spectral (Fourier–Galerkin) homogenisation with ≥ 2 resolutions and a stated extrapolation. Report σ_eff/σ₀, α_∞, and an error estimate.

**Step 3 — reconcile.** Compare Step 1, Step 2 and the pre-registered 1.64 ± 0.03.

**Step 4 — downstream statement.** State c₄/c_s and the implied g = α_∞ mc²/n₀ (App AZ6 audit note) and m/m_P = 1/(√(2α_∞) ξ/a) (Gate BUBBLE_BELLS N9) with propagated errors. No other corpus number is touched.

## 4. Verdict codes

- **SC-BBA-1 (anchored):** Step 1 or Step 2 lands within 3 % of 1.64, and no located source contradicts it beyond 5 %. α_∞, c₄/c_s and N9 move to **CONJECTURE (independently anchored)** — the tier below PROVEN, since the physical identification (void sound = light) is not tested here.
- **SC-BBA-2 (anchored with a shift):** independent values agree with each other but sit 3–10 % from 1.64. Record the corrected α_∞; downstream numbers move with it.
- **SC-BBA-3 (not anchored):** independent values disagree with 1.64 by more than 10 %, or disagree with each other by more than 10 %. The in-house number is flagged for a fresh high-resolution recomputation; nothing downstream is promoted.
- **SC-BBA-0 (cannot evaluate):** no literature value found *and* no independent method implemented to a stated error.

## 5. No-fit clause

The geometry (FCC, touching, R = a/2) is fixed. No comparison with α, 137 or any measured constant is part of this gate. The gate is not evidence for or against the void geometry or the bubble-bells reading itself; it anchors one number.

## 6. Run protocol

Fresh thread inside the BCT project, one gate per thread, settings step before and after. Fetch this card by commit-pinned raw URL with curl to disk, compute SHA-256, compare with the pre-registered digest **before reading**. Deliverable `gate_BBALPHA_RESULT.md` (hash check, contamination statement incl. model and memory-listing disclosure, Steps 1–4, verdict, plain-language summary) + scripts, committed under `audit/gates/BBALPHA/` as a patch for Michel. Same-session results capped at CONJECTURE.
