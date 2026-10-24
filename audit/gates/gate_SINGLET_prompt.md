# GATE SINGLET — CAN WRITTEN BCT STRUCTURE SUPPLY A SIGNED MEASURE?
## Cold Ledger gate. Fresh thread. Pre-register by SHA-256 **from the file the session receives.**

**Background (premises, re-check rather than inherit).** Gate PILOT closed at **SC-PILOT-3
(IMPORT)**: no faster-than-c channel BCT writes can carry Bell correlations without signalling
(2a/2b); a classical field cannot hold an N-party joint state (2c); a Bell violation appears only
with quantum structure the corpus postulates. Gate MAD (CN-MAD-04) found Letter 254's mechanism to
be a local-hidden-variable model, capped at CHSH ≤ 2.

PILOT did **not** test one of Bell's exits: **keep locality and measurement independence, give up
non-negativity of the joint measure over hidden configurations** (a signed or quasi-probability
measure). A recent construction (Hsieh, Zenodo 21301391, 10 July 2026; and HFT v22 App. H, Zenodo
21207025) takes this exit. From a non-negative local random walk on a discretised phase circle, a
single Z₂ holonomy (the antiperiodic sector of the double cover), and a squared readout of the
signed sum, it obtains E(θ) = −cos θ, CHSH = 2√2 and setting-independent marginals. BCT's written
field has an S¹ phase, and Appendix JH writes a ℂ²-valued interior field.

**The question.**

> **Does written BCT structure supply — without addition — a spin-½ readout and the three
> ingredients of the signed-measure route: (i) a non-negative local process on the phase
> variable, (ii) a Z₂ sign carried by closed loops of a double cover, (iii) a readout that squares
> a signed sum? If it does, does the resulting construction give E(θ) = −cos θ, CHSH = 2√2 and no
> signalling, and does BCT supply anything the prior construction had to assume?**

Notices **CN-SINGLET-01** onward.

## 0 — HANDOFF, QUARANTINE, SCOPE

**0.1 — HANDOFF.** Receive as a file at a commit-pinned `raw.githubusercontent.com` URL. `curl`
to disk, `sha256sum`, record the digest, **then** read. If pasted, claim no digest and say so.

**0.2 — QUARANTINE.** Do not consult the 25 Oct 2026 chat in which this card was drafted, or any
concurrent gate. Do not read `audit/notes/`. Of the `audit/gates/*/` deliverables, read **only**
`audit/gates/PILOT/` (all of it) and, in `audit/gates/MAD/gate_MAD_RESULT.md`, the verdict and
CN-MAD-04. You may read `audit/MINIMAL_BCT.md` §0–2.
Corpus files are read for their **written equations and actions**; prose claims are claims, not
results:
- `BCT_Letter254_Entanglement.tex` **as of commit `501ea793df505442375a3065a64a0c0e87189ee0`**
  (`git show 501ea79:BCT_Letter254_Entanglement.tex`; SHA-256 of that content
  `d849e96dd52ec43c43f581d98e4cae0e3586f3bd38d0c3397f2aa6dc4863b32d`). Do not read later revisions.
- the Appendix JH source — several versions exist in `tex/`; state which you treat as canonical
  and why; `tex/BCT_Appendix_J_SphereAction.tex`; `tex/BCT_Appendix_AZ6.tex`;
  `tex/BCT_Appendix_AZ7.tex`; `tex/BCT_Letter36_OHC_tex.tex`; `tex/BCT_Letter60.tex`;
  `tex/BCT_Letter64.tex`; `tex/BCT_OneMedium_JournalEdition_v2.txt`; `tex/BCT_Monograph_PLB.tex`
  (search only).
Prior constructions may be read in full as literature: Hsieh's two Zenodo records above (if a file
will not download, ask the user to attach it), and the references in §4.

**0.3 — INHERITANCE IS FORBIDDEN.** PILOT's and MAD's findings are premises to re-check where this
gate leans on them, not to cite as settled. Any second-hand summary of a mechanism must be traced
to a written equation or declared under "untraced claims".

**0.4** Derivation first; light numerics second.

## 0.6 — WHAT SETTLING THIS BUYS. Reproduce verbatim in the deliverable, whatever the verdict.

> This gate asks whether BCT's own written structure supplies the one route to quantum
> correlations that Gate PILOT did not test. It does **not** test quantum mechanics:
> E(θ) = −cos θ is already confirmed by loophole-free Bell experiments, so reproducing it is a
> consistency requirement, not a prediction. **A survivor does not vindicate BCT** — it shows BCT
> can host entanglement by the signed-measure route, and counts only if BCT supplies an
> ingredient the prior construction had to assume. **An import or a kill does not refute the rest
> of BCT** — it means entanglement must be added to BCT rather than explained by it, and Letter
> 254's physical claim stays withdrawn. A single number equal to cos 45°, or 2√2 at one setting,
> does not count: the whole curve is required.

## 1 — STEP 0: BASELINE AND POSITIVE CONTROL

By script:
1. Enumerate the 16 deterministic local strategies and confirm max |CHSH| = 2.
2. **Positive control.** Re-implement the signed-measure construction independently (a lazy
   nearest-neighbour walk on a 2m-site double cover of an m-site phase circle, antiperiodic
   projection, sum over source framing, squared readout) and confirm E(θ) = −cos θ, |CHSH| = 2√2
   and setting-independent marginals. Also confirm that dropping the Z₂ sign, or the squaring,
   loses the violation. **This gate must be able to find a survivor.**

## 2 — STEP 1: THE CARRIER (spin-½ readout)

Identify, from **written actions or equations**, a degree of freedom with a two-outcome readout
along an arbitrary axis whose state overlap is cos(θ/2). Candidates to examine at minimum: the
written S¹ phase (with or without a double cover); Appendix JH's ℂ² interior field and its
S³ → S² structure; vortex strings. For each: written / addable (state the addition) / absent.
State the target manifold and the relevant homotopy group before using any topological invariant.
PILOT §4 (topology before invariants) and `MINIMAL_BCT.md` §0–2 are premises to re-check, not
inherit.

## 3 — STEP 2: THE THREE INGREDIENTS

For each, cite file and equation, or report NONE FOUND and state the minimal addition:
- **(i) Non-negative local process** on the phase variable: a written transfer operator, master
  equation or stochastic rule (not the deterministic Gross–Pitaevskii flow unless a stochastic
  reading is written).
- **(ii) Z₂ sign on loops of a double cover.** Possible sources: half-integer winding or
  half-quantum vortices of the written field; the SU(2) double cover of a ℂ² field; a spin
  structure fixed by the lattice point group. A choice of antiperiodic sector that the written
  theory leaves free is an **addition**, not a supply.
- **(iii) Squared readout.** A written measurement rule that squares a signed sum (Born). A rule
  postulated in the corpus counts as postulated, not derived.

## 4 — STEP 3: CURVE, SIGNALLING AND PRIOR ART

If (i)–(iii) are all supplied, build the construction on BCT's own variables and compute E(θ) at
≥ 13 angles in [0, π], CHSH at (0, π/2, π/4, 3π/4), and each single-wing marginal as the distant
setting varies, under complete readout. Then compare with Hsieh (Zenodo 21301391; HFT v22 App. H,
Zenodo 21207025); Christian, *R. Soc. Open Sci.* 5, 180526 (2018), and its published critiques;
Mosseri & Dandoloff, *J. Phys. A* 34, 10243 (2001); and the quasi-probability literature Hsieh
cites (Wigner 1932; Spekkens 2007; Fine 1982). A BCT construction counts as BCT's own only if
BCT's written structure supplies an ingredient the prior construction assumed.

## 5 — STEP 4: THE STEELMAN

**Required, both directions.** For: the compact S¹ phase on a lattice is the same kind of object
as the prior construction's phase register; a ℂ² field carries an SU(2) double cover. Against: a
spin structure is extra data a scalar field does not fix; a scalar condensate has no half-quantum
vortices; `MINIMAL_BCT.md` records per-sphere interior structure as closed (ξ > a); the squared
readout is a postulate in the prior construction too. If the steelman for one side succeeds, say so prominently.

**Stated prior: SC-SINGLET-2 (import).** The run must be able to overturn it.

## 6 — STOP CONDITIONS

**SC-SINGLET-1 — Survivor.** A spin-½ readout and ingredients (i)–(iii) are all written in BCT
primary sources (cited), the construction gives E(θ) = −cos θ at every tested angle
(|ΔE| < 10⁻³), |CHSH| = 2√2 ± 10⁻³ and marginals independent of the distant setting (< 10⁻⁹), and
BCT supplies at least one ingredient the prior construction had to assume. → **Favourable.** Tier
CONJECTURE until independently replicated; the prior construction must be cited.
**SC-SINGLET-2 — Import.** The curve can be built on BCT variables only by adding one or more
ingredients (name each), or BCT supplies nothing the prior construction did not already assume.
→ BCT is compatible with the signed-measure route but does not explain it.
**SC-SINGLET-3 — No carrier.** No written or minimally addable degree of freedom gives a spin-½
readout, so the singlet correlation cannot be posed on BCT variables. → Letter 254's claim stays
withdrawn; report the minimal addition needed.
**SC-SINGLET-4 — Signalling.** A construction reaches −cos θ but a marginal depends on the distant
setting. → Kill that construction.
**SC-SINGLET-5 — Undetermined.** The written definitions conflict (for example S¹ versus ℂ² for
the same field) and the verdict differs between branches. → Report every branch and state what
must be decided.

**If the outcome matches no stop condition, record it as a prompt defect.** **No stop condition
licenses a favourable conclusion, and none licenses an unfavourable one, beyond what its text
says.**

## 7 — DELIVERABLE

Digest or refusal · **verdict first** · Step 0 baseline and positive control · carrier finding with
citations · ingredients (i)–(iii), each written / addable / absent · E(θ) table and plot if any ·
prior-art comparison · steelman both ways · CN-SINGLET notices tiered PROVEN / CONJECTURE /
ASSERTED · untraced second-hand claims · scripts · contamination statement · **§0.6 reproduced
verbatim** · what the gate did **not** establish.

**Revise notices clause by clause.** **At close, produce a `git format-patch` adding the
deliverable, scripts and as-run prompt under `audit/gates/SINGLET/`. Do NOT modify
`audit/NEXT.md`.**

*Written 25 October 2026. Not executed. Pre-register before use.*
