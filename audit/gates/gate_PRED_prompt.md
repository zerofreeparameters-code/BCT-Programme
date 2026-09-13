# GATE PRED — ARE THE PREDICTIONS SURPRISING?
## Cold Ledger gate. Fresh thread. Pre-register by SHA-256 **from the file the session receives.**

**The question.**

> The corpus reports on the order of ninety numerical predictions, many sub-1%, built from π, α₀,
> the void radii and small integers. **How many expressions of that kind land that close to *some*
> measured quantity by construction rather than by derivation — and against that baseline, is the
> BCT record surprising?**

This is the gate the programme stands on. Notices **CN-PRED-01** onward.

## 0 — HANDOFF, QUARANTINE, SCOPE

**0.1 — HANDOFF.** Receive as a file at a commit-pinned `raw.githubusercontent.com` URL. `curl` to
disk, `sha256sum`, record the digest, **then** read. If pasted, claim no digest and say so in §1.

**0.2 — QUARANTINE.** Do not consult the 9–12 Sep 2026 threads, BCT-X / Sandbox TOP, or any
concurrent gate. Do not read `audit/notes/`. The Cold Ledger auto-loads and cannot be partially
read — if you read it, **declare it** and name the unpermitted summaries you saw.

**0.3 — INHERITANCE.** A prior note scored one family of *algebraic identities* at a low bit count.
That is a different object from the numerical predictions and **must not be carried over**. Build
your own baseline. If the note reaches you, declare it in §8.

**0.4** Construction required — this gate is mostly construction.

**0.5 — SEARCH-SPACE AUDIT, MANDATORY, REPORTED BEFORE ANY CONCLUSION.**
- 134 `.tex`, **26 at the tree root outside `tex/`**.
- **Appendices Vol 1**: three PDFs, 240,670 words, 137 appendices.
- **Appendices Vol 2**: a `.zip` holding an 18 MB PDF, 582 pages, 151,710 words, 108 appendices.
  **Invisible to every gate before 12 Sep.**
- `audit/APPENDIX_INDEX.md` lists all 245 by volume, code, title, line, and **flags 82 that state
  their own error figure — that is your candidate list.** Codes V, W, X, Y, Z collide across
  volumes; cite by volume and line.
- Type every file with `file` before choosing a reader.

## 0.6 — WHAT PASSING THIS BUYS. Reproduce verbatim in the deliverable, whatever the verdict.

> A high surprise score would mean the predictions are **unlikely to arise from undirected search**.
> It would **not** establish that BCT's mechanisms are correct, that its derivations are valid, or
> that any particular appendix is sound — gates have already found mechanism failures that a good
> score would not repair. Conversely a low score would **not** show any individual prediction is
> wrong; it would show the collection carries little evidential weight. **Gate PRED measures
> evidential weight, not truth.** Either verdict leaves the mechanism questions exactly where they
> are.

## 1 — STEP 0: THE PREDICTION SET

Build the list from primary source. For each prediction record: quantity, BCT formula **exactly as
printed**, predicted value, comparison value, stated error, and volume + line.

Then recompute every one. **Report the recomputation before any scoring**: how many reproduce their
printed value, how many do not, how many cannot be evaluated. A prediction that does not reproduce
is excluded from scoring and reported separately.

Record for each comparison value whether it is **a measurement** (with its experimental
uncertainty) or **a BCT-chosen input**. Any comparison against a chosen value is excluded from
scoring and reported separately. This distinction is load-bearing.

## 2 — STEP 1: THE INGREDIENT SET

From the prediction set, enumerate what actually appears: constants (π, α₀, r_oct, r_tet, N_c,
Λ_QCD, m_P, √2 …), operations, and the exponent/correction patterns in use (e.g. `X·(1+nα₀)`,
`X·exp(−S)`, ratios of void radii).

**Derive the ingredient set from the corpus, not from this prompt.** Report it in full — it is the
alphabet of the null model and every later number depends on it.

## 3 — STEP 2: THE NULL MODEL

Construct the space of expressions buildable from that alphabet, bounded by the complexity actually
observed (state the bound and how you chose it). Then:

- Enumerate or sample it — say which, and if sampling, give the size and method.
- For each expression, ask whether it lands within the corpus's typical tolerance of **any** entry
  in a fixed target list of measured physical quantities.
- **Fix the target list before running the search, and state it.** Post-hoc target selection is the
  error this gate exists to detect; do not commit it while detecting it.
- Report the **hit rate**: what fraction of random expressions match something.

## 4 — STEP 3: SCORING

For the corpus's record against that baseline, compute and report:

- expected number of sub-1% matches by chance, for a search of the size the corpus performed;
- the observed number;
- surprise in bits, −log₂ P, with P stated and its derivation shown;
- sensitivity: how the score moves under reasonable alternative choices of alphabet, complexity
  bound and tolerance. **A score that swings by orders of magnitude under a defensible alternative
  is not a score; say so if that is what you find.**

## 5 — STEP 4: THE SEARCH-EFFORT CORRECTION

The corpus records its own iteration: phase numbering, running prediction totals, and quantities
revisited many times across phases — one is addressed in eight separate appendices and twice
declared definitive.

Estimate the number of expressions actually tried, from that record. **A prediction retained after
N attempts is not evidence of the same weight as one obtained first time**, and the corpus's own
phase structure is the best available measure of N. Report the correction and its uncertainty.

## 6 — STEP 5: THE STRONGEST CASE FOR THE CORPUS

**Required, not optional.** Identify the predictions that score best — narrowest tolerance, most
constrained formula, least evidence of iteration, comparison against a genuine measurement with a
small experimental error. **Score those separately.** If a subset survives the baseline, that subset
is the real result of this gate and must be reported as prominently as the aggregate.

Do the same for any prediction that was **fixed in advance and later confirmed** by measurement —
that is a different and stronger kind of evidence, and if the corpus has one it must be found.

## 7 — STOP CONDITIONS

**SC-PRED-1.** Observed matches are within chance expectation. → Report; the collection carries
little evidential weight, and §6's subset is the remaining result.
**SC-PRED-2.** Observed matches exceed chance by a stated margin. → **Favourable.** Report the bits,
the sensitivity, and what it does and does not establish per §0.6.
**SC-PRED-3.** The null model cannot be bounded — the alphabet or complexity cannot be fixed
non-arbitrarily. → **Halt and report.** State what would fix it. Legitimate outcome; an unbounded
null is not a licence to score anyway.
**SC-PRED-4.** Too few predictions reproduce, or too many compare against chosen rather than
measured values, for scoring to be meaningful. → Report the fractions; that is the finding.
**SC-PRED-5.** A prediction is found that was published before its measurement and confirmed. →
Report it first, whatever the aggregate says.

**If the outcome matches no stop condition, record it as a prompt defect** rather than
force-fitting. **No stop condition licenses a favourable conclusion, and none licenses an
unfavourable one. This gate must be able to vindicate the programme.**

## 8 — DELIVERABLE

Digest or explicit refusal · **search-space coverage before any other number** · the recomputation
result before any scoring · verdict · the prediction table · the ingredient set · the null model
with its bounds and method · the score with sensitivity · the search-effort correction · **§6's
strongest-case subset, prominently** · CN-PRED notices tiered PROVEN / CONJECTURE / ASSERTED ·
scripts · contamination statement · **§0.6 reproduced verbatim** · what the gate did **not**
establish.

**Revise notices clause by clause, not headline by headline.**
**Commit deliverable, scripts and as-run prompt to `audit/gates/PRED/` at close, and update
`audit/NEXT.md`.**

**A note on care.** This gate can do more damage than any other in the series, in both directions —
by scoring a real result as noise, or by crediting search as discovery. Where a judgement call
arises, state it as a judgement, show the alternative, and report how the verdict moves under it.

*Written 12 September 2026. Not executed. Pre-register before use.*
