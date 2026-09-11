# GATE Ψ2 — IS THE INTERIOR PHASE TIED DOWN?
## Cold Ledger gate. Fresh thread. Pre-register by SHA-256 **from the file the session receives.**

**The question.**

> App J §1.2 asserts that the interior field $\Psi_2$ costs no new field, no new coupling and no
> new free parameter. Is its phase $\theta_2$ Josephson-locked to the exterior phase $\theta_1$?
> If locked, $\Psi_2$ supplies no second independent $A_{1g}$ Goldstone. If unlocked, what fixes
> the $\alpha_0$ boundary condition?

E5 established that the shortfall against CN-R2-05's rank-9 Jacobian is **exactly one $O_h$-scalar
mode**, that Class A cannot supply it, and that $\Psi_2$ is the only candidate anywhere that claims
to cost nothing. This gate tests that claim. Notices **CN-Ψ2-01** onward.

## 0 — QUARANTINE, INHERITANCE, HANDOFF, SCOPE

**0.1** Do not run in the 10–11 Sep commissioning threads, which proposed this gate and speculated
about its outcome. **0.2 Quarantined:** those sessions; BCT-X / Sandbox TOP; the 9–10 Sep session.
**0.3 Permitted:** CN-R2-02/03/05/06, CN-OP-05/06/07/12/14, CN-PH-01, CN-P-02, E5-01…E5-05,
Theorem OP-1, App J, App JH, Letter 36. **0.4** Construction permitted.

**0.5 — HANDOFF DEFECT, FOURTH OCCURRENCE.** R2, P and J all ran without byte-exact
pre-registration. **Receive this as a file. Hash that file. Record the digest before reading on.**
A digest of text copied through a chat window certifies nothing; if that is what you have, claim no
digest and say so in §1.

**0.6 — WHAT PASSING THIS GATE BUYS. Reproduce verbatim in the deliverable, pass or fail.**

> A second independent $A_{1g}$ mode is **necessary and not sufficient** for gravity. It fills the
> one unreachable direction in CN-R2-05's Jacobian; it does not supply an induced Einstein–Hilbert
> term, a sign, or a polarisation count. **Gate Ψ2 cannot deliver gravity. At most it delivers the
> right to re-run Gate R2 Steps 2–4 with enlarged field content** — and R2's Steps 2–4 have never
> been executed by anyone, because R2 halted at Step 1. A favourable verdict here is a ticket to a
> harder gate, not a result about gravity.

## 1 — STEP 0: WHICH INTERIOR DOES THE CORPUS HAVE?

The gate cannot start until this is settled, and the corpus does not settle it:

- **App J §1.2** — one complex scalar, same GP action as the exterior, s-wave Bessel modes,
  $\kappa_0 = 3.39$; "no new field, no new coupling, no new free parameter."
- **App JH / Letter 36** (doi:10.5281/zenodo.18974754) — $\Psi_{\rm int}: B^3(R)\to\mathbb{C}^2$,
  unit-normalised, $S^3\to S^2$ classified by $\pi_3(S^2)=\mathbb{Z}$, ground state an Octet-Hopfion
  Condensate with $N_H=1$, "forced by the $\alpha_0$ Josephson boundary condition."

Both are written up as DERIVED and they are not the same object. Four copies of App JH sit in the
repo and none is marked canonical.

Determine what each requires and **run the gate separately for each interior if the corpus does not
adjudicate.** Do not pick one for tidiness. If they cannot be reconciled, that is itself the finding
and it also blocks open item 1 (Gate PT).

## 2 — THE CALCULATION

**Step 1 — Is there a Josephson coupling at all?** App J treats the double layer as a zero-thickness
shell $V(r)=\sigma_s\delta(r-R)$ with $\sigma_s=\alpha_0$, and states $\xi/R = 4.635 \gg 1$ — "the
condensate permeates the object… a weakly perturbing potential, not a hard wall." Determine whether
that geometry produces a phase-coupling term $\propto\cos(\theta_2-\theta_1)$, and compute its
stiffness $E_J$ from App J's own stated parameters. Do not import a value.

**Step 2 — Three horns, not two.** The relative phase $\vartheta=\theta_2-\theta_1$ is one of:

| horn | condition | consequence to establish |
|---|---|---|
| **locked** | $E_J$ large | $\vartheta$ frozen; no second Goldstone; the hole stays open |
| **unlocked** | $E_J = 0$ | second gapless $A_{1g}$ exists — go to Step 3 |
| **soft** | $E_J$ finite | $\vartheta$ **gapped**, not Goldstone |

The soft horn is the one the commissioning thread missed and the one most likely to be true.
Establish the gap explicitly, and state what a gapped relative-phase mode mediates. A gapped mode
gives a Yukawa potential, not $1/r$ — if that is right, say so and note that it fails for a *stated*
reason rather than by analogy with the locked horn.

**Step 3 — If unlocked: what fixes $\alpha_0$?** App JH says the interior ground state is *forced by
the $\alpha_0$ Josephson boundary condition*. A Josephson boundary condition that fixes anything is a
phase relation. Determine whether an unlocked $\theta_2$ leaves $\alpha_0$ undetermined. If it does,
the route buys a Goldstone at the cost of the constant the whole programme is built on.

**Step 4 — If Step 3 survives: count.** State the free parameters honestly — couplings, boundary
data, $\kappa_0$, anything the enlarged content introduces. App J §1.2's claim is *zero*. Test it
rather than repeating it.

**Step 5 — Symmetry check.** Confirm the new mode is genuinely $A_{1g}$ under $O_h$ and genuinely
independent of $\rho$, i.e. that it is not slaved by its own constraint the way $\theta_1$ is by
continuity and Euler (CN-R2-06). E5-05's lemma is *at most one $H$-singlet per order parameter*;
verify that $\Psi_2$ counts as a second order parameter rather than a second component of one.

## 3 — STOP CONDITIONS

**SC-Ψ2-1 (Step 2, locked).** $\vartheta$ frozen. → Closed; the Class B shortfall stands.
**SC-Ψ2-2 (Step 2, soft).** $\vartheta$ gapped. → Closed, with the gap and the mediated potential
stated.
**SC-Ψ2-3 (Step 3).** Unlocking leaves $\alpha_0$ undetermined. → Closed against the
zero-free-parameter claim, whichever way the physics goes.
**SC-Ψ2-4 (Step 5).** The mode is not an independent $A_{1g}$, or is slaved as $\theta_1$ is. →
Closed; independent arrival at CN-R2-06.
**SC-Ψ2-5 (Step 0).** The two interiors cannot be adjudicated from the corpus. → Halt and report;
this blocks Gate PT as well and is a finding in its own right.

**Gate G′ does not close this gate.** CN-PH-01's "$\Psi_2$ does not rescue" was decided against a
requirement for helicity $\pm1$. This gate wants helicity $0$. Do not inherit that dismissal; if the
gate closes, close it on its own grounds.

No stop condition licenses a favourable conclusion. See §0.6.

## 4 — DELIVERABLE

Digest or explicit refusal · verdict first · which interior(s) tested · CN-Ψ2 notices tiered
PROVEN / CONJECTURE / ASSERTED · scripts · contamination statement · **§0.6 reproduced verbatim
whatever the verdict.**

*Written 11 September 2026. Not executed. Pre-register before use.*
