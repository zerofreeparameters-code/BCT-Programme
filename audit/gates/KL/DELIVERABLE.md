# GATE KL — DELIVERABLE
## Does the woven knot-lattice stand up?

**Handoff digest (SHA-256 of the file this session received):**
`9ae6e37b9050cbafd2b06f3136b0f241a0fc7ebf08c5a05370e9963a3d1b8e9d`  ·  `gate_KL_prompt.md`, 10716 bytes, curl-to-disk from the commit-pinned `raw.githubusercontent.com` URL at `0ecfa11`. Not pasted.

Repo checked out at `0ecfa1145d96f4ebbdec219371351391259a703d`. Tracked-path tree digest (SHA-256 of the sorted `git ls-files`): `8b7aa680ebf913a20ea74561b27a5d03795bd6aec2a33a9cd34c609b66d40993` (302 tracked files).

---

## VERDICT — **SC-KL-1**

**No modulated crystal is a ground state under the geometry-fixed Faddeev/BFN energy. The uniform state is the unconditional global minimum; no woven S² knot-lattice lies below it. The hopfion-medium route forecloses along this route, and the downstream photon / void-fermion / gravity gates are spared.**

The result is not a numerical near-miss; it is a one-line inequality (below), confirmed numerically. The escape route proposed after Gate JHF — "stop demanding one lonely knot, make the vacuum a space-filling overlapping-knot crystal" — does not rescue the programme, because the obstruction was never the *lone-soliton* Derrick collapse. It is that the standard Faddeev/BFN energy is **positive-definite and minimised by the uniform state**, with no chiral (Dzyaloshinskii–Moriya / Lifshitz) term to push any modulated texture below it — and BCT's centrosymmetric lattice **forbids** such a term. A knot/skyrmion crystal can at most be a *metastable topological excitation above* the vacuum, and even that is not self-consistent as a single-length geometry-fixed crystal (§ Step 2). Insisting on a modulated *ground* state requires a coupling that geometry does not supply and in fact excludes → the fallback SC-KL-2 is itself geometrically closed, collapsing back to SC-KL-1.

---

## SEARCH-SPACE COVERAGE (reported before any conclusion, per §0.6)

- **HEAD SHA:** `0ecfa11…a703d`.  **Tree digest:** `8b7aa680…0993`.
- **JH variants file-typed** (LaTeX source, `tex/`):
  | file | bytes | md5 (16) | status |
  |---|---|---|---|
  | `BCT_Appendix_JH.tex` | 24734 | `1c91a1e2267c7785` | older, distinct |
  | `BCT_Appendix_JH (1).tex` | 25712 | `bcbe122836e2ca1b` | == `_FINAL` |
  | `BCT_Appendix_JH_FINAL.tex` | 25712 | `bcbe122836e2ca1b` | == `(1)` |
  | `BCT_Appendix_JH_GRRRRRRRR.tex` | 25733 | `b4f21092dfe3f797` | near-dup (+21 B) |
  - `BCT_Appendix_JH4_YangMills_v2_CORRECTED.tex` **excluded** by §0.2 (JH4 is not the hopfion appendix).
- **Canonical text?** `audit/APPENDIX_INDEX.md` names **no** canonical JH hopfion appendix (its only JH-adjacent row, "GR2", is the hyperon-octet Gell-Mann–Okubo entry — unrelated). **Finding (per §0.6): App JH has no canonical text — three distinct variants, none index-designated.**
- **Field content, read cold from the `.tex` (not inherited):**
  - `audit/MINIMAL_BCT.md` §1.1–1.2: the written field is **a single complex scalar** Ψ = √ρ e^{iθ}; action `S = ∫ J(∂Ψ)*(∂Ψ) − (J/4ξ²)(|Ψ|²−Ψ₀²)²` — **two-derivative, one-component GP, order-parameter manifold S¹**. §1.5: π₂(S¹)=π₃(S¹)=0 → the *written* theory admits **no hopfion at all**.
  - `BCT_Appendix_JH_FINAL.tex`: prose asserts a "two-component … S²" field with H ∈ π₃(S²) (lines 195–198), but the equation of motion it actually writes ("Eq. GP", lines 116–120) is the **one-component** GP equation `−(ℏ²/2m)∇²Ψ + g|Ψ|²Ψ = μΨ`, and the energy it writes (lines 203–205) is **two-derivative** (|∇Ψ|² + a surface term). The only "Faddeev"/"Skyrme" strings anywhere in App JH or Letter 36 are **bibliography entries** (JH_FINAL lines 555, 560, 566; Letter36_OHC line 318) — **no four-derivative stabilising term is written anywhere in the corpus.**
- **FCC/BCT identification:** BCT with **c/a = √2** is the FCC lattice; adopted period = the conventional cubic FCC constant `a` (nearest-neighbour distance a/√2). `α₀ = r_oct·r_tet/π = 0.00740806` matches App JH's own `α₀` verbatim.
- **ξ/a and knot size derived cold** (Step 0 below) **before any energy was written.**
- **Quarantine honoured:** `audit/notes/` (incl. `note_healing_length.md`, `note_KA4_hopf.md`) and **every** `audit/gates/*/` deliverable were listed but **never opened**. No 9–15 Sep thread, no `gate-jhf`, no concurrent gate consulted.

---

## §0.5 — reproduced verbatim

**0.5 — THE PREMISE, STATED AS A COST.** The S² (two-component) order parameter is **not** the corpus's written field content — MINIMAL_BCT and App JH's own equation of motion (Eq. GP) are one-component (S¹). Promoting to S² is the premise of this gate and its first declared cost. A verdict of SC-KL-3 therefore establishes the ground for a *hypothetical* S² theory; it does **not** retroactively make App JH a written theory (that still owes a complete stabilised action). Record this explicitly.

> **Recorded.** This gate did **not** reach SC-KL-3; but the point stands regardless — the S² promotion is a premise, contradicted by App JH's own one-component GP equation, and nothing here converts App JH into a written theory.

## §0.7 — reproduced verbatim

> This gate decides whether a woven, FCC-periodic S² knot-lattice is a stable geometry-fixed ground state of the standard Faddeev/BFN energy. It does **not** decide whether that lattice has a photon, fermions, or gravity — each is a separate, later gate. **A verdict of "stable geometry-fixed crystal" does not vindicate BCT** — it means the S² ground the photon question needs now exists, and asking the photon question is a separate and harder gate. It also does not supply App JH a written action; that remains owed. **A verdict of "no stable crystal" does not refute the geometry** — the void radii, the percolating interstitial network, and α₀ remain correct; what fails is the specific claim that a knot-lattice is the vacuum's ground state.

---

## STEP 0 — THE ENERGY AND ITS GEOMETRY-FIXED COEFFICIENTS (derived, not posited)

**Two-component GP → Faddeev reduction (BFN).** For Ψ = (ψ₁,ψ₂) ∈ ℂ², write Ψ = √ρ₀ χ with a normalised ℂP¹ spinor χ (|χ|=1) and n̂ = χ†σχ ∈ S². The neutral two-component GP energy density is
`ε = (ℏ²/2m)(|∇ψ₁|²+|∇ψ₂|²) + (g/2)(ρ−ρ₀)²`, ρ = |ψ₁|²+|ψ₂|².
At fixed amplitude, `|∇ψ₁|²+|∇ψ₂|² = ρ₀|∇χ|²`, and the ℂP¹ identity gives
`|∇χ|² = ¼(∇n̂)² + (∂φ − C)²`, where C_i = −i χ†∂_iχ is the ℂP¹ connection and φ the overall phase. The composite field strength of C is exactly the Faddeev two-form: `∂_iC_j − ∂_jC_i = ½ F_ij`, `F_ij = n̂·(∂_i n̂ × ∂_j n̂)`.

- **c₂ (two-derivative, spin stiffness):** `c₂ = ℏ²ρ₀/(8m)` (the ¼ from |∇χ|² × ℏ²ρ₀/2m). **Positive, fixed by the stiffness.**
- **c₄ (four-derivative Faddeev):** generated by integrating out the massive amplitude mode δρ, whose gap is the inverse healing length: `ξ² = ℏ²/(2mgρ₀)`. The gradient expansion's small parameter is `(ξ∇)²`, so the leading generated four-derivative term is `c₄ F² ` with **`c₄ = κ · c₂ ξ²`, κ = O(1) and positive.** Hence **`c₄/c₂ ∼ ξ²`** — derived, not assumed. **Both couplings are geometry-fixed through ξ; neither is free** (this is *why* the crystal cannot be tuned — see Step 2).
- **No other term is generated.** The GP functional is real and inversion-symmetric; the reduction produces only even-gradient, positive terms. In particular **no chiral/Lifshitz term `c₁ n̂·(∇×n̂)`** appears — the ingredient that a modulated ground state would require.

**Cold geometry (script `kl_step0_xi.py`, mpmath 60 dps, reported 40):**
```
r_oct = (√2−1)/2 = 0.2071067811865475244008443621048490392848
r_tet = (√6−2)/4 = 0.1123724356957945245493210186764728479915
α₀ = r_oct·r_tet/π = 0.007408055727547908079640101104499873416
ξ/a = 1/√(8π α₀) = 2.317543794911664963039020806144813022013
     = 1/√(8 r_oct r_tet)  (identical; |diff| = 0)
c/a = √2 (BCT ≡ FCC)
```
**Natural knot size** `λ* = √(c₄I₄/(c₂I₂)) = ξ·√(I₄/I₂)`. From the standard H=1 Hopf ansatz (script `kl_step1_crystal.py`, part 4) the dimensionless shape ratio `√(I₄/I₂) = 0.546`, giving **`λ*/a = 1.26`** at that shape (and `~ξ/a = 2.32` at order-unity shape ratio). **Either way λ* > a: the natural knot is larger than one FCC cell / one sphere.**

---

## STEP 1 — THE PERIODIC STABILITY CALCULATION (load-bearing)

### The topology of a *periodic* texture (not π₃(S²))
A crystal is a map from the 3-torus, `n̂ : T³ → S²`, whose homotopy content is **not** π₃(S²)=ℤ (that classifies maps from S³, i.e. a lone finite-energy hopfion). Maps T³→S² carry:
- a **primary invariant** `n̂*(ω) ∈ H²(T³;ℤ) ≅ ℤ³` — three integers (m₁,m₂,m₃) counting the wrapping of n̂ over the three 2-subtori. A *baby-skyrmion tube lattice* (a π₂-charge per 2-D section, stacked along a third axis) realises a nonzero primary invariant; the preimage of a regular value is the straight tube-core 1-manifold.
- a **secondary Hopf-type invariant** (Pontryagin / framed-cobordism of the preimage 1-manifolds), well-defined **only when the primary invariant vanishes**, and then valued in ℤ (mod 2·gcd). A genuine "Hopf charge per cell" is this secondary class and requires the primary charge to be zero (closed, linked preimage loops confined to the cell).

**So a well-defined "integer charge per cell" does exist** (the robust one is the primary π₂-wrapping). **The topology is therefore *not* the obstruction — the energetics is.** The natural BCT candidate ("one unit of charge per primitive cell") is the baby-skyrmion tube lattice; the Hopf-crystal (secondary) is more delicate and only rarer, but the energetics verdict below is identical for both.

### The one-line result
`E[n̂] = ∫ [ c₂(∂n̂)² + c₄ F² ]` with `c₂, c₄ > 0` is **pointwise non-negative and vanishes iff ∂n̂ = 0 everywhere** (uniform n̂). Therefore
> **inf E = 0, attained only by the uniform state; every non-uniform periodic texture has E > 0.**
No modulated crystal — in any topological sector — can be at or below the uniform energy. To beat uniform you need a term that is *negative* for some texture, i.e. odd in gradients (a DM/Lifshitz term). The BFN reduction of a non-chiral GP produces none, and a centrosymmetric FCC/BCT lattice (inversion symmetry) **forbids** a bulk DM term. **SC-KL-1.**

### Numerical confirmation (`kl_step1_crystal.py`, N=16 periodic box, c₂=1, c₄=ξ²)
```
(1) uniform          E2,E4,Etot = 0, 0, 0            <- exact global minimum
(2) random texture   Etot = 236835.7                 (>0)
    skyrmion tube    Etot = 2979.6, Q_section ≈ 1     (>0; integer charge available)
(3) gradient flow (monotone; never below 0):
    random init  216977 -> 2437 ...  toward 0 (homogenises to uniform)
    tube  init     2972 -> 91   ...  toward 0 (unwinds on the lattice)
(4) 3D Hopf Derrick: √(I4/I2)=0.546 -> λ*/a = 1.26 > 1 (knot exceeds one cell)
    2D size scan: Etot falls 4733 -> 2085 as R: 0.20a -> 0.45a
                  (no sub-cell equilibrium; the texture inflates to fill the cell)
```
Gradient flow *never* produces a state below the uniform energy; textures either homogenise or unwind toward it. Confirmed.

### Derrick in the fixed cell + the size-vs-period decision
With the period pinned, the remaining modulus is how the winding distributes inside the cell.
- **2-D tube (baby-skyrmion):** the c₂ term is scale-invariant in 2-D, the c₄ term scales as λ⁻²; `E(λ) = E₂ + E₄λ⁻²` is monotone decreasing → the tube **inflates without an intrinsic size**, capped only by the cell wall. No geometry-fixed size; a mass/potential term (absent from BFN) would be needed to fix one.
- **3-D hopfion:** `E(λ) = E₂λ + E₄λ⁻¹` → finite `λ* = √(E₄/E₂) ∼ ξ ≈ 2.3a`, **larger than the FCC period.** The knot does not fit in one cell; "one knot per sphere" is impossible and even "one knot per cell" is strained.
- **The crux the woven picture rests on** — that `λ* ∼ ξ > a` gives a *stable overlapping* crystal as in a skyrmion lattice — **fails**: overlap in a *non-chiral* energy does not lower the texture below uniform (a skyrmion lattice beats uniform only via its DM term). Overlap here only raises E further above 0.

---

## STEP 2 — SELF-CONSISTENCY AND THE PARAMETER COUNT

- **Self-consistent single length?** No. The geometry-fixed `c₄` sets `λ* ∼ ξ ≈ 2.32a`, which is **not** equal to the FCC period a. A crystal with charge-per-cell therefore needs the period **imposed independently** — a *second* length not equal to ξ. That is precisely the SC-KL-2 failure mode (an imposed period), and it is required *before* one even asks about beating uniform.
- **Parameter cost relative to "zero free parameters":**
  1. **S² promotion** (premise, §0.5) — +1 structural assumption, contradicted by the written one-component GP EoM.
  2. **An imposed period** (a second length ≠ ξ) to make a charge-per-cell crystal at all — +1.
  3. **A chiral/DM coupling** to push the modulated state *below* uniform (make it a *ground* state, not a metastable excitation) — +1, and this one is **not merely un-fixed by geometry — it is forbidden by the geometry's inversion symmetry.**
- **Honest statement:** the knot-lattice ground state costs at minimum a forbidden coupling on top of two structural additions. It is not a zero-parameter object; it is not even reachable with free parameters while keeping BCT's centrosymmetry.

---

## STEP 3 — THE STEELMAN (required)

**Strongest case that a stable, geometry-fixed, integer-charge S² crystal exists:**
1. Skyrmion lattices are *real* thermodynamic ground states (MnSi and other B20 chiral magnets; Mühlbauer *et al.*, Science 323 (2009) 915) — a modulated texture genuinely below the uniform ferromagnet.
2. Knotted/linked solitons of the Faddeev–Niemi energy exist and are stable up to high Hopf charge (Faddeev–Niemi, Nature 387 (1997) 58; Battye–Sutcliffe, PRL 81 (1998) 4798; Sutcliffe, Proc. R. Soc. A 463 (2007) 3001), with the Vakulenko–Kapitanskii bound `E ≥ c|Q|^{3/4}` guaranteeing they cannot shrink to zero.
3. Two-component BEC / two-gap superconductor reductions do generate exactly the Faddeev term (Babaev–Faddeev–Niemi, PRB 65 (2002) 100512), so the S² energy is not ad hoc.

**Why the steelman, pushed honestly, still lands on SC-KL-1:**
- Every example in (1) that is a *ground state below uniform* requires a **Dzyaloshinskii–Moriya term** (chiral magnet, broken inversion) or an external field/rotation. Remove the DM term and the uniform ferromagnet wins — this is textbook. BCT's FCC/BCT lattice is **centrosymmetric**, so no bulk DM term exists: the one ingredient that makes skyrmion lattices ground states is geometrically absent.
- The FN knots in (2) are **metastable topological solitons**, energetically *above* the vacuum (E>0), stabilised by topology, *not* ground states relative to uniform. They confirm exactly the picture here: a knot crystal can be metastable-above-uniform, never below.
- (3) delivers the c₄ term but, being the reduction of a non-chiral GP, delivers **no** chiral term — so it cannot produce a below-uniform crystal.

The steelman thus converts into a precise statement of the missing ingredient (a DM/Lifshitz term of definite size), which is not geometry-fixed and is in fact **forbidden** by BCT's inversion symmetry. Where a ground state *could* have existed (add DM by hand), that is SC-KL-2 with an *excluded* coupling. No route reaches SC-KL-3.

---

## CN-KL NOTICES (tiered)

- **CN-KL-01 [PROVEN].** The written BCT corpus contains no four-derivative/Faddeev term; the canonical action (MINIMAL_BCT §1.2; App E/J) is two-derivative one-component GP on S¹. App JH's own EoM is one-component GP. (Cold from `.tex`.)
- **CN-KL-02 [PROVEN].** `ξ/a = 1/√(8π α₀) = 1/√(8 r_oct r_tet) = 2.31754…`; `α₀ = 0.00740806`; c/a=√2 (BCT≡FCC). (Script, 40 dps.)
- **CN-KL-03 [PROVEN].** For c₂,c₄>0, `E=∫[c₂(∂n̂)²+c₄F²] ≥ 0` with equality iff n̂ uniform. Uniform is the unconditional global minimum; no modulated periodic texture lies at or below it. (Pointwise inequality + numerics: uniform=0, all textures>0, flow never below 0.)
- **CN-KL-04 [PROVEN].** The BFN reduction of a non-chiral, inversion-symmetric GP generates only even-gradient positive terms; no `n̂·(∇×n̂)` Lifshitz/DM term. A centrosymmetric FCC/BCT lattice forbids a bulk DM term. Hence no mechanism to bring a modulated state below uniform. (Symmetry argument.)
- **CN-KL-05 [PROVEN].** Geometry-fixed `c₄/c₂ ∼ ξ²` gives `λ* ∼ ξ ≈ 2.3a > a`: the natural knot exceeds one FCC cell; no sub-cell geometry-fixed size (2-D tube inflates; 3-D λ*>period). A charge-per-cell crystal needs an independently imposed period. (Derrick + size scan.)
- **CN-KL-06 [PROVEN].** Periodic topology: `[T³,S²]` has primary invariant in `H²(T³;ℤ)=ℤ³` (baby-skyrmion wrapping) plus a secondary Hopf-type class (defined when primary=0). An integer charge per cell is well-defined; the obstruction is energetic, not topological.
- **CN-KL-07 [ASSERTED].** The precise O(1) constant κ in `c₄ = κ c₂ ξ²` and the shape ratio `√(I₄/I₂)` depend on the full amplitude-mode integration and the chosen ansatz; only their *scale* (O(1)) is used. The verdict does not depend on κ (it rests on the sign/positivity, not the magnitude).
- **CN-KL-08 [PROVEN, §0.6].** App JH has no canonical text (three distinct variants; none index-designated).

---

## WHAT THIS GATE DID **NOT** ESTABLISH

- It did **not** answer the photon question (nor fermions, nor gravity) — moot here, since no S² ground state was found; each remains a separate later gate had SC-KL-3 been reached.
- It did **not** supply App JH a written action — that remains owed (§0.5); App JH is still prose-only S² over a one-component GP EoM.
- It does **not** refute the BCT geometry: the void radii, the percolating interstitial network, and α₀ remain correct (§0.7). What fails is the specific claim that a knot-lattice is the vacuum's ground state.
- It did **not** rule out a *metastable* topological texture existing above the vacuum — such states can exist (FN knots do); they are simply never the ground state, which is what the hopfion-medium programme needs.

---

## CONTAMINATION STATEMENT

Primary sources read (permitted by §0.2): `tex/BCT_Appendix_JH.tex`, `BCT_Appendix_JH_FINAL.tex` (= `(1)`), `BCT_Appendix_JH_GRRRRRRRR.tex`, `tex/BCT_Letter36_OHC_tex.tex`, `tex/BCT_Letter36_D4Qubit.tex`, `audit/MINIMAL_BCT.md`, `audit/APPENDIX_INDEX.md`; standard literature (Faddeev–Niemi 1997; Babaev–Faddeev–Niemi 2002; Sutcliffe 2007; Battye–Sutcliffe 1998; Vakulenko–Kapitanskii; Mühlbauer *et al.* 2009).

**Never opened (quarantine, §0.2):** `audit/notes/` — including `note_healing_length.md` and `note_KA4_hopf.md`, which by their names bear directly on ξ and the hopfion and would have been inheritance; every `audit/gates/*/` deliverable (JHF, RATIO, LINK, MAD, RANK, MP, PRED, XI, YM2, C1, INT, PSI2, TANH, crossaudits); no 9–15 Sep thread, BCT-X/Sandbox TOP, or concurrent gate.

**Prior findings that reached me, and how handled (§0.3):** the gate prompt itself recites the Gate JHF result (two-derivative GP, lone-knot Derrick collapse, ξ≈2.3a, c₄∼ξ² scaling) as the premise of the KL question, and my memory-listing descriptions name a JHF verdict and an "Octet-Hopfion Condensate." I did **not** rely on any of these: ξ/a was re-derived cold from the void radii (Step 0); c₄/c₂∼ξ² was re-derived from the BFN gradient expansion (Step 0); the field content was re-established directly from the `.tex` and `MINIMAL_BCT.md`; the central inequality and the periodic-topology classification were derived from field theory. The independently derived ξ/a = 2.31754 coincides with the recited value — this is a confirmation, not an inheritance.

---

## SCRIPTS (deterministic, re-runnable)

- `scripts/kl_step0_xi.py` — geometry-fixed inputs (mpmath, seedless). `python3 scripts/kl_step0_xi.py`.
- `scripts/kl_step1_crystal.py` — periodic energy, gradient flow, Derrick, size scan (`numpy`, `np.random.seed(0)`). `python3 scripts/kl_step1_crystal.py`.

*Gate KL executed 15 September 2026. Pre-registered digest `9ae6e37b…b8e9d`. Verdict SC-KL-1.*
