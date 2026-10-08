# Gate CRIT — pre-registration card

**Programme:** "Nothing says why 1/137" (successor to the BCT Cold Ledger)
**Card written:** 8 October 2026, Claude, at Michel's request ("we are going to try it")
**Status:** PRE-REGISTERED, NOT RUN. The quantity this card asks for has not been computed.
**Type:** a measurement with a kill attached. Not a derivation of α.
**Depends on:** Gate SPECTRUM2 (card SHA-256 d5d052c9…ed285c, result T0: A_Y = 55.477, A_2 = 49.460)
and Gate LINK (SC-LINK-2: a compact-U(1) link formulation is available to BCT at a stated cost).

---

## 1. Background (stated, not a result of this card)

Bennett, Nielsen and Froggatt (arXiv:hep-ph/9607278, hep-ph/9707234) obtain
1/α = 137 ± 9 by assuming that the gauge couplings at the Planck scale sit at a lattice
critical point. Their U(1) input is the critical coupling of compact U(1) lattice gauge
theory on the **hypercubic** lattice, β_crit = 1.01. A lattice critical coupling is not
universal: it depends on the lattice and on the action.

**Prior art, searched twice on 8 October 2026, then checked against four source papers
supplied by Michel.** No published critical coupling was found
for compact U(1) on the D4 (F4, body-centred hypercubic) lattice. What was found:

- Every simulation located on that lattice is SU(2): Celmaster (Phys. Rev. D 26, 2955,
  1982; Phys. Rev. Lett. 52, 403, 1984), Celmaster and Moriarty (1985 to 1987), Celmaster,
  Kovacs, Green and Gupta (1985, 1986), and one- and two-loop perturbative work.
- Nearest neighbour: Drouffe, Moriarty and Mouhas, "U(1) four-dimensional gauge theory on
  a simplicial lattice", J. Phys. G (1984). The simplicial (A4) lattice also has triangular
  plaquettes, but 20 neighbours and 6 triangles per link, against 24 and 8 for D4. They
  report a transition near β ≈ 0.85.
- Kulkarni (2026, self-published) writes a triangular action on the D4 lattice for SU(N),
  performs no simulation, and lists the lattice's numerical track record as none.

Read in full: Celmaster's 1982 preprint (NUB 2561) and 1984 preprint (NUB 2617), and the
two CERN preprints of Drouffe, Moriarty and Mouhas (TH.3653 and TH.3654, July 1983).
Celmaster treats SU(N) only and calls the lattice "BCT" (body-centred tesseract); his
counts (24 neighbours, 96 triangles touching each site, 8 per edge) match section 4.1.

All 52 papers INSPIRE lists as citing Celmaster's 1982 paper were checked by title
(1983 to 2025). None treats U(1) on this lattice. The closest:

- Katz and Nógrádi, "QCD on the 16-cell honeycomb", Phys. Rev. D 114 (2026) 054504,
  arXiv:2512.10604. The 16-cell honeycomb is this lattice; the gauge group is SU(3).
  It shows the lattice is in current use for QCD and is the first place to look for
  conventions.
- Neuberger (1987) and Bhanot, Bitar, Heller and Neuberger (1990): scalar (φ⁴) fields
  on F4. No gauge field.
- Drouffe and Moriarty's simplicial papers (section 7 validation), on a different lattice.

Limit of the search: the citing papers' full texts were not read, and the citers of
Celmaster's 1984 paper were not listed separately. The claim is "none found", not
"none exists".

## 2. Question

1. What is the critical coupling β_c of compact U(1) lattice gauge theory with the Wilson
   action on triangular plaquettes of the D4 lattice?
2. Put in place of the hypercubic value, by the fixed rule of section 5, does it leave the
   Planck-scale hypercharge coupling where experiment needs it, within the programme's
   3-unit tolerance?

## 3. Why the D4 lattice, and what that choice costs

BCT at c/a = √2 is the face-centred cubic lattice. A lattice gauge theory with a phase
transition needs four dimensions. D4 (points of Z⁴ with even coordinate sum, 24 nearest
neighbours (±1, ±1, 0, 0)) is the four-dimensional lattice whose three-dimensional slices
are face-centred cubic, and all of its elementary plaquettes (triangles) are equivalent
by symmetry. It therefore needs no space-to-time weighting, which "FCC × a time axis"
would. **This is a choice made by the analyst.** Other four-dimensional completions exist
and are not run.

## 4. Fixed rules

**4.1 Model.** Link angles θ on the 12 positive root directions. Action
S = β · Σ over triangles of (1 − cos θ_triangle), 32 triangles per site, 8 per link.
Periodic integer array of side L (L even); the array holds two independent copies of the
lattice, which are both used.

**4.2 Code.** `audit/gates/CRIT/u1lat.py` (SHA-256 11d5ffbc…069de065) and
`audit/gates/CRIT/scan.py` (SHA-256 2823c30d…7f24b3bf), exactly as committed. Heat-bath
updates. No change to either file is allowed; a bug found during the run stops the gate
and is reported, and a corrected card is registered.

**4.3 Runs.** Every run is `python3 scan.py d4 L β n_therm n_meas seed start`, with
seed = 1000·L + round(1000·β) and both start = hot and start = cold.

| Stage | L | β grid | n_therm | n_meas |
|---|---|---|---|---|
| A (locate) | 4 | 0.20 to 1.50, step 0.05 | 500 | 2000 |
| B | 6 | β_A − 0.06 to β_A + 0.06, step 0.01 | 2000 | 5000 |
| C | 8 | β_B − 0.02 to β_B + 0.02, step 0.005 | 2000 | 4000 |

β_A, β_B, β_C are the grid points with the largest specific heat C = N_p · var(E), taking
the larger of the hot and cold values at each β. If the largest value sits on the edge of
a grid, the grid is extended by its own step until it does not; nothing else may be added.

**4.4 Result.** β_c ≡ β_C. Uncertainty ≡ the larger of 0.005 and 2·|β_C − β_B|.
Also report: E in both phases at β_C, and whether hot and cold starts disagree there
(a sign of a first-order transition).

## 5. The rule that connects β_c to 1/α (fixed here, before the run)

In the classical continuum limit 1/e² = k·β, with k = 1 for the hypercubic lattice and
k = 2 for D4 with triangles (computed by `naive_k` in `u1lat.py`; the run must reprint it).

    R = (2 · β_c) / 1.0111

1.0111 is the hypercubic value (infinite volume, Wilson action). The rule assumes that the
step from bare to physical coupling at the transition is the same on both lattices, and
that the Bennett–Nielsen factors (three generations, the U(1) factor of about 6.5) are
unchanged. Under it, the hypercubic lattice is taken to reproduce A_Y, and D4 gives

    1/α_Y(M_P) = R · 55.477        shift in 1/α(0) = (R − 1) · 55.477

The tolerance is the programme's 3 units of 1/α: |R − 1| ≤ 3/55.477 = 0.054.

Also to be reported, with no verdict attached: k·β at the specific-heat peak for L = 6 on
all three lattices (hypercubic and A4 from section 7, D4 from stage B).

## 6. Verdict codes

- **SC-CRIT-0 (unposable).** No specific-heat peak in 0.20 ≤ β ≤ 3.00.
- **SC-CRIT-1 (lattice-blind).** |R − 1| ≤ 0.054, uncertainty included. The critical-point
  route gives the same answer on the BCT-shaped lattice as on the cubic one. A requirement,
  not evidence: the factors that make 137 are still borrowed.
- **SC-CRIT-2 (kill).** |R − 1| > 0.108, uncertainty included. On the BCT-shaped lattice
  the critical-point route does not give 137; report the value it gives.
- **SC-CRIT-3 (inconclusive).** Anything between.

β_c is reported whatever the code. It is a statement about a lattice model and stands
or falls independently of section 5.

## 7. Validation already done (this is why the card is not blind to the code)

In the card-writing thread, 8 October 2026:

- Hypercubic lattice, L = 6, β = 0.990 to 1.015 in steps of 0.005, hot and cold: the
  specific-heat peak lies between 1.000 and 1.005. Literature for L = 6: about 1.0018.
  Output: `audit/gates/CRIT/validation_hc_L6.jsonl` (SHA-256 bbeb2a2d…12e6c8d6).
- Both lattices at β = 20 and β = 0.1, L = 4: E matches the weak-coupling value
  (1/(4β) hypercubic, 11/(64β) D4) and ⟨cos⟩ matches β/2, to about 1%.
- A4 (simplicial) lattice, L = 6, β = 0.79 to 1.03, hot and cold: the specific-heat peak
  is at 0.91, between 0.90 and 0.92. The published figure is "β ≈ 0.85". The preprint
  (TH.3653) uses the same action and the same 6⁴ lattice, with 150 heat-bath sweeps from
  ordered starts, and reads the transition by eye from a plot of the action. The action
  values read from its Fig. 2 agree with this code on both sides (about 0.47 at 0.85 and
  0.28 at 1.0). The difference is one of estimator (middle of the drop against the
  specific-heat peak), not of simulation. Its relation β = 4/(√5 g₀²) reproduces the
  ratio k(A4)/k(hypercubic) = √5/2 used here. Its weak-coupling formula 1/(4β) differs
  from this code's 9/(40β) by 10%; the code's value is the one its runs reproduce. Output: `audit/gates/CRIT/validation_a4_L6.jsonl` (SHA-256 e7b48ce4…8240cc85).
  The A4 lattice at β = 20 and β = 0.1 matches its exact limits (9/(40β), β/2) to 1%.
- With k = 1.1180 for A4, k·β at the L = 6 peak is 1.017 ± 0.011 on A4 and about 1.002
  on the hypercubic lattice. In continuum units the two critical couplings agree to
  about 1.5%.
- Gauge invariance of E checked on all three lattices.
- D4 was run for 20 sweeps at β = 1.0, L = 6, for timing only. No energy was looked at.

No D4 run between β = 0.1 and β = 20 has been examined.

## 8. No-fit clause

- No lattice, action, grid, seed rule, estimator, constant or tolerance may be changed
  after the run starts.
- No result may be described as deriving α. SC-CRIT-1 would mean a borrowed argument is
  insensitive to one change of lattice.
- The audited BCT model has one phase per site and no link variables. Whatever the
  outcome, it is not evidence for or against BCT void geometry.
- If R lands near a simple number, that is not a finding.

## 9. Analyst's disclosure

The analyst has two forecasts and they disagree.

- **Counting guess:** β_c scales inversely with plaquettes per link. From the hypercubic
  lattice, 1.011 × 6/8 ≈ 0.76; from A4, 0.91 × 6/8 ≈ 0.68. Either gives R between 1.35
  and 1.5 and **SC-CRIT-2**.
- **Pattern guess:** section 7 shows k·β at the transition is the same on the hypercubic
  and A4 lattices to about 1.5%. If that holds on D4, β_c ≈ 0.50 to 0.51, R ≈ 1, and
  **SC-CRIT-1**. Note the counting guess already fails between hypercubic and A4 (same 6
  plaquettes per link, β_c of 1.00 and 0.91).
- The analyst leans to the pattern guess, about 60 to 40, and records that this lean was
  formed after seeing the A4 validation, which was run for a different purpose.
- A hit needs β_c between 0.478 and 0.533.
- The analyst has no estimate of whether the transition is first order.

## 10. Known limitations (stated in advance)

- Bare couplings are compared. The physical coupling at the transition is not measured.
- Wilson action only. The Villain action has a different β_c on the hypercubic lattice
  (about 0.64), so "the" critical coupling of a lattice is action-dependent.
- Small lattices. On the hypercubic lattice the shift from L = 6 to infinite volume is
  about 1%, well inside the tolerance.
- D4 is one completion of a three-dimensional lattice into four dimensions.

## 11. Run protocol

- Fresh thread, inside the BCT project. One gate per thread.
- Fetch this card and both scripts by commit-pinned raw URL, hash all three on disk
  (SHA-256) before reading the card, and record digests and commit.
- At most two runs in parallel per CPU core available. Stage C is expected to take about
  an hour on two cores.
- Deliverable: `gate_CRIT_RESULT.md` with the three stage tables, β_c, R, the verdict
  code, the disclosure scored, and a plain-language summary; raw `.jsonl` outputs saved.
- Same-session results are capped at CONJECTURE.
