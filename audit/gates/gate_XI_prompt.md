# GATE XI — IS ξᵢ A FIELD?
## Cold Ledger gate. Fresh thread. Pre-register by SHA-256 **from the file the session receives.**

**The question.**

> *One Medium* introduces ξᵢ, an octahedral void displacement field with three components, and
> uses it where two transverse polarisations are needed. A three-component field would supply
> those polarisations directly — without gauge variables and without the mass term a gauge field
> acquires in a condensate. **Does ξᵢ exist as a dynamical field with a Hamiltonian, or is it a
> notation used where one is needed? And if it exists, is it the elastic vacuum the same document
> excludes?**

This is the cheapest remaining route to electromagnetism in this programme. Notices
**CN-XI-01** onward.

## 0 — HANDOFF, QUARANTINE, SCOPE

**0.1 — HANDOFF.** Receive as a file at a commit-pinned `raw.githubusercontent.com` URL. `curl` to
disk, `sha256sum`, record the digest, **then** read. If pasted, claim no digest and say so in §1.

**0.2 — QUARANTINE.** Do not consult the 9–14 Sep 2026 threads, BCT-X / Sandbox TOP, or any
concurrent gate. Do not read `audit/notes/` or any `audit/gates/*/` deliverable — **in particular
not `LINK/` or `RANK/`**, which bear directly on this question. The Cold Ledger auto-loads and
cannot be partially read — if you read it, **declare it** and name the unpermitted summaries.

**0.3 — INHERITANCE IS FORBIDDEN.** Establish ξᵢ's status yourself from primary source. If a prior
finding about field content, rank, or degree-of-freedom counts reaches you, declare it in §7 and
state whether your assessment preceded it.

**0.4** Construction permitted and expected — §3 asks you to build.

**0.5 — SEARCH-SPACE AUDIT, MANDATORY, REPORTED BEFORE ANY CONCLUSION.**
- **Repo:** tarball, digest recorded. 134 `.tex`, 26 at the tree root outside `tex/`.
- **Appendices Vol 1 and Vol 2**; `audit/APPENDIX_INDEX.md` maps 245 appendices by volume and line.
- **`tex/BCT_OneMedium_JournalEdition_v2.txt`** — the primary document for this gate.
- Type every file with `file` before choosing a reader. Report page-level coverage.

## 0.6 — WHAT SETTLING THIS BUYS. Reproduce verbatim in the deliverable, whatever the verdict.

> A dynamical three-component field would make two transverse polarisations **available** to this
> programme without gauge variables. It would **not** by itself supply Maxwell's equations, a
> coupling to charge, the fine structure constant, or gravity — a vector field carries helicity 0
> and ±1, never ±2. **Gate XI decides whether a field exists, not what it does.** And a favourable
> verdict immediately owes an answer to the isotropy constraint: any elastic medium on a cubic or
> tetragonal lattice carries a fourth-rank tensor with more than one independent constant, and
> directional sound-speed variation is bounded experimentally at the 10⁻¹⁷ level. **A field that
> exists but is excluded by isotropy is not a gain.**

## 1 — STEP 0: EVERY APPEARANCE OF ξᵢ

From primary source, quoting the text. For each appearance record: location, what ξᵢ is said to
be, how many components, and — the load-bearing column — **whether that passage gives it an
energy functional, a Lagrangian, a Hamiltonian, or an equation of motion.**

Separate the results into two groups and report them separately:

- **Group A — ξᵢ appears with dynamics written.** An energy, an action, or an EOM.
- **Group B — ξᵢ appears in prose, a coupling, or a definition only.**

**If Group A is empty, that is the finding.** A field named in a coupling term but never given a
kinetic term is a notation, not a degree of freedom. Say so plainly if that is what you find.

## 2 — STEP 1: THE ISOTROPY EXCLUSION

*One Medium* contains an argument that an elastic vacuum is excluded — waves in a solid are
governed by a fourth-rank elastic tensor which cubic symmetry leaves with three independent
constants, producing directional sound-speed variation that experiment bounds severely.

- Locate it, quote it, and **re-derive its central number independently.** Do not accept the
  printed figure. State the experimental bound it invokes and check that the bound is real.
- State exactly what the argument excludes: any elastic medium, or a particular one.
- **Then ask whether ξᵢ falls inside that exclusion.** A displacement field with an elastic energy
  is what the argument rules out. If ξᵢ has no elastic energy, what energy does it have?

**If the same document both introduces ξᵢ and excludes what ξᵢ would be, report that as an
internal contradiction**, and say which side the rest of the corpus takes.

## 3 — STEP 2: CONSTRUCT IT AND COUNT

Independently of what the corpus writes, build the theory ξᵢ would need:

- the most general quadratic energy for a three-component displacement field on the BCT lattice,
  with its independent elastic constants for the actual point group (state the group, and derive
  the count);
- the dynamical matrix, its eigenvalues, and the degree-of-freedom count;
- the polarisation content: how many longitudinal, how many transverse, and their speeds;
- **whether the transverse speeds are isotropic**, and if not, by how much — computed, against the
  experimental bound from §2.

State the number of new parameters this costs. **A theory needing three elastic constants is not a
zero-free-parameter theory**; say so if that is what you find.

## 4 — STEP 3: WHAT USES ξᵢ, AND WHAT BREAKS

Find every result in the corpus that invokes ξᵢ or a displacement/vector field. For each, state
what happens under both branches — ξᵢ dynamical, and ξᵢ notational. Name documents and sections.

## 5 — STOP CONDITIONS

**SC-XI-1.** ξᵢ has written dynamics and survives the isotropy constraint. → **Favourable. Report
prominently**, with the parameter cost and §0.6 reproduced.
**SC-XI-2.** ξᵢ has written dynamics but is excluded by isotropy. → Report the exclusion with its
re-derived number.
**SC-XI-3.** ξᵢ is notation — no energy, no EOM anywhere. → Report; state what the corpus's
results that invoke it then rest on.
**SC-XI-4.** The corpus both asserts and excludes it. → Report the contradiction and which side
the rest of the corpus takes.
**SC-XI-5.** *One Medium* cannot be located in full. → Halt; report coverage.

**If the outcome matches no stop condition, record it as a prompt defect** rather than
force-fitting. **No stop condition licenses a favourable conclusion, and none licenses an
unfavourable one. This gate must be able to find that BCT has a vector field.**

## 6 — DELIVERABLE

Digest or explicit refusal · **search-space coverage before any other number** · verdict first ·
the Group A / Group B table **kept separate** · the isotropy argument re-derived · the constructed
dynamical matrix with its DOF and polarisation counts · the parameter cost · the §4 consequence
table · CN-XI notices tiered PROVEN / CONJECTURE / ASSERTED · scripts · contamination statement ·
**§0.6 reproduced verbatim** · what the gate did **not** establish.

**Revise notices clause by clause, not headline by headline.**
**At close, produce a `git format-patch` adding the deliverable, scripts and as-run prompt under
`audit/gates/XI/`. Do NOT modify `audit/NEXT.md`.**

*Written 14 September 2026. Not executed. Pre-register before use.*
