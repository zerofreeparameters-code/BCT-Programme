# Gate SPECTRUM2 — RESULT

**Run:** 8 October 2026, Claude, fresh thread, one gate.
**Card:** `audit/gates/gate_SPECTRUM2_prompt.md` @ commit `d3eee7766d42bc0d93a81846cbd1523d1762e3ba`
**Card SHA-256 (hashed on disk before reading):** `d5d052c9483579ac8dcf9189d21687d5d75a201008f87c2b080841cdf1ed285c` — matches the pre-registration.
**Script:** `gate_SPECTRUM2_run.py` (SHA-256 `f7ee48ca…60d3278`). **Raw output, 40 dps:** `gate_SPECTRUM2_output.txt` (SHA-256 `bb86649c…0c9b323`).
**Method:** one loop, step thresholds, mpmath 60 dps working, 40 dps reported.

## Verdict: SC-SPEC2-1 (requirement map)

**Tier: CONJECTURE** (same-session cap). **This is a requirement, not evidence.**

| Family | C0 | C2: 1/α_s(M_P) | C1 clean PASS | MARGINAL | EXCLUDED | Survive C0–C3 | Outcome |
|---|---|---|---|---|---|---|---|
| G + T | PASS | 19.19, PASS | 20 | 4 | 12 | 20 | survives from (N_G, N_T) = (3, 2) upward |
| G + L | PASS | 43.45, PASS | 0 | 0 | 36 | 0 | killed by experiment, every row |
| G + Q | PASS | 8.79, PASS | 20 | 5 | 11 | 20 | survives from (N_G, N_Q) = (3, 2) upward |

Forty of 108 rows survive all four checks. The no-fit clause applies in full: each row has two masses tuned to two numbers, a survivor was expected, and it carries zero evidential weight. G + T and G + Q are each "one way it could be done", never "the way". The outcome is not evidence for or against BCT void geometry.

**The smallest surviving N_G is 3 in both surviving families. That is the edge of an inequality, not a prediction of three generations.** In G + Q the edge is not even sharp: the N_G = 2 rows are MARGINAL, not EXCLUDED (see below).

## Reading of MARGINAL (fixed and sent before any computation)

1. Three statuses: PASS, MARGINAL, EXCLUDED. MARGINAL is neither pass nor fail.
2. Centre: a mass below threshold is EXCLUDED; otherwise a mass below 3 × threshold is MARGINAL.
3. Corners (A_Y ± 3, A_2 ± 3): plain threshold test, applied in both directions. A centre PASS excluded at any corner becomes MARGINAL; a centre EXCLUDED that is not excluded at some corner becomes MARGINAL.
4. Sub-M_Z rows get the corner rule like any other row; their figures are flagged (†).
5. A corner with no solution (x < 0) makes the row MARGINAL.
6. MARGINAL does not count as "passes C1" for SC-SPEC2-1 nor as "fails C1" for SC-SPEC2-2.

**Effect of this reading.** All nine MARGINAL rows come from the second half of point 3: centrally EXCLUDED rows that a corner lifts above threshold. No centre-PASS row was demoted, and no row sat within a factor of 3 of a threshold at centre. The verdict code does not depend on how MARGINAL is read: 40 rows pass cleanly.

**One sensitivity, declared.** Under a stricter reading (factor of 3 also required at every corner), the five G + Q rows with N_Q = 2 would become MARGINAL, because M_Q falls to 5711 GeV at one corner, inside the 2000–6000 GeV margin. G + Q would then survive from (3, 3), G + T unchanged, verdict unchanged. I did not adopt that reading; it is recorded so the choice is visible.

## T0 — Standard-Model-only values at M_P

| | value (40 dps) |
|---|---|
| A_Y | 55.47744331681777783764450302701003634707 |
| A_2 | 49.46009370293810295328669371919047096111 |
| A_3 | 52.47705083095665044397867874123226320025 |

ln(M_P/M_Z) = 39.43577794494305122528639567994803623636. All four ingredient coefficient sets were rebuilt from field content and asserted against the card's table, including b_em = b_Y + b_2 = (4/3) Σ N_c Q².

## T1 — solution, C0 and C2 (independent of N_G, N_X)

| Family | x_G | x_X | C0 | 1/α_s(M_P) | C2 |
|---|---|---|---|---|---|
| G + T | 12.48242474628400001347001318107725817809 | 6.065110392317788594012496963619168432327 | PASS | 19.190584840865983741391976925026241392 | PASS |
| G + L | 3.3847591578073171224512677356485055296 | 60.65110392317788594012496963619168432327 | PASS | 43.45102641013713811744196477950291512131 | PASS |
| G + Q | 12.04920257540415797104054911224731757578 | 8.664443417596840848589281376598812046181 | PASS | 8.793252739749774723084839273107666936586 | PASS |

## T2 — masses and C1 status, all 108 rows

Three significant figures here; 40-digit values are in the raw output. † = a mass below M_Z, so the linear solve is invalid and the row's figures are not meaningful (EXCLUDED by the card).

**G+T** (rows N_G, columns N_X; each cell M_G / M_X in GeV, then status)

| N_G \ N_X | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| 1 | 1.06e-15 / 3.44e+02 EXCL† | 1.06e-15 / 6.48e+10 EXCL† | 1.06e-15 / 3.71e+13 EXCL† | 1.06e-15 / 8.89e+14 EXCL† | 1.06e-15 / 5.98e+15 EXCL† | 1.06e-15 / 2.13e+16 EXCL† |
| 2 | 1.14e+02 / 3.44e+02 EXCL | 1.14e+02 / 6.48e+10 EXCL | 1.14e+02 / 3.71e+13 EXCL | 1.14e+02 / 8.89e+14 EXCL | 1.14e+02 / 5.98e+15 EXCL | 1.14e+02 / 2.13e+16 EXCL |
| 3 | 5.41e+07 / 3.44e+02 MARG | 5.41e+07 / 6.48e+10 PASS | 5.41e+07 / 3.71e+13 PASS | 5.41e+07 / 8.89e+14 PASS | 5.41e+07 / 5.98e+15 PASS | 5.41e+07 / 2.13e+16 PASS |
| 4 | 3.73e+10 / 3.44e+02 MARG | 3.73e+10 / 6.48e+10 PASS | 3.73e+10 / 3.71e+13 PASS | 3.73e+10 / 8.89e+14 PASS | 3.73e+10 / 5.98e+15 PASS | 3.73e+10 / 2.13e+16 PASS |
| 5 | 1.88e+12 / 3.44e+02 MARG | 1.88e+12 / 6.48e+10 PASS | 1.88e+12 / 3.71e+13 PASS | 1.88e+12 / 8.89e+14 PASS | 1.88e+12 / 5.98e+15 PASS | 1.88e+12 / 2.13e+16 PASS |
| 6 | 2.57e+13 / 3.44e+02 MARG | 2.57e+13 / 6.48e+10 PASS | 2.57e+13 / 3.71e+13 PASS | 2.57e+13 / 8.89e+14 PASS | 2.57e+13 / 5.98e+15 PASS | 2.57e+13 / 2.13e+16 PASS |

**G+L** (rows N_G, columns N_X; each cell M_G / M_X in GeV, then status)

| N_G \ N_X | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| 1 | 7.09e+09 / 3.84e-147 EXCL† | 7.09e+09 / 2.17e-64 EXCL† | 7.09e+09 / 8.31e-37 EXCL† | 7.09e+09 / 5.14e-23 EXCL† | 7.09e+09 / 9.69e-15 EXCL† | 7.09e+09 / 3.18e-09 EXCL† |
| 2 | 2.94e+14 / 3.84e-147 EXCL† | 2.94e+14 / 2.17e-64 EXCL† | 2.94e+14 / 8.31e-37 EXCL† | 2.94e+14 / 5.14e-23 EXCL† | 2.94e+14 / 9.69e-15 EXCL† | 2.94e+14 / 3.18e-09 EXCL† |
| 3 | 1.02e+16 / 3.84e-147 EXCL† | 1.02e+16 / 2.17e-64 EXCL† | 1.02e+16 / 8.31e-37 EXCL† | 1.02e+16 / 5.14e-23 EXCL† | 1.02e+16 / 9.69e-15 EXCL† | 1.02e+16 / 3.18e-09 EXCL† |
| 4 | 5.99e+16 / 3.84e-147 EXCL† | 5.99e+16 / 2.17e-64 EXCL† | 5.99e+16 / 8.31e-37 EXCL† | 5.99e+16 / 5.14e-23 EXCL† | 5.99e+16 / 9.69e-15 EXCL† | 5.99e+16 / 3.18e-09 EXCL† |
| 5 | 1.74e+17 / 3.84e-147 EXCL† | 1.74e+17 / 2.17e-64 EXCL† | 1.74e+17 / 8.31e-37 EXCL† | 1.74e+17 / 5.14e-23 EXCL† | 1.74e+17 / 9.69e-15 EXCL† | 1.74e+17 / 3.18e-09 EXCL† |
| 6 | 3.53e+17 / 3.84e-147 EXCL† | 3.53e+17 / 2.17e-64 EXCL† | 3.53e+17 / 8.31e-37 EXCL† | 3.53e+17 / 5.14e-23 EXCL† | 3.53e+17 / 9.69e-15 EXCL† | 3.53e+17 / 3.18e-09 EXCL† |

**G+Q** (rows N_G, columns N_X; each cell M_G / M_X in GeV, then status)

| N_G \ N_X | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| 1 | 1.61e-14 / 2.78e-05 EXCL† | 1.61e-14 / 1.84e+07 EXCL† | 1.61e-14 / 1.61e+11 EXCL† | 1.61e-14 / 1.50e+13 EXCL† | 1.61e-14 / 2.28e+14 EXCL† | 1.61e-14 / 1.40e+15 EXCL† |
| 2 | 4.44e+02 / 2.78e-05 EXCL† | 4.44e+02 / 1.84e+07 MARG | 4.44e+02 / 1.61e+11 MARG | 4.44e+02 / 1.50e+13 MARG | 4.44e+02 / 2.28e+14 MARG | 4.44e+02 / 1.40e+15 MARG |
| 3 | 1.34e+08 / 2.78e-05 EXCL† | 1.34e+08 / 1.84e+07 PASS | 1.34e+08 / 1.61e+11 PASS | 1.34e+08 / 1.50e+13 PASS | 1.34e+08 / 2.28e+14 PASS | 1.34e+08 / 1.40e+15 PASS |
| 4 | 7.36e+10 / 2.78e-05 EXCL† | 7.36e+10 / 1.84e+07 PASS | 7.36e+10 / 1.61e+11 PASS | 7.36e+10 / 1.50e+13 PASS | 7.36e+10 / 2.28e+14 PASS | 7.36e+10 / 1.40e+15 PASS |
| 5 | 3.24e+12 / 2.78e-05 EXCL† | 3.24e+12 / 1.84e+07 PASS | 3.24e+12 / 1.61e+11 PASS | 3.24e+12 / 1.50e+13 PASS | 3.24e+12 / 2.28e+14 PASS | 3.24e+12 / 1.40e+15 PASS |
| 6 | 4.04e+13 / 2.78e-05 EXCL† | 4.04e+13 / 1.84e+07 PASS | 4.04e+13 / 1.61e+11 PASS | 4.04e+13 / 1.50e+13 PASS | 4.04e+13 / 2.28e+14 PASS | 4.04e+13 / 1.40e+15 PASS |

MARGINAL rows, with reason:

- G + T, (N_G ≥ 3, N_T = 1): M_T = 344 GeV at centre (excluded), but the mass band runs from 0.004 GeV to 2.8 × 10⁷ GeV, so two corners clear 1000 GeV.
- G + Q, (N_G = 2, N_Q ≥ 2): M_G = 444 GeV at centre (excluded), band 36 GeV to 5539 GeV, so two corners clear 2000 GeV.

G + L: M_L is below M_Z in all 36 rows, at centre and at all four corners. Diagnostic outside the card's tables: six doublets at the 1000 GeV floor supply at most x_L = 35.37, against 60.65 needed (42.65 at the most favourable corner). The kill does not rest on the invalid sub-M_Z figures.

## T3 — smallest passing counts and their mass band

In both surviving families the smallest passing N_G is 3 and the smallest passing N_X is 2, and the row (3, 2) itself passes.

| Row | M_G centre (GeV) | M_G band (GeV) | M_X centre (GeV) | M_X band (GeV) |
|---|---|---|---|---|
| G + T (3, 2) | 5.4057973568909157 × 10⁷ | 1.31 × 10⁷ to 2.22 × 10⁸ | 6.4801242606713788 × 10¹⁰ | 2.27 × 10⁸ to 1.85 × 10¹³ |
| G + Q (3, 2) | 1.3394047009685584 × 10⁸ | 2.49 × 10⁷ to 7.21 × 10⁸ | 1.8412587274486326 × 10⁷ | 5.71 × 10³ to 5.94 × 10¹⁰ |

The ±3 tolerance moves the generation mass by a factor of about 17 to 29 and the second ingredient's mass by five to seven orders of magnitude. The requirement fixes the counts far better than it fixes the masses.

Smallest non-excluded rows where they differ from the above: G + T (3, 1) MARGINAL; G + Q (2, 2) MARGINAL.

## T4 — C3 for every row passing C1

All 40 rows PASS C3. Neither electroweak term is zero or negative anywhere below M_P.

- 1/α_Y: smallest value at any node below M_P across the 40 rows is 20.39 (G + T, (3, 6)); largest of the row minima is 82.78.
- 1/α_2: row minima lie between 21.06 (G + T, (3, 6)) and 29.58483022 (the starting value at M_Z, which is the minimum in most rows).
- Both reach zero at M_P to within 2 × 10⁻⁵⁹ (forward run of the solved masses, a separate code path from the 2 × 2 solve), with the final-segment b_Y and b_2 positive in every row, so the approach is from above.

Per-row 40-digit minima are in the raw output. Diagnostic: C3 also passes for every non-surviving row whose masses both lie above M_Z.

## T5 — consistency with Gate LOG

1/α(0) from the Gate LOG V1 formula plus the solved content = **138.0914593921335815608471095984964472868**, for all three families.
Difference from 137.035999 = **+1.055460392133581560847109598496447286775**. Within 3 units; no notice.

The figure is the same for every family and row because the added content contributes b_em(G)·x_G + b_em(X)·x_X = A_Y + A_2 identically. It is one check, not three, and what it measures is the known mismatch of about 1 unit between Gate LOG's low-energy thresholds and the measured couplings at M_Z.

## Disclosure scored (card section 10)

| Hand estimate in card | Computed | Score |
|---|---|---|
| A_Y ≈ 55.5, A_2 ≈ 49.5, A_3 ≈ 52.5 | 55.48, 49.46, 52.48 | right |
| G + T: x_G ≈ 12.5, x_T ≈ 6.1, 1/α_s ≈ 19 | 12.48, 6.07, 19.19 | right |
| G + T: M_G ~10² (N_G = 2), 5 × 10⁷ (N_G = 3) | 114, 5.41 × 10⁷ | right |
| G + T: M_T ~3 × 10² (N_T = 1), 6 × 10¹⁰ (N_T = 2) | 344, 6.48 × 10¹⁰ | right |
| G + L: x_G ≈ 3.4, x_L ≈ 61, 1/α_s ≈ 43; M_G ~7 × 10⁹ at N_G = 1 | 3.38, 60.65, 43.45; 7.09 × 10⁹ | right |
| G + L: every row EXCLUDED | 36 of 36 EXCLUDED | right |
| G + Q: x_G ≈ 12.0, x_Q ≈ 8.7, 1/α_s ≈ 9 | 12.05, 8.66, 8.79 | right |
| G + Q: M_G ~4 × 10² (N_G = 2), 10⁸ (N_G = 3); M_Q ~2 × 10⁷ (N_Q = 2) | 444, 1.34 × 10⁸; 1.84 × 10⁷ | right |
| Survive from (3, 2) upward in G + T and G + Q | yes, both | right |
| C0 passes for all three; C3 passes wherever C1 passes | yes; yes | right |
| Expected verdict SC-SPEC2-1, G + L killed by experiment | SC-SPEC2-1, G + L killed | right |

Every disclosed estimate was confirmed. That is the expected result of a run whose analyst had already done the arithmetic by hand: the gate produced no surprise and so little new information. What the estimates did not anticipate: the nine MARGINAL rows, and the width of the mass bands.

## What the gate did and did not establish

- **Established (to CONJECTURE):** the two-condition version of the induced-light idea is not self-contradictory at one loop for two of the three menu families. It demands at least 3 whole vector-like generations at about 10⁷–10⁸ GeV or heavier, plus at least 2 triplets or 2 coloured doublets.
- **Killed:** G + L. A colourless doublet cannot close the gap with six or fewer copies.
- **Not established:** that any of this happens in nature, that α is derived, or that N_G = 3 is meaningful.
- **No experimental handle.** Every surviving mass at centre is above 10⁷ GeV, far beyond any collider. The surviving rows cannot currently be killed by experiment, which is a weakness of the requirement, not a strength.
- **Card limitations stand:** one loop only, least reliable in the last few e-folds below M_P where the condition is imposed; top threshold ignored in the electroweak running; M_P as cutoff is an assumption.

## Plain-language summary 🦜

Light's strength is really two dials added together, and for the "light comes from nothing at the Planck scale" idea both dials must read zero there. One new ingredient can only turn one knob, so we gave it two ingredients and asked what it would take.

Answer: it can be done, in two of the three recipes we allowed. Each needs at least three extra heavy copies of a full family of particles, plus at least two of a second kind. All of them would be far too heavy for any machine to see. The third recipe fails outright.

This does not explain 137. We had two free weights and two targets, so of course we could hit them. The only real news is the recipe that died, and that three families is where the sums first stop breaking, which is an edge, not a prophecy. I had guessed every number by hand before the run and they all came out as guessed, so the gate confirmed the arithmetic rather than teaching us something new.
