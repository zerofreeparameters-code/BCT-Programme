# Gate DL-BETA P50R — result

**Verdict: SC-DLBPR-5 (void method failed).** At void L = 6 one branch run's 20 block means spread wider than the
card's integrity limit: the hot run at β = 1.2450 has a span of 0.00919 against 0.25·G = 0.00809, a ratio of 1.14.
Card §5 tests that before any comparison with Gate DL-BETA P50, so the gate stops there. **Nothing changes.
P50's β_c = 1.25771 ± 0.00107 stays CONJECTURE** — it is neither moved to REPLICATED nor flagged as not
reproduced. Every number is reported below.

**What the numbers say, for the record.** The second code's own measurement is
**β_c(P50R) = 1.25801 ± 0.00111** (so 1/e²_c = 0.88955 ± 0.00079), against P50's 1.25771 ± 0.00107:

> **D = β_c(P50R) − β_c(P50) = +0.00030**, with **U_D = 0.00155 (|D| = 0.19 U_D)** and
> **σ_D = 0.00042 (|D| = 0.71 σ_D)**. Both are inside their 2× thresholds.

Had the void integrity test passed, the ordered code would have been **SC-DLBPR-1** — agreement at statistical
precision. It did not pass, so that is a counterfactual, not the verdict. The two codes' β₅₀ at void L = 8 differ
by 0.00003 (0.14 σ_boot); at void L = 6 by 0.00076 (1.63 σ_boot).

**Checks.** K1 passes. All four K2 runs are within 2 % of their targets and **all four are bit-identical** to Gate
DL-BETA's stored series, comparing exact bits. K3 passes: Z4 at L = 12 is clean, bracketed and converged, with
β₅₀ = 1.01003 inside [1.0051, 1.0171]. No bracket extension was triggered on any lattice. On Z4 the same estimator
extrapolates to β_∞ = 1.01066 ± 0.00109, which is −0.44 U from the literature value 1.0111331 (Q6, not a verdict
input).

**Run.** 13 November 2026, 05:00–10:10 UTC (16:00–21:10 AEDT). Analyst: Claude; this session was configured as
`claude-fable-5-1`, and the runtime reported serving-model fallbacks to `claude-opus-5-5` and `claude-opus-5`
during the run, so the model serving any given step is not certain (§0). Simulation
05:03:35–09:51:22 UTC: 136 runs, 575.5 core-minutes (9.59 core-hours) on 2 cores. **This run was started as a
scheduled task (a fresh cloud session) at the user's request, rather than in a hand-opened thread inside the BCT
Project** (§0). Same-session results are capped at CONJECTURE.

---

## 0. Provenance and disclosures

**Card.** I fetched `audit/gates/gate_DLBETA_P50R_prompt.md` at commit
`dcf22c72170e55613be779718a19488f726ecc9e` with `curl` from its commit-pinned raw URL, wrote it to disk and hashed
it **before reading it**. Its record, `audit/gates/PREREG_20261113_DLBETA_P50R.sha256`, was hashed the same way.

| file | SHA-256 | expected | |
|---|---|---|---|
| `gate_DLBETA_P50R_prompt.md` | `767be760e0ccbfb0bd73c4da3d6748816ec77dd5f4daf0c671f9c041f9a05f3b` | same | match |
| `PREREG_20261113_DLBETA_P50R.sha256` | `7a640a088e9fd866401d4121a82444dc6e4e49baba0462ca1fc6f640833378a2` | same | match |

The record's content is the card's digest (`767be760…5f3b`).

**Repository.** `zerofreeparameters-code/BCT-Programme` was cloned and checked out at `dcf22c72…`; `origin/main`
was at the same commit, so the card's commit was also the head of main. All eleven §4.1 files were hash-checked
before use and all eleven match (`as_run/pins_check.txt`). The three code files were copied into a work directory
outside the repository and hashed again there; all three match.

**Environment.** Python 3.13.18, NumPy 2.5.3, SciPy 1.18.1, numba 0.68.1 (from `pip install numba==0.68.1`),
llvmlite 0.50.0. 2 cores, 7 GB RAM, 2 workers, one chain per core. These versions are exactly the toolchain Gate
DL-BETA recorded, which is what K2's bit-identity depends on.

**Disclosures.**

- **Scheduled task.** This run was started as a scheduled task (a fresh cloud session) at the user's request,
  rather than in a hand-opened thread inside the BCT Project. Card §10 asks the user to switch off "Search and
  reference past chats" and "Generate memory from chats" before opening such a thread. This session cannot see
  those settings. It called no memory, past-chat or Project tool, and read nothing but the §4.1 paths.
- **Analyst identity.** The session was configured as `claude-fable-5-1`. Partway through the simulation the
  runtime reported that the serving model had fallen back, first to `claude-opus-5-5` and then to `claude-opus-5`.
  Which model served which step is not recoverable from here, so no single model is claimed. This cannot affect a
  number: every number in this file was produced by the pinned code, and all of them are reproduced independently
  in §8.
- **Not blind.** The card states P50's result in §1, and so did this run. Under §4.7, `dlbpr_numbers.txt` was
  written, hashed and its hash posted in the conversation **before** the verdict step opened P50's `analysis.json`.
- **Seeds.** The 132 gate seeds run from 5,073,152 to 6,575,979, all distinct, all in the card's 5,000,000 (Z4)
  and 6,000,000 (void) families, and every one follows the §4.4 formula (verified independently, §8). None can
  coincide with Gate DL-BETA's, REP1's or P50's, which lie in lower families. K2 reuses Gate DL-BETA's four K3
  seeds on purpose.
- **Clean repository (R6).** The driver set `sys.dont_write_bytecode` and pointed numba's cache at the work
  directory. `git status` in the clone was empty before and after the run: running the original code wrote nothing
  into the repository.
- **Scripts written during the run.** `run/dlbpr_report.py` (Markdown tables) was written while the void chains
  ran. `run/dlbpr_crosscheck.py` (§8) and `run/dlbpr_assemble.py` (this file's assembly) were written after the
  verdict. None computes a verdict input; the report and assembler compute nothing at all.
- **Delivery.** The run prompt asked for a push first. This session cannot push: `gh auth status` reports the
  token invalid, and `git push --dry-run` is refused by the git proxy — "zerofreeparameters-code/BCT-Programme is
  not in this session's authorized repository set" — and no `add_repo` tool exists in this session. The proxy's
  README says policy denials are not to be retried or routed around. Delivery is therefore the card's
  `git format-patch` fallback, adding `audit/gates/DLBETA_P50R/` only, on top of `dcf22c72…`.

## 1. Code and checks (Q1)

**Card versus code.** Before running, I read `dlbpr_driver.py` and `dlbpr_rules.py` against the card:

- the two seed families and the round-half-even rule (§4.4);
- the four lattices, their branch points, windows, step and chain counts (§4.4);
- the 500 + 1500 branch runs and the 3000-sweep mixed chains, with row 0 of each series being the start (§4.2);
- E_end from the last 10 of the 50-sweep readings and E_mid from sweeps 1050–1500;
- the import of P50's `dlbp_analysis.py` unmodified, hash-checked at both the driver and the rules module, which
  is what makes every estimator, the bracket rule, the extension rule, the bootstrap seeds and the σ floor P50's;
- σ_∞,stat as √[((1+k)·σ_boot,big)² + (k·σ_boot,small)²], with no floor (§4.5 b);
- the verdict order and thresholds of §5, and the §4.7 refusals (no hash file, wrong P50 hash).

All agree. The driver calls the original simulator only through `run_job(spec)`, as §4.2 R2 requires. No mismatch
between card and code was found, before or after the run: **there is no correction notice** (§9).


| check | run | seed | value | target | dev | pass | bit-identical to Gate DL-BETA's stored series |
|---|---|---|---|---|---|---|---|
| K1 | dlb_sim.py SHA-256 | — | `4a813cf7eea0b883…` | `4a813cf7eea0b883…` | — | PASS | — |
| K1 | dlb_complex.py SHA-256 | — | `4aa142b0f57122b0…` | `4aa142b0f57122b0…` | — | PASS | — |
| K1 | dlbp_analysis.py SHA-256 | — | `3ab1b43e44e3ace8…` | `3ab1b43e44e3ace8…` | — | PASS | — |
| K1 | K3_series.npz SHA-256 (reference) | — | `705bd34a814fbf38…` | `705bd34a814fbf38…` | — | match | — |
| K2 | void_L2_b0.10000_hot (1000 + 10000) | 516838 | 0.049739 | 0.049938 | -0.397 % | PASS | yes |
| K2 | void_L2_b20.00000_cold (1000 + 10000) | 715839 | 0.014358 | 0.014258 | +0.699 % | PASS | yes |
| K2 | z4_L4_b0.10000_hot (1000 + 10000) | 32676 | 0.049938 | 0.049938 | +0.002 % | PASS | yes |
| K2 | z4_L4_b20.00000_cold (1000 + 10000) | 231677 | 0.012526 | 0.012451 | +0.603 % | PASS | yes |
| K3 | Z4 L = 12 control | — | β₅₀ = 1.01003; clean True; bracketed True; fit True | β₅₀ in [1.0051, 1.0171] | — | PASS | — |

K2 run timings:

| run | seed | sweeps | seconds | ms/sweep | E_start | E (meas.) |
|---|---|---|---|---|---|---|
| void_L2_b0.10000_hot | 516838 | 1000 + 10000 | 8.8 | 0.80 | 1.00472 | 0.950261 |
| void_L2_b20.00000_cold | 715839 | 1000 + 10000 | 7.7 | 0.70 | 0.00000 | 0.014358 |
| z4_L4_b0.10000_hot | 32676 | 1000 + 10000 | 4.7 | 0.42 | 0.99069 | 0.950062 |
| z4_L4_b20.00000_cold | 231677 | 1000 + 10000 | 4.1 | 0.37 | 0.00000 | 0.012526 |

K1 passes. Each K2 run is within 2 % of its target. **K2 bit-identity: yes for all four.** Every byte of every
series matches Gate DL-BETA's stored series, on both complexes and both starts — the forecast's 80 % branch. That
is consistent with the matching toolchain recorded above, and it means this session's rebuild of the original code
reproduces it exactly, not merely statistically. K3 passes.

## 2. Branches, φ and crossings, lattice by lattice (Q2, Q3)

Window chains ran 3000 sweeps from the mixed start: 4 chains per point on Z4, 6 on the void. Every chain's E_end,
f, E_mid and seed is in Appendix A. **No bracket extension was triggered on any lattice**: the driver's
`state.json` records `ext = []` for all four, so every grid is the card's fixed window and every seed is a fixed
one.

### z4_8: z4 L = 8 (L_t = 8), V = 4096

**Branch runs** (500 + 1500 sweeps; E = mean over the 1500 measurement sweeps; error from 20 blocks)

| start | β | seed | E | σ_E | block span | G(β) | 0.25·G | ok | ms/sweep |
|---|---|---|---|---|---|---|---|---|---|
| hot | 0.9800 | 5073152 | 0.45016 | 0.00042 | 0.00691 | 0.08356 | 0.02089 | ok | 7.0 |
| hot | 0.9850 | 5073202 | 0.44123 | 0.00106 | 0.01612 | 0.07919 | 0.01980 | ok | 6.7 |
| hot | 0.9900 | 5073252 | 0.43498 | 0.00100 | 0.01745 | 0.07481 | 0.01870 | ok | 7.0 |
| hot | 0.9950 | 5073302 | 0.42316 | 0.00104 | 0.01739 | 0.07044 | 0.01761 | ok | 6.9 |
| cold | 1.0200 | 5073553 | 0.33180 | 0.00049 | 0.00939 | 0.04859 | 0.01215 | ok | 6.6 |
| cold | 1.0250 | 5073603 | 0.32817 | 0.00051 | 0.00901 | 0.04422 | 0.01105 | ok | 6.8 |
| cold | 1.0300 | 5073653 | 0.32333 | 0.00045 | 0.00693 | 0.03984 | 0.00996 | ok | 6.7 |
| cold | 1.0350 | 5073703 | 0.31890 | 0.00031 | 0.00553 | 0.03547 | 0.00887 | ok | 7.0 |

- S(β) = 2.160578 + (-1.745010)·β; residuals [-0.00031, -0.00051, 0.00196, -0.00114]
- W(β) = 1.220274 + (-0.870778)·β; residuals [-0.00028, 0.00044, -5e-05, -0.00012]
- Integrity: **clean** (every span ≤ 0.25·G: True; S strictly decreasing: True; W strictly decreasing: True; G > 0 at every window point: True)

**φ(β)** (3000-sweep mixed starts; f = (S − E_end)/(S − W); every chain's f and seed in Appendix A)

| β | S(β) | W(β) | G(β) | n | φ | σ_φ | weak fraction (f > ½) |
|---|---|---|---|---|---|---|---|
| 1.0000 | 0.41557 | 0.34950 | 0.06607 | 4 | 0.0723 | 0.0128 | 0.000 |
| 1.0025 | 0.41121 | 0.34732 | 0.06389 | 4 | 0.0618 | 0.0221 | 0.000 |
| 1.0050 | 0.40684 | 0.34514 | 0.06170 | 4 | 0.1176 | 0.0547 | 0.000 |
| 1.0075 | 0.40248 | 0.34297 | 0.05952 | 4 | 0.4855 | 0.2128 | 0.500 |
| 1.0100 | 0.39812 | 0.34079 | 0.05733 | 4 | 0.9334 | 0.0084 | 1.000 |

- Grid [1.0000, 1.0100]; extensions: none; bracketed: **yes**
- Probit: **β₅₀ = 1.00747**, w = 0.00193, converged: **True**; σ_boot = 0.00061, **σ = 0.00070**; bootstrap failures 0/1000

### z4_12: z4 L = 12 (L_t = 12), V = 20736

**Branch runs** (500 + 1500 sweeps; E = mean over the 1500 measurement sweeps; error from 20 blocks)

| start | β | seed | E | σ_E | block span | G(β) | 0.25·G | ok | ms/sweep |
|---|---|---|---|---|---|---|---|---|---|
| hot | 0.9800 | 5104828 | 0.44980 | 0.00030 | 0.00445 | 0.08347 | 0.02087 | ok | 38.7 |
| hot | 0.9850 | 5104878 | 0.44242 | 0.00040 | 0.00696 | 0.07973 | 0.01993 | ok | 40.0 |
| hot | 0.9900 | 5104928 | 0.43445 | 0.00038 | 0.00715 | 0.07599 | 0.01900 | ok | 39.0 |
| hot | 0.9950 | 5104978 | 0.42554 | 0.00046 | 0.00771 | 0.07225 | 0.01806 | ok | 41.3 |
| cold | 1.0200 | 5105229 | 0.33227 | 0.00026 | 0.00400 | 0.05355 | 0.01339 | ok | 40.7 |
| cold | 1.0250 | 5105279 | 0.32744 | 0.00022 | 0.00378 | 0.04980 | 0.01245 | ok | 38.8 |
| cold | 1.0300 | 5105329 | 0.32312 | 0.00014 | 0.00208 | 0.04606 | 0.01152 | ok | 36.2 |
| cold | 1.0350 | 5105379 | 0.31927 | 0.00016 | 0.00246 | 0.04232 | 0.01058 | ok | 39.3 |

- S(β) = 2.032666 + (-1.614798)·β; residuals [-0.00036, 0.00033, 0.00044, -0.0004]
- W(β) = 1.216124 + (-0.866762)·β; residuals [0.00024, -0.00025, -0.00024, 0.00024]
- Integrity: **clean** (every span ≤ 0.25·G: True; S strictly decreasing: True; W strictly decreasing: True; G > 0 at every window point: True)

**φ(β)** (3000-sweep mixed starts; f = (S − E_end)/(S − W); every chain's f and seed in Appendix A)

| β | S(β) | W(β) | G(β) | n | φ | σ_φ | weak fraction (f > ½) |
|---|---|---|---|---|---|---|---|
| 1.0050 | 0.40979 | 0.34503 | 0.06477 | 4 | 0.1121 | 0.0154 | 0.000 |
| 1.0075 | 0.40576 | 0.34286 | 0.06290 | 4 | 0.2046 | 0.0374 | 0.000 |
| 1.0100 | 0.40172 | 0.34069 | 0.06103 | 4 | 0.3974 | 0.0748 | 0.250 |
| 1.0125 | 0.39768 | 0.33853 | 0.05916 | 4 | 0.9390 | 0.0101 | 1.000 |
| 1.0150 | 0.39365 | 0.33636 | 0.05729 | 4 | 0.9683 | 0.0081 | 1.000 |

- Grid [1.0050, 1.0150]; extensions: none; bracketed: **yes**
- Probit: **β₅₀ = 1.01003**, w = 0.00244, converged: **True**; σ_boot = 0.00029, **σ = 0.00070**; bootstrap failures 0/1000

### void_6: void L = 6 (L_t = 18), V = 3888

**Branch runs** (500 + 1500 sweeps; E = mean over the 1500 measurement sweeps; error from 20 blocks)

| start | β | seed | E | σ_E | block span | G(β) | 0.25·G | ok | ms/sweep |
|---|---|---|---|---|---|---|---|---|---|
| hot | 1.2300 | 6059814 | 0.35834 | 0.00025 | 0.00406 | 0.04105 | 0.01026 | ok | 70.6 |
| hot | 1.2350 | 6059864 | 0.35267 | 0.00035 | 0.00599 | 0.03815 | 0.00954 | ok | 72.9 |
| hot | 1.2400 | 6059914 | 0.34743 | 0.00028 | 0.00475 | 0.03526 | 0.00881 | ok | 74.1 |
| hot | 1.2450 | 6059964 | 0.34018 | 0.00052 | 0.00919 | 0.03236 | 0.00809 | FAIL | 76.9 |
| cold | 1.2650 | 6060165 | 0.29622 | 0.00019 | 0.00300 | 0.02078 | 0.00519 | ok | 76.2 |
| cold | 1.2700 | 6060215 | 0.29275 | 0.00013 | 0.00249 | 0.01788 | 0.00447 | ok | 74.1 |
| cold | 1.2750 | 6060265 | 0.28977 | 0.00016 | 0.00238 | 0.01499 | 0.00375 | ok | 73.1 |
| cold | 1.2800 | 6060315 | 0.28696 | 0.00012 | 0.00206 | 0.01209 | 0.00302 | ok | 70.5 |

- S(β) = 1.827373 + (-1.194116)·β; residuals [-0.00027, 3e-05, 0.00076, -0.00052]
- W(β) = 1.074025 + (-0.615011)·β; residuals [0.00018, -0.00021, -0.00012, 0.00015]
- Integrity: **FAIL** (every span ≤ 0.25·G: False; S strictly decreasing: True; W strictly decreasing: True; G > 0 at every window point: True)

**φ(β)** (3000-sweep mixed starts; f = (S − E_end)/(S − W); every chain's f and seed in Appendix A)

| β | S(β) | W(β) | G(β) | n | φ | σ_φ | weak fraction (f > ½) |
|---|---|---|---|---|---|---|---|
| 1.2525 | 0.33174 | 0.30372 | 0.02802 | 6 | 0.1344 | 0.0181 | 0.000 |
| 1.2550 | 0.32876 | 0.30219 | 0.02657 | 6 | 0.1963 | 0.0219 | 0.000 |
| 1.2575 | 0.32577 | 0.30065 | 0.02512 | 6 | 0.5315 | 0.0896 | 0.500 |
| 1.2600 | 0.32279 | 0.29911 | 0.02367 | 6 | 0.9096 | 0.0366 | 1.000 |
| 1.2625 | 0.31980 | 0.29757 | 0.02223 | 6 | 0.9582 | 0.0098 | 1.000 |

- Grid [1.2525, 1.2625]; extensions: none; bracketed: **yes**
- Probit: **β₅₀ = 1.25708**, w = 0.00272, converged: **True**; σ_boot = 0.00034, **σ = 0.00070**; bootstrap failures 0/1000

### void_8: void L = 8 (L_t = 24), V = 12288

**Branch runs** (500 + 1500 sweeps; E = mean over the 1500 measurement sweeps; error from 20 blocks)

| start | β | seed | E | σ_E | block span | G(β) | 0.25·G | ok | ms/sweep |
|---|---|---|---|---|---|---|---|---|---|
| hot | 1.2300 | 6075652 | 0.35789 | 0.00016 | 0.00326 | 0.03976 | 0.00994 | ok | 223.9 |
| hot | 1.2350 | 6075702 | 0.35263 | 0.00014 | 0.00219 | 0.03685 | 0.00921 | ok | 233.3 |
| hot | 1.2400 | 6075752 | 0.34664 | 0.00016 | 0.00249 | 0.03394 | 0.00849 | ok | 230.2 |
| hot | 1.2450 | 6075802 | 0.33968 | 0.00022 | 0.00410 | 0.03103 | 0.00776 | ok | 231.5 |
| cold | 1.2650 | 6076003 | 0.29661 | 0.00011 | 0.00194 | 0.01939 | 0.00485 | ok | 220.3 |
| cold | 1.2700 | 6076053 | 0.29323 | 0.00007 | 0.00130 | 0.01648 | 0.00412 | ok | 226.7 |
| cold | 1.2750 | 6076103 | 0.28992 | 0.00008 | 0.00148 | 0.01357 | 0.00339 | ok | 218.6 |
| cold | 1.2800 | 6076153 | 0.28720 | 0.00006 | 0.00117 | 0.01066 | 0.00266 | ok | 220.7 |

- S(β) = 1.850092 + (-1.212834)·β; residuals [-0.00041, 0.00039, 0.00046, -0.00044]
- W(β) = 1.094396 + (-0.630773)·β; residuals [0.00014, -9e-05, -0.00024, 0.00019]
- Integrity: **clean** (every span ≤ 0.25·G: True; S strictly decreasing: True; W strictly decreasing: True; G > 0 at every window point: True)

**φ(β)** (3000-sweep mixed starts; f = (S − E_end)/(S − W); every chain's f and seed in Appendix A)

| β | S(β) | W(β) | G(β) | n | φ | σ_φ | weak fraction (f > ½) |
|---|---|---|---|---|---|---|---|
| 1.2525 | 0.33102 | 0.30435 | 0.02667 | 6 | 0.0876 | 0.0175 | 0.000 |
| 1.2550 | 0.32799 | 0.30278 | 0.02521 | 6 | 0.1794 | 0.0130 | 0.000 |
| 1.2575 | 0.32495 | 0.30120 | 0.02376 | 6 | 0.3848 | 0.0394 | 0.167 |
| 1.2600 | 0.32192 | 0.29962 | 0.02230 | 6 | 0.9083 | 0.0172 | 1.000 |
| 1.2625 | 0.31889 | 0.29804 | 0.02084 | 6 | 0.9531 | 0.0115 | 1.000 |

- Grid [1.2525, 1.2625]; extensions: none; bracketed: **yes**
- Probit: **β₅₀ = 1.25772**, w = 0.00237, converged: **True**; σ_boot = 0.00017, **σ = 0.00070**; bootstrap failures 0/1000

**Integrity margins.** The largest block span as a fraction of its limit 0.25·G:

| lattice | largest span / (0.25·G) | at |
|---|---|---|
| z4 L = 8 | 0.99 | hot, β = 0.9950 |
| z4 L = 12 | 0.43 | hot, β = 0.9950 |
| void L = 6 | 1.14 | hot, β = 1.2450 |
| void L = 8 | 0.53 | hot, β = 1.2450 |

### The integrity failure at void L = 6 (the verdict)

The one failing run is **void L = 6, hot, β = 1.2450, seed 6059964**: E = 0.34018 ± 0.00052, block span 0.00919
against the limit 0.25·G = 0.00809 (ratio 1.14). Its 20 block means, each over 75 measurement sweeps, are

```
0.33502 0.33641 0.33996 0.34222 0.34054   0.33959 0.34039 0.33936 0.34142 0.34157
0.33810 0.33933 0.33675 0.34186 0.34421   0.34301 0.33916 0.34102 0.34229 0.34139
```

The minimum is the **first** block (0.33502) and the maximum is block 14 (0.34421). E at the end of the 500
thermalisation sweeps is 0.33620, and the first 100 measurement sweeps average 0.3350 against ≈0.3400 for the
rest: the chain was still relaxing upward from the hot start when measurement began. Excluding block 0 alone, the
span would be 0.00780, inside the limit. The run's mean is not anomalous — it sits +0.11 σ from P50's value at the
same point (0.34011 ± 0.00038) — so this is a within-run spread, not a disagreement about E.

Three observations, none of them a change to anything (§6's no-fit clause forbids that):

- β = 1.2450 is the hot branch point **closest to the transition**, where relaxation is slowest, and it is also
  where the limit is tightest, because G(β) is smallest there. It is the design's most fragile point by
  construction. P50's run at the same point had ratio 0.78 with the nearly identical limit 0.00820.
- The margin is thin on both codes and both gates: this run's z4 L = 8 worst ratio is 0.99 (hot, β = 0.9950), and
  P50's worst was 0.90 (hot, β = 0.990). A 500-sweep thermalisation against a 0.25·G spread limit is close to the
  edge wherever the branch nears the transition.
- The failure is **confined to one branch run on one lattice**. Every other branch run on all four lattices is
  clean, both branches are strictly decreasing everywhere, G > 0 at every window point, all four windows bracket
  the crossing without extension, and all four probit fits converge with zero bootstrap failures.

## 3. Result (Q4)


| extrapolation | k | β₅₀(small) ± σ | β₅₀(big) ± σ | shift | σ_∞ | σ_∞,stat (no floor) | U | β_∞ |
|---|---|---|---|---|---|---|---|---|
| **void, L = 6 → 8** | 0.46286 | 1.25708 ± 0.00070 | 1.25772 ± 0.00070 | +0.00029 | 0.00107 | 0.00029 | **0.00111** | **1.25801** |
| Z4, L = 8 → 12 | 0.24615 | 1.00747 ± 0.00070 | 1.01003 ± 0.00070 | +0.00063 | 0.00089 | 0.00039 | **0.00109** | **1.01066** |

> **β_c(P50R) = 1.25801 ± 0.00111** (card convention); **1/e²_c = 0.88955 ± 0.00079**
> Statistical part alone (σ_∞,stat): 0.00029 in β, 0.00020 in 1/e².

**What U is made of.** Every σ_boot is below the 0.0007 floor (0.00034 at void L = 6, 0.00017 at void L = 8), so
both void σ are the floor, and σ_∞ is the floor's 1.53 × 0.0007 = 0.00107. The extrapolation shift is +0.00029
(β₅₀(6) − β₅₀(8) = −0.00063 unrounded), which raises U to 0.00111. The statistical part alone would give 0.00029. This is
P50R's own figure, a same-session single-code measurement, **CONJECTURE**, and under a verdict of SC-DLBPR-5 it
changes nothing in the ledger.

## 4. Diagnostics (Q5) and calibration (Q6) — reported, not verdict inputs


| lattice | β₅₀ (probit) | φ interpolation crossing | weak-fraction crossing | β₅₀ from E_mid | drift β₅₀ − β₅₀(mid) | w | bootstrap failures |
|---|---|---|---|---|---|---|---|
| z4 L = 8 | 1.00747 | 1.00758 | 1.00750 | 1.00748 | -0.00001 | 0.00193 | 0 / 1000 |
| z4 L = 12 | 1.01003 | 1.01047 | 1.01083 | 1.01036 | -0.00033 | 0.00244 | 0 / 1000 |
| void L = 6 | 1.25708 | 1.25727 | 1.25750 | 1.25835 | -0.00127 | 0.00272 | 0 / 1000 |
| void L = 8 | 1.25772 | 1.25805 | 1.25850 | 1.25825 | -0.00053 | 0.00237 | 0 / 1000 |

- **Monotone.** φ has exactly one interpolation crossing on every lattice; none is flagged non-monotone.
- **Estimator spread on the void.** As in P50, the interpolation crossing sits above the probit β₅₀ (+0.00019 at
  L = 6, +0.00033 at L = 8) and the weak-fraction crossing higher still (+0.00042, +0.00078). Both are inside U.
- **φ's strong-side floor.** φ at the lowest window point is 0.134 (L = 6) and 0.088 (L = 8), against P50's 0.158
  and 0.109; at the top it reaches 0.958 and 0.953, against P50's 0.978 and 0.970. The same asymmetry P50 reported
  — φ does not reach 0 on the strong side but nearly reaches 1 on the weak side — appears on the second code, at
  slightly smaller magnitude. It is a property of the method, not of either implementation.
- **Time drift.** Between sweeps 1050–1500 and 2550–3000 the void crossings move down by 0.00127 (L = 6) and
  0.00053 (L = 8); P50's moved by 0.00020 and 0.00024. The L = 6 drift is larger than P50's and is about 1.1 U.
  It points the same way as the integrity failure above: at L = 6 this code's chains were still settling.
- **Cross-code branch energies** (§4.5 b R5; the 32 branch points are identical in the two gates, so they compare
  point by point):

| lattice | z (hot then cold) | rms \|z\| | max \|z\| |
|---|---|---|---|
| z4 L = 8 | 1.64, −0.97, −0.41, −2.03, 1.37, 2.01, 1.17, −0.93 | 1.42 | 2.03 |
| z4 L = 12 | −0.11, −0.59, −0.68, −0.24, 0.36, −0.15, 0.38, 0.33 | 0.40 | 0.68 |
| void L = 6 | 1.13, 1.41, −0.30, 0.11, 0.52, −0.50, −0.33, −0.89 | 0.77 | 1.41 |
| void L = 8 | 0.99, 0.83, 0.44, −1.34, 1.96, 2.55, 0.76, −0.70 | 1.37 | 2.55 |

  On both void lattices the rms is ≤ 1.5, the forecast's bound. The two codes agree on the energies themselves;
  the largest single deviation, 2.55 at void L = 8 cold β = 1.2700, is one point out of 32 and both runs are
  short-error runs where σ_E ≈ 10⁻⁴.

- **Cross-code β₅₀ and φ.**

| lattice | β₅₀(P50R) | β₅₀(P50) | difference | in σ (floor) | in σ_boot |
|---|---|---|---|---|---|
| z4 L = 8 | 1.00747 | 1.00640 | +0.00107 | +1.08 | +1.26 |
| z4 L = 12 | 1.01003 | 1.01045 | −0.00042 | −0.42 | −1.18 |
| void L = 6 | 1.25708 | 1.25784 | −0.00076 | −0.76 | −1.63 |
| **void L = 8** | **1.25772** | **1.25775** | **−0.00003** | **−0.03** | **−0.14** |

  φ(P50R) − φ(P50) at the common window points is small everywhere except at the steep middle of each window,
  where a difference in φ of 0.17 (void L = 6 at 1.2575) or 0.18 (z4 L = 8 at 1.0050) corresponds to a shift in β
  of well under one step: full lists are in `OUT/verdict.txt`.

- **Z4 calibration (Q6).** β_∞(Z4) = 1.01066 ± 0.00109, against 1.0111331 (hep-lat/0210010): **−0.00048 = −0.44 U**.
  P50 gave +0.00031 = +0.23 U on the same grid. The two codes bracket the literature value: they differ from each
  other by 0.00079 in β, which is 0.46 of their combined error (0.00172), and each error is dominated by the
  common floor and the extrapolation shift. Both are calibration observations, not verdict inputs.

## 5. Hash before comparison (§4.7)

| file | SHA-256 | hashed (UTC) | posted (UTC) |
|---|---|---|---|
| `dlbpr_numbers.txt` | `0b624155e579c82581f65a54ec4b5943d0bc598add1300a07cc0a6b26ca64c63` | 2026-11-13T09:54:06Z | 09:54 (SendUserMessage), before the verdict step at 2026-11-13T09:54:15Z |

The numbers step opened nothing of P50's and compared nothing; the verdict step is the only step that read
`DLBETA_P50/OUT/analysis.json`, and it verified that file's pinned hash before using it. There was one numbers
pass and one verdict run; no file was superseded.

## 6. Comparison and verdict (Q7)

`OUT/verdict.txt`:

```
K1 True; K2 True; K3 (Z4 L=12 beta_50 = 1.01003 in [1.0051, 1.0171], clean, bracketed, fit) True
void L=6, L=8 clean, bracketed, fit: False
beta_c(P50R) = 1.25801 +- 0.00111 (stat 0.00029); U <= 0.002: True
beta_c(P50)  = 1.25771 +- 0.00107 (stat 0.00031)
D = beta_c(P50R) - beta_c(P50) = +0.00030; U_D = 0.00155 (|D| = 0.19 U_D); sigma_D(stat) = 0.00042 (|D| = 0.71 sigma_D)
|D| <= 2 U_D: True; |D| <= 2 sigma_D(stat): True
diag z4_8: beta_50 1.00747 vs P50 1.00640; diff +0.00107 = +1.08 sigma (with floor) = +1.26 sigma_boot
diag z4_8: branch E cross-code z (hot then cold) = [1.64, -0.97, -0.41, -2.03, 1.37, 2.01, 1.17, -0.93]; rms 1.42; max |z| 2.03
diag z4_8: phi(P50R) - phi(P50) at common window points = [(1.0, 0.013), (1.0025, -0.046), (1.005, -0.181), (1.0075, -0.165), (1.01, 0.04)]
diag z4_12: beta_50 1.01003 vs P50 1.01045; diff -0.00042 = -0.42 sigma (with floor) = -1.18 sigma_boot
diag z4_12: branch E cross-code z (hot then cold) = [-0.11, -0.59, -0.68, -0.24, 0.36, -0.15, 0.38, 0.33]; rms 0.40; max |z| 0.68
diag z4_12: phi(P50R) - phi(P50) at common window points = [(1.005, -0.02), (1.0075, 0.005), (1.01, 0.086), (1.0125, 0.043), (1.015, -0.004)]
diag void_6: beta_50 1.25708 vs P50 1.25784; diff -0.00076 = -0.76 sigma (with floor) = -1.63 sigma_boot
diag void_6: branch E cross-code z (hot then cold) = [1.13, 1.41, -0.3, 0.11, 0.52, -0.5, -0.33, -0.89]; rms 0.77; max |z| 1.41
diag void_6: phi(P50R) - phi(P50) at common window points = [(1.2525, -0.024), (1.255, -0.005), (1.2575, 0.174), (1.26, 0.096), (1.2625, -0.02)]
diag void_8: beta_50 1.25772 vs P50 1.25775; diff -0.00003 = -0.03 sigma (with floor) = -0.14 sigma_boot
diag void_8: branch E cross-code z (hot then cold) = [0.99, 0.83, 0.44, -1.34, 1.96, 2.55, 0.76, -0.7]; rms 1.37; max |z| 2.55
diag void_8: phi(P50R) - phi(P50) at common window points = [(1.2525, -0.021), (1.255, -0.033), (1.2575, 0.006), (1.26, 0.075), (1.2625, -0.017)]
diag Z4: beta_inf(P50R) = 1.01066 +- 0.00109; P50 1.01144 +- 0.00134; literature 1.0111331
VERDICT SC-DLBPR-5
```

Card §5's codes are tested in order, and the first that matches is the verdict:

- **SC-DLBPR-0** (method failed): K1, K2 and K3 all pass, so it does not apply.
- **SC-DLBPR-5** (void method failed): at void L = 6 the branches are **not clean** — the hot run at β = 1.2450
  has a block span of 0.00919 against its limit of 0.00809. **This matches, and it is the verdict.**
- The later codes are not reached. For the record, with |D| = 0.00030, U = 0.00111 and the two thresholds
  2 U_D = 0.00309 and 2 σ_D = 0.00084, the ordered code **had the void integrity passed** would have been
  SC-DLBPR-1 (|D| ≤ 2 σ_D). That is stated as a counterfactual and carries no weight.

**Effect.** Nothing changes. P50's β_c = 1.25771 ± 0.00107 (1/e²_c = 0.88933 ± 0.00076) **remains the quoted
value and remains CONJECTURE**: this gate neither raises it to REPLICATED nor flags it as not reproduced.
P50R's own β_c = 1.25801 ± 0.00111 is recorded beside it as a same-session figure, also CONJECTURE, and no
average is formed. The located transition [1.250, 1.255] is unaffected, and remains REPLICATED on its own
footing.

**What a re-run would need.** Card §5 says of SC-DLBPR-0 that one fixes the cause and re-runs under a new digest;
SC-DLBPR-5 says only that nothing changes and every number is reported. The cause here is not a code defect — the
code is Gate DL-BETA's own, bit-reproducing its stored series — but a thermalisation budget that is thin at the
branch point nearest the transition. Any successor card would be choosing a new sweep budget or a new integrity
rule, which is a design decision for a new pre-registration, not for this run.

**Also reported (§5):**

- D = +0.00030 = 0.19 U_D = 0.71 σ_D;
- the cross-code diagnostics of §4 above;
- Z4 calibration: −0.44 U (P50R) against +0.23 U (P50);
- K2 bit-identity: **yes, all four**;
- time drift: −0.00127 at void L = 6, −0.00053 at void L = 8.

## 7. Analyst's forecasts (card §8), scored

The card's forecasts were written by P50's analyst, who had seen P50's raw data but not this run's.

| forecast | outcome | score |
|---|---|---|
| K1–K3 pass: 90 % | all three pass | **hit** (Brier 0.010) |
| K2 bit-identical, all four: 80 % | all four bit-identical | **hit** (Brier 0.040) |
| Verdict: SC-DLBPR-1 55 %; -2 25 %; -0 7 %; **-5 5 %**; -3 5 %; -4 3 % | **SC-DLBPR-5** | **miss** — the outcome fell in a 5 % bin (multi-class Brier 1.276) |
| \|D\| ≤ 0.0005: 55 % | 0.00030 | **hit** (Brier 0.203) |
| \|β₅₀(void, L = 8; P50R) − 1.25775\| ≤ 0.001: 70 % | 0.00003 | **hit** (Brier 0.090) |
| Branch cross-code rms z ≤ 1.5 on both void lattices: 70 % | 0.77 and 1.37 | **hit** (Brier 0.090) |

Five of six hit. The one miss is the one that mattered: the forecast put 88 % on the run reaching a comparison at
all (codes -1, -2, -3, -4), 5 % on the void method failing and 7 % on a check failing. The physics forecasts were
well calibrated — |D| and β₅₀(L = 8) both came in far inside their bounds, and the cross-code rms z held — while
the forecast that the *procedure* would complete was overconfident. A single branch run out of 32, at the one
point where the margin was always thin, decided the gate.

## 8. Verification (after the verdict; not a verdict input)

`run/dlbpr_crosscheck.py` recomputes §4.5 from the raw `.npz` series rather than from the records' summary fields,
with different routines (`numpy.polyfit`, `scipy.optimize.curve_fit` with bounds) and re-derives every seed from
the §4.4 formula:

```
# Gate DL-BETA P50R cross-check (136 records)

## 1. Series hashes and seeds
  OK   all 136 series files match their recorded SHA-256 (0 mismatches)
  OK   every gate seed follows the section 4.4 formula (0 mismatches)
  OK   K2 reuses Gate DL-BETA's four K3 seeds: [32676, 231677, 516838, 715839]
  OK   all 132 gate seeds distinct; range 5073152–6575979
  OK   every gate seed is in the card's 5,000,000 / 6,000,000 families

## 2. Observables recomputed from the raw series
  OK   branch E reproduced from the series (max |diff| 0.00e+00)
  OK   20-block sigma_E reproduced (max |diff| 0.00e+00)
  OK   E_end (sweeps 2550-3000) reproduced (max |diff| 0.00e+00)
  OK   E_mid (sweeps 1050-1500) reproduced (max |diff| 0.00e+00)
  OK   row 0 of the series is (E at the start, NaN, NaN) as card section 4.2 states

## 3. Branch lines, phi and the probit, with different routines
  OK   z4_8: S and W lines match polyfit (max |diff| 4.97e-14)
  z4_8: worst span/(0.25 G) = 0.987 at hot beta 0.9950 (span 0.01739, limit 0.01761) -> integrity ok
  OK   z4_8: integrity verdict reproduced (ok)
  OK   z4_8: beta_50 1.007466 vs 1.007466, w 0.001929 vs 0.001929
  z4_8: independent 300-replica bootstrap sigma_boot = 0.00066 (pinned 1000-replica: 0.00061)
  OK   z4_12: S and W lines match polyfit (max |diff| 4.86e-14)
  z4_12: worst span/(0.25 G) = 0.427 at hot beta 0.9950 (span 0.00771, limit 0.01806) -> integrity ok
  OK   z4_12: integrity verdict reproduced (ok)
  OK   z4_12: beta_50 1.010027 vs 1.010027, w 0.002442 vs 0.002442
  z4_12: independent 300-replica bootstrap sigma_boot = 0.00026 (pinned 1000-replica: 0.00029)
  OK   void_6: S and W lines match polyfit (max |diff| 3.26e-14)
  void_6: worst span/(0.25 G) = 1.136 at hot beta 1.2450 (span 0.00919, limit 0.00809) -> integrity FAIL
  OK   void_6: integrity verdict reproduced (FAIL)
  OK   void_6: beta_50 1.257085 vs 1.257085, w 0.002719 vs 0.002719
  void_6: independent 300-replica bootstrap sigma_boot = 0.00034 (pinned 1000-replica: 0.00034)
  OK   void_8: S and W lines match polyfit (max |diff| 4.88e-14)
  void_8: worst span/(0.25 G) = 0.529 at hot beta 1.2450 (span 0.00410, limit 0.00776) -> integrity ok
  OK   void_8: integrity verdict reproduced (ok)
  OK   void_8: beta_50 1.257716 vs 1.257716, w 0.002367 vs 0.002367
  void_8: independent 300-replica bootstrap sigma_boot = 0.00018 (pinned 1000-replica: 0.00017)

## 4. Extrapolations
  OK   void: k 0.46286, beta_inf 1.258008, U 0.001113, sigma_inf_stat 0.000288 all reproduced
  OK   void: 1/e^2 = beta_inf/sqrt(2) = 0.889546 reproduced
  OK   z4: k 0.24615, beta_inf 1.010658, U 0.001090, sigma_inf_stat 0.000394 all reproduced

## 5. Verdict inputs recomputed (card section 5 order)
  D = +0.000300; U_D = 0.001547 (0.19 U_D); sigma_D = 0.000420 (0.71 sigma_D)
  OK   D, U_D and sigma_D match verdict.txt
  OK   verdict code reproduced: SC-DLBPR-5
  (had the void integrity passed, the ordered code would have been SC-DLBPR-1)

CROSS-CHECK PASS
```

**CROSS-CHECK PASS.** All 136 series hashes match their records; every gate seed follows §4.4 and all 132 are
distinct; every branch E, σ_E, E_end and E_mid is reproduced exactly from the series; the lines, every β₅₀ and w
match to 10⁻⁶; an independent 300-replica bootstrap with a different RNG gives σ_boot 0.00066, 0.00026, 0.00034
and 0.00018 (pinned: 0.00061, 0.00029, 0.00034, 0.00017); both extrapolations and all three verdict inputs are
reproduced; and the integrity verdict at every one of the 32 branch points — including the single FAIL — is
reproduced independently.

## 9. Correction notices

**None.** No mismatch between the card and the pinned code was found, before or after the run. No lattice, size,
grid, chain count, sweep count, seed rule, estimator, threshold or extension rule was changed. The numbers file
was written, hashed and posted once, and the verdict was run once.

## 10. Limits

- **The gate did not reach its question.** SC-DLBPR-5 means the second code's void measurement did not satisfy the
  card's own quality test, so this run is not evidence either way about whether the two codes agree. The agreement
  figures in §3 and §6 are reported, not established.
- **It replicates the code, not the method** (card §9). The estimator, grids, branch points, windows, chain counts
  and floor are P50's, so the method's systematics are shared and untested: the fixed-time estimator, straight
  branch lines, φ's strong-side floor, two sizes, and a U set by its floor. The present failure is in fact a
  symptom of one of those shared choices — the thermalisation budget — showing up on a different code.
- **Partly independent codes** (card §9). The two simulators were written in different threads, but share the
  card's model specification, numba's RNG and the Best–Fisher method.
- **K2 bit-identity tests the toolchain, not the physics** — though here it does establish that this session
  reproduced Gate DL-BETA's original code byte for byte.
- **The earlier cards' limits apply:** Wilson action only, β_t = β_s only, one spatial complex, bare couplings,
  a tree-level k, two sizes, and the order of the transition is not addressed.
- **Same-session cap.** Everything measured here is CONJECTURE.

## 11. Plain-language summary

The question was whether a number measured last night survives being measured again by a different program. The
number is the "tipping point" of electromagnetism simulated on the network of gaps between packed spheres, with
time added: below it the field is trapped, above it light travels freely. An earlier gate measured it as
1.25771 ± 0.00107 using one simulator. This gate re-ran exactly the same measurement — same box sizes, same
settings, same scoring, same arithmetic, only new random seeds — on the *other* simulator the programme had
written months earlier in a different session.

The second program agreed, and closely. It gives 1.25801 ± 0.00111, a difference of 0.0003, which is about a fifth
of the combined error bar and well inside even the much tighter purely statistical comparison. On the larger of the
two boxes the two programs' crossings differ by 0.00003 — three parts in a hundred thousand. As a side check, both
programs were pointed at an ordinary cubic lattice where the right answer is known from the literature; one lands
just above it and the other just below, each well within its error.

But the gate still fails, and it fails on a technicality that was written into the card in advance for good
reason. Before the comparison is allowed, each reference simulation must be *steady*: its output, chopped into
twenty consecutive chunks, must not wander by more than a quarter of the gap between the two phases. On the smaller
box, one of the eight reference runs wandered by 14 % more than that limit. Looking at it afterwards, the reason is
plain: the chunk that is furthest off is the very first one, and the simulation was still visibly settling down
from its starting state when measurement began. It needed a longer warm-up. That run sits at the setting closest to
the tipping point, where settling is slowest and where the allowed wander is smallest — the hardest spot in the
whole design, and the margin was thin for both programs everywhere near it.

The card's rules are applied in a fixed order, and "a reference run was not steady" is tested before "do the two
answers agree". So the verdict is that the method failed on this run, and the earlier number keeps exactly the
status it had: a conjecture resting on one program. It has not been contradicted — if anything the opposite — but
it has not been confirmed either, because the confirmation was not permitted to count. Fixing this would mean a new
card with a longer warm-up, which is a decision for the next pre-registration, not something this run may change.

One genuinely good piece of news came out of the checks. The four calibration runs that re-ran the original
program's own test cases came back *byte for byte identical* to the series stored months ago. The program was
rebuilt in a fresh machine from the repository and reproduced its old output exactly, not just statistically.

## 12. Files

Everything below `audit/gates/DLBETA_P50R/` is listed with SHA-256 in `MANIFEST.sha256`.

| path | what |
|---|---|
| `gate_DLBETA_P50R_RESULT.md` | this file |
| `as_run/gate_DLBETA_P50R_prompt.md`, `as_run/PREREG_20261113_DLBETA_P50R.sha256` | the card and its record, as fetched |
| `as_run/run_prompt.txt` | the run prompt (scheduled task) |
| `as_run/P50R_RUN_LOG.md` | timestamped log |
| `as_run/pins.sha256`, `as_run/pins_check.txt` | the §4.1 pins and their check |
| `run/dlbpr_driver.py`, `run/dlbpr_rules.py`, `run/dlbp_analysis.py` | the pinned code as run (hashes as §4.1) |
| `run/dlbpr_report.py`, `run/dlbpr_crosscheck.py`, `run/dlbpr_assemble.py` | report tables; independent cross-check; this file's assembly |
| `OUT/records/*.json`, `OUT/series/*.npz` | 136 run records (seeds, E, block means, readings every 50 sweeps, series hashes) and full series (E, E_s, E_t after every sweep, row 0 = start) |
| `OUT/state.json`, `OUT/analysis.json` | driver state (K1, K2, extensions); all estimators |
| `OUT/dlbpr_numbers.txt`, `OUT/dlbpr_numbers.sha256`, `OUT/dlbpr_numbers_hashed_at.txt` | numbers, their hash and the time |
| `OUT/verdict.txt`, `OUT/verdict_run_at.txt`, `OUT/verdict_stdout.txt` | verdict |
| `OUT/driver_log.txt`, `OUT/driver_stdout.txt`, `OUT/numbers_stdout.txt` | logs |
| `OUT/environment.txt` | host, cores, toolchain versions, commit |
| `OUT/tables.md`, `OUT/crosscheck_output.txt` | tables used here; cross-check output |

## 13. Timing


| lattice | runs | sweeps | core-seconds | mean ms/sweep |
|---|---|---|---|---|
| K2 | 4 | 44000 | 25 | 0.6 |
| z4_8 | 28 | 76000 | 533 | 7.0 |
| z4_12 | 28 | 76000 | 2931 | 38.6 |
| void_6 | 38 | 106000 | 7572 | 71.4 |
| void_8 | 38 | 106000 | 23471 | 221.4 |
| **total** | 136 | | **34531** (575.5 core-minutes) | |

The budget (card §4.6) was 615 core-minutes; the run took 575.5. Void L = 8 ran at 221 ms/sweep against the
card's 236, void L = 6 at 71 against 75, Z4 L = 12 at 39 against 42, Z4 L = 8 at 7.0 against 7.6. No sweep budget
was shortened.

## Appendix A — every mixed chain


f = (S(β) − E_end)/(S(β) − W(β)), with S and W the lattice's lines. f_mid uses E_mid. Seeds follow §4.4.

**z4_8**

| β | chain | seed | E_end | f | E_mid | f_mid | ms/sweep |
|---|---|---|---|---|---|---|---|
| 1.0000 | 0 | 5073354 | 0.41148 | 0.0619 | 0.41776 | -0.0332 | 7.4 |
| 1.0000 | 1 | 5173354 | 0.41232 | 0.0492 | 0.41247 | 0.0469 | 7.7 |
| 1.0000 | 2 | 5273354 | 0.40841 | 0.1084 | 0.41640 | -0.0126 | 6.9 |
| 1.0000 | 3 | 5373354 | 0.41098 | 0.0695 | 0.41876 | -0.0484 | 7.0 |
| 1.0025 | 0 | 5073379 | 0.41071 | 0.0078 | 0.40610 | 0.0799 | 7.1 |
| 1.0025 | 1 | 5173379 | 0.40684 | 0.0683 | 0.40878 | 0.0379 | 7.1 |
| 1.0025 | 2 | 5273379 | 0.40764 | 0.0558 | 0.40669 | 0.0707 | 6.9 |
| 1.0025 | 3 | 5373379 | 0.40384 | 0.1153 | 0.41023 | 0.0152 | 7.1 |
| 1.0050 | 0 | 5073404 | 0.39965 | 0.1166 | 0.40586 | 0.0159 | 6.9 |
| 1.0050 | 1 | 5173404 | 0.40603 | 0.0133 | 0.40113 | 0.0926 | 7.2 |
| 1.0050 | 2 | 5273404 | 0.39025 | 0.2690 | 0.40896 | -0.0343 | 7.1 |
| 1.0050 | 3 | 5373404 | 0.40244 | 0.0714 | 0.40156 | 0.0856 | 7.2 |
| 1.0075 | 0 | 5073429 | 0.39422 | 0.1388 | 0.38657 | 0.2673 | 7.1 |
| 1.0075 | 1 | 5173429 | 0.35611 | 0.7791 | 0.39960 | 0.0485 | 7.0 |
| 1.0075 | 2 | 5273429 | 0.34762 | 0.9218 | 0.35039 | 0.8753 | 6.9 |
| 1.0075 | 3 | 5373429 | 0.39640 | 0.1022 | 0.35339 | 0.8248 | 6.9 |
| 1.0100 | 0 | 5073454 | 0.34385 | 0.9466 | 0.34167 | 0.9846 | 7.0 |
| 1.0100 | 1 | 5173454 | 0.34403 | 0.9434 | 0.34083 | 0.9993 | 6.9 |
| 1.0100 | 2 | 5273454 | 0.34455 | 0.9343 | 0.34293 | 0.9627 | 6.9 |
| 1.0100 | 3 | 5373454 | 0.34598 | 0.9094 | 0.34176 | 0.9831 | 6.8 |

**z4_12**

| β | chain | seed | E_end | f | E_mid | f_mid | ms/sweep |
|---|---|---|---|---|---|---|---|
| 1.0050 | 0 | 5105080 | 0.40021 | 0.1479 | 0.40198 | 0.1207 | 38.1 |
| 1.0050 | 1 | 5205080 | 0.40292 | 0.1062 | 0.40538 | 0.0681 | 37.7 |
| 1.0050 | 2 | 5305080 | 0.40500 | 0.0741 | 0.40060 | 0.1420 | 37.9 |
| 1.0050 | 3 | 5405080 | 0.40201 | 0.1202 | 0.40059 | 0.1422 | 38.5 |
| 1.0075 | 0 | 5105105 | 0.39188 | 0.2206 | 0.39191 | 0.2201 | 37.4 |
| 1.0075 | 1 | 5205105 | 0.39960 | 0.0979 | 0.39230 | 0.2139 | 40.3 |
| 1.0075 | 2 | 5305105 | 0.38859 | 0.2729 | 0.39144 | 0.2276 | 39.6 |
| 1.0075 | 3 | 5405105 | 0.39149 | 0.2269 | 0.38944 | 0.2594 | 38.0 |
| 1.0100 | 0 | 5105130 | 0.36395 | 0.6189 | 0.36921 | 0.5326 | 37.7 |
| 1.0100 | 1 | 5205130 | 0.38361 | 0.2967 | 0.38461 | 0.2803 | 39.4 |
| 1.0100 | 2 | 5305130 | 0.38013 | 0.3537 | 0.38798 | 0.2252 | 38.8 |
| 1.0100 | 3 | 5405130 | 0.38218 | 0.3201 | 0.38244 | 0.3159 | 40.3 |
| 1.0125 | 0 | 5105155 | 0.34225 | 0.9371 | 0.35624 | 0.7006 | 39.0 |
| 1.0125 | 1 | 5205155 | 0.34312 | 0.9224 | 0.34178 | 0.9450 | 37.2 |
| 1.0125 | 2 | 5305155 | 0.34043 | 0.9678 | 0.34298 | 0.9248 | 38.3 |
| 1.0125 | 3 | 5405155 | 0.34275 | 0.9287 | 0.35492 | 0.7229 | 36.6 |
| 1.0150 | 0 | 5105180 | 0.33716 | 0.9860 | 0.33878 | 0.9578 | 37.3 |
| 1.0150 | 1 | 5205180 | 0.33762 | 0.9781 | 0.33726 | 0.9843 | 38.8 |
| 1.0150 | 2 | 5305180 | 0.33901 | 0.9538 | 0.33763 | 0.9778 | 39.6 |
| 1.0150 | 3 | 5405180 | 0.33892 | 0.9554 | 0.33734 | 0.9829 | 37.0 |

**void_6**

| β | chain | seed | E_end | f | E_mid | f_mid | ms/sweep |
|---|---|---|---|---|---|---|---|
| 1.2525 | 0 | 6060041 | 0.32803 | 0.1326 | 0.33049 | 0.0447 | 70.4 |
| 1.2525 | 1 | 6160041 | 0.32655 | 0.1853 | 0.32657 | 0.1845 | 69.6 |
| 1.2525 | 2 | 6260041 | 0.32866 | 0.1101 | 0.32699 | 0.1696 | 68.6 |
| 1.2525 | 3 | 6360041 | 0.32667 | 0.1809 | 0.32708 | 0.1663 | 75.5 |
| 1.2525 | 4 | 6460041 | 0.32812 | 0.1294 | 0.32843 | 0.1182 | 78.2 |
| 1.2525 | 5 | 6560041 | 0.32984 | 0.0679 | 0.32584 | 0.2106 | 75.8 |
| 1.2550 | 0 | 6060066 | 0.32438 | 0.1647 | 0.32471 | 0.1523 | 74.9 |
| 1.2550 | 1 | 6160066 | 0.32343 | 0.2006 | 0.32018 | 0.3229 | 71.5 |
| 1.2550 | 2 | 6260066 | 0.32305 | 0.2148 | 0.32337 | 0.2026 | 71.2 |
| 1.2550 | 3 | 6360066 | 0.32384 | 0.1851 | 0.32410 | 0.1751 | 68.8 |
| 1.2550 | 4 | 6460066 | 0.32540 | 0.1265 | 0.32448 | 0.1609 | 70.1 |
| 1.2550 | 5 | 6560066 | 0.32116 | 0.2860 | 0.32386 | 0.1844 | 76.8 |
| 1.2575 | 0 | 6060091 | 0.31075 | 0.5978 | 0.31495 | 0.4306 | 77.5 |
| 1.2575 | 1 | 6160091 | 0.31533 | 0.4157 | 0.31543 | 0.4118 | 72.2 |
| 1.2575 | 2 | 6260091 | 0.31856 | 0.2869 | 0.32021 | 0.2212 | 71.3 |
| 1.2575 | 3 | 6360091 | 0.30364 | 0.8809 | 0.31382 | 0.4758 | 69.6 |
| 1.2575 | 4 | 6460091 | 0.30958 | 0.6447 | 0.31890 | 0.2737 | 69.3 |
| 1.2575 | 5 | 6560091 | 0.31665 | 0.3630 | 0.31878 | 0.2783 | 70.8 |
| 1.2600 | 0 | 6060116 | 0.29957 | 0.9805 | 0.31352 | 0.3913 | 71.4 |
| 1.2600 | 1 | 6160116 | 0.30171 | 0.8903 | 0.30502 | 0.7503 | 67.4 |
| 1.2600 | 2 | 6260116 | 0.29986 | 0.9686 | 0.30407 | 0.7905 | 67.4 |
| 1.2600 | 3 | 6360116 | 0.30053 | 0.9401 | 0.31023 | 0.5304 | 67.1 |
| 1.2600 | 4 | 6460116 | 0.30053 | 0.9401 | 0.29989 | 0.9673 | 67.0 |
| 1.2600 | 5 | 6560116 | 0.30532 | 0.7379 | 0.31104 | 0.4962 | 68.4 |
| 1.2625 | 0 | 6060141 | 0.29797 | 0.9821 | 0.30001 | 0.8906 | 69.3 |
| 1.2625 | 1 | 6160141 | 0.29786 | 0.9872 | 0.30081 | 0.8544 | 68.0 |
| 1.2625 | 2 | 6260141 | 0.29892 | 0.9392 | 0.29911 | 0.9308 | 68.7 |
| 1.2625 | 3 | 6360141 | 0.29925 | 0.9247 | 0.29724 | 1.0149 | 71.2 |
| 1.2625 | 4 | 6460141 | 0.29847 | 0.9596 | 0.29756 | 1.0006 | 72.9 |
| 1.2625 | 5 | 6560141 | 0.29855 | 0.9563 | 0.29947 | 0.9148 | 70.9 |

**void_8**

| β | chain | seed | E_end | f | E_mid | f_mid | ms/sweep |
|---|---|---|---|---|---|---|---|
| 1.2525 | 0 | 6075879 | 0.33086 | 0.0061 | 0.32695 | 0.1525 | 221.3 |
| 1.2525 | 1 | 6175879 | 0.32879 | 0.0835 | 0.32811 | 0.1092 | 224.9 |
| 1.2525 | 2 | 6275879 | 0.32821 | 0.1051 | 0.32841 | 0.0976 | 215.9 |
| 1.2525 | 3 | 6375879 | 0.32859 | 0.0909 | 0.32778 | 0.1216 | 219.7 |
| 1.2525 | 4 | 6475879 | 0.32763 | 0.1271 | 0.32674 | 0.1605 | 216.7 |
| 1.2525 | 5 | 6575879 | 0.32801 | 0.1129 | 0.32940 | 0.0608 | 220.6 |
| 1.2550 | 0 | 6075904 | 0.32388 | 0.1628 | 0.32469 | 0.1307 | 221.7 |
| 1.2550 | 1 | 6175904 | 0.32434 | 0.1447 | 0.32320 | 0.1898 | 225.4 |
| 1.2550 | 2 | 6275904 | 0.32251 | 0.2173 | 0.32405 | 0.1561 | 223.2 |
| 1.2550 | 3 | 6375904 | 0.32318 | 0.1906 | 0.32192 | 0.2406 | 227.3 |
| 1.2550 | 4 | 6475904 | 0.32263 | 0.2125 | 0.32194 | 0.2399 | 226.5 |
| 1.2550 | 5 | 6575904 | 0.32424 | 0.1486 | 0.32419 | 0.1506 | 227.9 |
| 1.2575 | 0 | 6075929 | 0.31738 | 0.3186 | 0.31748 | 0.3145 | 228.7 |
| 1.2575 | 1 | 6175929 | 0.31804 | 0.2908 | 0.31576 | 0.3872 | 232.9 |
| 1.2575 | 2 | 6275929 | 0.31174 | 0.5563 | 0.31549 | 0.3986 | 222.1 |
| 1.2575 | 3 | 6375929 | 0.31473 | 0.4303 | 0.31360 | 0.4778 | 227.0 |
| 1.2575 | 4 | 6475929 | 0.31679 | 0.3435 | 0.31571 | 0.3893 | 204.7 |
| 1.2575 | 5 | 6575929 | 0.31619 | 0.3689 | 0.31646 | 0.3577 | 206.8 |
| 1.2600 | 0 | 6075954 | 0.30252 | 0.8699 | 0.30835 | 0.6086 | 210.2 |
| 1.2600 | 1 | 6175954 | 0.30297 | 0.8496 | 0.30865 | 0.5953 | 215.9 |
| 1.2600 | 2 | 6275954 | 0.30044 | 0.9632 | 0.30429 | 0.7908 | 217.6 |
| 1.2600 | 3 | 6375954 | 0.30113 | 0.9323 | 0.30631 | 0.7001 | 221.1 |
| 1.2600 | 4 | 6475954 | 0.30122 | 0.9284 | 0.30769 | 0.6383 | 221.2 |
| 1.2600 | 5 | 6575954 | 0.30171 | 0.9063 | 0.30224 | 0.8825 | 226.9 |
| 1.2625 | 0 | 6075979 | 0.29863 | 0.9720 | 0.29966 | 0.9225 | 223.7 |
| 1.2625 | 1 | 6175979 | 0.29908 | 0.9505 | 0.30085 | 0.8654 | 221.6 |
| 1.2625 | 2 | 6275979 | 0.29905 | 0.9520 | 0.29829 | 0.9881 | 217.4 |
| 1.2625 | 3 | 6375979 | 0.29892 | 0.9582 | 0.29993 | 0.9095 | 219.5 |
| 1.2625 | 4 | 6475979 | 0.30009 | 0.9021 | 0.30471 | 0.6802 | 216.3 |
| 1.2625 | 5 | 6575979 | 0.29838 | 0.9840 | 0.30068 | 0.8736 | 215.2 |
