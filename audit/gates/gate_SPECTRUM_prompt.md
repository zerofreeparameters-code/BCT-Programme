# Gate SPECTRUM — pre-registration card

**Programme:** "Nothing says why 1/137" (successor to the BCT Cold Ledger)
**Card written:** 7 October 2026, Claude, at Michel's request
**Status:** PRE-REGISTERED, NOT RUN. Nothing in this card has been computed to standard.
**Type:** requirement map with consistency checks. Not a derivation, not a blind test (see section 9).
**Depends on:** Gate LOG (card SHA-256 f334c6dd…a56466dd, commit 4237c852…, verdict SC-LOG-3, status CONJECTURE).

---

## 1. Question

Gate LOG found that, with light induced at the Planck scale, the known charged
particles supply about 33 of the 137 units of 1/α. A proposal made after that
run (Gemini, 7 October 2026, "Spectrum Solutions") fills the gap with extra
heavy "vector-like generations" and solves for their mass.

This gate turns that proposal around. It does not ask "which mass gives 137?"
It asks:

1. For each number N_V of extra vector-like generations, what single mass M_V
   does the induced condition demand?
2. Is that mass already excluded by experiment?
3. Is the resulting theory internally consistent up to the Planck scale?

A row that survives is a requirement the idea must meet. It is not evidence
for the idea.

## 2. Fixed rules for the mass (inherits Gate LOG, variant V1)

All Gate LOG inputs, masses, coefficients and the formula of card section 3
are used unchanged. The V1 baseline B = 1/α(0) from known particles is
recomputed inside this run; it is not copied from the Gate LOG result.

**Added content.** N_V complete vector-like generations, each a 16 + 16-bar
of SO(10), all at one common mass M_V. Charged Dirac content per generation:

| Field | Colour | Charges | Σ N_c·Q² |
|---|---|---|---|
| U | 3 | 2/3 | 12/9 |
| D | 3 | 1/3 | 3/9 |
| Q doublet | 3 | 2/3, 1/3 | 15/9 |
| E | 1 | 1 | 9/9 |
| L doublet | 1 | 0, 1 | 9/9 |
| N | 1 | 0 | 0 |

Sum = 48/9, so b_V = (4/3)·(48/9) = 64/9 per vector-like generation.

**Requirement.**

    137.035999 − B = (1/2π) · N_V · (64/9) · ln(M_P / M_V)

solved for M_V.

**Rows.** N_V = 1, 2, 3, 4, 5, 6. All six are run and reported. No other
values, no split or hierarchical masses, no other multiplets.

**Sensitivity.** The whole table is repeated with the Gate LOG V4 baseline
(constituent light quarks). V1 is the headline.

## 3. Check C1 — experiment

A row is **EXCLUDED** if M_V < 2000 GeV.

This threshold is a round, conservative figure fixed by this card. Collider
searches exclude new coloured vector-like fermions up to roughly 1.3–1.6 TeV;
the card does not depend on the exact published limit. A row within a factor
of 3 above the threshold (2000–6000 GeV) is reported as **MARGINAL**.

## 4. Check C2 — strong force stays finite

One-loop running of 1/α_s from M_Z to M_P:

- α_s(M_Z) = 0.1180, M_Z = 91.1876 GeV
- d(1/α_s)/d ln μ = −b₃/(2π), with b₃ = −23/3 from M_Z to m_t = 172.57 GeV,
  b₃ = −7 from m_t to M_V, and b₃ = −7 + (8/3)·N_V above M_V

A row **FAILS C2** if 1/α_s reaches zero at or below M_P.

## 5. Check C3 — the two electroweak forces stay finite

Above the electroweak scale, 1/α = 1/α₂ + 1/α_Y. The induced condition sets
the sum to zero at M_P. Each term is the inverse square of a real coupling and
cannot be negative. So both must stay non-negative all the way up to M_P.

One-loop running from M_Z (top threshold ignored, full Standard Model
coefficients used from M_Z):

- Inputs at M_Z: 1/α = 127.951, sin²θ_W = 0.23122
- 1/α₂(M_Z) = sin²θ_W · 127.951, 1/α_Y(M_Z) = (1 − sin²θ_W) · 127.951
- d(1/α_Y)/d ln μ = −b_Y/(2π), b_Y = 41/6 below M_V, 41/6 + (40/9)·N_V above
- d(1/α₂)/d ln μ = −b₂/(2π), b₂ = −19/6 below M_V, −19/6 + (8/3)·N_V above

(Cross-check on the coefficients: 40/9 + 8/3 = 64/9, the electromagnetic
value in section 2.)

For each row report 1/α₂(M_P), 1/α_Y(M_P), and, if either reaches zero below
M_P, the scale μ_pole where it does.

A row **FAILS C3** if either 1/α₂ or 1/α_Y reaches zero below M_P by more
than the tolerance: μ_pole < M_P / 100.

## 6. Outputs

- **S1.** Table of M_V for N_V = 1…6 (V1 baseline, then V4 baseline), in GeV
  and in orders of magnitude below M_P.
- **S2.** C1 status per row.
- **S3.** 1/α_s(M_P) per row and C2 status.
- **S4.** 1/α₂(M_P), 1/α_Y(M_P), μ_pole if any, and C3 status per row.
- **S5.** Scoring of the 7 October proposal: N_V = 3 at M_V ≈ 9.089 × 10¹² GeV.
  Report 1/α(0) that this content and mass actually give under the card's
  formula, and the M_V the card's formula requires for N_V = 3.

## 7. Verdict codes

- **SC-SPEC-1 (requirement map).** At least one row passes C1, C2 and C3.
  Report the surviving rows as what the induced-light idea demands. State
  that this is a requirement, not evidence.
- **SC-SPEC-2 (kill by experiment).** Every row fails C1.
- **SC-SPEC-3 (kill by inconsistency).** Every row that passes C1 fails C2 or
  C3. Light induced at the Planck scale, completed by whole vector-like
  generations, is not self-consistent at one loop.

## 8. No-fit clause

- No row, multiplet, mass pattern, cutoff, input or threshold may be added,
  removed or changed after the run starts.
- No result may be described as "deriving" α. Every M_V in the table is the
  output of one parameter tuned to one number and carries zero evidential
  weight on its own. Only the C1–C3 outcomes carry information.
- If the smallest surviving N_V happens to equal 3, that is the edge of an
  inequality, not a prediction of three generations, and must be reported
  with that sentence attached.
- Whatever the outcome, it is not evidence for or against BCT void geometry.

## 9. Analyst's disclosure (why this is not a blind test)

Claude made rough estimates before writing this card. Recorded here so they
cannot be hidden later:

- M_V, V1 baseline: N_V = 1 near 10⁻²¹ GeV; N_V = 2 near 0.1 GeV; N_V = 3
  near 6 × 10⁵ GeV; N_V = 4 near 10⁹ GeV; N_V = 5 near 10¹¹ GeV; N_V = 6 near
  3 × 10¹² GeV.
- C1: rows 1 and 2 expected EXCLUDED; rows 3–6 expected to pass.
- C2: 1/α_s(M_P) expected near 13–14 for every row (pass). Whole generations
  shift all three forces by an amount fixed by the requirement itself, so the
  answer should not depend on N_V.
- C3: expected to FAIL for every row. Rough values 1/α₂(M_P) ≈ +10 and
  1/α_Y(M_P) ≈ −9, again independent of N_V: hypercharge would blow up below
  the Planck scale while the weak force is still finite.
- Expected verdict: **SC-SPEC-3**.
- S5: a quick double-precision check on 7 October gave about 6.3 × 10⁵ GeV
  for N_V = 3, and about 81 for 1/α(0) at the proposal's own mass.

If C3 fails as expected, the reason is structural: the Standard Model's two
electroweak forces do not meet at zero at the same scale, and adding whole
generations moves them together without closing the gap between them.

## 10. Known limitations (stated in advance)

- One loop only, step thresholds, as in Gate LOG.
- The mass requirement uses Gate LOG's low-energy thresholds; checks C2 and
  C3 use measured couplings at M_Z. The two differ by about 1 unit of 1/α at
  M_Z. A C3 result within 3 units of zero is to be reported as INCONCLUSIVE,
  not as pass or fail.
- Only complete 16 + 16-bar generations at one common mass are tested. Other
  charged content (incomplete multiplets, scalars, extra gauge bosons) is
  outside this card and would need its own.
- The Planck scale as cutoff is an assumption, not an output.

## 11. Run protocol

- Fresh thread, inside the BCT project. One gate per thread.
- Fetch this file from the repo by commit-pinned raw URL, hash it on disk
  (SHA-256) before reading, and record the digest and commit.
- Python with mpmath, 60 dps working, 40 dps reported. Script saved and
  delivered with the result.
- Deliverable: `gate_SPECTRUM_RESULT.md` with S1–S5, the verdict code, the
  disclosure scored, and a plain-language summary.
- Same-session results are capped at CONJECTURE.
