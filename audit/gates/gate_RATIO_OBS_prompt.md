# GATE RATIO-OBS — IS AN INDIVIDUAL VOID RADIUS OBSERVABLE?
## Cold Ledger gate. Fresh thread. Pre-register by SHA-256 **from the file the session receives.**

**The question.**

> Gate RATIO closed SC-RATIO-2: every observable of the minimal theory depends on r_oct and
> r_tet only through their product, via ξ = 1/√(8·r_oct·r_tet). It left exactly one thread open
> (CN-RATIO-07): the corpus states a "structural invariant" ξ/r_oct = 1/(√8·r_oct^{3/2}·r_tet^{1/2})
> = 11.19 (Letter 19), which **does** depend on the two radii with unequal powers, and claims it is
> testable by "a sub-Planckian probe of the electron's internal structure."
>
> **Does the minimal theory — one complex scalar, GP action on the BCT lattice — contain any
> observable whose value resolves r_oct from r_tet, i.e. that depends on an individual void radius
> rather than only on the product?** Equivalently: is either void radius an in-principle observable
> of the theory, or only a parameter of a substrate the theory does not measure?
>
> If some observable resolves an individual radius, ξ/r_oct = 11.19 is a genuine prediction and the
> RATIO verdict must be qualified. If none does, ξ/r_oct is an inert restatement of ξ and the
> product, SC-RATIO-2 is final, and the individual-radius citation family retires with it.

Notices **CN-OBS-01** onward.

## 0 — HANDOFF, QUARANTINE, SCOPE

**0.1 — HANDOFF.** Receive as a file at a commit-pinned `raw.githubusercontent.com` URL. `curl`
to disk, `sha256sum`, record the digest, **then** read. If pasted, claim no digest and say so.

**0.2 — QUARANTINE.** Do not consult concurrent threads or any other gate. **Do not read
`audit/notes/` or any `audit/gates/*/` deliverable — in particular `audit/gates/RATIO/`.** This
gate exists to test Gate RATIO's own reasoning about its open thread; inheriting that reasoning
defeats it. You may read `audit/MINIMAL_BCT.md`, which defines the theory under test — but note it
is a construction that has never itself been gated, and **you are not bound by its conclusions.**

**0.3 — INHERITANCE IS FORBIDDEN.** Derive the healing length, the lattice cutoff, and the
resolution argument yourself. If a prior finding about ξ, ξ > a, the field content, or the RATIO
verdict reaches you, declare it in the contamination statement and do not rely on it.

**0.4** Construction required. You must (a) fix a precise definition of "observable" for this
theory and (b) either exhibit an operator that resolves an individual radius or prove none exists.

**0.5 — SEARCH-SPACE AUDIT, reported before any conclusion.** Repo tarball, digest recorded; type
every file with `file` first. Locate every corpus formula that uses an individual radius rather
than the product (Gate RATIO found: α₂ = r_oct²/π → v_BCT in Volume2; x_EW ∝ r_oct and
x_SU(3) ∝ r_tet in Letter127; cos θ_K = r_oct − ½ in the Monograph; ξ/r_oct = 11.19 in Letter19).
Re-derive that list yourself; do not take it on trust.

## 0.6 — WHAT SETTLING THIS BUYS. Reproduce verbatim in the deliverable, whatever the verdict.

> This gate decides whether an individual void radius is an observable of the minimal theory, and
> therefore whether ξ/r_oct = 11.19 is a prediction or a restatement. It does **not** decide
> whether the radii are the correct packing inradii (they are), nor whether a substrate-inclusive
> theory would be well-motivated, nor whether such a theory would have zero free parameters.
> **A verdict of "observable" does not vindicate BCT** — even if r_oct is separately measurable,
> the ratio r_oct/r_tet is fixed by FCC close-packing, so what is measured is a prediction of the
> packing, not a free parameter; and the measurement would lie in a substrate-inclusive theory
> that is not the minimal one. **A verdict of "not observable" does not refute the geometry** — it
> means the minimal theory sees the two radii only through ξ, exactly as Gate RATIO found.

## 1 — STEP 0: DEFINE "OBSERVABLE," THEN COUNT THE SCALES

Fix a definition before testing anything. In a field theory an observable is a functional of the
fields and their correlation functions (expectation values of operators). State whether, for this
gate, the "minimal theory" is:

- **(A) the action alone** — one complex scalar Ψ on a fixed BCT lattice, observables = functionals
  of Ψ; or
- **(B) the action plus a physically real substrate** — spheres of radius R at lattice sites with
  real interstitial voids of radii r_oct, r_tet, observables may include direct geometric probes of
  the substrate.

Report both readings. Then establish, by your own calculation, the scale hierarchy: the lattice
spacing a, the sphere radius R = a/2, the void radii r_oct, r_tet, and the healing length ξ. **Order
them.** State whether a is set to a physical unit by assumption (identify it) or derived.

## 2 — STEP 1: CAN THE FIELD RESOLVE A VOID?

Under reading (A), an individual radius is observable only if some functional of Ψ takes a value
that depends on r_oct separately from r_tet. Establish, by calculation:

- the shortest length over which a finite-energy configuration of Ψ can vary (the healing length ξ),
  and its size relative to a and to the void radii;
- whether any two-point function, condensate-depletion profile, or scattering observable of Ψ
  carries a feature at the scale of a single void radius, **given** that the field cannot vary below
  ξ. If ξ exceeds a and both void radii, state what that implies for resolving sub-a structure.
- whether the minimal action contains **any** term that references void position or an individual
  radius. If it does not, an individual radius can enter an observable only through the substrate,
  i.e. only under reading (B).

**If an operator under reading (A) resolves an individual radius, report it first.**

## 3 — STEP 2: THE SUBSTRATE ROUTE, AND ITS DOMAIN OF VALIDITY

Under reading (B), the voids are real objects and r_oct is a real length. Assess:

- what physical probe would resolve a void of radius r_oct ≈ 0.207 a, and at what wavelength;
- whether that probe lies **inside or outside** the theory's domain of validity — in particular,
  if a = ℓ_P is the cutoff, whether sub-a ("sub-Planckian") probing is describable by the theory at
  all. The corpus's own stated test (Letter 19: "a sub-Planckian probe of the electron's internal
  structure") should be assessed against the cutoff you established in Step 0.
- whether adopting reading (B) adds structure — a real elastic substrate, a probe field — that the
  minimal action does not contain, and if so, whether that structure adds free parameters. (Note
  One Medium §5.3's own exclusion of an elastic vacuum, if the corpus is invoked.)

## 4 — STEP 3: THE STEELMAN

**Required. This gate must be able to return "observable."** Construct the strongest case that an
individual radius is a genuine observable. Consider at least: a condensate-depletion profile pinned
to a specific void; a scattering resonance at a void radius; the substrate taken as ontologically
real and directly probeable; and whether ξ/r_oct = 11.19, or any of the corpus's individual-radius
formulas, can be grounded as an observable of a theory the minimal action supports. If the steelman
succeeds, **say so prominently**, and state precisely which reading (A or B) it requires and what it
costs.

## 5 — STOP CONDITIONS

**SC-OBS-1.** Some observable of the minimal theory resolves an individual void radius. →
**Favourable. Report which observable, which reading it requires, and what probe realises it.**
Gate RATIO's SC-RATIO-2 is thereby qualified for the substrate-inclusive theory.
**SC-OBS-2.** No observable of the minimal theory resolves the individual radii. → ξ/r_oct is an
inert invariant; SC-RATIO-2 is final; the individual-radius citation family (CN-RATIO-06) retires.
State the reason your own calculation establishes, whatever it is.
**SC-OBS-3.** Undecidable because the minimal theory does not fix whether the substrate is a
physical, probeable object or mere scaffolding — an ontological convention is missing. → **Halt and
report which convention must be declared.** Legitimate outcome.
**SC-OBS-4.** `MINIMAL_BCT.md` misstates the theory relevant to observability (e.g. the action does
contain a void-coupling term). → Report the correction; this gate re-scopes.

**If the outcome matches no stop condition, record it as a prompt defect.** **No stop condition
licenses a favourable conclusion, and none licenses an unfavourable one.**

## 6 — DELIVERABLE

Digest or refusal · **search-space coverage first** · verdict first · the definition of "observable"
and the two readings · the scale hierarchy with a ordered against ξ · the field-resolution argument
· the substrate-route domain-of-validity analysis · the steelman · CN-OBS notices tiered
PROVEN / CONJECTURE / ASSERTED · scripts · contamination statement · **§0.6 reproduced verbatim** ·
what the gate did **not** establish.

**Revise notices clause by clause.** **At close, produce a `git format-patch` adding the
deliverable, scripts and as-run prompt under `audit/gates/RATIO-OBS/`. Do NOT modify
`audit/NEXT.md`.**

*Drafted 15 September 2026 as the CN-RATIO-07 follow-on to Gate RATIO. Not executed. Pre-register before use.*
