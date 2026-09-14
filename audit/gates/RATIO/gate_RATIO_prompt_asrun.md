# GATE RATIO — TWO NUMBERS, OR ONE?
## Cold Ledger gate. Fresh thread. Pre-register by SHA-256 **from the file the session receives.**

**The question.**

> BCT takes two geometric inputs, r_oct and r_tet, and claims zero free parameters. In the
> minimal surviving theory — one complex scalar, GP action, void radii as input — the coupling
> α₀ enters only through the healing length ξ = 1/√(8·r_oct·r_tet), which depends on the two
> radii **only through their product**. **Does any observable of the minimal theory depend on
> r_oct and r_tet separately — on their ratio, or on either alone — or does the geometry collapse
> to a single number?**
>
> If it collapses, "two radii, zero parameters" is one number fixing one length scale, which is
> the same epistemic situation as a chosen Λ_QCD. If it does not, the geometry is doing genuine
> two-parameter work and that is the minimal theory's one untested claim.

Notices **CN-RATIO-01** onward.

## 0 — HANDOFF, QUARANTINE, SCOPE

**0.1 — HANDOFF.** Receive as a file at a commit-pinned `raw.githubusercontent.com` URL. `curl`
to disk, `sha256sum`, record the digest, **then** read. If pasted, claim no digest and say so.

**0.2 — QUARANTINE.** Do not consult the 9–14 Sep 2026 threads, BCT-X / Sandbox TOP, or any
concurrent gate. **Do not read `audit/notes/` or any `audit/gates/*/` deliverable.** You may read
`audit/MINIMAL_BCT.md`, which defines the theory under test — but note it is a construction
that has never itself been gated, and **you are not bound by its conclusions**. If its §1 is
wrong about the field content or the action, say so.

**0.3 — INHERITANCE IS FORBIDDEN.** Derive the minimal theory's observables yourself. If a prior
finding about ξ, α₀, or parameter counting reaches you, declare it in §7.

**0.4** Construction required. This gate is mostly calculation.

**0.5 — SEARCH-SPACE AUDIT, reported before any conclusion.** Repo tarball, digest recorded;
134 `.tex` with 26 at the tree root; Appendices Vol 1 (3 PDFs) and Vol 2 (a `.zip` holding an
18 MB PDF); `audit/APPENDIX_INDEX.md` for navigation. Type every file with `file` first.

## 0.6 — WHAT SETTLING THIS BUYS. Reproduce verbatim in the deliverable, whatever the verdict.

> This gate decides how many independent numbers the minimal theory contains. It does **not**
> decide whether the theory is correct, whether it predicts anything, or whether the void
> geometry is physically motivated. **A verdict of "two" does not vindicate BCT** — it means one
> claim survives that has not yet been scored, and scoring it is a separate and harder gate.
> **A verdict of "one" does not refute the geometry** — the void radii remain the correct
> inradii of that packing; what fails is the claim that the model extracts two numbers' worth of
> content from them.

## 1 — STEP 0: ENUMERATE THE OBSERVABLES

From the minimal theory's action alone — one complex scalar, GP form, on the BCT lattice — list
every quantity that is in principle observable. At minimum:

healing length ξ · sound speed c_s · the amplitude-mode gap · the phonon dispersion including
its lattice corrections · vortex core size · vortex energy per unit length · circulation quantum
· the vortex–vortex interaction · any anisotropy in c_s along the lattice axes · the condensate
depletion at a void.

For each, write it explicitly in terms of r_oct and r_tet, and **state whether it depends on the
product r_oct·r_tet only, or on the ratio / either radius separately.**

## 2 — STEP 1: THE LATTICE, WHICH IS WHERE THE RATIO COULD ENTER

The product collapses the two radii in the *continuum* GP theory. The lattice is where they
might separate. Establish, by calculation:

- the BCT lattice's actual geometry — axial ratio c/a, point group, coordination number — and
  **whether it depends on r_oct and r_tet or is fixed independently of them**;
- the phonon dispersion on that lattice to the first order at which anisotropy appears;
- **whether the directional sound speeds depend on the ratio r_oct/r_tet.** This is the most
  likely place for genuine two-parameter content, and it is the calculation that matters most.
- whether the void *positions*, as distinct from their radii, carry information the radii do not.

**If the ratio appears anywhere in a physical observable, report where, and report it first.**

## 3 — STEP 2: THE COUNTING

State the minimal theory's independent parameters explicitly:

- how many dimensionless numbers does it contain?
- how many dimensionful scales, and what fixes them?
- **is the lattice spacing a set equal to ℓ_P by assumption, or derived?** A geometry that fixes
  only ratios cannot produce a dimensionful quantity without an external scale; identify that
  scale or report that none is supplied.

Then answer plainly: **taking the minimal theory alone, how many free numbers must be supplied
from outside to compute anything measurable?**

## 4 — STEP 3: THE STEELMAN

**Required.** Construct the strongest case that the geometry does two numbers' work. Consider at
least: lattice anisotropy; the two void species having distinct occupation or distinct coupling;
any observable sensitive to void *volume* rather than *inradius*; and whether the corpus's own
formulas that use the ratio r_oct/r_tet (e.g. in App FQ's spectral zeta, App GC's κ_p) are using
it in a way the minimal theory can support.

If the steelman succeeds, **say so prominently.** This gate must be able to find two.

## 5 — STOP CONDITIONS

**SC-RATIO-1.** Some observable depends on r_oct and r_tet separately. → **Favourable. Report
which observable, and what it would take to test it.**
**SC-RATIO-2.** Every observable depends only on the product. → The geometry supplies one number.
Report what that means for the zero-parameter claim.
**SC-RATIO-3.** The question is not decidable from the minimal theory because the action is
underspecified — a convention, a scale, or a lattice detail is missing. → **Halt and report
which.** Legitimate outcome.
**SC-RATIO-4.** `MINIMAL_BCT.md` misstates the surviving theory. → Report the correction; this
gate re-scopes.

**If the outcome matches no stop condition, record it as a prompt defect.** **No stop condition
licenses a favourable conclusion, and none licenses an unfavourable one.**

## 6 — DELIVERABLE

Digest or refusal · **search-space coverage first** · verdict first · the §1 observable table with
its product/ratio column · the lattice dispersion calculation · the parameter count · the
steelman · CN-RATIO notices tiered PROVEN / CONJECTURE / ASSERTED · scripts · contamination
statement · **§0.6 reproduced verbatim** · what the gate did **not** establish.

**Revise notices clause by clause.** **At close, produce a `git format-patch` adding the
deliverable, scripts and as-run prompt under `audit/gates/RATIO/`. Do NOT modify
`audit/NEXT.md`.**

*Written 14 September 2026. Not executed. Pre-register before use.*
