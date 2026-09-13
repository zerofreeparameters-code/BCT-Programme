# GATE PRED — HOW SURPRISING ARE THE NUMBERS?
## Cold Ledger gate. Fresh thread. Pre-register by SHA-256 **from the file the session receives.**

**The question.**

> Gate STAT scored the identity family (π⁵/6 and its relatives) at 3.3 bits of surprise. The
> numerical predictions — α, m_e, m_P, G, the Koide relation, the quark and lepton mass ratios,
> sin²θ_W, the Wolfenstein and CP phases — are unscored, and they are what the programme stands
> on in public. **For each published prediction: given the grammar of constants and operations
> the corpus actually uses, how many expressions of equal or lower complexity land as close to
> the measured value as the corpus's expression does, and how many bits of surprise remain after
> that look-elsewhere count and after every post-hoc correction factor is charged for?**

Notices **CN-PRED-01** onward.

## 0 — HANDOFF, QUARANTINE, SCOPE

**0.1 — HANDOFF.** Receive as a file at a commit-pinned `raw.githubusercontent.com` URL. `curl` to
disk, `sha256sum`, record the digest, **then** read. If pasted, claim no digest and say so in §1.

**0.2 — QUARANTINE.** Do not consult the 9–13 Sep 2026 threads, BCT-X / Sandbox TOP, or any
concurrent gate. Do not read `audit/notes/` **except** the scoring-definition section of
`notes/note_identities.md` (Gate STAT), which may be read once, **after §2 below is written and
committed to the transcript**, solely so the bits reported here are commensurable with STAT's.
Do not read STAT's verdict or its per-identity scores. The Cold Ledger auto-loads and cannot be
partially read — if you read it, **declare it** and name the unpermitted summaries you saw.

**0.3 — INHERITANCE.** Nothing numerical is inherited. Every predicted value, every measured value
and every stated error is **recomputed** from the expression as printed and from a CODATA / PDG
value fetched and cited in this session. If a recomputed error disagrees with the corpus's printed
error, that is a finding and is charged to the prediction, not silently corrected.

**0.4** Construction permitted and expected — §2 asks you to build a grammar and enumerate it.

**0.5 — SEARCH-SPACE AUDIT, MANDATORY, REPORTED BEFORE ANY CONCLUSION.**
- **Repo:** tarball, digest recorded. **134 `.tex`, 26 at the tree root outside `tex/`.**
- **Mount:** 33 ZIP archives of page images with `.txt` layers, 14 true PDFs, **2 raw UTF-8 text
  files** that `file` reports as `data`. `BCT_CompleteRegistry.pdf`, `BCT_LetterList_v4.pdf`,
  One Medium §§10–11, Monograph v2.1 tables, and App D.2–D.4, AL2, AD–AG are in the mount.
  **Type every file with `file`.** Report page-level coverage.
- **The prediction census is part of the search space.** Before scoring anything, list **every**
  numerical prediction the corpus publishes with a stated error, with its printed expression,
  printed value, printed error, and source. Report the count. A prediction not in this list is
  not scored; a prediction the corpus prints in two incompatible forms is listed twice.

**0.6 — EXTERNAL LITERATURE AND TOOLS PERMITTED.** The look-elsewhere effect; Wyler (1969, 1971)
and its published critiques as the benchmark near-miss; inverse-symbolic search (RIES, Plouffe's
Inverter, Bailey–Borwein on numerical coincidences); minimum-description-length arguments.
Running an inverse-symbolic search in-session is permitted and expected. **Cite only what you
read; run only what you can show.**

## 0.7 — WHAT PASSING THIS BUYS. Reproduce verbatim in the deliverable, whatever the verdict.

> A prediction that scores high after the look-elsewhere charge is evidence that the corpus's
> expression is not a coincidence of its own grammar. It is **not** evidence that the derivation
> printed beside it is correct, that the mechanism is physical, or that the framework is
> unified — a true formula with a false derivation is still a true formula, and this gate cannot
> tell them apart. A prediction that scores low is not thereby false; it is thereby **unsurprising**,
> and the programme should stop citing it as evidence. **Gate PRED cannot deliver physics. At
> most it delivers a ranked list of which numbers are worth defending and which are noise the
> grammar produces for free.** A favourable verdict is a ticket to a harder gate on the one or two
> expressions that survive.

## 1 — STEP 0: THE CENSUS AND THE RECOMPUTATION

From primary source, quoting the printed expression each time:

- The full prediction list of §0.5, with for each: (a) the expression as printed, (b) the corpus's
  printed value and error, (c) the value recomputed here from the printed expression to 12
  significant figures, (d) the measured value with its source and date, (e) the recomputed
  relative error ε, (f) the **number of distinct correction factors** between the bare geometric
  expression and the final one (e.g. α: α₀ → α₀(1−2α₀) → α₀(1−3α₀)/(1−α₀) is two; m_e: S_D4 →
  S_D4/(1−x_lep) → the (4π+1)/π² dressing is two), and (g) the **date order**: was the expression's
  final form printed before or after the corpus records the discrepancy it closes?
- Flag every case where (c) ≠ (b), or where the same target has more than one printed final form.
- Flag every prediction whose target is not a measured number (e.g. "no QCD axion", "δ_CP = −π/2
  exact" before DUNE) as **unscorable here** and set it aside without judgement.

## 2 — STEP 1: THE GRAMMAR, WRITTEN BEFORE ANY SCORE

**Write this section in full, with its enumeration counts, before evaluating any target in §3.**
The deliverable must show that ordering.

- **Atoms.** The constants the corpus draws on, listed from the census: at minimum
  {1, 2, 3, 4, 6, 8, 12, 24, 48, π, √2, √3, √6, e, α₀, r_tet, r_oct, R, S_D4 = π⁵/6, x_lep = 4α₀/π,
  N_gen = 3, ℓ_P-normalised void quantities}. Add any atom the census shows the corpus using; do
  not add atoms it does not use.
- **Operations.** {+, −, ×, ÷, √, x^n for |n| ≤ 5, exp, ln, 1/(1−x)} — again, only those the
  census shows in use.
- **Complexity measure.** Node count of the expression tree. State it. Record the complexity of
  each corpus expression under it.
- **Enumeration.** For complexity C = 1 … C_max (C_max ≥ the largest corpus expression), count
  N(C), the number of distinct real values the grammar generates, by exhaustive enumeration where
  feasible and by sampling with a stated confidence interval where not. Report N(C) as a table.
- **Density.** For each target value T and complexity C, estimate the number of grammar
  expressions with |x − T|/T ≤ ε, either directly from the enumeration or as N(C) × 2ε × ρ(T),
  where ρ is the local density of grammar values per unit log-value near T, measured from the
  enumeration. State which.
- **Pre-registered thresholds.** Before §3: **≥ 10 bits after all charges = "surprising";
  3–10 bits = "suggestive"; < 3 bits = "unsurprising — the grammar produces this for free".**
  These numbers are fixed now and may not be moved after the scores are seen.

## 3 — STEP 2: THE SCORES

For each scorable prediction, in the order of the census:

- **Raw bits** = −log₂ P(a grammar expression of complexity ≤ C_expr lands within ε of T).
- **Look-elsewhere charge**: −log₂ of the number of targets the corpus tried a geometric formula
  for (the census count, not the number it published successes for), and −log₂ of the number of
  candidate expressions the corpus itself reports testing for that target (App D.2 §3 reports
  four approaches and an "exhaustive systematic search over all two-quantity products"; charge
  that search).
- **Correction-factor charge**: each post-hoc factor in §1(f) is a further draw from the grammar
  at its own complexity; charge its bits.
- **Date-order charge**: a factor introduced after the discrepancy it closes was recorded is
  charged at full grammar cost; a factor printed before is not.
- **Net bits**, and the bin. Show the arithmetic per prediction.
- **Benchmark.** Score Wyler's α formula under the same grammar and charges, so the reader can see
  what a celebrated near-miss scores.
- **Inverse-symbolic control.** For each target, run an inverse-symbolic search restricted to the
  §2 grammar at complexity ≤ C_expr and report the **best** expression it finds and its ε. If the
  control beats or ties the corpus expression, say so.

## 4 — STEP 3: THE OBSTRUCTION CHECK

Independently of the scoring, establish whether the corpus **anywhere** pre-registered a
prediction before the relevant measurement, or predicts a quantity not yet measured to the stated
precision (the neutron EDM bound, δ_CKM at degree precision, the 62.9 GeV scalar, r = 0.0046).
Quote it if it exists. **A genuine out-of-sample prediction is not scored by §3 at all**; it is
listed separately with its falsification date, because surprise-scoring is a substitute for
out-of-sample testing, not a replacement for it.

## 5 — STOP CONDITIONS

**SC-PRED-1.** At least one scorable prediction nets ≥ 10 bits. → Report it with its full charge
sheet; it is the candidate for a derivation-audit gate. Favourable outcome; report it as plainly
as any other.
**SC-PRED-2.** Every scorable prediction nets < 3 bits. → Report; the programme's public evidence
is grammar noise, and the deliverable says which sentences in One Medium §10 and the Monograph
tables should stop being cited.
**SC-PRED-3.** All predictions land in the 3–10 bit band. → Report; recommend the two highest for
a derivation audit and the rest for retirement from public claims.
**SC-PRED-4.** The grammar cannot be bounded — the corpus's correction factors are open-ended, so
C_max has no ceiling and P cannot be estimated. → **Halt and report** with the list of unbounded
factors. Legitimate outcome.
**SC-PRED-5.** Recomputation (§1c) contradicts the printed values for a material fraction of the
census. → Report the recount first; score only what recomputes.

**If the outcome matches no stop condition, record it as a prompt defect** rather than force-fitting
it. **No stop condition licenses a favourable conclusion, and none licenses an unfavourable one.**

## 6 — DELIVERABLE

Digest or explicit refusal · **search-space coverage and the prediction census before any other
number** · verdict first · the recomputation table · **the grammar and enumeration counts, shown
to have been written before any score** · the per-prediction charge sheets with net bits and bins ·
the Wyler benchmark · the inverse-symbolic controls · the §4 out-of-sample list · CN-PRED notices
tiered PROVEN / CONJECTURE / ASSERTED · scripts (enumerator, scorer, inverse-symbolic search) ·
external citations, each actually read · contamination statement · **§0.7 reproduced verbatim** ·
what the gate did **not** establish.

**Revise notices clause by clause.** **Commit deliverable, scripts and as-run prompt to
`audit/gates/PRED/` at close, and update `audit/NEXT.md`.**

*Written 13 September 2026. Not executed. Pre-register before use.*
