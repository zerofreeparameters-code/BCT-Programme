# Gate DL-BETA REP1 — result

**Verdict: SC-DLBR-1 (replicated).** A second code, written in a second thread from the original card's
specification without sight of the original's code or numbers, passes K1–K5 and puts the transition of
compact U(1) (Wilson action, FCC void network × time, β_t = β_s) in the **same grid step as Gate DL-BETA at
both L = 4 and L = 6, [1.250, 1.255]**. Its mixed-phase result, under the pre-registered branch-relative rule
C1, is **β_∞ = 1.2588 [1.25875] ± 0.0025** (card convention), **1/e²_c = β_∞/√2 = 0.8901 ± 0.0018**.
**Resolved: yes.** **β^R = 1.25875.** The original's interval is I_O = [1.24875, 1.25875], so **d = 0**
(β^R sits on I_O's upper end). The two β_∞ differ by +0.0050.

**Read this with the verdict.** "Resolved" rests on two L = 8 runs whose C1 outcomes sit at their cuts:
the weak win at 1.26125 has f = 0.667003, 0.0003 above 2/3 (7 × 10⁻⁶ in E), and the strong win at 1.25625
has f = 0.32441, 0.009 below 1/3. On this run's own statistical errors, each is close to a coin flip
(probability of the other side 0.49 and 0.41, §9.1). Had either come out unresolved, the code would be
**SC-DLBR-3** (inconclusive). The card's rules apply to the outcome as it fell, and they give SC-DLBR-1.
What does not depend on that margin is the location: the L = 4 and L = 6 jump intervals are identical
across the two codes, and their energies agree run by run (rms 0.97σ and 0.93σ away from the jump, §9.2).

**Status (card §5, §6).** Gate DL-BETA's located transition moves from CONJECTURE to **REPLICATED (two
codes, two threads)**. This run's β_∞ ± u becomes the quoted value, as a **single-code figure at
CONJECTURE**. Everything else in this file is a same-session result, capped at CONJECTURE.
**Order:** "order undetermined" (step 7). New relative to the original: **hysteresis at L = 6** (the hot-start
jump is one grid step later, [1.260, 1.265]).
**Run:** 12–13 November 2026, 23:41–02:20 AEDT, one fresh thread. Analyst: Claude (Opus 5.5). Simulation
23:55–02:10, 261 core-minutes on 2 cores. Same-session results are capped at CONJECTURE.

---

## 0. Provenance and blinding

**Card.** `audit/gates/gate_DLBETA_REP1_prompt.md` at commit `6058f4e63d1ec0aadeb60ce5bb4a73e5c76b5369`, fetched
by commit-pinned raw URL with `curl` to disk and hashed before it was read:
`2ffa8de365a01af1cd3e372998d264d16c2327459e2ffbb5b126f08e7f39a349` (matches
`PREREG_20261112_DLBETA_REP1.sha256`, itself `fc6b6d22c98474795eb470f99ce9f19bc187f4ff61bd60a591caf1f4ffcd51b2` as the
run prompt gave it). §0 was read first.

**Repository.** `git fetch --depth 1` of the pinned commit into an empty repository whose sparse-checkout pattern was
`/audit/gates/DLBETA_REP1/` only, so no file of the commit was written to a working tree. The seven §4.1 open
sources were extracted by exact path with `git show <commit>:<path>` and hashed before reading; all seven match §4.1
(`src_rep1/HASHCHECK.txt`). `dlb_deskcheck.py` was extracted, hash-checked and moved into a mode-000 directory until
the run's own K1 numbers were written and hashed. No repository-wide search, listing, `git log -p` or `git show` of
the DL-BETA commit was run. The two sealed files were not opened, printed, searched or listed before §4.7.

**Pre-existing files (disclosed).** When this run started (23:41 AEDT), its working directory already held
`CHECKPOINT_00_fetch.txt`, `CHECKPOINT_01_hash_verified.txt` and two directories, `prior_attempt_note/` and
`sources/`, with modification times 23:36–23:40, before this thread's first command. The session's task list also
started at #14. Both point to an earlier, interrupted attempt in the same container. None of those files or
directories was opened or listed, and nothing from them was used: this run re-fetched everything into fresh
directories. No sealed material was seen. SC-DLBR-1 is therefore scorable.

**Memory, Project, chats.** Nothing was read from memory, past chats or the Project's knowledge base (claude.ai memory
is off for this account; the Project tool was not called).

**Environment.** Python 3.13.18, NumPy 2.5.3, SciPy 1.18.1, numba 0.68.1. 2 CPU cores, 7 GB RAM; two simulations at
a time, one per core.

## 1. The code (written in this thread from the original card §4.2)

`run/dlbr_sim.py` (complexes, kernel, sampler), `run/dlbr_k1.py` (K1), `run/dlbr_k23.py` (K2, K3, sampler
test), `run/dlbr_stats.py` (estimators and the card's rules; readings RD1–RD12), `run/dlbr_driver.py`
(stages, applied mechanically and in order, resumable), `run/dlbr_numbers.py` (§4.7 file),
`run/dlbr_tables.py` (tables below), `run/dlbr_post.py` (after the hash: Q7 and observations).

- **Complex.** Built from the card's coordinates (units a/4, side 4L): atoms 4(i,j,k) + basis; octs at
  atom + (2,2,2); tets at atom + (1,1,1), (3,3,3). Spatial links oct → tet at (±1,±1,±1). Rhombi per atom and
  bond vector b exactly as the card states, cycle O₁ → T₁ → O₂ → T₂. Temporal links and squares as stated;
  L_t = 3L.
- **Storage and sweep order** (fixed in the module docstring before any run): slice-major; within a slice,
  the 8N spatial links (atom-major, 8 offsets), then the 3N temporal links. One sweep = one heat-bath update
  of link 0, 1, …, N_l − 1.
- **Update.** The staple sum R e^{iφ} over the 4–8 loops containing the link. The new angle is x − φ with
  x ~ von Mises(0, βR), drawn by the Best–Fisher (1979) rejection sampler. Its ρ is written as
  2κ/(τ + √(2τ)), algebraically equal to the textbook form and free of cancellation. κ < 10⁻⁸ draws
  uniformly. No overrelaxation.
- **RNG.** numba's Mersenne Twister, seeded inside compiled code at the start of each chain. The initial
  configuration is drawn from that stream, so each chain is fixed by its seed. Seeds follow REP1 §4.3: Z4
  7919·L + round(10⁴·β) + s + 300,000; void the same + 700,000; s = 0, 1, 2, 3. Every seed is in the tables
  and in `out/raw_records.jsonl`.
- **Mixed start.** Void: every link whose origin node has t < L_t/2 is set to 0, others uniform. Z4 (K5, R4):
  links whose origin site has x₁ < L/2 are set to 0.
- **Observables** every sweep: E, E_s (rhombi), E_t (temporal squares). E errors: 20 blocks, sample sd of
  block means / √20 (RD1). C = N_loops·var(E), population variance; C errors: 20-block jackknife (RD2).
- **Speed:** 0.9, 15–17, 80–88 and 250–255 ms/sweep at void L = 2, 4, 6, 8 (reference code 0.92, 15.2,
  74.3, 241.7).
- **Code frozen** before K4 (`out/code_frozen_before_K4.sha256`). `dlbr_sim.py` was hashed when own K1
  was recorded (`560c256f…`) and is unchanged since. After the driver finished, only the report scripts
  were added or edited (CN-DLBR-02).

**Readings fixed in code before the first run, beyond R1–R9** (`dlbr_stats.py` docstring): RD1 block
sd with ddof = 1; RD2 jackknife form; RD3 locate extension mechanics; RD4 L = 4 edge extension; RD5
hysteresis σ = √(σ_h² + σ_c²); RD6 readings after sweeps 50…2000 and E_end over 1550…2000; RD7 extension
order within a round; RD8 "at most one unresolved L = 8 point" counts every L = 8 run; RD9 no L = 8 run
without an L = 6 primary flip; RD10 Q5 sampling points; RD11 K5 flip interval; RD12 β held as integers in
units of 10⁻⁷. Exercised: RD1, RD2, RD5, RD6, RD8, RD10, RD11, RD12. RD3, RD4, RD7 and RD9 were never
triggered: no stage needed an extension, and an L = 6 flip existed.

## 2. Checks K1–K5 — all pass

| check | lattice | measured | target | pass |
|---|---|---|---|---|
| K1 counts per cell | void, L = 2, 3 | V = 3N, E = 8N, rhombi = 6N, 3-cells = N; degrees oct 8, tet 4; bipartite | desk check A | yes |
| K1 rhombus geometry | void, L = 2, 3 | closed O–T–O–T, planar, area a²/(4√2) = 0.1767766953, normal ∥ bond | desk check A | yes |
| K1 4-cycles | void, L = 2, 3 | exactly the rhombi: 192, 648; no 3-cycles; 3 rhombi per link | 192, 648 | yes |
| K1 rank ∂₂ (space) | void, L = 2, 3 | 158, 538 (SVD and exact mod-p) | 5N − 2 | yes |
| K1 3-cells, χ | void, L = 2, 3 | N rhombic dodecahedra, outward boundaries close; χ = 0 | 0 | yes |
| K1 space × time | L = 2, L_t = 6 | N_v 576, N_l 2112, N_loops 2688; 5 / 8 / 4 loops per link | desk check B | yes |
| K1 rank ∂₂ (space × time) | L = 2, L_t = 6 | 1533 (SVD and mod-p) | N_l − N_v − 3 = 1533 | yes |
| K1 smallest loops | L = 2, L_t = 6 | 4-cycles of the space-time graph = rhombi + temporal squares (2688) | — | yes |
| K1 zero momentum | 11 link classes | rank 5 (14 × 11 class matrix, rows class-consistent) | 5 | yes |
| K1 normalisation | Z4 | c_E = c_B = 1 → a_t = 1, k = 1 | k = 1 | yes |
| K1 normalisation | void × time | c_E = 2, c_B = 1/4 → a_t = 0.3535533906, k = 0.7071067812 | a/(2√2), 1/√2 | yes |
| K1 cross-check | — | `dlb_deskcheck.py` re-run after own K1 was hashed: 49/49, output identical to `dlb_deskcheck_output.txt` except timing lines | — | yes |
| K2 gauge invariance | void L = 2 / Z4 L = 4 | max \|Δcos θ\| 3.6 × 10⁻¹⁵ / 3.5 × 10⁻¹⁵ | 0 | yes |
| K2 local ΔS | void / Z4 | max diff 5.7 × 10⁻¹³ / 2.8 × 10⁻¹³ (200 links) | 0 | yes |
| K3 β = 0.1 hot | void L = 2, L_t = 6 | ⟨cos⟩ = 0.049794 ± 0.000104 (seed 716838) | 0.049938 | −0.29 % |
| K3 β = 20 cold | void | E = 0.014361 ± 0.000005 (seed 915839) | 0.014258 | +0.72 % |
| K3 β = 0.1 hot | Z4 L = 4 | ⟨cos⟩ = 0.049866 ± 0.000181 (seed 332676) | 0.049938 | −0.14 % |
| K3 β = 20 cold | Z4 | E = 0.012527 ± 0.000007 (seed 531677) | 0.012451 | +0.61 % |
| sampler | κ = 0.05–40 | 16 KS p-values 0.150–0.980; ⟨cos⟩ within 1.73σ of I₁/I₀ | — | yes |
| K4 Z4 transition | L = 8 | C max at **1.0075** (hot, 14.56); cold jump [1.0050, 1.0075], fall 0.02343; E\*_hc = 0.37301 | [1.000, 1.012] | yes |
| K5 Z4 mixed | L = 12 | strong 1.002, 1.007; weak 1.012, 1.017, 1.022 → flip **[1.007, 1.012]** | meets [1.0051, 1.0171] | yes |

The β = 20 void value agrees with the desk check's 0.014369 ± 0.000005 (1.1σ), and E_t/E_s = 0.9649
against 0.9643. Own K1 (`out/k1_own.txt`, SHA-256 `469b6ff8…20cd`) was written and hashed at 23:49,
before `dlb_deskcheck.py` was unlocked. No SC-DLBR-4, no SC-DLBR-0.

## 3. Void runs (REP1 §4.4) and the Z4 tables

### K4 — Z4, L = 8, hot and cold, 1000 + 3000 sweeps
| β | E hot | E cold | C hot | C cold | C_max | seeds (hot, cold) |
|---|---|---|---|---|---|---|
| 0.9950 | 0.42474 ± 0.00077 | 0.42592 ± 0.00071 | 2.116 ± 0.177 | 1.789 ± 0.176 | 2.116 | 373302, 373303 |
| 0.9975 | 0.42012 ± 0.00094 | 0.41924 ± 0.00096 | 1.983 ± 0.269 | 2.106 ± 0.242 | 2.106 | 373327, 373328 |
| 1.0000 | 0.41278 ± 0.00100 | 0.41484 ± 0.00085 | 2.311 ± 0.173 | 2.178 ± 0.191 | 2.311 | 373352, 373353 |
| 1.0025 | 0.41049 ± 0.00075 | 0.40791 ± 0.00099 | 1.772 ± 0.153 | 2.314 ± 0.266 | 2.314 | 373377, 373378 |
| 1.0050 | 0.40362 ± 0.00141 | 0.38473 ± 0.00470 | 2.619 ± 0.281 | 12.907 ± 1.655 | 12.907 | 373402, 373403 |
| **1.0075** | 0.37230 ± 0.00512 | 0.36130 ± 0.00458 | 14.557 ± 1.448 | 11.533 ± 2.655 | 14.557 | 373427, 373428 |
| 1.0100 | 0.36146 ± 0.00469 | 0.35162 ± 0.00314 | 12.470 ± 1.906 | 6.219 ± 1.696 | 12.470 | 373452, 373453 |
| 1.0125 | 0.34210 ± 0.00073 | 0.34151 ± 0.00091 | 1.670 ± 0.131 | 1.569 ± 0.181 | 1.670 | 373477, 373478 |
| 1.0150 | 0.33724 ± 0.00076 | 0.33742 ± 0.00065 | 1.474 ± 0.294 | 1.310 ± 0.145 | 1.474 | 373502, 373503 |
| 1.0175 | 0.33452 ± 0.00045 | 0.33441 ± 0.00048 | 1.109 ± 0.083 | 1.085 ± 0.082 | 1.109 | 373527, 373528 |
| 1.0200 | 0.33212 ± 0.00041 | 0.33252 ± 0.00036 | 1.114 ± 0.114 | 1.022 ± 0.047 | 1.114 | 373552, 373553 |

### K5 — Z4, L = 12, mixed start, 2000 sweeps, band E\*_hc ± 0.01
| β | E at start | E_end (mean of readings 1550–2000) | E final | outcome | seed |
|---|---|---|---|---|---|
| 1.0020 | 0.54263 | 0.40744 | 0.40802 | strong | 405050 |
| 1.0070 | 0.54170 | 0.39460 | 0.39949 | strong | 405100 |
| 1.0120 | 0.54158 | 0.34197 | 0.34801 | weak | 405150 |
| 1.0170 | 0.54096 | 0.33470 | 0.33174 | weak | 405200 |
| 1.0220 | 0.54109 | 0.33045 | 0.33364 | weak | 405250 |

### Stage 1 — locate, void L = 2, L_t = 6, 500 + 2000 sweeps (β₀ ± 0.08 shown; every point in Appendix A)
| β | E hot | E cold | C hot | C cold | C_max |
|---|---|---|---|---|---|
| 1.14 | 0.42921 | 0.42941 | 0.645 | 0.646 | 0.646 |
| 1.15 | 0.42236 | 0.42372 | 0.662 | 0.665 | 0.665 |
| 1.16 | 0.41434 | 0.41566 | 0.725 | 0.728 | 0.728 |
| 1.17 | 0.40742 | 0.40687 | 0.688 | 0.729 | 0.729 |
| 1.18 | 0.40028 | 0.40205 | 0.802 | 0.694 | 0.802 |
| 1.19 | 0.39135 | 0.38919 | 0.906 | 0.959 | 0.959 |
| 1.20 | 0.37827 | 0.37507 | 1.131 | 1.749 | 1.749 |
| 1.21 | 0.37036 | 0.37004 | 1.156 | 1.417 | 1.417 |
| **1.22** | 0.35242 | 0.34590 | 1.898 | 2.180 | 2.180 |
| 1.23 | 0.32396 | 0.33346 | 1.454 | 1.853 | 1.853 |
| 1.24 | 0.31318 | 0.31339 | 1.214 | 1.371 | 1.371 |
| 1.25 | 0.30373 | 0.30579 | 0.920 | 1.180 | 1.180 |
| 1.26 | 0.29459 | 0.29446 | 0.566 | 0.571 | 0.571 |
| 1.27 | 0.28957 | 0.29048 | 0.507 | 0.571 | 0.571 |
| 1.28 | 0.28446 | 0.28499 | 0.459 | 0.503 | 0.503 |
| 1.29 | 0.27946 | 0.27946 | 0.421 | 0.424 | 0.424 |
| 1.30 | 0.27536 | 0.27590 | 0.369 | 0.460 | 0.460 |

### Stage 2 — fine scan, void L = 4, L_t = 12, 2000 + 4000 sweeps
| β | E hot | E cold | C hot | C cold | C_max | seeds (hot, cold) |
|---|---|---|---|---|---|---|
| 1.170 | 0.40810 ± 0.00011 | 0.40852 ± 0.00015 | 0.683 ± 0.027 | 0.757 ± 0.027 | 0.757 | 743376, 743377 |
| 1.175 | 0.40512 ± 0.00019 | 0.40475 ± 0.00023 | 0.695 ± 0.026 | 0.751 ± 0.037 | 0.751 | 743426, 743427 |
| 1.180 | 0.40125 ± 0.00017 | 0.40105 ± 0.00020 | 0.707 ± 0.025 | 0.767 ± 0.035 | 0.767 | 743476, 743477 |
| 1.185 | 0.39749 ± 0.00018 | 0.39723 ± 0.00019 | 0.820 ± 0.031 | 0.728 ± 0.035 | 0.820 | 743526, 743527 |
| 1.190 | 0.39367 ± 0.00022 | 0.39359 ± 0.00022 | 0.780 ± 0.037 | 0.756 ± 0.030 | 0.780 | 743576, 743577 |
| 1.195 | 0.38948 ± 0.00019 | 0.38975 ± 0.00030 | 0.733 ± 0.029 | 0.832 ± 0.036 | 0.832 | 743626, 743627 |
| 1.200 | 0.38512 ± 0.00021 | 0.38551 ± 0.00021 | 0.864 ± 0.050 | 0.746 ± 0.029 | 0.864 | 743676, 743677 |
| 1.205 | 0.38112 ± 0.00033 | 0.38085 ± 0.00019 | 0.898 ± 0.064 | 0.821 ± 0.044 | 0.898 | 743726, 743727 |
| 1.210 | 0.37714 ± 0.00024 | 0.37751 ± 0.00022 | 0.808 ± 0.045 | 0.759 ± 0.040 | 0.808 | 743776, 743777 |
| 1.215 | 0.37282 ± 0.00028 | 0.37234 ± 0.00031 | 0.926 ± 0.061 | 0.863 ± 0.056 | 0.926 | 743826, 743827 |
| 1.220 | 0.36759 ± 0.00037 | 0.36806 ± 0.00030 | 0.916 ± 0.064 | 0.973 ± 0.049 | 0.973 | 743876, 743877 |
| 1.225 | 0.36327 ± 0.00029 | 0.36275 ± 0.00025 | 0.976 ± 0.076 | 0.846 ± 0.038 | 0.976 | 743926, 743927 |
| 1.230 | 0.35743 ± 0.00047 | 0.35801 ± 0.00042 | 1.148 ± 0.081 | 1.150 ± 0.105 | 1.150 | 743976, 743977 |
| 1.235 | 0.35269 ± 0.00045 | 0.35260 ± 0.00047 | 1.032 ± 0.064 | 1.184 ± 0.083 | 1.184 | 744026, 744027 |
| 1.240 | 0.34678 ± 0.00039 | 0.34599 ± 0.00038 | 1.213 ± 0.076 | 1.221 ± 0.113 | 1.221 | 744076, 744077 |
| 1.245 | 0.33876 ± 0.00050 | 0.34060 ± 0.00059 | 1.197 ± 0.082 | 1.346 ± 0.147 | 1.346 | 744126, 744127 |
| 1.250 | 0.33303 ± 0.00057 | 0.33272 ± 0.00085 | 1.454 ± 0.120 | 1.665 ± 0.198 | 1.665 | 744176, 744177 |
| **1.255** | 0.30886 ± 0.00158 | 0.31606 ± 0.00238 | 2.913 ± 0.726 | 5.703 ± 0.542 | 5.703 | 744226, 744227 |
| 1.260 | 0.29956 ± 0.00025 | 0.30047 ± 0.00045 | 0.719 ± 0.036 | 0.922 ± 0.066 | 0.922 | 744276, 744277 |
| 1.265 | 0.29611 ± 0.00026 | 0.29651 ± 0.00028 | 0.719 ± 0.040 | 0.690 ± 0.042 | 0.719 | 744326, 744327 |
| 1.270 | 0.29253 ± 0.00022 | 0.29270 ± 0.00019 | 0.592 ± 0.026 | 0.631 ± 0.027 | 0.631 | 744376, 744377 |

### Stage 3 — scan, void L = 6, L_t = 18, hot and cold (C2), 500 + 1500 sweeps
| β | E hot | E cold | C hot | C cold | C_max | seeds (hot, cold) |
|---|---|---|---|---|---|---|
| 1.225 | 0.36281 ± 0.00021 | 0.36330 ± 0.00024 | 0.988 ± 0.077 | 1.117 ± 0.120 | 1.117 | 759764, 759765 |
| 1.230 | 0.35790 ± 0.00021 | 0.35801 ± 0.00028 | 0.863 ± 0.070 | 1.040 ± 0.104 | 1.040 | 759814, 759815 |
| 1.235 | 0.35161 ± 0.00026 | 0.35228 ± 0.00036 | 1.022 ± 0.119 | 1.371 ± 0.185 | 1.371 | 759864, 759865 |
| 1.240 | 0.34694 ± 0.00024 | 0.34693 ± 0.00028 | 0.955 ± 0.091 | 1.106 ± 0.111 | 1.106 | 759914, 759915 |
| 1.245 | 0.33960 ± 0.00039 | 0.34030 ± 0.00028 | 1.451 ± 0.151 | 1.109 ± 0.122 | 1.451 | 759964, 759965 |
| **1.250** | 0.33273 ± 0.00029 | 0.33037 ± 0.00074 | 1.079 ± 0.108 | 3.024 ± 0.675 | 3.024 | 760014, 760015 |
| **1.255** | 0.32076 ± 0.00040 | 0.31372 ± 0.00146 | 1.358 ± 0.199 | 9.528 ± 1.844 | 9.528 | 760064, 760065 |
| 1.260 | 0.31181 ± 0.00051 | 0.30124 ± 0.00029 | 1.751 ± 0.293 | 1.031 ± 0.128 | 1.751 | 760114, 760115 |
| 1.265 | 0.29860 ± 0.00067 | 0.29644 ± 0.00022 | 2.497 ± 0.504 | 0.854 ± 0.070 | 2.497 | 760164, 760165 |
| 1.270 | 0.29480 ± 0.00056 | 0.29320 ± 0.00021 | 1.784 ± 0.387 | 0.739 ± 0.088 | 1.784 | 760214, 760215 |
| 1.275 | 0.29109 ± 0.00034 | 0.28973 ± 0.00015 | 0.990 ± 0.187 | 0.597 ± 0.061 | 0.990 | 760264, 760265 |
| 1.280 | 0.28849 ± 0.00019 | 0.28713 ± 0.00010 | 0.625 ± 0.059 | 0.522 ± 0.036 | 0.625 | 760314, 760315 |
| 1.285 | 0.28465 ± 0.00015 | 0.28446 ± 0.00010 | 0.562 ± 0.047 | 0.490 ± 0.025 | 0.562 | 760364, 760365 |

### Stage 4 — mixed-phase starts, void L = 6, L_t = 18, 2000 sweeps
| β | E at start | E_end | S(β) | W(β) | f | primary (C1) | secondary (E\* ± 0.01) | seed |
|---|---|---|---|---|---|---|---|---|
| 1.2450 | 0.53162 | 0.34167 | 0.34008 | 0.31215 | -0.057 | strong | strong | 759966 |
| 1.2475 | 0.53183 | 0.33656 | 0.33710 | 0.31026 | 0.020 | strong | strong | 759991 |
| 1.2500 | 0.53144 | 0.33307 | 0.33412 | 0.30837 | 0.041 | strong | strong | 760016 |
| 1.2525 | 0.53264 | 0.33229 | 0.33114 | 0.30648 | -0.047 | strong | strong | 760041 |
| 1.2550 | 0.53183 | 0.32454 | 0.32816 | 0.30459 | 0.154 | strong | unresolved | 760066 |
| 1.2575 | 0.53291 | 0.31793 | 0.32518 | 0.30271 | 0.323 | strong | unresolved | 760091 |
| 1.2600 | 0.53011 | 0.30320 | 0.32221 | 0.30082 | 0.889 | weak | weak | 760116 |

Readings (E after sweeps 250, 500, …, 2000):

| β | readings |
|---|---|
| 1.2450 | 0.3416 0.3392 0.3374 0.3407 0.3391 0.3418 0.3441 0.3434 |
| 1.2475 | 0.3394 0.3357 0.3340 0.3358 0.3349 0.3360 0.3359 0.3356 |
| 1.2500 | 0.3301 0.3352 0.3346 0.3337 0.3317 0.3320 0.3295 0.3378 |
| 1.2525 | 0.3296 0.3273 0.3283 0.3314 0.3302 0.3244 0.3317 0.3310 |
| 1.2550 | 0.3234 0.3199 0.3189 0.3234 0.3266 0.3212 0.3242 0.3252 |
| 1.2575 | 0.3168 0.3119 0.3128 0.3153 0.3129 0.3138 0.3153 0.3180 |
| 1.2600 | 0.3072 0.3061 0.3084 0.3079 0.3024 0.3031 0.3025 0.3034 |

### Stage 4 — mixed-phase starts, void L = 8, L_t = 24, 2000 sweeps
| β | E at start | E_end | S(β) | W(β) | f | primary (C1) | secondary (E\* ± 0.01) | seed |
|---|---|---|---|---|---|---|---|---|
| 1.2537 [1.25375] | 0.52450 | 0.32575 | 0.32965 | 0.30554 | 0.162 | strong | unresolved | 775892 |
| 1.2563 [1.25625] | 0.52269 | 0.31920 | 0.32667 | 0.30365 | 0.324 | strong | unresolved | 775916 |
| 1.2588 [1.25875] | 0.52276 | 0.31039 | 0.32370 | 0.30176 | 0.607 | unresolved | weak | 775942 |
| 1.2612 [1.26125] | 0.52448 | 0.30681 | 0.32072 | 0.29987 | 0.667 | weak | weak | 775966 |
| 1.2637 [1.26375] | 0.52354 | 0.29733 | 0.31774 | 0.29798 | 1.033 | weak | weak | 775992 |

Readings (E after sweeps 250, 500, …, 2000):

| β | readings |
|---|---|
| 1.2537 [1.25375] | 0.3206 0.3237 0.3251 0.3245 0.3257 0.3245 0.3254 0.3240 |
| 1.2563 [1.25625] | 0.3155 0.3130 0.3202 0.3192 0.3195 0.3202 0.3168 0.3222 |
| 1.2588 [1.25875] | 0.3130 0.3082 0.3071 0.3089 0.3102 0.3131 0.3122 0.3105 |
| 1.2612 [1.26125] | 0.3118 0.3079 0.3059 0.3036 0.3068 0.3029 0.3065 0.3090 |
| 1.2637 [1.26375] | 0.3070 0.3052 0.3008 0.2993 0.2991 0.2979 0.2966 0.2981 |

### Stage 6 — histogram, void L = 6, β = 1.2588 [1.25875], mixed start, seed 760105, 2000 + 20,000 sweeps
B = 0.666541; ⟨E⟩ = 0.30261 ± 0.00045; peaks (bins) [18]; two peaks: False 

Counts (50 bins over [min E, max E] = [0.29287, 0.31694]):

`1 0 2 4 9 16 26 58 104 165 283 406 595 820 1011 1216 1402 1504 1555 1511 1498 1341 1173 1010 850 644 517 424 352 241 200 144 150 105 92 73 71 62 75 62 66 40 41 23 19 13 11 3 9 3`

### Stage decisions

| step | rule | result |
|---|---|---|
| 1 locate (L = 2) | largest C, larger of hot and cold | **β₀ = 1.22** (cold, C = 2.180); interior (0.72 and 0.78 from the edges); no extension |
| 2 fine scan (L = 4) | largest C | **β₄ = 1.255** (cold, C = 5.70); interior to [1.170, 1.270]; no extension |
| 2 jump interval L = 4 | largest fall in E | **hot [1.250, 1.255]** (fall 0.02416); **cold [1.250, 1.255]** (fall 0.01666) |
| 3 jump interval L = 6, cold | largest fall in E | **[1.250, 1.255]**, E 0.33037 → 0.31372, fall 0.01665 > 3σ = 0.00491 |
| 3 jump interval L = 6, hot | largest fall in E | **[1.260, 1.265]**, E 0.31181 → 0.29860, fall 0.01321 |
| 3 E\* | mean of cold E at β_lo, β_hi | **0.32205** (Q6 only) |
| 3 Located | β₄ interior and fall > 3σ | **yes** |
| 3 branch S (hot, 1.230–1.245) | least-squares line | **S(β) = 1.823294 − 1.191339 β**; points 0.35790, 0.35161, 0.34694, 0.33960; residuals ≤ 0.0009 |
| 3 branch W (cold, 1.260–1.275) | least-squares line | **W(β) = 1.252638 − 0.755413 β**; points 0.30124, 0.29644, 0.29320, 0.28973; residuals ≤ 0.0006 |
| 3 grid | branch points inside grid | yes; no extension |
| 4 L = 6 mixed | C1 | **β_mix(6) = 1.25875**, flip [1.2575, 1.2600], monotonic, 0 unresolved, no extension |
| 4 L = 8 mixed | C1 | **β_mix(8) = 1.25875**, flip [1.25625, 1.26125], monotonic, 1 unresolved (1.25875), no extension |
| 6 histogram | at β_mix(6) | β = 1.25875, B = 0.666541, one peak |

The gap S − W shrinks from 0.0279 at 1.245 to 0.0198 at 1.26375. It is never large compared with 0.02.
From 1.2525 upwards the strong branch itself lies less than 0.01 above E\*, so a pure strong-phase run there
is "unresolved" under the original card's ±0.01 band (Q6).

### Result (step 5)

| quantity | card convention (β) | continuum (1/e² = β/√2) |
|---|---|---|
| β₀ (L = 2) | 1.22 | 0.8627 |
| β₄ (L = 4, C max) | 1.255 | 0.8874 |
| jump interval L = 4 (hot and cold) | [1.250, 1.255] | [0.8839, 0.8874] |
| jump interval L = 6, cold / hot | [1.250, 1.255] / [1.260, 1.265] | [0.8839, 0.8874] / [0.8910, 0.8945] |
| β_mix(6) | 1.2588 [1.25875], interval [1.2575, 1.2600] | 0.8901 |
| β_mix(8) | 1.2588 [1.25875], interval [1.2563 [1.25625], 1.2612 [1.26125]] | 0.8901 |
| **β_∞ = β_mix(8)** | **1.2588 [1.25875] ± 0.0025** | **0.8901 ± 0.0018** |
| u | max(half L = 8 interval 0.0025, \|β_mix(8) − β_mix(6)\| 0) = **0.0025** | 0.0018 |
| ΔE(L = 8) | E_end(1.25625, strong) − E_end(1.26125, weak) = **0.01239** | — |
| check: line through (1/(L³L_t), β_mix(L)), L = 6, 8, at 0 | 1.25875 (β_mix did not move) | — |
| **Resolved** | L = 8 flip, 1 unresolved ≤ 1, u = 0.0025 ≤ 0.010 → **yes** | — |
| **β^R** | **1.25875** | — |

## 4. Hash before unblinding (REP1 §4.7)

`out/dlbr_numbers.txt` (every Q3 and Q6 number, written by `run/dlbr_numbers.py` from `out/state.json`):
**SHA-256 `dfafee6ca8f2cba4f7967990d500ea4daaab6c7595fe77bb48de37494c2d5646`**. It was written and hashed at
**02:13:53 AEDT, 13 Nov 2026** and posted to the conversation immediately, with the headline numbers,
before either sealed file was extracted. Extraction is logged at 02:14:06 (`as_run/REP1_RUN_LOG.md`). Both
sealed hashes matched §4.1 (`dlb_numbers.txt` 5f60f1d7…8aae; `gate_DLBETA_RESULT.md` 47cff87f…2c8a).

## 5. Q4 — order (step 7; reported, not a verdict input)

| diagnostic | finding | holds? |
|---|---|---|
| (a) hysteresis at L = 4 **or** L = 6 | L = 4: hot and cold jump intervals identical, largest \|E_h − E_c\| 2.52σ (1.255) → no. **L = 6: hot [1.260, 1.265] vs cold [1.250, 1.255]; 5 grid points beyond 3σ (1.255, 1.260, 1.265, 1.275, 1.280; largest 17.9σ at 1.260)** → yes | **yes** |
| (b) jump L = 4 (cold) → L = 6 (cold) → ΔE(8) | 0.01666 → 0.01665 → 0.01239 (−25.6 %); 0.7 × jump(4) = 0.01166 | does **not** shrink by > 30 % |
| (c) two peaks in the step-6 histogram (R7) | one peak (bin 18, E ≈ 0.3018); B = 0.666541 | **no** |

**Call: order undetermined.** First-order requires (a) and (c). (c) fails. The histogram run settled on the
weak branch, mean 0.30261 against W(1.25875) = 0.30176, with a tail towards higher E, and did not visit the
strong branch in 20,000 sweeps. ΔE(8) is taken between two part-mixed runs (f = 0.32 and 0.67). It is
therefore about half the branch gap at β_∞ (S − W = 0.0219), which pulls (b) down (§9.4).

## 6. Q5 — anisotropy record (recorded, not interpreted)

| where | E_s (rhombi) | E_t (temporal squares) | E_t/E_s |
|---|---|---|---|
| L = 6 hot scan, β = 1.255 (below β_∞) | 0.32968 ± 0.00042 | 0.31408 ± 0.00039 | 0.9527 |
| L = 6 cold scan, β = 1.255 (below β_∞; part-melted) | 0.32209 ± 0.00158 | 0.30744 ± 0.00137 | 0.9545 |
| L = 6 hot scan, β = 1.260 (above β_∞; part-mixed) | 0.32021 ± 0.00056 | 0.30551 ± 0.00048 | 0.9541 |
| L = 6 cold scan, β = 1.260 (above β_∞) | 0.30878 ± 0.00030 | 0.29558 ± 0.00028 | 0.9572 |
| L = 8 mixed, β = 1.25625 (strong win, below β_∞) | 0.32832 | 0.31237 | 0.9514 |
| L = 8 mixed, β = 1.26125 (weak win, above β_∞) | 0.31486 | 0.30078 | 0.9553 |
| β = 20 (K3; void L = 2, L_t = 6, cold) | 0.014655 ± 0.000007 | 0.014141 ± 0.000006 | 0.9649 |

On the L = 6 scan, E_t/E_s is 0.9488–0.9496 at 1.225–1.245 (both starts) and 0.9579–0.9599 at 1.265–1.285.
Every L = 6 point is in `out/post_obs.txt`.

## 7. Q6 — the original card's fixed-band rule on this run's mixed runs (reported, not a verdict input)

E\* = 0.32205: weak if E_end < 0.31205, strong if E_end > 0.33205.

| L | β | E_end | primary (C1) | secondary (band) |
|---|---|---|---|---|
| 6 | 1.2450 / 1.2475 / 1.2500 / 1.2525 | 0.34167 / 0.33656 / 0.33307 / 0.33229 | strong ×4 | strong ×4 |
| 6 | 1.2550 / 1.2575 | 0.32454 / 0.31793 | strong / strong | **unresolved / unresolved** |
| 6 | 1.2600 | 0.30320 | weak | weak |
| 8 | 1.25375 / 1.25625 | 0.32575 / 0.31920 | strong / strong | **unresolved / unresolved** |
| 8 | 1.25875 | 0.31039 | unresolved | **weak** |
| 8 | 1.26125 / 1.26375 | 0.30681 / 0.29733 | weak / weak | weak / weak |

- **β_mix_sec(6) = 1.25625**, interval [1.2525, 1.2600], 2 unresolved inside.
- **β_mix_sec(8): none** on the run's grid: no strong win, 2 unresolved, 3 weak. The secondary rule
  triggers no extensions (§4.4 step 4). Under the original card, the missing strong win would have
  triggered an extension below (CN-DLBR-04).
- **Code the original card's §5 would give: SC-DLB-2** (checks pass, located at L = 4 and 6, the L = 8 method
  does not resolve).

## 8. Q7 — comparison and verdict (after §4.7)

**I_O** (from `dlb_numbers.txt`: `beta_inf` 1.25375, `uncertainty` 0.00500) = **[1.24875, 1.25875]**.
**β^R = 1.25875**, which is I_O's upper end, so **d = 0**.

| code (applied in order) | condition | found | matches? |
|---|---|---|---|
| SC-DLBR-4 | desk-check geometry wrong | K1 agrees with the desk check | no |
| SC-DLBR-0 | a K2–K5 check failed | all pass | no |
| SC-DLBR-5 | no interior C max at L = 2, or not Located | β₀ interior; Located | no |
| **SC-DLBR-1** | Resolved and d ≤ 0.005; sealed material not seen early | Resolved (1 unresolved, u = 0.0025); d = 0; not seen | **yes** |

**Verdict: SC-DLBR-1 (replicated).**

**Also reported (§5):**
- **L = 6 cold jump interval:** this run [1.250, 1.255]; the original [1.250, 1.255]. **Equal.**
- **Does the Q6 rule reproduce the original's resolution status?** **Yes.** The original's verdict was
  SC-DLB-2 (located, not resolved; three of five L = 8 points unresolved under the band, assigned under its
  CN-DLB-01). This run's mixed runs give SC-DLB-2 under the same rule.
- **β_∞(REP1) − β_∞(original) = 1.25875 − 1.25375 = +0.0050.** That is one original uncertainty, or two of
  this run's.

## 9. Observations (after unblinding; not verdict inputs; CONJECTURE; `out/post_obs.txt`)

**9.1 How firm "Resolved" is.** σ_f comes from Monte Carlo propagation of three errors: σ(E_end), the sd of
the 10 readings / √10; and σ(S), σ(W), the 20-block errors of the eight branch points carried through the
two lines.

| L | β | f | σ_f | distance to nearest cut / σ_f | P(other side) |
|---|---|---|---|---|---|
| 6 | 1.2575 | 0.3228 | 0.040 | 0.26 | 0.40 |
| 8 | 1.25625 | 0.3244 | 0.037 | 0.24 | 0.41 |
| 8 | 1.25875 | 0.6068 | 0.022 | 2.7 | 0.003 |
| 8 | **1.26125** | **0.6670** | 0.024 | **0.014** | **0.49** |
| all others | — | — | 0.016–0.051 | ≥ 5.5 | 0.000 |

If 1.26125 had been unresolved: L = 8 flip [1.25625, 1.26375], β_mix(8) = 1.2600, u = 0.00375, 2 unresolved,
**not Resolved, d = 0.00125 → SC-DLBR-3**. The same holds if 1.25625 had been unresolved: flip
[1.25375, 1.26125], β_mix(8) = 1.2575, 2 unresolved. The SC-DLBR-1 verdict needed both coin-flip outcomes to
fall as they did. Neither the card nor the original had a rule for this, and none is applied here. The
L = 8 runs at 1.25875 and 1.26125 were still between branches after 2000 sweeps (readings in §3). With one
chain per β, the β_∞ uncertainty u = 0.0025 is the card's grid rule and carries no statistical part.

**9.2 Do the two codes simulate the same model?** Yes, to the precision of the scans.
z = (E_REP1 − E_orig)/√(σ² + σ²):
- L = 4, both starts, 34 comparisons away from 1.245–1.260: **rms 0.97, max 1.91**.
- L = 6 cold, 7 comparisons away from 1.250–1.255: **rms 0.93, max 2.08**.
- At the jump the runs are part-mixed and differ by more (L = 4: +4.1 at 1.250 hot, +4.4 at 1.255 cold;
  L = 6: −3.2 at 1.250). That is the expected scatter of runs that move between phases, not a model
  difference.
- The L = 6 mixed runs used the same grid in both codes. E_end agrees to within 0.002 at 6 of 7 points;
  at 1.2525 the two differ by 0.005.
- β₀ agrees (1.22). β₄ differs by one step (1.255 here, 1.250 there). Both are C maxima at the two ends
  of the same part-mixed jump step.
- The step-6 histograms give B = 0.666541 here and 0.666537 there, each with one peak.

**9.3 Where the +0.005 comes from.** The two codes' mixed-run energies are close. The difference in β_∞ is
mostly the outcome rule and the grid placement. Applying this run's C1 lines to the original's own L = 8
E_end values gives f = −0.01, 0.12, 0.18, 0.27, 0.78 at 1.24875 … 1.25875: a flip between 1.25625 (strong)
and 1.25875 (weak), midpoint 1.2575, with no unresolved point. Pooling both codes' L = 8 runs, every run
at ≤ 1.25625 is a strong win, and the weak side begins at 1.25875–1.26125. From about 1.2525 upwards the
strong branch lies less than 0.01 above E\*, for either code's E\* (0.32205 here, 0.32411 there). The original
card's band rule therefore cannot call the strong side in this window. That is the defect C1 was written
for, and it is what produced the original's three unresolved points. This paragraph is a
cross-application the card says cannot be made pre-run (§3). It is an observation only.

**9.4 ΔE(8) and the order call.** The two runs that define ΔE(8) have f = 0.32 and 0.67, so neither is a
pure phase. At β_∞ the branch gap S − W is 0.0219, about 1.8 × ΔE(8). Q4(b) is computed as the card
defines it.

**9.5 Hysteresis at L = 6** (new; the original ran no hot L = 6 scan). Hot starts at 1.255–1.280 sit above
their cold partners, by more than 3σ at five of the six points (largest 17.9σ, at 1.260). Hot starts stay
partly in the strong phase one grid step further than cold starts.
This is the metastability a first-order transition shows. The step-6 histogram, which settled into the
weak phase, has no second peak, so the order call stays "undetermined".

## 10. Analyst's disclosure (REP1 §8), scored

The card's author had run Gate DL-BETA. Each forecast is scored against this run's outcome.

| forecast | outcome | score |
|---|---|---|
| Checks K1–K5 pass: 92 % | all pass | **hit** |
| Verdict: SC-DLBR-1 60 %; -3 27 %; -2 6 %; -0 5 %; -4/-5 2 % | SC-DLBR-1 | the modal bin (60 %) |
| β^R inside I_O (d = 0): 75 % | d = 0 (on I_O's upper end) | **hit** |
| Resolved under the primary rule: 70 % | yes (by a margin far below its error, §9.1) | **hit** |

All four forecasts land on the outcome they favoured. §9.1 suggests that SC-DLBR-1 and SC-DLBR-3 were
closer to even than 60 : 27, given this run's raw data. That is hindsight on one run, not a scoring rule.

## 11. Correction notices

- **CN-DLBR-01 (disclosure: an earlier attempt's files).** This run's working directory already held two
  checkpoint files and two directories from an earlier, interrupted attempt (§0). They were neither opened
  nor listed, and everything was re-fetched into fresh directories. No sealed material was seen. No effect on
  any number.
- **CN-DLBR-02 (report scripts after the driver finished).** `run/dlbr_numbers.py` was written while the void
  stages ran. One edit was made after the driver finished and before `dlbr_numbers.txt` was first written:
  f is printed to 6 decimals instead of 4, because two values sat within 0.001 of a cut. `run/dlbr_post.py`
  was written after unblinding. Neither script changes a stage decision, which the frozen driver had already
  made and recorded in `out/state.json`.
- **CN-DLBR-03 (readings).** RD1–RD12 (§1) were fixed in code before the first run. Four were never exercised.
  None of them decided a verdict input.
- **CN-DLBR-04 (Q6 and extensions).** By REP1 §4.4, the secondary rule triggers no extensions, so on this
  run's L = 8 grid it has no strong win and no flip. The original card's own procedure would have added up to
  eight steps below. Q6's code (SC-DLB-2) is computed on the fixed grids, as the card says.

## 12. Tier movements (as REP1 §5 fixes them)

| # | statement | tier |
|---|---|---|
| 1 | Transition of compact U(1), Wilson, void network × time (β_t = β_s), located at L = 4 and 6 in [1.250, 1.255] | **REPLICATED** (two codes, two threads), from CONJECTURE |
| 2 | Quoted value β_c = β_∞ = 1.2588 [1.25875] ± 0.0025; 1/e²_c = 0.8901 ± 0.0018 | **Quoted value**, single-code figure, **CONJECTURE**; "Resolved" is fragile (§9.1) |
| 3 | Gate DL-BETA's β_∞ = 1.25375 ± 0.0050 | Contains this run's β^R (d = 0, on its edge); not contested |
| 4 | Order of the transition | Undetermined in both runs; L = 6 hysteresis observed (OBSERVATION) |

## 13. Limits

- Those of both cards: Wilson action only; β_t = β_s only; one spatial complex; bare couplings; a lattice β_c
  with a tree-level k.
- Two mixed-phase sizes and one chain per β. The quoted u is the card's grid rule, with no statistical part.
  §9.1 shows that, at L = 8, the outcomes next to the flip are statistically undetermined at 2000 sweeps.
- C1's branch lines are extrapolated by up to 0.019 in β from the nearest branch point (L = 8 at 1.26375 is
  0.019 above 1.245, the last S point). Curvature is not modelled. The S fit residuals are ≤ 0.0004.

## 14. Plain-language summary

Gate DL-BETA found the "tipping point" of electromagnetism simulated on the network of gaps between packed
spheres, with time added: below a certain coupling the field is confined, above it light travels freely. That
gate used one program, in one conversation, so its number stood only as a conjecture.

This gate wrote a second program from the written recipe alone, without seeing the first program or its
answer. It passed the same five tests, including the ordinary cubic lattice, where the answer is known (it
found 1.0075 on a small box and 1.007–1.012 with the two-phase method; the literature value is 1.0111). On
the sphere-gap network it then found the tipping point **in exactly the same grid step as the original,
between 1.250 and 1.255, on two box sizes and from both starting conditions**. Its energies agree with the
original's point by point to within ordinary statistical scatter. Only after its own numbers were written
down and fingerprinted was the sealed original opened.

The refined "two-phase" estimate, which starts half the box in each phase, gives **1.2588 ± 0.0025** here.
The original gave 1.2538 ± 0.0050. The two agree: the new value sits exactly on the edge of the old one's
error bar. That agreement is what the card counts as a replication.

A caution. The rule that decides whether the two-phase method has "resolved" the answer depends here on two
runs that landed right on their decision lines, one of them by a hair. Had either landed the other way, the
card's verdict would have been "inconclusive" rather than "replicated", with almost the same number. The
location is solid, at about 1.25–1.26 in the card's units (1/e² ≈ 0.89). The last digit and its error bar are
softer than the verdict code alone suggests.

## 15. Files

Everything below `audit/gates/DLBETA_REP1/` is listed with SHA-256 in `MANIFEST.sha256`. Key files:

| file | SHA-256 |
|---|---|
| `run/dlbr_sim.py` | `560c256fe391bfa7b0a2bf4e5abc520f8179b75647ece51006b5cba82425c9e6` |
| `run/dlbr_stats.py` | `2ded89b33779c3c612dbdfcbcb350fdc30584985dbc6eae251b1ae78eb7e0d45` |
| `run/dlbr_driver.py` | `37a9ecfb94e1d341db96bbb6d40124c161a39c517eb08e43986cdfbd1aa6c957` |
| `run/dlbr_k1.py` | `7f24667b48fb0aae0fcb40c4f4853afe4d70a752ecac7ee39bde1d7bef6a29ad` |
| `run/dlbr_k23.py` | `a3dff1d8752b8edd58d2211178f984aed4db5bbbd176c58e02f0ab7111d4bd5b` |
| `run/dlbr_numbers.py` | `d56460b2b29366f09459cfabb9a9d6b54e3738be6838a042de27eb4ade18dd37` |
| `run/dlbr_tables.py` | `d1ab456814cd78de28fde8d009726552138d2cf1d5ef52bacef0fc1c9a2032f5` |
| `run/dlbr_post.py` | `d00e6ba45b70d017f75aa4f83fe0c418605e4217ff5ad457f084c8267c46b2ed` |
| `out/dlbr_numbers.txt` | `dfafee6ca8f2cba4f7967990d500ea4daaab6c7595fe77bb48de37494c2d5646` |
| `out/state.json` | `56f2bb18f3c918278ed6ffbf27e9e2b9fbb131cd8a4546050aadc19186532f9a` |
| `out/raw_records.jsonl` | `7fa034deb197d2c1e4725d263875ccb7f802cd4e4ef9abe2ffd1bf24920efa4e` |
| `out/k1_own.txt` | `469b6ff85c1a6a0ce5c3add9955c7af6167caae7e984619581e6e91c1cc820cd` |
| `out/k23.txt` | `ffd2629bf250c98ad2ef7195fb94386f5613e2cc8048255457f6c2979bf4a757` |
| `out/post_obs.txt` | `f3b6e6ed0e8f7cd45e28d62f4a9e5bd41a21b5dfb135e63efaf13447752c6544` |
| `out/driver_log.txt` | `766ef0298a33b27305060614cb662040cc3332df71e7147faf4857a4a6551994` |
| `out/deskcheck_rerun_output.txt` | `c27bcbb75c64bdeb55e57948debd9814a43e6f63e9c27091cc62c05ae2accba3` |
| `as_run/gate_DLBETA_REP1_prompt.md` | `2ffa8de365a01af1cd3e372998d264d16c2327459e2ffbb5b126f08e7f39a349` |
| `as_run/run_prompt.txt` | `b085cf67b9d7ab2dc39b5717e013cffca27e21078e8e1dc2ff88cba4a81d8e31` |
| `as_run/REP1_RUN_LOG.md` | `c4364715662785747c462a8a4f838bdcce27e9da500dc1d8ed8e6dd0db4bf80b` |

Raw series: `out/series/*.npz` (410 gate runs and 4 K3 runs; float64 E, E_s, E_t after every sweep, row 0
= initial state; each carries its seed). Per-run records with seeds and the hash of each series file:
`out/raw_records.jsonl`. As-run copies: `as_run/gate_DLBETA_REP1_prompt.md` (the card as fetched),
`as_run/run_prompt.txt` (the run prompt), `as_run/REP1_RUN_LOG.md` (timestamped log).

## Appendix A — locate scan (L = 2, L_t = 6), every grid point

| β | E hot | E cold | C hot | C cold | C_max |
|---|---|---|---|---|---|
| 0.50 | 0.75576 | 0.75505 | 0.463 | 0.454 | 0.463 |
| 0.51 | 0.74982 | 0.75065 | 0.475 | 0.487 | 0.487 |
| 0.52 | 0.74558 | 0.74595 | 0.474 | 0.460 | 0.474 |
| 0.53 | 0.74147 | 0.74153 | 0.511 | 0.471 | 0.511 |
| 0.54 | 0.73644 | 0.73685 | 0.494 | 0.460 | 0.494 |
| 0.55 | 0.73208 | 0.73151 | 0.487 | 0.470 | 0.487 |
| 0.56 | 0.72720 | 0.72775 | 0.483 | 0.457 | 0.483 |
| 0.57 | 0.72277 | 0.72172 | 0.483 | 0.476 | 0.483 |
| 0.58 | 0.71735 | 0.71793 | 0.457 | 0.503 | 0.503 |
| 0.59 | 0.71239 | 0.71333 | 0.490 | 0.475 | 0.490 |
| 0.60 | 0.70850 | 0.70825 | 0.481 | 0.498 | 0.498 |
| 0.61 | 0.70293 | 0.70328 | 0.508 | 0.477 | 0.508 |
| 0.62 | 0.69864 | 0.69941 | 0.454 | 0.447 | 0.454 |
| 0.63 | 0.69354 | 0.69387 | 0.450 | 0.452 | 0.452 |
| 0.64 | 0.68890 | 0.68852 | 0.488 | 0.463 | 0.488 |
| 0.65 | 0.68449 | 0.68460 | 0.470 | 0.465 | 0.470 |
| 0.66 | 0.67969 | 0.67958 | 0.469 | 0.475 | 0.475 |
| 0.67 | 0.67469 | 0.67478 | 0.493 | 0.494 | 0.494 |
| 0.68 | 0.67038 | 0.66992 | 0.473 | 0.500 | 0.500 |
| 0.69 | 0.66503 | 0.66522 | 0.484 | 0.492 | 0.492 |
| 0.70 | 0.66065 | 0.66003 | 0.478 | 0.487 | 0.487 |
| 0.71 | 0.65560 | 0.65575 | 0.494 | 0.494 | 0.494 |
| 0.72 | 0.65126 | 0.65071 | 0.502 | 0.470 | 0.502 |
| 0.73 | 0.64636 | 0.64540 | 0.514 | 0.484 | 0.514 |
| 0.74 | 0.64119 | 0.64106 | 0.463 | 0.469 | 0.469 |
| 0.75 | 0.63652 | 0.63754 | 0.495 | 0.465 | 0.495 |
| 0.76 | 0.63206 | 0.63139 | 0.508 | 0.485 | 0.508 |
| 0.77 | 0.62698 | 0.62766 | 0.492 | 0.487 | 0.492 |
| 0.78 | 0.62264 | 0.62233 | 0.508 | 0.492 | 0.508 |
| 0.79 | 0.61772 | 0.61743 | 0.470 | 0.490 | 0.490 |
| 0.80 | 0.61223 | 0.61198 | 0.472 | 0.457 | 0.472 |
| 0.81 | 0.60736 | 0.60734 | 0.456 | 0.511 | 0.511 |
| 0.82 | 0.60221 | 0.60251 | 0.465 | 0.486 | 0.486 |
| 0.83 | 0.59780 | 0.59813 | 0.490 | 0.487 | 0.490 |
| 0.84 | 0.59232 | 0.59250 | 0.504 | 0.477 | 0.504 |
| 0.85 | 0.58762 | 0.58768 | 0.478 | 0.502 | 0.502 |
| 0.86 | 0.58182 | 0.58303 | 0.478 | 0.499 | 0.499 |
| 0.87 | 0.57790 | 0.57815 | 0.506 | 0.495 | 0.506 |
| 0.88 | 0.57324 | 0.57338 | 0.516 | 0.470 | 0.516 |
| 0.89 | 0.56722 | 0.56827 | 0.510 | 0.491 | 0.510 |
| 0.90 | 0.56319 | 0.56318 | 0.505 | 0.493 | 0.505 |
| 0.91 | 0.55757 | 0.55753 | 0.508 | 0.519 | 0.519 |
| 0.92 | 0.55374 | 0.55252 | 0.522 | 0.492 | 0.522 |
| 0.93 | 0.54818 | 0.54740 | 0.494 | 0.546 | 0.546 |
| 0.94 | 0.54194 | 0.54217 | 0.521 | 0.534 | 0.534 |
| 0.95 | 0.53709 | 0.53718 | 0.545 | 0.545 | 0.545 |
| 0.96 | 0.53095 | 0.53122 | 0.552 | 0.535 | 0.552 |
| 0.97 | 0.52577 | 0.52657 | 0.503 | 0.526 | 0.526 |
| 0.98 | 0.52231 | 0.52150 | 0.530 | 0.501 | 0.530 |
| 0.99 | 0.51590 | 0.51493 | 0.517 | 0.538 | 0.538 |
| 1.00 | 0.51002 | 0.51006 | 0.519 | 0.511 | 0.519 |
| 1.01 | 0.50554 | 0.50519 | 0.529 | 0.518 | 0.529 |
| 1.02 | 0.50038 | 0.49964 | 0.491 | 0.535 | 0.535 |
| 1.03 | 0.49513 | 0.49385 | 0.555 | 0.528 | 0.555 |
| 1.04 | 0.48874 | 0.48785 | 0.559 | 0.522 | 0.559 |
| 1.05 | 0.48253 | 0.48234 | 0.541 | 0.589 | 0.589 |
| 1.06 | 0.47748 | 0.47742 | 0.573 | 0.562 | 0.573 |
| 1.07 | 0.47141 | 0.47146 | 0.611 | 0.572 | 0.611 |
| 1.08 | 0.46712 | 0.46565 | 0.595 | 0.579 | 0.595 |
| 1.09 | 0.46210 | 0.45997 | 0.557 | 0.609 | 0.609 |
| 1.10 | 0.45334 | 0.45531 | 0.620 | 0.578 | 0.620 |
| 1.11 | 0.44834 | 0.44740 | 0.628 | 0.623 | 0.628 |
| 1.12 | 0.44373 | 0.44094 | 0.619 | 0.581 | 0.619 |
| 1.13 | 0.43614 | 0.43610 | 0.636 | 0.633 | 0.636 |
| 1.14 | 0.42921 | 0.42941 | 0.645 | 0.646 | 0.646 |
| 1.15 | 0.42236 | 0.42372 | 0.662 | 0.665 | 0.665 |
| 1.16 | 0.41434 | 0.41566 | 0.725 | 0.728 | 0.728 |
| 1.17 | 0.40742 | 0.40687 | 0.688 | 0.729 | 0.729 |
| 1.18 | 0.40028 | 0.40205 | 0.802 | 0.694 | 0.802 |
| 1.19 | 0.39135 | 0.38919 | 0.906 | 0.959 | 0.959 |
| 1.20 | 0.37827 | 0.37507 | 1.131 | 1.749 | 1.749 |
| 1.21 | 0.37036 | 0.37004 | 1.156 | 1.417 | 1.417 |
| 1.22 | 0.35242 | 0.34590 | 1.898 | 2.180 | 2.180 |
| 1.23 | 0.32396 | 0.33346 | 1.454 | 1.853 | 1.853 |
| 1.24 | 0.31318 | 0.31339 | 1.214 | 1.371 | 1.371 |
| 1.25 | 0.30373 | 0.30579 | 0.920 | 1.180 | 1.180 |
| 1.26 | 0.29459 | 0.29446 | 0.566 | 0.571 | 0.571 |
| 1.27 | 0.28957 | 0.29048 | 0.507 | 0.571 | 0.571 |
| 1.28 | 0.28446 | 0.28499 | 0.459 | 0.503 | 0.503 |
| 1.29 | 0.27946 | 0.27946 | 0.421 | 0.424 | 0.424 |
| 1.30 | 0.27536 | 0.27590 | 0.369 | 0.460 | 0.460 |
| 1.31 | 0.27218 | 0.27217 | 0.375 | 0.378 | 0.378 |
| 1.32 | 0.26822 | 0.26849 | 0.345 | 0.348 | 0.348 |
| 1.33 | 0.26631 | 0.26525 | 0.391 | 0.377 | 0.391 |
| 1.34 | 0.26140 | 0.26220 | 0.333 | 0.312 | 0.333 |
| 1.35 | 0.25817 | 0.25914 | 0.305 | 0.318 | 0.318 |
| 1.36 | 0.25522 | 0.25586 | 0.297 | 0.295 | 0.297 |
| 1.37 | 0.25242 | 0.25325 | 0.291 | 0.305 | 0.305 |
| 1.38 | 0.24946 | 0.24880 | 0.271 | 0.280 | 0.280 |
| 1.39 | 0.24678 | 0.24709 | 0.265 | 0.289 | 0.289 |
| 1.40 | 0.24444 | 0.24421 | 0.269 | 0.262 | 0.269 |
| 1.41 | 0.24132 | 0.24161 | 0.244 | 0.249 | 0.249 |
| 1.42 | 0.24728 | 0.23912 | 0.282 | 0.242 | 0.282 |
| 1.43 | 0.23676 | 0.23736 | 0.217 | 0.230 | 0.230 |
| 1.44 | 0.23476 | 0.23452 | 0.216 | 0.235 | 0.235 |
| 1.45 | 0.23251 | 0.23244 | 0.219 | 0.217 | 0.219 |
| 1.46 | 0.23029 | 0.23042 | 0.211 | 0.207 | 0.211 |
| 1.47 | 0.23469 | 0.22800 | 0.224 | 0.216 | 0.224 |
| 1.48 | 0.22607 | 0.22608 | 0.192 | 0.195 | 0.195 |
| 1.49 | 0.22398 | 0.22359 | 0.200 | 0.209 | 0.209 |
| 1.50 | 0.22201 | 0.22217 | 0.209 | 0.189 | 0.209 |
| 1.51 | 0.21966 | 0.21975 | 0.193 | 0.191 | 0.193 |
| 1.52 | 0.21844 | 0.21813 | 0.181 | 0.188 | 0.188 |
| 1.53 | 0.22317 | 0.21592 | 0.193 | 0.174 | 0.193 |
| 1.54 | 0.21451 | 0.21460 | 0.182 | 0.176 | 0.182 |
| 1.55 | 0.21244 | 0.21223 | 0.164 | 0.179 | 0.179 |
| 1.56 | 0.21086 | 0.21127 | 0.176 | 0.172 | 0.176 |
| 1.57 | 0.20906 | 0.20897 | 0.175 | 0.177 | 0.177 |
| 1.58 | 0.21300 | 0.20778 | 0.177 | 0.164 | 0.177 |
| 1.59 | 0.21256 | 0.20573 | 0.172 | 0.150 | 0.172 |
| 1.60 | 0.20421 | 0.20423 | 0.160 | 0.155 | 0.160 |
| 1.61 | 0.20268 | 0.20252 | 0.159 | 0.155 | 0.159 |
| 1.62 | 0.20115 | 0.20111 | 0.152 | 0.155 | 0.155 |
| 1.63 | 0.19986 | 0.19938 | 0.154 | 0.149 | 0.154 |
| 1.64 | 0.20443 | 0.19788 | 0.158 | 0.147 | 0.158 |
| 1.65 | 0.20209 | 0.19675 | 0.145 | 0.137 | 0.145 |
| 1.66 | 0.19482 | 0.19488 | 0.144 | 0.143 | 0.144 |
| 1.67 | 0.19387 | 0.19382 | 0.137 | 0.137 | 0.137 |
| 1.68 | 0.19874 | 0.19212 | 0.143 | 0.136 | 0.143 |
| 1.69 | 0.19736 | 0.19080 | 0.140 | 0.132 | 0.140 |
| 1.70 | 0.18984 | 0.18916 | 0.137 | 0.138 | 0.138 |
| 1.71 | 0.18818 | 0.18820 | 0.134 | 0.128 | 0.134 |
| 1.72 | 0.18683 | 0.18656 | 0.129 | 0.130 | 0.130 |
| 1.73 | 0.18550 | 0.18556 | 0.128 | 0.132 | 0.132 |
| 1.74 | 0.18431 | 0.18438 | 0.124 | 0.126 | 0.126 |
| 1.75 | 0.18867 | 0.18276 | 0.130 | 0.110 | 0.130 |
| 1.76 | 0.18180 | 0.18152 | 0.119 | 0.124 | 0.124 |
| 1.77 | 0.18059 | 0.18069 | 0.124 | 0.117 | 0.124 |
| 1.78 | 0.19120 | 0.17961 | 0.125 | 0.121 | 0.125 |
| 1.79 | 0.17837 | 0.17810 | 0.119 | 0.121 | 0.121 |
| 1.80 | 0.17732 | 0.17721 | 0.119 | 0.121 | 0.121 |
| 1.81 | 0.18218 | 0.17585 | 0.120 | 0.114 | 0.120 |
| 1.82 | 0.17471 | 0.17479 | 0.119 | 0.112 | 0.119 |
| 1.83 | 0.17357 | 0.17366 | 0.111 | 0.114 | 0.114 |
| 1.84 | 0.17261 | 0.17249 | 0.112 | 0.109 | 0.112 |
| 1.85 | 0.17737 | 0.17133 | 0.109 | 0.109 | 0.109 |
| 1.86 | 0.17046 | 0.17066 | 0.101 | 0.103 | 0.103 |
| 1.87 | 0.16985 | 0.16939 | 0.098 | 0.109 | 0.109 |
| 1.88 | 0.17338 | 0.16809 | 0.106 | 0.102 | 0.106 |
| 1.89 | 0.16735 | 0.16709 | 0.100 | 0.108 | 0.108 |
| 1.90 | 0.17156 | 0.16641 | 0.100 | 0.096 | 0.100 |
| 1.91 | 0.16512 | 0.16549 | 0.102 | 0.100 | 0.102 |
| 1.92 | 0.16452 | 0.16428 | 0.099 | 0.101 | 0.101 |
| 1.93 | 0.16338 | 0.16349 | 0.098 | 0.092 | 0.098 |
| 1.94 | 0.16757 | 0.16221 | 0.098 | 0.096 | 0.098 |
| 1.95 | 0.16113 | 0.16139 | 0.095 | 0.095 | 0.095 |
| 1.96 | 0.16611 | 0.16062 | 0.094 | 0.092 | 0.094 |
| 1.97 | 0.16494 | 0.15966 | 0.090 | 0.093 | 0.093 |
| 1.98 | 0.16368 | 0.15866 | 0.086 | 0.091 | 0.091 |
| 1.99 | 0.16889 | 0.15762 | 0.090 | 0.086 | 0.090 |
| 2.00 | 0.15642 | 0.15654 | 0.086 | 0.095 | 0.095 |
