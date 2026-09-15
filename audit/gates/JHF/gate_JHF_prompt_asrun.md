# GATE JH-FIELD — IS THE HOPFION MEDIUM A THEORY, OR A TARGET?
## Cold Ledger gate. Fresh thread. Pre-register by SHA-256 **from the file the session receives.**

**The question.**

> The audit built "minimal BCT" from the one-component (S¹) scalar of App J, and the S¹ no-go
> results followed: no photon (Gate G′, LINK), no graviton (Gate RANK), Hopf charge identically
> zero (π₃(S¹)=0). But App JH describes a **different medium** — a two-component (S²) order
> parameter whose ground state is a crystal of Planck-scale **hopfions** (Octet-Hopfion
> Condensate, N_H=1), with the double-layer shell and the interstitial superfluid as features of
> that one textured field. **Does App JH actually contain a complete, stabilised S² field theory
> — a written action with a stabilising term whose coefficient is fixed, not free — or is it a
> physical picture described in prose that has not been written down as a theory?**
>
> If it is a complete stabilised action, the photon question can at last be asked on S² ground,
> where the S¹ no-go results do not reach — a separate, later gate. If it is not, the hopfion
> medium is a research target, and that is its honest status until it is written down.

Notices **CN-JHF-01** onward.

## 0 — HANDOFF, QUARANTINE, SCOPE

**0.1 — HANDOFF.** Receive as a file at a commit-pinned `raw.githubusercontent.com` URL. `curl`
to disk, `sha256sum`, record the digest, **then** read. If pasted, claim no digest and say so.

**0.2 — QUARANTINE.** Do not consult the 9–15 Sep 2026 threads, BCT-X / Sandbox TOP, or any
concurrent gate. **Do not read `audit/notes/` or any `audit/gates/*/` deliverable** (including
`audit/gates/RATIO/`). You **may and must** read the primary source under test: every
`BCT_Appendix_JH*.tex` variant (the hopfion appendix — **not** JH4, which is Yang–Mills), the
App J / App E action if you can locate it, Letter 36, and `audit/MINIMAL_BCT.md` /
`audit/APPENDIX_INDEX.md`. You are auditing App JH; read it in full.

**0.3 — INHERITANCE IS FORBIDDEN.** Derive the topology (which homotopy group classifies the
claimed soliton, and what field content it requires) and the stability analysis (Derrick scaling;
whether a higher-derivative term is present and what it costs) **yourself**, from the `.tex` and
from standard field theory — not from any ledger summary. If a prior finding about App JH, the
S¹/S² contradiction, N_H, or ξ>a reaches you, declare it in the contamination statement.

**0.4** Construction/audit of a written action. This gate reads source and computes; it writes
**no** new Lagrangian of its own (that would be doing App JH's job for it — a permitted output is
"the action as written is incomplete," not "here is the action it should have been").

**0.5 — SEARCH-SPACE AUDIT, reported before any conclusion.** Repo tarball/tree digest recorded;
`file`-type every candidate. **Enumerate all App JH variants, diff them, and report which — if
any — is marked canonical.** (At last inventory: `JH.tex` ~556 lines; `JH (1).tex`; `JH_FINAL`
and `JH_GRRRRRRRR` ~581 lines differing by tens of bytes; none marked canonical — a theory with
no canonical text is itself a finding.) If the variants disagree on the action or the stabilising
term, the audit is of the union and the disagreement is a notice.

## 0.6 — WHAT SETTLING THIS BUYS. Reproduce verbatim in the deliverable, whatever the verdict.

> This gate decides whether the hopfion / S² medium is a written, stabilised field theory or a
> research target described in prose. It does **not** decide whether that theory has a photon,
> fermions in the voids, or gravity — each is a separate, later gate. **A verdict of "complete
> stabilised action" does not vindicate BCT** — it means the photon question can finally be asked
> on S² ground, where the S¹ no-go results (Gate G′, LINK, RANK) do not reach, and asking it is a
> separate and harder gate. **A verdict of "not a complete action" does not refute the geometry
> or the hopfion intuition** — the void radii remain the correct inradii of that packing and the
> picture may yet be right; what fails is the claim that it is *already a theory* rather than a
> target still to be written down.

## 1 — STEP 0: FIND THE ACTION

From the App JH source alone, extract — verbatim, with equation numbers — the claimed action for
the interior/medium. State plainly:

- what the field is (component count, target space) as **written in an equation**, not in prose;
- whether a complete Lagrangian density is given, or whether the "action" is a named object with
  undefined terms;
- whether App JH's field content **contradicts** the App J / App E action the minimal theory was
  built from (one complex scalar, S¹). Reproduce both and compare. This is CN-territory already
  flagged in the corpus; confirm or refute it at source.

## 2 — STEP 1: THE TOPOLOGY (derive it)

- Establish, from first principles, which homotopy group classifies the claimed hopfion and what
  target space it requires. Show that a phase-only (S¹) field gives π₃(S¹)=0 (no hopfion) and
  that a genuine Hopf charge needs an S² target (π₃(S²)=ℤ). One page, self-contained.
- Confirm whether App JH's field, **as written in its action** (Step 0), actually has that target
  space — or whether it asserts a Hopf charge on content that cannot carry one.
- Report whether N_H=1 "forced by the α₀ Josephson boundary condition" is derived or asserted.

## 3 — STEP 2: STABILITY (the load-bearing calculation)

A pure S² sigma model in 3+1D has no stable finite-size soliton — Derrick's theorem: the
two-derivative energy scales as λ under x→λx, so the texture collapses. A stabilised hopfion
(Faddeev–Niemi) requires a **higher-derivative term** with its own length scale.

- Do the Derrick scaling for the action **as App JH writes it**. Does a stabilising term appear
  in the *equation*, or only in the prose?
- If a Faddeev/Skyrme quartic term is present, **is its coefficient fixed by the geometry (α₀,
  the void radii, ξ) or is it a free parameter?** Read the coefficient off the source. This is the
  hinge: a stabiliser with a geometry-fixed coefficient is a zero-parameter save; a free or
  absent coefficient is not.
- Is the claimed hopfion **crystal** (one N_H=1 knot per lattice site) shown to be a stable or
  metastable ground state of the written action, or asserted? Note ξ/R = 4.635 (independently
  recompute): a knot core, the healing length, and the sphere radius are three lengths — check
  the source assigns them consistently rather than conflating them.

## 4 — STEP 3: THE COUNTING

Taking App JH's action as written:

- how many free dimensionless numbers beyond the S¹ theory does the stabilised S² theory require?
- is each new coupling fixed by geometry, or supplied from outside?
- state the honest parameter cost of the hopfion medium relative to "zero free parameters."

## 5 — STEP 4: THE STEELMAN

**Required.** Construct the strongest case that App JH **is** a complete, stabilised,
zero-parameter S² theory: that the stabilising term is present and its coefficient geometry-fixed,
that the hopfion crystal is a genuine ground state, and that the S¹/App-J contradiction is a
superseded draft rather than a live inconsistency. If the steelman succeeds, **say so
prominently** — this gate must be able to find a theory where one exists.

## 6 — STOP CONDITIONS

**SC-JHF-1.** No complete action is written (terms undefined, or stabiliser only in prose). →
**Halt.** The hopfion medium is a research target, not yet a theory. Legitimate, honest outcome.
**SC-JHF-2.** A complete S² action exists but the hopfion crystal is unstable, or the stabiliser
needs one or more couplings **not** fixed by geometry. → Report the parameter cost to the
zero-parameter claim.
**SC-JHF-3.** A complete, stabilised S² action exists with all couplings geometry-fixed and a
defensible ground state. → **Favourable. The photon question is now askable on S² ground** — hand
off to a separate later gate; do **not** attempt the photon here.
**SC-JHF-4.** The primary source is unauditable — variants disagree irreconcilably on the action
with none canonical. → **Halt and report;** the corpus must designate a canonical App JH first.

**If the outcome matches no stop condition, record it as a prompt defect.** **No stop condition
licenses a favourable conclusion, and none licenses an unfavourable one.**

## 7 — DELIVERABLE

Digest or refusal · **search-space coverage first** (with the JH-variant diff) · verdict first ·
the action as written (Step 0) · the topology derivation · the Derrick/stability analysis with
the stabiliser-coefficient reading · the parameter count · the steelman · CN-JHF notices tiered
PROVEN / CONJECTURE / ASSERTED · scripts · contamination statement · **§0.6 reproduced verbatim**
· what the gate did **not** establish (in particular: it does **not** answer the photon question).

**Revise notices clause by clause.** **At close, produce a `git format-patch` adding the
deliverable, scripts and as-run prompt under `audit/gates/JHF/`. Do NOT modify `audit/NEXT.md`.**

*Written 15 September 2026. Not executed. Pre-register before use.*
