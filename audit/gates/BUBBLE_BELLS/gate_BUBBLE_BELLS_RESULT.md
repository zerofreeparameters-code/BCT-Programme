# Gate BUBBLE_BELLS — RESULT

**Card:** `gate_BUBBLE_BELLS_prompt.md`, SHA-256 `848b825a5b5d70afbd645eda4e749c393d2eca5f0f9f6ea0e84e75b984b3b2d8`, 4067 bytes (written and hashed before the run).
**Run:** 10 Nov 2026, 08:36–09:10 AEDT, Claude Fable 5.1, same thread as Gate TWIST and the desk-check; not blind; one instance. **Tier cap: CONJECTURE.**
**Type:** construction gate (positive framing by request: PASS = the construction holds as stated).

## Verdict — **SC-BB-2: the construction holds, with repairs**

| Q | result | one line |
|---|---|---|
| Q1 tortuosity reproducible? | **PASS** | random walk α_∞ = 1.668 (δ = 0.01a), 1.617 (δ = 0.005a) → 1.64 ± 0.03, vs finite-difference 1.64 ± 0.03: agreement 1.7 % / 1.4 % |
| Q2 where does 1/√α_∞ land? | **PARTIAL** | nothing with a quoted error moves; two printed numbers move by α_∞, both already in the asserted/closed class (Letter 73 scalar-mode amplitude; AZ6/AZ7's g = mc²/n₀) |
| Q3 ladder stable under proper matching? | **PARTIAL** | κ₀ reproduces App J to 7 figures; E₁/E₀ = 3.46 (desk-check's 2.81 superseded, +23 %) — the ladder exists and is stable, the desk-check rungs were wrong |
| Q4 committed numbers | written (N1–N10 below) | |

"Repairs" = the three things to carry forward: (i) use the k_ℓ-matched ladder (N5/N6), not the desk-check's; (ii) note in App J/AZ6 that the *macroscopic* sound speed is c_s/√α_∞, so AZ6's g = mc²/n₀ reads g = α_∞ mc²/n₀ if c_eff = c; (iii) Letter 73's h_scalar/h_tensor = α₀/(v_ph/c)² becomes 1.61 × 10⁻⁴/α_∞ ≈ 9.8 × 10⁻⁵ under the same identification (and rests on App JH content closed by JHF anyway).

## Q1 — independent tortuosity (`bb_q1_randomwalk.py`)

Off-lattice Gaussian random walkers in the FCC void space (touching rigid spheres, R = a/2, periodic minimum image), specular reflection off sphere surfaces (rejection fraction 10⁻³–10⁻⁴), MSD slope over the late half of the run after walkers have crossed 3–4 cells:

| δ (a) | walkers × steps | α_∞ | local quarters |
|---|---|---|---|
| 0.010 | 20 000 × 200 000 | 1.668 | 1.63, 1.60, 1.66, 1.69 |
| 0.005 | 10 000 × 400 000 | 1.617 | 1.61, 1.59, 1.63, 1.64 |

Random-walk estimate **1.64 ± 0.03** (spread between step sizes and quarters). Finite-difference extrapolation (`bells_tortuosity.py`, N = 64–224): **1.64 ± 0.03**. Two methods sharing no discretisation agree within 2 %. **PASS.** Literature: periodic-array conductivities for FCC exist (Sangani & Acrivos 1983; Cheng & Torquato 1997); the close-packed insulating value was not retrieved in-session — still worth one lookup, but the two in-house methods now stand on their own.

So: **σ_eff/σ₀ = φ/α_∞ = 0.158 ± 0.003, c_eff/c_s = 0.781 ± 0.007**, isotropic at O(k²).

## Q2 — where the factor lands (repo grep, 49 hits classified)

- **(a) identification only, no number moves:** Letter 20 ("Lorentz-invariance condition c_s = c"), AZ6 §lemma (i) ("g = mc²/n₀ ⇒ c_s = c"), Monograph PLB §286 (ratio of sound speeds along z, x — the isotropy statement; unchanged: the void-network tensor is a scalar at O(k²)). These become "c_eff = c" with g = α_∞ mc²/n₀. Nothing printed changes except the stated value of g, which is asserted (Gate BC/LINK: the phonon identification and the Josephson condition are assertions).
- **(b) printed number moves, quoted error:** none found. No corpus prediction with an error bar depends on c_s vs c_eff.
- **(c) printed number moves, already asserted/closed:** Letter 73 h_scalar/h_tensor = α₀/(v_ph/c)² = 1.61 × 10⁻⁴ → /α_∞ = 9.8 × 10⁻⁵ if "c exterior" is c_eff (it drops from "at Einstein Telescope sensitivity" to below it); but v_ph = 6.78c is App JH's dimensionally inconsistent phase velocity (CN-JHF, non-load-bearing) on a closed H = 1 hopfion, so the prediction was already not live. AZ7's g_n fixed by c_s = c (the α-correction family; FWD/STAT/QED(iv): zero bits) rescales by α_∞ — in the fitted class.
- Interior phase-velocity mentions (App JH, L36, L64, L70, L73, L103, L105): all cite the same closed App JH number; the bells reading replaces "6.78c interior phase velocity" with "κ₀ = 3.39 cavity mode", which is what App J actually computed.

**PARTIAL** (two class-(c) moves, zero class-(b)). Positive content: the construction forces a *definite* restatement of the sound-speed identification, g = α_∞ mc²/n₀, instead of leaving it implicit.

## Q3 — the ladder with k_ℓ(r/ξ) matching (`bb_q3_ladder.py`)

App J's s-wave condition follows exactly from ψ_in = j₀(κr), ψ_out = k₀(r/ξ) and the δ-jump ψ'_out/ψ_out − ψ'_in/ψ_in = −α₀ (the −1/R terms cancel; verified). Generalising the exterior to k_ℓ(r/ξ):

| ℓ | κ_ℓ a | κ_ℓR | E_ℓ/E₀ | desk-check (inherited Robin) |
|---|---|---|---|---|
| 0 | 3.390463 | 1.6952 | 1 | 1 |
| 1 | 6.305048 | 3.1525 | 3.458 | 2.814 |
| 2 | 8.991980 | 4.4960 | 7.034 | 5.452 |
| 3 | 11.528852 | 5.7644 | 11.563 | 8.887 |

κ₀ reproduces App J's 3.3905 (3.3904626). The desk-check's rungs were 20–25 % low: the inherited Robin constant under-weights the exterior's ℓ-dependent decay. **PARTIAL** by the card's 10 % rule; the *construction* is intact (a discrete, Planck-scale ladder, lowest rotating state ΔE = 28.3 ħ²/2ma²), the earlier numbers are superseded by these.

## Q4 — committed numbers (all CONJECTURE, zero free parameters; `bb_q4_numbers.py`)

| # | quantity | value | what would falsify it |
|---|---|---|---|
| N1 | void porosity | φ = 1 − π/(3√2) = 0.259520 | — (geometry) |
| N2 | tortuosity of FCC void network | α_∞ = 1.64 ± 0.03 | an exact/literature value outside 1.5–1.8 |
| N3 | macroscopic sound speed | c_eff/c_s = 0.781 ± 0.007 | N2 |
| N4 | isotropy of c_eff | exact at O(k²), anisotropic O(k⁴) | — (symmetry; RATIO/WHY√2) |
| N5 | bell ladder κ_ℓ a | 3.3905, 6.3050, 8.9920, 11.5289 | a different exterior decay law than k_ℓ(r/ξ) |
| N6 | ladder ratios E_ℓ/E₀ | 1, 3.458, 7.034, 11.563 | N5 |
| N7 | bell note vs host | ω₀a/c_s = 18.84; ω₀/ω(π/a) = 1.14 | — (follows from κ₀, ξ) |
| N8 | rigidity | soft shell fails both ways ⇒ Horn A | a derived shell stiffness ≫ α₀ |
| N9 | condensate particle mass if c_eff = c | m/m_P = 1/(√(2α_∞) ξ/a) = 0.238 ± 0.002 (0.305 without α_∞) | N2, or a different ξ |
| N10 | sub-resonant effect of the bells | ≲ 10⁻²⁸ relative | — |

N9 is the one new *interpretive* number: the corpus's ξ together with "the void sound is light" fixes the mass of the condensate's constituent at about a quarter of the Planck mass. It is not a prediction of anything measurable; it is what the model's own inputs imply, and it was implicit before (0.305 m_P) — the bells reading only corrects it by 1/√α_∞.

## What this gate does and does not do

Holds: the sphere interiors are consistently described as rigid depleted cavities with a fixed Planck-scale mode ladder in a single-component superfluid whose long-wavelength sound moves at 0.78 c_s through the voids, isotropically, with everything above fixed by geometry and the corpus's ξ. Nothing here reopens QED-DERIV, PROMOTE, JHF, KL or TWIST; nothing touches α₀ or the void radii; nothing predicts a new observable. The honest value of the gate is a clean, numbered, falsifiable-in-principle statement of what the interior *is* in the model as written, replacing a picture (knot of light) the audits had already closed.

## 🦜 Baby-speak

We checked the bubble-bells picture three ways. (1) Two completely different computer methods — one pushing current through the gaps, one letting particles wander through them — agree that sound in the gaps moves at 78 % of its free speed. That number is now solid. (2) We looked for every place the corpus says "the sound speed is the speed of light": none of them has a measured number attached, so nothing we've claimed to the world moves; two internal numbers (one in Letter 73, one in AZ6/AZ7) shift by 1.64, and both were already on the "asserted" shelf. (3) The bells' notes: the ground note is exactly App J's, the higher notes I'd guessed yesterday were ~20 % low and are now computed properly (3.46×, 7.03×, 11.56× the ground note). Bonus: the model's own numbers imply the superfluid is made of something weighing about a quarter of a Planck mass.

Verdict: **holds, with repairs** — update the ladder numbers, write "g = α_∞ mc²/n₀" where AZ6 says "g = mc²/n₀", and let Letter 73's scalar-wave amplitude drop by 1.64. The bubble-bells reading is now the live CONJECTURE for what lives inside the spheres.

## Files
`gate_BUBBLE_BELLS_prompt.md` (card, hashed) · `scripts/bb_q1_randomwalk.py`, `bb_q3_ladder.py`, `bb_q4_numbers.py` (+ `bells_tortuosity.py`, `bells_resonator.py` from the desk-check) · `output/q1_randomwalk_d010.txt`, `q1_randomwalk_d005.txt`, `q3_ladder.txt`, `q4_numbers.txt`.
