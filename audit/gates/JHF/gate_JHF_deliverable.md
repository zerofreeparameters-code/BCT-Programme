# GATE JH-FIELD (JHF) — DELIVERABLE

**Is the hopfion / S² medium a written, stabilised field theory, or a target described in prose?**

- **Model:** Claude Opus 4.8 (`claude-opus-4-8`).
- **Date run:** 15 September 2026. Cold Ledger gate, fresh thread, one gate this thread.
- **Handoff / digest:** `gate_JHF_prompt.md` fetched by `curl` to disk from the commit-pinned
  `raw.githubusercontent.com` URL (commit `495c867f`), then hashed **before** reading.
  `sha256sum` = `1b3e142e7f74302de0ff19a74c54211bedf110788456dc12a9c9388729240526`,
  9288 bytes — **byte-exact** against the pre-registration in `audit/gates/PREREG_20260915.sha256`.
  Third clean curl-to-disk handoff (paste-defect chain closed at LINK/RATIO). Pre-registration
  chain intact; §0.1 satisfied.

---

## SEARCH-SPACE COVERAGE (reported before any conclusion)

Repo cloned at HEAD `495c867fcda9ab2afa14b3b5430ebe1ce9925449` (the commit the prompt was pinned to);
135 `.tex`, 298 tracked files. `file`-typed every App JH candidate. codeload tarball digest not
obtainable in-session (codeload/api/push all 403 per standing infra note), so the HEAD SHA-1 above
stands in for the tree digest, and per-file SHA-256 are recorded below.

**App JH variants (JH4 = Yang–Mills, excluded per §0.2):**

| file | SHA-256 (16) | bytes | lines | relation |
|---|---|---|---|---|
| `tex/BCT_Appendix_JH.tex` | `ab4464f6c1d8bcb6` | 24734 | 556 | older; differs from FINAL in **front-matter only** |
| `tex/BCT_Appendix_JH (1).tex` | `2d830856427897c5` | 25712 | 581 | **byte-identical to FINAL** |
| `tex/BCT_Appendix_JH_FINAL.tex` | `2d830856427897c5` | 25712 | 581 | audited (clean LaTeX) |
| `tex/BCT_Appendix_JH_GRRRRRRRR.tex` | `f09002d164571a4d` | 25733 | 581 | FINAL + **one line** (bibitem record no.) |

Diffs (derived cold, not inherited):
- `JH (1)` ≡ `FINAL` byte-for-byte.
- `GRRRRRRRR` vs `FINAL`: a **single** line — the self-citation record number. GRRR prints
  `Record~BCT Programme Record 53` (a LaTeX duplicated-string typo carrying "53"); FINAL prints the
  stale `Record~27`. No physics.
- `JH.tex` (556) vs `FINAL` (581): the 25-line delta is entirely front-matter — section-numbering
  `\renewcommand`s, title/affiliation formatting, the DOI line, `\tableofcontents`, and two
  `\bibitem`s. Grep for Lagrangian/action/κ/Faddeev/Skyrme/coefficient/∂/term/`=` across the delta
  returns **nothing**.

**Canonical marker:** none. The string "canonical" occurs in all four only inside "the canonical
commutation relation" (§JH.5). No file self-marks canonical.

**Verdict on the source's auditability:** the four variants are **physics-identical** — the only
disagreements are front-matter and a record-number typo. The union has no disagreement on the
action or any stabilising term. **SC-JHF-4 does not fire**: the source is auditable. (Citation of
record: the published Zenodo deposit is Record 53 / DOI 10.5281/zenodo.18975018 — this is an
inherited fact from the ledger, flagged in the contamination statement, not derived here.)

**App J is absent from the tree.** The action App JH inherits — `S[\Psi_2]`, bibitem `AppJ`,
"in BCT Appendices Vol. 2" — has **no `.tex` in this repo**. The only form of App J's dynamical
equation available to this gate is the one App JH itself quotes (Eq. GP, Eq. BC). This is a
finding, not a gap I can close: the load-bearing prior action is not in the auditable corpus.
Permitted files read: `audit/MINIMAL_BCT.md`, `audit/APPENDIX_INDEX.md`, the four App JH variants,
`tex/BCT_Letter36_OHC_tex.tex`, `tex/BCT_Letter36_D4Qubit.tex`.

---

## VERDICT (first)

**SC-JHF-1 — HALT. App JH does not contain a complete, stabilised S² field theory. The hopfion /
Octet-Hopfion medium is a physical picture described in prose (plus a plain Gross–Pitaevskii free
energy that cannot support it), not a written theory.**

The single term Derrick's theorem requires to stabilise a 3+1D hopfion — a four-derivative
(Faddeev/Skyrme) term — is **absent from every equation** in App JH and in the OHC companion
Letter 36. "Faddeev" and "Skyrme" appear in both documents **only in the bibliography**: the theory
cites the papers that contain the stabiliser without importing the stabiliser. The prose "stability"
section (§JH.3.3) argues topological protection against the Hopf charge *changing* — a restatement
of π₃(S²)=ℤ — which is a different question from energetic (Derrick) stability and does not touch it.

**Robustness against the stop-condition boundary.** If one insists on reading the written free
energy (Eq. free-energy) as "a complete S² action," the verdict does not improve — it slides to
**SC-JHF-2**: the action is complete in its own terms but the hopfion crystal is Derrick-unstable
and the missing stabiliser is an undetermined coupling, so the parameter cost is ≥ 1 and the
zero-parameter claim fails. **Both readings are unfavourable in the same direction; neither
SC-JHF-3 (favourable) nor SC-JHF-4 (unauditable) is reachable.** No prompt defect: the outcome
matches SC-JHF-1, with SC-JHF-2 as a same-direction fallback. Per §6, the verdict is reached from
the Derrick calculation, not from a stop-condition label.

**This decides nothing about the geometry.** See §0.6 (reproduced verbatim below).

---

## STEP 0 — THE ACTION AS WRITTEN

The only field-theoretic objects carrying equations in App JH:

1. **Eq. (GP)** [§JH.1, inherited from App J]:
   `−(ℏ²/2m)∇²Ψ₂ + g|Ψ₂|²Ψ₂ = μΨ₂` — the **standard one-component Gross–Pitaevskii equation**.
   Its order-parameter manifold is a single U(1) phase, i.e. **S¹**.
2. **Eq. (BC)** [§JH.1]: the derivative-jump Josephson boundary condition,
   `∂Ψ₂/∂r|_{R⁻} − ∂Ψ₁/∂r|_{R⁺} = −α₀Ψ(R)`, `α₀ = r_oct·r_tet/π = 0.00740806`.
3. **Eq. (free-energy)** [§JH.3.1] — the **only complete energy functional** in the document:

   ```
   F[Ψ₂] = ∫_{B³} [ (ℏ²/2m)|∇Ψ₂|²  +  (g/2)|Ψ₂|⁴ ] d³r
            +  (α₀ℏ²/2mR_s) ∮_{S²} |Ψ₂|² dA
   ```

**What the field is, as written in an equation (not prose):** contradictory across the document.
- §JH.3.1 (line 194) *declares* `Ψ₂ : B³(R_s) → ℂ²`, `|Ψ₂|² = |ψ₊|²+|ψ₋|² = ρ₀`; the normalised
  field then maps `S³ → S²` (S² content — correct for a hopfion).
- But the **equation of motion actually written**, Eq. (GP), is one-component GP — an **S¹** field.
- And Eq. (free-energy), though written for ℂ², contains only `|∇Ψ₂|²` (two-derivative stiffness),
  `|Ψ₂|⁴` (a **zero-derivative potential**, U(2)-symmetric — a function of the total density ρ
  only, blind to the S² direction n̂), and a surface term. **It is a plain GP functional.** There
  is no term that depends on the texture n̂ beyond the two-derivative stiffness, and **no
  four-derivative term**.

**Is a complete Lagrangian density given?** A complete *free energy* (Eq. free-energy) is given,
with all coefficients specified. But it is not a *stabilised S² (hopfion) action*: it is the
two-derivative GP functional, which is the wrong functional for a finite-size hopfion (Step 2).

**Does App JH's field content contradict the App J / minimal (S¹) action?** Yes, and the
contradiction is confirmed cold at source:
- `audit/MINIMAL_BCT.md`: *"The field is a one-component compact scalar. Every written action in
  392,000 words … A single complex scalar Ψ on a body-centred tetragonal lattice."* → **S¹**,
  π₃(S¹)=0.
- App JH's own Eq. (GP) is exactly this one-component GP.
- App JH's §JH.3.1 setup then *declares* a ℂ²/S² field for the free energy.

So the S¹/S² contradiction the corpus flagged is real and lies **within App JH itself** (Eq. GP
vs the §JH.3.1 setup), not only between App JH and App J. Confirmed. → **CN-JHF-06.**

---

## STEP 1 — THE TOPOLOGY (derived, not inherited)

**π₃(S¹) = 0.** S¹ has contractible universal cover ℝ; the covering map induces isomorphisms on
πₙ for n ≥ 2, and πₙ(ℝ)=0. Hence πₙ(S¹)=0 for all n ≥ 2, in particular π₃(S¹)=0. A phase-only
(S¹) field carries **no** Hopf charge.

**π₃(S²) = ℤ.** From the Hopf fibration `S¹ ↪ S³ → S²`, the long exact sequence of homotopy groups
gives `π₃(S¹) → π₃(S³) → π₃(S²) → π₂(S¹)`, i.e. `0 → ℤ → π₃(S²) → 0`, so
**π₃(S³) ≅ π₃(S²) = ℤ**, generated by the Hopf map itself (H=1). Self-contained; one paragraph.

**Does App JH's field, as written in its action, have the S² target?** Only in the §JH.3.1 *setup*
(ℂ², normalised → S²). The *dynamical equation* (Eq. GP) is one-component (S¹, π₃(S¹)=0), which
cannot carry a hopfion. App JH's abstract and eq:homotopy state π₃(S²)=ℤ **correctly** — the
topological prerequisite is sound. The failure is not topological; it is that the field carrying
the winding is not the field the equation of motion governs.

A category slip runs alongside: §JH.1 calls the *spatial domain* "the three-sphere S³ (the interior
of a Planck sphere)". The interior of a sphere is a 3-ball B³, not S³. The S³ that carries π₃ is
either compactified space (ℝ³∪{∞}) or the **field-space** unit sphere of a ℂ² value with fixed
modulus — not the spatial region. The document conflates spatial B³ with field-space S³.

**Is N_H = 1 "forced by the α₀ Josephson boundary condition" derived or asserted?** **Asserted**,
via an ill-founded matching equation. Eq. (hopf-matching) sets
`∮_{∂B³} J_Hopf·n̂ dA = α₀ρ₀·4πR_s²` and declares H=1 "the unique smooth solution." But the Hopf
invariant is a **bulk** integral `H = (1/16π²)∫_{S³} A∧dA` (a linking number of preimage fibres) —
it is **not** any surface flux. A net superfluid-current flux through a closed surface is π₂
(vortex/monopole) data, not π₃ (Hopf) data; for a localised hopfion the Hopf current is
divergence-free and the surface flux is generically zero. Equating a boundary current flux to a
Hopf charge is a topological type error; the flux condition cannot "force" H=1. → **CN-JHF-08.**

---

## STEP 2 — STABILITY (the load-bearing calculation)

**Derrick scaling of Eq. (free-energy), as written.** Take the texture `n̂: ℝ³ → S²` at fixed
`|Ψ₂| = √ρ₀` and rescale `x → λx`:

| term in Eq. (free-energy) | derivative order | scales as |
|---|---|---|
| `(ℏ²/2m)|∇Ψ₂|²` (stiffness / σ-model) | 2 | **λ** |
| `(g/2)|Ψ₂|⁴` (potential, ρ only) | 0 | λ³ |
| surface Josephson (fixed R_s) | — | fixed |
| *(a Faddeev/Skyrme term, if present)* | 4 | *λ⁻¹* |

As written, `E(λ) = E₂λ + V_p λ³ + E_s`, with `dE/dλ = E₂ + 3V_pλ² > 0` for all λ>0 — **monotone
increasing**, minimised as **λ → 0**. The H=1 texture lowers its energy by shrinking its core
toward zero size, with the winding fixed and **no node crossed**. This is Derrick collapse: the
written functional has **no finite-size hopfion**. A stable knot requires a term scaling as λ⁻¹ to
balance the λ collapse (`λ* = √(E₄/E₂)`); that term is the four-derivative Faddeev/Skyrme term, and
**E₄ = 0** in Eq. (free-energy). Confirmed numerically (`gate_JHF_verify.py`). → **CN-JHF-03.**

**Is the stabiliser in the equation, or only in the prose?** In **neither**. There is no
four-derivative term in any App JH equation, and none in Letter 36. "Faddeev"/"Skyrme" occur in
both only as bibliography entries (App JH lines 555/560/566; Letter 36 line 318). The §JH.3.3
"Stability" prose argues **topological protection** (H cannot change without a node at infinite
energy) — true, but it is the statement π₃(S²)=ℤ, and it does **not** address Derrick size-collapse
(which fixes H and crosses no node). Topological protection ≠ energetic stability. → **CN-JHF-04.**

**If a Faddeev/Skyrme term is present, is its coefficient geometry-fixed or free?** No such term is
present, so there is **no coefficient to read**. This is why the outcome is SC-JHF-1 rather than
SC-JHF-2: the hinge coefficient is not free — it is absent.

**Also:** Eq. (hopfion-energy) `E_H = H·ε₀` (linear in H) is asserted with a Faddeev–Niemi/Sutcliffe
citation, but the Faddeev–Niemi hopfion energy is **sub-linear**, `E ∝ H^{3/4}`
(Vakulenko–Kapitanskii), and that result *requires* the four-derivative term the functional lacks.
The linear formula is neither derivable from Eq. (free-energy) nor consistent with the cited
literature. → **CN-JHF-05.**

**Three lengths (recomputed cold, 60 dps).** With `r_oct=(√2−1)/2`, `r_tet=(√6−2)/4`,
`α₀ = r_oct·r_tet/π`:
- `α₀ = 0.007408055727547908` (App JH abstract: 0.0074081 ✓)
- `ξ/a = 1/√(8·r_oct·r_tet) = 1/√(8πα₀) = 2.317543794911665` (MINIMAL_BCT: 2.3175 ✓)
- With `R_s = ℓ_P/2 = a/2`: **`ξ/R_s = 2·(ξ/a) = 4.635087589823330`** (gate: 4.635 ✓)
- `r_oct/r_tet = 1.843038997100767` (close-packing constant ✓)

The healing length is **4.635× larger than the sphere radius**. ξ is the shortest length over which
the order parameter can vary; a knot must complete its winding within its localisation volume.
With ξ/R_s = 4.635 there is **no room for even one full winding inside R_s** — the knot core
(~ξ) would be larger than the sphere meant to contain it. The one-N_H=1-knot-per-site **crystal is
geometrically excluded by the document's own ξ**, independently of the Derrick argument. The three
lengths (knot core, healing length ξ, sphere radius R_s) are assigned inconsistently. → **CN-JHF-09.**
(Tangential: Eq. (phase-velocity) `v_ph = k₀/R_s = 6.78c` is dimensionally inconsistent —
wavenumber-over-length is not a velocity; a Result-6 defect, not load-bearing here.)

**Is the crystal shown to be a stable/metastable ground state of the written action?** No — it is
asserted (§JH.3.3), on the wrong stability criterion, and is excluded both by Derrick (no E₄) and
by ξ/R_s = 4.635.

---

## STEP 3 — THE COUNTING

Relative to the S¹ minimal theory (one complex scalar; GP with g, μ), a *stabilised* S² hopfion
theory requires, at minimum:

1. a field-**content** change S¹ → S² (ℂ² order parameter) — not a numerical parameter, but a
   change App JH's own equation of motion (Eq. GP) does not make;
2. **at least one new dimensionful coupling** — the Faddeev/Skyrme quartic coefficient c₄, which
   sets the knot size (`ℓ_knot ~ √(c₄/c₂)`).

Is c₄ fixed by geometry or supplied from outside? **Neither.** App JH writes no such term, so c₄ is
**undetermined** — not read off α₀, the void radii, or ξ, and not supplied externally. It is simply
missing.

**Honest parameter cost of the hopfion medium as written, relative to "zero free parameters":**
**≥ 1 undetermined coupling** (the stabiliser), plus the unresolved S¹/S² content inconsistency.
The abstract's and Table caption's "zero free parameters" is **not met** by the written functional.
→ **CN-JHF-10.**

---

## STEP 4 — THE STEELMAN (required)

**Strongest case that App JH *is* a complete, stabilised, zero-parameter S² theory:**

- The field is *declared* ℂ² (§JH.3.1), genuine S² content after normalisation; π₃(S²)=ℤ
  (eq:homotopy) is stated correctly and does admit hopfions; the right literature (Faddeev–Niemi,
  Sutcliffe) is cited. The topological scaffolding is in place.
- The interior is confined to a **fixed** sphere `R_s = ℓ_P/2`, and the Josephson boundary
  condition fixes the winding. One could argue that fixed-box confinement replaces the Faddeev
  term: the texture cannot escape to infinity, and the box supplies the length scale — so
  **geometry (R_s) would fix the knot size at zero extra parameters**, a genuine zero-parameter save.
- The published deposit (Record 53) lists six derived results and "zero free parameters."

**Does the steelman succeed? No — and here is where it breaks:**

- **Confinement does not substitute for the Faddeev term.** A two-derivative energy in a *fixed*
  box still collapses the core toward zero size (E₂ ∝ λ falls as the texture shrinks), winding
  fixed, no node. The boundary pins *total winding*, not *core size*. Derrick bites on the interior
  scale regardless of the box. (The Vakulenko–Kapitanskii finite-size bound `E₂·E₄ ≥ c|H|^{3/2}`
  needs E₄ ≠ 0; with E₄=0 there is no lower bound preventing collapse.)
- **The numbers forbid the crystal.** ξ/R_s = 4.635 (recomputed cold) puts the natural variation
  scale at 4.6× the sphere; "geometry fixes the size at R_s" is contradicted by the document's own
  ξ, which leaves no room for a sub-R_s knot.
- **The equation of motion is S¹.** Eq. (GP) governs a one-component field (π₃(S¹)=0); the S²
  content lives only in the setup prose, not in the dynamics.
- **The energy formula is inconsistent with its own citation** (linear E_H vs Faddeev–Niemi H^{3/4}).

The steelman **does not succeed**. No reading recovers a complete, stabilised, zero-parameter S²
theory. → **CN-JHF-11.**

---

## §0.6 — WHAT SETTLING THIS BUYS (reproduced verbatim)

> This gate decides whether the hopfion / S² medium is a written, stabilised field theory or a
> research target described in prose. It does **not** decide whether that theory has a photon,
> fermions in the voids, or gravity — each is a separate, later gate. **A verdict of "complete
> stabilised action" does not vindicate BCT** — it means the photon question can finally be asked
> on S² ground, where the S¹ no-go results (Gate G′, LINK, RANK) do not reach, and asking it is a
> separate and harder gate. **A verdict of "not a complete action" does not refute the geometry
> or the hopfion intuition** — the void radii remain the correct inradii of that packing and the
> picture may yet be right; what fails is the claim that it is *already a theory* rather than a
> target still to be written down.

---

## CN-JHF NOTICES (tiered)

- **CN-JHF-01 [PROVEN].** Search space: four App JH variants at HEAD `495c867f`. `JH (1)` ≡ `FINAL`
  (SHA-256 `2d830856…`); `GRRRRRRRR` = FINAL + one bibitem-record-number line (carries "53" with a
  duplicated-string typo; FINAL prints stale "27"); `JH.tex` (556 ln) differs only in front-matter.
  All four **physics-identical**. None self-marks canonical. Source auditable → **SC-JHF-4 does not
  fire.**
- **CN-JHF-02 [PROVEN].** The only complete energy functional is Eq. (free-energy) §JH.3.1: a
  two-derivative GP stiffness + a zero-derivative U(2)-symmetric quartic **potential** + a surface
  Josephson term. It contains **no four-derivative (Faddeev/Skyrme) term.**
- **CN-JHF-03 [PROVEN].** Derrick scaling of Eq. (free-energy) at fixed |Ψ₂|: `E(λ)=E₂λ+V_pλ³+E_s`,
  monotone increasing, minimised at λ→0. No finite-size hopfion; the H=1 texture collapses (winding
  fixed, no node). A stabiliser scaling as λ⁻¹ (four-derivative) is required and absent.
- **CN-JHF-04 [PROVEN].** §JH.3.3 "Stability" establishes only topological protection against H
  *changing* (a restatement of π₃(S²)=ℤ); it does not address Derrick size-collapse. Topological
  protection ≠ energetic stability; the document conflates them.
- **CN-JHF-05 [PROVEN].** Eq. (hopfion-energy) `E_H = H·ε₀` (linear) is asserted with a
  Faddeev–Niemi/Sutcliffe citation, but the Faddeev–Niemi energy is sub-linear (`H^{3/4}`, VK
  bound) and requires the missing four-derivative term. The linear formula is neither derived from
  the written functional nor consistent with the cited literature.
- **CN-JHF-06 [PROVEN].** Field-content contradiction **within** App JH: Eq. (GP) is one-component
  GP (S¹, π₃(S¹)=0), while §JH.3.1 declares Ψ₂ ∈ ℂ² (→ S²). Confirmed cold against
  `MINIMAL_BCT.md` ("one-component compact scalar; every written action … a single complex
  scalar"). The corpus's S¹/S² contradiction is real and internal to App JH, not only App-JH-vs-App-J.
- **CN-JHF-07 [PROVEN].** π₃(S²)=ℤ and π₃(S¹)=0 derived cold (Hopf-fibration LES; S¹ universal
  cover ℝ). App JH states both correctly; the topological prerequisite is sound. The failure is
  dynamical (stabiliser), not topological.
- **CN-JHF-08 [ASSERTED — refuted].** N_H=1 "forced by the α₀ Josephson boundary condition"
  (Eq. hopf-matching) is asserted via a type error: it equates the Hopf charge (a bulk integral,
  `(1/16π²)∫A∧dA`, a linking number) to a boundary current flux `∮J·n̂ dA` (π₂ data). A surface
  flux cannot force a π₃ (Hopf) charge; the matching argument does not derive N_H=1.
- **CN-JHF-09 [PROVEN].** ξ/R_s = 2·(ξ/a) = 4.635087589823330 (60 dps; R_s=a/2). The healing length
  exceeds the sphere radius by 4.6×, so no full winding fits inside R_s; the one-knot-per-site
  crystal is geometrically excluded by the document's own ξ, independent of Derrick. (Also:
  Eq. phase-velocity `v_ph=k₀/R_s=6.78c` is dimensionally inconsistent — non-load-bearing.)
- **CN-JHF-10 [PROVEN].** Parameter cost of the stabilised S² theory relative to the S¹ theory:
  **≥ 1 undetermined coupling** (the Faddeev quartic coefficient c₄, absent from the source —
  neither geometry-fixed nor externally supplied), plus the unresolved S¹/S² content
  inconsistency. The "zero free parameters" claim is not met by the written functional.
- **CN-JHF-11 [CONJECTURE].** Steelman fails: fixed-box confinement does not replace the Faddeev
  term (two-derivative energy still collapses the core in a box); ξ/R_s=4.635 forbids a sub-R_s
  knot; the EOM is S¹; the energy law contradicts its own citation. No reading recovers a complete
  stabilised zero-parameter S² theory.
- **CN-JHF-12 [note].** Results 3–6 (half-integer spin from SU(2)→SO(3); twistor helicity h=H/2;
  three generations from D₄ triality; superluminal interior / Kondo electron-mass) all presuppose
  the stabilised hopfion crystal and inherit the SC-JHF-1 gap; each is out of scope here and
  unevaluated. "Three generations = three D₄-triality OHC states" is a relabelling asserted on top
  of an object that is not yet a stabilised soliton.
- **CN-JHF-13 [PROVEN].** App J (`S[\Psi_2]`, bibitem AppJ, "Appendices Vol. 2") has **no `.tex`
  in the tree at HEAD `495c867f`.** The load-bearing prior action is not in the auditable corpus;
  the only form available to this gate is App JH's own quotation of it (Eq. GP, one-component).

---

## SCRIPTS

- `gate_JHF_verify.py` — void radii → α₀, ξ/a, ξ/R_s, r_oct/r_tet at 60 dps (report 40); Derrick
  scaling demonstration. Deterministic; re-runnable in seconds. Output reproduced inline in Step 2.

## CONTAMINATION STATEMENT

This project auto-loads the Cold Ledger (`audit-findings.md`), so before §0 the run had in view the
ledger's item-19 framing of App JH: the S¹/S² contradiction, N_H=1, the four-variant
physics-identity, ξ>a, and the Record-53/DOI facts. Per §0.3 the topology (π₃(S²)=ℤ, π₃(S¹)=0),
the Derrick stability analysis, and every number (α₀, ξ/a, ξ/R_s, r_oct/r_tet) were **re-derived
cold** from the `.tex` and from standard field theory in the terminal, not taken from the ledger.
The variant diff, the absence of any Faddeev term in the equations, the internal Eq.(GP)-vs-§3.1
contradiction, and the ill-founded flux-matching were each established directly from source. The
inherited items I could not derive and have flagged as such: the canonical citation (Record 53 /
DOI 18975018) and the ledger's prior N_H/ξ>a framing.

Incidental exposure: a `grep` for ξ/a surfaced single lines from `audit/notes/note_healing_length.md`
and `audit/gates/LINK/*` — both quarantined by §0.2. I did **not** open those files; ξ/a was taken
from the permitted `audit/MINIMAL_BCT.md` and recomputed from first principles, and the Derrick
result is independent of them.

## WHAT THIS GATE DID **NOT** ESTABLISH

- It did **not** answer the photon question. Whether an S² medium carries a photon (two
  polarisations) is a separate, later gate, and it is **not** reached — SC-JHF-3 did not fire, so
  the S² ground on which that question would be asked does not yet exist as a written theory.
- It did not evaluate fermions-in-voids, gravity, twistor/octonion Results 3–6, or the electron-mass
  mechanism (all presuppose the stabilised crystal).
- It did not refute the geometry or the hopfion **intuition** (§0.6): the void radii remain correct
  inradii; what fails is the claim that the medium is *already a theory*.
- It did not audit App J's action directly (absent from the tree) or App JH4 (Yang–Mills, out of
  scope).
- It wrote **no** new Lagrangian (§0.4): the permitted output is "the action as written lacks a
  stabiliser," not "here is the action it should have been."

*Gate JHF — run and closed 15 September 2026. Model: Claude Opus 4.8. Do not re-run.*
