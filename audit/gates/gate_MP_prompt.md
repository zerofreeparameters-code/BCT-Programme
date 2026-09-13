# GATE MP — IS THE PLANCK MASS AN INPUT OR AN OUTPUT?
## Cold Ledger gate. Fresh thread. Pre-register by SHA-256 **from the file the session receives.**

**The question.**

> A large family of BCT predictions has the form X = m_P · exp(−S), with m_P supplied as an input
> and S built from void geometry. A separate appendix is titled as deriving m_P itself from α₀.
> **Is m_P an input to the corpus, an output of it, or both — and if both, does any prediction
> chain close on itself?**

Notices **CN-MP-01** onward.

## 0 — HANDOFF, QUARANTINE, SCOPE

**0.1 — HANDOFF.** Receive as a file at a commit-pinned `raw.githubusercontent.com` URL. `curl` to
disk, `sha256sum`, record the digest, **then** read. If you received pasted text, claim no digest
and say so in §1.

**0.2 — QUARANTINE.** Do not consult the 9–12 Sep 2026 threads, BCT-X / Sandbox TOP, or any
concurrent gate. Do not read `audit/notes/`. The Cold Ledger auto-loads and cannot be partially
read — if you read it, **declare it** and name the unpermitted summaries you saw.

**0.3 — INHERITANCE IS FORBIDDEN ON THE CENTRAL QUESTION.** Establish the dependency structure
yourself from primary source. If a prior finding about m_P or about the electron mass reaches you,
declare it in §7 and state whether your derivation preceded it.

**0.4** Construction permitted.

**0.5 — SEARCH-SPACE AUDIT, MANDATORY, REPORTED BEFORE ANY CONCLUSION.**
The corpus is now fully archived in the repo. Search **all** of it:
- 134 `.tex`, **26 of them at the tree root outside `tex/`**.
- **Appendices Volume 1** — three PDFs, 240,670 words, 137 appendices.
- **Appendices Volume 2** — a `.zip` containing an 18 MB PDF, 582 pages, 151,710 words,
  108 appendices. **This volume was invisible to every gate before 12 Sep.**
- `audit/APPENDIX_INDEX.md` gives all 245 appendices by volume, code, title and line. **Use it.**
  Note codes V, W, X, Y, Z appear in two volumes with different content — cite by volume and line.
- Type every file with `file` before choosing a reader. Some mount PDFs are ZIPs of page images;
  two are raw text that no PDF tool will open.

## 0.6 — WHAT SETTLING THIS BUYS. Reproduce verbatim in the deliverable, whatever the verdict.

> Establishing whether m_P is an input or an output does **not** validate or refute any individual
> prediction, and it does not measure whether the predictions are surprising — that is a separate
> question for a separate gate. **What this gate buys is the dependency graph**: which quantities
> the corpus takes from measurement, which it claims to derive, and whether any derivation consumes
> its own output. A clean graph is a precondition for scoring anything. **A favourable verdict here
> is a ticket to a harder gate, not a result about physics.**

## 1 — STEP 0: BUILD THE DEPENDENCY GRAPH

From primary source, for each of the following, record: is it **stated as measured input**,
**claimed as derived output**, or **both**? Quote the text and give volume and line.

m_P · α₀ · r_oct, r_tet · ξ · J · Λ_QCD · v_EW · M_R (the see-saw or PH-breaking scale) ·
S_D4 = π⁵/6 · m_e · ℏ, c, G.

Then draw the graph. **If any node is both an input and an output, that is the finding**, and §2
applies to it.

## 2 — STEP 1: TEST FOR CIRCULARITY

For each node that appears as both:

- Write the derivation chain in full, each step cited.
- Ask whether the chain, followed all the way back, terminates at a measured quantity or returns
  to its own starting point.
- **A chain that terminates at measurement is not circular** — it may still be a fit, but that is a
  different defect and belongs to a different gate. Say which you have found.
- Where a derivation of X consumes a measured value of X, state the numerical consistency: does the
  derived value agree with the measured one it presupposes, and to what precision?

## 3 — STEP 2: PRECISION AGAINST INPUT PRECISION

For every prediction of the form X = m_P · exp(−S) you can locate:

- Record the claimed error, the value of m_P used, and the number of significant figures in it.
- Recompute with m_P to full CODATA precision and report the shift.
- **Flag any prediction whose claimed error is smaller than the uncertainty in its own inputs.**
  A prediction quoted to 0.01% from a 3-significant-figure input is not accurate to 0.01%.

## 4 — STEP 3: THE UNITS QUESTION

m_P is not dimensionless. Establish, from primary source, what fixes the *scale* of the BCT lattice
— what sets a = 1 ℓ_P rather than any other length. If the lattice spacing is set equal to the
Planck length by assumption, say so and state where. **A geometry that fixes only ratios cannot
predict a dimensionful quantity without an external scale.** Identify that scale, or report that
the corpus does not supply one.

## 5 — STOP CONDITIONS

**SC-MP-1.** m_P is an input everywhere; the titled derivation is a consistency check or a fit. →
Report, and state which.
**SC-MP-2.** m_P is genuinely derived, and the predictions consuming it are therefore circular. →
Report the chain in full, with the affected predictions enumerated.
**SC-MP-3.** Both, inconsistently — different documents treat it differently. → Report which do
which; this is a corpus-consistency finding, not a physics one.
**SC-MP-4.** The dependency graph cannot be built because a link is unstated. → Halt and report
which link, and what would settle it.
**SC-MP-5.** No circularity and the scale is externally fixed and declared. → **Favourable
outcome.** Report it as plainly as any other, and say what it leaves open.

**If the outcome matches no stop condition, record it as a prompt defect** rather than
force-fitting. **No stop condition licenses a favourable conclusion, and none licenses an
unfavourable one.**

## 6 — DELIVERABLE

Digest or explicit refusal · **search-space coverage before any other number** · verdict first ·
the dependency graph · the circularity analysis · the precision-against-input table · the scale
finding · CN-MP notices tiered PROVEN / CONJECTURE / ASSERTED · scripts · contamination statement ·
**§0.6 reproduced verbatim** · what the gate did **not** establish.

**Revise notices clause by clause, not headline by headline.**
**Commit deliverable, scripts and as-run prompt to `audit/gates/MP/` at close, and update
`audit/NEXT.md`.**

*Written 12 September 2026. Not executed. Pre-register before use.*
