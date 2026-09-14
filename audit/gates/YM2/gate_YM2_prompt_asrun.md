# Gate YM2 — AS-RUN PROMPT

Executed by: Claude Opus 4.8 (claude-opus-4-8), web/app chat surface.
Date executed: 14 September 2026.

## Handoff digests (recorded before reading)
- Gate prompt file (gate_YM2_prompt.md):
  - pre-registered SHA-256: ada82fc1969fc1a2eb14d0bf5aeea60fe992b2413470b10a88495f1dadb5c922 (7313 bytes)
  - computed        SHA-256: ada82fc1969fc1a2eb14d0bf5aeea60fe992b2413470b10a88495f1dadb5c922 (7313 bytes)  -> MATCH
- Corpus tarball (BCT-Programme @ 12ae196):
  - computed SHA-256: 1b5924484b84aef2bb8253183f02d2ef8142ce64aa57fbccf70aa6455b8a43cc (45712225 bytes) [pinned corpus state]

## Verbatim prompt as received
```markdown
# GATE YM2 — IS THE FINITE-LATTICE MASS GAP PROVEN?
## Cold Ledger gate. Fresh thread. Pre-register by SHA-256 **from the file the session receives.**

**The question.**

> Appendix JH4 constructs a lattice gauge theory on the BCT D4 lattice at a geometrically fixed
> bare coupling and claims: (a) the finite-lattice theory exists and satisfies the
> Osterwalder–Schrader axioms at every lattice spacing, and (b) it has a strictly positive spectral
> gap δ_latt > 0. **Are (a) and (b) proven, as stated, at the standard of rigour their own tier
> statement claims — and does the version history of this appendix tell a consistent story?**

Notices **CN-YM2-01** onward. Supersedes the unrun 12 September `gate_YM_prompt.md`
(SHA-256 `9cec524a602ace2cf8f2b98029b87ec8b68998406838d2255931b16cd2fca096`), whose file was lost
before execution. **That pre-registration is void and is recorded as never used.**

## 0 — HANDOFF, QUARANTINE, SCOPE

**0.1 — HANDOFF.** Receive as a file at a commit-pinned `raw.githubusercontent.com` URL. `curl` to
disk, `sha256sum`, record the digest, **then** read. If you received pasted text, claim no digest
and say so in §1.

**0.2 — QUARANTINE.** Do not consult the 9–14 Sep 2026 threads, BCT-X / Sandbox TOP, or any
concurrent gate. Do not read `audit/notes/` or any `audit/gates/*/` deliverable. The Cold Ledger
auto-loads and cannot be partially read — if you read it, **declare it** and name the unpermitted
summaries you saw.

**0.3 — INHERITANCE IS FORBIDDEN.** Assess JH4 on its own mathematics. Do not inherit any prior
finding about this appendix, its tier, or its version history. If one reaches you, declare it in
§7 and state whether your assessment preceded it.

**0.4 — EXTERNAL LITERATURE PERMITTED AND EXPECTED.** Osterwalder–Schrader, Balaban's
renormalisation-group programme, Jaffe–Witten's official Millennium Problem statement, and the
standard lattice-gauge-theory literature are admissible and should be read rather than recalled.
**Cite only what you actually open.**

**0.5 — SEARCH-SPACE AUDIT, MANDATORY, REPORTED BEFORE ANY CONCLUSION.**
- **Repo:** tarball, digest recorded. 134 `.tex`, 26 at the tree root outside `tex/`.
- **Appendices Vol 1 and Vol 2**, and `audit/APPENDIX_INDEX.md` for navigation. Type every file
  with `file` before choosing a reader.
- **JH4 itself.** Locate **every** version you can reach, and treat the set as evidence:
  the repo copy, any appendix-volume copy, and **the public Zenodo deposition
  `10.5281/zenodo.21781545`**, which is reachable and should be fetched. Record for each: its
  date, its title, its abstract's claim, and its tier statement. **If the versions differ in what
  they claim, that difference is a finding of this gate**, not a distraction from it.

## 0.6 — WHAT SETTLING THIS BUYS. Reproduce verbatim in the deliverable, whatever the verdict.

> A sound finite-lattice existence-and-gap result is **real mathematical physics** and is worth
> having on its own terms. It is **not** the Clay Millennium Problem, which requires a continuum
> measure on ℝ⁴ and a non-perturbative control of a → 0 that has resisted proof for seventy years.
> **Gate YM2 can confirm or refute the finite-lattice claim only.** A favourable verdict does not
> solve Yang–Mills, does not earn a prize, and must not be reported as if it did. An unfavourable
> one does not show the construction is worthless — it locates where the argument stops.

## 1 — STEP 0: WHAT IS ACTUALLY CLAIMED, AND BY WHICH VERSION

Tabulate every JH4 version located, with date, title, abstract claim, and tier statement, quoted.
State plainly which version is the **public record** — the one a reader following the DOI receives
— and whether the public record matches the most recent version.

## 2 — STEP 1: AUDIT THE OS AXIOMS CLAIM

The claim is that the finite-lattice theory satisfies Osterwalder–Schrader at every lattice
spacing. For each axiom — **OS0 analyticity, OS1 regularity, OS2 Euclidean invariance,
OS3 reflection positivity, OS4 ergodicity** — establish:

- does JH4 prove it, cite it, or assume it?
- for anything cited: is the citation to a theorem that actually covers this case — compact gauge
  group, this lattice, this action — or to a nearby result?
- **OS2 deserves particular care.** Euclidean invariance on a lattice holds only in the continuum
  limit; on a fixed lattice the symmetry group is the lattice point group. State how JH4 handles
  this, or whether it does.

**Standard results honestly cited are a strength, not a weakness.** The question is whether the
citation covers the case, not whether JH4 re-proves known theorems.

## 3 — STEP 2: AUDIT THE SPECTRAL GAP

- Write out JH4's derivation of δ_latt > 0 in full, step by step, and recompute every number.
- Identify the mechanism. If it is a strong-coupling expansion, state its radius of convergence and
  whether g² = π⁵/24 lies inside it. **Compute this; do not accept a claim about it.**
- Establish whether the gap is uniform in a or degrades as a → 0.
- State any premise carried without proof.

## 4 — STEP 3: THE COUPLING

g² = π⁵/24 is said to be geometrically fixed. Establish where that value comes from, whether it is
derived or chosen, and — separately — whether the theory is claimed to hold **only** at that
coupling or over a range. **A theory at one fixed coupling is a different object from a theory with
a renormalisation trajectory**; say which JH4 has.

## 5 — STOP CONDITIONS

**SC-YM2-1.** Both (a) and (b) proven at the stated standard. → **Favourable. Report it plainly**,
with §0.6 reproduced, and state exactly what it does and does not establish.
**SC-YM2-2.** (b) proven, (a) partially — one or more OS axioms assumed or cited beyond their
scope. → Report which, and whether the gap survives without them.
**SC-YM2-3.** Neither proven as stated; the argument stops earlier than claimed. → Report where.
**SC-YM2-4.** The versions disagree about what is claimed, and the public record overstates the
current version. → **Report this first, whatever else you find.** It is a matter of the public
record, not of mathematics.
**SC-YM2-5.** JH4 cannot be located in full. → Halt; report coverage.

**If the outcome matches no stop condition, record it as a prompt defect** rather than
force-fitting. **No stop condition licenses a favourable conclusion, and none licenses an
unfavourable one. This gate must be able to confirm that the finite-lattice result is sound.**

## 6 — DELIVERABLE

Digest or explicit refusal · **search-space coverage before any other number** · verdict first ·
the version table · the OS axiom-by-axiom table · the gap derivation recomputed · the coupling
finding · CN-YM2 notices tiered PROVEN / CONJECTURE / ASSERTED · scripts · external citations, each
actually opened · contamination statement · **§0.6 reproduced verbatim** · what the gate did
**not** establish.

**Revise notices clause by clause, not headline by headline.**
**At close, produce a `git format-patch` adding the deliverable, scripts and as-run prompt under
`audit/gates/YM2/`. Do NOT modify `audit/NEXT.md` — concurrent patches conflict there.**

*Written 14 September 2026. Not executed. Pre-register before use.*
```
