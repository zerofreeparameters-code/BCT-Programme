# Gate DL-BETA — pre-registration card

**Programme:** BCT Cold Ledger — DL construction track ("building the DL theory from scratch").
**Card written:** 12 November 2026, Claude (Opus 5.5), at Michel's request ("Yes"), in the thread
that ran Gate DL-STIFF, after that gate's deliverable had been produced.
**Status:** PRE-REGISTERED, NOT RUN. No Monte Carlo has been run at any β in [0.2, 5] on any lattice
in the card thread (§7).
**Type:** numerical measurement. Its verdicts are about the measurement's integrity, as in Gate LATT
§6, not about a theory. Item 2 of the DL scoping note's §5 sequence.
**Depends on:** Gate DL (the construction; CN-DL-01/04/05/06), Gate LATT (conventions, §2), Gate CRIT2
(checks §4 and method §5), the DL scoping note §5. **Independent of Gate DL-STIFF** — see §0.

---

## 0. A note on Gate DL-STIFF, read first

This card was written in the thread that ran Gate DL-STIFF. **That gate's result is deliberately not
stated anywhere in this card.** Its blind replication has not yet run, it will run inside the same
claude.ai Project, and this card may be mirrored there. Nothing below depends on DL-STIFF's result:
β_c is a property of the lattice and the action, whatever does or does not fix β. The one place this
card touches DL-STIFF is a convention in DL-STIFF's *card* (§6.3), which is pre-registration material
and already public.

## 1. Background (stated, not a result of this card)

**The construction.** Gate DL (15 Sep 2026) put a compact U(1) link field on the FCC void network —
nodes = octahedral and tetrahedral voids, links = the triangular windows between them — with the
Wilson action and Gauss's law at the nodes, the superfluid neutral under it. The neutral medium gives
no Meissner mass (CN-DL-02, PROVEN); the network is loop-rich and isotropic (CN-DL-01/04, PROVEN).
What DL left open is the phase: in (3+1)D the theory has a massless photon only in its Coulomb phase,
**β > β_c** (CN-DL-06). **No measurement of β_c on this lattice is known; this gate makes one.**
LATT's prior-art search
(§0 there) found none on any non-hypercubic 4D lattice beyond CRIT's D4. A two-query check on
12 Nov 2026 found 4D compact U(1) on hypercubic tori and on spherical and other non-toroidal lattices
(Jersák–Lang–Neuhaus, hep-lat/9606013; Campos–Cruz–Tarancón, hep-lat/9803007; Lang–Neuhaus,
hep-lat/9407005), and nothing on the FCC void network or the rhombic-dodecahedral honeycomb. That
check is not exhaustive.

**Why it is a new number.** Gate LATT (card 11 Oct 2026, run 17 Oct, SC-LATT-1 per `audit/NEXT.md`,
result not in the tree) compared compact U(1) on Z4, D4, A4 and F4, all root lattices with one site per
cell. The void network × time is not a root lattice: two node types, two link types, two loop types.
LATT §1: "Any lattice added later is a separate gate." This is that gate, under LATT's conventions.

**What the card thread established before registering (§7, `dlb_deskcheck.py`, 49 assertions).**

- **The loops are forced, not chosen.** The 4-cycles of the void graph are exactly the rhombic faces
  of the FCC Voronoi tessellation (the rhombic-dodecahedral honeycomb), one per nearest-neighbour bond,
  6 per primitive cell. There are no 3-cycles (the graph is bipartite) and no other 4-cycles. The
  rhombi span every contractible cycle (rank ∂₂ = 5N − 2), and V − E + F − C₃ = 3 − 8 + 6 − 1 = 0: the
  void network with its rhombi is a genuine cellulation of space. With time added, the smallest loops
  are the rhombi plus one temporal square per spatial link, and nothing else (for L ≥ 2, L_t ≥ 5).
- **Counts per primitive cell per time slice:** 3 nodes, 11 links (8 spatial, 3 temporal), 14 loops
  (6 rhombi, 8 squares). Each spatial link lies in 5 loops; a temporal link in 8 (oct) or 4 (tet). Mean
  loops per link 56/11 = 5.0909, against 6 (Z4) and 8 (D4).
- **Normalisation.** With every smallest loop at the same β (β_t = β_s, LATT's convention), the
  classical continuum limit is Euclidean-invariant when one time step is **a_t = a/(2√2)**, and then
  **1/e² = k·β with k = 1/√2**. The method reproduces k = 1 (Z4) and k = 2 (D4, the value CRIT2's card
  states) before it is applied here.
- **Modes.** Of the 11 link modes per cell, 3 are gauge, 3 are acoustic (the long-wavelength A_μ
  modulo gauge, which carry the photon's two polarisations) and **5 are optical**: the loop map has
  rank 5 at zero crystal momentum, so those 5 cost action at k = 0 and are gapped at the lattice scale
  at tree level. This is the tree-level content of CN-DL-05, which DL left at CONJECTURE.

## 2. Questions

1. **The complex (Q1).** Build the (3+1)D complex from §4.2's specification, independently, and
   reproduce the desk check's counts, incidences, ranks, zero-momentum rank, a_t and k (§4.3, K1).
2. **The code (Q2).** Pass the correctness checks and the Z4 calibration (§4.3, K2–K5).
3. **β_c (Q3).** Measure β_c on the void network × time by CRIT2's method (§4.4): β_∞ with its
   uncertainty, in the card convention and as 1/e²_c = β_∞/√2.
4. **Order (Q4).** The three diagnostics of LATT §4.5, adapted (§4.4 step 7). Reported, not a verdict
   input.
5. **Anisotropy record (Q5).** E_s (rhombi) and E_t (temporal squares) separately, their ratio either
   side of β_∞ and at β = 20. Recorded, not interpreted (the CN-QED-09 echo of the scoping note §5).
6. **Placement (Q6).** β_∞ against Z4 and D4 in both normalisations; the §9 heuristics scored; the
   programme's candidate number placed for orientation (§6). After the §4.6 hash, never before.

## 3. Choices made by the analyst, and what they cost

- **β_t = β_s** (every smallest loop at one β; LATT §2). Cost: the space–time anisotropy is fixed by
  convention. At this convention light speed 1 corresponds to a_t = a/(2√2). Another ratio gives
  another β_c; none is run.
- **L_t = 3L.** Then L_t·a_t = 1.06·L·a, so the 4-box is physically isotropic to 6 %. Cost: finite-size
  values depend on the aspect ratio; β_∞ should not.
- **Loops = smallest loops.** No cost: §1 shows there is no choice once "smallest loops" is fixed.
- **Mixed-phase start split in time** (cold for t < L_t/2). Cost: the interface is a spatial slice; a
  spatial split would cut the network unevenly and is not used.
- **No D4 regression** (LATT required one). The void complex's loops are 4-cycles, like Z4's; the
  triangle code path is not exercised. Cost: one fewer cross-check of the code.
- **Sizes L ∈ {2, 4, 6, 8}.** The largest box (540,672 links) is comparable to CRIT2's D4 L = 16
  (393,216). Cost: two mixed-phase sizes, as in CRIT2; LATT used three.
- **Out of scope:** other actions (Villain), other gauge groups, monopole observables, the continuum
  limit, the value of β in the DL theory, and anything about α.

## 4. Fixed rules

### 4.1 Sources, pinned

Repository `zerofreeparameters-code/BCT-Programme` at the pre-registration commit (the commit that adds
this card; its SHA is given in the run prompt). Every source below other than the card's own two files
is byte-identical to its version at `9993a2381cdbdd8604975f285644aabb94063325`. **Verify every hash
before reading the file.**

| File | SHA-256 | used for |
|---|---|---|
| `audit/gates/gate_LATT_prompt.md` | 1dccde5b3160121d2297f5de906aeb787ceeda9ddfd933e162b9385e7cb45cdd | conventions §2, order diagnostics §4.5 |
| `audit/gates/gate_CRIT2_prompt.md` | b30436875a2b12ea9b38a4d5d366c1ab9fcad83bcfe0405b3af5974876df4c79 | checks §4, method §5 |
| `audit/gates/CRIT2/gate_CRIT2_RESULT.md` | 25b2653cb4623897b33d84e62141cd377bf301237a314516ef7b7117e08c09ce | Z4 reference values; D4 β_∞ for §6 |
| `audit/gates/DL/gate_DL_RESULT.md` | 3eff786202696bd1613187bdb35c3ac2b9a9918a27138995999b6a90d3c128b4 | the construction |
| `audit/gates/DL/gate_DL_step0_network.py` | 7935f7e7a8a784c03c3465349a539d3fce95665957009a6b88d4b9b93874a4ee | the network, reusable |
| `audit/scoping/DL_scoping_2026-11-12.md` | fede02d1514563e11d30c05aa136a416b38cdd40ab1d6af15e95d7b8009f8a65 | origin (§5 item 2), forecast (§7) |
| `audit/gates/gate_DLSTIFF_prompt.md` | 294da0f50c5d740956bb0b3d64871f580a00f454a0f541701467bba47ee48e21 | **§1 only**: the candidate number and its convention, for §6.3 |
| `audit/gates/DLBETA/dlb_deskcheck.py` | 93de5d29f05c25b57fad8e7b37c6994958215b229b241188efeb1c2402407d71 | card-thread desk check (§7) |
| `audit/gates/DLBETA/dlb_deskcheck_output.txt` | 10d58dbbb45d3c118880d1f437c38166f946e66772152d613011fe765fc150ae | its output: the targets of K1–K3 |

Literature: Arnold, Lippert, Neuhaus, Schilling, hep-lat/0210010 (Z4, β_c = 1.0111331(21)).
**Nothing else** from the repository, the Project, past chats or memory. In particular, nothing under
`audit/gates/DLSTIFF/`: that directory is not a source of this gate.

### 4.2 The model (specification for the run's own code)

Written in the run thread from this specification. `pip install numba` is allowed.

- **Space.** Conventional FCC cube a = 1; integer coordinates in units of a/4; periodic box of side
  4L. Atoms at 4·(i, j, k) + {(0,0,0), (2,2,0), (2,0,2), (0,2,2)}. Octahedral voids at atom + (2,2,2);
  tetrahedral voids at atom + (1,1,1) and atom + (3,3,3), all mod 4L.
- **Spatial links.** One per oct–tet pair at offset (±1, ±1, ±1), oriented oct → tet.
- **Rhombi.** For each atom A and each b ∈ {(2,2,0), (2,−2,0), (2,0,2), (2,0,−2), (0,2,2), (0,2,−2)}: the
  two octs A + o, o ∈ {±2eᵢ}, with |o − b|² = 4, and the two tets A + t, t ∈ {(±1,±1,±1)}, with
  |t − b|² = 3, taken in the cyclic order O₁ → T₁ → O₂ → T₂ → O₁.
- **Time.** L_t = 3L slices, periodic. A temporal link (v, t) → (v, t + 1) at every node and slice. For
  every spatial link u → w and slice t, the temporal square u(t) → w(t) → w(t+1) → u(t+1) → u(t).
- **Action.** S = β Σ_loops (1 − cos θ_loop), θ_loop the oriented sum of its link angles.
- **Update.** Sequential single-link heat bath; the conditional law of a link is
  exp(βR cos(θ + φ)), sampled exactly (von Mises). **One sweep = one update of every link in a fixed
  storage order**, chosen and recorded in code before the first run. No overrelaxation. Hot start =
  uniform phases; cold start = all zero.
- **Observables, every sweep.** E = mean of (1 − cos θ_loop) over all loops; E_s over rhombi; E_t over
  temporal squares; C = N_loops · var(E) over the measurement sweeps. Errors: 20 blocks; C by block
  jackknife (reporting only).
- **Seeds.** Z4: CRIT2's rule, seed = 7919·L + round(10⁴·β) + s. Void: the same plus 500,000.
  s = 0 hot, 1 cold, 2 mixed, 3 histogram. Every seed printed in the raw records.
- **Z4** (calibration only): Z⁴, square plaquettes, the same action and update.

### 4.3 Checks the code must pass before any void number is used

**The run builds its complex and records its own K1 numbers before it reads or runs
`dlb_deskcheck.py`** (it may read `dlb_deskcheck_output.txt` at any time: those numbers are the
targets). After recording them it runs the desk check as a cross-check.

- **K1 — complex.** At L = 2 and 3 (space) and L = 2, L_t = 6 (space × time): every count and
  incidence of §1; every 4-cycle of the void graph is a rhombus; rank ∂₂ = 5N − 2 (space) and
  N_l − N_v − 3 (space × time); rank 5 at zero crystal momentum on the 11 link classes; a_t = a/(2√2)
  and k = 1/√2 by the constant-F method, with the same method returning k = 1 on Z4.
- **K2 — local correctness.** Gauge invariance of every cos θ_loop under a random gauge transformation
  (void L = 2, L_t = 6; Z4 L = 4), and the local staple ΔS equal to the global recompute.
- **K3 — limits**, 1000 + 10,000 sweeps: at β = 0.1, hot, ⟨cos θ_loop⟩ = I₁(0.1)/I₀(0.1) = 0.049938
  within 2 %; at β = 20, cold, E = rank ∂₂/(2β N_loops) within 2 % (void L = 2, L_t = 6: 0.014258;
  Z4 L = 4: 0.012451).
- **K4 — Z4 transition:** CRIT2 card §4 check 3, verbatim (L = 8, β = 0.995 to 1.020 step 0.0025, hot
  and cold, 1000 + 3000 sweeps; the C maximum in [1.000, 1.012]; E*_hc as defined there).
- **K5 — Z4 mixed phase:** CRIT2 card §4 check 4, verbatim (L = 12; the flip interval contains a point
  within 0.006 of 1.0111).

If K2–K5 fails: **SC-DLB-0**, stop, report. If K1 disagrees with the desk check, the run runs the desk
check and determines which is wrong; a coding error in the run is fixed and K1 repeated; an error in the
desk check is **SC-DLB-4**, stop, report.

### 4.4 Void runs (CRIT2 §5, adapted)

1. **Locate** (L = 2, L_t = 6). Hot and cold, β = 0.50 to 2.00 step 0.01, 500 + 2000 sweeps. β₀ = grid
   point with the largest C (larger of hot and cold). If β₀ is within 0.05 of an edge, extend the scan
   by 0.25 on that side, never below 0.20 or above 4.00, and repeat. No interior C maximum in
   [0.20, 4.00]: **SC-DLB-3**, stop, report.
2. **Fine scan** (L = 4, L_t = 12). Hot and cold, β₀ − 0.050 to β₀ + 0.050 step 0.005, 2000 + 4000
   sweeps. β₄ = grid point with the largest C. Jump interval for each start = adjacent pair with the
   largest fall in E. If β₄ is at an edge, extend by 0.005 steps until it is not.
3. **Cold scan** (L = 6, L_t = 18). Cold, β₄ − 0.020 to β₄ + 0.020 step 0.005, 500 + 1500 sweeps.
   Jump interval (L = 6) as above. **E\*** = mean of E at its two ends.
4. **Mixed-phase starts** (L = 6 and L = 8; L_t = 18 and 24). Initial state: every link whose origin
   node has time t < L_t/2 set to θ = 0, every other link uniform. E recorded every 50 sweeps; outcome
   from the mean of the 10 readings at sweeps 1550–2000: **weak wins** if below E* by more than 0.01,
   **strong wins** if above E* by more than 0.01, **unresolved** otherwise.
   - L = 6: midpoint of the L = 6 jump interval ± 0.0075, step 0.0025 (7 points), 2000 sweeps.
   - **β_mix(L)** = midpoint between the highest β where strong wins and the lowest β where weak wins;
     unresolved points between them widen the interval; report its ends.
   - L = 8: β_mix(6) ± 0.005, step 0.0025 (5 points), 2000 sweeps.
   - If the outcome does not flip inside a grid: no weak win → one 0.0025 step above; no strong win →
     one step below; at most 8 extensions per size, then stop that size and report.
5. **Result.** **β_∞ = β_mix(8).** Uncertainty = the larger of half the L = 8 flip interval and
   |β_mix(8) − β_mix(6)|. **1/e²_c = β_∞/√2.** ΔE(L = 8) = end-state E of the nearest strong-win run
   below β_∞ minus that of the nearest weak-win run above it. Check, not headline: the straight line
   through (1/(L³L_t), β_mix(L)) for L = 6, 8, evaluated at 0.
6. **Histogram** (L = 6, L_t = 18) at β = β_mix(6): mixed start, 2000 + 20,000 sweeps, seed s = 3. E
   histogram (50 bins) and B = 1 − ⟨E⁴⟩/(3⟨E²⟩²).
7. **Order (Q4)**: (a) hysteresis at L = 4 — the hot and cold jump intervals differ, or hot and cold E
   differ by more than 3σ at some grid point; (b) the jump at L = 4 (cold), L = 6 (cold scan) and
   ΔE(L = 8) — does it shrink by more than 30 % from L = 4 to L = 8; (c) two peaks in the step-6
   histogram. **First-order** if (a) and (c) hold and (b) shrinks by no more than 30 %; otherwise
   **order undetermined**. Reported, not a verdict input.

### 4.5 Budget

From the desk check's timings (reference code, numba, one simulation per core):

| stage | sweeps | ms/sweep | core-minutes |
|---|---|---|---|
| K4 (Z4 L = 8) | 88,000 | 7.5 | 11 |
| K5 (Z4 L = 12) | 10,000 | 37.7 | 6 |
| locate (L = 2) | 755,000 | 0.92 | 12 |
| fine scan (L = 4) | 252,000 | 15.2 | 64 |
| cold scan (L = 6) | 18,000 | 74.3 | 22 |
| mixed L = 6 | 14,000 | 74.3 | 17 |
| mixed L = 8 | 10,000 | 241.7 | 40 |
| histogram (L = 6) | 22,000 | 74.3 | 27 |
| **total** | | | **≈ 200 (3.3 core-hours)** |

About 2 to 4 hours of wall time on 2 cores, plus any grid extensions. Run under `nohup`, checkpoint to
disk after every stage, resumable. **Do not shorten any sweep budget to fit a session.**

### 4.6 Hash, then place

Write every Q3 number (β₀, β₄, the jump intervals, E*, β_mix(6) and its interval, β_mix(8) and its
interval, β_∞, its uncertainty, 1/e²_c, ΔE) to `dlb_numbers.txt`, and record its SHA-256 in the
deliverable **before** computing anything in §6.

### 4.7 Conventions

β is the coefficient of Σ_loops (card convention, LATT §2). 1/e² = kβ with k = 1 (Z4), 2 (D4),
1/√2 (void × time at β_t = β_s). Numbers to 4 decimals for β, 5 for E.

## 5. Verdict codes

- **SC-DLB-0 (method failed).** A K2–K5 check failed. No void number. Re-run after the fix under a new
  digest.
- **SC-DLB-1 (measured).** Checks pass; the L = 8 mixed-phase outcome flips with at most one
  unresolved point; uncertainty ≤ 0.010. β_∞ stands at **CONJECTURE** (same-session cap) until a
  blind replication.
- **SC-DLB-2 (located, not resolved).** Checks pass; the transition is located at L = 4 and 6 (C peak
  and E jump) but the L = 8 mixed-phase method does not resolve within the extension limit, or the
  uncertainty exceeds 0.010. β_c is reported as the L = 6 jump interval widened by the L = 4 → 6 shift.
- **SC-DLB-3 (no transition signal in [0.20, 4.00]).** Reported as found. Not expected: the strong- and
  weak-coupling regimes differ qualitatively on any 4D complex of this kind.
- **SC-DLB-4 (card defect).** The desk check's geometry is wrong (§4.3). The gate is unposable as
  specified.

**What the number decides.** With the DL construction's coupling β, the photon is massless iff
β > β_∞ (CN-DL-06, now with a number). That statement holds whether β is a free input or fixed by
something; which of those is true is not this gate's question.

## 6. Placement (Q6; after §4.6, never before)

**6.1 Against the other lattices.**

| lattice | β_c (card) | k | 1/e²_c | source |
|---|---|---|---|---|
| Z4 | 1.0111 | 1 | 1.0111 | Arnold et al.; CRIT2 K4/K5 |
| D4 | 0.6150 ± 0.00125 | 2 | 1.2300 | CRIT2 (β_∞ from one code; its L = 8 interval replicated across two) |
| **void × time** | **β_∞** | **1/√2** | **β_∞/√2** | this gate |

**6.2 The §9 heuristics,** each scored hit or miss by whether β_∞ ± its uncertainty meets the interval.

**6.3 The programme's candidate number, for orientation only.** The DL-STIFF card (§1) names
β_geom = 2ξ²/a² = 10.742018 under its own convention β = 1/e² (its §4.4), which is the k = 1
normalisation. On this complex k = 1/√2: a Wilson β of 10.742018 here means 1/e² = 7.595754, and the
Wilson β whose 1/e² is 10.742018 is 15.191508. Report β_geom/β_∞ and 15.191508/β_∞. **This is a
statement about a convention in that card, not about that gate's result.** Whether anything fixes β
is DL-STIFF's question; this gate rescores nothing.

## 7. Validation already done (why the card is not blind to the arithmetic)

`dlb_deskcheck.py` (SHA-256 93de5d29…07d71, 24,081 B), output `dlb_deskcheck_output.txt` (SHA-256
10d58dbb…150ae, 6,822 B), 12 Nov 2026, card thread; Python 3.13, NumPy 2.5.3, SciPy 1.18.1, numba
0.68.1; **49 assertions, all passed**.

- **A — space.** At L = 2 and 3: V = 3N, E = 8N, rhombi = 6N, 3-cells = N; degrees 8 (oct) and 4 (tet);
  bipartite; every rhombus a closed O–T–O–T 4-cycle of existing links, planar, area a²/(4√2), normal
  along its bond; the 4-cycles of the graph are exactly the rhombi (192 at L = 2, 648 at L = 3); every
  link in 3 rhombi; rank ∂₂ = 5N − 2 (158, 538); χ = 0.
- **B — space × time** (L = 2, L_t = 6): N_v = 576, N_l = 2112, N_loops = 2688; incidences 5 / 8 / 4;
  rank ∂₂ = 1533 = N_l − N_v − 3; rank 5 at zero crystal momentum.
- **C — normalisation.** Z4: c_E = c_B = 1, k = 1. D4: 32 triangles per site, c_E = c_B = 2, k = 2.
  Void: c_E(a_t = 1) = 2, c_B(a_t = 1) = 1/4, so a_t = a/(2√2) = 0.3535533906 and k = 1/√2 =
  0.7071067812. (a/(2√2) is numerically the radius of the touching FCC spheres; no physical weight is
  attached to that, and it is recorded so nobody later "discovers" it.)
- **D — reference simulator** (sequential heat bath, numba), **β = 0.1 and 20 only**:

| lattice | check | measured | target | deviation |
|---|---|---|---|---|
| void L = 2, L_t = 6 | gauge invariance | 4.1 × 10⁻¹⁵ | 0 | — |
| void | local vs global ΔS | 7.4 × 10⁻¹³ | 0 | — |
| void | β = 0.1 hot ⟨cos⟩ | 0.049804 ± 0.000133 | 0.049938 | −0.27 % (−1.0σ) |
| void | β = 20 cold E | 0.014369 ± 0.000005 | 0.014258 | +0.78 % |
| void | β = 20 E_s, E_t | 0.014668, 0.014145 | — | E_t/E_s = 0.9643 |
| Z4 L = 4 | β = 0.1 hot ⟨cos⟩ | 0.049974 ± 0.000144 | 0.049938 | +0.07 % (+0.3σ) |
| Z4 L = 4 | β = 20 cold E | 0.012531 ± 0.000005 | 0.012451 | +0.64 % |

  The Z4 value at β = 20 agrees with CRIT2's independent 0.012526 ± 0.000007 (0.6σ). The positive
  weak-coupling deviations on both lattices are the expected higher-order correction.
- **E — timing** at β = 20: §4.5.
- **Blindness.** No Monte Carlo was run at any β in [0.2, 5] on any lattice. The author has read
  CRIT2's published Z4 and D4 data (a pinned source) and nothing near any transition on this complex.

## 8. No-fit clause

- No lattice, size, convention, grid, sweep count, seed rule, estimator, threshold or tolerance may
  change after the run starts. Grid extensions only as written in §4.4.
- A first-order call is an observation, not a verdict input.
- Same-session results are capped at CONJECTURE.

## 9. Analyst's disclosure

**Forecasts, to be scored.**

- **Verdict:** SC-DLB-1 75 %; SC-DLB-2 15 %; SC-DLB-0 8 %; SC-DLB-3 or -4 2 %.
- **β_∞ (card convention):** in [1.00, 1.30], 55 %; in (1.30, 1.80], 30 %; below 1.00, 10 %; above
  1.80, 5 %. Central guess 1.15. So **β_∞ above Z4's 1.0111, at about 85 %** (what those four bins
  imply, spreading each uniformly): the void complex has
  fewer loops per link (5.09 against 6), so each link is less constrained and needs a larger β to order.
- **Three heuristics, each calibrated on Z4 and D4 and scored in §6.2:**
  - **H1** — the transition sits at a fixed weak-coupling loop fluctuation ⟨θ²⟩ = (rank/N_loops)/β:
    Z4 gives 0.4945, D4 0.5589, so the void interval is **[1.0223, 1.1555]**.
  - **H2** — the transition sits at a fixed continuum coupling 1/e²_c: Z4 1.0111, D4 1.2300, so the
    void interval is **[1.4299, 1.7395]**.
  - **H3** — β_c × (loops per link) is fixed: Z4 6.0666, D4 4.9200, so the void interval is
    **[0.9664, 1.1917]**.
  The author's central guess follows H1 and H3. H2 is the live alternative, and the gate separates it
  from the other two.
- **The scoping note's forecast** (§7 there, a different analyst, recorded for scoring too): "β_c for
  the void network somewhere between the D4 and hypercubic values", i.e. 0.615 to 1.011. The author of
  this card forecasts against it.
- **Order:** "first-order" by §4.4 step 7, 50 %; "order undetermined", 50 % (LATT reported "order
  undetermined" for its table).
- **E_t/E_s near β_∞:** within 10 % of 1.

**Interest.** The author ran Gate DL-STIFF in this thread (result withheld, §0). After that gate was
delivered, the author read two unpinned files at Michel's request, recorded in the post-gate note in
that gate's directory; neither bears on β_c. The author has no stake in the number. Its programme value
is the same whatever it is: it turns CN-DL-06 into a statement with a number in it.

## 10. Known limitations

- Wilson action only; β_t = β_s only; one spatial complex; bare couplings.
- Compact U(1) in 4D has no interacting continuum limit at the transition. β_c is a lattice quantity,
  and k is a tree-level normalisation.
- Two mixed-phase sizes. The method assumes a first-order transition; if it is continuous or very weak,
  outcomes near β_c are unresolved and SC-DLB-2 records an interval. That is reported, not repaired.
- The 5 optical modes per cell are a tree-level statement; whether they reorganise near β_c is not
  examined.

## 11. Run protocol

- Fresh thread inside the BCT Project. Before opening it, switch off "Search and reference past chats"
  and "Generate memory from chats"; switch them back on afterwards. One gate per thread.
- Fetch this card by commit-pinned raw URL with `curl` to disk; hash it and compare with
  `audit/gates/PREREG_20261112_DLBETA.sha256` **before reading it**. Record the digest and the commit.
- Get the repository at the pre-registration commit (a single-commit `git fetch --depth 1` is
  sufficient and preferred); verify every §4.1 hash before reading any source.
- Q1 first (and record its numbers before opening `dlb_deskcheck.py`), then Q2's checks; then the §4.4
  stages in order; then the §4.6 hash; then Q4–Q6.
- Deliverable: `audit/gates/DLBETA/gate_DLBETA_RESULT.md` with the K-check table, every stage table,
  β₀, β₄, the jump intervals, E*, β_mix(6), β_mix(8), β_∞ (both normalisations), ΔE, the SHA-256 of
  `dlb_numbers.txt`, the order diagnostics, the Q5 record, the §6 placement, the verdict, the §9
  forecasts scored item by item, correction notices CN-DLB-nn, and a plain-language summary. The code,
  the raw time series (JSONL or npz, hashed), and a copy of the as-run prompt. The session cannot push:
  deliver a `git format-patch` bundle adding `audit/gates/DLBETA/` only.
- Same-session results are capped at CONJECTURE.
