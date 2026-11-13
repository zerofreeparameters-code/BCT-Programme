# Gate DL-BETA P50R — pre-registration card (P50's β_c on a second code)

**Programme:** BCT Cold Ledger — DL construction track.
**Card written:** 13 November 2026, Claude (Opus 5.5), at Michel's request ("Yes"). It was written in the session
that ran Gate DL-BETA P50 (a scheduled-task cloud session), after P50's deliverable was pushed as commit
`9012769f98bcc388f7b4c6cb2dc77d4d852a894a`.
**Status:** PRE-REGISTERED, NOT RUN.
**Type:** replication of a precision measurement on an independent code. **Not blind:** P50's result is stated
in §1. The protection is that every grid, seed, estimator, threshold and the code itself are fixed here, so the
run makes no choices.
**Depends on:** Gate DL-BETA (the original code), Gate DL-BETA REP1, and Gate DL-BETA P50 (design, estimators,
result). **This card's commit must contain P50's deliverable (`audit/gates/DLBETA_P50/`).**

---

## 0. What the run must and must not do

- One gate per thread. Use a fresh session. Use nothing from memory, past chats or the Project's knowledge base.
- Nothing is sealed. Open only the §4.1 paths, after checking their hashes.
- The run executes the pinned code (§4.1) as written. It chooses no grid, seed, chain count, sweep budget,
  estimator or threshold. The bracket-extension rule is the only data-driven step, and the pinned driver
  applies it.
- `dlbpr_numbers.txt` is written, hashed and its hash posted before the verdict step opens P50's numbers (§4.7).

## 1. Background

Gate DL-BETA P50 (commit `9012769`, verdict SC-DLBP-1) measured β_c of compact U(1) on the FCC void network ×
time. It used the Wilson action with β_t = β_s, in the model of `audit/gates/gate_DLBETA_prompt.md` §4.2. Each
window point had many 3000-sweep mixed-start chains, each scored on a continuous scale. A probit was fitted per
lattice, the error came from a bootstrap with a floor, and the result was extrapolated in 1/V from L = 6 and 8:

> **β_c = 1.25771 ± 0.00107** (card convention); **1/e²_c = 0.88933 ± 0.00076**.
> β₅₀(6) = 1.25784, β₅₀(8) = 1.25775, each σ = 0.0007 (the floor; σ_boot = 0.00032 and 0.00018).
> Statistical part of β_c's error alone: 0.00031. Z4 control: 1.01144 ± 0.00134 (+0.23 U from 1.0111331).

That figure is P50's quoted value. It is a **single-code figure, CONJECTURE**: it ran on REP1's simulator in one
session. The transition's location, [1.250, 1.255] at L = 4 and 6, is already REPLICATED: the original code and
REP1 found it independently.

This gate runs P50's design unchanged on the **other** code: Gate DL-BETA's original simulator. That simulator
was written in a different thread, with its own complex construction, storage and sweep order, sampler algebra
and start procedure. Both codes pass their K-checks, and their energies agree run by run (REP1 result §9.2). If
P50's β_c reappears here, the figure moves from CONJECTURE to REPLICATED.

## 2. Questions

1. **Code and checks (Q1).** K1–K3 (§4.3).
2. **Branches (Q2).** The strong and weak branch lines on the four lattices (Z4 L = 8, 12; void L = 6, 8) and
   their integrity, as P50.
3. **Crossings (Q3).** φ(β) at every window point, with every chain's f and seed, and β₅₀(L) ± σ(L) per lattice.
4. **Result (Q4).** β_c(P50R) = β_∞(void) ± U_R, in the card convention and as 1/e²_c.
5. **Diagnostics (Q5).** All of P50's diagnostics: interpolation crossing, weak-fraction crossing, time drift,
   w and bootstrap failures. Also the cross-code comparisons of §4.5 (b). Reported, not verdict inputs.
6. **Calibration (Q6).** Z4 β_∞ against 1.0111331. Reported, not a verdict input.
7. **Comparison (Q7, after §4.7).** D = β_c(P50R) − β_c(P50) against U_D and σ_D, and the verdict (§5).

## 3. Design, and why

- **R1 — only the simulator and the seeds change.** The lattices, sizes, branch points, windows, step, chain
  counts, sweep counts, readings, extension rule, estimators, bootstrap (including its RNG seeds) and floor are
  P50's. They are executed by P50's own `dlbp_analysis.py`, imported unmodified. A difference in β_c can
  therefore come only from the code or from chance.
- **R2 — the original code, unmodified, through its own entry point.** Gate DL-BETA's `dlb_sim.py` and
  `dlb_complex.py` are called through `run_job(spec)`, exactly as its own driver called them.
- **R3 — two comparison scales.** U_D = √(U_R² + U_P²) carries both quoted uncertainties, including P50's
  conservative floor. It decides the tier. σ_D uses only the two bootstrap errors (no floor). The floor stands
  for where the grid points sit, and the grid is identical in both runs, so it is common to both and cancels in D.
  σ_D therefore tests whether the codes agree at statistical precision. It decides only the label within
  "replicated" (§5).
- **R4 — K2 against the original's own stored series.** K2 re-runs Gate DL-BETA's four K3 runs with its seeds.
  It reports whether each series is bit-identical to the original's stored series, comparing exact bits. This
  avoids P50's CN-DLBP-01, where `array_equal` mishandled NaN.
- **R5 — cross-code diagnostics.** The 32 branch points are identical in the two gates, so their energies can be
  compared point by point (z-scores). Should the verdict be SC-DLBPR-3, they say whether the two codes simulate
  different energies or only move differently in time.
- **R6 — a clean repository.** The driver sets `sys.dont_write_bytecode` and points numba's cache into the work
  directory. Running the original code then writes nothing into the repository.

## 4. Fixed rules

### 4.1 Sources, pinned

Repository `zerofreeparameters-code/BCT-Programme` at the pre-registration commit (its SHA is given in the run
prompt). **Verify every hash before reading or running the file.**

| File | SHA-256 | used for |
|---|---|---|
| `audit/gates/DLBETA_P50R_prereg/dlbpr_driver.py` | c97eb0614fbf738b4091c8dc89e73f726bdd5fa89448b0702a3daefdbd9ca01f | the driver (run as is) |
| `audit/gates/DLBETA_P50R_prereg/dlbpr_rules.py` | 51c78401e3acf27963dbbb338bdb995dbc5e7343a362867b19b52f9ecc10734c | seeds, numbers, verdict (run as is) |
| `audit/gates/DLBETA_P50_prereg/dlbp_analysis.py` | 3ab1b43e44e3ace845880ceea6af66d1872b76da9637a80d5485fd5b6b57870b | P50's estimators (imported, unmodified) |
| `audit/gates/DLBETA/run/dlb_sim.py` | 4a813cf7eea0b883eaa3ced4fb6d1d10662683f6ac610077c1f85df62332ed77 | the simulator (imported, unmodified) |
| `audit/gates/DLBETA/run/dlb_complex.py` | 4aa142b0f57122b02a4590ce221d7510ca86ccff051a156ce38a1e8e75214d8a | the complexes (imported by `dlb_sim.py`) |
| `audit/gates/DLBETA/out/series/K3_series.npz` | 705bd34a814fbf38ec9e50b70ac2ae9fe46d1bfe85e439ff84046a24bd26ecf1 | K2 reference series |
| `audit/gates/DLBETA_P50/OUT/analysis.json` | 56beab6898239358164235d7cc4b28ec29a2726922c3d0f29d04f8356c9f63c1 | P50's numbers (verdict step only) |
| `audit/gates/DLBETA_P50/gate_DLBETA_P50_RESULT.md` | 8e876e544e373a3f43de3848215c7ba092102425efaf17fac7e3b963d1362fde | background |
| `audit/gates/gate_DLBETA_P50_prompt.md` | 50525acce2f167ee78536c519562f6ea09d8aaa1768d524b2e6aaa1b483cfb9e | P50's design (§3–§4), inherited here |
| `audit/gates/gate_DLBETA_prompt.md` | eae34f3becfa4c8ce798eb01f307c7560e1d1301bfb4f2e3e70d11d5c73c9024 | the model (§4.2), conventions (§4.7) |
| `audit/gates/DLBETA/gate_DLBETA_RESULT.md` | 47cff87f5a0342060cad895672fcb15b6a0b3e6b9a00dbf9b9af99d8bf7a2c8a | the original code's description (§1), K3 (§3) |

Literature: Arnold, Lippert, Neuhaus, Schilling, hep-lat/0210010 (Z4, β_c = 1.0111331(21)). Nothing else is needed.

### 4.2 The model and code

- **Model:** the original card §4.2, as in P50: void network × time with L_t = 3L, Wilson action on rhombi and
  temporal squares, β_t = β_s, sequential single-link heat bath, no overrelaxation. Z4 with the standard
  plaquette action.
- **Simulator:** Gate DL-BETA's `dlb_sim.py` and `dlb_complex.py`, unmodified, called through
  `run_job(dict(lattice, L, Lt, beta, start, seed, n_sweeps))`. Everything below is the original's, as documented
  in those files:
  - storage and sweep order: void slice-major, with the spatial links oct-major in offset product order, then
    the temporal links; Z4 site-major, μ = 0…3;
  - the cancellation-free Best–Fisher sampler;
  - numba's Mersenne Twister, seeded in compiled code;
  - the starts. Hot is uniform. Cold is all zero, with no draws. Mixed sets to zero the links whose origin has
    t < L_t/2 (void) or x₁ < L/2 (Z4), and draws the others uniformly in storage order.
- **Series:** the driver stores (E, E_s, E_t) after every sweep, as rows 1…n. Row 0 is (E at the start, NaN, NaN),
  because `run_job` returns only the starting E. Every reading P50 uses comes from rows ≥ 50.
- **Driver and rules:** the two pinned files, with P50's `dlbp_analysis.py` beside them. `pip install numba scipy`
  is allowed. Any number of parallel workers may be used. Every run is an independently seeded chain, so
  scheduling cannot change a number.

### 4.3 Checks

- **K1 — code identity.** The five code files match §4.1. The driver re-checks `dlb_sim.py`, `dlb_complex.py` and
  `dlbp_analysis.py` and stops on a mismatch. It also records the K2 reference file's hash.
- **K2 — limits.** The driver re-runs Gate DL-BETA's four K3 runs with its seeds and sweeps (1000 + 10,000):
  - void L = 2 (L_t = 6): β = 0.1 hot, seed 516838; β = 20 cold, seed 715839;
  - Z4 L = 4: β = 0.1 hot, seed 32676; β = 20 cold, seed 231677.

  Each passes within 2 % of its target: ⟨cos θ⟩ = I₁/I₀(0.1) = 0.049938 at β = 0.1; E = 0.014258 (void) or
  0.012451 (Z4) at β = 20. The run also reports whether E, E_s and E_t are **bit-identical** to the original's
  stored series, comparing exact bits through a `uint64` view. That is not a pass condition.
- **K3 — Z4 control.** As P50: at Z4 L = 12 the branches are clean, the crossing is bracketed after extensions,
  and the probit fit converges with β₅₀ in [1.0051, 1.0171].

### 4.4 Runs

These are P50's runs (P50 card §4.4) with new seeds:

| lattice | L (L_t) | S points, hot start | W points, cold start | mixed window, step 0.0025 | chains per point |
|---|---|---|---|---|---|
| Z4 | 8 | 0.980, 0.985, 0.990, 0.995 | 1.020, 1.025, 1.030, 1.035 | 1.0000 … 1.0100 (5) | 4 |
| Z4 | 12 | 0.980, 0.985, 0.990, 0.995 | 1.020, 1.025, 1.030, 1.035 | 1.0050 … 1.0150 (5) | 4 |
| void | 6 (18) | 1.230, 1.235, 1.240, 1.245 | 1.265, 1.270, 1.275, 1.280 | 1.2525 … 1.2625 (5) | 6 |
| void | 8 (24) | 1.230, 1.235, 1.240, 1.245 | 1.265, 1.270, 1.275, 1.280 | 1.2525 … 1.2625 (5) | 6 |

- **Branch runs:** 500 + 1500 sweeps. **Mixed chains:** 3000 sweeps. E_end, E_mid, the 20 blocks and the
  extension rule are as P50.
- **Seeds:** round() is Python's, half to even, on the float 10⁴·β. c is the chain index (0 for branch runs);
  s = 0 hot, 1 cold, 2 mixed.
  - Z4: **5,000,000** + 100,000·c + 7919·L + round(10⁴·β) + s;
  - void: **6,000,000** + 100,000·c + 7919·L + round(10⁴·β) + s.

  The 212 seeds this rule can produce, counting every possible extension, run from 5,073,152 to 6,576,029. None
  coincides with any of the 943 seeds of Gate DL-BETA, REP1 or P50 (checked when this card was written). K2 reuses
  the original's four K3 seeds on purpose.

### 4.5 Estimators

**(a) Per lattice and extrapolation: P50 card §4.5, unchanged.** P50's `dlbp_analysis.py` executes it. That
covers:

- the branch lines and the integrity test;
- f, φ, the bracket test and the probit with its convergence rule;
- the bootstrap: 1000 replicas, RNG `default_rng(51000 + L)` for void and `(52000 + L)` for Z4, flagged above 5 %
  failures;
- σ(L) = max(σ_boot, 0.0007);
- the 1/V extrapolation with k = 0.46286 (void) and 0.24615 (Z4), σ_∞, and U = √(σ_∞² + shift²);
- the diagnostics.

**Result:** **β_c(P50R) = β_∞(void) ± U_R; 1/e²_c = β_c/√2 ± U_R/√2.**

**(b) New quantities (`dlbpr_rules.py`):**

- **σ_∞,stat** = √[((1 + k)·σ_boot,big)² + (k·σ_boot,small)²], the statistical error of β_∞ with no floor.
  It is printed in the numbers file.
- **Verdict inputs** (verdict step only, from P50's pinned `analysis.json`):
  - **D** = β_c(P50R) − β_c(P50), with β_c(P50) = 1.2577078629… and U_P = 0.0010748672…;
  - **U_D** = √(U_R² + U_P²);
  - **σ_D** = √(σ_∞,stat,R² + σ_∞,stat,P²), where σ_∞,stat,P = 0.00031 from P50's σ_boot.
- **Cross-code diagnostics** (reported, not verdict inputs). For each lattice:
  - β₅₀(P50R) − β₅₀(P50), in units of both σ (with the floor) and σ_boot;
  - z = (E_R − E_P)/√(σ_R² + σ_P²) at each of the 8 branch points, with rms and max |z|;
  - φ(P50R) − φ(P50) at the common window points.

  Also the Z4 β_∞ of both gates against 1.0111331.

### 4.6 Budget

Timings are Gate DL-BETA's own (2-core container, one chain per core; P50's environment ran REP1's code about
20 % faster than REP1 had recorded):

| lattice | sweeps | ms/sweep | core-minutes |
|---|---|---|---|
| K2 (4 runs) | 44,000 | ≤ 1 | 1 |
| Z4 L = 8: 8 branch runs + 20 chains | 76,000 | 7.6 | 10 |
| Z4 L = 12 | 76,000 | 42 | 54 |
| void L = 6: 8 branch runs + 30 chains | 106,000 | 75 | 133 |
| **void L = 8: 8 branch runs + 30 chains** | **106,000** | **236** | **417** |
| **total** | | | **≈ 615 (10.3 core-hours)** |

That is about 5.1 h of wall time on 2 cores. Each extension at void L = 8 adds about 71 core-minutes. Run under
`nohup`. The driver checkpoints every run and is resumable. **Do not shorten any sweep budget.**

### 4.7 Hash, then compare

1. After `DRIVER COMPLETE`, run `python3 -I dlbpr_rules.py numbers OUT`. It writes `dlbpr_numbers.txt` and
   `analysis.json`, opens nothing of P50's and compares nothing.
2. Record the SHA-256 of `dlbpr_numbers.txt` in `OUT/dlbpr_numbers.sha256` and **post it in the conversation**.
3. Only then run `python3 -I dlbpr_rules.py verdict OUT <repo>/audit/gates/DLBETA_P50/OUT/analysis.json`. It
   refuses to run without the hash file, or if P50's `analysis.json` does not match its pinned hash.

### 4.8 Conventions

As P50 §4.8: β is the coefficient of Σ_loops, and 1/e² = β/√2 on the void complex at β_t = β_s. Statistical
results are given to 5 decimals in β, and E to 5.

## 5. Verdict codes

Codes are applied in this order; the first that matches is the verdict.

- **SC-DLBPR-0 (method failed).** K1, K2 or K3 failed. Nothing changes. Fix the cause, then re-run under a new
  digest.
- **SC-DLBPR-5 (void method failed).** At void L = 6 or 8, the branches are not clean, the crossing is not
  bracketed after extensions, or the probit fit did not converge. Nothing changes; every number is reported.
- **SC-DLBPR-4 (inconclusive).** U_R > 0.0020: the second code's result is too broad to test P50's. Nothing
  changes.
- **SC-DLBPR-3 (not replicated).** |D| > 2·U_D. P50's figure stays CONJECTURE, flagged "not reproduced by a second
  code". The quoted value is unchanged until a diagnosis gate, starting from the §4.5 (b) diagnostics. The located
  transition [1.250, 1.255] is unaffected.
- **SC-DLBPR-2 (replicated within U).** 2·σ_D < |D| ≤ 2·U_D. **P50's quoted value, β_c = 1.25771 ± 0.00107
  (1/e²_c = 0.88933 ± 0.00076), moves from CONJECTURE to REPLICATED (two codes, two sessions).** It is flagged
  that the codes differ by more than their statistical errors, which points to a code- or dynamics-dependent
  systematic of size |D|.
- **SC-DLBPR-1 (replicated).** |D| ≤ 2·σ_D. **The same tier movement as SC-DLBPR-2, without the flag.** The two
  codes agree at statistical precision.

Under SC-DLBPR-1 and -2, the quoted value stays P50's. P50R's own β_c ± U_R is recorded beside it as a
same-session figure (CONJECTURE). No average is formed: both errors are dominated by the same common floor.

**Also reported, whatever the code:**

- D in units of U_D and of σ_D;
- the cross-code diagnostics;
- the Z4 calibration;
- K2 bit-identity;
- the time drift.

## 6. No-fit clause

- No lattice, size, grid, chain count, sweep count, seed rule, estimator, threshold or extension rule may change
  after the run starts.
- If the pinned code contradicts this card's text, the card governs. Fix the code in the smallest way, record a
  correction notice CN-DLBPR-nn with the old and new hashes, and re-run only what the fix affects. If the hashed
  numbers file changes, keep the first one, re-hash and re-post before the verdict step.
- Diagnostics (Q5) and the Z4 calibration (Q6) are not verdict inputs.
- Same-session results are capped at CONJECTURE. The tier movement in §5 concerns P50's figure, which was
  measured in a different session.

## 7. Validation already done (in the card's session)

- **Dry run** with `DLBP_DRYRUN=1`, in which P50's module shrinks the lattices to void L = 2, 3 and Z4 L = 4, 6
  and the sweeps to 20 + 40 and 1000. Seeds were offset by +9,000,000; 172 runs took 2.4 min. It exercised:
  - K1;
  - the K2 path;
  - both extension rounds, on all four lattices;
  - the integrity-failure and fit-failure paths and the bootstrap-failure flag;
  - the numbers file;
  - the verdict guards: no hash file, and a wrong P50 hash.

  No gate lattice or seed was used, and its numbers are meaningless. The repository's working tree stayed clean
  (R6).
- **K2 comparison unit test.** Short runs with a non-gate seed were written to a reference file in the stored
  format (`<tag>__E/__Es/__Et`). The comparison returned "identical" for the exact series and "not identical"
  after a one-ulp change, on both void and Z4.
- **Verdict paths.** P50's own `analysis.json` was used as stand-in input, with β_∞, U, a fit flag or K2 altered.
  The verdict step returned each of SC-DLBPR-1, -2, -3, -4, -5 and -0 as designed:
  - |D| = 0.0002 gave -1;
  - 0.0012 gave -2;
  - 0.0035 gave -3.

  With U_R ≈ U_P, 2σ_D = 0.00087 and 2U_D = 0.00304.
- **The simulator** passed Gate DL-BETA's K1–K5 and was cross-checked against REP1 (REP1 result §9.2).

## 8. Analyst's disclosure and forecasts

The author ran P50 and has seen all of its raw data. To write the driver, the author read the original code
(`dlb_sim.py`, `dlb_complex.py`) and Gate DL-BETA's result §0–§3. The author made no design choice here: every
window and branch point is P50's.

Forecasts:

- **K1–K3 pass:** 90 %.
- **K2 bit-identical to Gate DL-BETA's stored series, all four:** 80 %. The toolchain recorded by Gate DL-BETA
  (Python 3.13.18, NumPy 2.5.3, SciPy 1.18.1, numba 0.68.1) is the one with which P50 reproduced REP1 bit for bit.
- **Verdict:** SC-DLBPR-1 55 %; -2 25 %; -0 7 %; -5 5 %; -3 5 %; -4 3 %.
- **|D| ≤ 0.0005:** 55 %.
- **|β₅₀(void, L = 8; P50R) − 1.25775| ≤ 0.001:** 70 %.
- **Branch cross-code rms z ≤ 1.5 on both void lattices:** 70 %.

**Interest.** The author has none in the number. A failure to replicate would be as informative as a success.

## 9. Known limitations

- **It replicates the code, not the method.** The estimator, grids, branch points, windows, chain counts and
  floor are P50's. The method's own systematics are therefore shared and untested: the fixed-time estimator, the
  straight branch lines, φ's strong-side floor of 0.11–0.16 seen in P50, two sizes, and a U set by its floor.
- **Partly independent codes.** The two simulators were written in different threads. The original was written
  from the card; REP1 was written blind to the original's code. They share the card's model specification,
  numba's RNG and the Best–Fisher method.
- **K2 bit-identity** tests the toolchain, not the physics.
- **The earlier cards' limits apply:** Wilson action only, β_t = β_s only, one spatial complex, bare couplings,
  and a tree-level k.

## 10. Run protocol

- **Session.** A fresh session, with nothing from memory, past chats or the Project's knowledge base. The result
  must say whether this was a hand-opened thread inside the BCT Project or a scheduled task. If it is a
  hand-opened thread, switch off "Search and reference past chats" and "Generate memory from chats" before
  opening it, and switch them back on afterwards. One gate per thread.
- **Card.** Fetch this card by commit-pinned raw URL with `curl` to disk. Hash it and compare with
  `audit/gates/PREREG_20261113_DLBETA_P50R.sha256` **before reading it**. Record the digest and the commit.
- **Sources.** Get the repository at that commit and verify every §4.1 hash.
- **Run.** Copy `dlbpr_driver.py`, `dlbpr_rules.py` and P50's `dlbp_analysis.py` into one work directory outside
  the repository. Then run
  `nohup python3 -I dlbpr_driver.py <repo>/audit/gates/DLBETA/run <repo>/audit/gates/DLBETA/out/series OUT [workers] > OUT/driver_stdout.txt 2>&1 &`.
  Use every core. Keep the turn alive and poll. Do not end a reply with jobs in the background.
- **After `DRIVER COMPLETE`,** follow §4.7: numbers → hash → post → verdict.
- **Deliverable:** `audit/gates/DLBETA_P50R/gate_DLBETA_P50R_RESULT.md`, containing:
  - the K table, with K2's bit-identity;
  - for each lattice: the branch table (E, error, span, G, seed), integrity, lines, the φ table with every chain's
    f and seed, β₅₀, w, σ_boot, σ and the extensions;
  - both extrapolations, with σ_∞,stat;
  - β_c(P50R) ± U_R in both normalisations;
  - the Q5 diagnostics, including the cross-code ones, and the Q6 calibration;
  - the SHA-256 of `dlbpr_numbers.txt`, with the time it was posted;
  - Q7: D, U_D, σ_D, the verdict and the "also reported" items of §5;
  - the §8 forecasts, scored item by item;
  - correction notices CN-DLBPR-nn;
  - a plain-language summary.

  Also deliver `OUT/` (records, series, state, `analysis.json`, the numbers file and its hash, the verdict file,
  the logs) and copies of the as-run card and run prompt.
- **Delivery.** If the session can push, make exactly one commit adding `audit/gates/DLBETA_P50R/` only, on top of
  the latest main, and push it. Otherwise deliver a `git format-patch` of that commit as a file in the
  conversation.
- Same-session results are capped at CONJECTURE.
