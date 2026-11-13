# Gate DL-BETA P50 — result

**Verdict: SC-DLBP-1 (sharpened).** Compact U(1) (Wilson action, FCC void network × time, β_t = β_s) gives
**β_c = 1.25771 ± 0.00107** in the card convention, so **1/e²_c = β_c/√2 = 0.88933 ± 0.00076**. U = 0.00107 is
below the 0.0020 threshold. The interval β_c ± 2U = [1.25556, 1.25986] overlaps both prior intervals, and β_c lies
inside each of them: 0.00104 below the top of Gate DL-BETA's [1.24875, 1.25875] and 0.00146 above the bottom of
REP1's [1.25625, 1.26125]. Its distance to each interval is 0.00 U.

**Status.** Card §5 makes β_c ± U the **quoted value**: a single-code figure with a statistical error, **CONJECTURE
as a figure**. It replaces REP1's 1.25875 ± 0.0025. Everything in this file is a same-session result, capped at
CONJECTURE.

**Checks.** K1, K2 and K3 pass. The Z4 control gives β₅₀(L = 12) = 1.01045, inside K3's window [1.0051, 1.0171].
All four lattices have clean branches, are bracketed without extensions, and have converged probit fits with no
bootstrap failures. On Z4, the same estimator extrapolates to β_∞ = 1.01144 ± 0.00134, which is +0.23 U from the
literature value 1.0111331 (Q6, not a verdict input). All four K2 series are bit-identical to REP1's. The pinned
driver at first said "no" for the two Z4 series. That was a NaN-comparison artefact, fixed under CN-DLBP-01 (§9).

**Run.** 12–13 November 2026, 23:31–04:05 UTC (10:31–15:05 AEDT, 13 November). Analyst: Claude (Opus 5.5).
Simulation 23:33:34–03:53:03 UTC: 136 runs, 518.9 core-minutes on 2 cores. **This run was started as a scheduled
task (a fresh cloud session) at the user's request, rather than in a hand-opened thread inside the BCT Project**
(§0).

---

## 0. Provenance and disclosures

**Card.** I fetched `audit/gates/gate_DLBETA_P50_prompt.md` at commit `26c91c99608a2742d7cbf8dafdec6193c7831926`
with `curl` from its commit-pinned raw URL, wrote it to disk and hashed it before reading it. Its record,
`audit/gates/PREREG_20261113_DLBETA_P50.sha256`, was hashed the same way.

| file | SHA-256 | expected | |
|---|---|---|---|
| `gate_DLBETA_P50_prompt.md` | `50525acce2f167ee78536c519562f6ea09d8aaa1768d524b2e6aaa1b483cfb9e` | same | match |
| `PREREG_20261113_DLBETA_P50.sha256` | `fdb993a5b0b5255426ac27096ec1dffc8c28914a73c0606b0fd958d237e88b53` | same | match |

The record's content is the card's digest (`50525acc…cfb9e`).

**Repository.** The session's clone of `zerofreeparameters-code/BCT-Programme` was already at `26c91c99…`. A
`git fetch --depth 1 origin 26c91c99…` returned the same SHA, and the diff against it was empty. All ten §4.1
files were hash-checked before use and all ten match (`as_run/pins_check.txt`). The two pinned code files were
copied into a work directory and hashed again there; both match.

**Environment.** Python 3.13.18, NumPy 2.5.3, SciPy 1.18.1, numba 0.68.1 (from `pip install numba scipy`), llvmlite
0.50.0. 2 cores (Intel Xeon @ 2.10 GHz), 7 GB RAM, 2 workers, one chain per core. These versions are REP1's
(REP1 result §0).

**Disclosures.**

- **Scheduled task.** This run was started as a scheduled task (a fresh cloud session) at the user's request,
  rather than in a hand-opened thread inside the BCT Project. Card §10 asks the user to switch off "Search and
  reference past chats" and "Generate memory from chats" before opening the thread. This session cannot see those
  settings. It called no memory, past-chat or Project tool.
- **Not blind.** The card states both prior results (§1), and so did this run. Under §4.7, `dlbp_numbers.txt` was
  hashed and the hash posted before the verdict step compared anything with the prior gates.
- **Seeds.** None of the 212 seeds this card can generate (fixed runs plus every possible extension) coincides with
  any of REP1's 410 gate seeds. K2 reuses REP1's four K3 seeds on purpose.
- **Numba cache.** The simulator's `@njit(cache=True)` wrote untracked cache files into the clone's
  `audit/gates/DLBETA_REP1/run/__pycache__/`. They are not committed, and they cannot change a number.
- **Scripts written during the run.** `run/dlbp_report.py` (Markdown tables) was written while the void chains ran.
  `run/dlbp_crosscheck.py` (§8) was written after the verdict. Neither computes a verdict input.
- **Delivery.** Card §10 says the session cannot push and asks for a `git format-patch`. The run prompt said to try a
  push first, and to fall back to the patch only if the push failed. This file's commit adds
  `audit/gates/DLBETA_P50/` only.

## 1. Code and checks (Q1)

**Card versus code.** Before running, I compared `dlbp_driver.py`, `dlbp_analysis.py` and `dlbr_sim.py` with the
card, item by item:

- the seeds and the round-half-even rule;
- the E_end readings (sweeps 2550–3000) and the E_mid readings (sweeps 1050–1500), with row 0 of the series being
  the start;
- the 500 + 1500 branch runs with 20 blocks;
- the integrity rule, the bracket rule and the extension rule;
- the probit's start values and its convergence rule;
- the bootstrap: resampling, branch redraws, RNG seeds 51000 + L and 52000 + L, and the 5 % flag;
- the σ floor, k, β_∞, σ_∞, U;
- the verdict order and the two prior intervals.

All agree. One mismatch surfaced after the run, in a reported item that is not a pass condition: the K2
bit-identity test (CN-DLBP-01, §9).

| check | run | seed | value | target | dev | pass | bit-identical to REP1 |
|---|---|---|---|---|---|---|---|
| K1 | dlbr_sim.py SHA-256 | — | `560c256fe391bfa7…` | `560c256fe391bfa7…` | — | PASS | — |
| K2 | void_b0.1_hot (1000 + 10000) | 716838 | 0.049794 | 0.049938 | -0.287 % | PASS | yes |
| K2 | void_b20_cold (1000 + 10000) | 915839 | 0.014361 | 0.014258 | +0.724 % | PASS | yes |
| K2 | z4_b0.1_hot (1000 + 10000) | 332676 | 0.049866 | 0.049938 | -0.143 % | PASS | yes |
| K2 | z4_b20_cold (1000 + 10000) | 531677 | 0.012527 | 0.012451 | +0.610 % | PASS | yes |

K1 passes. Each K2 run is within 2 % of its target. **K2 bit-identity: yes for all four.** Every byte of every
series matches REP1's stored series. That is consistent with the matching toolchain above. K3 passes: Z4 at L = 12
is clean and bracketed, its fit converges, and β₅₀ = 1.01045 lies inside [1.0051, 1.0171].

## 2. Branches, φ and crossings, lattice by lattice (Q2, Q3)

Window chains ran 3000 sweeps from the mixed start: 4 chains per point on Z4, 6 on the void. Every chain's E_end,
f, E_mid and seed is listed in Appendix A. **No bracket extension was triggered on any lattice.** The driver's
`state.json` records `ext = {}` for all four, so every grid is the card's fixed window.

### z4_8: z4 L = 8 (L_t = 8), V = 4096

**Branch runs** (500 + 1500 sweeps; E = mean over the 1500 measurement sweeps; error from 20 blocks)

| start | β | seed | E | σ_E | block span | G(β) | 0.25·G | ok | ms/sweep |
|---|---|---|---|---|---|---|---|---|---|
| hot | 0.9800 | 3073152 | 0.44868 | 0.00080 | 0.01344 | 0.08719 | 0.02180 | ok | 6.6 |
| hot | 0.9850 | 3073202 | 0.44250 | 0.00077 | 0.01500 | 0.08373 | 0.02093 | ok | 6.5 |
| hot | 0.9900 | 3073252 | 0.43559 | 0.00111 | 0.01806 | 0.08027 | 0.02007 | ok | 6.7 |
| hot | 0.9950 | 3073302 | 0.42640 | 0.00121 | 0.01643 | 0.07681 | 0.01920 | ok | 6.6 |
| cold | 1.0200 | 3073553 | 0.33101 | 0.00032 | 0.00564 | 0.05951 | 0.01488 | ok | 6.5 |
| cold | 1.0250 | 3073603 | 0.32688 | 0.00039 | 0.00639 | 0.05605 | 0.01401 | ok | 6.6 |
| cold | 1.0300 | 3073653 | 0.32267 | 0.00033 | 0.00630 | 0.05259 | 0.01315 | ok | 6.6 |
| cold | 1.0350 | 3073703 | 0.31936 | 0.00038 | 0.00562 | 0.04913 | 0.01228 | ok | 6.4 |

- S(β) = 1.894636 + (-1.474780)·β; residuals [-0.00067, 0.00052, 0.00099, -0.00083]
- W(β) = 1.129371 + (-0.782864)·β; residuals [0.00016, -6e-05, -0.00035, 0.00025]
- Integrity: **clean** (every span ≤ 0.25·G: True; S strictly decreasing: True; W strictly decreasing: True; G > 0 at every window point: True)

**φ(β)** (3000-sweep mixed starts; f = (S − E_end)/(S − W); every chain's f and seed in Appendix A)

| β | S(β) | W(β) | G(β) | n | φ | σ_φ | weak fraction (f > ½) |
|---|---|---|---|---|---|---|---|
| 1.0000 | 0.41986 | 0.34651 | 0.07335 | 4 | 0.0591 | 0.0228 | 0.000 |
| 1.0025 | 0.41617 | 0.34455 | 0.07162 | 4 | 0.1077 | 0.0296 | 0.000 |
| 1.0050 | 0.41248 | 0.34259 | 0.06989 | 4 | 0.2985 | 0.1846 | 0.250 |
| 1.0075 | 0.40880 | 0.34064 | 0.06816 | 4 | 0.6505 | 0.1101 | 0.750 |
| 1.0100 | 0.40511 | 0.33868 | 0.06643 | 4 | 0.8934 | 0.0167 | 1.000 |

- Grid [1.0000, 1.0100]; extensions: none; bracketed: **yes**
- Probit: **β₅₀ = 1.00640**, w = 0.00299, converged: **True**; σ_boot = 0.00059, **σ = 0.00070**; bootstrap failures 0/1000

### z4_12: z4 L = 12 (L_t = 12), V = 20736

**Branch runs** (500 + 1500 sweeps; E = mean over the 1500 measurement sweeps; error from 20 blocks)

| start | β | seed | E | σ_E | block span | G(β) | 0.25·G | ok | ms/sweep |
|---|---|---|---|---|---|---|---|---|---|
| hot | 0.9800 | 3104828 | 0.44984 | 0.00031 | 0.00663 | 0.08369 | 0.02092 | ok | 33.4 |
| hot | 0.9850 | 3104878 | 0.44274 | 0.00037 | 0.00569 | 0.08000 | 0.02000 | ok | 33.4 |
| hot | 0.9900 | 3104928 | 0.43490 | 0.00054 | 0.00798 | 0.07631 | 0.01908 | ok | 33.8 |
| hot | 0.9950 | 3104978 | 0.42570 | 0.00050 | 0.00846 | 0.07262 | 0.01815 | ok | 33.8 |
| cold | 1.0200 | 3105229 | 0.33215 | 0.00020 | 0.00299 | 0.05416 | 0.01354 | ok | 33.4 |
| cold | 1.0250 | 3105279 | 0.32749 | 0.00026 | 0.00384 | 0.05046 | 0.01262 | ok | 33.2 |
| cold | 1.0300 | 3105329 | 0.32304 | 0.00018 | 0.00320 | 0.04677 | 0.01169 | ok | 33.1 |
| cold | 1.0350 | 3105379 | 0.31919 | 0.00015 | 0.00237 | 0.04308 | 0.01077 | ok | 33.2 |

- S(β) = 2.023483 + (-1.605253)·β; residuals [-0.00049, 0.00043, 0.00062, -0.00055]
- W(β) = 1.216093 + (-0.866787)·β; residuals [0.00018, -0.00014, -0.00027, 0.00023]
- Integrity: **clean** (every span ≤ 0.25·G: True; S strictly decreasing: True; W strictly decreasing: True; G > 0 at every window point: True)

**φ(β)** (3000-sweep mixed starts; f = (S − E_end)/(S − W); every chain's f and seed in Appendix A)

| β | S(β) | W(β) | G(β) | n | φ | σ_φ | weak fraction (f > ½) |
|---|---|---|---|---|---|---|---|
| 1.0050 | 0.41020 | 0.34497 | 0.06523 | 4 | 0.1319 | 0.0164 | 0.000 |
| 1.0075 | 0.40619 | 0.34280 | 0.06339 | 4 | 0.1995 | 0.0112 | 0.000 |
| 1.0100 | 0.40218 | 0.34064 | 0.06154 | 4 | 0.3114 | 0.0380 | 0.000 |
| 1.0125 | 0.39816 | 0.33847 | 0.05969 | 4 | 0.8957 | 0.0211 | 1.000 |
| 1.0150 | 0.39415 | 0.33630 | 0.05785 | 4 | 0.9721 | 0.0077 | 1.000 |

- Grid [1.0050, 1.0150]; extensions: none; bracketed: **yes**
- Probit: **β₅₀ = 1.01045**, w = 0.00236, converged: **True**; σ_boot = 0.00020, **σ = 0.00070**; bootstrap failures 0/1000

### void_6: void L = 6 (L_t = 18), V = 3888

**Branch runs** (500 + 1500 sweeps; E = mean over the 1500 measurement sweeps; error from 20 blocks)

| start | β | seed | E | σ_E | block span | G(β) | 0.25·G | ok | ms/sweep |
|---|---|---|---|---|---|---|---|---|---|
| hot | 1.2300 | 4059814 | 0.35788 | 0.00032 | 0.00584 | 0.04114 | 0.01029 | ok | 62.5 |
| hot | 1.2350 | 4059864 | 0.35207 | 0.00025 | 0.00461 | 0.03836 | 0.00959 | ok | 63.0 |
| hot | 1.2400 | 4059914 | 0.34756 | 0.00031 | 0.00507 | 0.03557 | 0.00889 | ok | 62.8 |
| hot | 1.2450 | 4059964 | 0.34011 | 0.00038 | 0.00640 | 0.03278 | 0.00820 | ok | 62.5 |
| cold | 1.2650 | 4060165 | 0.29609 | 0.00016 | 0.00268 | 0.02164 | 0.00541 | ok | 62.2 |
| cold | 1.2700 | 4060215 | 0.29285 | 0.00015 | 0.00232 | 0.01885 | 0.00471 | ok | 62.4 |
| cold | 1.2750 | 4060265 | 0.28984 | 0.00012 | 0.00198 | 0.01606 | 0.00402 | ok | 62.2 |
| cold | 1.2800 | 4060315 | 0.28711 | 0.00012 | 0.00179 | 0.01328 | 0.00332 | ok | 62.4 |

- S(β) = 1.780576 + (-1.156503)·β; residuals [-0.0002, -0.00023, 0.00105, -0.00062]
- W(β) = 1.053871 + (-0.599137)·β; residuals [0.00012, -0.00012, -0.00014, 0.00013]
- Integrity: **clean** (every span ≤ 0.25·G: True; S strictly decreasing: True; W strictly decreasing: True; G > 0 at every window point: True)

**φ(β)** (3000-sweep mixed starts; f = (S − E_end)/(S − W); every chain's f and seed in Appendix A)

| β | S(β) | W(β) | G(β) | n | φ | σ_φ | weak fraction (f > ½) |
|---|---|---|---|---|---|---|---|
| 1.2525 | 0.33206 | 0.30345 | 0.02860 | 6 | 0.1584 | 0.0116 | 0.000 |
| 1.2550 | 0.32916 | 0.30195 | 0.02721 | 6 | 0.2016 | 0.0166 | 0.000 |
| 1.2575 | 0.32627 | 0.30046 | 0.02582 | 6 | 0.3577 | 0.0602 | 0.167 |
| 1.2600 | 0.32338 | 0.29896 | 0.02442 | 6 | 0.8141 | 0.0690 | 1.000 |
| 1.2625 | 0.32049 | 0.29746 | 0.02303 | 6 | 0.9782 | 0.0169 | 1.000 |

- Grid [1.2525, 1.2625]; extensions: none; bracketed: **yes**
- Probit: **β₅₀ = 1.25784**, w = 0.00305, converged: **True**; σ_boot = 0.00032, **σ = 0.00070**; bootstrap failures 0/1000

### void_8: void L = 8 (L_t = 24), V = 12288

**Branch runs** (500 + 1500 sweeps; E = mean over the 1500 measurement sweeps; error from 20 blocks)

| start | β | seed | E | σ_E | block span | G(β) | 0.25·G | ok | ms/sweep |
|---|---|---|---|---|---|---|---|---|---|
| hot | 1.2300 | 4075652 | 0.35768 | 0.00013 | 0.00222 | 0.04085 | 0.01021 | ok | 203.0 |
| hot | 1.2350 | 4075702 | 0.35245 | 0.00017 | 0.00261 | 0.03798 | 0.00949 | ok | 203.4 |
| hot | 1.2400 | 4075752 | 0.34654 | 0.00015 | 0.00246 | 0.03511 | 0.00878 | ok | 200.8 |
| hot | 1.2450 | 4075802 | 0.34006 | 0.00018 | 0.00304 | 0.03224 | 0.00806 | ok | 200.7 |
| cold | 1.2650 | 4076003 | 0.29625 | 0.00014 | 0.00239 | 0.02076 | 0.00519 | ok | 196.0 |
| cold | 1.2700 | 4076053 | 0.29296 | 0.00008 | 0.00125 | 0.01789 | 0.00447 | ok | 195.7 |
| cold | 1.2750 | 4076103 | 0.28984 | 0.00008 | 0.00132 | 0.01502 | 0.00376 | ok | 197.6 |
| cold | 1.2800 | 4076153 | 0.28725 | 0.00005 | 0.00101 | 0.01216 | 0.00304 | ok | 197.3 |

- S(β) = 1.804129 + (-1.175714)·β; residuals [-0.00032, 0.00033, 0.0003, -0.00031]
- W(β) = 1.057522 + (-0.601924)·β; residuals [0.00016, -0.00012, -0.00023, 0.0002]
- Integrity: **clean** (every span ≤ 0.25·G: True; S strictly decreasing: True; W strictly decreasing: True; G > 0 at every window point: True)

**φ(β)** (3000-sweep mixed starts; f = (S − E_end)/(S − W); every chain's f and seed in Appendix A)

| β | S(β) | W(β) | G(β) | n | φ | σ_φ | weak fraction (f > ½) |
|---|---|---|---|---|---|---|---|
| 1.2525 | 0.33155 | 0.30361 | 0.02794 | 6 | 0.1088 | 0.0161 | 0.000 |
| 1.2550 | 0.32861 | 0.30211 | 0.02650 | 6 | 0.2127 | 0.0161 | 0.000 |
| 1.2575 | 0.32567 | 0.30060 | 0.02507 | 6 | 0.3791 | 0.0311 | 0.000 |
| 1.2600 | 0.32273 | 0.29910 | 0.02363 | 6 | 0.8334 | 0.0602 | 1.000 |
| 1.2625 | 0.31979 | 0.29759 | 0.02220 | 6 | 0.9701 | 0.0067 | 1.000 |

- Grid [1.2525, 1.2625]; extensions: none; bracketed: **yes**
- Probit: **β₅₀ = 1.25775**, w = 0.00294, converged: **True**; σ_boot = 0.00018, **σ = 0.00070**; bootstrap failures 0/1000

**Integrity margins.** The largest block span as a fraction of its limit 0.25·G:

| lattice | largest span / (0.25·G) | at |
|---|---|---|
| Z4 L = 8 | 0.90 | hot, β = 0.990 |
| Z4 L = 12 | 0.47 | hot, β = 0.995 |
| void L = 6 | 0.78 | hot, β = 1.245 |
| void L = 8 | 0.46 | cold, β = 1.265 |

The tightest is Z4 L = 8, which is neither a verdict input nor part of K3.

## 3. Result (Q4)

| extrapolation | k | β₅₀(small) | β₅₀(big) | shift | σ_∞ | U | β_∞ |
|---|---|---|---|---|---|---|---|
| **void, L = 6 → 8** | 0.46286 | 1.25784 ± 0.00070 | 1.25775 ± 0.00070 | −0.00004 | 0.00107 | **0.00107** | **1.25771** |
| Z4, L = 8 → 12 | 0.24615 | 1.00640 ± 0.00070 | 1.01045 ± 0.00070 | +0.00100 | 0.00089 | 0.00134 | 1.01144 |

> **β_c = 1.25771 ± 0.00107** (card convention: β is the coefficient of Σ_loops)
> **1/e²_c = β_c/√2 = 0.88933 ± 0.00076** (void complex, β_t = β_s)

**What U is made of.** Every lattice's σ_boot is below the 0.0007 floor: 0.00032 at void L = 6 and 0.00018 at
void L = 8. So both void σ are the floor, and U is the floor's 1.53 × 0.0007 = 0.00107, plus a negligible
extrapolation shift (β₅₀(6) − β₅₀(8) = +0.00009). The statistical part alone would give U ≈ 0.00031. I report that
as an observation; the card's U, 0.00107, is the result.

## 4. Diagnostics (Q5) and calibration (Q6) — reported, not verdict inputs

| lattice | β₅₀ (probit) | φ interpolation crossing | weak-fraction crossing | β₅₀ from E_mid | drift β₅₀ − β₅₀(mid) | w | bootstrap failures |
|---|---|---|---|---|---|---|---|
| Z4 L = 8 | 1.00640 | 1.00643 | 1.00625 | 1.00703 | −0.00064 | 0.00299 | 0 / 1000 |
| Z4 L = 12 | 1.01045 | 1.01081 | 1.01125 | 1.01043 | +0.00002 | 0.00236 | 0 / 1000 |
| void L = 6 | 1.25784 | 1.25828 | 1.25850 | 1.25804 | −0.00020 | 0.00305 | 0 / 1000 |
| void L = 8 | 1.25775 | 1.25817 | 1.25875 | 1.25799 | −0.00024 | 0.00294 | 0 / 1000 |

- **Monotone.** φ has exactly one interpolation crossing on every lattice.
- **Time drift.** Between sweeps 1050–1500 and 2550–3000, the void crossings move down by 0.0002, about 0.2 U. The
  Z4 L = 12 crossing does not move.
- **Estimator spread on the void.** The interpolation crossing sits 0.0004 above the probit β₅₀, and the
  weak-fraction crossing 0.0007–0.0010 above. Both are within U. A likely contributor is that φ does not reach 0
  on the strong side of the window (0.11–0.16 at 1.2525) but does nearly reach 1 on the weak side (0.97–0.98).
  A symmetric 0-to-1 probit then leans to lower β. Whether that floor is slow relaxation at 3000 sweeps or
  curvature of the hot branch over the 0.0075 extrapolation (card §9) is not separated here. This is an
  observation (CONJECTURE).
- **Z4 calibration (Q6).** β_∞(Z4) = 1.01144 ± 0.00134, against 1.0111331 (hep-lat/0210010): **+0.00031 = +0.23 U**.
  β₅₀(L = 12) alone is 0.00069 below the literature value. On Z4 the extrapolation shift (+0.00100) is the larger
  part of U.

## 5. Hash before comparison (§4.7)

| file | SHA-256 | hashed (UTC) | posted (UTC) |
|---|---|---|---|
| `dlbp_numbers.txt`, first pass (kept in `OUT/superseded_CN01/`) | `810450ce0a940ee195fbdf87713ed114ac400f2602fb5fc0010ceed3080bf31f` | 2026-11-13 03:54:38 | 03:54:45 (SendUserMessage), before the verdict step at 03:54:49 |
| `dlbp_numbers.txt`, after CN-DLBP-01 (current, `OUT/`) | `3e033974730cbeaf9fa963bbc5e72af2ff270559bbe56688593e0ff0698b2d5b` | 2026-11-13 03:57:04 | 03:57:16 (SendUserMessage), before the verdict re-run |

The two files differ in the two Z4 K2 lines only ("bit-identical … = no" became "= yes"). `analysis.json` is
byte-identical across the two passes, and so is `verdict.txt`.

## 6. Comparison and verdict (Q7)

`OUT/verdict.txt`:

```
K1 True; K2 True; K3 (Z4 L=12 beta_50 = 1.01045 in [1.0051, 1.0171], clean, bracketed, fit) True
void L=6, L=8 clean, bracketed, fit: True
beta_c = 1.25771 +- 0.00107; U <= 0.002: True
beta_c +- 2U = [1.25556, 1.25986]; overlaps Gate DL-BETA [1.24875, 1.25875]: True; overlaps REP1 [1.25625, 1.26125]: True
distance of beta_c to Gate DL-BETA interval = 0.00000 (0.00 U); to REP1 interval = 0.00000 (0.00 U)
VERDICT SC-DLBP-1
```

| prior | interval | β_c − nearest end | distance to interval | β_c − its central value |
|---|---|---|---|---|
| Gate DL-BETA | [1.24875, 1.25875] | 0.00104 below the upper end | **0 (0.00 U)** | +0.00396 (+3.68 U) |
| Gate DL-BETA REP1 | [1.25625, 1.26125] | 0.00146 above the lower end | **0 (0.00 U)** | −0.00104 (−0.97 U) |

Card §5's codes are tested in order:

- SC-DLBP-0: K1–K3 pass, so it does not apply.
- SC-DLBP-4: the void lattices are clean, bracketed and converged, so it does not apply.
- SC-DLBP-3: U = 0.00107 ≤ 0.0020, so it does not apply.
- SC-DLBP-2: β_c ± 2U overlaps both intervals, so it does not apply.
- **SC-DLBP-1** applies.

The last column of the table is an observation, not a card metric. Neither prior interval had a statistical part
(card §1). The new value sits inside both: 0.00104 below REP1's central value and 0.00396 above the original's.

**Also reported (§5):**

- distances: 0.00 U to both prior intervals;
- Z4 calibration: +0.23 U;
- K2 bit-identity: yes, all four (after CN-DLBP-01);
- time drift: −0.00020 at void L = 6, −0.00024 at void L = 8.

## 7. Analyst's forecasts (card §8), scored

| forecast | outcome | score |
|---|---|---|
| K1–K3 pass: 88 % | all pass | **hit** (Brier 0.014) |
| Verdict: SC-DLBP-1 55 %; -3 22 %; -2 8 %; -4 8 %; -0 7 % | SC-DLBP-1 | the modal bin (multi-class Brier 0.269) |
| β₅₀(void, L = 8) in [1.2565, 1.2600]: 65 % | 1.25775 | **hit** (Brier 0.123) |
| \|β₅₀(6) − β₅₀(8)\| ≤ 0.002: 65 % | 0.00009 | **hit** (Brier 0.123) |
| Z4 β_∞ within 2U of 1.0111331: 60 % | +0.23 U | **hit** (Brier 0.160) |
| K2 bit-identical to REP1: 70 % if the same container image, otherwise low | all four bit-identical. The toolchain matches REP1's; whether the image is the same is not known | **hit** under the 70 % branch (Brier 0.090). The pinned code's raw output said 2 of 4 until CN-DLBP-01 |

Every forecast fell on the side it favoured. The |β₅₀(6) − β₅₀(8)| outcome (0.00009) was far inside its bound.

## 8. Verification (after the verdict; not a verdict input)

`run/dlbp_crosscheck.py` recomputes §4.5 from the raw `.npz` series rather than from the records' summary fields.
It uses different routines (`numpy.polyfit`, `scipy.optimize.curve_fit` with bounds) and re-derives every seed from
the §4.4 formula. Results (`OUT/crosscheck_output.txt`):

- all 136 series hashes match their records;
- every seed follows §4.4;
- every branch E and σ_E, E_end and E_mid matches to 10⁻¹³;
- the lines and φ match;
- every β₅₀ and w matches to 10⁻⁶;
- an independent 300-replica bootstrap with a different RNG gives σ_boot 0.00063, 0.00020, 0.00031 and 0.00018
  (pinned: 0.00059, 0.00020, 0.00032, 0.00018);
- both extrapolations reproduce β_∞ and U.

**CROSS-CHECK PASS.**

## 9. Correction notices

- **CN-DLBP-01 (K2 bit-identity: a NaN comparison).**
  - **What was wrong.** The pinned driver tested bit-identity with `np.array_equal(ref, ser)`. Z4 has no temporal
    loops, so column 2 (E_t) of every Z4 series is NaN, and `array_equal` treats NaN ≠ NaN. So it reported
    "not bit-identical" for the two Z4 K2 series, which are byte-for-byte identical to REP1's. Card §4.3 asks
    whether each series is bit-identical, so the code contradicted the card.
  - **The fix (§6).** One line: both arrays are compared through a `uint64` view, which is an exact bit
    comparison. `dlbp_driver.py` `29e7e175ecbaffc80b164ed0b3de6572d5f85f219906da230d0ee2f960aaa8db` →
    `run/dlbp_driver_CN01.py` `9f26b6fc3cd2dad7ae1cf44d5eddeeff2ed6229c2d019b6eae1beb800954f820`.
  - **What was re-run.** Only what the fix affects: the four K2 chains. Their first-pass records and series were
    moved to `OUT/superseded_CN01/`. The re-run series are byte-identical to the first pass.
  - **Re-hash.** The numbers step was re-run, the new file hashed and the hash posted, then the verdict re-run.
  - **Effect.** The K2 bit-identity item changes from "2 of 4" to "4 of 4". Nothing else changes: `analysis.json`
    and `verdict.txt` are byte-identical. It is not a pass condition and not a verdict input.
  - **Kept.** The first pass's state, analysis, numbers file (with its posted hash), verdict and logs are in
    `OUT/superseded_CN01/`.
- No other notice. No lattice, size, grid, chain count, sweep count, seed, estimator, threshold or extension rule
  was changed.

## 10. Limits

- Card §9's limits all apply:
  - Wilson action only, β_t = β_s only, one spatial complex, bare couplings, and a tree-level k;
  - two sizes;
  - a fixed-time estimator;
  - straight branch lines extrapolated by up to 0.0175 in β here (no extensions were triggered);
  - one code in one session;
  - the order of the transition is not addressed.
- **U is the floor.** It is set by the 0.0007 floor, not by the bootstrap (§3). The estimator spread (§4) is
  within U but is not part of its statistical content.
- **φ's strong-side floor.** φ sits at 0.11–0.16 on the strong side of the window (§4). That is the curvature or
  relaxation question the card flags, and it is unresolved.

## 11. Plain-language summary

Two earlier gates located the "tipping point" of electromagnetism simulated on the network of gaps between packed
spheres, with time added. Below it the field is confined; above it, light travels freely. The two gates agreed on
where it is, about 1.25–1.26 in the card's units, but neither gave a real error bar. Each tried one simulation per
setting and sorted it with hard cut-offs. The second gate's headline number rested on two runs that landed almost
exactly on their cut-offs.

This gate ran 6 independent simulations at each of 5 settings, on two box sizes. Each was started half in one phase
and half in the other. Each simulation was scored on a smooth scale, by how far it had moved towards each phase, so
no single run could tip the answer. It fitted a smooth S-curve through all of them, used resampling to get the
error, and extrapolated to an infinite box. The identical method was first tried on the ordinary cubic lattice,
where the answer is known (1.0111). It gave 1.0114 ± 0.0013.

On the sphere-gap network, the answer is **β_c = 1.2577 ± 0.0011, so 1/e² = 0.8893 ± 0.0008**. Both box sizes give
the same crossing to within 0.0001, so the extrapolation hardly moves it. The new value sits inside both earlier
error bars: a little below the second gate's 1.2588 and a little above the first gate's 1.2538. Its error is a
little over 2.3 times smaller than the second gate's. Most of that error is a deliberately cautious floor (the spread of a value known only to within one grid step,
applied to each box size); the purely statistical scatter is three to four times smaller still.

The number counts as the quoted value now. It is still a conjecture: one program, one session.

## 12. Files

Everything below `audit/gates/DLBETA_P50/` is listed with SHA-256 in `MANIFEST.sha256`.

| path | what |
|---|---|
| `gate_DLBETA_P50_RESULT.md` | this file |
| `as_run/gate_DLBETA_P50_prompt.md`, `as_run/PREREG_20261113_DLBETA_P50.sha256` | the card and its record, as fetched |
| `as_run/run_prompt.txt` | the run prompt (scheduled task) |
| `as_run/P50_RUN_LOG.md` | timestamped log |
| `as_run/pins.sha256`, `as_run/pins_check.txt` | the §4.1 pins and their check |
| `run/dlbp_driver.py`, `run/dlbp_analysis.py` | the pinned code as run (hashes as §4.1) |
| `run/dlbp_driver_CN01.py` | CN-DLBP-01's one-line fix (K2 re-run only) |
| `run/dlbp_report.py`, `run/dlbp_crosscheck.py` | report tables; independent cross-check |
| `OUT/records/*.json`, `OUT/series/*.npz` | 136 run records (seeds, E, block means, readings every 50 sweeps, series hashes) and full series (E, E_s, E_t after every sweep, row 0 = start) |
| `OUT/state.json`, `OUT/analysis.json` | driver state (K1, K2, extensions); all estimators |
| `OUT/dlbp_numbers.txt`, `OUT/dlbp_numbers.sha256`, `OUT/dlbp_numbers_hashed_at.txt`, `OUT/dlbp_numbers_posted_at.txt` | numbers, their hash and times |
| `OUT/verdict.txt`, `OUT/verdict_run_at.txt` | verdict |
| `OUT/driver_log.txt`, `OUT/driver_stdout.txt`, `OUT/driver_stdout_CN01.txt`, `OUT/numbers_stdout.txt` | logs |
| `OUT/tables.md`, `OUT/crosscheck_output.txt` | tables used here; cross-check output |
| `OUT/superseded_CN01/` | the first pass's state, analysis, numbers (hash `810450ce…`), verdict, logs and four K2 records and series |

## Appendix A — every mixed chain

f = (S(β) − E_end)/(S(β) − W(β)), with S and W the lattice's lines. f_mid uses E_mid. Seeds follow §4.4.

**z4_8**

| β | chain | seed | E_end | f | E_mid | f_mid | ms/sweep |
|---|---|---|---|---|---|---|---|
| 1.0000 | 0 | 3073354 | 0.41742 | 0.0332 | 0.40933 | 0.1436 | 6.5 |
| 1.0000 | 1 | 3173354 | 0.41084 | 0.1229 | 0.41454 | 0.0725 | 6.6 |
| 1.0000 | 2 | 3273354 | 0.41836 | 0.0204 | 0.41278 | 0.0965 | 6.5 |
| 1.0000 | 3 | 3373354 | 0.41546 | 0.0599 | 0.40786 | 0.1636 | 6.6 |
| 1.0025 | 0 | 3073379 | 0.40305 | 0.1831 | 0.39970 | 0.2300 | 6.5 |
| 1.0025 | 1 | 3173379 | 0.41239 | 0.0527 | 0.41042 | 0.0803 | 6.7 |
| 1.0025 | 2 | 3273379 | 0.41122 | 0.0691 | 0.40583 | 0.1443 | 6.5 |
| 1.0025 | 3 | 3373379 | 0.40716 | 0.1258 | 0.41078 | 0.0752 | 6.6 |
| 1.0050 | 0 | 3073404 | 0.40915 | 0.0477 | 0.40527 | 0.1033 | 6.6 |
| 1.0050 | 1 | 3173404 | 0.39774 | 0.2110 | 0.40276 | 0.1392 | 6.6 |
| 1.0050 | 2 | 3273404 | 0.35360 | 0.8425 | 0.37614 | 0.5199 | 6.6 |
| 1.0050 | 3 | 3373404 | 0.40601 | 0.0926 | 0.39859 | 0.1988 | 6.5 |
| 1.0075 | 0 | 3073429 | 0.35784 | 0.7476 | 0.38706 | 0.3189 | 6.6 |
| 1.0075 | 1 | 3173429 | 0.38519 | 0.3463 | 0.35766 | 0.7502 | 6.6 |
| 1.0075 | 2 | 3273429 | 0.35023 | 0.8592 | 0.38925 | 0.2868 | 6.5 |
| 1.0075 | 3 | 3373429 | 0.36456 | 0.6490 | 0.35935 | 0.7254 | 6.6 |
| 1.0100 | 0 | 3073454 | 0.34664 | 0.8802 | 0.34256 | 0.9416 | 6.6 |
| 1.0100 | 1 | 3173454 | 0.34649 | 0.8824 | 0.34554 | 0.8967 | 6.6 |
| 1.0100 | 2 | 3273454 | 0.34249 | 0.9427 | 0.35329 | 0.7800 | 6.5 |
| 1.0100 | 3 | 3373454 | 0.34741 | 0.8685 | 0.35133 | 0.8096 | 6.5 |

**z4_12**

| β | chain | seed | E_end | f | E_mid | f_mid | ms/sweep |
|---|---|---|---|---|---|---|---|
| 1.0050 | 0 | 3105080 | 0.40443 | 0.0885 | 0.40309 | 0.1091 | 33.0 |
| 1.0050 | 1 | 3205080 | 0.39969 | 0.1612 | 0.39879 | 0.1750 | 33.2 |
| 1.0050 | 2 | 3305080 | 0.40023 | 0.1529 | 0.40267 | 0.1155 | 33.2 |
| 1.0050 | 3 | 3405080 | 0.40206 | 0.1248 | 0.40035 | 0.1511 | 33.4 |
| 1.0075 | 0 | 3105105 | 0.39543 | 0.1698 | 0.39262 | 0.2141 | 33.1 |
| 1.0075 | 1 | 3205105 | 0.39375 | 0.1962 | 0.38741 | 0.2963 | 33.0 |
| 1.0075 | 2 | 3305105 | 0.39286 | 0.2103 | 0.39513 | 0.1745 | 33.3 |
| 1.0075 | 3 | 3405105 | 0.39213 | 0.2218 | 0.39381 | 0.1954 | 33.6 |
| 1.0100 | 0 | 3105130 | 0.38584 | 0.2655 | 0.38386 | 0.2976 | 33.4 |
| 1.0100 | 1 | 3205130 | 0.38647 | 0.2553 | 0.38510 | 0.2775 | 33.6 |
| 1.0100 | 2 | 3305130 | 0.37627 | 0.4210 | 0.37348 | 0.4664 | 33.6 |
| 1.0100 | 3 | 3405130 | 0.38348 | 0.3038 | 0.38006 | 0.3595 | 33.7 |
| 1.0125 | 0 | 3105155 | 0.34290 | 0.9258 | 0.33982 | 0.9774 | 33.1 |
| 1.0125 | 1 | 3205155 | 0.34533 | 0.8852 | 0.34480 | 0.8940 | 33.1 |
| 1.0125 | 2 | 3305155 | 0.34258 | 0.9312 | 0.34279 | 0.9276 | 33.2 |
| 1.0125 | 3 | 3405155 | 0.34799 | 0.8405 | 0.37829 | 0.3329 | 33.6 |
| 1.0150 | 0 | 3105180 | 0.33760 | 0.9777 | 0.34399 | 0.8671 | 33.6 |
| 1.0150 | 1 | 3205180 | 0.33924 | 0.9493 | 0.33767 | 0.9764 | 33.5 |
| 1.0150 | 2 | 3305180 | 0.33753 | 0.9788 | 0.33799 | 0.9708 | 33.3 |
| 1.0150 | 3 | 3405180 | 0.33730 | 0.9827 | 0.33778 | 0.9745 | 33.4 |

**void_6**

| β | chain | seed | E_end | f | E_mid | f_mid | ms/sweep |
|---|---|---|---|---|---|---|---|
| 1.2525 | 0 | 4060041 | 0.32800 | 0.1417 | 0.32604 | 0.2104 | 62.5 |
| 1.2525 | 1 | 4160041 | 0.32812 | 0.1377 | 0.32743 | 0.1617 | 62.5 |
| 1.2525 | 2 | 4260041 | 0.32608 | 0.2088 | 0.32961 | 0.0856 | 64.1 |
| 1.2525 | 3 | 4360041 | 0.32751 | 0.1590 | 0.32717 | 0.1706 | 64.3 |
| 1.2525 | 4 | 4460041 | 0.32719 | 0.1703 | 0.32748 | 0.1600 | 64.3 |
| 1.2525 | 5 | 4560041 | 0.32826 | 0.1328 | 0.32852 | 0.1237 | 65.0 |
| 1.2550 | 0 | 4060066 | 0.32220 | 0.2560 | 0.32232 | 0.2516 | 63.4 |
| 1.2550 | 1 | 4160066 | 0.32515 | 0.1474 | 0.32437 | 0.1761 | 63.6 |
| 1.2550 | 2 | 4260066 | 0.32275 | 0.2359 | 0.32209 | 0.2600 | 62.3 |
| 1.2550 | 3 | 4360066 | 0.32448 | 0.1723 | 0.32258 | 0.2418 | 62.3 |
| 1.2550 | 4 | 4460066 | 0.32338 | 0.2127 | 0.32321 | 0.2189 | 63.8 |
| 1.2550 | 5 | 4560066 | 0.32411 | 0.1856 | 0.32342 | 0.2112 | 63.2 |
| 1.2575 | 0 | 4060091 | 0.31977 | 0.2517 | 0.31410 | 0.4715 | 63.0 |
| 1.2575 | 1 | 4160091 | 0.31498 | 0.4375 | 0.31934 | 0.2685 | 62.8 |
| 1.2575 | 2 | 4260091 | 0.31447 | 0.4572 | 0.31848 | 0.3017 | 62.1 |
| 1.2575 | 3 | 4360091 | 0.32053 | 0.2225 | 0.31224 | 0.5434 | 62.3 |
| 1.2575 | 4 | 4460091 | 0.32075 | 0.2139 | 0.31790 | 0.3241 | 62.1 |
| 1.2575 | 5 | 4560091 | 0.31173 | 0.5635 | 0.31692 | 0.3622 | 62.1 |
| 1.2600 | 0 | 4060116 | 0.30615 | 0.7054 | 0.31309 | 0.4213 | 62.3 |
| 1.2600 | 1 | 4160116 | 0.29972 | 0.9687 | 0.29997 | 0.9588 | 62.4 |
| 1.2600 | 2 | 4260116 | 0.30215 | 0.8693 | 0.30568 | 0.7248 | 63.9 |
| 1.2600 | 3 | 4360116 | 0.30228 | 0.8642 | 0.30827 | 0.6188 | 63.3 |
| 1.2600 | 4 | 4460116 | 0.31053 | 0.5263 | 0.30339 | 0.8186 | 64.4 |
| 1.2600 | 5 | 4560116 | 0.30017 | 0.9505 | 0.30600 | 0.7116 | 63.9 |
| 1.2625 | 0 | 4060141 | 0.29661 | 1.0368 | 0.29806 | 0.9739 | 62.6 |
| 1.2625 | 1 | 4160141 | 0.29823 | 0.9666 | 0.29786 | 0.9825 | 62.5 |
| 1.2625 | 2 | 4260141 | 0.29791 | 0.9806 | 0.29960 | 0.9072 | 63.5 |
| 1.2625 | 3 | 4360141 | 0.29762 | 0.9929 | 0.30368 | 0.7301 | 63.2 |
| 1.2625 | 4 | 4460141 | 0.29784 | 0.9833 | 0.29747 | 0.9994 | 62.6 |
| 1.2625 | 5 | 4560141 | 0.29955 | 0.9091 | 0.30100 | 0.8461 | 62.9 |

**void_8**

| β | chain | seed | E_end | f | E_mid | f_mid | ms/sweep |
|---|---|---|---|---|---|---|---|
| 1.2525 | 0 | 4075879 | 0.32932 | 0.0798 | 0.32695 | 0.1645 | 197.0 |
| 1.2525 | 1 | 4175879 | 0.32802 | 0.1262 | 0.32806 | 0.1248 | 197.2 |
| 1.2525 | 2 | 4275879 | 0.32682 | 0.1691 | 0.32709 | 0.1597 | 198.3 |
| 1.2525 | 3 | 4375879 | 0.32986 | 0.0603 | 0.32870 | 0.1018 | 198.4 |
| 1.2525 | 4 | 4475879 | 0.32899 | 0.0914 | 0.32573 | 0.2084 | 199.3 |
| 1.2525 | 5 | 4575879 | 0.32802 | 0.1262 | 0.32869 | 0.1021 | 199.7 |
| 1.2550 | 0 | 4075904 | 0.32407 | 0.1713 | 0.32456 | 0.1527 | 200.5 |
| 1.2550 | 1 | 4175904 | 0.32378 | 0.1823 | 0.32326 | 0.2017 | 200.2 |
| 1.2550 | 2 | 4275904 | 0.32242 | 0.2337 | 0.32088 | 0.2917 | 199.4 |
| 1.2550 | 3 | 4375904 | 0.32355 | 0.1909 | 0.32353 | 0.1917 | 199.7 |
| 1.2550 | 4 | 4475904 | 0.32275 | 0.2209 | 0.32237 | 0.2356 | 201.1 |
| 1.2550 | 5 | 4575904 | 0.32126 | 0.2773 | 0.32114 | 0.2819 | 201.8 |
| 1.2575 | 0 | 4075929 | 0.31359 | 0.4820 | 0.31367 | 0.4788 | 198.5 |
| 1.2575 | 1 | 4175929 | 0.31629 | 0.3743 | 0.31450 | 0.4457 | 198.1 |
| 1.2575 | 2 | 4275929 | 0.31710 | 0.3417 | 0.31452 | 0.4449 | 201.9 |
| 1.2575 | 3 | 4375929 | 0.31743 | 0.3285 | 0.31433 | 0.4525 | 201.9 |
| 1.2575 | 4 | 4475929 | 0.31416 | 0.4590 | 0.31277 | 0.5144 | 203.9 |
| 1.2575 | 5 | 4575929 | 0.31842 | 0.2892 | 0.31968 | 0.2390 | 204.0 |
| 1.2600 | 0 | 4075954 | 0.30975 | 0.5492 | 0.30989 | 0.5433 | 211.7 |
| 1.2600 | 1 | 4175954 | 0.30134 | 0.9053 | 0.30392 | 0.7960 | 212.3 |
| 1.2600 | 2 | 4275954 | 0.30128 | 0.9076 | 0.30932 | 0.5674 | 209.7 |
| 1.2600 | 3 | 4375954 | 0.30395 | 0.7946 | 0.30837 | 0.6074 | 210.4 |
| 1.2600 | 4 | 4475954 | 0.30088 | 0.9248 | 0.30255 | 0.8539 | 203.3 |
| 1.2600 | 5 | 4575954 | 0.30101 | 0.9192 | 0.30733 | 0.6517 | 202.3 |
| 1.2625 | 0 | 4075979 | 0.29804 | 0.9797 | 0.29959 | 0.9101 | 204.8 |
| 1.2625 | 1 | 4175979 | 0.29854 | 0.9574 | 0.30091 | 0.8507 | 205.2 |
| 1.2625 | 2 | 4275979 | 0.29797 | 0.9829 | 0.29929 | 0.9237 | 202.3 |
| 1.2625 | 3 | 4375979 | 0.29814 | 0.9754 | 0.29849 | 0.9596 | 201.3 |
| 1.2625 | 4 | 4475979 | 0.29886 | 0.9427 | 0.30047 | 0.8704 | 202.6 |
| 1.2625 | 5 | 4575979 | 0.29798 | 0.9824 | 0.29941 | 0.9179 | 202.0 |
