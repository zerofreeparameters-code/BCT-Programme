# GATE TANH — WHICH JOSEPHSON COUPLING DOES THE CORPUS HAVE?
## Cold Ledger gate. Fresh thread. Pre-register by SHA-256 **from the file the session receives.**

**The question.**

> App J §3.1 computes a dimensionless coupling from geometry, prints a number, and then boxes a
> different number as the result. The two differ by roughly a factor of twenty. Which one is the
> BCT Josephson coupling, and what happens downstream when the right one is used?

Notices **CN-TANH-01** onward.

## 0 — HANDOFF, QUARANTINE, SCOPE

**0.1 — HANDOFF.** Receive this as a file at a commit-pinned `raw.githubusercontent.com` URL.
`curl` it to disk, `sha256sum` it, record the digest, **then** read it. A digest of pasted text
certifies nothing; if that is what you have, claim no digest and say so in §1.

**0.2 — QUARANTINE.** Do not consult the 9–11 Sep 2026 threads, BCT-X / Sandbox TOP, or Gate INT
if it is running concurrently. The Cold Ledger auto-loads and cannot be partially read — if you
read it, **declare it** and name the unpermitted gate summaries you saw.

**0.3 — INHERITANCE IS FORBIDDEN ON THE CENTRAL QUESTION.** Prior sessions have recorded findings
about App J §3.1. **Do not read them as inputs and do not cite them.** Derive the arithmetic
yourself from App J's own printed factors. If a prior notice reaches you anyway, say so in §7 and
state whether your derivation preceded it. The value of this gate is that it is independent; a
session that confirms an earlier finding by reading it has produced nothing.

**0.4** Construction permitted.

**0.5 — SEARCH-SPACE AUDIT, MANDATORY, REPORTED BEFORE ANY CONCLUSION.**
- **Repo:** `zerofreeparameters-code/BCT-Programme`, pulled by tarball, digest recorded. **134
  `.tex`, 26 of them at the tree root outside `tex/`.** A `tex/*.tex` glob covers 108 and is not
  the corpus. This error has been made.
- **Mount:** 33 mount `.pdf` files are **ZIP archives** of per-page images with a `.txt` layer per
  page. `unzip` opens them; `pdftotext` and `pymupdf` do not. A prior gate wrongly concluded from
  two extractor failures that they were unreadable. Unpack, grep the text layers, report page-level
  coverage.

## 0.6 — WHAT SETTLING THIS BUYS. Reproduce verbatim in the deliverable, whatever the verdict.

> Fixing a coupling constant does **not** supply the BCT mass mechanism, the Higgs mass, or any
> prediction. A separate gate found the inter-component coupling this constant is used *as* is
> never written down anywhere, so a corrected value may have nothing correct to be the coefficient
> of. **What this gate buys is a known number in place of an ambiguous one, and an honest count of
> what moves when it changes.** If nothing published moves, that is the result and it should be
> stated as plainly as any other.

## 1 — STEP 0: REPRODUCE APP J §3.1 EXACTLY

From primary source, quoting the text:

- Write out the full expression App J §3.1 gives for the dimensionless coupling, with every factor.
- Evaluate it at 40 dps from `r_oct`, `r_tet` and ξ, deriving ξ yourself and stating how.
- Compare against **every** number App J prints in that section, including the intermediate factors
  it shows.
- Then quote the sentence and the boxed statement that follow the computation, verbatim.

**State the ratio between the computed value and the boxed value.** Do not characterise it yet.

## 2 — STEP 1: STEELMAN THE BOXED VALUE

**Do not assume the boxed result is the error.** Test it properly:

- Is there a limit, regime, or alternative reading in which the discarded factor tends to 1?
  Compute what ξ, `r_oct` or R would have to be for that, and say whether the corpus anywhere
  places the model there.
- Is the boxed value perhaps the *correct* object and the computed one a different quantity —
  a bare coupling versus a screened one, a per-sphere versus a per-void figure, a surface versus a
  bulk figure? App J's own §1.3 and §2.1 bear on this. Resolve it from the text, not by preference.
- Does the discarded factor appear correctly elsewhere, such that dropping it here is a
  transcription slip rather than a physics claim?
- **If the boxed value survives, the gate closes in favour of the corpus.** Say so plainly. Two
  prior gates recorded outcomes their prompts did not anticipate and were right to.

## 3 — STEP 2: DIMENSIONS AND CONVENTION

Independently of which value wins, establish:

- whether the printed expression is dimensionally consistent as written;
- what unit convention it silently assumes, and what the expression becomes under the alternatives
  the corpus uses elsewhere;
- whether the same convention question has arisen at other locations, and whether it is local to
  this appendix or structural.

## 4 — STEP 3: DOWNSTREAM TRACE

Find **every** document in either corpus that uses a Josephson coupling numerically or cites App J
for one. Do not work from a list supplied here; build it by search and state the search.

For each, record: the location, what it uses the value for, the number it obtains, and the number
it would obtain under the Step-1 verdict. **Recompute each, do not scale them.**

## 5 — STEP 4: THE COUNT

Separate, and report as two distinct tallies:

- **published numeric predictions affected** — how many, which, and by how much;
- **structural claims affected** — named by document and section.

A gate that conflates these overstates itself. If the numeric tally is zero, say so first.

## 6 — STOP CONDITIONS

**SC-TANH-1.** The computed value is right; the boxed value is an error. → Report, with the
downstream trace and both tallies.
**SC-TANH-2.** The boxed value is right; the computed value is a different quantity or a slip. →
Report; the corpus is vindicated and the prior concern retires.
**SC-TANH-3.** Both are right, for different objects, and the corpus conflates them. → Report which
belongs where, and which downstream uses took the wrong one.
**SC-TANH-4.** The expression is not dimensionally well-formed, so neither value is determinate
until a convention is declared. → Halt on the numeric question; still deliver §4 and §5.
**SC-TANH-5.** The discrepancy does not reproduce — App J's arithmetic is internally consistent and
the premise of this gate is wrong. → Report; the gate is void and say so in the first line.

**If the outcome matches no stop condition, record it as a prompt defect rather than force-fitting
it.** No stop condition licenses a favourable conclusion, and none licenses an unfavourable one.

## 7 — DELIVERABLE

Digest or explicit refusal · **search-space coverage, before any other number** · verdict first ·
the Step-0 reproduction with every printed factor · the Step-1 steelman, including what would have
made the boxed value right · the downstream table · the two tallies kept separate · CN-TANH notices
tiered PROVEN / CONJECTURE / ASSERTED · scripts · contamination statement, including whether any
prior finding on this question reached you and when · **§0.6 reproduced verbatim** · what the gate
did **not** establish.

**Revise notices clause by clause, not headline by headline.** Three gates have shipped errors in
trailing clauses hanging off sound headlines. An "unaffected" list is a set of claims and needs the
same evidence as any other.

**Commit the deliverable, the scripts and any state to `audit/` at close, not at leisure.**

*Written 11 September 2026. Not executed. Pre-register before use.*
