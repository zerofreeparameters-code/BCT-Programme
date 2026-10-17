# Gate LATT — pre-registration

**Compact U(1) gauge theory on four-dimensional lattices beyond the hypercube: critical coupling and transition order as a function of lattice geometry.**

Drafted 11 Oct 2026 for M. R. Cabrié by Claude (Fable 5.1), warm thread. Status: PRE-REGISTERED, UNRUN. Commit to `audit/gates/gate_LATT_prompt.md`, digest in `audit/gates/PREREG_20261011_LATT.sha256`, run in a fresh thread with memory paused. One gate per thread. Deliverable is the data section of a Letter, not a BCT verdict.

---

## 0. Purpose and status of the question

Gates CRIT (8 Oct 2026, β_c = 0.610 ± 0.005, L ≤ 8) and CRIT2 (8 Oct, blind replication, β_∞ = 0.6150 ± 0.00125 at L = 12 and 16, mixed-phase method, first-order) measured the confinement–deconfinement coupling of compact U(1) with the Wilson action on the D4 root lattice. The prior-art search in `gate_CRIT_prompt.md` (Celmaster 1982–87 SU(N) only; all 52 INSPIRE citers; Katz & Nógrádi 2026 SU(3) on the same lattice) and a fresh search on 11 Oct 2026 found no published U(1) result on D4 or on any non-hypercubic four-dimensional lattice. The compact-QED literature through Cuteri et al. 2024 (arXiv:2404.15907, tricriticality) is hypercubic.

This gate turns the single D4 number into a comparison: the same theory, the same action, the same code, on a fixed list of 4D lattices, with the hypercubic value as the calibration anchor. The physics question is how β_c and the transition order depend on lattice coordination and symmetry. **No BCT claim is in scope.** The D4 lattice is one row of a table; the ledger has already found (Gate D4) that it is not BCT's physical lattice, and CRIT closed the 1/137 route.

## 1. What is fixed before the run

Sections 2–6. Digest of this file is the record. Lattices, sizes, sweep budgets, observables, the calibration pass criterion and the reporting format are not changed after the digest. Any lattice added later is a separate gate.

## 2. Theory and conventions (unchanged from CRIT2)

- Compact U(1), Wilson action on the smallest closed loops of each lattice: S = β Σ_loops (1 − cos θ_loop). Periodic boundaries. Sequential single-link heat bath, one sweep = one update of every link in storage order, no overrelaxation. Hot start = uniform random phases; cold start = all zero.
- β is the card convention of CRIT/CRIT2 (coefficient of the sum over loops). Report alongside the Katz–Nógrádi convention where the lattice has one (D4: β_KN = 2β) and the continuum normalisation 1/e² = k·β with k stated per lattice.
- Observables: mean action per loop E; specific heat C from the block jackknife of E (20 blocks); for the mixed-phase method, E after 250 … 2000 sweeps from a half-ordered/half-disordered start as in CRIT2 §5.4.

## 3. Lattices (fixed list, in run order)

| id | lattice | sites per cell | coordination (links per site) | smallest loop | loops per link | why |
|---|---|---|---|---|---|---|
| Z4 | hypercubic | 1 | 8 | square (plaquette) | 6 | calibration; literature β_c known |
| D4 | D4 root lattice (16-cell honeycomb, Celmaster's "BCT") | 1 (even-sum points of Z⁴) | 24 | triangle | 8 | CRIT/CRIT2 value; the new number |
| A4 | A4 root lattice (4-simplex honeycomb) | 1 | 20 | triangle | computed and asserted by the code | second non-hypercubic lattice; CRIT validated A4 geometry |
| F4 | F4 root lattice (24-cell honeycomb) | 1 | 24 (same count as D4, different symmetry) | triangle | computed and asserted | distinguishes "coordination 24" from "D4 symmetry" |

The code must build each lattice from its root-vector definition, count links per site and loops per link, and assert the counts printed above (A4 and F4 loops-per-link are to be computed by the code and recorded; the run halts if a count differs from the integer the code derives in its own self-check). Lattices not on this list are not run.

## 4. Protocol per lattice (CRIT2 §5, applied identically)

1. **Locate** (L = 4): β scan 0.30 to 1.30 step 0.01, hot and cold, 500 + 2000 sweeps. Record the hysteresis interval if any.
2. **Fine scan** (L = 8): β₀ ± 0.030 step 0.005, hot and cold, 2000 + 4000 sweeps. Record the jump interval and whether any run tunnels.
3. **Mixed-phase** (L = 12, 16, and **20**): β around the L = 8 midpoint, step 0.0025, 2000 sweeps from a half/half start; outcome = which phase takes over. β_mix(L) = midpoint of the flip interval. **L = 20 is new relative to CRIT2** and is what a referee will ask for.
4. **Infinite-volume estimate**: β_∞ from β_mix(12), β_mix(16), β_mix(20), reported three ways: the L = 20 value with half-grid-step uncertainty (CRIT2's convention), a linear fit in 1/L⁴, and a linear fit in 1/L² (first-order transitions scale as the volume; both fits reported so the reader can see the sensitivity). The headline value is the L = 20 mixed-phase value; the fits are stated as checks.
5. **Transition order**: three diagnostics, each reported, none decisive alone: (a) hysteresis between hot and cold at L = 8; (b) the size of the E jump across the flip at L = 12, 16, 20 and whether it shrinks with L; (c) the two-peak structure of the E histogram at β_mix(16) over 20,000 sweeps, with the Binder cumulant B = 1 − ⟨E⁴⟩/3⟨E²⟩². A transition is called first-order if (a) and (c) both hold and the jump in (b) does not shrink by more than 30 % from L = 12 to L = 20.

**Calibration pass criterion (Z4).** The L = 8 hot/cold flip must bracket 1.0074 ± 0.01 and the L = 12–16 mixed-phase β must land in [1.005, 1.015] (literature: 1.0111, Arnold et al. hep-lat/0210010; the known transition is weakly first-order). If Z4 fails, the run halts and reports the failure; no other lattice is run.

**Budget.** CRIT2 took 46 minutes for D4 at 2 cores through L = 16. Four lattices through L = 20 with the histogram runs is estimated at 8–14 hours on 2 cores. The run uses `nohup` and polls; it does not shorten the sweep budget to fit a session.

## 5. Deliverables (the data section of the Letter)

- `latt_table.csv`: one row per lattice: coordination, loops per link, k, β_c (card), β_c (KN where defined), β_∞ three ways, transition order with the three diagnostics, L = 8 hysteresis width.
- `latt_raw/`: every E time series, JSONL, hashed.
- `latt_fig1.pdf`: E vs β at L = 8 hot and cold, four panels; `latt_fig2.pdf`: mixed-phase outcomes vs β for L = 12/16/20, four panels; `latt_fig3.pdf`: E histograms at β_mix(16), four panels, with B.
- `gate_LATT_RESULT.md`: the table, the figures described, the Z4 calibration, the order diagnostics, and a §"what this does not show".
- `u1latt.py` (the one simulator, all four lattices), unit tests, run driver. The code re-derives k(D4) = 2 and reproduces CRIT2's L = 16 flip interval [0.6125, 0.6175] as a regression test before any new lattice runs.

## 6. Verdicts (fixed now)

This gate is a measurement, so its verdicts are about the measurement's integrity, not about a theory.

- **SC-LATT-1 (table stands).** Z4 calibrates; D4 regression reproduces CRIT2; A4 and F4 each give a β_∞ with a stated uncertainty and an order call from the three diagnostics. The table goes into the Letter.
- **SC-LATT-2 (partial).** Z4 calibrates and D4 regresses, but one of A4/F4 fails to give a clean flip (e.g. tunnelling at L = 20, or diagnostics (a)–(c) disagree). That lattice is reported with what was found and marked "order undetermined"; the Letter carries three firm rows and one open one.
- **SC-LATT-0 (halt).** Z4 fails calibration or D4 fails regression. Nothing new is reported; the code is at fault and the gate is re-run after the fix, as a new digest.

Forecast, disclosed: D4 at 0.615 first-order (known); A4 and F4 both first-order with β_c between 0.5 and 0.8, F4 below D4 (same coordination, higher symmetry usually lowers β_c); Z4 at 1.011. If F4 ≈ D4 to within errors, coordination is the controlling variable; if they differ by more than 5 %, symmetry matters too. Either is a result.

## 7. The Letter (written after the run, not by the run)

Target: arXiv hep-lat, then Phys. Rev. D (regular article, short) or Phys. Lett. B. Working title: *Compact U(1) lattice gauge theory on the D4, A4 and F4 root lattices: critical coupling and transition order.* Sections: introduction (why non-hypercubic lattices; Celmaster's SU(N) work; Katz–Nógrádi), method, table and figures, discussion of coordination vs symmetry, provenance (AI-assisted, pre-registered, blind-replicated for D4, all code and raw data at a pinned commit, origin in a programme whose physical claims failed audit, stated in one paragraph), conclusion. Author: M. R. Cabrié; AI assistance acknowledged per journal policy. A lattice physicist is to be asked to read it before submission; Nógrádi has been contacted already.

## 8. What this gate does not do

It does not test BCT. It does not use r_oct, r_tet or α₀ anywhere. It does not vary the action or the gauge group. It does not add lattices after the digest. It does not claim a continuum limit: β_c on a lattice is a lattice quantity, and compact U(1) in 4D has no interacting continuum limit at the transition, which the Letter says in its first paragraph.

## 9. Pre-registration record

- Prompt: `audit/gates/gate_LATT_prompt.md`; digest: `audit/gates/PREREG_20261011_LATT.sha256`.
- Inputs the run may read: `gate_CRIT_prompt.md`, `gate_CRIT2_prompt.md`, `audit/gates/CRIT2/` (code and result), Arnold et al. hep-lat/0210010, Katz & Nógrádi arXiv:2512.10604, Celmaster PRD 26 2955 (1982). Nothing else from the corpus.
- Run thread: fresh; memory paused; long-running, so the run must checkpoint to disk after every stage and be resumable.
