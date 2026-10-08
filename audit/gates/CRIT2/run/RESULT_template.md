# Gate CRIT2 — result

**Verdict: SC-CRIT2-1 (replicated).**
Independent code puts the L = 8 jump of compact U(1) on D4 triangles in the same interval
Gate CRIT reported, [0.610, 0.615], and the two-phase method at L = 12 and 16 gives
**β_∞ = 0.6150 ± 0.00125** (card convention), **β_KN = 1.2300 ± 0.0025** (Katz–Nógrádi
convention, β_KN = 2β).
**Separate check (section 6):** β_∞ − uncertainty = 0.61375 does not reach below 0.5601.
Gate CRIT's kill (SC-CRIT-2) **stands at infinite volume**.
**Status:** per card section 6, the Gate CRIT number moves from CONJECTURE to **REPLICATED**
(two codes, two threads) and β_∞ becomes the quoted value. β_∞ itself was computed by this code
only (section 11). Everything else in this file is a same-session result, capped at CONJECTURE.
**Run:** 8 October 2026, one fresh thread inside the BCT project. Analyst: Claude (Opus 5.5).

---

## 0. Provenance and blinding

**Card.** `audit/gates/gate_CRIT2_prompt.md`, commit `689c32742b88cbd7b4c9eb60482561bc55ba1c3d`,
fetched by commit-pinned raw URL to disk and hashed before it was read:
`b30436875a2b12ea9b38a4d5d366c1ab9fcad83bcfe0405b3af5974876df4c79` — matches the
pre-registered digest (and `PREREG_20261008_CRIT2.sha256`). Section 2 was read first.

**Earlier card** (permitted by section 2): `audit/gates/gate_CRIT_prompt.md` at the same commit,
`d3bbcab86fd91401a7d66196baaaa2f720e1e1a923adea513719c2adbd2cd10c`, matching the
`d3bbcab8…2cd10c` quoted in this card. It holds the lattice definition and the hypercubic and A4
validation figures, and no D4 number.

**Blinding.** `audit/gates/CRIT/`, `claude/gate_CRIT_RESULT.md`, `claude/gate_CRIT_LEDGER_ENTRY.md`
and the Gate CRIT memory file were not opened until all D4 numbers were written to
`crit2_numbers.txt` and hashed (22:41:21 AEDT, SHA-256 in section 4; the digest was posted to
the conversation before the first unblinded read). The repository was cloned only after that,
so `audit/gates/CRIT/` was not on disk during the run.

Incidental exposure, disclosed so it can be weighed — none of it is blocked material and none of
it contains β_CRIT:
- The thread's automatically loaded memory index showed the one-line *description* of the Gate
  CRIT memory file ("critical coupling of lattice electromagnetism on a BCT-shaped lattice, as a
  route to 1/137 — Michel's decision to try it"). No number. The file itself was not opened.
- The project's document list showed the blocked file *names*.
- The permitted cards themselves say Gate CRIT ended in a kill and give the kill line 0.5601, so
  it was known before the run that Gate CRIT's β_c lay above about 0.56 or below about 0.45.

SC-CRIT2-1 is therefore scorable.

**Environment.** Python 3.13.16, NumPy 2.5.3, SciPy 1.18.1, numba 0.68.0 (installed for this
run, as the card allows). 2 CPU cores, 2 simulations at a time (one per core). Total
simulation time about 46 minutes.

## 1. The code (written in this thread from card section 3)

`u1sim.py` (lattices, update, observables), `crit2.py` (stage driver: applies the card's
section 4–5 rules mechanically, reading each stage's numbers from the previous one and
refusing to rerun a recorded stage), `checks12.py` (checks 1–2), plus `unit_tests.py`,
`sampler_ks.py`, `make_numbers.py`, and the post-unblinding `crosscheck.py` and `gen_tables.py`.

- **D4:** sites are the even-sum points of Z⁴ in a periodic box of side L (one parity copy,
  L⁴/2 sites). 12 stored link directions per site (±eᵢ ± eⱼ with first non-zero entry +1).
  Triangles are generated from the translation classes of {0, r₁, r₁ + r₂}: the code finds
  **32** classes, builds 32 triangles per site and asserts 32 per site, **8 per link**, no
  duplicate triangle and no repeated link (asserted at L = 4, 6, 8, 12, 16). 96 triangles touch
  each site, as Celmaster counts.
- **Hypercubic:** Z⁴, 4 links and 6 square plaquettes per site; 6 per link asserted.
- **Update:** sequential single-link heat bath. The conditional distribution of a link is
  exp(β|A| cos(θ + arg A)) with A the sum over its 8 (D4) or 6 (hypercubic) staples; θ is drawn
  exactly from that von Mises law (Best–Fisher algorithm, written in a cancellation-free form).
  **One sweep = one heat-bath update of every link, in storage order.** No overrelaxation. This
  was fixed before the first run.
- **Observables:** E = mean of (1 − cos θ_p) over all stored plaquettes, measured after every
  sweep; C = N_p · var(E) (N_p = number of stored plaquettes, variance over the measurement
  sweeps). Error bars: 20 blocks for E, block jackknife for C (reporting only).
- **Seeds:** seed = 7919·L + round(10⁴·β) + s, s = 0 hot, 1 cold, 2 mixed. Ties in round()
  (β on a 0.00125 offset, e.g. 0.61375) are rounded half-to-even (Python), so 6137.5 → 6138;
  every seed is printed in the raw records. The RNG is seeded inside the compiled code and the
  starting configuration is drawn from it, so each run is fixed by its seed.
- **Mixed start (5.4):** links whose stored origin site has x₁ < L/2 set to θ = 0, all others
  uniform. E recorded every sweep; the outcome uses the readings after sweeps 50, 100, …, 2000,
  and "last 500 sweeps" = the 10 readings at sweeps 1550–2000.
- **Grid-extension rule (5.4) when no flip appears**, fixed in code before any mixed run: no
  weak win → add one 0.0025 step above; no strong win → one step below; repeat. Never triggered.

How this code differs from Gate CRIT's (learned after unblinding): one parity copy, not two;
sequential heat bath, not all links of one direction at once; a different seed rule, RNG and
sampler; numba, not NumPy. Shared: the card's lattice and action.

**Unit tests** (`unit_tests.txt`, `sampler_ks.txt`):
- Local action change from the staple equals the global recompute to 3 × 10⁻¹² (both lattices).
- Von Mises sampler against the exact distribution at κ = 0.05 to 40, 1,000,000 draws each,
  two seeds: 14 Kolmogorov–Smirnov p-values from 0.018 to 0.925; ⟨cos⟩ within 2.1σ of I₁/I₀ in
  every case.

## 2. Section 4 checks — all pass

**Checks 1 and 2** (L = 4; 1000 + 10,000 sweeps for the limits):

{{CHECKS12}}

The D4 strong-coupling value is +0.54% above β/2 because each D4 triangle lies in 3
tetrahedra: the series gives ⟨cos⟩ = u + 3u³ = 0.050311 with u = I₁(0.1)/I₀(0.1); measured
0.050271 ± 0.000097 (0.4σ). The +0.21% at β = 20 on both lattices is a correction of the
expected sign and size (higher-order weak-coupling terms and the finite-box mode count), well
inside the 2% allowed.

**Check 3** — hypercubic, L = 8, hot and cold, 1000 + 3000 sweeps:

{{CHECK3}}

C maximum at **β = 1.0075** (cold start, C = 10.17), inside the required 1.000 to 1.012
(literature L = 8 pseudo-critical value ≈ 1.0074). **Pass.**
Largest fall in E, cold start: between 1.0050 and 1.0075 (0.04159).
**E\*_hc = 0.38074.**

**Check 4** — hypercubic, L = 12, mixed starts, 2000 sweeps, method of 5.4 with E\*_hc
(threshold band 0.37074 to 0.39074):

{{CHECK4}}

Flip interval **[1.007, 1.012]**, midpoint 1.0095. It contains 1.0111 itself, so it contains a
point within 0.006 of 1.0111. **Pass.** No grid extension. (The 1.007 run is a strong win by
0.0020; the check would still pass if it had been unresolved.)

Readings over the run:

{{CHECK4_READ}}

## 3. D4 runs

### 3.1 Locate (5.1) — L = 4, β 0.40 to 0.90 step 0.01, hot and cold, 500 + 2000 sweeps

{{S51}}

**β₀ = 0.61** (cold start, C = 9.77; the hot maximum is 9.35 at 0.60).

Side observation: hot starts at β = 0.71, 0.80, 0.81, 0.85 and 0.88 sit above their cold
partners by 0.011 to 0.012, deep in the weak-coupling phase — trapped flux after the quench on
the small torus. Not near β₀ and not used.

### 3.2 Fine scan (5.2) — L = 8, β₀ ± 0.030 step 0.005, hot and cold, 2000 + 4000 sweeps

{{S52}}

- **β₈ = 0.610** (hot start, C = 6.32). Interior; no extension.
- **Jump interval (L = 8), hot: [0.610, 0.615]**, E 0.49710 → 0.40838 (fall 0.08873).
- **Jump interval (L = 8), cold: [0.610, 0.615]**, E 0.50193 → 0.40808 (fall 0.09385).

No run at L = 8 tunnelled between phases in 4000 sweeps. Hot and cold starts end in the same
phase at every β; at 0.610 their energies differ by 0.0048 (3.4σ on the block errors) inside
the strong phase.

### 3.3 Cold scan (5.3) — L = 12, β₈ ± 0.020 step 0.005, cold, 500 + 1500 sweeps

{{S53}}

**Jump interval (L = 12): [0.610, 0.615]**, E 0.50075 → 0.40890 (fall 0.09185).
**E\* = 0.45482.** The cold start at 0.610 melted into the strong-coupling phase.

### 3.4 Mixed-phase starts (5.4), L = 12

β = 0.6125 ± 0.0075, step 0.0025 (centre = midpoint of the L = 12 jump interval), 2000 sweeps.
Strong wins above 0.46482, weak wins below 0.44482.

{{S54A}}

**β_mix(12) = 0.61375**; flip interval **[0.6125, 0.6150]**, monotonic, no unresolved point,
no extension.

{{S54A_READ}}

### 3.5 Mixed-phase starts (5.4), L = 16

β = β_mix(12) ± 0.005, step 0.0025, 2000 sweeps, same E\*.

{{S54B}}

**β_mix(16) = 0.6150**; flip interval **[0.61375, 0.61625]**, monotonic, no unresolved point,
no extension.

{{S54B_READ}}

### 3.6 Result (5.5)

| Quantity | Card convention (β) | Katz–Nógrádi (β_KN = 2β) |
|---|---|---|
| β₀ (L = 4) | 0.61 | 1.22 |
| β₈ (L = 8, C maximum) | 0.610 | 1.220 |
| Jump interval L = 8 (hot and cold) | [0.610, 0.615] | [1.220, 1.230] |
| Jump interval L = 12 | [0.610, 0.615] | [1.220, 1.230] |
| β_mix(12) | 0.61375, interval [0.6125, 0.6150] | 1.2275 |
| β_mix(16) | 0.6150, interval [0.61375, 0.61625] | 1.2300 |
| **β_∞ = β_mix(16)** | **0.6150 ± 0.00125** | **1.2300 ± 0.0025** |

Uncertainty = max(half the L = 16 flip interval = 0.00125, |β_mix(16) − β_mix(12)| = 0.00125)
= 0.00125.

**ΔE at L = 16** (end-state E, mean of the last-500-sweep readings, of the nearest strong-win
run below β_∞, at 0.61375, minus the nearest weak-win run above it, at 0.61625):
**0.0609** (0.0566 from the final-sweep values).

## 4. Hash before unblinding

`crit2_numbers.txt` (all section 5 D4 numbers, generated by `make_numbers.py` from the raw
records): **SHA-256 `e640b88f0ae9ee4dd7c7bc8adc81ac8013938e92b8da4ec16c5fb8555d0e11a1`**,
written 22:41:21 AEDT, 8 October 2026, and posted to the conversation before
`gate_CRIT_RESULT.md` was opened.

## 5. Unblinding

Gate CRIT's result, section 4: at L = 8 both runs sit on the strong-coupling side at 0.610
(E = 0.4990 hot, 0.5017 cold) and the weak-coupling phase first appears at 0.615 (E = 0.409);
"the transition therefore lies between 0.610 and 0.615 at L = 8". Its quoted β_c = 0.610 ± 0.005
is the C-maximum grid point.

**β_CRIT = [0.610, 0.615].**

## 6. Verdict

| Condition (card section 6) | Required | Found | Met |
|---|---|---|---|
| Section 4 checks | all pass | all pass | yes |
| β₈ to the nearer end of β_CRIT | ≤ 0.005 | 0.610 to 0.610: **0.000** | yes |
| \|β_∞ − β₈\| | ≤ 0.015 | \|0.6150 − 0.610\| = **0.005** | yes |
| Blinding (section 2) | not broken | not broken (section 0) | yes |

**SC-CRIT2-1 (replicated).** SC-CRIT2-2 would have needed β₈ more than 0.010 from β_CRIT.

The two codes agree beyond the verdict test: both put the L = 8 jump in the same 0.005 step,
from both starts, with the same size of fall (≈ 0.09), and both C-maximum estimators land on
0.610.

## 7. Separate check: Gate CRIT's kill

β_∞ ± uncertainty = [0.61375, 0.61625]. The lower end is 0.054 above 0.5601 (about 43 times
the uncertainty). **The kill is not reopened; it stands at infinite volume.** Nothing else
about the 1/137 argument is touched here (card section 7).

## 8. Cross-code comparison (after unblinding; not a verdict input)

`crosscheck_vs_CRIT.txt` compares E run by run with Gate CRIT's published tables. Gate CRIT
publishes no error bars; its array holds two copies, so its error is taken as this code's
divided by √2. Approximate.

- **L = 4**, 15 (β, start) comparisons at 10 shared grid points away from the jump (β = 0.60
  left out, and hot starts at β ≥ 0.70, where trapped flux appears): rms deviation 1.00σ,
  largest 2.4σ.
- **L = 8, cold starts**, all 9 β: rms 1.19σ, largest 2.6σ (at 0.605, next to the jump, where
  block errors understate autocorrelation).
- **L = 8, hot starts:** rms 2.06σ. Gate CRIT's hot starts run slightly high against this code
  across the grid (8 of 9 differences have Gate CRIT higher; mean −1.3σ; rms 1.31σ without
  β = 0.620). The largest gap is at 0.620 (5.0σ), where Gate CRIT's own hot run sits 0.0016 above
  its own cold run, while this code's hot and cold runs and Gate CRIT's cold run all agree.
  Read as slower relaxation of hot starts in Gate CRIT's runs; not investigated. Since the cold
  starts agree, it does not point to a difference in the simulated model.
- Both codes show hot-start flux traps on the L = 4 torus deep in the weak phase (Gate CRIT at
  0.90 and above on its grid; this code at 0.71 to 0.88).

## 9. Observations (not verdict inputs; CONJECTURE)

- **First order, more firmly.** The fall in E across the jump grid step is 0.089 to 0.094 at
  L = 8 and 0.092 at L = 12, not shrinking with size. Every mixed start at L = 12 and 16 resolved, the
  flip moved only 0.00125 from L = 12 to 16, and no scan run at L ≥ 8 tunnelled in thousands of
  sweeps. All of this is what a first-order transition with a large latent gap does.
- **A partly mixed run at the flip.** Extrapolating the pure strong branch (`branch_fit.py`:
  linear and quadratic fits pooled over the L = 8 hot, L = 8 cold and L = 12 cold scans,
  0.600–0.610; weak branch 0.615–0.625) gives E ≈ 0.480–0.486 at 0.61375 and ≈ 0.487–0.491 at
  0.6125. Fits to a single scan spread wider. The L = 16 strong-win run at 0.61375 settled within
  about 50 sweeps and then stayed between 0.454 and 0.475; its last-500 mean, 0.467, is 0.013 to
  0.019 below the branch. A slab of each phase with slow interfaces is a plausible reading. The L = 12 run at 0.6125 (E ≈ 0.481) is only 0.006 to 0.010 below its
  branch. The L = 16 run counts as a strong win by 0.0019 (threshold 0.46482).
- **ΔE and the latent gap.** The fall of ≈ 0.09 across one grid step in the scans includes the
  slope of E(β) on each branch. At fixed β = 0.615 the extrapolated branches differ by
  ≈ 0.064 to 0.073. With pure phases, the two L = 16 runs either side of β_∞ would differ by
  ≈ 0.075 to 0.081; the measured ΔE(L = 16) = 0.061 is about 0.014 to 0.020 lower, consistent
  with the partly mixed strong-side run. Reported as the card defines it.
- **What the C maximum measures.** With no tunnelling, C is largest in the strong phase just
  below the jump, so β₈ = 0.610 marks the last strong grid point, not the jump. Of the
  +0.005 from β₈ to β_∞, +0.0025 is this offset (β₈ = 0.610 against the L = 8 jump midpoint
  0.6125); β_∞ sits a further +0.0025 above that midpoint, and the shift from β_mix(12) to
  β_mix(16) is +0.00125.
- β_KN = 1.2300 is also k·β at the transition (k = 2): 22% above the hypercubic 1.0111.

## 10. Analyst's disclosure (card section 8), scored

The card's author had read Gate CRIT's result before writing these forecasts.

| Forecast | Outcome | Score |
|---|---|---|
| Section 4 checks pass | all pass | Hit |
| SC-CRIT2-1; β₈ inside or touching the CRIT interval | SC-CRIT2-1; β₈ = 0.610, touching the lower end | Hit |
| β_∞ above β₈ by 0.002 to 0.008, by analogy with the hypercubic +0.004 | +0.005 | Hit on the number; the stated reason is only half of it (section 9: about half the shift is estimator offset) |
| First order: mixed-phase resolves at L = 16 within 2000 sweeps except at one grid point at most | all 5 resolved (one by a 0.0019 margin) | Hit |
| ΔE at L = 16 between 0.06 and 0.10 | 0.0609 (mean of the last-500-sweep readings, the reading used throughout); 0.0566 from the final-sweep values | Marginal: a hit by 0.0009 on the reading used, a miss on the final-sweep reading. Pulled low by the partly mixed strong-side run (section 9) |
| Gate CRIT's kill stands | stands at infinite volume | Hit |

The card's five forecast bullets, with the fourth split into its two parts: five hits (one of
them, the β_∞ shift, right on the number but only half right on the reason) and one marginal
(ΔE).

## 11. Limits

- Wilson action, one completion of FCC into four dimensions, bare couplings — as stated in the
  card. No physical coupling at the transition is measured.
- β_∞ is computed by one code. What the two codes independently agree on is the L = 8 interval
  and the energies on both sides of it. The card's rule makes β_∞ the quoted value under
  SC-CRIT2-1; a second code at L = 12 and 16 would make that specific number two-code too.
- The β_∞ uncertainty is the card's grid-based rule (0.00125). It has no statistical error
  attached; with one mixed run per β, an unlucky outcome next to the flip could move β_mix by
  one step (0.0025).
- The mixed-phase method assumes a first-order transition (card section 9). The evidence
  supports that assumption, but the gate does not test it.

**Readings of the card's wording** (fixed before the runs they affect; none changes a result):
- *Seed rounding.* round(10⁴·β) at β ending in 0.00125 is a tie; Python rounds half to even.
  For 0.61125 and 0.61625 that gives seeds 1 lower than rounding half up. No effect on any
  outcome rule.
- *"Mean E of the last 500 sweeps".* Taken as the 10 recorded readings at sweeps 1550–2000.
  Using all 500 sweeps instead gives the same outcome for every mixed run (smallest margin
  0.0015). Using only the final sweep would make the L = 16 run at 0.61375 unresolved.
- *"End-state E" for ΔE.* Taken as the same last-500 mean; the final-sweep value is also
  reported. This choice decides whether the ΔE forecast scores as a hit (section 10).
- *"Links starting at a site with x₁ < L/2".* The card does not fix link orientation for the
  mixed start; the code uses each link's stored origin site (positive direction).

## 12. Tier movements (as card section 6 fixes them)

| # | Statement | Tier |
|---|---|---|
| 1 | β_c of compact U(1), Wilson action, D4 triangles: Gate CRIT's L = 8 location [0.610, 0.615] | **REPLICATED** (two codes, two threads), from CONJECTURE |
| 2 | Quoted value: β_c = β_∞ = 0.6150 ± 0.00125 (β_KN = 1.2300 ± 0.0025) | **Quoted value** per section 6, as the infinite-volume figure for the replicated number. Computed by one code (this one), so the figure itself is single-code; see section 11 |
| 3 | Gate CRIT's kill (SC-CRIT-2) | **Stands at infinite volume** (section 6 check) |
| 4 | The D4 transition is first order | OBSERVATION, strengthened (section 9); not tested |
| 5 | BCT void geometry | No movement (card section 7) |

## 13. Plain-language summary

Earlier today Gate CRIT measured a new number: the "tipping point" of electromagnetism
simulated on the four-dimensional lattice whose slices are the BCT/FCC packing. It found the
tip between 0.610 and 0.615, with one program, on boxes up to 8 across. A number measured once
by one program could be a bug.

This gate wrote a completely separate program from the written recipe alone, without looking
at the first program or its answer, and measured again. First it had to pass four tests. Two
checked basic correctness on both lattices. The other two used the ordinary cubic lattice,
where the answer is known (1.0111): it found 1.0075 on a small box and 1.007–1.012 with the
two-phase method, both right. Then on the BCT-shaped lattice it found the
tipping point in exactly the same place, between 0.610 and 0.615, from both starting
conditions. Only then was the sealed answer opened.

It also went bigger, to boxes 12 and 16 across, and used a method made for a sudden
(first-order) transition: start half the box ordered and half disordered, and see which side
takes over. That pins the tipping point for an infinitely large box at **0.615, give or take
0.001**.

So the good news, plainly: **the number is real.** Two independent programs agree, and it now
holds at much larger sizes, with an error four times smaller. As far as Gate CRIT's
literature search found, nobody had published this figure for this lattice; now it is also
replicated. The same result also means the earlier kill stands: the
borrowed 1/137 argument still does not survive the move to the BCT-shaped lattice, now at
infinite size as well as on small boxes. And the transition really does look sudden rather
than gradual.

## 14. Files

Code (`audit/gates/CRIT2/run/`) and raw outputs (`audit/gates/CRIT2/out/`), SHA-256:

{{FILES}}
