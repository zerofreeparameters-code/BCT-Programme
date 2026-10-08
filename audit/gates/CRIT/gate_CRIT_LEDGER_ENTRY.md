# Gate CRIT — ledger entry (tier decision)

**Date:** 8 October 2026. **Recorded by:** Claude, in the card-writing thread, after the run.
**Card:** `audit/gates/gate_CRIT_prompt.md`, commit `f89120c`, SHA-256 `d3bbcab8…2cd10c`.
**Run:** one fresh thread, 8 October 2026 (Claude Opus 5.5). Result: `gate_CRIT_RESULT.md`.

## Checks made on the result in the card-writing thread

- The run used the registered code at the registered hashes, the card's grids, seeds and
  sweep counts (54, 26 and 18 runs), and triggered no grid extension.
- The arithmetic of sections 4 and 5 recomputes exactly: R = 2 × 0.610 / 1.0111 = 1.2066;
  the kill line is β_c > 0.5601; the hit window was 0.4783 to 0.5328.
- Two Stage B points were rerun with the registered code and seeds (d4, L = 6, cold,
  β = 0.60 and 0.62). Both reproduce the reported E and C to every printed digit
  (0.54022, 2.964; 0.39537, 2.394). Same code, seeds and NumPy version, so this confirms
  the run was done as reported. It is not an independent replication.

## Tier movements

| # | Statement | Tier | Basis |
|---|---|---|---|
| 1 | β_c of compact U(1), Wilson action, D4 triangles = 0.610 ± 0.005 at L = 8 | **CONJECTURE** (same-session cap), reproducible | one run; spot rerun bit-exact. Finite-volume, pseudo-critical value |
| 2 | Verdict SC-CRIT-2: the Bennett–Nielsen–Froggatt critical-point route, moved to D4 by the card's rule, misses by about +11.5 in 1/α(0) | **Recorded as run. KILL** of that route on D4 | |R − 1| = 0.207 against a 0.108 kill line; holds at both ends of the uncertainty |
| 3 | "k·β at the transition is lattice-independent" (the analyst's pattern guess) | **FALSIFIED** as a general rule | 1.00 (hypercubic), 1.02 (A4), 1.22 (D4) |
| 4 | The D4 transition is first order | **OBSERVATION**, not tested | 20% jump in E within one 0.005 step at L = 8; hot/cold split at L = 6 |
| 5 | No published U(1) critical coupling exists for D4 | **"None found"**, not "none exists" | card section 1 search, all 52 citers of Celmaster 1982 checked by title |
| 6 | BCT void geometry | **No movement** | card section 8 |

## Standing sentences

- The kill is of one borrowed argument on one completion of FCC into four dimensions, with
  one action, comparing bare couplings. It says nothing about α itself.
- Both analyst forecasts missed in value; the lean (60 to 40 for a pass) was wrong.
- With Gate SPECTRUM2 (induced light: a requirement map with no experimental handle), both
  routes to 1/137 opened on 7–8 October 2026 are now tested. Neither derives α.

## What would move item 1 up

An independent check: different code (e.g. Metropolis, or an independent heat bath), or
larger lattices (L = 10, 12) with enough statistics to see tunnelling and extrapolate to
infinite volume.
