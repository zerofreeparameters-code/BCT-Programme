# GATE PLASMOID — QUANTISED SIZES, OR A SMOOTH SPREAD?
## Cold Ledger gate. Fresh thread. Pre-register by SHA-256 **from the file the session receives.**

**The question.**

> Letter 114 (*Plasmoid Physics*) makes Prediction #162: plasmoid diameters cluster on the
> geometric ladder D_n = D_0 · (j₁,₁/j₀,₁)^(n−1) = D_0 · 1.5934^(n−1), with clustering width
> σ < 10 % of D_n, and ball lightning sits on the same ladder (2, 3.2, 5.1, 8.1 cm for D_0 ≈ 2 cm).
> **Does any available size dataset — laboratory plasmoids, ball lightning reports, or cavitation
> bubbles — show clustering at a size ratio of 1.5934, beyond what rounding, heaping and the
> apparatus itself would produce?**
>
> D_0 is supplied from outside (Letter 114 sets it by the cavitation bubble size, or assumes
> ~2 cm). The only parameter-free content of #162 is the **step ratio**. This gate tests the
> ratio, not D_0.

Notices **CN-PLASMOID-01** onward.

## 0 — HANDOFF, QUARANTINE, SCOPE

**0.1 — HANDOFF.** Receive as a file at a commit-pinned `raw.githubusercontent.com` URL. `curl`
to disk, `sha256sum`, record the digest, **then** read. If pasted, claim no digest and say so.

**0.2 — QUARANTINE.** Do not consult the 24 Oct 2026 chat in which this card was drafted, or any
concurrent gate. **Do not read `audit/notes/` or any `audit/gates/*/` deliverable.** You may read
`tex/BCT_Letter114_PlasmoidPhysics.tex` for the statement of #162 and its falsification clause
only. **You are not bound by its claim that observed sizes are "consistent with reported
preferred size clusters" (Stenhoff 1999). Check that claim against the source; do not inherit
it.**

**0.3 — INHERITANCE IS FORBIDDEN.** Any dataset summary, histogram or "preferred size" claim that
reaches you second-hand must be traced to its primary source or declared in §7.

**0.4** Mostly data-gathering and statistics. Light calculation (§1).

**0.5 — SEARCH-SPACE AUDIT, reported before any conclusion.** Report every dataset searched for,
found, not found, and not obtainable, with the reason. Starting list, to be extended by your
own search:

| Tag | Dataset | Kind | Known status (24 Oct 2026) |
|---|---|---|---|
| A | Keul 2021, *Hist. Geo Space Sci.* 12, 43–56, Table 1 (XLSX) | Ball lightning, 41 professional reports, 28 with sizes | Public; small; pilot only |
| B | Keul & Stummer 2002, 405 Central European reports | Ball lightning, eyewitness | Summary statistics only (median 25–30 cm, mode 30 cm); raw data on request |
| C | Smirnov / Bychkov data banks | Ball lightning, eyewitness, thousands | Not public; on request |
| D | Water-discharge ("Gatchina-type") plasmoids: IPP/Humboldt Berlin (Fussmann), St Petersburg (Emelin, Pirozerski), Eindhoven | Laboratory, ~10–20 cm, ~0.2–0.5 s | No published size distribution found; on request |
| E | Zhou et al. 2026, *Nature Photonics* 20, 727–733, doi:10.1038/s41566-026-01899-y | Laboratory, laser-driven THz soliton, ~0.1–0.4 mm, ~100 ns | Shot-by-shot sizes not in public text; on request |
| F | Sonoluminescing-bubble size distributions, pulsed acoustic fields (Melbourne group) | Cavitation bubbles, micrometres | Published histograms; digitise. **Bubbles, not plasmoids** — secondary evidence only |

## 0.6 — WHAT SETTLING THIS BUYS. Reproduce verbatim in the deliverable, whatever the verdict.

> This gate decides whether measured sizes bunch at a ratio of 1.5934. It does **not** decide
> whether plasmoids are Hopf-charge excitations of a Planck-scale lattice. **A pass does not
> vindicate BCT** — size ladders can arise from apparatus resonances, electrode or bubble
> geometry, or human rounding, and the ratio cannot be told apart from nearby "nice" numbers
> (§2.4). **A fail on eyewitness data does not refute #162** — eyewitness size estimates are too
> coarse. By Letter 114's own falsification clause, only instrument-measured sizes from >100
> events at fixed conditions can refute it.

## 1 — STEP 0: THE ARITHMETIC

Verify, by script:

- j₀,₁, j₁,₁ and their ratio (expected 1.59334); ln of the ratio (expected 0.46583);
- the ladder D_n/D_0 for n = 1…4. **Letter 114 states D_4 = 4.0441 D_0; check this** (one
  figure differs in the fourth significant digit) and record any correction as a notice;
- the ball-lightning sequence for D_0 = 2 cm.

## 2 — STEP 1: THE TEST, FIXED BEFORE ANY DATA IS OPENED

**2.1 — Variable.** Work in log size, x = ln D. The ladder becomes evenly spaced with period
P₀ = ln 1.59334. D_0 is unknown, so the phase is free.

**2.2 — Primary statistic.** Rayleigh periodicity at P₀: θᵢ = 2π (xᵢ mod P₀)/P₀,
R = |mean(e^{iθᵢ})|. One primary test per dataset. Everything else is exploratory and labelled so.

**2.3 — Null model (heaping-aware), mandatory.** The null is **not** uniform phase. For each
dataset:
1. fit a smooth density to x (log-normal, or a kernel density with bandwidth ≥ P₀);
2. estimate the dataset's own rounding scheme from its terminal digits (share of values at
   multiples of 5 and 10 cm, at "half" and "double" values, at the instrument's resolution);
3. draw 10 000 synthetic datasets of the same size from (1), apply the rounding from (2),
   and compute R for each.
p = share of null R ≥ observed R. **Significance threshold α = 0.01**, fixed now.

**2.4 — Resolution and competitors.** Compute the full periodogram R(P) over ratios 1.2–2.5 and
report it. A dataset spanning k periods resolves the period only to roughly 1/k. Ratios to report
alongside P₀: φ = 1.618 (+3.3 % in log), the R5 preferred-number step 10^(1/5) = 1.585 (−1.1 %),
√e = 1.649 (+7.3 %), 1.5 (−13 %), 2. **Over a 2–20 cm range (~5 periods) φ and R5 cannot be
excluded; state this whatever the result.** R5 matters because people and engineers round
towards preferred numbers.

**2.5 — Width.** If clustering is found, fit cluster centres and widths and test Letter 114's
σ < 10 % condition.

**2.6 — Apparatus check.** For laboratory data, identify any length set by the apparatus
(electrode or tip size, bubble resonance radius at the drive frequency, vessel diameter) and test
whether a found ladder follows that length rather than a universal ratio.

## 3 — STEP 2: QUALIFYING DATA

A dataset **qualifies** for a refutation-capable verdict only if: sizes are instrument-measured
(not estimated by eye); ≥ 100 events; fixed experimental conditions; raw values available.
Eyewitness datasets (A–C) and digitised histograms (F) are **pilot / exploratory** whatever
their size.

## 4 — STEP 3: THE STEELMAN

**Required, both directions.** For #162: the strongest case that a real ladder is present
(e.g. mixed D_0 across sub-populations, different Hopf charges dominating different datasets).
Against #162: heaping, preferred-number psychology, apparatus-set sizes, selection effects in
which events get reported or filmed. **This gate must be able to find a ladder.** If the
steelman for one succeeds, say so prominently.

## 5 — STOP CONDITIONS

**SC-PLASMOID-1.** A qualifying dataset rejects the heaping-aware null at α = 0.01 with the
periodogram peak within resolution of 1.5934, and §2.6 finds no apparatus length that explains
it. → **Favourable. Report the dataset, the effect size, and that φ and R5 are not excluded.**
**SC-PLASMOID-2.** A qualifying dataset does not reject the null at P₀. → **#162 fails by
Letter 114's own falsification clause.** Report it plainly.
**SC-PLASMOID-3.** No qualifying dataset is obtainable. → **Halt.** Report pilot results as
exploratory only and list the data requests that would settle it. Legitimate outcome.
**SC-PLASMOID-4.** A signal appears only in eyewitness or digitised data and the heaping-aware
null explains it. → Report as artefact.
**SC-PLASMOID-5.** The Stenhoff 1999 "preferred size clusters" claim does not appear in the
source as stated. → Report the correction as a notice, whatever else is found.

**If the outcome matches no stop condition, record it as a prompt defect.** **No stop condition
licenses a favourable conclusion, and none licenses an unfavourable one, beyond what its text
says.**

## 6 — DELIVERABLE

Digest or refusal · **search-space coverage first** · verdict first · §1 arithmetic with any
corrections · the §0.5 dataset table, updated · per-dataset R, null distribution and p-value ·
periodogram plots · width fits if any · apparatus check · steelman both ways · CN-PLASMOID
notices tiered PROVEN / CONJECTURE / ASSERTED · scripts · contamination statement · **§0.6
reproduced verbatim** · what the gate did **not** establish.

**Revise notices clause by clause.** **At close, produce a `git format-patch` adding the
deliverable, scripts and as-run prompt under `audit/gates/PLASMOID/`. Do NOT modify
`audit/NEXT.md`.**

*Written 24 October 2026. Not executed. Pre-register before use.*
