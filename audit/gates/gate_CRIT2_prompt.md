# Gate CRIT2 — pre-registration card

**Programme:** "Nothing says why 1/137" (successor to the BCT Cold Ledger)
**Card written:** 8 October 2026, Claude, at Michel's request ("let's check it")
**Status:** PRE-REGISTERED, NOT RUN.
**Type:** independent replication, plus the infinite-volume limit.
**Depends on:** Gate CRIT (card SHA-256 d3bbcab8…2cd10c, commit f89120c; result and ledger
entry committed after it).

---

## 1. Why this gate

Gate CRIT measured the critical coupling of compact U(1) lattice gauge theory on the D4
lattice once, with one code, on lattices up to L = 8, and capped the number at CONJECTURE.
A rerun of two of its points with the same code and seeds reproduced them exactly; that
shows the run was done as reported, not that the number is right. This gate asks for the
number again from code written independently, on larger lattices, with an estimator suited
to a first-order transition.

## 2. Blinding (read this first)

Until the thread has computed its own D4 numbers and recorded their SHA-256 in its
deliverable, it must **not** open any of:

- `audit/gates/CRIT/` (code, validation data, result, ledger entry)
- the project documents `claude/gate_CRIT_RESULT.md` and `claude/gate_CRIT_LEDGER_ENTRY.md`
- the memory file for Gate CRIT (`…/gate-crit.md`)

It may read `audit/gates/gate_CRIT_prompt.md` (the earlier card), which contains the
lattice definition and the hypercubic and simplicial validation figures but no D4 result.
If any of the blocked material is seen early, say so in the deliverable; the run continues
but cannot score SC-CRIT2-1.

## 3. The model (specification for the new code)

- **Lattice D4:** sites are the points of Z⁴ with even coordinate sum. Each site has 24
  neighbours at r ∈ {±eᵢ ± eⱼ, i < j}. Periodic box of side L (L even) in each coordinate.
- **Links:** one angle θ ∈ [0, 2π) per nearest-neighbour pair, θ reversed with orientation.
- **Plaquettes:** triangles (x, x + r₁, x + r₁ + r₂) with r₁, r₂ and r₁ + r₂ all
  neighbour vectors. There are 32 triangles per site and each link lies in 8 of them. The
  code must count these and assert both numbers.
- **Action:** S = β Σ_triangles (1 − cos θ_triangle).
- **Observables:** E = mean of (1 − cos θ_triangle) over all triangles in the stored
  lattice; C = N_Δ · var(E), with N_Δ the number of stored triangles.
- **Hypercubic lattice** (validation only): Z⁴, square plaquettes, S = β Σ (1 − cos θ_p).

Any correct local update is allowed (heat bath, Metropolis, overrelaxation mixed with
either). The code must be written from this specification, in this thread. Seeds:
seed = 7919·L + round(10⁴·β) + s, with s = 0 (hot), 1 (cold), 2 (mixed). `pip install
numba` is allowed.

**Normalisation (stated, not to be re-derived for the verdict):** in the classical
continuum limit 1/e² = k·β with k = 1 (hypercubic) and k = 2 (D4). Katz and Nógrádi
(arXiv:2512.10604) write the D4 action as (β_KN/2) Σ (1 − (1/N) Re Tr P) and set
β_KN = 2N/g₀² "as with the cubic action", which is the same statement: β_KN = 2β.
Report β_c in both conventions.

## 4. Checks the code must pass before any D4 number is used

1. **Gauge invariance** of E under a random gauge transformation, both lattices.
2. **Limits**, both lattices, L = 4: at β = 0.1, ⟨cos⟩ = β/2 within 2%; at β = 20 from a
   cold start, E = (n_links − 1)/(2β · n_triangles) per site within 2%
   (hypercubic 1/(4β); D4 11/(64β)).
3. **Hypercubic transition**, L = 8, hot and cold, β = 0.995 to 1.020 step 0.0025,
   1000 + 3000 sweeps: the C maximum lies in 1.000 to 1.012 (literature pseudo-critical
   value at L = 8 ≈ 1.0074; infinite volume 1.0111331(21), Arnold et al.,
   hep-lat/0210010). E\*_hc = mean of E at the two ends of the adjacent pair of grid
   points with the largest fall in E, cold start.
4. **Hypercubic mixed-phase bracket**, L = 12, β = 1.002, 1.007, 1.012, 1.017, 1.022,
   2000 sweeps each, method of section 5.4 with E\*_hc: the flip interval must contain a
   point within 0.006 of 1.0111.

If any check fails: verdict **SC-CRIT2-0**, stop, report.

## 5. D4 runs

**5.1 Locate (L = 4).** Hot and cold, β = 0.40 to 0.90 step 0.01, 500 + 2000 sweeps.
β₀ = grid point with the largest C (larger of hot and cold).

**5.2 Fine scan (L = 8).** Hot and cold, β = β₀ − 0.030 to β₀ + 0.030 step 0.005,
2000 + 4000 sweeps.
- **β₈** = grid point with the largest C (same estimator as Gate CRIT).
- **Jump interval (L = 8)**, for each start: the adjacent pair of grid points with the
  largest fall in E.
- If β₈ is at an edge, extend by 0.005 steps until it is not.

**5.3 Cold scan (L = 12).** Cold start only, β = β₈ − 0.020 to β₈ + 0.020 step 0.005,
500 + 1500 sweeps. **Jump interval (L = 12)** as above. **E\*** = mean of E at its two ends.

**5.4 Mixed-phase starts (L = 12 and L = 16).** Initial state: links starting at a site with
x₁ < L/2 set to θ = 0, all others uniform random. Record E every 50 sweeps. Outcome from
the mean E of the last 500 sweeps: **weak wins** if below E\* by more than 0.01, **strong
wins** if above E\* by more than 0.01, **unresolved** otherwise.
- L = 12: β = midpoint of the L = 12 jump interval ± 0.0075, step 0.0025 (7 points),
  2000 sweeps.
- **β_mix(L)** = midpoint between the highest β where strong wins and the lowest β where
  weak wins. Unresolved points between them widen the interval; report its ends.
- L = 16: β = β_mix(12) ± 0.005, step 0.0025 (5 points), 2000 sweeps.
- At either size, if the outcome does not flip inside the grid, extend by 0.0025 steps
  until it does.

**5.5 Result.** **β_∞** = β_mix(16). Uncertainty = the larger of half the L = 16 flip
interval and |β_mix(16) − β_mix(12)|. Also report ΔE at L = 16: the difference between the
end-state E of the nearest strong-win and weak-win runs either side of β_∞.

**5.6 Hash, then unblind.** Write all D4 numbers above to `crit2_numbers.txt`, record its
SHA-256 in the deliverable, then open the Gate CRIT result.

**Cost.** With pure NumPy on two cores, about 4 to 5 hours, most of it at L = 16. With
numba, expect well under half that. Run at most two simulations per core.

## 6. Verdict codes

β_CRIT means the L = 8 jump interval reported in Gate CRIT's result, section 4.

- **SC-CRIT2-0 (method failed).** A section 4 check failed. No D4 claim.
- **SC-CRIT2-1 (replicated).** β₈ is within 0.005 of β_CRIT (distance to the nearer end of
  the interval), and |β_∞ − β₈| ≤ 0.015. The Gate CRIT number moves from CONJECTURE to
  REPLICATED (two codes, two threads); β_∞ becomes the quoted value.
- **SC-CRIT2-2 (not replicated).** β₈ is more than 0.010 from β_CRIT.
- **SC-CRIT2-3 (inconclusive).** Anything else.

Separately, whatever the code: if β_∞ ± its uncertainty reaches below 0.5601, Gate CRIT's
kill (SC-CRIT-2) is reopened and must be reported as such. Otherwise it stands at infinite
volume.

## 7. No-fit clause

- No lattice, action, grid, sweep count, seed rule, estimator, threshold or tolerance may
  change after the run starts. Grid extensions only as written in 5.2 and 5.4.
- This gate tests one number. It does not touch the 1/137 argument beyond the separate
  check in section 6, and it is not evidence for or against BCT void geometry.
- A first-order reading from ΔE is an observation, not a verdict input.

## 8. Analyst's disclosure (this card is not blind on its author's side)

The author has read the Gate CRIT result and reran two of its points. Forecast, recorded
so it can be scored:

- Section 4 checks pass.
- SC-CRIT2-1. β₈ inside or touching the CRIT interval.
- β_∞ above β₈ by 0.002 to 0.008, by analogy with the hypercubic shift from L = 8 to
  infinity (about +0.004).
- The transition is clearly first order: the mixed-phase method resolves at L = 16 within
  2000 sweeps except at one grid point at most, and ΔE at L = 16 lies between 0.06 and
  0.10.
- Gate CRIT's kill stands.

The hypercubic mixed-phase check was tried in the card-writing thread, with the Gate CRIT
code, before this card was registered, to size the sweep counts; the outcome is recorded
in section 10.

## 9. Known limitations

- Wilson action only; one completion of FCC into four dimensions.
- Bare couplings. No physical coupling at the transition is measured.
- The mixed-phase method assumes a first-order transition. If the transition turns out
  to be continuous, outcomes near β_c will be unresolved and β_∞ will carry a wide
  interval; that is reported, not repaired.

## 10. Sizing test done before registration

Hypercubic lattice, L = 12, Gate CRIT code (heat bath, NumPy), mixed-phase start as in
5.4, 3000 sweeps, E every 250 sweeps:

| β | E over the run | outcome |
|---|---|---|
| 1.000 | 0.408 to 0.420 | strong |
| 1.006 | 0.385 to 0.402 | strong |
| 1.016 | 0.332 to 0.353 | weak |
| 1.022 | 0.328 to 0.334 | weak |

The flip lies between 1.006 and 1.016 (midpoint 1.011; literature 1.0111). Every run had
settled by its first 250-sweep reading, so 2000 sweeps is ample at this distance from β_c.
No D4 run was made for this test.

## 11. Run protocol

- Fresh thread inside the BCT project. One gate per thread. Opus-class model.
- Fetch this card by commit-pinned raw URL and check its SHA-256 before reading it.
- Respect section 2 throughout.
- Deliverable: `gate_CRIT2_RESULT.md` with the section 4 checks, all tables, β₈, jump
  intervals, β_mix(12), β_mix(16), β_∞ (both conventions), ΔE, the SHA-256 of
  `crit2_numbers.txt`, the verdict, the disclosure scored, and a plain-language summary.
  Save the code and raw outputs.
- Same-session results are capped at CONJECTURE, except as section 6 allows for β_c.
