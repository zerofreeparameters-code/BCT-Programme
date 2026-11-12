# Gate DL-BETA — result

**Verdict: SC-DLB-2 (located, not resolved), assigned under CN-DLB-01.** Every check passes (K1–K5).
The transition of compact U(1) with the Wilson action on the FCC void network × time (β_t = β_s) is
located at L = 4 and L = 6 in the same grid step, **[1.250, 1.255]**. The card's step 5 gives
**β_∞ = β_mix(8) = 1.2538 ± 0.0050** (exactly 1.25375 ± 0.00500), i.e. **1/e²_c = β_∞/√2 = 0.8865 ± 0.0035**.
The L = 8 mixed-phase method flipped inside its grid with no extension, but three of its five points
are unresolved. The card allows at most one for SC-DLB-1. Under SC-DLB-2's rule, β_c is reported as
the L = 6 jump interval widened by the L = 4 → 6 shift (zero): **β_c ∈ [1.250, 1.255]**, so
**1/e²_c ∈ [0.8839, 0.8874]**.
**Status:** CONJECTURE (same-session cap, card §8), until a blind replication.
**What the number decides (card §5):** with the DL construction's coupling β, the photon is massless
iff β > β_c ≈ 1.25 (card convention), i.e. 1/e² > ≈ 0.89. This is CN-DL-06 with a number in it.
**Order:** "order undetermined" by card §4.4 step 7. **Placement:** β_∞ is above Z4 (×1.240) and D4
(×2.039) in the card convention, and in the continuum normalisation it is *below* both
(0.877 × Z4's 1/e²_c). All three of the card's heuristics miss, and so does the scoping note's
forecast (§8).
**Run:** 12 November 2026, 18:07–20:20 AEDT, one fresh thread inside the BCT Project. Analyst: Claude
(Opus 5.5). Simulation 18:21–20:06, 199 core-minutes on 2 cores.

---

## 0. Provenance

**Card.** `audit/gates/gate_DLBETA_prompt.md` at commit `bf7d97a11742ddfe086b78ad800fe9a0083f9859`.
Fetched by commit-pinned raw URL with `curl` to disk together with `PREREG_20261112_DLBETA.sha256`
and `DLBETA/dlb_deskcheck_output.txt`, and all three hashed **before the card was read**:

| file | SHA-256 | vs run prompt |
|---|---|---|
| `gate_DLBETA_prompt.md` | `eae34f3becfa4c8ce798eb01f307c7560e1d1301bfb4f2e3e70d11d5c73c9024` | match |
| `PREREG_20261112_DLBETA.sha256` | `941aaf107274510af9eb395935b6efd102ed7f8cccdfa9fac3c85edb4b27eca7` | match |
| `dlb_deskcheck_output.txt` | `10d58dbbb45d3c118880d1f437c38166f946e66772152d613011fe765fc150ae` | match |

The PREREG record lists the card, `dlb_deskcheck.py` and its output; the card's digest matches it.

**Sources (card §4.1).** The repository was fetched as a single commit (`git fetch --depth 1 origin
bf7d97a…`). All nine §4.1 hashes, plus the card and PREREG at their repository paths, were verified
with `sha256sum -c` **before any source was read**: 11/11 OK. Read: the CRIT2 card, CRIT2 result,
LATT card, DL result, DL step-0 script, scoping note (in full), and **DL-STIFF card lines 20–48 only
(its §1)**; headers were located by `grep '^#'` first. `dlb_deskcheck_output.txt` was read at the
start, as §4.3 permits. **`dlb_deskcheck.py` was not opened until the run's own K1 numbers were
recorded and hashed** (18:14:53 AEDT; `out/k1_recorded_at.txt`). Nothing under `audit/gates/DLSTIFF/`,
no other repository file, nothing from the Project knowledge base, past chats or memory (memory is
not enabled on this account) was read. The scoping note's §7 contains a *forecast* about DL-STIFF's
outcome; it is a forecast, not a result, and nothing here uses it.

**Literature:** Arnold et al., hep-lat/0210010, used only as the card quotes it (β_c = 1.0111331(21)).

**Environment.** Python 3.13.18, NumPy 2.5.3, SciPy 1.18.1, numba 0.68.1 (installed for this run, as
the card allows). 2 CPU cores, one simulation per core. Full timeline: `out/provenance_log.txt`.

**One pre-run stop.** The driver's first launch (18:20) stopped at its own guard assertion before K2:
a mistyped constant for I₁(0.1)/I₀(0.1). No simulation had run. The constant was replaced by SciPy's
value (0.04993760398793892), the code was re-frozen (`out/code_frozen_before_runs.sha256`, 18:21:50)
and the driver relaunched at 18:21:51. The code was not changed again during the runs.

## 1. The code (written in this thread from card §4.2)

`run/dlb_complex.py` builds the complexes, `run/dlb_k1.py` runs K1, and `run/dlb_sim.py` holds the
simulator. `run/dlb_driver.py` applies §4.3–4.4 mechanically, stage by stage, reading each stage's
numbers from the previous one, and resumes from disk. `run/dlb_unit_tests.py` holds the unit tests.
`run/make_numbers.py` (§4.6), `run/q4q5.py`, `run/place.py` (§6, refuses to run before the §4.6 hash),
`run/post_obs.py` (post-hash observations), `run/gen_tables.py`, `run/consolidate.py` and
`run/assemble_result.py` (this file's tables) complete the set.

- **Complex.** As §4.2: integer coordinates in units of a/4, box 4L, atoms, octs at atom + (2,2,2),
  tets at atom + (1,1,1) and + (3,3,3). Spatial links run oct → tet at (±1,±1,±1). Rhombi come from
  the six bond vectors, in the order O₁ → T₁ → O₂ → T₂. There are L_t = 3L slices, a temporal link at
  every node, and a temporal square on every spatial link.
- **Storage and sweep order (fixed before the first run, in the module docstrings).** Void: by slice;
  within slice t the 8N spatial links (by oct cell, then offset (±1)³ in product order), then the 3N
  temporal links (oct, tet₁, tet₂ sublattices). Z4: by site, μ = 0…3.
- **Update.** Sequential single-link heat bath. With Z = Σ_{p∋l} e^{i s_{p,l} θ_p}, the conditional law
  is exp(β|Z| cos(θ_l + φ)) with φ = arg Z − θ_l. θ_l + φ is drawn exactly from von Mises(0, β|Z|)
  with the Best–Fisher algorithm, written in a cancellation-free form (b, 1 − b, r² − 1 and arccos f
  all without subtraction of near-equal numbers). No overrelaxation.
- **RNG and starts.** numba's generator, seeded inside the compiled code; the starting configuration
  is drawn from it. Hot: uniform [0, 2π). Cold: all zero. Mixed (void): every link whose origin node
  has t < L_t/2 is zero, all others uniform. Mixed (Z4, K5): origin site x₁ < L/2.
- **Observables after every sweep** (thermalisation included): E, E_s (rhombi; Z4 space–space), E_t
  (temporal squares; Z4 μ = 0). Statistics use the measurement sweeps: 20-block errors, C = N_loops ·
  var(E), and C errors by 20-block jackknife.
- **Seeds.** 7919·L + round(10⁴·β) + s (+500,000 on the void complex), with s = 0 hot, 1 cold, 2 mixed,
  3 histogram. Python's round(), half to even, as CRIT2 did. Every seed is in the raw records.

**Unit tests** (`out/unit_tests.txt`, before any card run):
- The von Mises sampler against the exact law at κ = 10⁻³ … 200, with 10⁶ draws × 2 seeds per κ:
  20 KS p-values from 0.150 to 0.913, and ⟨cos⟩ within 1.6σ of I₁/I₀ in every case.
- The local staple ΔS equals the global recompute to 1.3 × 10⁻¹².
- Timing matches the card's §4.5 to within 16 % at every size.

**Readings of the card's wording**, fixed in `dlb_driver.py`'s docstring (R1–R10) before the runs
they affect. The ones that matter here:
- **R3.** "The 10 readings at sweeps 1550–2000" are the readings after sweeps 1550, 1600, …, 2000.
  "End-state E" for ΔE is the same 10-reading mean; the final-sweep value is also given.
- **R6.** β_mix uses S = the highest strong-win β and W = the lowest weak-win β; the interval is
  [S, W]. Unresolved points between S and W lie inside the interval.
- **R7.** "Two peaks" in the step-6 histogram: two bins, each the maximum within ±5 bins and at
  least 10 % of the largest count, with a bin between them below half the smaller of the two.
- **R8.** Hysteresis: the jump intervals differ, or |E_hot − E_cold| > 3σ at some grid point.
- **R9.** The jump at L = 4 is the cold-start fall. "Shrinks by more than 30 %" means
  ΔE(8) < 0.7 × jump(4).
- **R10.** Step 6 depends only on β_mix(6), so it ran concurrently with the L = 8 mixed runs of
  step 4. Each run is an independently seeded chain, so this cannot change a number. It is the only
  departure from strictly sequential stage execution.

## 2. K1 — the complex (own numbers recorded before the desk check was opened)

Own code: `out/k1_own.txt` (SHA-256 `7c2f24c8…483e5`, recorded 18:14:53). Desk check rerun
afterwards: `out/deskcheck_rerun_output.txt`, **all 49 assertions pass, output identical to the pinned
`dlb_deskcheck_output.txt` except the six timing lines.**

| quantity | this run | desk check (target) | agree |
|---|---|---|---|
| L = 2 space: V, E, rhombi, 3-cells | 96, 256, 192, 32 | 96, 256, 192, 32 | yes |
| L = 2: degrees oct / tet; bipartite; 3-cycles | 8 / 4; yes; 0 | 8 / 4; yes; — | yes |
| L = 2: 4-cycles of the void graph = rhombi | 192 = 192 | 192 | yes |
| L = 2: rhombi per link; rhombus area; rhombus normal | 3; a²/(4√2); along its ⟨110⟩ bond | same | yes |
| L = 2: rank ∂₂ (exact mod p and SVD) | 158 = 5N − 2 | 158 | yes |
| L = 2: V − E + F − C₃ | 0 | 0 | yes |
| L = 3 space: V, E, rhombi, 3-cells; 4-cycles; rank ∂₂; χ | 324, 864, 648, 108; 648; 538; 0 | same | yes |
| L = 2, L_t = 6: N_v, N_l, N_loops | 576, 2112, 2688 | 576, 2112, 2688 | yes |
| loops per spatial link; per temporal link (oct / tet) | 5 (3 rhombi + 2 squares); 8 / 4 | 5; 8 / 4 | yes |
| mean loops per link | 56/11 = 5.090909 | 5.090909 | yes |
| 4-cycles of the space × time graph = rhombi + temporal squares | 2688 = 2688; no 3-cycles | (stated in card §1) | yes |
| rank ∂₂ (space × time) | 1533 = N_l − N_v − 3 | 1533 | yes |
| 11 link classes, equally populated; rank at zero crystal momentum | yes; **5** | yes; 5 | yes |
| void: c_E(a_t = 1), c_B(a_t = 1) | 2.0000000000, 0.2500000000 | same | yes |
| void: a_t, k | **0.3535533906 = a/(2√2), 0.7071067812 = 1/√2** | same | yes |
| at a_t = a/(2√2): flux form | (1/√2)·I₆, off-diagonal 2.6 × 10⁻¹⁹ | — | — |
| Z4: k (method validation) | 1.0000000000 | 1 | yes |
| weak-coupling targets at β = 20 | void 1533/(40·2688) = 0.014258; Z4 765/(40·1536) = 0.012451 | same | yes |

Beyond the card's list, the run also checked these, all passing:
- The rhombi are the faces of a genuine cellulation of T³. ∂₁∂₂ = 0 and ∂₂∂₃ = 0 with outward-oriented
  rhombic-dodecahedral cells (each rhombus bounds 2 cells, each cell has 12 faces). The Betti numbers
  are (1, 3, 3, 1) at L = 2 and 3.
- At three generic allowed crystal momenta, rank ∂₂(k) = 8 = 11 − 3 gauge.
- D4 gives 32 triangle classes and k = 2.

**K1: agrees with the desk check on every item. No SC-DLB-4.**

## 3. K2–K5 — all pass

**K2** (`out/state.json`, deterministic; random gauge transformation, 100 random links):

| lattice | max \|Δ cos θ_loop\| under gauge transformation | max \|ΔS_local − ΔS_global\| | pass |
|---|---|---|---|
| void L = 2, L_t = 6 | 3.5 × 10⁻¹⁵ | 7.8 × 10⁻¹³ | yes |
| Z4 L = 4 | 4.2 × 10⁻¹⁵ | 2.9 × 10⁻¹³ | yes |

**K3** (1000 + 10,000 sweeps):

| run | seed | measured | target | deviation | pass |
|---|---|---|---|---|---|
| void L=2 Lt=6 β=0.1 hot | 516838 | ⟨cos⟩ = 0.049739 ± 0.000172 | 0.049938 | -0.40 % | yes |
| void L=2 Lt=6 β=20.0 cold | 715839 | E = 0.014358 ± 0.000005 | 0.014258 | +0.70 % | yes |
| z4 L=4 β=0.1 hot | 32676 | ⟨cos⟩ = 0.049938 ± 0.000202 | 0.049938 | +0.00 % | yes |
| z4 L=4 β=20.0 cold | 231677 | E = 0.012526 ± 0.000007 | 0.012451 | +0.60 % | yes |

The Z4 value at β = 20, 0.012526 ± 0.000007, is identical to CRIT2's independent 0.012526 ± 0.000007
and 0.6σ from the desk check's 0.012531 ± 0.000005. The void value is 1.6σ from the desk check's
0.014369 ± 0.000005. The weak-coupling deviations are positive on both lattices (+0.70 %, +0.60 %), as
the card expects.

**K4** — Z4, L = 8, hot and cold, 1000 + 3000 sweeps (CRIT2 card §4 check 3):

| β | E hot | E cold | C hot | C cold | C_max |
|---|---|---|---|---|---|
| 0.9950 | 0.42538 ± 0.00073 | 0.42512 ± 0.00089 | 1.850 ± 0.096 | 1.846 ± 0.111 | 1.850 |
| 0.9975 | 0.42026 ± 0.00078 | 0.42119 ± 0.00067 | 2.123 ± 0.129 | 2.110 ± 0.149 | 2.123 |
| 1.0000 | 0.41616 ± 0.00111 | 0.41426 ± 0.00119 | 2.120 ± 0.144 | 2.466 ± 0.370 | 2.466 |
| 1.0025 | 0.40839 ± 0.00079 | 0.40922 ± 0.00096 | 2.002 ± 0.178 | 2.111 ± 0.213 | 2.111 |
| **1.0050** | 0.38319 ± 0.00508 | 0.39987 ± 0.00176 | 13.808 ± 2.161 | 3.678 ± 0.726 | 13.808 |
| 1.0075 | 0.39030 ± 0.00386 | 0.38271 ± 0.00333 | 9.469 ± 2.702 | 7.698 ± 1.965 | 9.469 |
| 1.0100 | 0.34723 ± 0.00138 | 0.34436 ± 0.00057 | 2.540 ± 0.429 | 1.478 ± 0.103 | 2.540 |
| 1.0125 | 0.34001 ± 0.00059 | 0.34112 ± 0.00093 | 1.271 ± 0.111 | 1.782 ± 0.243 | 1.782 |
| 1.0150 | 0.33740 ± 0.00043 | 0.33822 ± 0.00061 | 1.192 ± 0.076 | 1.261 ± 0.098 | 1.261 |
| 1.0175 | 0.33612 ± 0.00080 | 0.33464 ± 0.00047 | 1.313 ± 0.153 | 1.075 ± 0.079 | 1.313 |
| 1.0200 | 0.33172 ± 0.00047 | 0.33251 ± 0.00042 | 1.094 ± 0.070 | 1.008 ± 0.036 | 1.094 |

C maximum at **β = 1.0050** (hot start, C = 13.81 ± 2.16), inside the required [1.000, 1.012].
**Pass.** Largest fall in E, cold start: [1.0075, 1.0100] (0.38271 → 0.34436, fall 0.03834).
**E\*_hc = 0.36353.** CRIT2's code found its C maximum at 1.0075, its cold jump at [1.0050, 1.0075]
and E\*_hc = 0.38074. The two codes' cold jumps sit in adjacent steps. Near 1.005–1.0075 the L = 8
runs move between phases here (C = 7.7–13.8), which is what makes the step uncertain at this size.

**K5** — Z4, L = 12, mixed starts, 2000 sweeps (CRIT2 card §4 check 4):

E* = 0.36353; strong wins above 0.37353, weak wins below 0.35353.

| β | E at start | E, mean of readings 1550–2000 | E final | E_s, E_t (same readings) | outcome | seed |
|---|---|---|---|---|---|---|
| 1.00200 | 0.5403 | 0.41033 | 0.40535 | 0.41025, 0.41041 | strong | 105050 |
| 1.00700 | 0.5414 | 0.39792 | 0.39870 | 0.39779, 0.39806 | strong | 105100 |
| 1.01200 | 0.5460 | 0.34504 | 0.34553 | 0.34559, 0.34449 | weak | 105150 |
| 1.01700 | 0.5420 | 0.33622 | 0.33851 | 0.33678, 0.33565 | weak | 105200 |
| 1.02200 | 0.5447 | 0.33046 | 0.33134 | 0.33009, 0.33083 | weak | 105250 |

| β | E after 250, 500, 750, …, 2000 sweeps |
|---|---|
| 1.00200 | 0.4096 0.4136 0.4130 0.4060 0.4048 0.4122 0.4067 0.4054 |
| 1.00700 | 0.4005 0.4032 0.3995 0.3911 0.3987 0.3936 0.3992 0.3987 |
| 1.01200 | 0.3683 0.3775 0.3818 0.3575 0.3480 0.3520 0.3487 0.3455 |
| 1.01700 | 0.3421 0.3360 0.3423 0.3402 0.3381 0.3327 0.3410 0.3385 |
| 1.02200 | 0.3279 0.3278 0.3297 0.3241 0.3328 0.3300 0.3296 0.3313 |

Flip interval **[1.007, 1.012]** (β_mix 1.0095), monotonic, no unresolved point. It contains 1.0111.
**Pass.** This is CRIT2's interval exactly.

## 4. Void runs (card §4.4)

### 4.1 Locate — L = 2, L_t = 6, β 0.50 to 2.00 step 0.01, hot and cold, 500 + 2000 sweeps

Full table in Appendix A. **β₀ = 1.22** (hot start, C = 2.315 ± 0.205; cold 1.840 at the same point),
interior (0.72 from the lower edge, 0.78 from the upper), so there was no extension. The scan has a
single C peak, at 1.21–1.22. E falls by about 0.063 across 1.20–1.23 from both starts. C is 0.45–0.57
across 0.50–1.00, 0.20–0.27 across 1.40–1.50 and 0.09–0.10 near 2.00.

### 4.2 Fine scan — L = 4, L_t = 12, β₀ ± 0.050 step 0.005, hot and cold, 2000 + 4000 sweeps

| β | E hot | E cold | C hot | C cold | C_max |
|---|---|---|---|---|---|
| 1.1700 | 0.40823 ± 0.00015 | 0.40865 ± 0.00016 | 0.711 ± 0.028 | 0.661 ± 0.025 | 0.711 |
| 1.1750 | 0.40460 ± 0.00023 | 0.40456 ± 0.00020 | 0.742 ± 0.039 | 0.726 ± 0.025 | 0.742 |
| 1.1800 | 0.40099 ± 0.00019 | 0.40092 ± 0.00019 | 0.727 ± 0.028 | 0.790 ± 0.028 | 0.790 |
| 1.1850 | 0.39703 ± 0.00016 | 0.39728 ± 0.00030 | 0.781 ± 0.044 | 0.754 ± 0.040 | 0.781 |
| 1.1900 | 0.39402 ± 0.00019 | 0.39351 ± 0.00017 | 0.713 ± 0.026 | 0.783 ± 0.029 | 0.783 |
| 1.1950 | 0.38934 ± 0.00023 | 0.38958 ± 0.00018 | 0.809 ± 0.033 | 0.709 ± 0.023 | 0.809 |
| 1.2000 | 0.38522 ± 0.00027 | 0.38521 ± 0.00018 | 0.812 ± 0.029 | 0.826 ± 0.025 | 0.826 |
| 1.2050 | 0.38139 ± 0.00024 | 0.38114 ± 0.00026 | 0.811 ± 0.045 | 0.894 ± 0.055 | 0.894 |
| 1.2100 | 0.37685 ± 0.00038 | 0.37707 ± 0.00018 | 0.972 ± 0.055 | 0.875 ± 0.039 | 0.972 |
| 1.2150 | 0.37275 ± 0.00023 | 0.37241 ± 0.00039 | 0.888 ± 0.054 | 0.964 ± 0.072 | 0.964 |
| 1.2200 | 0.36799 ± 0.00033 | 0.36731 ± 0.00027 | 0.972 ± 0.056 | 0.963 ± 0.052 | 0.972 |
| 1.2250 | 0.36256 ± 0.00032 | 0.36304 ± 0.00047 | 0.928 ± 0.052 | 1.083 ± 0.074 | 1.083 |
| 1.2300 | 0.35825 ± 0.00035 | 0.35820 ± 0.00045 | 0.931 ± 0.060 | 1.034 ± 0.075 | 1.034 |
| 1.2350 | 0.35334 ± 0.00046 | 0.35328 ± 0.00049 | 1.173 ± 0.093 | 1.059 ± 0.074 | 1.173 |
| 1.2400 | 0.34648 ± 0.00041 | 0.34642 ± 0.00039 | 1.210 ± 0.085 | 1.138 ± 0.067 | 1.210 |
| 1.2450 | 0.33865 ± 0.00078 | 0.34027 ± 0.00063 | 1.737 ± 0.252 | 1.262 ± 0.123 | 1.737 |
| **1.2500** | 0.32567 ± 0.00172 | 0.32984 ± 0.00146 | 4.076 ± 0.689 | 2.782 ± 0.681 | 4.076 |
| 1.2550 | 0.30919 ± 0.00175 | 0.30517 ± 0.00061 | 3.446 ± 1.032 | 1.098 ± 0.103 | 3.446 |
| 1.2600 | 0.30025 ± 0.00048 | 0.30023 ± 0.00052 | 0.898 ± 0.089 | 1.028 ± 0.155 | 1.028 |
| 1.2650 | 0.29565 ± 0.00024 | 0.29627 ± 0.00027 | 0.700 ± 0.033 | 0.750 ± 0.049 | 0.750 |
| 1.2700 | 0.29230 ± 0.00023 | 0.29245 ± 0.00025 | 0.630 ± 0.043 | 0.626 ± 0.031 | 0.630 |

E_s and E_t, L = 4:
| β | E_s hot | E_t hot | E_s cold | E_t cold | E_t/E_s cold |
|---|---|---|---|---|---|
| 1.1700 | 0.41942 | 0.39983 | 0.41994 | 0.40018 | 0.9529 |
| 1.1750 | 0.41581 | 0.39620 | 0.41583 | 0.39610 | 0.9526 |
| 1.1800 | 0.41222 | 0.39257 | 0.41220 | 0.39246 | 0.9521 |
| 1.1850 | 0.40833 | 0.38856 | 0.40851 | 0.38885 | 0.9519 |
| 1.1900 | 0.40530 | 0.38556 | 0.40489 | 0.38497 | 0.9508 |
| 1.1950 | 0.40069 | 0.38083 | 0.40077 | 0.38119 | 0.9511 |
| 1.2000 | 0.39644 | 0.37680 | 0.39644 | 0.37679 | 0.9504 |
| 1.2050 | 0.39259 | 0.37298 | 0.39235 | 0.37272 | 0.9500 |
| 1.2100 | 0.38799 | 0.36848 | 0.38827 | 0.36868 | 0.9495 |
| 1.2150 | 0.38390 | 0.36438 | 0.38348 | 0.36412 | 0.9495 |
| 1.2200 | 0.37903 | 0.35972 | 0.37826 | 0.35909 | 0.9493 |
| 1.2250 | 0.37339 | 0.35443 | 0.37393 | 0.35487 | 0.9490 |
| 1.2300 | 0.36898 | 0.35020 | 0.36901 | 0.35009 | 0.9487 |
| 1.2350 | 0.36398 | 0.34536 | 0.36393 | 0.34528 | 0.9488 |
| 1.2400 | 0.35688 | 0.33869 | 0.35682 | 0.33862 | 0.9490 |
| 1.2450 | 0.34863 | 0.33116 | 0.35037 | 0.33269 | 0.9496 |
| 1.2500 | 0.33490 | 0.31875 | 0.33929 | 0.32274 | 0.9512 |
| 1.2550 | 0.31713 | 0.30323 | 0.31281 | 0.29945 | 0.9573 |
| 1.2600 | 0.30768 | 0.29467 | 0.30761 | 0.29468 | 0.9580 |
| 1.2650 | 0.30278 | 0.29030 | 0.30355 | 0.29082 | 0.9581 |
| 1.2700 | 0.29936 | 0.28701 | 0.29951 | 0.28716 | 0.9588 |

- **β₄ = 1.250** (hot start, C = 4.08 ± 0.69). Interior; no extension.
- **Jump interval (L = 4), hot: [1.250, 1.255]**, E 0.32567 → 0.30919 (fall 0.01649).
- **Jump interval (L = 4), cold: [1.250, 1.255]**, E 0.32984 → 0.30517 (fall 0.02466).

C is large at both 1.250 and 1.255 (hot 4.1 and 3.4). The L = 4 runs there move between the phases,
and hot and cold agree to within 2.2σ at every grid point.

### 4.3 Cold scan — L = 6, L_t = 18, β₄ ± 0.020 step 0.005, cold, 500 + 1500 sweeps

| β | E cold | E_s (rhombi) | E_t (temporal) | E_t/E_s | C cold | seed |
|---|---|---|---|---|---|---|
| 1.2300 | 0.35836 ± 0.00023 | 0.36921 | 0.35023 | 0.9486 | 0.964 ± 0.087 | 559815 |
| 1.2350 | 0.35262 ± 0.00033 | 0.36323 | 0.34465 | 0.9488 | 1.375 ± 0.150 | 559865 |
| 1.2400 | 0.34694 ± 0.00031 | 0.35733 | 0.33915 | 0.9491 | 1.126 ± 0.145 | 559915 |
| 1.2450 | 0.34050 ± 0.00033 | 0.35054 | 0.33297 | 0.9499 | 1.159 ± 0.124 | 559965 |
| 1.2500 | 0.33292 ± 0.00033 | 0.34259 | 0.32567 | 0.9506 | 1.160 ± 0.126 | 560015 |
| 1.2550 | 0.31530 ± 0.00087 | 0.32381 | 0.30891 | 0.9540 | 3.886 ± 0.964 | 560065 |
| 1.2600 | 0.30042 ± 0.00027 | 0.30792 | 0.29480 | 0.9574 | 0.911 ± 0.097 | 560115 |
| 1.2650 | 0.29639 ± 0.00017 | 0.30364 | 0.29096 | 0.9582 | 0.685 ± 0.046 | 560165 |
| 1.2700 | 0.29311 ± 0.00018 | 0.30016 | 0.28783 | 0.9589 | 0.691 ± 0.067 | 560215 |

**Jump interval (L = 6): [1.250, 1.255]**, E 0.33292 → 0.31530 (fall 0.01762); the next step,
[1.255, 1.260], falls 0.01488. The cold start at 1.255 part-melted (E = 0.31530, between the branches,
C = 3.89). **E\* = 0.32411.**

### 4.4 Mixed-phase starts — L = 6, L_t = 18, 1.2525 ± 0.0075 step 0.0025, 2000 sweeps

E* = 0.32411; strong wins above 0.33411, weak wins below 0.31411.

| β | E at start | E, mean of readings 1550–2000 | E final | E_s, E_t (same readings) | outcome | seed |
|---|---|---|---|---|---|---|
| 1.24500 | 0.5302 | 0.34168 | 0.34472 | 0.35133, 0.33444 | strong | 559966 |
| 1.24750 | 0.5305 | 0.33710 | 0.33454 | 0.34752, 0.32929 | strong | 559991 |
| 1.25000 | 0.5310 | 0.33259 | 0.33482 | 0.34249, 0.32517 | unresolved | 560016 |
| 1.25250 | 0.5323 | 0.32727 | 0.32949 | 0.33610, 0.32065 | unresolved | 560041 |
| 1.25500 | 0.5338 | 0.32430 | 0.32489 | 0.33353, 0.31737 | unresolved | 560066 |
| 1.25750 | 0.5309 | 0.31620 | 0.31968 | 0.32538, 0.30931 | unresolved | 560091 |
| 1.26000 | 0.5317 | 0.30233 | 0.30461 | 0.31001, 0.29656 | weak | 560116 |

| β | E after 250, 500, 750, …, 2000 sweeps |
|---|---|
| 1.24500 | 0.3365 0.3423 0.3461 0.3421 0.3379 0.3433 0.3430 0.3447 |
| 1.24750 | 0.3385 0.3358 0.3361 0.3349 0.3297 0.3321 0.3404 0.3345 |
| 1.25000 | 0.3373 0.3342 0.3366 0.3306 0.3326 0.3318 0.3323 0.3348 |
| 1.25250 | 0.3283 0.3261 0.3278 0.3262 0.3282 0.3229 0.3273 0.3295 |
| 1.25500 | 0.3279 0.3253 0.3213 0.3195 0.3238 0.3258 0.3208 0.3249 |
| 1.25750 | 0.3152 0.3170 0.3166 0.3138 0.3096 0.3195 0.3134 0.3197 |
| 1.26000 | 0.3127 0.3119 0.3082 0.3047 0.2998 0.3031 0.3029 0.3046 |

**β_mix(6) = 1.25375**, flip interval **[1.2475, 1.2600]**, monotonic. The four points 1.2500, 1.2525,
1.2550 and 1.2575 are unresolved, inside the interval. No extension.

### 4.5 Mixed-phase starts — L = 8, L_t = 24, β_mix(6) ± 0.005 step 0.0025, 2000 sweeps

E* = 0.32411; strong wins above 0.33411, weak wins below 0.31411.

| β | E at start | E, mean of readings 1550–2000 | E final | E_s, E_t (same readings) | outcome | seed |
|---|---|---|---|---|---|---|
| 1.24875 | 0.5240 | 0.33578 | 0.33577 | 0.34571, 0.32834 | strong | 575842 |
| 1.25125 | 0.5234 | 0.32954 | 0.33078 | 0.33908, 0.32238 | unresolved | 575866 |
| 1.25375 | 0.5236 | 0.32540 | 0.32434 | 0.33469, 0.31843 | unresolved | 575892 |
| 1.25625 | 0.5242 | 0.32046 | 0.32142 | 0.32926, 0.31386 | unresolved | 575916 |
| 1.25875 | 0.5238 | 0.30653 | 0.30600 | 0.31425, 0.30074 | weak | 575942 |

| β | E after 250, 500, 750, …, 2000 sweeps |
|---|---|
| 1.24875 | 0.3351 0.3340 0.3319 0.3358 0.3378 0.3360 0.3363 0.3358 |
| 1.25125 | 0.3312 0.3321 0.3293 0.3285 0.3315 0.3298 0.3265 0.3308 |
| 1.25375 | 0.3247 0.3256 0.3237 0.3245 0.3262 0.3264 0.3253 0.3243 |
| 1.25625 | 0.3204 0.3180 0.3212 0.3211 0.3221 0.3228 0.3214 0.3214 |
| 1.25875 | 0.3163 0.3125 0.3106 0.3094 0.3076 0.3051 0.3070 0.3060 |

**β_mix(8) = 1.25375**, flip interval **[1.24875, 1.25875]**, monotonic. The three points 1.25125,
1.25375 and 1.25625 are unresolved, inside the interval. No extension.

### 4.6 Result (step 5)

| quantity | card convention (β) | continuum (1/e² = β/√2) |
|---|---|---|
| β₀ (L = 2) | 1.22 | 0.8627 |
| β₄ (L = 4, C maximum) | 1.250 | 0.8839 |
| jump interval L = 4 (hot and cold) | [1.250, 1.255] | [0.8839, 0.8874] |
| jump interval L = 6 | [1.250, 1.255] | [0.8839, 0.8874] |
| β_mix(6) | 1.25375, interval [1.2475, 1.2600] | 0.8865 |
| β_mix(8) | 1.25375, interval [1.24875, 1.25875] | 0.8865 |
| **β_∞ = β_mix(8)** | **1.2538 ± 0.0050** (1.25375 ± 0.00500) | **0.8865 ± 0.0035** |
| SC-DLB-2 interval (L = 6 jump widened by the L = 4 → 6 shift, 0) | **[1.250, 1.255]** | **[0.8839, 0.8874]** |

- Uncertainty = max(half the L = 8 flip interval = 0.00500, |β_mix(8) − β_mix(6)| = 0) = **0.00500**.
- **ΔE(L = 8)** = end-state E of the nearest strong-win run below β_∞ (1.24875, 0.33578) minus that
  of the nearest weak-win run above it (1.25875, 0.30653) = **0.02926** (0.02977 from final-sweep
  values).
- Check, not headline: the line through (1/(L³L_t), β_mix(L)) for L = 6 and 8, evaluated at 0, gives
  1.25375 (β_mix did not move).

### 4.7 Histogram (step 6) — L = 6, L_t = 18, β = β_mix(6) = 1.25375, mixed start, 2000 + 20,000 sweeps, seed 560055

- Mean E = 0.32610 and sd 0.00322 over 20,000 sweeps, binned over [0.3110, 0.3395] in 50 bins.
- **One peak** (bin 26, E = 0.3261); the counts fall smoothly on both sides (`out/post_obs.txt`).
- **Binder B = 0.666537** (2/3 = 0.666667).
- The E autocorrelation is 0.90 at lag 1, 0.40 at lag 100 and 0.0 at lag 500.
- The forty 500-sweep block means all lie in 0.3201–0.3291.
- E crosses E\* 2357 times; 25.6 % of sweeps lie below E\*. These are fluctuations about a mean 0.002
  above E\*, not visits to the weak branch (about 0.305 at this β).

## 5. Hash before placement (card §4.6)

`out/dlb_numbers.txt` (every Q3 number, written by `run/make_numbers.py` from `out/state.json`):
**SHA-256 `5f60f1d7b660b5407352846d30c63354b883a81313aa9a9fc984ffa55fec8aae`**, written 20:07 AEDT and
posted to the conversation before `run/place.py` (§6) was run (`place.py` refuses to run without the
recorded hash).

## 6. Q4 — transition order (card §4.4 step 7; reported, not a verdict input)

| diagnostic | finding | holds? |
|---|---|---|
| (a) hysteresis at L = 4 | hot and cold jump intervals identical ([1.250, 1.255]); largest \|E_hot − E_cold\| = 2.16σ (at 1.255) | **no** |
| (b) jump L = 4 (cold) → L = 6 → L = 8 | 0.02466 → 0.01762 → ΔE(8) 0.02926 (+18.6 % from L = 4 to 8) | does not shrink by > 30 % |
| (c) two peaks in the step-6 histogram | one peak; B = 0.666537 | **no** |

**Call: order undetermined.** First-order needs (a) and (c), and neither holds. §11 explains why
neither test could detect a first-order transition in these runs; that explanation is not a verdict
input.

## 7. Q5 — anisotropy record (recorded, not interpreted)

| where | E_s (rhombi) | E_t (temporal squares) | E_t/E_s |
|---|---|---|---|
| L = 6 cold scan, β = 1.250 (strong side of the jump) | 0.34259 ± 0.00037 | 0.32567 ± 0.00031 | 0.9506 |
| L = 6 cold scan, β = 1.255 (weak side; part-melted run) | 0.32381 ± 0.00095 | 0.30891 ± 0.00081 | 0.9540 |
| L = 6 cold scan, β = 1.260 (weak side) | 0.30792 | 0.29480 | 0.9574 |
| L = 8 mixed, β = 1.24875 (strong win, below β_∞) | 0.34571 | 0.32834 | 0.9497 |
| L = 8 mixed, β = 1.25875 (weak win, above β_∞) | 0.31425 | 0.30074 | 0.9570 |
| β = 20 (K3; void L = 2, L_t = 6, cold) | 0.014654 ± 0.000007 | 0.014135 ± 0.000007 | 0.9646 |

The desk check's β = 20 values were 0.014668 and 0.014145 (ratio 0.9643). On every scan E_t/E_s is
0.949–0.953 on the strong side and 0.957–0.959 on the weak side (L = 4 table in §4.2; L = 6 table in §4.3).

## 8. Q6 — placement (computed after §5; `out/placement.txt`)

**8.1 Against the other lattices**

| lattice | β_c (card) | k | 1/e²_c | 1/e²_c ÷ Z4's | source |
|---|---|---|---|---|---|
| Z4 | 1.0111 | 1 | 1.0111 | 1 | Arnold et al.; K4/K5 here |
| D4 | 0.6150 ± 0.00125 | 2 | 1.2300 ± 0.0025 | 1.2165 | CRIT2 |
| **void × time** | **1.2538 ± 0.0050** | **1/√2** | **0.8865 ± 0.0035** | **0.8768** | this gate |

β_∞ is 1.240 × Z4's and 2.039 × D4's β_c in the card convention. In the continuum normalisation the
order reverses: void (0.887) < Z4 (1.011) < D4 (1.230).

**8.2 The card's §9 heuristics** (hit iff [β_∞ − 0.005, β_∞ + 0.005] = [1.24875, 1.25875] meets the
interval; intervals recomputed from their stated definitions and checked against the card's):

| heuristic | interval | result | implied quantity on the void complex |
|---|---|---|---|
| H1 fixed ⟨θ²⟩ = (rank/N_loops)/β | [1.0223, 1.1555] | **miss** by 0.093 | 0.4558 (Z4 0.4945, D4 0.5589) |
| H2 fixed 1/e²_c | [1.4299, 1.7395] | **miss** by 0.171 | 0.8865 (Z4 1.0111, D4 1.2300) |
| H3 fixed β_c × loops per link | [0.9664, 1.1917] | **miss** by 0.057 | 6.3827 (Z4 6.0666, D4 4.9200) |
| scoping note §7: between D4 and Z4 | [0.615, 1.011] | **miss** (lower end 0.238 above 1.011) | — |

β_∞ lies between H1/H3 and H2: higher than the two "fixed lattice quantity" heuristics, lower than
the "fixed continuum coupling" one. On H3's own measure, β_c × loops per link, the void value (6.38)
is 5 % above Z4's (6.07) and continues the trend Z4 sets against D4 (4.92). With the narrower SC-DLB-2
interval [1.250, 1.255] the four results are the same (misses by 0.0945, 0.175, 0.058 and 0.239).

**8.3 The programme's candidate number, for orientation only.** Under the DL-STIFF card's convention
(its §1, k = 1), β_geom = 2ξ²/a² = 10.742018:

- **β_geom/β_∞ = 8.568**, and **15.191508/β_∞ = 12.117**. Over the SC-DLB-2 interval these are
  8.559–8.594 and 12.105–12.153.
- A Wilson β of 10.742018 on this complex means 1/e² = 7.595754.

This is a statement about a convention in that card. It is not about that gate's result, and nothing
is rescored.

## 9. Verdict

| condition | SC-DLB-1 requires | found | met |
|---|---|---|---|
| checks K1–K5 | pass | all pass | yes |
| L = 8 mixed-phase outcome flips | yes | yes, inside the first grid, no extension | yes |
| unresolved points at L = 8 | **at most one** | **three** (1.25125, 1.25375, 1.25625) | **no** |
| uncertainty | ≤ 0.010 | 0.00500 | yes |

**Not SC-DLB-1.** The card's SC-DLB-2 names two triggers: the L = 8 method "does not resolve within
the extension limit", or "the uncertainty exceeds 0.010". Read literally, neither describes this
outcome, which is a flip with too many unresolved points. That is a gap in the card's verdict list
(**CN-DLB-01**). SC-DLB-2 is the card's code for "located, not resolved", and the transition was
located at L = 4 and 6 by both C peak and E jump. The run therefore assigns **SC-DLB-2**, the less
favourable of the two adjacent codes. It reports the β_c that SC-DLB-2 prescribes, **[1.250, 1.255]**,
and alongside it the β_∞ that step 5 defines unconditionally, **1.2538 ± 0.0050**. The two are
consistent. SC-DLB-0, -3 and -4 do not apply.

## 10. Analyst's disclosure (card §9), scored

| forecast | outcome | score |
|---|---|---|
| verdict: SC-DLB-1 75 %, SC-DLB-2 15 %, SC-DLB-0 8 %, SC-DLB-3/4 2 % | SC-DLB-2 (under CN-DLB-01) | outcome had 15 % |
| β_∞ in [1.00, 1.30] 55 %; (1.30, 1.80] 30 %; < 1.00 10 %; > 1.80 5 % | 1.2538 | **hit**: the 55 % bin |
| central guess 1.15 | 1.2538 | off by +0.104 (+9 %) |
| β_∞ above Z4's 1.0111, about 85 % ("fewer loops per link, so a larger β to order") | 1.240 × Z4 | **hit** |
| H1 [1.0223, 1.1555] | 1.24875–1.25875 | **miss** (0.093) |
| H2 [1.4299, 1.7395] ("the live alternative") | — | **miss** (0.171) |
| H3 [0.9664, 1.1917] | — | **miss** (0.057) |
| "the gate separates H2 from the other two" | it separates all three from the result, which lies between them | — |
| scoping note §7: between D4 and Z4, 0.615 to 1.011 (different analyst) | above both | **miss**; the card's author forecast against it, which scores as a hit for the card |
| order: first-order 50 %, undetermined 50 % | order undetermined | 50 % outcome |
| E_t/E_s near β_∞ within 10 % of 1 | 0.950–0.957 | **hit** |

The card's §1/§7 statements of the desk check are all reproduced (§2).

## 11. Observations (not verdict inputs; CONJECTURE; computed after the §4.6 hash, `out/post_obs.txt`)

- **What the unresolved points are.** Fit the L = 6 cold-scan strong branch (1.230–1.250) with a
  quadratic: the residuals at the fit points are at most 0.00027. Fit the weak branch (1.260–1.270)
  with a line.
  - Every L = 8 "unresolved" run then sits on the **strong** (confining) branch, within 0.0016–0.0026
    of it (the run-to-run spread of the 10 readings is about 0.002), and 0.017–0.023 above the weak branch.
  - So do the L = 6 runs at 1.2500–1.2550 (within 0.0004–0.0019); 1.2575 is 0.0048 below it.
  - None of these runs drifted: their readings over sweeps 250–2000 stay within a 0.006–0.012 range.
  - They are pure strong-phase end states that fall inside the ±0.01 band: E\* = 0.32411 lies only
    about 0.009 below the strong branch at 1.250, and the extrapolated branch gap at 1.2525 is about 0.025.
  - Read that way, the mixed-start outcomes flip at **[1.2575, 1.2600] (L = 6)** and **[1.25625,
    1.25875] (L = 8)**. Step 5's formula would then give 1.2575 ± 0.0013. This is post hoc, inside the
    card's β_∞ ± 0.005, and **not** a result of this gate. The card's band is ±0.01 fixed (inherited
    from CRIT2, where the D4 gap was about 0.09), so the outcome rule cannot see it (CN-DLB-02).
- **Why the order tests could not fire.**
  - (c) The step-6 histogram ran at β_mix(6) = 1.25375. On the reading above, that is about 0.005
    below where the L = 6 mixed starts flip. The run stayed in the strong phase for 20,000 sweeps: its
    mean is 0.0011 below the strong branch, and nothing tunnelled. One peak is what a metastable or
    stable single phase gives, whatever the order.
  - (a) At L = 4 the runs tunnel near the jump (C = 3–4), so hot and cold agree.
  - (b) ΔE(8) spans 0.01 in β and the L = 4 and 6 jumps span 0.005, so (b) compares falls that
    include different amounts of branch slope.
  - The data are consistent with a first-order transition with a modest gap: the gap does not shrink
    from L = 4 to 8, nothing tunnels at L = 6 in 20,000 sweeps, and the L = 8 weak-win run took about
    1500 sweeps to settle (0.316 → 0.306). They do not establish one.
- **Size of the jump.** The extrapolated branch gap at L = 6 is about 0.025 in E per loop. Z4's fall
  at L = 8 here is 0.038, and D4's is about 0.09 (CRIT2). By this crude measure the void complex has
  the smallest gap of the three.
- **C maximum.** As CRIT2 found on D4, β₄ (1.250) marks the last strong-phase grid point, not the
  jump. Here β₄ and the L = 6 jump interval share their lower end.
- **The anisotropy record moves across the transition**: E_t/E_s rises from about 0.950 (strong) to
  about 0.957 (weak), and is 0.965 at β = 20.

## 12. Correction notices

- **CN-DLB-01 (card, verdict codes).** SC-DLB-1 requires at most one unresolved L = 8 point.
  SC-DLB-2's stated triggers are no resolution within the extension limit, or uncertainty > 0.010.
  Neither code covers "flip inside the grid, uncertainty ≤ 0.010, more than one unresolved point".
  This run assigns SC-DLB-2 (§9). A successor card should state the rule. Not SC-DLB-4, which is
  reserved for a wrong desk-check geometry.
- **CN-DLB-02 (method, inherited from CRIT2 §5.4).** The ±0.01 outcome band is absolute. On this
  complex it is comparable to the phase gap: band width 0.02, extrapolated gap ≈ 0.025 at L = 6, and
  E\* about 0.009 from the strong branch. So pure-phase end states near β_c score "unresolved" (§11).
  A replication should fix the band relative to the measured gap (for example ± one third of the
  L = 6 fall), or score outcomes against the two branches. It should also take the step-6 histogram
  at the flip of the mixed starts, not at a midpoint that unresolved points can bias. Recommendation
  only; nothing was changed here.
- **CN-DLB-03 (Gate DL, CN-DL-06).** CN-DL-06 quotes "β > β_c ≈ 1.01", the hypercubic value. On the
  DL construction's own lattice, with every smallest loop at one β, the threshold is β_c ≈ 1.25 (card
  convention), 1/e²_c ≈ 0.89 (CONJECTURE, this gate). The statement "massless iff β > β_c" is
  unchanged; its number is.
- **CN-DLB-04 (card §7, minor).** The card's D4 row and K1 are consistent with this run. The β = 20
  E_s / E_t values differ from the desk check's by 1–2σ, which is expected from a different random
  stream. No defect.

## 13. Tier movements

| # | statement | tier |
|---|---|---|
| 1 | β_c of compact U(1), Wilson action, FCC void network × time, β_t = β_s: located at [1.250, 1.255] (L = 4, 6); β_∞ = 1.2538 ± 0.0050; 1/e²_c = 0.8865 ± 0.0035 | **CONJECTURE** (new; same-session cap), pending blind replication |
| 2 | CN-DL-06: the photon of the DL construction is massless iff β > β_c, now with β_c ≈ 1.25 | number added at CONJECTURE (CN-DLB-03) |
| 3 | K1 combinatorics (counts, cellulation, ranks, zero-momentum rank 5, a_t = a/(2√2), k = 1/√2) | reproduced by a second, independent code; as combinatorics, closed by computation (as Gate DL treated its own network counts) |
| 4 | order of the transition | undetermined (§6); OBSERVATION in §11 |
| 5 | anything about α, or about whether anything fixes β | no movement (card §3, §6.3) |

## 14. Limits

- The card's limits apply: Wilson action only, β_t = β_s only, one spatial complex, and bare
  couplings. β_c is a lattice quantity; compact U(1) in 4D has no interacting continuum limit at the
  transition, and k is a tree-level normalisation.
- The uncertainty is the card's grid rule. It carries no statistical error. There is one mixed run
  per β, and outcomes near the flip depend on the ±0.01 band (CN-DLB-02).
- Two mixed-phase sizes. β_mix did not move from L = 6 to 8, so the shift term in the uncertainty is
  zero. That is a grid statement and says nothing about smaller shifts.
- One code, one thread. The desk check's simulator was used only at β = 0.1 and 20 in the card thread,
  and only as K3's targets here.

## 15. Plain-language summary

The DL construction puts electromagnetism on the network of holes between packed spheres. It has a
light-carrying (massless photon) phase only if its coupling β is above a tipping point. Nobody had
measured that tipping point for this network; this gate measured it.

First the program had to pass five checks:
1. It rebuilt the network independently and matched every count in the card. Only then did it open
   the card author's checking script.
2. Basic correctness tests passed.
3. Limit tests passed: very hot and very cold.
4. On the ordinary cubic lattice, where the answer is known (1.0111), it found the transition on a
   small box …
5. … and found the same two-phase bracket as the earlier independent program, 1.007–1.012.

On the void network the tipping point sits at **β ≈ 1.25** in the card's units. The scan from small
to large boxes put it in the same 0.005-wide step at two sizes. The two-phase method on the two
largest boxes centred it at 1.2538 ± 0.005. That is about 24 % above the cubic lattice's value. In the
units that measure the actual electric charge, 1/e² ≈ 0.89, which is *below* the cubic lattice's
1.011.

The card's three rules of thumb all missed: the answer lies between them. The verdict is "located,
not fully resolved". The two-phase method left three of its five points undecided. Looking afterwards
explains why: on this lattice the two phases differ by less in energy than the method's fixed
tolerance. The number stands as a CONJECTURE until a second, blind run reproduces it.

What it decides: the photon in this construction is massless only if the coupling exceeds about
1.25. Whether anything fixes the coupling is a different gate's question.

## 16. Files

All under `audit/gates/DLBETA/`. `MANIFEST.sha256` lists every file including this one.
Raw time series: `out/series/<stage>_series.npz` (E, E_s, E_t after every sweep, float64, key
`<tag>__E` etc.) and `out/series/<stage>.jsonl` (one record per run, with its seed); consolidated
bit-identically from the per-run files by `run/consolidate.py`.

| file | bytes | SHA-256 |
|---|---|---|
| `gate_DLBETA_prompt_as_run.md` | 25450 | `eae34f3becfa4c8ce798eb01f307c7560e1d1301bfb4f2e3e70d11d5c73c9024` |
| `out/code_frozen_before_runs.sha256` | 443 | `60d3a3e73ca21fe668d5702396f63ffc0c89c09c45daf792ae38a4272cda90c0` |
| `out/deskcheck_rerun_output.txt` | 6822 | `0695e451fb9542a54e31d8082307520bb46f6fa69799a61142fef7959e49664b` |
| `out/dlb_numbers.sha256` | 111 | `b6b1c070cc35e7becb674939b1c1808661580bfb8c0232623d67dcd9346c9725` |
| `out/dlb_numbers.txt` | 1550 | `5f60f1d7b660b5407352846d30c63354b883a81313aa9a9fc984ffa55fec8aae` |
| `out/driver.log` | 21143 | `c07047a2e08ca1e53dd9306947a98d6c1831dfca76f3c7f131b7964cac835644` |
| `out/k1_own.json` | 844 | `fe2617f2d65d3e7f48064e5d4af40f18cdf41e5d9000fd379cd76bbc87f5fa3b` |
| `out/k1_own.txt` | 7177 | `7c2f24c8469f1cf62094b4d86ca70e70a18b5bc1e832dde134a4f56a52d483e5` |
| `out/k1_recorded_at.txt` | 353 | `68940d5827696e8a1478da1e11cac8eb2f1ff810bd4614dd6f84797f0b714c38` |
| `out/placement.json` | 512 | `7b2eb1984d50e3e9c368365f5b456257171f1022409e6b4026a1dfb6d1ad57fa` |
| `out/placement.txt` | 1232 | `5e9b53c5d292bd0cf2adc2a2ad4c88d142f90b2f1742b7f682c4f589282d7e63` |
| `out/post_obs.txt` | 3540 | `4772bec5a386aeb7603ca7e59a4c07480662a438c7ae4592cfd8afb5785a315e` |
| `out/provenance_log.txt` | 2883 | `430e92867d38512ce23dfe8e8da5383238a34cb9600bfc8acf40bb84e2e3b62b` |
| `out/q4q5.json` | 1916 | `522d5d4f73151f0a384da2042e0c350254074f9d986480a5484c807ae3d1eba1` |
| `out/q4q5.txt` | 1147 | `9fb3caf8a2a9c5a071ebd0d56ca4b37a3057fc78bea078823ebbb5cce883e681` |
| `out/run_prompt_as_received.txt` | 2139 | `1e5a39679ebdcc1f8242d2a854cd29c13da3676144d66a76f4e061ebe47ff314` |
| `out/series/K3.jsonl` | 1549 | `1f43a3e44e70f433572f7152ee38c71460b8ad77b007ed015bb84c686e3628f1` |
| `out/series/K3_series.npz` | 962260 | `705bd34a814fbf38ec9e50b70ac2ae9fe46d1bfe85e439ff84046a24bd26ecf1` |
| `out/series/K4.jsonl` | 8566 | `bc61f47cce97a14c80bbb632a14b9f5457eee300f22faec98f8c919ebbeeebda` |
| `out/series/K4_series.npz` | 1924181 | `0a02bf2e9c8f1e86345a74858d46c3473471d249b886b91129e463b6201eaddf` |
| `out/series/K5.jsonl` | 2000 | `6dec06451ed2c1e49b75d094fc83f49ad65b895e84b37799827e0bf95011bca2` |
| `out/series/K5_series.npz` | 219212 | `9eadf716eb2985adf7759b664347245e5510bbe59cb3e4c6138d7c221943baec` |
| `out/series/S1_locate.jsonl` | 118698 | `458fd79e45c845e0443d48dc2da93370a727c310aed6edfd70a6483438e10116` |
| `out/series/S1_locate_series.npz` | 16707272 | `0cdafb138238c0e072148995c263b055c088f74f5d886b6cc07712513a474285` |
| `out/series/S2_fine.jsonl` | 16667 | `f73d1e125e7a11d4edb35f3c110e9b8d0761391cb13809031ebb38f6dbe287de` |
| `out/series/S2_fine_series.npz` | 5439219 | `755d69cbca385199296e664b84aea099b213d7933cdbf4c5964621a6b58d3dc3` |
| `out/series/S3_cold.jsonl` | 3528 | `5ff7fc7847322e18d987ec92bf02a6ad06379061603ce6b41c65108c27e1b7de` |
| `out/series/S3_cold_series.npz` | 391160 | `12be17eacf79698e7a77348da74721e590972744e240f8bb11bb6ba40d34c8eb` |
| `out/series/S4_mixed6.jsonl` | 2865 | `136dfb22a2799b5b996199657874e2b1e6cd79f7b366d98c02e27ba31205a598` |
| `out/series/S4_mixed6_series.npz` | 304163 | `5ea2f7dd93210b8e67d5099082f99ab9c5f63e19de64995af48e83fafe5d13e0` |
| `out/series/S4_mixed8.jsonl` | 2065 | `e42aa1f401dd36a2db8430f12334ff4c4821fb5511d406599fad42b3e9c93f78` |
| `out/series/S4_mixed8_series.npz` | 216027 | `69959c09c42e9e34c5cfce67e1cad77744a1181552e20c53fe3d963e8a2303bf` |
| `out/series/S6_hist.jsonl` | 413 | `75b6d6acfd2f31e9c85bc2c5a40b06540e923b91370c8f257dfd123a632c193f` |
| `out/series/S6_hist_series.npz` | 468043 | `2fce710460577aaaf1439852714ff43c836a29a0990e0c2f7cc3e516f8ecd182` |
| `out/state.json` | 162778 | `4b39462ed319c7274538c1fd0ee88ef77353a1330b4aae9e6a90f10cdec4a2c2` |
| `out/tables.md` | 17703 | `5b14218bc3efa082a99a7a1752b3fe892ccf95b3de8532d29ee3199ffd825aac` |
| `out/unit_tests.json` | 731 | `388f9e1d25623ef88fcfeb1bd1147e6cd4c40a263196a11de1b530211a4a88d8` |
| `out/unit_tests.txt` | 2176 | `e93da14f01c4d54414a7e25cfab0904193bf7a385fddbe06a7b0e3c76b90b4c8` |
| `run/RESULT_template.md` | 30152 | `35bd6996f2d71b927c198438ce00fe828ac2a71d6b35aeb32f2a74dd1bd90599` |
| `run/assemble_result.py` | 1754 | `70561d5e66f04e241bea9b12f3da708913a67619c4adcdc8d24c86a21ff577ec` |
| `run/consolidate.py` | 1408 | `4fdfd91f15bd1f08982b0d927fb074c1d9f5449d9bce04421e1a9247c9048503` |
| `run/dlb_complex.py` | 11405 | `4aa142b0f57122b02a4590ce221d7510ca86ccff051a156ce38a1e8e75214d8a` |
| `run/dlb_driver.py` | 20217 | `720dee806ac09d0d32a9555fcf1787d05203ebef106fad53509cdd31ffaf1d72` |
| `run/dlb_k1.py` | 15764 | `64214508e575496a5a769440535e8a475d44b3df6b365883c97e18d54154985a` |
| `run/dlb_sim.py` | 7997 | `4a813cf7eea0b883eaa3ced4fb6d1d10662683f6ac610077c1f85df62332ed77` |
| `run/dlb_unit_tests.py` | 3715 | `1946ed8d7dfbf28511fdf1d5ad88e9a8fdc35f227cd3652fd91c1008865c2d26` |
| `run/gen_tables.py` | 3677 | `97e916211eb13ba86931a09018a67fedeb3f9057800aeb320ced257bfba97fab` |
| `run/make_numbers.py` | 3165 | `a03b28ba03b3155b70f779ce31bee821b06415ac17601d5502a62e8ea1f3917b` |
| `run/place.py` | 3369 | `bff91973fc6f9517dcaaed15f5df5d7b2f50f4a76cebde73a3d9a11ccda341aa` |
| `run/post_obs.py` | 3424 | `abe41274f5d8a07294831bf96448e7679dceca4d4014f124ef737bc632a106ad` |
| `run/q4q5.py` | 3906 | `1bca2a8f68eb2608ee676772a9e677bfe767ab939e8f1275913c45593168ec2e` |

## Appendix A — locate scan (L = 2, L_t = 6), every grid point

| β | E hot | E cold | C hot | C cold | C_max |
|---|---|---|---|---|---|
| 0.5000 | 0.75532 | 0.75587 | 0.470 | 0.472 | 0.472 |
| 0.5100 | 0.75086 | 0.75031 | 0.456 | 0.467 | 0.467 |
| 0.5200 | 0.74631 | 0.74613 | 0.464 | 0.475 | 0.475 |
| 0.5300 | 0.74125 | 0.74112 | 0.498 | 0.460 | 0.498 |
| 0.5400 | 0.73666 | 0.73682 | 0.467 | 0.475 | 0.475 |
| 0.5500 | 0.73136 | 0.73158 | 0.479 | 0.484 | 0.484 |
| 0.5600 | 0.72738 | 0.72804 | 0.463 | 0.480 | 0.480 |
| 0.5700 | 0.72286 | 0.72242 | 0.475 | 0.478 | 0.478 |
| 0.5800 | 0.71756 | 0.71862 | 0.468 | 0.462 | 0.468 |
| 0.5900 | 0.71259 | 0.71255 | 0.452 | 0.452 | 0.452 |
| 0.6000 | 0.70763 | 0.70753 | 0.452 | 0.453 | 0.453 |
| 0.6100 | 0.70298 | 0.70353 | 0.480 | 0.462 | 0.480 |
| 0.6200 | 0.69849 | 0.69860 | 0.461 | 0.463 | 0.463 |
| 0.6300 | 0.69420 | 0.69425 | 0.495 | 0.469 | 0.495 |
| 0.6400 | 0.68893 | 0.68861 | 0.481 | 0.492 | 0.492 |
| 0.6500 | 0.68397 | 0.68456 | 0.452 | 0.450 | 0.452 |
| 0.6600 | 0.67966 | 0.68014 | 0.470 | 0.451 | 0.470 |
| 0.6700 | 0.67492 | 0.67482 | 0.463 | 0.458 | 0.463 |
| 0.6800 | 0.67021 | 0.66960 | 0.494 | 0.450 | 0.494 |
| 0.6900 | 0.66530 | 0.66582 | 0.449 | 0.478 | 0.478 |
| 0.7000 | 0.66068 | 0.66047 | 0.464 | 0.476 | 0.476 |
| 0.7100 | 0.65559 | 0.65604 | 0.461 | 0.443 | 0.461 |
| 0.7200 | 0.65069 | 0.65067 | 0.482 | 0.471 | 0.482 |
| 0.7300 | 0.64626 | 0.64626 | 0.455 | 0.497 | 0.497 |
| 0.7400 | 0.64157 | 0.64212 | 0.512 | 0.488 | 0.512 |
| 0.7500 | 0.63709 | 0.63625 | 0.475 | 0.498 | 0.498 |
| 0.7600 | 0.63216 | 0.63187 | 0.482 | 0.471 | 0.482 |
| 0.7700 | 0.62737 | 0.62734 | 0.503 | 0.507 | 0.507 |
| 0.7800 | 0.62141 | 0.62196 | 0.511 | 0.511 | 0.511 |
| 0.7900 | 0.61721 | 0.61763 | 0.481 | 0.471 | 0.481 |
| 0.8000 | 0.61241 | 0.61219 | 0.499 | 0.494 | 0.499 |
| 0.8100 | 0.60663 | 0.60787 | 0.477 | 0.466 | 0.477 |
| 0.8200 | 0.60257 | 0.60310 | 0.491 | 0.507 | 0.507 |
| 0.8300 | 0.59732 | 0.59774 | 0.476 | 0.487 | 0.487 |
| 0.8400 | 0.59241 | 0.59291 | 0.519 | 0.513 | 0.519 |
| 0.8500 | 0.58807 | 0.58779 | 0.490 | 0.506 | 0.506 |
| 0.8600 | 0.58321 | 0.58290 | 0.458 | 0.486 | 0.486 |
| 0.8700 | 0.57803 | 0.57821 | 0.479 | 0.464 | 0.479 |
| 0.8800 | 0.57249 | 0.57268 | 0.521 | 0.527 | 0.527 |
| 0.8900 | 0.56784 | 0.56769 | 0.484 | 0.527 | 0.527 |
| 0.9000 | 0.56244 | 0.56327 | 0.499 | 0.504 | 0.504 |
| 0.9100 | 0.55789 | 0.55809 | 0.485 | 0.498 | 0.498 |
| 0.9200 | 0.55279 | 0.55263 | 0.491 | 0.501 | 0.501 |
| 0.9300 | 0.54662 | 0.54684 | 0.510 | 0.500 | 0.510 |
| 0.9400 | 0.54232 | 0.54179 | 0.514 | 0.531 | 0.531 |
| 0.9500 | 0.53735 | 0.53715 | 0.541 | 0.536 | 0.541 |
| 0.9600 | 0.53256 | 0.53184 | 0.511 | 0.560 | 0.560 |
| 0.9700 | 0.52593 | 0.52745 | 0.510 | 0.502 | 0.510 |
| 0.9800 | 0.52055 | 0.52174 | 0.515 | 0.559 | 0.559 |
| 0.9900 | 0.51640 | 0.51691 | 0.542 | 0.515 | 0.542 |
| 1.0000 | 0.51055 | 0.51074 | 0.566 | 0.515 | 0.566 |
| 1.0100 | 0.50567 | 0.50546 | 0.557 | 0.533 | 0.557 |
| 1.0200 | 0.50069 | 0.49895 | 0.537 | 0.561 | 0.561 |
| 1.0300 | 0.49389 | 0.49414 | 0.522 | 0.543 | 0.543 |
| 1.0400 | 0.48958 | 0.48923 | 0.556 | 0.550 | 0.556 |
| 1.0500 | 0.48455 | 0.48295 | 0.527 | 0.614 | 0.614 |
| 1.0600 | 0.47684 | 0.47744 | 0.582 | 0.590 | 0.590 |
| 1.0700 | 0.47227 | 0.47204 | 0.598 | 0.552 | 0.598 |
| 1.0800 | 0.46561 | 0.46681 | 0.556 | 0.573 | 0.573 |
| 1.0900 | 0.45967 | 0.46065 | 0.606 | 0.595 | 0.606 |
| 1.1000 | 0.45389 | 0.45474 | 0.605 | 0.562 | 0.605 |
| 1.1100 | 0.44831 | 0.44711 | 0.588 | 0.670 | 0.670 |
| 1.1200 | 0.43946 | 0.44164 | 0.652 | 0.609 | 0.652 |
| 1.1300 | 0.43478 | 0.43396 | 0.716 | 0.648 | 0.716 |
| 1.1400 | 0.42894 | 0.42788 | 0.732 | 0.680 | 0.732 |
| 1.1500 | 0.42172 | 0.42095 | 0.657 | 0.699 | 0.699 |
| 1.1600 | 0.41462 | 0.41466 | 0.677 | 0.746 | 0.746 |
| 1.1700 | 0.40749 | 0.40792 | 0.623 | 0.747 | 0.747 |
| 1.1800 | 0.40047 | 0.40018 | 0.794 | 0.779 | 0.794 |
| 1.1900 | 0.39153 | 0.39276 | 0.847 | 0.785 | 0.847 |
| 1.2000 | 0.38336 | 0.38174 | 0.920 | 1.020 | 1.020 |
| 1.2100 | 0.36672 | 0.36970 | 1.693 | 1.861 | 1.861 |
| **1.2200** | 0.34535 | 0.35852 | 2.315 | 1.840 | 2.315 |
| 1.2300 | 0.32035 | 0.31751 | 1.199 | 1.186 | 1.199 |
| 1.2400 | 0.31449 | 0.30961 | 1.298 | 0.873 | 1.298 |
| 1.2500 | 0.29895 | 0.30167 | 0.564 | 0.637 | 0.637 |
| 1.2600 | 0.29609 | 0.29507 | 0.602 | 0.603 | 0.603 |
| 1.2700 | 0.29091 | 0.29032 | 0.503 | 0.519 | 0.519 |
| 1.2800 | 0.28541 | 0.28568 | 0.480 | 0.576 | 0.576 |
| 1.2900 | 0.28078 | 0.28088 | 0.451 | 0.479 | 0.479 |
| 1.3000 | 0.27635 | 0.27893 | 0.393 | 0.491 | 0.491 |
| 1.3100 | 0.27292 | 0.27173 | 0.414 | 0.381 | 0.414 |
| 1.3200 | 0.26889 | 0.26857 | 0.369 | 0.369 | 0.369 |
| 1.3300 | 0.26489 | 0.26491 | 0.331 | 0.312 | 0.331 |
| 1.3400 | 0.26155 | 0.26198 | 0.350 | 0.327 | 0.350 |
| 1.3500 | 0.26589 | 0.25827 | 0.378 | 0.289 | 0.378 |
| 1.3600 | 0.25544 | 0.25491 | 0.324 | 0.304 | 0.324 |
| 1.3700 | 0.25275 | 0.25309 | 0.292 | 0.288 | 0.292 |
| 1.3800 | 0.24975 | 0.24975 | 0.268 | 0.265 | 0.268 |
| 1.3900 | 0.24701 | 0.24665 | 0.273 | 0.246 | 0.273 |
| 1.4000 | 0.24432 | 0.24436 | 0.265 | 0.269 | 0.269 |
| 1.4100 | 0.24191 | 0.24154 | 0.263 | 0.261 | 0.263 |
| 1.4200 | 0.24659 | 0.23903 | 0.264 | 0.250 | 0.264 |
| 1.4300 | 0.23699 | 0.23723 | 0.225 | 0.228 | 0.228 |
| 1.4400 | 0.23436 | 0.23397 | 0.233 | 0.232 | 0.233 |
| 1.4500 | 0.23244 | 0.23279 | 0.219 | 0.233 | 0.233 |
| 1.4600 | 0.22999 | 0.23005 | 0.223 | 0.209 | 0.223 |
| 1.4700 | 0.22810 | 0.22806 | 0.210 | 0.209 | 0.210 |
| 1.4800 | 0.22587 | 0.22602 | 0.195 | 0.201 | 0.201 |
| 1.4900 | 0.22405 | 0.22413 | 0.201 | 0.197 | 0.201 |
| 1.5000 | 0.22196 | 0.22194 | 0.205 | 0.204 | 0.205 |
| 1.5100 | 0.22027 | 0.22020 | 0.191 | 0.187 | 0.191 |
| 1.5200 | 0.21802 | 0.21762 | 0.183 | 0.186 | 0.186 |
| 1.5300 | 0.21607 | 0.21653 | 0.175 | 0.191 | 0.191 |
| 1.5400 | 0.21408 | 0.21429 | 0.176 | 0.174 | 0.176 |
| 1.5500 | 0.21266 | 0.21284 | 0.180 | 0.176 | 0.180 |
| 1.5600 | 0.21080 | 0.21122 | 0.172 | 0.173 | 0.173 |
| 1.5700 | 0.20915 | 0.20945 | 0.170 | 0.173 | 0.173 |
| 1.5800 | 0.20754 | 0.20730 | 0.172 | 0.164 | 0.172 |
| 1.5900 | 0.20577 | 0.20599 | 0.172 | 0.167 | 0.172 |
| 1.6000 | 0.20429 | 0.20396 | 0.157 | 0.165 | 0.165 |
| 1.6100 | 0.20244 | 0.20246 | 0.164 | 0.168 | 0.168 |
| 1.6200 | 0.20138 | 0.20139 | 0.159 | 0.156 | 0.159 |
| 1.6300 | 0.19961 | 0.19935 | 0.150 | 0.150 | 0.150 |
| 1.6400 | 0.19796 | 0.19797 | 0.147 | 0.153 | 0.153 |
| 1.6500 | 0.19679 | 0.19674 | 0.156 | 0.150 | 0.156 |
| 1.6600 | 0.19513 | 0.19525 | 0.142 | 0.143 | 0.143 |
| 1.6700 | 0.19348 | 0.19358 | 0.139 | 0.141 | 0.141 |
| 1.6800 | 0.19227 | 0.19282 | 0.142 | 0.139 | 0.142 |
| 1.6900 | 0.19083 | 0.19117 | 0.129 | 0.138 | 0.138 |
| 1.7000 | 0.18966 | 0.18948 | 0.131 | 0.135 | 0.135 |
| 1.7100 | 0.18826 | 0.18842 | 0.134 | 0.135 | 0.135 |
| 1.7200 | 0.18683 | 0.18687 | 0.134 | 0.125 | 0.134 |
| 1.7300 | 0.19710 | 0.18569 | 0.132 | 0.125 | 0.132 |
| 1.7400 | 0.18417 | 0.18450 | 0.123 | 0.124 | 0.124 |
| 1.7500 | 0.18305 | 0.18282 | 0.119 | 0.119 | 0.119 |
| 1.7600 | 0.18762 | 0.18176 | 0.127 | 0.121 | 0.127 |
| 1.7700 | 0.18050 | 0.18076 | 0.119 | 0.125 | 0.125 |
| 1.7800 | 0.17926 | 0.17933 | 0.117 | 0.115 | 0.117 |
| 1.7900 | 0.17802 | 0.17824 | 0.114 | 0.114 | 0.114 |
| 1.8000 | 0.17692 | 0.17714 | 0.114 | 0.118 | 0.118 |
| 1.8100 | 0.18094 | 0.17594 | 0.114 | 0.110 | 0.114 |
| 1.8200 | 0.17466 | 0.17489 | 0.111 | 0.117 | 0.117 |
| 1.8300 | 0.17373 | 0.17368 | 0.114 | 0.113 | 0.114 |
| 1.8400 | 0.17261 | 0.17250 | 0.107 | 0.105 | 0.107 |
| 1.8500 | 0.17733 | 0.17129 | 0.106 | 0.108 | 0.108 |
| 1.8600 | 0.17572 | 0.17031 | 0.104 | 0.104 | 0.104 |
| 1.8700 | 0.17436 | 0.16923 | 0.094 | 0.100 | 0.100 |
| 1.8800 | 0.16817 | 0.16839 | 0.109 | 0.110 | 0.110 |
| 1.8900 | 0.17311 | 0.16727 | 0.109 | 0.100 | 0.109 |
| 1.9000 | 0.16656 | 0.16635 | 0.104 | 0.104 | 0.104 |
| 1.9100 | 0.16518 | 0.16516 | 0.097 | 0.097 | 0.097 |
| 1.9200 | 0.16427 | 0.16415 | 0.093 | 0.096 | 0.096 |
| 1.9300 | 0.16327 | 0.16330 | 0.100 | 0.099 | 0.100 |
| 1.9400 | 0.16239 | 0.16232 | 0.098 | 0.093 | 0.098 |
| 1.9500 | 0.16149 | 0.16134 | 0.098 | 0.098 | 0.098 |
| 1.9600 | 0.16057 | 0.16046 | 0.094 | 0.093 | 0.094 |
| 1.9700 | 0.16557 | 0.15957 | 0.090 | 0.090 | 0.090 |
| 1.9800 | 0.15869 | 0.15874 | 0.088 | 0.096 | 0.096 |
| 1.9900 | 0.15760 | 0.15759 | 0.082 | 0.091 | 0.091 |
| 2.0000 | 0.16256 | 0.15678 | 0.091 | 0.090 | 0.091 |
