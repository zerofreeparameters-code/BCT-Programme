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

<!--TABLE:K3-->

The Z4 value at β = 20, 0.012526 ± 0.000007, is identical to CRIT2's independent 0.012526 ± 0.000007
and 0.6σ from the desk check's 0.012531 ± 0.000005. The void value is 1.6σ from the desk check's
0.014369 ± 0.000005. The weak-coupling deviations are positive on both lattices (+0.70 %, +0.60 %), as
the card expects.

**K4** — Z4, L = 8, hot and cold, 1000 + 3000 sweeps (CRIT2 card §4 check 3):

<!--TABLE:K4-->

C maximum at **β = 1.0050** (hot start, C = 13.81 ± 2.16), inside the required [1.000, 1.012].
**Pass.** Largest fall in E, cold start: [1.0075, 1.0100] (0.38271 → 0.34436, fall 0.03834).
**E\*_hc = 0.36353.** CRIT2's code found its C maximum at 1.0075, its cold jump at [1.0050, 1.0075]
and E\*_hc = 0.38074. The two codes' cold jumps sit in adjacent steps. Near 1.005–1.0075 the L = 8
runs move between phases here (C = 7.7–13.8), which is what makes the step uncertain at this size.

**K5** — Z4, L = 12, mixed starts, 2000 sweeps (CRIT2 card §4 check 4):

<!--TABLE:K5-->

Flip interval **[1.007, 1.012]** (β_mix 1.0095), monotonic, no unresolved point. It contains 1.0111.
**Pass.** This is CRIT2's interval exactly.

## 4. Void runs (card §4.4)

### 4.1 Locate — L = 2, L_t = 6, β 0.50 to 2.00 step 0.01, hot and cold, 500 + 2000 sweeps

Full table in Appendix A. **β₀ = 1.22** (hot start, C = 2.315 ± 0.205; cold 1.840 at the same point),
interior (0.72 from the lower edge, 0.78 from the upper), so there was no extension. The scan has a
single C peak, at 1.21–1.22. E falls by about 0.063 across 1.20–1.23 from both starts. C is 0.45–0.57
across 0.50–1.00, 0.20–0.27 across 1.40–1.50 and 0.09–0.10 near 2.00.

### 4.2 Fine scan — L = 4, L_t = 12, β₀ ± 0.050 step 0.005, hot and cold, 2000 + 4000 sweeps

<!--TABLE:S2-->

- **β₄ = 1.250** (hot start, C = 4.08 ± 0.69). Interior; no extension.
- **Jump interval (L = 4), hot: [1.250, 1.255]**, E 0.32567 → 0.30919 (fall 0.01649).
- **Jump interval (L = 4), cold: [1.250, 1.255]**, E 0.32984 → 0.30517 (fall 0.02466).

C is large at both 1.250 and 1.255 (hot 4.1 and 3.4). The L = 4 runs there move between the phases,
and hot and cold agree to within 2.2σ at every grid point.

### 4.3 Cold scan — L = 6, L_t = 18, β₄ ± 0.020 step 0.005, cold, 500 + 1500 sweeps

<!--TABLE:S3-->

**Jump interval (L = 6): [1.250, 1.255]**, E 0.33292 → 0.31530 (fall 0.01762); the next step,
[1.255, 1.260], falls 0.01488. The cold start at 1.255 part-melted (E = 0.31530, between the branches,
C = 3.89). **E\* = 0.32411.**

### 4.4 Mixed-phase starts — L = 6, L_t = 18, 1.2525 ± 0.0075 step 0.0025, 2000 sweeps

<!--TABLE:S4_L6-->

**β_mix(6) = 1.25375**, flip interval **[1.2475, 1.2600]**, monotonic. The four points 1.2500, 1.2525,
1.2550 and 1.2575 are unresolved, inside the interval. No extension.

### 4.5 Mixed-phase starts — L = 8, L_t = 24, β_mix(6) ± 0.005 step 0.0025, 2000 sweeps

<!--TABLE:S4_L8-->

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

<!--FILES-->

## Appendix A — locate scan (L = 2, L_t = 6), every grid point

<!--TABLE:S1-->
