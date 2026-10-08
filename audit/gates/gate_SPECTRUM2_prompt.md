# Gate SPECTRUM2 — pre-registration card

**Programme:** "Nothing says why 1/137" (successor to the BCT Cold Ledger)
**Card written:** 7 October 2026, Claude, at Michel's request
**Status:** PRE-REGISTERED, NOT RUN. Nothing in this card has been computed to standard.
**Type:** requirement map with consistency checks. Not a derivation, not a blind test (see section 10).
**Depends on:** Gate LOG (card SHA-256 f334c6dd…a56466dd, verdict SC-LOG-3) and
Gate SPECTRUM (card SHA-256 69ff9dd0…7f0ca3e2, verdict SC-SPEC-1, tolerance-decided,
two runs agreeing to 40 digits).

---

## 1. Why a successor

Gate SPECTRUM returned SC-SPEC-1 only because its fail rule was written in units of
scale (pole more than 100 times below M_P). In units of 1/α the same rows miss by 9.4,
three times that card's own 3-unit inconclusive band. The verdict depended on the
yardstick. This card fixes the yardstick and then asks a question whose answer is not
already known.

## 2. What is already known (stated, not a result of this card)

Above the electroweak scale 1/α = 1/α₂ + 1/α_Y. Each term is the inverse square of a
real coupling and cannot be negative. If the sum is zero at M_P, **each term is zero at
M_P**. The induced condition is therefore two conditions, not one.

Whole vector-like generations at one mass supply one adjustable quantity,
N_V · ln(M_P/M_V). One quantity cannot meet two conditions unless they happen to agree.
Gate SPECTRUM shows they do not: with the sum set to zero, 1/α₂(M_P) = +10.50 and
1/α_Y(M_P) = −9.45 in every row with M_V above M_Z.

Scored in units of 1/α with a 3-unit band, every such row fails. **This re-scoring is
made after seeing the numbers. Its outcome is known in advance and it carries no new
information.** It is recorded here so that it is not later presented as a finding of
this gate.

## 3. Question

Two conditions need two adjustable quantities. For a small, fixed menu of second
ingredients added to whole vector-like generations:

1. Is there a solution with both electroweak terms zero at M_P?
2. What two masses does it demand?
3. Are those masses excluded by experiment?
4. Does the strong force stay finite up to M_P?

A row that survives is a requirement. It is not evidence.

## 4. Fixed rules

**4.1 Running.** One loop, step thresholds, from M_Z to M_P = 1.220890 × 10¹⁹ GeV.
Inputs exactly as Gate SPECTRUM sections 4 and 5:

- 1/α(M_Z) = 127.951, sin²θ_W = 0.23122, M_Z = 91.1876 GeV
- 1/α₂(M_Z) = sin²θ_W · 127.951, 1/α_Y(M_Z) = (1 − sin²θ_W) · 127.951
- α_s(M_Z) = 0.1180
- Standard Model coefficients: b_Y = 41/6, b₂ = −19/6 from M_Z (top threshold ignored);
  b₃ = −23/3 from M_Z to m_t = 172.57 GeV and −7 above
- d(1/α_i)/d ln μ = −b_i/(2π)

Define the Standard-Model-only values at M_P: A_Y, A_2, A_3.

**4.2 Ingredients.** All Dirac (vector-like). Coefficients per copy, same conventions as
Gate SPECTRUM (hypercharge normalised so Q = T₃ + Y):

| Label | Content | b_Y | b₂ | b₃ | b_em = b_Y + b₂ |
|---|---|---|---|---|---|
| G | whole generation, 16 + 16-bar | 40/9 | 8/3 | 8/3 | 64/9 |
| T | SU(2) triplet, Y = 0, colourless | 0 | 8/3 | 0 | 8/3 |
| L | SU(2) doublet, Y = 1/2, colourless | 2/3 | 2/3 | 0 | 4/3 |
| Q | SU(2) doublet, Y = 1/6, colour triplet | 2/9 | 2 | 4/3 | 20/9 |

The script must rebuild every coefficient from the field content and assert these
values, including b_em = (4/3) · Σ N_c Q².

**4.3 Families.** Exactly three: G + T, G + L, G + Q. N_G copies of G at one common
mass M_G and N_X copies of X at one common mass M_X.

**4.4 Requirement.** With x_i = N_i · ln(M_P/M_i) / (2π):

    b_Y(G) · x_G + b_Y(X) · x_X = A_Y
    b₂(G) · x_G + b₂(X) · x_X = A_2

solved exactly for x_G and x_X. Then M_i = M_P · exp(−2π · x_i / N_i).

**4.5 Rows.** N_G = 1…6 and N_X = 1…6 for each family: 36 rows per family, 108 in
all. All are run and reported. No other values, families, multiplets or mass patterns.

## 5. Checks

**C0 — a solution exists.** A family **FAILS C0** if x_G < 0 or x_X < 0 (a mass above
the cutoff).

**C1 — experiment.** A row is **EXCLUDED** if M_G < 2000 GeV, or M_Q < 2000 GeV, or
M_T < 1000 GeV, or M_L < 1000 GeV. These are round, conservative figures fixed by this
card. Collider limits on coloured vector-like fermions are roughly 1.3–1.6 TeV and on
colourless electroweak multiplets lower; the card does not depend on the exact
published limits. A row with any mass within a factor of 3 above its threshold is
**MARGINAL**.

Any mass below M_Z makes the linear solve of 4.4 invalid for that row. Such rows are
EXCLUDED by C1 and their other figures are to be flagged as not meaningful.

**C2 — strong force stays finite.** 1/α_s(M_P) = A_3 − b₃(G) · x_G − b₃(X) · x_X.
**FAILS** if below −3. **INCONCLUSIVE** if between −3 and +3. **Passes** if above +3.

**C3 — no earlier pole.** With both electroweak terms zero at M_P, confirm that neither
is zero or negative at any scale between M_Z and M_P. Report the minimum of each.
A row **FAILS C3** if either is below −3 anywhere.

## 6. The tolerance, and where it comes from

All tolerances are in units of 1/α, and all equal 3. The figure is not new: it is the
inconclusive band of Gate SPECTRUM section 10, fixed before any Gate SPECTRUM number was
computed, and sized on the roughly 1-unit mismatch between Gate LOG's thresholds and the
measured couplings at M_Z. No tolerance in units of scale is used anywhere in this card.

Because the two conditions are solved exactly, the tolerance cannot decide whether a
solution exists. It enters in two places only:

- the C2 and C3 bands above;
- **the mass band.** Each row is re-solved with A_Y and A_2 each shifted by +3 and by −3
  (four corners). Report the smallest and largest M_G and M_X over the corners. A row's
  C1 status must hold at all four corners; otherwise it is reported as **MARGINAL**.

## 7. Outputs

- **T0.** A_Y, A_2, A_3.
- **T1.** For each family: x_G, x_X, C0 status, and 1/α_s(M_P) with C2 status. (These
  do not depend on N_G or N_X.)
- **T2.** For each family, the 6 × 6 table of (M_G, M_X) in GeV with C1 status.
- **T3.** For each family, the smallest N_G and smallest N_X that pass C1, with the
  mass band of section 6 for that row.
- **T4.** C3 minimum values for every row that passes C1.
- **T5.** Consistency with Gate LOG: for each family, 1/α(0) from the Gate LOG V1
  formula with the solved content added. Expected within about 3 units of 137.036.
  Report the difference; a difference above 3 units is a notice, not a kill.

## 8. Verdict codes

- **SC-SPEC2-1 (requirement map).** At least one row in at least one family passes C0,
  C1, C2 and C3. Report surviving families and rows as what the induced-light idea
  demands. State that this is a requirement, not evidence.
- **SC-SPEC2-2 (kill by experiment).** At least one family passes C0, and every row of
  every such family fails C1.
- **SC-SPEC2-3 (kill by inconsistency).** No family passes C0, or every row that passes
  C0 and C1 fails C2 or C3.

Each family's own outcome is reported whatever the overall code.

## 9. No-fit clause

- No family, row, multiplet, mass pattern, cutoff, input, threshold or tolerance may be
  added, removed or changed after the run starts.
- No result may be described as "deriving" α. Each row has two masses tuned to two
  numbers and carries zero evidential weight. With 108 rows and three families, a
  survivor is expected and means nothing by itself. Only kills carry information.
- A menu of three second ingredients was chosen by the analyst. Other menus exist. A
  surviving family is "one way it could be done", never "the way".
- If the smallest surviving N_G equals 3, that is the edge of an inequality, not a
  prediction of three generations, and must be reported with that sentence attached.
- Whatever the outcome, it is not evidence for or against BCT void geometry.

## 10. Analyst's disclosure (why this is not a blind test)

Claude ran Gate SPECTRUM (run 2) before writing this card and made hand estimates.
Recorded so they cannot be hidden later:

- A_Y ≈ 55.5, A_2 ≈ 49.5, A_3 ≈ 52.5.
- G + T: x_G ≈ 12.5, x_T ≈ 6.1; 1/α_s(M_P) ≈ 19 (pass). M_G near 10² GeV for N_G = 2
  (excluded) and 5 × 10⁷ GeV for N_G = 3. M_T near 3 × 10² GeV for N_T = 1 (excluded)
  and 6 × 10¹⁰ GeV for N_T = 2. Expected to survive from (3, 2) upward.
- G + L: x_G ≈ 3.4, x_L ≈ 61; 1/α_s(M_P) ≈ 43 (pass). M_G near 7 × 10⁹ GeV already at
  N_G = 1. M_L far below M_Z for every N_L ≤ 6. Expected: every row EXCLUDED.
- G + Q: x_G ≈ 12.0, x_Q ≈ 8.7; 1/α_s(M_P) ≈ 9 (pass). M_G near 4 × 10² GeV for
  N_G = 2 (excluded) and 10⁸ GeV for N_G = 3. M_Q excluded at N_Q = 1, near 2 × 10⁷ GeV
  at N_Q = 2. Expected to survive from (3, 2) upward.
- C0: expected to pass for all three families.
- C3: expected to pass wherever C1 passes.
- Expected verdict: **SC-SPEC2-1**, with G + L killed by experiment.

The menu was chosen knowing that the gap needs more SU(2) charge relative to
hypercharge than a whole generation supplies. All three second ingredients have that
property. That is a selection made with the answer in view.

## 11. Known limitations (stated in advance)

- One loop only, step thresholds.
- A coupling that becomes infinite exactly at the cutoff is non-perturbative in the last
  few e-folds below it. One loop is least reliable exactly where the condition is
  imposed. This card cannot settle whether the condition is physically meaningful.
- The top threshold is ignored in the electroweak running, as in Gate SPECTRUM.
- Only the three listed families, each at one common mass per ingredient.
- The Planck scale as cutoff is an assumption, not an output.

## 12. Run protocol

- Fresh thread, inside the BCT project. One gate per thread.
- Fetch this file from the repo by commit-pinned raw URL, hash it on disk (SHA-256)
  before reading, and record the digest and commit.
- Python with mpmath, 60 dps working, 40 dps reported. Script saved and delivered with
  the result.
- Deliverable: `gate_SPECTRUM2_RESULT.md` with T0–T5, the verdict code, the disclosure
  scored, and a plain-language summary.
- Same-session results are capped at CONJECTURE.
