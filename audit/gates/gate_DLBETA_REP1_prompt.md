# Gate DL-BETA REP1 — pre-registration card (blind replication)

**Programme:** BCT Cold Ledger — DL construction track.
**Card written:** 12 November 2026, Claude (Opus 5.5), at Michel's request ("replication card pls"), in
the thread that ran Gate DL-BETA, after that gate's deliverable had been pushed (commit
`abf7b1e8562a974ed2dd04c47b91fab2d81e6ce4`).
**Status:** PRE-REGISTERED, NOT RUN.
**Type:** independent blind replication (a second code in a second thread) of Gate DL-BETA's
measurement of β_c, with two pre-registered method fixes (§3). The original procedure is also scored
on the replication's own runs, so the two runs can be compared like for like.
**Depends on:** Gate DL-BETA (its card, for the model and method; its result, sealed until §4.7),
Gate CRIT2 (checks §4, method §5), Gate LATT (conventions §2, order diagnostics §4.5).

---

## 0. Blinding (read this first)

This card's author ran Gate DL-BETA and has seen its result. **That result, its verdict and every
number in it are deliberately not stated anywhere in this card.** The repository at the
pre-registration commit contains them under `audit/gates/DLBETA/`. They are sealed until §4.7.

Until the run has written its own `dlbr_numbers.txt` and recorded and posted its SHA-256 (§4.7), it
must **not** open, print, search or list the contents of:

- anything under `audit/gates/DLBETA/` other than `dlb_deskcheck.py` (itself only after the run's own
  K1 numbers are recorded, as in the original card §4.3) and `dlb_deskcheck_output.txt`;
- any Project document, chat or memory about Gate DL-BETA other than this card and its PREREG record.

Do not run repository-wide searches (`grep -r`, `find … -exec cat`, `git log -p`, `git show` on the
DL-BETA commit) that could print sealed content; open only the paths listed in §4.1. If any sealed
material is seen early, say so in the deliverable: the run continues, but it **cannot score
SC-DLBR-1**.

## 1. Background

Gate DL-BETA (card `audit/gates/gate_DLBETA_prompt.md`, pre-registered 12 Nov 2026, run the same day)
measured the transition coupling β_c of compact U(1), Wilson action, on the FCC void network × time
with β_t = β_s. That gate's card §1 states the complex and its desk-checked properties, its §4.2
specifies the model, its §4.3 the checks K1–K5, and its §4.4 the method (CRIT2 §5, adapted). **This
card uses all of them as written there, except where §3 below says otherwise.**

The original run was a single code in a single thread, so its number stands at CONJECTURE (that card
§5, §8). This gate is the blind replication that card names as the next step.

## 2. Questions

1. **The complex (Q1).** Build the (3+1)D complex independently from the original card's §4.2 and
   pass K1 (that card §4.3), recording the run's own K1 numbers before opening `dlb_deskcheck.py`.
2. **The code (Q2).** Pass K2–K5 (that card §4.3, verbatim, with this card's seeds §4.3).
3. **β_c (Q3, blind).** Measure β_∞ and its uncertainty by the original method with this card's
   changes (§4.4), in the card convention and as 1/e²_c = β_∞/√2.
4. **Order (Q4).** The original card's §4.4 step 7, with hysteresis also tested at L = 6 (§4.4 step 7).
   Reported, not a verdict input.
5. **Anisotropy record (Q5).** E_s and E_t separately, their ratio either side of β_∞ and at β = 20.
   Recorded, not interpreted.
6. **Secondary scoring (Q6, blind).** The original card's fixed-band outcome rule applied to this run's
   own mixed-phase runs, with the β_mix values and the verdict that the original card's §5 would give.
   Reported, not a verdict input.
7. **Comparison (Q7, after §4.7).** The replication against the original's sealed numbers; the verdict
   (§5).

## 3. Changes from the original card, and why

Each change is fixed here, before the run. None depends on the original's numbers.

- **C1 — branch-relative outcome rule (primary).** The original scores a mixed-phase run against a
  fixed band of ±0.01 around E\*, the mean of the two ends of the L = 6 jump interval. A run that ends
  in a pure phase is scored "unresolved" whenever that phase's energy lies within 0.01 of E\*. That
  happens whenever the gap between the phases is not large compared with 0.02, or E\* is not centred
  between them (for example when one end of the jump interval is a part-melted run). C1 instead asks
  which phase the end state is in, by its position between the two phase branches measured at L = 6
  (§4.4 step 4). The original rule is still applied to every mixed run, as Q6.
- **C2 — the L = 6 scan uses both starts and a wider grid** (β₄ ± 0.030, hot and cold). This gives the
  branch data C1 needs on both sides of the jump, and a hysteresis test at L = 6.
- **C3 — exhaustive verdict codes.** Every outcome maps to exactly one code (§5); the last code is
  "anything else".
- **C4 — the wording of the original card is fixed** where a run must otherwise choose a reading
  (§4.5, R1–R9).
- **C5 — new seeds** (§4.3), so no random stream is shared with the original, even by accident.

Disclosure: C1 was written by an author who has seen the original run's raw data. Its parameters are
round choices: four grid points per branch, straight lines, thirds of the gap. **It cannot be applied
to the original data,** which has no hot-start L = 6 scan, and the author has not applied it to
anything.

## 4. Fixed rules

### 4.1 Sources, pinned

Repository `zerofreeparameters-code/BCT-Programme` at the pre-registration commit (the commit that adds
this card; its SHA is given in the run prompt). **Verify every hash before reading the file.**

| File | SHA-256 | used for |
|---|---|---|
| `audit/gates/gate_DLBETA_prompt.md` | eae34f3becfa4c8ce798eb01f307c7560e1d1301bfb4f2e3e70d11d5c73c9024 | the model §1, §4.2; checks §4.3; method §4.4; conventions §4.7 |
| `audit/gates/PREREG_20261112_DLBETA.sha256` | 941aaf107274510af9eb395935b6efd102ed7f8cccdfa9fac3c85edb4b27eca7 | the original card's record |
| `audit/gates/DLBETA/dlb_deskcheck.py` | 93de5d29f05c25b57fad8e7b37c6994958215b229b241188efeb1c2402407d71 | K1 cross-check, **only after own K1 is recorded** |
| `audit/gates/DLBETA/dlb_deskcheck_output.txt` | 10d58dbbb45d3c118880d1f437c38166f946e66772152d613011fe765fc150ae | K1–K3 targets, any time |
| `audit/gates/gate_CRIT2_prompt.md` | b30436875a2b12ea9b38a4d5d366c1ab9fcad83bcfe0405b3af5974876df4c79 | checks §4 (K4, K5), method §5 |
| `audit/gates/CRIT2/gate_CRIT2_RESULT.md` | 25b2653cb4623897b33d84e62141cd377bf301237a314516ef7b7117e08c09ce | Z4 reference values; CRIT2's readings of its own wording |
| `audit/gates/gate_LATT_prompt.md` | 1dccde5b3160121d2297f5de906aeb787ceeda9ddfd933e162b9385e7cb45cdd | conventions §2, order diagnostics §4.5 |

**Sealed until §4.7** (verify these hashes when opening them, not before):

| File | SHA-256 |
|---|---|
| `audit/gates/DLBETA/out/dlb_numbers.txt` | 5f60f1d7b660b5407352846d30c63354b883a81313aa9a9fc984ffa55fec8aae |
| `audit/gates/DLBETA/gate_DLBETA_RESULT.md` | 47cff87f5a0342060cad895672fcb15b6a0b3e6b9a00dbf9b9af99d8bf7a2c8a |

Literature: Arnold, Lippert, Neuhaus, Schilling, hep-lat/0210010 (Z4, β_c = 1.0111331(21)).
**Nothing else** from the repository, the Project, past chats or memory. Everything else under
`audit/gates/DLBETA/` (the original run's code, outputs, series, manifest and as-run copies) stays
closed for the whole run; it is not needed.

### 4.2 The model and code

As the original card §4.2, **written in the run thread from that specification**, without the original
run's code (sealed). `pip install numba` is allowed. Storage order, sweep order and the von Mises
sampler are the run's own and are recorded in code before the first run.

### 4.3 Checks and seeds

- **K1–K5:** the original card §4.3, verbatim, including the order (own K1 recorded and hashed before
  `dlb_deskcheck.py` is opened) and the SC codes it names, which map here to SC-DLBR-0 and SC-DLBR-4.
- **Seeds:** Z4: 7919·L + round(10⁴·β) + s **+ 300,000**. Void: 7919·L + round(10⁴·β) + s **+ 700,000**.
  s = 0 hot, 1 cold, 2 mixed, 3 histogram. round() is Python's, half to even, applied to the float
  10⁴·β. Every seed is printed in the raw records.

### 4.4 Void runs (the original card §4.4, with C1 and C2)

1. **Locate** (L = 2, L_t = 6): as the original step 1.
2. **Fine scan** (L = 4, L_t = 12): as the original step 2. Report the jump interval for each start.
3. **Scan** (L = 6, L_t = 18) — **changed (C2).** **Hot and cold**, β₄ − 0.030 to β₄ + 0.030 step
   0.005 (13 points), 500 + 1500 sweeps.
   - **Jump interval (L = 6) = [β_lo, β_hi]**, the adjacent pair with the largest fall in E, cold
     start, as in the original. Also report the hot-start jump interval.
   - **E\*** = mean of cold-start E at β_lo and β_hi (used only by the Q6 rule).
   - **Located** if β₄ is interior to its (extended) L = 4 grid and the L = 6 cold-start fall at
     [β_lo, β_hi] exceeds 3·√(σ_lo² + σ_hi²) (20-block errors).
   - **Branches.** S(β) is the least-squares straight line through the **hot-start** E at β_lo − 0.020,
     β_lo − 0.015, β_lo − 0.010, β_lo − 0.005. W(β) is the line through the **cold-start** E at
     β_hi + 0.005, β_hi + 0.010, β_hi + 0.015, β_hi + 0.020. If any of these points lies outside the
     grid, extend the L = 6 scan (both starts) by 0.005 steps on that side until it does not.
4. **Mixed-phase starts** (L = 6 and L = 8; L_t = 18 and 24): initial state, run length, readings and
   grids as the original step 4. L = 6: (β_lo + β_hi)/2 ± 0.0075, step 0.0025 (7 points). L = 8:
   β_mix(6) ± 0.005, step 0.0025 (5 points). 2000 sweeps each.
   - **End state** E_end = mean of the 10 readings after sweeps 1550, 1600, …, 2000.
   - **Primary outcome (C1).** f = (S(β) − E_end)/(S(β) − W(β)). **Strong wins** if f < 1/3, **weak
     wins** if f > 2/3, **unresolved** otherwise. If S(β) − W(β) ≤ 0 the point is unresolved and
     flagged.
   - **β_mix(L)** = midpoint of S and W, where S is the highest β with a strong win and W the lowest β
     with a weak win. The flip interval is [min(S, W), max(S, W)]; if S > W the pattern is flagged
     non-monotonic. Unresolved points between S and W lie inside the interval.
   - **Extensions** as the original, driven by the primary outcome: with no weak win, add one 0.0025
     step above; with no strong win, one step below; at most 8 per size, then stop that size and
     report.
   - **Secondary outcome (Q6).** For every mixed run, also report the original rule: weak if
     E_end < E\* − 0.01, strong if E_end > E\* + 0.01, unresolved otherwise. Report β_mix(6) and
     β_mix(8) on the same grids under that rule, if they exist. It triggers no extensions.
5. **Result** (primary outcome): **β_∞ = β_mix(8)**; uncertainty u = max(half the L = 8 flip interval,
   |β_mix(8) − β_mix(6)|); **1/e²_c = β_∞/√2**. ΔE(L = 8) = E_end of the nearest strong-win run below
   β_∞ minus that of the nearest weak-win run above it. Check, not headline: the line through
   (1/(L³L_t), β_mix(L)) for L = 6, 8, evaluated at 0.
   - **Resolved** if an L = 8 flip exists with at most one unresolved L = 8 point and u ≤ 0.010.
   - **The replication's β^R:** β_∞ if an L = 8 flip exists; otherwise (β_lo + β_hi)/2.
6. **Histogram** (L = 6, L_t = 18) at β = β_mix(6) (primary), as the original step 6 (2000 + 20,000
   sweeps, seed s = 3). If no L = 6 primary flip exists, at (β_lo + β_hi)/2.
7. **Order (Q4).** As the original step 7, except that (a) holds if hysteresis is found at L = 4
   **or** L = 6 (hot and cold jump intervals differ, or hot and cold E differ by more than 3σ at some
   grid point). Reported, not a verdict input.

### 4.5 Readings fixed in advance (C4)

- **R1.** "Within 0.05 of an edge" (locate) means |β₀ − edge| ≤ 0.05.
- **R2.** "C maximum" means the larger of hot and cold C at each grid point. Ties go to the lower β.
- **R3.** The fall over an adjacent pair (β_i, β_{i+1}) is E(β_i) − E(β_{i+1}). Ties go to the lower β.
- **R4.** Z4 mixed start (K5): links whose origin site has first coordinate x₁ < L/2 start at θ = 0.
  K5 passes iff the flip interval meets [1.0051, 1.0171]. No flip among the five fixed points means
  K5 fails.
- **R5.** E\*_hc (K4) is as CRIT2 defines it: mean of cold-start E at the two ends of the cold-start
  pair with the largest fall.
- **R6.** Statistics are over measurement sweeps only. E errors use 20 equal blocks (σ of block means
  /√20). C = N_loops·var(E), population variance. C errors use the 20-block jackknife.
- **R7.** "Two peaks" (histogram: 50 equal bins over [min E, max E] of the 20,000 measurement sweeps).
  A peak is a bin whose count is the maximum within ±5 bins (the first bin of a plateau) and at least
  10 % of the largest count. There are two peaks iff two such bins exist with a bin between them whose
  count is below half the smaller of the two.
- **R8.** The jump at L = 4 and L = 6 is the cold-start fall at the jump interval. "Shrinks by more
  than 30 %" means ΔE(8) < 0.7 × jump(4).
- **R9.** Runs that depend only on completed stages may be scheduled concurrently (for example the
  step-6 histogram with the L = 8 mixed runs). Every run is an independently seeded chain, so
  scheduling cannot change a number. Stage decisions are made in order.

### 4.6 Budget

Timings from the original card §4.5 (reference code, numba, one simulation per core):

| stage | sweeps | ms/sweep | core-minutes |
|---|---|---|---|
| K4 (Z4 L = 8) | 88,000 | 7.5 | 11 |
| K5 (Z4 L = 12) | 10,000 | 37.7 | 6 |
| locate (L = 2) | 755,000 | 0.92 | 12 |
| fine scan (L = 4) | 252,000 | 15.2 | 64 |
| **scan (L = 6), hot and cold, 13 points** | **52,000** | 74.3 | **64** |
| mixed L = 6 | 14,000 | 74.3 | 17 |
| mixed L = 8 | 10,000 | 241.7 | 40 |
| histogram (L = 6) | 22,000 | 74.3 | 27 |
| **total** | | | **≈ 240 (4 core-hours)** |

About 2 to 3 hours of wall time on 2 cores, plus any grid extensions. Run under `nohup`, checkpoint to
disk after every stage, resumable. **Do not shorten any sweep budget to fit a session.**

### 4.7 Hash, then unblind

Write every Q3 number (β₀; β₄; the L = 4 jump intervals; the L = 6 hot and cold jump intervals;
E\*; the branch lines S and W with their points; the primary outcome and f of every mixed run;
β_mix(6) and β_mix(8) with their intervals; β_∞; u; 1/e²_c; ΔE; Resolved yes or no; β^R) and every Q6
number (the secondary outcomes and β_mix values) to `dlbr_numbers.txt`. **Record its SHA-256 in the
deliverable and post it in the conversation before opening either sealed file.** Then verify the two
sealed hashes (§4.1), read `dlb_numbers.txt`, and read the original result as needed for Q7.

### 4.8 Conventions

As the original card §4.7: β is the coefficient of Σ_loops; 1/e² = kβ with k = 1/√2 on the void
complex at β_t = β_s. Numbers to 4 decimals for β (give the exact grid value in brackets when rounding
loses digits), 5 for E.

## 5. Verdict codes (C3)

**I_O** is the original's interval [β_∞ − u, β_∞ + u], read from its `dlb_numbers.txt` (the lines
`beta_inf` and `uncertainty`). If that file has no `beta_inf` line, I_O is its L = 6 jump interval.
**d** is the distance from β^R to I_O, which is 0 if β^R lies inside it.

Codes are applied in this order; the first that matches is the verdict.

- **SC-DLBR-4 (card defect).** The desk check's geometry is wrong (the original card §4.3). The gate
  is unposable as specified.
- **SC-DLBR-0 (method failed).** A K2–K5 check failed. No void number. Re-run after the fix under a
  new digest.
- **SC-DLBR-5 (no transition signal in [0.20, 4.00]).** No interior C maximum at L = 2 after the
  allowed extensions, or not Located (§4.4 step 3).
- **SC-DLBR-1 (replicated).** Resolved, and d ≤ 0.005. Gate DL-BETA's located transition moves from
  CONJECTURE to **REPLICATED (two codes, two threads)**. This run's β_∞ ± u becomes the quoted value
  (a single-code figure, CONJECTURE as a figure, as CRIT2 quoted its β_∞). Not available if sealed
  material was seen early (§0).
- **SC-DLBR-2 (not replicated).** d > 0.010. Gate DL-BETA's number stays at CONJECTURE and is marked
  **contested**; a third run is needed.
- **SC-DLBR-3 (inconclusive).** Anything else, for example not Resolved with d ≤ 0.010, or
  0.005 < d ≤ 0.010. Gate DL-BETA's number stays at CONJECTURE.

**Also reported, whatever the code:** whether this run's L = 6 cold jump interval equals or overlaps
the original's; whether the Q6 rule reproduces the original's own resolution status (the original
card's §5 code under that rule); and the difference between the two β_∞ values.

## 6. No-fit clause

- No lattice, size, convention, grid, sweep count, seed rule, estimator, threshold, tolerance or branch
  rule may change after the run starts. Grid extensions only as written in §4.4.
- Neither the order call nor the Q6 outcome is a verdict input.
- Same-session results are capped at CONJECTURE. REPLICATED requires the two-thread condition of §5.

## 7. Validation already done

None new. K1's targets and the K3 limits are the original card's desk check (§4.1; 49 assertions).
This card adds no code. The branch rule C1 has not been run on any data (§3).

## 8. Analyst's disclosure (this card is not blind on its author's side)

The author ran Gate DL-BETA, wrote its result, and has seen its raw data. To keep the run blind, the
forecasts below say nothing about the original's numbers, verdict, order call or anisotropy record.

- **Checks K1–K5 pass:** 92 %.
- **Verdict:** SC-DLBR-1 60 %; SC-DLBR-3 27 %; SC-DLBR-2 6 %; SC-DLBR-0 5 %; SC-DLBR-4 or -5 2 %.
- **β^R inside I_O (d = 0):** 75 %.
- **Resolved under the primary rule:** 70 %.

**Interest.** The author wrote the result under test. A failed or inconclusive replication will be
recorded as such. The author has no stake in the number: it turns CN-DL-06 into a statement with a
number in it, whatever the number is.

## 9. Known limitations

- Those of the original card §10: Wilson action only; β_t = β_s only; one spatial complex; bare
  couplings; a lattice β_c with a tree-level k.
- Two mixed-phase sizes, as in the original. No L = 10, so this gate tests the original's measurement,
  not its finite-size extrapolation.
- C1 assumes two phase branches that are close to straight over 0.015 in β and extrapolated by up to
  about 0.02. Curvature near the jump shifts f by a fraction of the gap. The thirds rule tolerates
  that; very strong curvature would show up as unresolved points, and is reported, not repaired.

## 10. Run protocol

- Fresh thread inside the BCT Project. Before opening it, switch off "Search and reference past chats"
  and "Generate memory from chats"; switch them back on afterwards. One gate per thread.
- Fetch this card by commit-pinned raw URL with `curl` to disk; hash it and compare with
  `audit/gates/PREREG_20261112_DLBETA_REP1.sha256` **before reading it**. Record the digest and the
  commit.
- Get the repository at the pre-registration commit (a single-commit `git fetch --depth 1` is
  sufficient and preferred). Verify every §4.1 source hash before reading the source. Do not open
  sealed files (§0).
- Order: Q1 (own K1 recorded and hashed before `dlb_deskcheck.py` is opened), then K2–K5, then the
  §4.4 stages in order, then the §4.7 hash, posted, then unblind, then Q4–Q7.
- Deliverable: `audit/gates/DLBETA_REP1/gate_DLBETA_REP1_RESULT.md` containing:
  - the K-check table and every stage table;
  - the branch lines and every mixed run's f and both outcomes;
  - β_∞ in both normalisations, u, ΔE, Resolved, and β^R;
  - the SHA-256 of `dlbr_numbers.txt`, with the time it was posted;
  - Q4, Q5 and Q6;
  - Q7: I_O, d, the verdict, and the "also reported" items of §5;
  - the §8 forecasts scored item by item;
  - correction notices CN-DLBR-nn;
  - a plain-language summary.

  Also deliver the code, the raw time series (JSONL or npz, hashed) and a copy of the as-run prompt.
  The session cannot push: deliver a `git format-patch` bundle adding `audit/gates/DLBETA_REP1/` only.
- Delivery notes from the original run:
  - The raw series make the patch about 30 MB. The Google Drive connector refuses uploads above about
    3 MB per call, so send the patch in the conversation as a file.
  - If an HTTPS `git push` of a pack this size fails with HTTP 400, push with
    `git -c http.postBuffer=524288000 -c http.version=HTTP/1.1 push`.
- Same-session results are capped at CONJECTURE.
