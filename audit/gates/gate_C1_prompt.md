# GATE C1 — DOES THE INTERIOR CARRY ITS OWN HEALING LENGTH?
## Cold Ledger gate. Fresh thread. Pre-register by SHA-256 **from the file the session receives.**

**The question.**

> BCT has a healing length ξ, fixed by the corpus's own parameters. The sphere interiors may be
> governed by that same ξ, or may carry their own ξ₂. Which of those holds decides whether the
> condensate can vary on the scale of a single sphere, and therefore whether site-local structure
> is available at all. **Which does the corpus have, and what determines it?**
>
> Derive ξ yourself. Its value, its relation to the lattice spacing, and whether one or two healing
> lengths exist are all findings of this gate, not inputs to it.

Notices **CN-C1-01** onward.

## 0 — HANDOFF, QUARANTINE, SCOPE

**0.1 — HANDOFF.** Receive as a file at a commit-pinned `raw.githubusercontent.com` URL. `curl` to
disk, `sha256sum`, record the digest, **then** read. A digest of pasted text certifies nothing; if
that is what you have, claim no digest and say so in §1.

**0.2 — QUARANTINE.** Do not consult the 9–11 Sep 2026 threads, BCT-X / Sandbox TOP, or any other
gate running concurrently. The Cold Ledger auto-loads and cannot be partially read — if you read
it, **declare it** and name the unpermitted gate summaries you saw.

**0.3 — INHERITANCE IS FORBIDDEN ON THE CENTRAL QUESTION.** A note in `audit/notes/` argues a
position on this exact question. **Do not read it, do not cite it.** Derive ξ and its scope
yourself from primary source. If it reaches you anyway, declare it in §7 and state whether your
derivation preceded it. A session that confirms an earlier conclusion by reading it has produced
nothing.

**0.4** Construction permitted.

**0.5 — SEARCH-SPACE AUDIT, MANDATORY, REPORTED BEFORE ANY CONCLUSION.**
- **Repo:** pulled by tarball, digest recorded. **134 `.tex`, 26 at the tree root outside `tex/`.**
  A `tex/*.tex` glob covers 108 and is not the corpus.
- **Mount:** of 49 files, 33 are **ZIP archives** of page images with `.txt` layers, 14 are true
  PDFs, and **2 are raw UTF-8 text** that `file` reports as `data` — neither `pdftotext`,
  `pymupdf` nor `unzip` opens those two, and App J, K, AG, AN, AT and AY live in them. **Type every
  file with `file` and handle by actual type.** Report page-level coverage.

## 0.6 — WHAT SETTLING THIS BUYS. Reproduce verbatim in the deliverable, whatever the verdict.

> Determining ξ₂ does **not** validate or refute any BCT prediction, supply a mechanism, or close
> a sector. What it decides is **which regime the model is in**, and therefore which claims are
> even available to be argued. A single healing length longer than the lattice spacing forbids
> site-local structure; an independent short interior healing length permits it. **Either verdict
> is a precondition for other work, not a result about physics.** A favourable verdict is a ticket
> to a harder question, not an answer to one.

## 1 — STEP 0: IS THERE A SECOND FIELD TO CARRY A SECOND ξ?

Gate INT returned **SC-INT-4**: three distinct interior commitments in the corpus, re-scoped to
enumeration. This gate inherits that fact and nothing else from it.

Enumerate, from primary source, every interior the corpus commits to, and for each record whether
it **has** an independent healing length:

| for each interior | record |
|---|---|
| location and quoted text | |
| is the interior a separate field, or a restriction of the exterior field? | |
| does it carry its own stiffness J₂ and chemical potential? | |
| is ξ₂ stated, derived, assumed equal to ξ, or absent? | |

**A restriction of one field to a subregion has no second healing length**, by construction. If all
interiors are restrictions, the gate closes at Step 0 and §2 does not run. Say so if so.

## 2 — STEP 1: WHAT FIXES ξ₂, IF ANYTHING?

For each interior that could carry one:

- Derive ξ from primary source, stating which equation gives it and where. Do not import a value from anywhere.
- Establish what ξ₂ would be **on the corpus's own stated inputs** — the interior GP action, the
  interior density, the interior stiffness. Where an input is missing, say which and stop.
- Test the specific argument that ξ₂ = ξ: that the same quartic and the same stiffness force it.
  **Steelman the opposite.** What would have to be true of the sphere interior — different density,
  different coupling, confinement — for ξ₂ ≪ a? Is any of it stated, derivable, or excluded?
- If ξ₂ is not determined, say what would determine it and at what cost in new parameters.

## 3 — STEP 2: THE REGIME, AND WHAT EACH BRANCH PERMITS

A lattice of condensates has two limits: ξ ≫ a, one order parameter over many sites; and ξ ≪ a,
per-site condensates weakly linked. **Establish which limit each branch of Step 1 places the model
in**, by computation, not by assertion.

Then, for **each** branch taken in turn, list what it permits and what it forbids. Name documents
and sections, not sectors. At minimum resolve: interior condensate modes and their κ values; the
Josephson network; site-local topological charge; the interior phase velocity; and the chemistry
series that depends on per-sphere structure.

**Both columns must be filled.** A consequence map with one branch worked and the other waved at is
the failure this step exists to prevent.

## 4 — STEP 3: THE MODE CHARACTER CHECK

Independently of ξ₂, establish where the corpus's interior modes sit relative to the Bogoliubov
crossover at kξ ~ 1. Compute kξ for each stated interior mode. State whether they are collective
(phonon-branch) or single-particle excitations, and whether the corpus's description of them
matches. Quote what the corpus says about their character.

## 5 — STOP CONDITIONS

**SC-C1-1.** The corpus determines ξ₂ = ξ. → Report, with the primary text, and deliver §3.
**SC-C1-2.** The corpus determines ξ₂ ≠ ξ, with a stated value or bound. → Report; the granular
regime is available and §3's other column applies.
**SC-C1-3.** ξ₂ is not determined by the corpus. → **Halt and report.** Deliver §3 both ways and
state what input would settle it. This is a legitimate outcome, not a failure to finish.
**SC-C1-4.** No interior is a separate field, so no second ξ exists to determine. → Report; the
question dissolves and §2 does not run.
**SC-C1-5.** ξ itself is not determined — the corpus gives conflicting values or conventions. →
Report; this gate is blocked and so is anything downstream of ξ.

**If the outcome matches no stop condition, record it as a prompt defect** rather than force-fitting
it. No stop condition licenses a favourable conclusion, and none licenses an unfavourable one.

## 6 — DELIVERABLE

Digest or explicit refusal · **search-space coverage before any other number** · verdict first ·
the Step-0 table in full · ξ derived from source with its equation cited · the ξ₂ analysis with the
steelman · the two-column consequence map · the mode-character table · CN-C1 notices tiered
PROVEN / CONJECTURE / ASSERTED · scripts · contamination statement including whether any prior
finding on this question reached you and when · **§0.6 reproduced verbatim** · what the gate did
**not** establish.

**Revise notices clause by clause, not headline by headline.** An "unaffected" list is a set of
claims and needs the same evidence as any other.

**Commit the deliverable, scripts and as-run prompt to `audit/gates/C1/` at close, and update
`audit/NEXT.md`.** Not at leisure. Unarchived deliverables have already caused later gates to print
false claims.

*Written 11 September 2026. Not executed. Pre-register before use.*
