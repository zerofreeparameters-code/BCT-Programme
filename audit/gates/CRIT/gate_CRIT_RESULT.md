# Gate CRIT — result

**Verdict: SC-CRIT-2 (kill).**
β_c(D4, compact U(1), Wilson, triangles) = **0.610 ± 0.005**. R = **1.207** (range 1.197 to 1.217). |R − 1| = 0.207, beyond the 0.108 kill line with the uncertainty included.
**Status:** CONJECTURE (same-session result, per card section 11).
**Run:** 8 October 2026, one thread, inside the BCT project. Analyst: Claude (Opus 5.5).

---

## 0. Provenance

Commit `f89120c597fa54201c412fa78aeb04361a2df063`, fetched by commit-pinned raw URL, hashed on disk before the card was read.

| File | SHA-256 on disk | Pre-registered | Match |
|---|---|---|---|
| gate_CRIT_prompt.md | d3bbcab86fd91401a7d66196baaaa2f720e1e1a923adea513719c2adbd2cd10c | d3bbcab8…2cd10c | yes |
| CRIT/u1lat.py | 11d5ffbcc64822e3eb6bf39c6021c5dc3dff7272824f6060b5115b11069de065 | 11d5ffbc…069de065 | yes |
| CRIT/scan.py | 2823c30dee26a802fb9fa35d9b66128817268c29cc9bb320f0eb31027f24b3bf | 2823c30d…7f24b3bf | yes |

Neither script was changed. Environment: Python 3.13.16, NumPy 2.5.3, 2 CPU cores, 4 runs in parallel (the card's maximum). Every run was `python3 scan.py d4 L β n_therm n_meas seed start` with seed = 1000·L + round(1000·β), hot and cold.

Raw outputs:

| File | Runs | SHA-256 |
|---|---|---|
| stageA_L4.jsonl | 54 | be82deb4f96ac0eb689b96072719f811575f4c4ea687669f664d09847731e625 |
| stageB_L6.jsonl | 26 | cacb1961508e3fb30bad7797e7c30ad987de7d3e2acb0aa4faa2386d10a097e2 |
| stageC_L8.jsonl | 18 | fafd5cf6ec2d8e2213b4a50549273172233dc8c51742a8d368b9532e7be04212 |

**Pre-run checks** (the `__main__` block of u1lat.py, reprinted as section 5 requires):

```
hc dirs 4  staples/link 6 plaq/site 6  k 1.0                gauge invariance: 0.0
d4 dirs 12 staples/link 8 plaq/site 32 k 2.0                gauge invariance: 0.0
a4 dirs 10 staples/link 6 plaq/site 20 k 1.118033988749895  gauge invariance: 2.2e-16
```

k(D4) = 2 confirmed; 32 triangles per site and 8 per link, as section 4.1 states.

**Code read for bugs (section 4.2).** None found. One point checked because it could have been one: on D4 the sweep updates every link of a given direction at once, with no checkerboard. That is a valid heat-bath step here, because no triangle holds two links of the same direction class (r₁ = ±r₂ or r₁ = ±r₃ would make a root zero or doubled), so links of one direction never share a plaquette and their conditional distributions are independent. The hypercubic branch does need a checkerboard and has one.

## 1. Stage A — L = 4, β 0.20 to 1.50, step 0.05, 500 + 2000 sweeps

C = N_p · var(E); C_max is the larger of hot and cold.

| β | E hot | E cold | C hot | C cold | C_max |
|---|---|---|---|---|---|
| 0.20 | 0.89725 | 0.89735 | 0.510 | 0.546 | 0.546 |
| 0.25 | 0.86963 | 0.86974 | 0.540 | 0.558 | 0.558 |
| 0.30 | 0.84072 | 0.84090 | 0.615 | 0.635 | 0.635 |
| 0.35 | 0.80975 | 0.80956 | 0.632 | 0.619 | 0.632 |
| 0.40 | 0.77600 | 0.77538 | 0.738 | 0.691 | 0.738 |
| 0.45 | 0.73738 | 0.73747 | 0.788 | 0.825 | 0.825 |
| 0.50 | 0.69242 | 0.69316 | 1.084 | 0.998 | 1.084 |
| 0.55 | 0.63639 | 0.63554 | 1.260 | 1.431 | 1.431 |
| **0.60** | 0.53282 | 0.52868 | 5.158 | 6.266 | **6.266** |
| 0.65 | 0.35052 | 0.35020 | 1.037 | 1.095 | 1.095 |
| 0.70 | 0.30796 | 0.30772 | 0.715 | 0.695 | 0.715 |
| 0.75 | 0.27795 | 0.27795 | 0.504 | 0.544 | 0.544 |
| 0.80 | 0.25406 | 0.25405 | 0.428 | 0.439 | 0.439 |
| 0.85 | 0.23483 | 0.23502 | 0.331 | 0.355 | 0.355 |
| 0.90 | 0.22452 | 0.21909 | 0.289 | 0.288 | 0.289 |
| 0.95 | 0.21021 | 0.20514 | 0.254 | 0.250 | 0.254 |
| 1.00 | 0.19314 | 0.19318 | 0.220 | 0.215 | 0.220 |
| 1.05 | 0.18741 | 0.18254 | 0.215 | 0.214 | 0.215 |
| 1.10 | 0.18291 | 0.17297 | 0.176 | 0.175 | 0.176 |
| 1.15 | 0.16425 | 0.16434 | 0.170 | 0.165 | 0.170 |
| 1.20 | 0.15673 | 0.15660 | 0.139 | 0.142 | 0.142 |
| 1.25 | 0.15951 | 0.14958 | 0.131 | 0.132 | 0.132 |
| 1.30 | 0.15304 | 0.14320 | 0.115 | 0.119 | 0.119 |
| 1.35 | 0.14231 | 0.13735 | 0.114 | 0.109 | 0.114 |
| 1.40 | 0.14173 | 0.13187 | 0.098 | 0.104 | 0.104 |
| 1.45 | 0.13193 | 0.12709 | 0.092 | 0.092 | 0.092 |
| 1.50 | 0.12239 | 0.12237 | 0.090 | 0.088 | 0.090 |

**β_A = 0.60**, interior; no grid extension needed. A single peak, 4.4 times the next-highest point.

Side observation, not used: at β ≥ 0.90 hot starts sometimes sit above cold by up to 0.01 in E (e.g. 1.10, 1.25, 1.30). These are deep in the weak-coupling phase and look like trapped flux in hot starts on the small L = 4 torus. They do not touch the peak.

## 2. Stage B — L = 6, β 0.54 to 0.66, step 0.01, 2000 + 5000 sweeps

| β | E hot | E cold | C hot | C cold | C_max |
|---|---|---|---|---|---|
| 0.54 | 0.64886 | 0.64900 | 1.251 | 1.268 | 1.268 |
| 0.55 | 0.63538 | 0.63553 | 1.355 | 1.411 | 1.411 |
| 0.56 | 0.62133 | 0.62156 | 1.441 | 1.520 | 1.520 |
| 0.57 | 0.60612 | 0.60599 | 1.735 | 1.758 | 1.758 |
| 0.58 | 0.58811 | 0.58790 | 1.818 | 1.897 | 1.897 |
| 0.59 | 0.56631 | 0.56673 | 2.335 | 2.343 | 2.343 |
| 0.60 | 0.54054 | 0.54022 | 2.956 | 2.964 | 2.964 |
| **0.61** | 0.48312 | 0.49859 | 19.923 | 6.039 | **19.923** |
| 0.62 | 0.39456 | 0.39537 | 2.066 | 2.394 | 2.394 |
| 0.63 | 0.37715 | 0.37715 | 1.477 | 1.487 | 1.487 |
| 0.64 | 0.36566 | 0.36365 | 1.269 | 1.252 | 1.269 |
| 0.65 | 0.35179 | 0.35146 | 1.103 | 1.098 | 1.103 |
| 0.66 | 0.34167 | 0.34161 | 0.999 | 0.956 | 0.999 |

**β_B = 0.61**, interior; no extension. At 0.61 the hot run's 5–95% band is 0.444 to 0.514 against the cold run's 0.479 to 0.519: the hot run spent part of its time in the ordered phase. This is the only point in the gate where hot and cold starts visibly disagree.

## 3. Stage C — L = 8, β 0.590 to 0.630, step 0.005, 2000 + 4000 sweeps

| β | E hot | E cold | C hot | C cold | C_max |
|---|---|---|---|---|---|
| 0.590 | 0.56646 | 0.56638 | 2.171 | 2.249 | 2.249 |
| 0.595 | 0.55454 | 0.55421 | 2.726 | 2.733 | 2.733 |
| 0.600 | 0.54031 | 0.53982 | 2.983 | 3.374 | 3.374 |
| 0.605 | 0.52228 | 0.52336 | 3.946 | 4.314 | 4.314 |
| **0.610** | 0.49897 | 0.50168 | 5.342 | 5.397 | **5.397** |
| 0.615 | 0.40904 | 0.40811 | 4.636 | 2.880 | 4.636 |
| 0.620 | 0.39740 | 0.39583 | 2.431 | 2.232 | 2.431 |
| 0.625 | 0.38590 | 0.38598 | 1.736 | 1.773 | 1.773 |
| 0.630 | 0.37798 | 0.37777 | 1.628 | 1.482 | 1.628 |

**β_C = 0.610**, interior; no extension.

## 4. Result (section 4.4)

- **β_c ≡ β_C = 0.610.** Uncertainty = max(0.005, 2·|0.610 − 0.61|) = **0.005**.
- **E in both phases at β_C.** At β_C = 0.610 both L = 8 runs are on the strong-coupling side: E = 0.4990 (hot) and 0.5017 (cold). The weak-coupling phase first appears one grid step up, at 0.615: E = 0.409. The jump between them is ΔE ≈ 0.09, with non-overlapping 5–95% bands (0.488–0.510 at 0.610, 0.400–0.419 at 0.615). The transition therefore lies between 0.610 and 0.615 at L = 8.
- **Do hot and cold disagree at β_C?** Not at L = 8 (0.499 vs 0.502, inside each run's band). They did at L = 6, β = 0.61 (above).

Reading of the order of the transition (not a verdict input): the evidence points to **first order**. E drops by about 20% within one 0.005 step at L = 8; the L = 6 run at 0.61 shows a hot/cold split; and the L = 8 peak height (5.4) is lower than the L = 6 one (19.9), which is what happens when the larger lattice no longer tunnels between phases during a run, so each run sits in one phase and C is measured inside it. The same effect means the C-maximum estimator here marks the last grid point below the jump rather than the jump itself. Both starts put the jump in the same 0.005 interval, so this changes nothing within the stated uncertainty.

## 5. Connection to 1/α (section 5, rule fixed before the run)

    R = 2 · β_c / 1.0111

| β | R | |R − 1| | 1/α_Y(M_P) = R · 55.477 | shift in 1/α(0) |
|---|---|---|---|---|
| 0.605 | 1.1967 | 0.197 | 66.39 | +10.9 |
| **0.610** | **1.2066** | **0.207** | **66.94** | **+11.5** |
| 0.615 | 1.2165 | 0.217 | 67.49 | +12.0 |

Under the card's rule, putting the D4 critical coupling in place of the hypercubic one moves 1/α(0) up by about 11.5 units. On a hypercubic baseline that reproduces 137, the D4 lattice gives about 148 to 149.

**Thresholds in β terms:** SC-CRIT-1 needed 0.478 ≤ β_c ≤ 0.533. SC-CRIT-2 begins at β_c > 0.560 (or < 0.452). The measured 0.610 ± 0.005 is 0.05 above the kill line, about nine times the uncertainty.

**k·β at the L = 6 specific-heat peak, no verdict attached:**

| Lattice | k | β at L = 6 peak | k·β | Source |
|---|---|---|---|---|
| Hypercubic | 1 | ≈ 1.002 | ≈ 1.00 | card section 7 |
| A4 (simplicial) | 1.118 | 0.91 | 1.017 ± 0.011 | card section 7 |
| **D4** | **2** | **0.61** | **1.22** | this run, stage B |

D4 breaks the pattern the other two lattices share by about 20%.

## 6. Verdict

**SC-CRIT-2 (kill).** |R − 1| = 0.207 (0.197 at the most favourable end of the uncertainty) > 0.108.
On the BCT-shaped (D4) lattice, the Bennett–Nielsen–Froggatt critical-point route does not reproduce the needed hypercharge coupling. The value it gives is 1/α_Y(M_P) ≈ 66.9 (66.4 to 67.5), against the 55.5 the hypercubic lattice is taken to reproduce, shifting 1/α(0) by about +11.5.

## 7. Analyst's disclosure, scored

| Forecast | Predicted | Outcome | Score |
|---|---|---|---|
| Counting guess (β_c ∝ 1/plaquettes per link) | β_c 0.68 to 0.76, R 1.35 to 1.5, SC-CRIT-2 | β_c 0.610, R 1.207, SC-CRIT-2 | Right code, wrong value: β_c lies below the whole predicted band and R below its lower end. |
| Pattern guess (k·β equal across lattices) | β_c 0.50 to 0.51, R ≈ 1, SC-CRIT-1 | k·β = 1.22, not ≈ 1.0 | Wrong. |
| Analyst's lean | Pattern, 60 to 40 | | Wrong. The lean was formed after seeing the A4 validation, as disclosed. |
| Hit window | 0.478 to 0.533 | 0.610 | Missed by 0.077. |
| Order of the transition | No estimate | Appears first order | Nothing to score; recorded. |

Neither forecast rule describes D4. The measured value sits between them: further from the pattern than the counting rule's overshoot is from the measurement.

## 8. Limits (as stated in advance, and two from the run)

- Bare couplings are compared; the physical coupling at the transition was not measured. The section 5 rule assumes the bare-to-physical step is the same on both lattices; this run does not test that.
- Wilson action only. Villain or other actions would give different β_c.
- Small lattices (L = 4, 6, 8). The volume shift needed to rescue the hypothesis would have to bring β_c from 0.610 to 0.560 or below, about 8%, against about 1% on the hypercubic lattice from L = 6 to infinity.
- D4 is one of several possible four-dimensional completions of FCC; others were not run.
- *From the run:* the transition looks first order, and at L = 8 runs no longer tunnel between phases, so the specific-heat estimator locates the jump only to its grid step. Both starts agree on that step.
- *From the run:* N_p in C counts both decoupled copies held in the integer array (as the code does). This scales C but does not move its maximum.

## 9. What this does and does not say (section 8 no-fit clause)

- β_c = 0.610 ± 0.005 is a statement about compact U(1) with the Wilson action on D4 triangles. It stands whatever one thinks of section 5. As far as the card's prior-art search found, it is a new number.
- The kill is of one borrowed argument (Bennett–Nielsen–Froggatt's critical-point route) when moved to the BCT-shaped lattice. It is not a statement about α itself.
- The audited BCT model has one phase per site and no link variables. This result is not evidence for or against BCT void geometry.
- No grid, seed, estimator, constant or tolerance was changed after the run started. No grid extension was triggered.

## 10. Plain-language summary

Bennett, Nielsen and Froggatt got close to 1/137 by assuming that nature's electric-type force sits exactly at the tipping point of a lattice version of electromagnetism, and they used the tipping point of a cubic (square-box) lattice. Where that tipping point lies depends on the shape of the lattice. This gate asked: if the lattice is instead the four-dimensional shape whose slices are the BCT/FCC packing, does the tipping point land where the 137 argument needs it?

It does not. The tipping point was measured at β = 0.610, about 20% away from where it would have to be. Fed through the rule fixed before the run, the argument would give roughly 148 to 149 instead of 137, a miss of about 11 units against a tolerance of 3. The gate's own forecasts both missed too: one rule of thumb predicted a kill for the wrong reason and with the wrong number, the other predicted a pass.

What survives is the number itself: the critical coupling of compact U(1) lattice electromagnetism on this lattice, which the prior-art search did not find anywhere in the literature, and which appears to be a first-order transition.
