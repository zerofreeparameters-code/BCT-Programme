# GATE KL — DOES THE WOVEN KNOT-LATTICE STAND UP?
## Cold Ledger gate. Fresh thread. Pre-register by SHA-256 **from the file the session receives.**

**The question.**

> Gate JHF (SC-JHF-1) found App JH writes no stabilised S² action: the free energy is a
> two-derivative Gross–Pitaevskii functional with no Faddeev term, so a lone hopfion collapses
> (Derrick), and even with a geometry-fixed Faddeev term the knot's size comes out at the healing
> length ξ ≈ 2.3 lattice spacings — far bigger than one sphere. The proposed escape is to stop
> demanding one localised knot per sphere and instead let the vacuum be **one space-filling,
> FCC-periodic S² texture** — a *knot lattice* in which the texture size ~ξ exceeds the lattice
> period and neighbouring knots overlap (as in a skyrmion lattice), so there is no lonely soliton
> left to collapse. **Under the Faddeev–Niemi / Babaev–Faddeev–Niemi energy, with coefficients
> fixed by the condensate stiffness and ξ (not tuned), does such a modulated S² crystal exist as a
> stable or metastable ground state — energetically below the uniform state, with the claimed
> integer topological charge per cell, and with every coupling geometry-fixed — or does it not?**
>
> If it does, the S² ground the photon question needs finally exists (a separate, later gate). If
> it does not, the hopfion-medium programme forecloses along this route and every downstream gate
> (photon, void-fermions, gravity) is spared.

Notices **CN-KL-01** onward.

## 0 — HANDOFF, QUARANTINE, SCOPE

**0.1 — HANDOFF.** Receive as a file at a commit-pinned `raw.githubusercontent.com` URL. `curl`
to disk, `sha256sum`, record the digest, **then** read. If pasted, claim no digest and say so.

**0.2 — QUARANTINE.** Do not consult the 9–15 Sep 2026 threads, BCT-X / Sandbox TOP, `gate-jhf`,
or any concurrent gate. **Do not read `audit/notes/` or any `audit/gates/*/` deliverable**
(including `audit/gates/JHF/` and `audit/gates/RATIO/`). You **may and must** read the primary
sources: every `BCT_Appendix_JH*.tex` (the hopfion appendix — **not** JH4), the App J / App E
action if locatable, Letter 36, `audit/MINIMAL_BCT.md`, `audit/APPENDIX_INDEX.md`, and the
standard literature on the Faddeev model and two-component-condensate knot solitons
(Faddeev–Niemi Nature 387 (1997) 58; Babaev–Faddeev–Niemi PRB 65 (2002) 100512; Sutcliffe
Proc. R. Soc. A 463 (2007) 3001; Vakulenko–Kapitanskii for the energy bound).

**0.3 — INHERITANCE IS FORBIDDEN.** Derive the following **yourself**, from field theory and the
`.tex`, not from any ledger or gate summary: (a) the reduction of a two-component GP free energy to
a Faddeev energy for the S² direction n̂, and the resulting coefficients c₂, c₄ in terms of the
condensate stiffness, gap, and healing length ξ; (b) the Derrick / stability analysis for a
**periodic** texture (the box is now the unit cell, not empty space); (c) ξ/a from the void radii,
cold. If a prior finding about App JH, the S¹/S² contradiction, ξ/R, N_H, the collapse of the lone
knot, or the c₄∼ξ² scaling reaches you, declare it in the contamination statement and re-derive.

**0.4 — SCOPE.** This gate **analyses a standard, literature-defined energy** (Faddeev / BFN) on a
periodic ansatz and computes whether it has a stable modulated minimum. Writing that energy down
is permitted **because it is the standard functional, not an ad-hoc BCT construction** — but you
may **not** invent new terms, and you may **not** tune any coefficient away from its
geometry-derived value to manufacture stability (that is the selected-fit failure; if stability
needs a tuned coefficient, that is SC-KL-2, report the cost). Permitted outputs: "no stable
geometry-fixed crystal exists," or "a stable geometry-fixed crystal exists," or "stability needs a
non-geometry coupling of size X." You do **not** address the photon, fermions, or gravity here.

**0.5 — THE PREMISE, STATED AS A COST.** The S² (two-component) order parameter is **not** the
corpus's written field content — MINIMAL_BCT and App JH's own equation of motion (Eq. GP) are
one-component (S¹). Promoting to S² is the premise of this gate and its first declared cost. A
verdict of SC-KL-3 therefore establishes the ground for a *hypothetical* S² theory; it does **not**
retroactively make App JH a written theory (that still owes a complete stabilised action). Record
this explicitly.

**0.6 — SEARCH-SPACE AUDIT, reported before any conclusion.** Repo tree digest / HEAD SHA recorded;
`file`-type the JH variants; confirm which (if any) is canonical (a theory with no canonical text is
a finding). State the FCC/BCT identification (c/a=√2) and the lattice period you adopt, and derive
ξ/a and R_s/a cold before any energy is written.

## 0.7 — WHAT SETTLING THIS BUYS. Reproduce verbatim in the deliverable, whatever the verdict.

> This gate decides whether a woven, FCC-periodic S² knot-lattice is a stable geometry-fixed ground
> state of the standard Faddeev/BFN energy. It does **not** decide whether that lattice has a
> photon, fermions, or gravity — each is a separate, later gate. **A verdict of "stable
> geometry-fixed crystal" does not vindicate BCT** — it means the S² ground the photon question
> needs now exists, and asking the photon question is a separate and harder gate. It also does not
> supply App JH a written action; that remains owed. **A verdict of "no stable crystal" does not
> refute the geometry** — the void radii, the percolating interstitial network, and α₀ remain
> correct; what fails is the specific claim that a knot-lattice is the vacuum's ground state.

## 1 — STEP 0: THE ENERGY AND THE COEFFICIENTS (derive, don't posit)

- Write the two-component GP free energy for Ψ ∈ ℂ² and reduce it, at fixed |Ψ|=√ρ₀, to an energy
  for n̂ = Ψ†σΨ/ρ₀ ∈ S². Exhibit the two-derivative term c₂(∂n̂)² and, from the next order of the
  gradient expansion / integrating out the amplitude mode, the four-derivative Faddeev term
  c₄ F_ij² with F_ij = n̂·(∂ᵢn̂×∂ⱼn̂).
- Read off c₂ and c₄ **in terms of ρ₀, m, g and ξ**. State plainly whether c₄ is fixed by the
  geometry (through ξ) or whether the reduction leaves it free. Derive, with the gradient-expansion
  small parameter identified, the scaling c₄/c₂ ∼ ξ² (or refute it).
- Confirm cold: ξ/a = 1/√(8π α₀), α₀ = r_oct·r_tet/π, r_oct=(√2−1)/2, r_tet=(√6−2)/4 (60 dps,
  report 40). State the resulting natural knot size λ\* = √(c₄I₄/(c₂I₂)) relative to the FCC period.

## 2 — STEP 1: THE PERIODIC STABILITY CALCULATION (the load-bearing computation)

- Set up an FCC-periodic S² texture ansatz with one unit of the relevant charge per primitive cell
  (state which charge: Hopf H per cell, or a baby-Skyrme/π₂ charge per 2D section — justify the
  choice from the topology of a *periodic* map, which is **not** the same as π₃(S²) for a map from
  S³; a 3-torus target has its own homotopy content — establish it).
- Compute the energy per cell of the modulated texture vs the uniform state, at the geometry-fixed
  c₂, c₄. Is the modulated state a local minimum (metastable) or the global minimum (stable), or is
  the uniform state always lower? Do the Derrick scaling **in the fixed cell** (period pinned):
  which deformations lower the energy?
- Report whether the natural size λ\* ∼ ξ ≈ 2.3a being larger than the period is compatible with a
  stable overlapping-knot crystal (as in a skyrmion lattice) or whether overlap destroys the charge
  / the minimum. This is the crux the woven picture rests on — decide it by computation.

## 3 — STEP 2: SELF-CONSISTENCY AND THE COUNTING

- Is the crystal self-consistent: does the geometry-fixed c₄ give a period equal to the FCC lattice
  constant, or must the period be imposed independently (a second length)? Count the free
  dimensionless numbers beyond the S¹ theory: the S² promotion (premise, §0.5), plus any coupling
  that stability requires which is **not** fixed by geometry.
- State the honest parameter cost of the knot-lattice relative to "zero free parameters."

## 4 — STEP 3: THE STEELMAN

**Required.** Construct the strongest case that a stable, geometry-fixed, FCC-periodic S² knot
crystal **exists** and carries integer charge per cell with no tuned coupling. If it succeeds, say
so **prominently** — this gate must be able to find a ground state where one exists. Cite the
skyrmion-lattice and BFN-crystal literature at primary source; do not assert stability from analogy
alone.

## 5 — STOP CONDITIONS

**SC-KL-1.** No modulated crystal is a stable or metastable minimum under the geometry-fixed energy
(uniform state always lower, or the texture unwinds). → **Halt.** The knot-lattice is not a ground
state; the hopfion-medium route forecloses. Legitimate, honest outcome.
**SC-KL-2.** A modulated crystal exists but only with ≥1 coupling **not** fixed by geometry (c₄
tuned away from its gradient-expansion value, or an imposed period). → Report the parameter cost.
**SC-KL-3.** A stable, geometry-fixed modulated S² crystal exists (energy below uniform, integer
charge per cell, all couplings geometry-fixed). → **Favourable. The S² ground now exists** — hand
the photon question to a separate later gate; do **not** attempt it here. (Still owes App JH a
written action per §0.5.)
**SC-KL-4.** The BFN reduction is inapplicable to the BCT content, or the periodic ansatz space is
unauditable. → **Halt and report;** designate the field content and energy first.

**If the outcome matches no stop condition, record it as a prompt defect.** **No stop condition
licenses a favourable conclusion, and none licenses an unfavourable one.**

## 6 — DELIVERABLE

Digest or refusal · **search-space coverage first** · verdict first · the energy and its
geometry-fixed coefficients (Step 0) · the periodic-topology derivation · the per-cell
stability/Derrick computation with the size-vs-period decision · the parameter count · the steelman
· CN-KL notices tiered PROVEN / CONJECTURE / ASSERTED · scripts (deterministic, re-runnable) ·
contamination statement · **§0.5 and §0.7 reproduced verbatim** · what the gate did **not**
establish (in particular: it does **not** answer the photon question and does **not** supply App JH
a written action).

**Revise notices clause by clause.** **At close, produce a `git format-patch` adding the
deliverable, scripts and as-run prompt under `audit/gates/KL/`. Do NOT modify `audit/NEXT.md`.**

*Written 15 September 2026. Not executed. Pre-register before use.*
