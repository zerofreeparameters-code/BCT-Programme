# Gate SPECTRUM — ledger entry (tier decision)

**Date:** 7 October 2026. **Decided by:** Claude, at Michel's instruction ("do 1 and 2").
**Card:** `audit/gates/gate_SPECTRUM_prompt.md`, commit `5e5365b3…`, SHA-256 `69ff9dd0…7f0ca3e2`.
**Runs:** run 1 and run 2, both 7 October 2026, separate fresh threads, separate scripts
(SHA-256 `b6481ebe…598e2836` and `c3950792…01d62d2f`). All reported figures agree to 40 digits.

## What the replication covers

Same card, same model family, two threads. Run 2 did not open run 1's result until its own
numbers were out. This replicates the arithmetic and the reading of the card. It is not a
check by a different method or a different analyst, and it says nothing beyond one loop.

## Tier movements

| # | Statement | Tier | Basis |
|---|---|---|---|
| 1 | The S1–S5 figures: required M_V for N_V = 1…6, 1/α_s(M_P), 1/α₂(M_P), 1/α_Y(M_P), pole scales, under the card's one-loop rules | **Closed by replication** (arithmetic only). Same-session cap lifted for the numbers. | two fresh threads, 40 digits |
| 2 | Verdict SC-SPEC-1 | **Recorded as run, qualified: tolerance-decided.** Not promoted. | the fail rule (pole more than 100× below M_P) is not met; the card's own prose condition (both terms non-negative up to M_P) is violated by 9.4 units |
| 3 | "Whole vector-like generations at one mass complete induced light consistently" | **Not supported. OPEN**, referred to Gate SPECTRUM2. | under the sum condition, rows 3–6 give 1/α₂(M_P) = +10.50 and 1/α_Y(M_P) = −9.45; the split of 19.95 is the same in every row |
| 4 | The 7 October proposal: N_V = 3 at 9.089 × 10¹² GeV gives 1/α = 137 | **FALSIFIED** under the card's formula. | it gives 81.06; the formula requires 6.3 × 10⁵ GeV |
| 5 | "Light is induced at the Planck scale" (the idea itself) | **CONJECTURE, unchanged.** | neither Gate LOG nor Gate SPECTRUM tests the idea, only two ways of completing it |
| 6 | BCT void geometry | **No movement.** | card section 8 |

## Standing sentences

- Every M_V is one parameter tuned to one number and carries zero evidential weight.
- The smallest surviving N_V equals 3. That is the edge of an inequality, not a prediction of
  three generations.
- The analyst's forecast of the verdict (SC-SPEC-3) was wrong, and is recorded as wrong.

## Why item 2 is not promoted

The card contains two yardsticks. Measured in 1/α, the hypercharge miss is three times the
card's 3-unit inconclusive band. Measured in scale, it is well inside the factor-100 fail line.
The verdict follows the written fail rule. A verdict that flips with the choice of yardstick
is a statement about the card, not about the physics, so it stays as recorded and no claim is
built on it. Gate SPECTRUM2 replaces the yardstick before any new number is computed.
