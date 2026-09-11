# GATE Ψ2 — RESULT

**Run:** 11 September 2026, execution thread. Cold Ledger. One gate, this thread.
**Question:** Is the interior phase θ₂ Josephson-locked to θ₁?
**Notices:** CN-Ψ2-01 … CN-Ψ2-21.

---

## 0 — PRE-REGISTRATION

The gate file was fetched to disk and hashed **before** being opened.

| | |
|---|---|
| Pre-registered SHA-256 | `948909cbd49a3fdfbaf50863958a04629dd4399a84509ff633ced2a0878b35a4` |
| Computed SHA-256 | `948909cbd49a3fdfbaf50863958a04629dd4399a84509ff633ced2a0878b35a4` |
| Pre-registered size | 6679 bytes |
| Computed size | 6679 bytes |
| Commit | `f6de7dc14c45eb45ff8b9d52124674ac64b8a47f` |

**MATCH — byte-exact.** The handoff defect of §0.5 (fourth occurrence) is **repaired at this
gate**: the file was received as a file, fetched by `curl` from the pinned commit, and hashed
before reading. This is the first gate in the R2 → P → J → Ψ2 chain to run on a confirmed digest.

Corpus pinned alongside it: repo tarball `zerofreeparameters-code/BCT-Programme` @ `main`,
SHA-256 `86aca2692650dd66fb2464c0825e7c9a160c1bc278666e6fd65796a85c2584d7`, pulled
2026-09-11, 166 files / 108 `.tex`. (The ledger records 134 `.tex` at the 10 Sep pull; the
tree has moved. Any recount must re-pin.)

---

## 1 — VERDICT, FIRST

**The gate closes. Ψ₂ does not supply a second independent A₁g Goldstone, on either interior.**

It closes earlier and harder than the gate's three horns anticipated, because **Step 1 fails
before the horns apply: the corpus contains no Josephson coupling at all.** Both places the
corpus names one — App J §3.1 and App JH eq (13) — write a surface integral of |Ψ|², which has
no dependence on any phase difference. A mechanical scan of all 108 `.tex` files returns **zero**
occurrences of `cos(θᵢ − θⱼ)` or any equivalent. There is no E_J in the corpus to be large,
finite, or zero.

Under §0.4 a Josephson coupling was therefore **constructed** from App J's own action and
parameters, and the gate run against it. Results:

| | Interior A — App J (ℂ, one complex scalar) | Interior B — App JH (ℂ², unit-normalised) |
|---|---|---|
| **Verdict** | **SC-Ψ2-2** (soft/locked) **and SC-Ψ2-4** (not independent) | **Closed at Step 4** — no listed SC covers it |
| Why | ϑ = θ₂−θ₁ is not a degree of freedom (Ψ is continuous at R); constructed E_J gaps it at Planck scale; (n,ϑ) is one canonical pair | It *is* a second order parameter, so E5-05 permits it a singlet — but App J §1.2's "no new field, no new coupling, no new free parameter" is **false** for it |
| Cost | 0 new parameters in the action (2 conditionals, 1 undeclared unit) | ≥ 1 new field + 1 **mandatory** new coupling (κ_FS) + 1 replaced potential |

**Step 0 also fires SC-Ψ2-5.** The corpus does not adjudicate between the two interiors, and they
are not reconcilable: they are separated by a homotopy invariant. Per §1's instruction the gate
was run separately on each rather than picking one. **This blocks Gate PT**, as §3 anticipated.

**SC-Ψ2-3 does not fire as literally worded**, and this is stated plainly rather than stretched:
α₀ is fixed in App D by void geometry and is merely *used* in App J, so unlocking does not leave
α₀ undetermined. What unlocking destroys is the α₀ boundary condition's *role* — and App JH's
"forced by the α₀ Josephson boundary condition" fails at every horn for an independent reason
(CN-Ψ2-09, CN-Ψ2-10, CN-Ψ2-16).

**Gate G′ was not used.** CN-PH-01's dismissal was against helicity ±1; this gate wanted
helicity 0 and closed on its own grounds — a nonzero gap and a slaved canonical pair. Nothing
below inherits the representation obstruction.

---

## 2 — §0.6, REPRODUCED VERBATIM

*(Required in the deliverable pass or fail. The verdict above is unfavourable; §0.6 is reproduced
regardless, exactly as written in the gate file.)*

> A second independent $A_{1g}$ mode is **necessary and not sufficient** for gravity. It fills the
> one unreachable direction in CN-R2-05's Jacobian; it does not supply an induced Einstein–Hilbert
> term, a sign, or a polarisation count. **Gate Ψ2 cannot deliver gravity. At most it delivers the
> right to re-run Gate R2 Steps 2–4 with enlarged field content** — and R2's Steps 2–4 have never
> been executed by anyone, because R2 halted at Step 1. A favourable verdict here is a ticket to a
> harder gate, not a result about gravity.

---

## 3 — STEP 0: WHICH INTERIOR DOES THE CORPUS HAVE?

Both interiors were read from **primary source** (repo `.tex`), not from any summary.

**Interior A — App J §§1.1–1.2.** One complex scalar. "The BCT condensate field Ψ fills all of
space." Same GP action restricted to r < R. Quartic (J/ξ²)(|Ψ|²−Ψ₀²)²/4. **"The field Ψ itself is
continuous. Only its radial derivative jumps."** s-wave Bessel modes, κ₀ = 3.3905.

**Interior B — App JH §3.1.** Ψ_int : B³(R) → ℂ², two-component, with |Ψ_int|² = ρ₀ **fixed**.
Unit-normalised field maps S³ → S², classified by π₃(S²) = ℤ. Ground state N_H = 1.

These are not two write-ups of one object:

1. **Field content.** ℂ vs ℂ².
2. **Amplitude sector.** App J has a quartic and therefore an amplitude (Higgs) mode at 2/ξ =
   0.8630. App JH fixes |Ψ_int|² = ρ₀ and has **no amplitude mode at all**. B does not extend A;
   it deletes part of it.
3. **Homotopy — decisive.** App J's vacuum manifold is S¹: π₂(S¹) = π₃(S¹) = 0. Hopf charge is
   **identically zero** on App J's field content, for every configuration. App JH requires
   π₃ = ℤ. No amount of interpretation moves a field between these.
4. **Boundary condition.** App JH carries App J's derivative-jump BC (its eq 2) while fixing
   |Ψ_int| constant. A field of constant modulus has zero radial derivative of its modulus from
   inside, so the jump is set by the exterior alone and cannot generically equal −α₀Ψ(R).

**SC-Ψ2-5 fires.** Recorded as a finding in its own right; the gate was nevertheless run on both.

**One live concern downgraded.** The four App JH copies in the repo were diffed. All four carry
the **same 14 displayed equations, symmetric difference 0**; differences are confined to
frontmatter, a table of contents, a bibliography, and one self-citation record number (27 vs 53).
`JH (1)` and `JH_FINAL` are byte-identical. **The canonicity problem is clerical, not physical** —
it changes no verdict here, though it remains a real archival defect.

---

## 4 — STEP 1: IS THERE A JOSEPHSON COUPLING AT ALL?

**No. Not anywhere in the corpus.**

A Josephson energy must depend on a phase *difference*: E = −E_J cos(θ₂ − θ₁), from an overlap
Re(Ψ₁*Ψ₂). What the corpus actually writes, at both places it uses the word:

- **App J §3.1:** `H_int = σ_s ∮_{r=R} |Ψ|² dS = σ_s · 4πR² · |Ψ(R)|²`
- **App JH eq (13):** `F_surf = (α₀ħ²/2mR) ∮_{S²} |Ψ_int|² dA`

Both are integrals of |Ψ|². Neither contains a phase difference. **Neither is a Josephson
coupling.** The scan (`gate_PSI2_corpus_scan.py`) confirms zero `cos(phase − phase)` terms in the
whole tree.

Worse for Interior A specifically: App J §1.2 states Ψ is **continuous** at r = R. A continuous
complex field has a continuous phase. θ₂(R) = θ₁(R) is imposed as a boundary condition, not
achieved dynamically. **There is no relative phase to lock.**

### The geometry is transparent, not a weak link

Reconstructing App J's parameters from its own printed numbers (all reproduce):

| quantity | value | App J prints |
|---|---|---|
| α₀ = r_oct·r_tet/π | 0.007408055728 | 0.00740806 |
| 1/ξ (from RHS = −1/ξ + α₀ = −0.424083) | 0.431491055728 | — |
| ξ | 2.31754514196 | — |
| ξ/R (R = ½) | **4.63509** | gate §2: 4.635 |
| 2/ξ (exterior gap) | 0.862982 | 0.8630 |
| κ₀ (first root) | **3.390462** | 3.3905 |
| κ₁, κ₂ | 9.513869, 15.76176 | 9.5139, 15.762 |
| tanh²(r_oct/ξ) | 0.0079437 | 0.007944 |

Dimensionless barrier strength:

- **b = α₀ξ = 0.017169**
- (1/ξ)/α₀ = **58.25** — the condensate's own inverse length is 58× the barrier's
- delta-shell transmission T = 1/(1 + b²/4) = **0.999926**
- depletion at the shell ≈ **1.7 %**

A junction needs b ≫ 1 (opaque link, two quasi-independent phases). The corpus sits a factor 58
on the **transparent** side of b = 1. App J's own sentence — *"the condensate permeates the
object… a weakly perturbing potential, not a hard wall"* — **is** the statement b ≪ 1.

**The unlocked horn (E_J = 0) requires b → ∞.** It is not marginally disfavoured; it is at the
opposite end of the barrier axis from where App J places the model, by an unbounded factor.

---

## 5 — STEP 2: THREE HORNS. THE ANSWER IS THE SOFT/LOCKED ONE, WITH THE GAP STATED

Constructing E_J from App J's own action (phase sector J·ρ|∇θ|², twist over the shortest length
the condensate permits without paying condensation energy, L = ξ):

```
E_J = 2 J ρ₀ A / ξ  = 2.711138    (A = 4πR² = π)
E_C = J / (2ξ² V)   = 0.177793    (from App J's own quartic; V = 4πR³/3)
E_J / E_C           = 15.249
```

**And the corpus states its own ratio, in a place the gate did not point at.** Letter 36
(D4-qubit variant — a *different* Letter 36 from the OHC one the gate cites) eq (3):

> E_J/E_C = 1/α₀ = π/(r_oct r_tet) = **134.99** … "placing the BCT qubit squarely in the
> **transmon regime** (E_J/E_C ≫ 1), where charge-noise sensitivity is exponentially suppressed."

The transmon regime is precisely the regime where the relative phase sits in a harmonic well at
the bottom of the cosine and its excitation is the **gapped plasma mode**. The corpus asserts the
locked horn itself, with a number, and has never connected it to Ψ₂.

### Every gap estimate found

| route | gap (m_P c²) | Yukawa range (ℓ_P) |
|---|---|---|
| App J's own printed interior A₁ ground mode κ₀ | 3.39046 | 0.29494 |
| constructed √(E_C E_J), App J parameters | 0.69428 | 1.44035 |
| same, transmon convention √(8E_C E_J) | 1.96371 | 0.50924 |
| Letter 36's 1/α₀, √(E_C E_J) | 2.06568 | 0.48410 |
| Letter 36's 1/α₀, √(8E_C E_J) | 5.84262 | 0.17116 |
| hard-wall limit of App J's stated profile, κR = π | 6.28319 | 0.15916 |

**Bracket: Δ ∈ [0.694, 6.283] m_P c². Range ∈ [0.159, 1.440] ℓ_P. No route gives zero.**

Phase localisation: rms spread √⟨ϑ²⟩ = (2E_C/E_J)^¼ = **0.349 rad** at the corpus ratio, 0.602
rad at the constructed one. A Goldstone's phase is flat and explores the whole circle at zero
cost. This one is confined to a well of width ~0.35 rad about zero. **That is "locked", stated
quantitatively.**

### What a gapped relative-phase mode mediates

A gapped scalar exchanges a **Yukawa** potential V(r) ~ −(g²/4πr)e^{−r/λ}, not 1/r. With
λ ≲ 1.44 ℓ_P, at r = 1 mm (r/ℓ_P = 6.19×10³¹) the suppression at the **most generous** gap in the
table is e^{−4.30×10³¹}.

**This fails for a stated reason — Δ ≠ 0 — and not by analogy with the locked horn.** The gate
asked for that distinction explicitly and it is honoured: the soft horn dies of its own gap, not
of the locked horn's freezing.

---

## 6 — STEP 3: WHAT FIXES α₀ IF UNLOCKED?

**SC-Ψ2-3 does not fire as worded, and is reported as not firing.**

α₀ = r_oct·r_tet/π is fixed in App D by void geometry. App J *uses* it; it does not *define* it.
Unlocking θ₂ therefore does not leave α₀ undetermined. Saying otherwise would be the favourable
reading the gate's §3 forbids, in reverse.

What unlocking does destroy is the α₀ boundary condition's *work*. And here the numbers are
unkind to App JH independently of any horn:

| | |
|---|---|
| α₀'s share of App J's eigenvalue RHS (−1/ξ + α₀) | **1.75 %** |
| κ₀ with α₀ | 3.390462 |
| κ₀ with α₀ = 0 | 3.394468 |
| shift from deleting the Josephson BC entirely | **−0.118 %** |

Deleting the α₀ boundary condition outright moves the interior ground state by about one part in
a thousand. **A perturbation of that size cannot "force" an integer topological charge.**
Topological selection is discrete and absolute; this input is a small continuous nudge. App JH's
word *forced* is not supportable at any horn — locked, soft, or unlocked.

---

## 7 — STEP 4: THE PARAMETER COUNT, TESTED RATHER THAN REPEATED

**Interior A (App J).** The action claim is **sustained**: S[Ψ₂] genuinely is the exterior GP
action restricted to r < R. Two riders:

- σ_s = α₀ is obtained in §1.3 under two stated conditionals — *"If the double layer charge Q = 1
  … and the shell thickness d = √(r_tet·r_oct)"*. Conditionals, not derivations.
- **Dimensions.** The jump condition [∂_rΨ] = −(σ_s/J)Ψ(R) requires σ_s/J to have units of
  1/length. α₀ is dimensionless. "σ_s = α₀" therefore carries an **undeclared unit convention** —
  α₀ per Planck length. Expressed per R it would read 2α₀ = 0.0148161. This is the same defect
  class as CN-FWD-02, surfaced here independently.

Net: 0 new parameters in the action; 2 conditionals; 1 undeclared unit. **Moot** — Interior A
supplies no second mode regardless.

**Interior B (App JH).** Against App J §1.2's *zero*:

1. **New field.** ℂ² in place of ℂ.
2. **Replaced potential.** |Ψ_int|² = ρ₀ fixed, replacing App J's quartic — this *deletes* the
   amplitude mode App J has.
3. **New coupling, mandatory.** The Faddeev–Skyrme coefficient κ_FS. Without it there is no
   stable hopfion (§8). With it, **κ_FS — not α₀ — sets the soliton size** and hence the interior
   spectrum, displacing exactly the thing App JH says α₀ determines.
4. **An inconsistency** (not a parameter): the derivative-jump BC is incompatible with constant
   modulus, as in §3 above.

**App J §1.2's claim of zero cost is FALSE for Interior B.** Whatever mode Interior B supplies, it
is not free, and it is not the mode App J §1.2 advertised.

---

## 8 — INTERIOR B'S OWN GROUND STATE DOES NOT EXIST

Three findings from App JH's own written free energy (its eq 13), each independent:

**(a) The selecting term is a constant.** With |Ψ_int|² = ρ₀ (its §3.1), the surface term
evaluates to 2πα₀ħ²ρ₀R/m = 0.0232731 (Planck units) — **independent of the configuration**. Its
functional derivative with respect to the unit field vanishes identically. The term App JH calls
the Josephson coupling, and credits with topological selection, **cannot select anything**.

**(b) The selection equation has no solutions and no N_H dependence.** App JH eq (14):

```
∮_{∂B³} J_Hopf · n̂ dA  =  α₀ ρ₀ 4πR²
```

For **any** stationary configuration, continuity gives ∇·J = −∂ρ/∂t = 0 throughout B³, so by the
divergence theorem the left side is **identically zero**. The right side is 0.0232731 ≠ 0. Eq (14)
reads 0 = 0.0233. It has no solutions — and the left side carries **no dependence on N_H
whatever**, so even if satisfiable it could not prefer N_H = 1 over N_H = 0. (Separately, the two
sides differ dimensionally by one power of velocity, ħ/mL.)

**(c) Derrick: there is no stable hopfion.** With |Ψ_int|² fixed and the surface term constant,
the *only* configuration-dependent term in App JH's free energy is the σ-model gradient energy.
For a texture of linear size a inside the fixed ball:

| term | scaling |
|---|---|
| E₂ σ-model gradient | E(a) ~ a^(+1) |
| E₄ Faddeev–Skyrme quartic (**absent**) | E(a) ~ a^(−1) |
| potential / volume | E(a) ~ a^(+3) |

E₂(a) → 0 as a → 0. The N_H = 1 texture **shrinks to a point**; the infimum of energy in the
N_H = 1 sector is zero and is not attained. Stabilisation requires the Faddeev–Skyrme
quartic-derivative term, whose coefficient κ_FS is a new dimensionful coupling absent from App J's
ingredient list.

**And the citation does not cover the gap.** App JH takes E_{N_H} = N_H·ε₀ from Faddeev–Niemi
[Nature 387, 58 (1997); PRL 82, 1624 (1999)]. Faddeev–Niemi work in the model **with** the quartic
term App JH omits, and the scaling there is the Vakulenko–Kapitanskii bound E ≥ c·N_H^{3/4} — not
linear. The formula is imported without the term that makes the source apply.

App JH's §3.4 stability argument ("changing N_H requires a nodal surface, which costs infinite
energy") is also not right as stated: vortex cores in a GP superfluid are nodal and cost finite
energy per unit length — that is the standard mechanism by which superfluid textures unwind.

---

## 9 — STEP 5: SYMMETRY AND INDEPENDENCE

**(a) Is ϑ genuinely A₁g under O_h? YES.** ϑ = θ₂ − θ₁ is a difference of two phases attached to
the same site. It carries no spatial index; it is l = 0 and transforms as A₁g. The gate's first
Step-5 question is answered affirmatively, and this is recorded even though it does not help the
programme.

**(b) Is it independent of ρ? NO.** In the two-mode reduction the canonical pair is (n, ϑ), where
n is the number **imbalance** between interior and exterior:

```
dϑ/dt = E_C n ,     dn/dt = −E_J sin ϑ
```

**One canonical pair, hence one mode — and it is the gapped plasma mode.** ϑ's conjugate momentum
*is* a density variable. This is the same slaving CN-R2-06 identifies for θ₁ (continuity + Euler),
reached here independently and by a different route. **SC-Ψ2-4 fires.**

**(c) E5-05 — at most one H-singlet per order parameter.**

- *Interior A:* App J §1.1 ("the field Ψ fills all of space") and §1.2 ("the field Ψ itself is
  continuous") make Ψ₂ a **restriction of Ψ to a subdomain**, not a second order parameter and not
  even a second component of one. One order parameter → at most one A₁g singlet → already spent on
  θ₁. **SC-Ψ2-4 fires on Interior A.**
- *Interior B:* Ψ_int : B³ → ℂ² with fixed modulus **is** a genuinely distinct order parameter, so
  E5-05 **permits** it a singlet. Interior B is **not** closed by E5-05. It is closed at Step 4 and
  by §8 instead. Stating this plainly matters: the E5-05 route does not reach Interior B, and
  claiming it did would be the easy wrong answer.

---

## 10 — NOTICES

**PROVEN** — established by computation or by quotation from primary source, reproducible from the
scripts.

| # | Notice |
|---|---|
| **CN-Ψ2-01** | **There is no Josephson term anywhere in the corpus.** App J §3.1's "dimensionless Josephson coupling g = α₀" is σ_s∮\|Ψ\|²dS; App JH eq (13)'s surface term is (α₀ħ²/2mR)∮\|Ψ_int\|²dA. Neither depends on a phase difference. Mechanical scan of all 108 `.tex`: zero `cos(θᵢ−θⱼ)` terms. The name has propagated to App I, App J, App JH, both Letter 36s and App AZ. |
| **CN-Ψ2-02** | In App J, Ψ₂ is not a second field. §1.1: "The BCT condensate field Ψ fills all of space." §1.2: "The field Ψ itself is continuous." θ₂(R) = θ₁(R) is imposed, not achieved. There is no relative phase to lock or unlock. |
| **CN-Ψ2-03** | The shell is transparent, not a weak link: b = α₀ξ = 0.017169, (1/ξ)/α₀ = 58.25, T = 0.999926, depletion 1.7 %. A junction needs b ≫ 1. The unlocked horn requires b → ∞. |
| **CN-Ψ2-04** | Constructed from App J's own action: E_J = 2.711138, E_C = 0.177793, E_J/E_C = 15.249. Six independent routes bracket the relative-phase gap at [0.694, 6.283] m_P c². **None gives zero.** |
| **CN-Ψ2-05** | Letter 36 (D4-qubit) eq (3) states E_J/E_C = 1/α₀ = 134.99 and names it "the transmon regime". **The corpus states the locked horn itself, with a number**, and has never connected it to Ψ₂. rms phase spread (2α₀)^¼ = 0.349 rad. |
| **CN-Ψ2-06** | A gapped ϑ mediates a Yukawa, range 0.159–1.440 ℓ_P; at 1 mm the suppression is e^{−4.30×10³¹} at the most generous gap. Fails for the stated reason Δ ≠ 0, **not** by analogy with the locked horn. |
| **CN-Ψ2-07** | (n, ϑ) is one canonical pair; ϑ's conjugate momentum is a density variable. One mode, and it is the gapped one. **Independent arrival at CN-R2-06** by a different route. |
| **CN-Ψ2-08** | E5-05 on Interior A: Ψ₂ is a restriction of Ψ to r < R, not a second order parameter. One singlet, already spent on θ₁. **SC-Ψ2-4.** |
| **CN-Ψ2-09** | App JH eq (14) is unsatisfiable and selects nothing. ∮J·n̂dA = 0 identically (divergence theorem + continuity) against RHS = 0.0232731. The LHS has no N_H dependence at all. Dimensionally inconsistent by one power of velocity. |
| **CN-Ψ2-10** | App JH's surface term is a **constant** on its own field space (|Ψ_int|² = ρ₀ fixed → 0.0232731, configuration-independent). Its variation vanishes. The term credited with topological selection cannot select. |
| **CN-Ψ2-11** | **Derrick.** App JH's free energy has only E₂ ~ a as configuration-dependent; the N_H = 1 texture shrinks to a point, infimum 0, not attained. **No stable hopfion exists in the free energy App JH writes.** Stabilisation needs a Faddeev–Skyrme κ_FS, which then — not α₀ — sets the soliton size. |
| **CN-Ψ2-12** | App JH cites Faddeev–Niemi for E = N_H·ε₀. Their model contains the quartic App JH omits, and their scaling is Vakulenko–Kapitanskii E ≥ c·N_H^{3/4}, not linear. The citation does not support the formula. Also, §3.4's "nodal surface costs infinite energy" is false — GP vortex cores are nodal at finite energy per unit length. |
| **CN-Ψ2-13** | **App J §1.2's "no new field, no new coupling, no new free parameter" is FALSE for Interior B:** ≥1 new field (ℂ²), 1 mandatory new coupling (κ_FS), 1 replaced potential (unit-normalisation deletes App J's amplitude mode). |
| **CN-Ψ2-14** | **The two interiors are separated by a homotopy invariant.** App J's vacuum manifold is S¹ (π₂ = π₃ = 0; Hopf charge identically zero on its field content); App JH requires π₃(S²) = ℤ. Not two write-ups of one object. **SC-Ψ2-5.** |
| **CN-Ψ2-15** | The four App JH copies are **physically identical**: 14 displayed equations, symmetric difference 0 across all four; `JH (1)` and `JH_FINAL` byte-identical; differences confined to frontmatter, ToC, bibliography and one self-citation record number (27 vs 53). **The canonicity problem is clerical, not physical** — downgrade its severity while keeping it on the archival list. |
| **CN-Ψ2-16** | α₀ contributes **1.75 %** of App J's eigenvalue RHS; deleting the Josephson BC entirely shifts κ₀ by **−0.118 %** (3.390462 → 3.394468). A continuous perturbation of that size cannot "force" an integer topological charge. **App JH's word *forced* is unsupportable at every horn.** |
| **CN-Ψ2-17** | App J §2.1 internal defect: the stated exterior profile Ψ_out = Ψ₀[1−(R/r)e^{−(r−R)/ξ}] **vanishes at r = R** (hard-wall limit, divergent log-derivative), while the printed eigenvalue equation is the weak-perturbation limit. Opposite limits. The hard-wall limit forces κR = π, κ = 6.2832, not the printed 3.3905. Live defect; does not change this verdict. |

**CONJECTURE**

| # | Notice |
|---|---|
| **CN-Ψ2-18** | σ_s = α₀ carries an undeclared unit convention: the jump condition needs an inverse length, α₀ is dimensionless. Per R it reads 2α₀ = 0.0148161. Same defect class as CN-FWD-02, surfaced independently. Tiered CONJECTURE because App J's "in units where J = 1" may intend a convention stated elsewhere; locate it or declare it. |
| **CN-Ψ2-20** | **Gate PT is not unblocked by App JH.** CN-PT-01 was assessed against π₃(S¹) = 0, and App JH does supply π₃(S²) = ℤ content — but at the cost of a new field and a mandatory new coupling, with a selection mechanism (eq 14) that is void and a ground state that is Derrick-unstable. Gate PT inherits a live Step-0 non-adjudication **plus** a broken selection argument, not a repaired axiom. |

**ASSERTED — flagged, not adjudicated here**

| # | Notice |
|---|---|
| **CN-Ψ2-19** | Letter 36 (D4-qubit) eq (2): η = r_oct·r_tet/α₀ **= π = 3.14159** by construction, since α₀ ≡ r_oct·r_tet/π. The printed value is 0.35174. The four expressions chained by "=" evaluate to π, π² = 9.8696, and 8.3246×10⁻⁴ — **mutually unequal, and none equals the printed value**. Eq (3), E_J/E_C = 1/α₀ = 134.99, is arithmetically correct but does not follow from η, which does not appear in it. Outside this gate's scope to repair; recorded because this gate used that ratio in §5. Also note: two different Letters bear the number 36. |
| **CN-Ψ2-21** | **Prompt defect.** §3 provides no stop condition for the outcome that actually closed Interior B — "the second A₁g may exist, but App J §1.2's zero-cost claim is false." Step 4 exists with no SC attached to it. Interior B is therefore recorded as *closed at Step 4* with no SC number, rather than folded into a stop condition it does not match. (Same class as the horn-(b) defect recorded against the R2 prompt: do not repair by mislabelling.) |

---

## 11 — WHAT THIS GATE DID **NOT** ESTABLISH

Stated explicitly, because §3 says no stop condition licenses a favourable conclusion and the
converse discipline applies too:

- It did **not** show that no second A₁g mode can exist anywhere. Interior B's field content
  genuinely admits one under E5-05; what fails is its cost, its selection mechanism, and its
  ground state.
- It did **not** compute a Josephson coupling that the corpus has. It computed one the corpus
  lacks. Every gap figure in §5 is a **construction** under §0.4, and is labelled as such.
- It did **not** reach Gate R2 Steps 2–4, and §0.6 above states why that would not have helped.
- It did **not** verify E5-01…E5-04 — the E5 scoping file was not available in this thread. E5-05
  was used only in the one-line form the gate itself states.
- It did **not** repair App J §2.1 (CN-Ψ2-17) or Letter 36 eq (2) (CN-Ψ2-19). Both need their own
  sessions.

---

## 12 — CONTAMINATION STATEMENT

**Quarantine held where it was specified.** `conversation_search` and `recent_chats` were **not
called at any point**. No 9–11 Sep session transcript was read.

**One breach to declare, with its ordering.** The project's Cold Ledger
(`/projects/…/audit-findings.md`) was read mid-session, at my own initiative, to obtain the exact
wording of the permitted notices (CN-R2-05/06, CN-OP-05/06/07/12/14, CN-PH-01, CN-P-02, Theorem
OP-1). That file contains two blocks explicitly labelled *"Unregistered chat observations, 10 Sep
2026"* — material from a session §0.2 quarantines. Specifically, its entry (i) describes the
App J / App JH conflict and entry (iv) quotes ξ/R = 4.635 and the κ_eff discussion. **Those are
evidently the source of the gate file's own §1 and §2 framing**, so that content was already in
front of me via the gate; the ledger added it a second time, plus roughly eight unpermitted gate
summaries — the ledger's own standing defect.

**Ordering, which the transcript shows.** The load-bearing Step-1 finding — that Ψ is continuous
at r = R, and that App J §3.1's "Josephson coupling" contains no phase difference — was obtained
from **App J primary text in the first corpus search, before the ledger was opened.** The ledger
read followed. It cannot have supplied that finding, and the ledger contains no statement of it.

**What was read from primary source.** App J (project mount, Appendices Vol.1 Part 1); App JH all
four copies and both Letter 36s (repo tarball, hash pinned above). Nothing about App JH was taken
from the ledger's secondhand description. Letter 36 (D4-qubit) and its E_J/E_C = 135 were found by
the corpus scan, not inherited.

**What was inherited as summary rather than primary.** CN-R2-05/06, CN-OP-05/06/07/12/14,
CN-PH-01, CN-P-02 and Theorem OP-1 were read as **ledger summaries**, not as the gate deliverables
themselves. Where this gate reaches those results independently — CN-Ψ2-07 vs CN-R2-06 — the
independence claim rests on the derivation in §9(b), which uses only App J's parameters.

**Not used anywhere below the verdict line:** Gate G′ / CN-PH-01's helicity-±1 dismissal, per §3's
explicit instruction.

**§0.5 status: repaired.** This gate ran on a byte-exact digest confirmed before reading, breaking
the four-gate run of paste-based handoffs.

---

## 13 — SCRIPTS

Deterministic, mpmath at 40 dps, no seeds, re-runnable in under a minute.

| script | covers |
|---|---|
| `gate_PSI2_step1_2.py` | App J parameter reconstruction (§4 table), barrier transparency, constructed E_J/E_C and gap, Yukawa range, App JH eq (14) evaluation, Derrick scaling, homotopy check |
| `gate_PSI2_corpus_scan.py` | corpus-wide search for a genuine phase-difference coupling; four-way App JH version diff |
| `gate_PSI2_step3_5.py` | α₀ sensitivity of κ₀, corpus E_J/E_C, transmon gap and phase localisation, gap bracket table, Step 4 and Step 5 reasoning, App J §2.1 consistency check |

Reproduce with: `python3 gate_PSI2_step1_2.py && python3 gate_PSI2_corpus_scan.py <repo> && python3 gate_PSI2_step3_5.py`

*One erratum in the script prose, corrected here and not in the file so the run output stays as
executed: `gate_PSI2_step3_5.py` §Step 3 says "shifts κ₀ by 0.6%"; the computed and correct figure
printed two lines above it is **0.118 %**. Use 0.118 %.*

---

*Gate Ψ2 executed 11 September 2026. Verdict: closed, unfavourably, on both interiors.
Not a result about gravity — see §2.*
