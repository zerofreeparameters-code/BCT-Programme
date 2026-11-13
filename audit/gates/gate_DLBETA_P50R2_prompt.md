# Gate DL-BETA P50R2 — pre-registration card (P50's β_c on a second code, with branch runs long enough to be tested)

**Programme:** BCT Cold Ledger — DL construction track.
**Card written:** 14 November 2026 AEDT (13 November, 14:15 UTC), Claude (session configured as `claude-fable-5-1`),
at Michel's request, in the session that ran Gate DL-BETA P50R (a scheduled-task cloud session), after P50R's
deliverable was pushed as commit `b127505` by Michel from his own machine.
**Status:** PRE-REGISTERED, NOT RUN.
**Type:** replication of a precision measurement on an independent code — Gate DL-BETA P50R's question, asked
again with the one defect that stopped P50R from reaching it removed. **Not blind:** P50's and P50R's results are
stated in §1. The protection is that every grid, seed, estimator, threshold and the code itself are fixed here.
**Depends on:** Gate DL-BETA (the original code), Gate DL-BETA P50 (design, estimators, result) and Gate DL-BETA
P50R (the failure this card answers). **This card's commit must contain P50R's deliverable
(`audit/gates/DLBETA_P50R/`).**

---

## 0. What the run must and must not do

- One gate per thread. Use a fresh session. Use nothing from memory, past chats or the Project's knowledge base.
- Nothing is sealed. Open only the §4.1 paths, after checking their hashes.
- The run executes the pinned code (§4.1) as written. It chooses no grid, seed, chain count, sweep budget,
  estimator or threshold. The bracket-extension rule is the only data-driven step, and the pinned driver
  applies it.
- `dlbpr2_numbers.txt` is written, hashed and its hash posted before the verdict step opens P50's or P50R's
  numbers (§4.7).

## 1. Background

Gate DL-BETA P50 (commit `9012769`, verdict SC-DLBP-1) measured β_c of compact U(1) on the FCC void network ×
time, Wilson action, β_t = β_s, on REP1's simulator:

> **β_c = 1.25771 ± 0.00107** (card convention); **1/e²_c = 0.88933 ± 0.00076**.
> β₅₀(6) = 1.25784, β₅₀(8) = 1.25775, each σ = 0.0007 (the floor). Statistical part of U: 0.00031.

That is the quoted value, a **single-code figure, CONJECTURE**.

Gate DL-BETA P50R (commit `b127505`, verdict **SC-DLBPR-5**) ran P50's design unchanged, with new seeds, on the
**other** code — Gate DL-BETA's original simulator — to move that figure to REPLICATED. It measured

> β_c(P50R) = 1.25801 ± 0.00111; D = β_c(P50R) − β_c(P50) = +0.00030 = 0.19 U_D = 0.71 σ_D;
> β₅₀(void, L = 8) = 1.25772 against P50's 1.25775.

Those numbers would have given SC-DLBPR-1 (replicated at statistical precision). They did not count, because
card §5 tests the branch runs' integrity before any comparison, and one branch run failed it: void L = 6, hot,
β = 1.2450, whose 20 block means spanned 0.00919 against the limit 0.25·G = 0.00809. P50R's result §2 and §4
diagnose it: the chain was still relaxing from its hot start when measurement began after 500 sweeps, and —
the larger point — at the hot branch point nearest the transition on each small lattice, the span a 1500-sweep
run's own block scatter *predicts* already sits at 0.9–1.06 of the limit (Z4 L = 8 at β = 0.990–0.995; void
L = 6 at β = 1.245), in P50's run as much as in P50R's. P50 escaped with worst ratios 0.90 and 0.86 at those
points; P50R escaped at Z4 L = 8 with 0.99 and tripped at void L = 6 with 1.14. The integrity rule is sound — a
branch run tunnelling between phases would show a span comparable to G, four times the limit — but a 1500-sweep
run is too short for the rule to be a test of tunnelling rather than of scatter.

Everything else in P50R passed: K1; all four K2 runs within 2 % and **bit-identical** to Gate DL-BETA's stored
series; K3 (Z4 L = 12 β₅₀ = 1.01003); no bracket extension on any lattice; every probit converged with no
bootstrap failures; cross-code branch energies with rms z of 0.77 and 1.37 on the void lattices.

This gate is P50R with **one change: the branch runs are 1500 + 4500 sweeps instead of 500 + 1500.** The
thermalisation is tripled so that a hot start near the transition has settled before measurement; the
measurement is tripled so that each of the 20 blocks is 225 sweeps and the expected span falls by √3 — from
about 1.0 of the limit at the worst point to about 0.6. Nothing else moves. If P50's β_c reappears here, the
figure moves from CONJECTURE to REPLICATED.

## 2. Questions

1. **Code and checks (Q1).** K1–K3 (§4.3).
2. **Branches (Q2).** The strong and weak branch lines on the four lattices (Z4 L = 8, 12; void L = 6, 8) and
   their integrity, as P50, now from 4500-sweep runs. Also, for every branch run, the span expected from its own
   block scatter as a fraction of the limit (§4.5 b).
3. **Crossings (Q3).** φ(β) at every window point, with every chain's f and seed, and β₅₀(L) ± σ(L) per lattice.
4. **Result (Q4).** β_c(P50R2) = β_∞(void) ± U_R, in the card convention and as 1/e²_c.
5. **Diagnostics (Q5).** All of P50's diagnostics: interpolation crossing, weak-fraction crossing, time drift,
   w and bootstrap failures. The cross-code comparisons of §4.5 (b) against P50, and the same-code comparisons
   against P50R. Reported, not verdict inputs.
6. **Calibration (Q6).** Z4 β_∞ against 1.0111331. Reported, not a verdict input.
7. **Comparison (Q7, after §4.7).** D = β_c(P50R2) − β_c(P50) against U_D and σ_D, and the verdict (§5).

## 3. Design, and why

- **R1 — one change from P50R: the branch-run length.** Branch runs are 1500 thermalisation + 4500 measurement
  sweeps, 20 blocks of 225. P50 and P50R used 500 + 1500. A longer run estimates the same quantity — the branch
  energy E(β) — with a smaller error; the lines, the integrity rule, the window chains (3000 sweeps), the
  estimators, the bootstrap (including its RNG seeds), the floor and the extension rule are P50's, executed by
  P50's own `dlbp_analysis.py`, imported unmodified. The branch errors enter the bootstrap's branch redraws, so a
  smaller σ_E gives a slightly smaller σ_boot; both void σ were at the floor in P50 and P50R and will be here.
- **R2 — the original code, unmodified, through its own entry point**, as P50R: Gate DL-BETA's `dlb_sim.py` and
  `dlb_complex.py`, called through `run_job(spec)`.
- **R3 — the integrity rule is kept, not loosened.** Raising the 0.25·G threshold would have cost nothing and
  would still have caught tunnelling. It was rejected because it reads as moving a goalpost after a failure,
  and because the longer runs also fix the slow-start problem that the threshold change would not.
- **R4 — a new seed family**, disjoint from every seed the four earlier gates used (§4.4).
- **R5 — two comparison scales**, as P50R: U_D = √(U_R² + U_P²) decides the tier; σ_D (bootstrap errors only,
  no floor) decides the label within "replicated".
- **R6 — the expected-span diagnostic.** For every branch run the numbers file reports the span its own block
  scatter predicts, 3.73 × sd(block means) (the expected range of 20 independent normal draws), as a fraction of
  the limit, beside the observed fraction. It is reported, never a verdict input. It makes the margin of the
  integrity test visible in the record, which P50 and P50R did not.
- **R7 — same-code diagnostics.** P50R and this gate run the same simulator; β_c(P50R2) − β_c(P50R), the per-
  lattice β₅₀ differences and the branch-energy z-scores against P50R say how much of any difference from P50
  is the code and how much is chance. Reported, not verdict inputs.
- **R8 — K2 against the original's stored series**, bit for bit, as P50R.
- **R9 — a clean repository**, as P50R.

## 4. Fixed rules

### 4.1 Sources, pinned

Repository `zerofreeparameters-code/BCT-Programme` at the pre-registration commit (its SHA is given in the run
prompt). **Verify every hash before reading or running the file.**

| File | SHA-256 | used for |
|---|---|---|
| `audit/gates/DLBETA_P50R2_prereg/dlbpr2_driver.py` | 4167e9f387435080599d2651b25947b0eb0bc65848ceea7f64e6b04cd47c0e5b | the driver (run as is) |
| `audit/gates/DLBETA_P50R2_prereg/dlbpr2_rules.py` | a56cbb802e6a4bc95c65fc56d8996657f642ede6750f3b744ee5011415f8bc5b | seeds, numbers, verdict (run as is) |
| `audit/gates/DLBETA_P50_prereg/dlbp_analysis.py` | 3ab1b43e44e3ace845880ceea6af66d1872b76da9637a80d5485fd5b6b57870b | P50's estimators (imported, unmodified) |
| `audit/gates/DLBETA/run/dlb_sim.py` | 4a813cf7eea0b883eaa3ced4fb6d1d10662683f6ac610077c1f85df62332ed77 | the simulator (imported, unmodified) |
| `audit/gates/DLBETA/run/dlb_complex.py` | 4aa142b0f57122b02a4590ce221d7510ca86ccff051a156ce38a1e8e75214d8a | the complexes (imported by `dlb_sim.py`) |
| `audit/gates/DLBETA/out/series/K3_series.npz` | 705bd34a814fbf38ec9e50b70ac2ae9fe46d1bfe85e439ff84046a24bd26ecf1 | K2 reference series |
| `audit/gates/DLBETA_P50/OUT/analysis.json` | 56beab6898239358164235d7cc4b28ec29a2726922c3d0f29d04f8356c9f63c1 | P50's numbers (verdict step only) |
| `audit/gates/DLBETA_P50R/OUT/analysis.json` | 5697cf580f0f841aba0154f06379d2b980ed47cb387a5cc12a59f799a2e144f1 | P50R's numbers (verdict step only; diagnostics) |
| `audit/gates/DLBETA_P50R/gate_DLBETA_P50R_RESULT.md` | 459da70ecb03321175fd43c309692b8b8cd4943729a0d0117c755f2b8d7b45d9 | the failure this card answers (§2, §4, §6) |
| `audit/gates/gate_DLBETA_P50R_prompt.md` | 767be760e0ccbfb0bd73c4da3d6748816ec77dd5f4daf0c671f9c041f9a05f3b | P50R's design, inherited here |
| `audit/gates/DLBETA_P50/gate_DLBETA_P50_RESULT.md` | 8e876e544e373a3f43de3848215c7ba092102425efaf17fac7e3b963d1362fde | background |
| `audit/gates/gate_DLBETA_P50_prompt.md` | 50525acce2f167ee78536c519562f6ea09d8aaa1768d524b2e6aaa1b483cfb9e | P50's design (§3–§4), inherited |
| `audit/gates/gate_DLBETA_prompt.md` | eae34f3becfa4c8ce798eb01f307c7560e1d1301bfb4f2e3e70d11d5c73c9024 | the model (§4.2), conventions (§4.7) |
| `audit/gates/DLBETA/gate_DLBETA_RESULT.md` | 47cff87f5a0342060cad895672fcb15b6a0b3e6b9a00dbf9b9af99d8bf7a2c8a | the original code's description (§1), K3 (§3) |

Literature: Arnold, Lippert, Neuhaus, Schilling, hep-lat/0210010 (Z4, β_c = 1.0111331(21)). Nothing else is needed.

### 4.2 The model and code

- **Model:** the original card §4.2, as in P50 and P50R: void network × time with L_t = 3L, Wilson action on
  rhombi and temporal squares, β_t = β_s, sequential single-link heat bath, no overrelaxation. Z4 with the
  standard plaquette action.
- **Simulator:** Gate DL-BETA's `dlb_sim.py` and `dlb_complex.py`, unmodified, called through
  `run_job(dict(lattice, L, Lt, beta, start, seed, n_sweeps))`, exactly as in P50R: its storage and sweep order,
  its cancellation-free Best–Fisher sampler, numba's Mersenne Twister seeded in compiled code, and its hot, cold
  and mixed starts.
- **Series:** the driver stores (E, E_s, E_t) after every sweep, as rows 1…n. Row 0 is (E at the start, NaN,
  NaN). Every reading P50 uses comes from rows ≥ 50.
- **Driver and rules:** the two pinned files, with P50's `dlbp_analysis.py` beside them. `pip install numba scipy`
  is allowed; the toolchain Gate DL-BETA recorded (Python 3.13.18, NumPy 2.5.3, SciPy 1.18.1, numba 0.68.1) is
  the one with which P50R reproduced its series bit for bit. Any number of parallel workers may be used. Every
  run is an independently seeded chain, so scheduling cannot change a number.

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

These are P50's runs (P50 card §4.4) with longer branch runs and new seeds:

| lattice | L (L_t) | S points, hot start | W points, cold start | mixed window, step 0.0025 | chains per point |
|---|---|---|---|---|---|
| Z4 | 8 | 0.980, 0.985, 0.990, 0.995 | 1.020, 1.025, 1.030, 1.035 | 1.0000 … 1.0100 (5) | 4 |
| Z4 | 12 | 0.980, 0.985, 0.990, 0.995 | 1.020, 1.025, 1.030, 1.035 | 1.0050 … 1.0150 (5) | 4 |
| void | 6 (18) | 1.230, 1.235, 1.240, 1.245 | 1.265, 1.270, 1.275, 1.280 | 1.2525 … 1.2625 (5) | 6 |
| void | 8 (24) | 1.230, 1.235, 1.240, 1.245 | 1.265, 1.270, 1.275, 1.280 | 1.2525 … 1.2625 (5) | 6 |

- **Branch runs: 1500 + 4500 sweeps**, E = the mean over the 4500 measurement sweeps, error and span from 20
  blocks of 225. **Mixed chains: 3000 sweeps.** E_end, E_mid, the 20 blocks and the extension rule are as P50.
- **Seeds:** round() is Python's, half to even, on the float 10⁴·β. c is the chain index (0 for branch runs);
  s = 0 hot, 1 cold, 2 mixed.
  - Z4: **7,000,000** + 100,000·c + 7919·L + round(10⁴·β) + s;
  - void: **8,000,000** + 100,000·c + 7919·L + round(10⁴·β) + s.

  The 212 seeds this rule can produce, counting every possible extension, run from 7,073,152 to 8,576,029. None
  coincides with any of the 1079 seeds of Gate DL-BETA (397), REP1 (410), P50 (136) or P50R (136), checked when
  this card was written. K2 reuses the original's four K3 seeds on purpose.

### 4.5 Estimators

**(a) Per lattice and extrapolation: P50 card §4.5, unchanged.** P50's `dlbp_analysis.py` executes it: the
branch lines and the integrity test (every branch run's 20-block span ≤ 0.25·G(β); each branch strictly
decreasing in β; G > 0 at every branch and window point); f, φ, the bracket test and the probit with its
convergence rule; the bootstrap (1000 replicas, RNG `default_rng(51000 + L)` for void and `(52000 + L)` for Z4,
flagged above 5 % failures); σ(L) = max(σ_boot, 0.0007); the 1/V extrapolation with k = 0.46286 (void) and
0.24615 (Z4), σ_∞, and U = √(σ_∞² + shift²); the diagnostics.

**Result:** **β_c(P50R2) = β_∞(void) ± U_R; 1/e²_c = β_c/√2 ± U_R/√2.**

**(b) Other quantities (`dlbpr2_rules.py`):**

- **σ_∞,stat** = √[((1 + k)·σ_boot,big)² + (k·σ_boot,small)²], as P50R. Printed in the numbers file.
- **Expected span** (R6): for each branch run, 3.73·√20·σ_E as a fraction of 0.25·G, beside the observed span as
  the same fraction; the worst of each per lattice. Printed in the numbers file. Reported, not a verdict input.
- **Verdict inputs** (verdict step only, from P50's pinned `analysis.json`):
  - **D** = β_c(P50R2) − β_c(P50), with β_c(P50) = 1.2577078629… and U_P = 0.0010748672…;
  - **U_D** = √(U_R² + U_P²);
  - **σ_D** = √(σ_∞,stat,R² + σ_∞,stat,P²), where σ_∞,stat,P = 0.00031 from P50's σ_boot.
- **Cross-code diagnostics against P50** (reported, not verdict inputs), as P50R: per lattice, β₅₀ differences
  in units of σ and σ_boot; z = (E_R − E_P)/√(σ_R² + σ_P²) at each of the 8 branch points, with rms and max |z|;
  φ differences at the common window points. Also the Z4 β_∞ of both gates against 1.0111331.
- **Same-code diagnostics against P50R** (R7; reported, not verdict inputs; from P50R's pinned `analysis.json`):
  β_c(P50R2) − β_c(P50R) against √(U_R² + U_P50R²) and the statistical scale; the same per-lattice β₅₀, branch
  z and φ comparisons; the Z4 β_∞.

### 4.6 Budget

Timings are P50R's own (2-core container, one chain per core): 7.0, 38.6, 71.4 and 221.4 ms/sweep on the four
lattices, K2 under 1 ms.

| lattice | sweeps | ms/sweep | core-minutes |
|---|---|---|---|
| K2 (4 runs) | 44,000 | ≤ 1 | 1 |
| Z4 L = 8: 8 branch runs (6000) + 20 chains (3000) | 108,000 | 7.0 | 13 |
| Z4 L = 12 | 108,000 | 38.6 | 70 |
| void L = 6: 8 branch runs + 30 chains | 138,000 | 71.4 | 164 |
| **void L = 8: 8 branch runs + 30 chains** | **138,000** | **221.4** | **509** |
| **total** | | | **≈ 757 (12.6 core-hours)** |

That is about 6.3 h of wall time on 2 cores, 3.0 core-hours more than P50R. Each extension at void L = 8 adds
about 66 core-minutes. Run under `nohup`. The driver checkpoints every run and is resumable. **Do not shorten
any sweep budget.**

### 4.7 Hash, then compare

1. After `DRIVER COMPLETE`, run `python3 -I dlbpr2_rules.py numbers OUT`. It writes `dlbpr2_numbers.txt` and
   `analysis.json`, opens nothing of P50's or P50R's and compares nothing.
2. Record the SHA-256 of `dlbpr2_numbers.txt` in `OUT/dlbpr2_numbers.sha256` and **post it in the conversation**.
3. Only then run
   `python3 -I dlbpr2_rules.py verdict OUT <repo>/audit/gates/DLBETA_P50/OUT/analysis.json <repo>/audit/gates/DLBETA_P50R/OUT/analysis.json`.
   It refuses to run without the hash file, or if either prior `analysis.json` does not match its pinned hash.

### 4.8 Conventions

As P50 §4.8: β is the coefficient of Σ_loops, and 1/e² = β/√2 on the void complex at β_t = β_s. Statistical
results are given to 5 decimals in β, and E to 5.

## 5. Verdict codes

Codes are applied in this order; the first that matches is the verdict.

- **SC-DLBPR2-0 (method failed).** K1, K2 or K3 failed. Nothing changes. Fix the cause, then re-run under a new
  digest.
- **SC-DLBPR2-5 (void method failed).** At void L = 6 or 8, the branches are not clean, the crossing is not
  bracketed after extensions, or the probit fit did not converge. Nothing changes; every number is reported.
  Should a branch run fail the integrity test again with 4500 measurement sweeps, the expected-span diagnostic
  (R6) says whether the rule was marginal or the run was anomalous; the next card, if any, starts there.
- **SC-DLBPR2-4 (inconclusive).** U_R > 0.0020. Nothing changes.
- **SC-DLBPR2-3 (not replicated).** |D| > 2·U_D. P50's figure stays CONJECTURE, flagged "not reproduced by a
  second code". The quoted value is unchanged until a diagnosis gate, starting from the §4.5 (b) diagnostics.
  The located transition [1.250, 1.255] is unaffected.
- **SC-DLBPR2-2 (replicated within U).** 2·σ_D < |D| ≤ 2·U_D. **P50's quoted value, β_c = 1.25771 ± 0.00107
  (1/e²_c = 0.88933 ± 0.00076), moves from CONJECTURE to REPLICATED (two codes, two sessions).** It is flagged
  that the codes differ by more than their statistical errors, which points to a code- or dynamics-dependent
  systematic of size |D|.
- **SC-DLBPR2-1 (replicated).** |D| ≤ 2·σ_D. **The same tier movement as SC-DLBPR2-2, without the flag.** The two
  codes agree at statistical precision.

Under SC-DLBPR2-1 and -2, the quoted value stays P50's. P50R2's own β_c ± U_R is recorded beside it as a
same-session figure (CONJECTURE), as P50R's already is. No average is formed: all three errors are dominated by
the same common floor. P50R's numbers remain what they were: a run that did not pass its quality test, whatever
this gate finds.

**Also reported, whatever the code:**

- D in units of U_D and of σ_D;
- the worst observed and expected span fractions on every lattice (R6);
- the cross-code diagnostics against P50 and the same-code diagnostics against P50R;
- the Z4 calibration;
- K2 bit-identity;
- the time drift.

## 6. No-fit clause

- No lattice, size, grid, chain count, sweep count, seed rule, estimator, threshold or extension rule may change
  after the run starts.
- If the pinned code contradicts this card's text, the card governs. Fix the code in the smallest way, record a
  correction notice CN-DLBPR2-nn with the old and new hashes, and re-run only what the fix affects. If the hashed
  numbers file changes, keep the first one, re-hash and re-post before the verdict step.
- Diagnostics (Q5) and the Z4 calibration (Q6) are not verdict inputs.
- Same-session results are capped at CONJECTURE. The tier movement in §5 concerns P50's figure, which was
  measured in a different session.

## 7. Validation already done (in the card's session)

- **Dry run** with `DLBP_DRYRUN=1`, in which P50's module shrinks the lattices to void L = 2, 3 and Z4 L = 4, 6
  and the mixed chains to 1000 sweeps, and this card's rules module shrinks the branch runs to 60 + 120. Seeds
  were offset by +9,000,000; 136 fixed runs and 32 extension runs took 140 s on 2 cores. It exercised K1, the K2
  path, both extension rounds on three lattices, the integrity-failure and fit-failure paths, the numbers file
  with the expected-span diagnostic, and the verdict guards: no hash file, a wrong P50 file, and a wrong P50R
  file. No gate lattice or seed was used, and its numbers are meaningless. The repository's working tree stayed
  clean (R9).
- **A typo caught by the dry run.** The first dry run stopped at K1 (SC-DLBPR2-0) because the driver's pinned
  hash for `dlb_sim.py` had one wrong character (`…b883aaa3…` for `…b883eaa3…`), a transcription error made when
  writing the driver. It was corrected from the verified value before the card was hashed; the hash in §4.1 is
  the corrected file's. The second dry run passed K1. This is recorded because it is exactly the kind of error
  §7 exists to catch, and because the card's hashes were written after it.
- **Verdict paths.** P50R's pinned `analysis.json` was used as stand-in input, with its void L = 6 integrity
  flag, β_∞, U, a fit flag or K2 altered one at a time. The verdict step returned each of SC-DLBPR2-5 (P50R as
  is), -1 (|D| = 0.0003), -2 (0.0012), -3 (0.0035), -4 (U = 0.0025), -5 (fit flag) and -0 (K2) as designed.
  With U_R ≈ U_P, 2σ_D ≈ 0.00084 and 2U_D ≈ 0.0031.
- **Seeds.** Every seed the rule can produce (212) was generated and compared with every seed in the records of
  Gate DL-BETA, REP1, P50 and P50R (1079): no overlap.
- **The simulator** passed Gate DL-BETA's K1–K5, was cross-checked against REP1 (REP1 result §9.2), and in P50R
  reproduced its own stored K3 series bit for bit.

## 8. Analyst's disclosure and forecasts

The author ran P50R and has seen all of its raw data, wrote P50R's result, and made the post-hoc analysis
(P50R result §4 and the expected-span table in that session) that identified the branch-run length as the
cause. The author made **one design choice** here — the branch-run length, 1500 + 4500 — and chose it before
any P50R2 number existed, from that analysis. The alternative of raising the integrity threshold was considered
and rejected (R3). Michel chose between the two lengths offered (1500 + 3000 and 1500 + 4500) and the threshold
change; the longer runs were recommended and chosen. Every window and branch point is P50's.

Forecasts:

- **K1–K3 pass:** 90 %.
- **K2 bit-identical to Gate DL-BETA's stored series, all four:** 85 %.
- **Every branch run passes the integrity test (worst observed span fraction ≤ 1.0 on all four lattices):** 85 %.
- **Worst expected span fraction on the void lattices ≤ 0.7:** 75 %.
- **Verdict:** SC-DLBPR2-1 58 %; -2 15 %; -5 14 %; -0 7 %; -3 3 %; -4 3 %.
- **|D| ≤ 0.0005:** 60 %.
- **|β₅₀(void, L = 8; P50R2) − 1.25775| ≤ 0.001:** 75 %.
- **|β_c(P50R2) − β_c(P50R)| ≤ 0.0005 (same code):** 60 %.
- **Branch cross-code rms z ≤ 1.5 on both void lattices, against P50:** 70 %.

**Interest.** The author has none in the number. A second failure of the integrity test would be the most
informative outcome, because it would say the margin analysis was wrong.

## 9. Known limitations

- **It replicates the code, not the method.** The estimator, grids, branch points, windows, chain counts and
  floor are P50's, so the method's own systematics are shared and untested: the fixed-time estimator, the
  straight branch lines, φ's strong-side floor (0.09–0.16 in P50 and P50R), two sizes, and a U set by its floor.
- **The branch runs are no longer P50's.** They are longer. The branch energy is the same quantity better
  measured, but a reader comparing the three gates' branch tables should expect smaller σ_E here.
- **Partly independent codes.** The two simulators were written in different threads and share the card's
  model specification, numba's RNG and the Best–Fisher method.
- **K2 bit-identity** tests the toolchain, not the physics.
- **The earlier cards' limits apply:** Wilson action only, β_t = β_s only, one spatial complex, bare couplings,
  and a tree-level k.

## 10. Run protocol

- **Session.** A fresh session, with nothing from memory, past chats or the Project's knowledge base. The result
  must say whether this was a hand-opened thread inside the BCT Project or a scheduled task. If it is a
  hand-opened thread, switch off "Search and reference past chats" and "Generate memory from chats" before
  opening it, and switch them back on afterwards. One gate per thread.
- **Card.** Fetch this card by commit-pinned raw URL with `curl` to disk. Hash it and compare with
  `audit/gates/PREREG_20261114_DLBETA_P50R2.sha256` **before reading it**. Record the digest and the commit.
- **Sources.** Get the repository at that commit and verify every §4.1 hash.
- **Run.** Copy `dlbpr2_driver.py`, `dlbpr2_rules.py` and P50's `dlbp_analysis.py` into one work directory
  outside the repository. Then run
  `nohup python3 -I dlbpr2_driver.py <repo>/audit/gates/DLBETA/run <repo>/audit/gates/DLBETA/out/series OUT [workers] > OUT/driver_stdout.txt 2>&1 &`.
  Use every core. Keep the turn alive and poll. Do not end a reply with jobs in the background.
- **After `DRIVER COMPLETE`,** follow §4.7: numbers → hash → post → verdict.
- **Deliverable:** `audit/gates/DLBETA_P50R2/gate_DLBETA_P50R2_RESULT.md`, containing:
  - the K table, with K2's bit-identity;
  - for each lattice: the branch table (E, error, span, G, observed and expected span fractions, seed),
    integrity, lines, the φ table with every chain's f and seed, β₅₀, w, σ_boot, σ and the extensions;
  - both extrapolations, with σ_∞,stat;
  - β_c(P50R2) ± U_R in both normalisations;
  - the Q5 diagnostics, including the cross-code (P50) and same-code (P50R) ones, and the Q6 calibration;
  - the SHA-256 of `dlbpr2_numbers.txt`, with the time it was posted;
  - Q7: D, U_D, σ_D, the verdict and the "also reported" items of §5;
  - the §8 forecasts, scored item by item;
  - correction notices CN-DLBPR2-nn;
  - a plain-language summary.

  Also deliver `OUT/` (records, series, state, `analysis.json`, the numbers file and its hash, the verdict file,
  the logs) and copies of the as-run card and run prompt.
- **Delivery.** If the session can push, make exactly one commit adding `audit/gates/DLBETA_P50R2/` only, on top
  of the latest main, and push it. Otherwise deliver a `git format-patch` of that commit as a file in the
  conversation. (P50R's session could not push: the repository was not in its authorised set. The patch was
  applied and pushed by Michel.)
- Same-session results are capped at CONJECTURE.
