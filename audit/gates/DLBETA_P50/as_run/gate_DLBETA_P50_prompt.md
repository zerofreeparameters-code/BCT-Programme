# Gate DL-BETA P50 — pre-registration card (β_c with a statistical error)

**Programme:** BCT Cold Ledger — DL construction track.
**Card written:** 13 November 2026, Claude (Opus 5.5), at Michel's request ("Go pls"), in the thread that
ran Gate DL-BETA REP1, after REP1's deliverable was produced (the format-patch adding
`audit/gates/DLBETA_REP1/`; its commit SHA is set when it is applied).
**Status:** PRE-REGISTERED, NOT RUN.
**Type:** precision measurement. **Not blind:** both prior results are stated in §1. The protection is
that every grid, seed, estimator, threshold and the code itself are fixed here, so the run makes no choices.
**Depends on:** Gate DL-BETA (model, method, result); Gate DL-BETA REP1 (simulator, result). **This card's
commit must contain REP1's deliverable (`audit/gates/DLBETA_REP1/`).**

---

## 0. What the run must and must not do

- One gate per thread; a fresh thread; nothing from memory, past chats or the Project's knowledge base.
- Nothing is sealed. Open only the §4.1 paths, after checking their hashes.
- The run executes the pinned code (§4.1) as written. It does not choose a grid, a seed, a chain count, a
  sweep budget, an estimator or a threshold. The bracket-extension rule (§4.4) is the only data-driven
  step, and it is applied by the pinned driver.
- `dlbp_numbers.txt` is written and hashed, and the hash posted, before the verdict step compares anything
  with the prior gates (§4.7).

## 1. Background

Both prior gates measured β_c of compact U(1) (Wilson action, FCC void network × time, β_t = β_s, the
model of `audit/gates/gate_DLBETA_prompt.md` §4.2):

| gate | L = 4 and L = 6 jump interval | β_∞ (card convention) | verdict |
|---|---|---|---|
| DL-BETA (original code) | [1.250, 1.255] | 1.25375 ± 0.0050 | SC-DLB-2: located, not resolved |
| DL-BETA REP1 (second code, blind) | [1.250, 1.255] | 1.25875 ± 0.0025 | SC-DLBR-1: replicated |

The location is solid: two codes, two threads, identical jump intervals, and energies that agree run by
run. **The number is not.** Both gates ran one 2000-sweep mixed-start chain per β and sorted each into
strong, weak or unresolved by hard cuts, and their u is a grid rule with no statistical part. REP1's
"Resolved" rested on two L = 8 outcomes that sat on their cuts. On REP1's own errors each had a 0.49 and
0.41 chance of falling the other way, and either change would have made that verdict SC-DLBR-3 (REP1
result §9.1). REP1's quoted figure, 1.25875 ± 0.0025, is CONJECTURE.

This gate measures β_c with a statistical error. It scores many chains per β on a continuous scale and
validates the same estimator on Z4, where the answer is known.

## 2. Questions

1. **Code and checks (Q1).** K1–K3 (§4.3).
2. **Branches (Q2).** The strong and weak branch lines on four lattices (Z4 L = 8, 12; void L = 6, 8) and
   their integrity (§4.5).
3. **Crossings (Q3).** φ(β) on every window point, with every chain's f and seed, and β₅₀(L) ± σ(L) for each
   lattice (§4.5).
4. **Result (Q4).** β_c = β_∞(void) ± U, in the card convention and as 1/e²_c = β_c/√2.
5. **Diagnostics (Q5).** The linear-interpolation crossing of φ, the weak-fraction crossing, the
   mid-length crossing (time drift), the fitted width w and bootstrap failures. Reported, not verdict
   inputs.
6. **Calibration (Q6).** Z4 β_∞ from L = 8 and 12 against 1.0111331 (hep-lat/0210010). Reported, not a
   verdict input.
7. **Comparison (Q7, after §4.7).** β_c against both prior intervals; the verdict (§5).

## 3. Design, and why

- **D1 — many chains per β.** 6 independent mixed-start chains at each void window point and 4 at each
  Z4 point, 3000 sweeps each, in place of one 2000-sweep chain.
- **D2 — a continuous score, no "unresolved" class.** Each chain's end state is scored by its position
  between the branches, f = (S(β) − E_end)/(S(β) − W(β)) (REP1's C1 position, without its thirds). A
  part-mixed chain contributes where it is, so no single chain can flip the result. φ(β) is the mean f
  over chains.
- **D3 — a fitted crossing with a real error.** β₅₀(L) is where a normal-CDF (probit) curve, fitted to
  every chain's f, crosses ½. Its error comes from a bootstrap over chains and branch points, with a floor
  of one grid step's uniform spread (0.0007).
- **D4 — two sizes and an extrapolation.** β_∞ = 1/V extrapolation through L = 6 and 8 (first-order
  scaling). The quoted uncertainty U includes the whole extrapolation shift as a systematic.
- **D5 — a known-answer control.** The identical estimator on Z4 at L = 8 and 12. K3 requires
  β₅₀(Z4, L = 12) in REP1's K5 window [1.0051, 1.0171]. The extrapolation is compared with 1.0111331 (Q6).
- **D6 — pinned code.** REP1's simulator, unmodified, driven by this card's `dlbp_driver.py` and scored by
  `dlbp_analysis.py` (§4.1). The card text governs: if the code contradicts it, §6 applies.

**Disclosure.** The windows and branch points were placed using both prior gates' data, by an author who
ran REP1 (§8). The estimator was tested only on synthetic data and in a dry run on tiny lattices (§7).

## 4. Fixed rules

### 4.1 Sources, pinned

Repository `zerofreeparameters-code/BCT-Programme` at the pre-registration commit (its SHA is given in
the run prompt). **Verify every hash before reading or running the file.**

| File | SHA-256 | used for |
|---|---|---|
| `audit/gates/DLBETA_P50_prereg/dlbp_driver.py` | 29e7e175ecbaffc80b164ed0b3de6572d5f85f219906da230d0ee2f960aaa8db | the driver (run as is) |
| `audit/gates/DLBETA_P50_prereg/dlbp_analysis.py` | 3ab1b43e44e3ace845880ceea6af66d1872b76da9637a80d5485fd5b6b57870b | grids, seeds, estimators, verdict (run as is) |
| `audit/gates/DLBETA_REP1/run/dlbr_sim.py` | 560c256fe391bfa7b0a2bf4e5abc520f8179b75647ece51006b5cba82425c9e6 | the simulator (imported, unmodified) |
| `audit/gates/DLBETA_REP1/out/series/k3_void_L2_b0.1_hot.npz` | c2644f4f8a3b22d8bfb12ff836b112617c104912ebf0e3b99aa4e4b5dadbb5e6 | K2 reference series |
| `audit/gates/DLBETA_REP1/out/series/k3_void_L2_b20_cold.npz` | f0e56479ef94957f0caf3c639a28c1ed8273406c4a56b63cd4cf89dff3530a05 | K2 reference series |
| `audit/gates/DLBETA_REP1/out/series/k3_z4_L4_b0.1_hot.npz` | 13a97af95ba6079ad9718962bae1acb19b3438730197470f3b93de40a4956d6c | K2 reference series |
| `audit/gates/DLBETA_REP1/out/series/k3_z4_L4_b20_cold.npz` | f000756dbcc5e3bcac3a75dd17a35c163422fab664941ceecce792b945baffeb | K2 reference series |
| `audit/gates/gate_DLBETA_prompt.md` | eae34f3becfa4c8ce798eb01f307c7560e1d1301bfb4f2e3e70d11d5c73c9024 | the model (§4.2), conventions (§4.7) |
| `audit/gates/DLBETA_REP1/gate_DLBETA_REP1_RESULT.md` | 92ca88b37610bed2b99e74d4ffb618629091863ba815b5457c121f8c630f4e72 | background (REP1's code §1, timings, §9.1) |
| `audit/gates/DLBETA/gate_DLBETA_RESULT.md` | 47cff87f5a0342060cad895672fcb15b6a0b3e6b9a00dbf9b9af99d8bf7a2c8a | background |

Literature: Arnold, Lippert, Neuhaus, Schilling, hep-lat/0210010 (Z4, β_c = 1.0111331(21)). Nothing else
is needed.

### 4.2 The model and code

- **Model:** the original card §4.2. Void network × time with L_t = 3L, Wilson action on rhombi and temporal
  squares, β_t = β_s, sequential single-link heat bath, no overrelaxation. Z4 with the standard plaquette
  action.
- **Simulator:** REP1's `dlbr_sim.py`, unmodified, through `get_lattice(kind, L)` and
  `run_chain(seed, start, mask, β, n, …)`. Storage order, sweep order, the von Mises sampler and the
  mixed-start masks are REP1's, as documented in that file. The mixed start sets links whose origin has
  t < L_t/2 (void) or x₁ < L/2 (Z4) to θ = 0, and draws the others uniformly.
- **Driver and analysis:** the two pinned files. `pip install numba scipy` is allowed. Any number of
  parallel workers may be used. Every run is an independently seeded chain, so scheduling cannot change a
  number.

### 4.3 Checks

- **K1 — code identity.** The three code files match §4.1. The driver re-checks `dlbr_sim.py` and stops on
  a mismatch.
- **K2 — limits.** REP1's four K3 runs are re-run with REP1's seeds and sweeps (1000 + 10,000):
  - void L = 2 (L_t = 6): β = 0.1 hot, seed 716838; β = 20 cold, seed 915839;
  - Z4 L = 4: β = 0.1 hot, seed 332676; β = 20 cold, seed 531677.

  Each passes within 2 % of its target: ⟨cos θ⟩ = I₁/I₀(0.1) = 0.049938 at β = 0.1, and E = rank
  ∂₂/(2β N_loops) = 0.014258 (void) or 0.012451 (Z4) at β = 20. Whether each series is **bit-identical** to
  REP1's stored series is also reported. That tests whether this environment matches REP1's; it is not a
  pass condition.
- **K3 — Z4 control.** At Z4 L = 12, three things must hold: the branches are clean (§4.5), the crossing is
  bracketed after extensions, and the probit fit converges with β₅₀ in [1.0051, 1.0171].

### 4.4 Runs

| lattice | L (L_t) | S points, hot start | W points, cold start | mixed window, step 0.0025 | chains per point |
|---|---|---|---|---|---|
| Z4 | 8 | 0.980, 0.985, 0.990, 0.995 | 1.020, 1.025, 1.030, 1.035 | 1.0000 … 1.0100 (5) | 4 |
| Z4 | 12 | 0.980, 0.985, 0.990, 0.995 | 1.020, 1.025, 1.030, 1.035 | 1.0050 … 1.0150 (5) | 4 |
| void | 6 (18) | 1.230, 1.235, 1.240, 1.245 | 1.265, 1.270, 1.275, 1.280 | 1.2525 … 1.2625 (5) | 6 |
| void | 8 (24) | 1.230, 1.235, 1.240, 1.245 | 1.265, 1.270, 1.275, 1.280 | 1.2525 … 1.2625 (5) | 6 |

- **Branch runs:** one chain per S or W point, 500 + 1500 sweeps. E is the mean over the 1500 measurement
  sweeps; its error uses 20 equal blocks (sample sd of block means / √20).
- **Mixed chains:** 3000 sweeps from the mixed start, with E recorded after every sweep.
  - **E_end** = mean of E after sweeps 2550, 2600, …, 3000.
  - **E_mid** = mean after sweeps 1050, …, 1500 (diagnostic only).
- **Seeds** (round() is Python's, half to even, on the float 10⁴·β; c = chain index, 0 for branch runs;
  s = 0 hot, 1 cold, 2 mixed):
  - Z4: 3,000,000 + 100,000·c + 7919·L + round(10⁴·β) + s;
  - void: 4,000,000 + 100,000·c + 7919·L + round(10⁴·β) + s.

  Every seed appears in the raw records. Apart from K2, which re-runs REP1's chains on purpose, no seed
  coincides with any seed of REP1.
- **Extensions:** applied only after all fixed runs, lattice by lattice. If φ at the lowest window point
  exceeds ½, add one 0.0025 step below; if φ at the highest is below ½, add one step above. New points get
  the full chain count. Repeat once more. At most 2 extensions per lattice.

### 4.5 Estimators

- **Branch lines:** S(β) and W(β) are unweighted least-squares straight lines through the four hot and the
  four cold branch E. G(β) = S(β) − W(β).
- **Integrity:** a lattice's branches are **clean** iff all three hold:
  - every branch run's 20 block means span at most 0.25·G at its β;
  - the S values strictly decrease with β, and so do the W values;
  - G > 0 at every window point.
- **Score:** f = (S(β) − E_end)/(S(β) − W(β)) per chain. φ(β) = mean f; σ_φ = sd/√n.
- **Bracketed** iff φ(lowest point) ≤ ½ ≤ φ(highest point).
- **β₅₀(L):** a least-squares fit of Φ((β − β₅₀)/w) to every chain-level f of the lattice, with w > 0 (fitted
  as log w).
  - Start values: β₅₀ = the mean of φ's linear-interpolation crossings (or the window centre if there are
    none); w = 0.003.
  - **Converged** iff the solver succeeds, 10⁻⁵ ≤ w ≤ 0.1, and β₅₀ lies within the grid ± 0.01.
- **σ(L) = max(σ_boot, 0.0007).** σ_boot is the sd of β₅₀ over 1000 bootstrap replicas. Each replica
  resamples the chains with replacement within each β, redraws every branch E as E + σ_E·N(0, 1), and refits
  the lines. The RNG is `numpy.random.default_rng(51000 + L)` for void and `(52000 + L)` for Z4. More than
  5 % non-converged replicas is flagged.
- **Extrapolation:**
  - x = 1/V, with V = L³·3L (void) or L⁴ (Z4); k = x_big/(x_small − x_big). That gives k = 0.46286 for
    void 6 → 8 and 0.24615 for Z4 8 → 12.
  - β_∞ = β₅₀(big) − k·(β₅₀(small) − β₅₀(big)).
  - σ_∞ = √[((1 + k)·σ_big)² + (k·σ_small)²].
  - **U = √(σ_∞² + (k·(β₅₀(small) − β₅₀(big)))²).**
- **Result:** **β_c = β_∞(void) ± U; 1/e²_c = β_c/√2 ± U/√2.**
- **Diagnostics (Q5),** reported, not verdict inputs:
  - φ's linear-interpolation crossings (more than one means non-monotone);
  - the crossing of the weak fraction (chains with f > ½);
  - β₅₀ from E_mid, giving the drift β₅₀ − β₅₀(mid);
  - the fitted w;
  - bootstrap failures.

### 4.6 Budget

Timings are REP1's (2-core container, one chain per core):

| lattice | sweeps | ms/sweep | core-minutes |
|---|---|---|---|
| K2 (4 runs) | 44,000 | ≤ 1 | 1 |
| Z4 L = 8: 8 branch runs + 20 chains | 76,000 | 8.7 | 11 |
| Z4 L = 12 | 76,000 | 53 | 67 |
| void L = 6: 8 branch runs + 30 chains | 106,000 | 85 | 150 |
| **void L = 8: 8 branch runs + 30 chains** | **106,000** | **255** | **451** |
| **total** | | | **≈ 680 (11.3 core-hours)** |

That is about 5.7 h of wall time on 2 cores, 3 h on 4, and 1.5 h on 8. Each extension adds up to
77 core-minutes at void L = 8. Run under `nohup`; the driver checkpoints every run and is resumable. **Do
not shorten any sweep budget.**

### 4.7 Hash, then compare

1. After `DRIVER COMPLETE`, run `python3 -I dlbp_analysis.py numbers OUT`. This writes `dlbp_numbers.txt`
   and `analysis.json`; neither contains any comparison with the prior gates.
2. Record the SHA-256 of `dlbp_numbers.txt` in `OUT/dlbp_numbers.sha256` and **post it in the
   conversation**.
3. Only then run `python3 -I dlbp_analysis.py verdict OUT`, which refuses to run without the hash file.

### 4.8 Conventions

As the original card §4.7: β is the coefficient of Σ_loops, and 1/e² = β/√2 on the void complex at
β_t = β_s. Statistical results are given to 5 decimals in β, and E to 5.

## 5. Verdict codes

Codes are applied in this order; the first that matches is the verdict.

- **SC-DLBP-0 (method failed).** K1, K2 or K3 failed. Nothing changes. Fix, then re-run under a new
  digest.
- **SC-DLBP-4 (void method failed).** At void L = 6 or 8, the branches are not clean, the crossing is not
  bracketed after extensions, or the probit fit did not converge. Nothing changes; every number is
  reported.
- **SC-DLBP-3 (not sharpened).** U > 0.0020. The quoted value stays REP1's 1.25875 ± 0.0025.
- **SC-DLBP-2 (sharpened, in tension).** U ≤ 0.0020, but [β_c − 2U, β_c + 2U] misses Gate DL-BETA's
  interval [1.24875, 1.25875] or REP1's [1.25625, 1.26125]. The quoted value becomes β_c ± U, flagged
  "in tension with" the gate it misses. Neither prior interval had a statistical part, so tension
  indicts those gates' grid rules, not the model. The located transition is unaffected.
- **SC-DLBP-1 (sharpened).** U ≤ 0.0020, and β_c ± 2U overlaps both prior intervals. **The quoted value
  becomes β_c ± U** (1/e²_c = β_c/√2 ± U/√2). That is a single-code figure with a statistical error, and it
  is **CONJECTURE as a figure**.

**Also reported, whatever the code:** the distance from β_c to each prior interval, in units of U; the Z4
calibration (Q6); K2 bit-identity; and the time drift.

## 6. No-fit clause

- No lattice, size, grid, chain count, sweep count, seed rule, estimator, threshold or extension rule may
  change after the run starts.
- If the pinned code contradicts this card's text, the card governs. Fix the code in the smallest way,
  record a correction notice CN-DLBP-nn with the old and new hashes, and re-run only what the fix affects.
- Diagnostics (Q5) and the Z4 calibration (Q6) are not verdict inputs.
- Same-session results are capped at CONJECTURE.

## 7. Validation already done (in the card's thread)

- **Dry run** of the driver and the analysis with `DLBP_DRYRUN=1`: void L = 2 and 3, Z4 L = 4 and 6,
  1000-sweep chains, seeds offset by +9,000,000. It exercised K1, K2, both extension rounds, the
  bootstrap, the integrity and fit-failure paths, and the verdict guard. No gate lattice or seed was used.
  Its numbers are meaningless and are not results.
- **Synthetic test of the probit estimator.** 5 points × 6 chains, 200 replicas per case, with true
  crossings 1.2580, 1.2565 and 1.2590 at widths 0.003, 0.0015 and 0.0005. It recovered 1.25796, 1.25659 and
  1.25894, with spreads of 0.00078, 0.00055 and 0.00052 (5 % of fits rejected at the sharpest width).
- **The simulator** passed REP1's K1–K5 and was cross-checked against the original code (REP1 result §2,
  §9.2).

## 8. Analyst's disclosure

The author ran REP1, has seen its raw data and the original's result, and placed the windows and branch
points using both. Forecasts:

- **K1–K3 pass:** 88 %.
- **Verdict:** SC-DLBP-1 55 %; SC-DLBP-3 22 %; SC-DLBP-2 8 %; SC-DLBP-4 8 %; SC-DLBP-0 7 %.
- **β₅₀(void, L = 8) in [1.2565, 1.2600]:** 65 %.
- **|β₅₀(6) − β₅₀(8)| ≤ 0.002:** 65 %.
- **Z4 β_∞ within 2U of 1.0111331:** 60 %.
- **K2 bit-identical to REP1:** 70 % if the run uses the same container image as REP1, otherwise low.

**Interest.** The author has none in the number, and wrote REP1's warning that its own "Resolved" was
fragile. This card exists to replace that fragile figure with one that has an error bar.

## 9. Known limitations

- Those of the earlier cards: Wilson action only; β_t = β_s only; one spatial complex; bare couplings; a
  lattice β_c with a tree-level k.
- Two sizes. 1/V is assumed to be the leading correction; U includes the full shift but no higher-order
  terms.
- A fixed-time estimator. ⟨f⟩ at 3000 sweeps crosses ½ at coexistence only if the interfaces move
  symmetrically there. The mid-length drift is reported, not repaired.
- The branch lines are straight and extrapolated by up to 0.0225 in β (with extensions). Curvature biases f
  systematically, and the bootstrap does not cover it.
- One code (REP1's) in one thread: a figure, not a replication.
- The order of the transition is not addressed.

## 10. Run protocol

- Fresh thread inside the BCT Project. Before opening it, switch off "Search and reference past chats" and
  "Generate memory from chats"; switch them back on afterwards. One gate per thread.
- Fetch this card by commit-pinned raw URL with `curl` to disk. Hash it and compare with
  `audit/gates/PREREG_20261113_DLBETA_P50.sha256` **before reading it**. Record the digest and the commit.
- Get the repository at that commit (a single-commit `git fetch --depth 1`). Verify every §4.1 hash.
- Copy the two pinned files into a work directory. Then run
  `nohup python3 -I dlbp_driver.py <repo>/audit/gates/DLBETA_REP1/run <repo>/audit/gates/DLBETA_REP1/out/series OUT [workers] > OUT/driver_stdout.txt 2>&1 &`.
  Keep the turn alive and poll; do not end a reply with jobs in the background.
- After `DRIVER COMPLETE`, follow §4.7 (numbers → hash → post → verdict).
- Deliverable: `audit/gates/DLBETA_P50/gate_DLBETA_P50_RESULT.md`, containing:
  - the K table, with the K2 bit-identity;
  - for each of the four lattices: the branch table (E, error, span, G, seed), the integrity result, the
    lines, the φ table with every chain's f and seed, β₅₀, w, σ_boot, σ and the extensions;
  - both extrapolations; β_c ± U in both normalisations;
  - Q5 diagnostics and the Q6 calibration;
  - the SHA-256 of `dlbp_numbers.txt`, with the time it was posted;
  - Q7: the distances, the verdict, and the "also reported" items of §5;
  - the §8 forecasts scored item by item;
  - correction notices CN-DLBP-nn;
  - a plain-language summary.

  Also deliver `OUT/` (records, series, state, `analysis.json`, the numbers file and its hash, the verdict
  file, the logs) and a copy of the as-run prompt. The session cannot push: deliver a `git format-patch`
  adding `audit/gates/DLBETA_P50/` only, sent in the conversation as a file.
- Same-session results are capped at CONJECTURE.
