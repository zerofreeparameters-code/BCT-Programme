# GATE KL — RESULT

## Does the woven knot-lattice stand up?

**Run 15 September 2026. Fresh thread, quarantined.**

---

## DIGEST

Prompt received as a file at a commit-pinned `raw.githubusercontent.com` URL, `curl`'d to disk,
hashed **before** reading:

```
SHA-256(gate_KL_prompt.md) = 9ae6e37b9050cbafd2b06f3136b0f241a0fc7ebf08c5a05370e9963a3d1b8e9d
```

matches the pre-registered digest. Gate executed.

Repo pinned at commit `0ecfa11` (tarball via `codeload`; GitHub API was rate-limited, so no
full 40-hex HEAD SHA is claimed — the short commit `0ecfa11` is the provenance). Primary
sources read from that tree only.

---

## VERDICT (first)

**SC-KL-2 — a modulated crystal can exist only at the cost of couplings *not* fixed by the
geometry; and even then it is never the ground state. SC-KL-3 is provably excluded. Under the
strict "geometry-fixed only" reading the outcome collapses to SC-KL-1 (route forecloses).**

Precisely:

1. **SC-KL-3 (a stable, geometry-fixed crystal *below the uniform state*) is unreachable — and
   this is elementary, not a close call.** The standard Faddeev/BFN energy `E = ∫(c₂|∂n̂|² +
   c₄F²)` with `c₂,c₄ ≥ 0` and **no odd-derivative (chiral / Dzyaloshinskii–Moriya) term** is
   pointwise non-negative. The uniform texture `n̂ = const` has `E = 0` and is therefore the
   global minimum over **all** configurations in **all** topological sectors. No modulated
   texture — knot-lattice or otherwise — can sit below it. A knot-lattice that is *the vacuum*
   (the ground state, below uniform) is what the woven picture needs; it cannot exist here.
   [**PROVEN**]

2. **The best a modulated crystal can be is metastable (a local minimum *above* uniform,
   protected by charge), and reaching even that requires two non-geometry inputs plus the S²
   premise:**
   - a **posited stabilising Faddeev coefficient** `c₄ > 0` of the right sign and size — the
     geometry-fixed gradient-expansion reduction does **not** deliver one (the leading induced
     quartic from integrating out the amplitude mode is destabilising; a positive Faddeev term
     is *posited* in Faddeev–Niemi, not derived from GP) [**CONJECTURE**, tiered below]; and
   - an **imposed period** — the geometry-fixed natural size is `λ* ~ ξ = 2.3175 a`, while the
     FCC primitive cell has period `a`, so `λ*/period = 2.3175 ≠ 1`; the period is a **second,
     independent length** not fixed by `c₂, c₄`. [**PROVEN**]

3. **The premise cost (§0.5):** the corpus's written field is one-component (S¹). Promoting to
   the two-component (S²) order parameter this gate analyses is itself an unwritten assumption.
   [**PROVEN from primary source** — see search-space coverage.]

**Net:** the hopfion-medium programme's load-bearing claim — that the vacuum *is* a woven
knot-lattice ground state — **forecloses along this route**. What survives is at most a
metastable, ≥3-input (S² promotion + posited `c₄` + imposed period) excited configuration, which
is not a vacuum and is not the S² ground the photon question would need. Every stop condition is
addressed; none licenses a favourable conclusion here.

---

## SEARCH-SPACE COVERAGE (before any conclusion, per §0.6)

**Repo tree:** downloaded `codeload` tarball at `0ecfa11`; enumerated the tree. GitHub API
`git/trees` was rate-limited (shared runner IP), so provenance is the short commit, not a full
HEAD SHA — recorded honestly rather than fabricated.

**Allowed primary sources read** (§0.2 permits and requires these):

| source | status |
|---|---|
| `audit/MINIMAL_BCT.md` | read — written field content + action |
| `audit/APPENDIX_INDEX.md` | scanned |
| `tex/BCT_Appendix_JH_FINAL.tex` | read (functional, GP eq., topology claim) |
| `tex/BCT_Appendix_JH.tex` | `file`-typed + diffed |
| `tex/BCT_Appendix_JH_GRRRRRRRR.tex` | `file`-typed + diffed |
| `tex/BCT_Appendix_JH (1).tex` | `file`-typed (≡ `_FINAL`) |
| `tex/BCT_Letter36_OHC_tex.tex` | scanned for any added action term |
| App J / App E standalone action `.tex` | **not locatable** as a file; the action is quoted in `MINIMAL_BCT.md §1.2` ("present in App E, App J") and used from there |
| standard literature (Faddeev–Niemi, BFN, Sutcliffe, Vakulenko–Kapitanskii) | used from knowledge, cited at primary source |

**Quarantine honoured:** did **not** read `audit/gates/*/` (including `JHF/` and `RATIO/`),
`audit/notes/`, the 9–15 Sep threads, BCT-X / Sandbox TOP, or any `gate-*` summary. `audit/gates/KL/`
did not previously exist.

**Canonicity of the hopfion appendix — a finding (CN-KL-01).** Four `BCT_Appendix_JH*.tex`
variants exist (excluding JH4). By MD5 they are **three distinct texts**:

```
bcbe1228…  BCT_Appendix_JH_FINAL.tex   (581 lines)   ≡  BCT_Appendix_JH (1).tex
1c91a1e2…  BCT_Appendix_JH.tex         (556 lines)
b4f21092…  BCT_Appendix_JH_GRRRRRRRR.tex (581 lines)
```

No naming or metadata designates one as canonical (`_FINAL` is duplicated as `(1)`; a
`_GRRRRRRRR` variant of equal length disagrees with it). **A theory whose central appendix has
three non-identical texts and no canonical designation has no single written statement of its
own hopfion.** This does not change the physics verdict — all three write the same *class* of
functional (checked below) — but it is recorded.

**Field content / FCC identification (cold, before any energy):**

- BCT ≡ FCC at `c/a = √2` (body-centred tetragonal special case). Lattice period adopted: `a`
  (one sphere / one primitive cell per period), consistent with `MINIMAL_BCT`'s `ξ = 2.3175 a`.
- Void inradii and coupling (60 dps, 40 reported — `kl_step0_numbers.py`):

```
r_oct = (√2−1)/2 = 0.2071067811865475244008443621048490392848
r_tet = (√6−2)/4 = 0.1123724356957945245493210186764728479915
α₀    = r_oct·r_tet/π = 0.007408055727547908079640101104499873416   (1/α₀ = 134.988…)
ξ/a   = 1/√(8π α₀) = 1/√(8 r_oct r_tet) = 2.317543794911664963039020806144813022013
```

  The two stated forms of ξ are **identical to 55 dps** (`8π α₀ = 8 r_oct r_tet` exactly). This
  reproduces the "ξ ≈ 2.3 a" that reached me via the prompt (contamination-declared) **cold and
  independently** from the radii.
- `R_s/a ≈ 0.5038` (from `MINIMAL_BCT`'s "ξ spans 4.6 sphere radii" ⇒ `ξ/R_s = 4.6`), i.e. a
  sphere of radius ≈ `a/2`. Hence `ξ ≈ 4.6 R_s`: the natural knot is ~4.6 sphere radii and ~2.32
  lattice periods — far larger than one sphere, and larger than the cell it is asked to occupy.

---

## STEP 0 — THE ENERGY AND ITS COEFFICIENTS (derived, not posited)

**What is actually written.** The interior functional, identical in class across all three JH
texts (`BCT_Appendix_JH*.tex`, Eq. *free-energy*), is

```
F[Ψ] = ∫_B³ [ (ℏ²/2m)|∇Ψ|² + (g/2)|Ψ|⁴ ] d³r  +  (α₀ℏ²/2mR_s) ∮_{S²} |Ψ|² dA .
```

Two-derivative Gross–Pitaevskii + on-site quartic + a Josephson surface term. **No
four-derivative (Faddeev/Skyrme) term is written in any variant** — the only occurrences of
"Faddeev"/"Skyrme" in the files are three `\bibitem` citations (lines 555/560/566 of `_FINAL`).
The equation of motion actually written (Eq. GP, `_FINAL` line 118) is one-component,
`−(ℏ²/2m)∇²Ψ + g|Ψ|²Ψ = μΨ`, `Ψ ∈ ℂ`. The topology section (lines 194–198) then **silently
redefines** `Ψ : B³ → ℂ²` to obtain `S³→S²` and `π₃(S²)=ℤ`. **The written dynamics are S¹; the
topological claim is S².** As written, therefore, `c₄ = 0`.

**Reduction to a Faddeev energy (the appendix's best shot, supplied here).** Write `Ψ = √ρ z`,
`z ∈ ℂ²`, `z†z = 1`, `n̂ = z†σz ∈ S²`. At fixed `ρ = ρ₀`,

```
|∇Ψ|² = ρ₀ |∂z|² ,     |∂z|² = ¼(∂n̂)² + |z†∂z|² .
```

The `n̂` two-derivative term is the CP¹ (O(3)) sigma model:

```
E₂ = ∫ c₂ (∂n̂)² ,     c₂ = ℏ²ρ₀ / 8m .        [PROVEN, direct from GP]
```

At this order **there is no Faddeev term.** It is generated only by letting the amplitude relax:
`n̂`-gradients source a density modulation `δρ` that couples linearly to `|∂z|²` with strength
`(ℏ²/2m)` and is penalised by the compressibility `~ g ρ₀`. Integrating `δρ` out (adiabatically)
gives an induced four-derivative term. **Dimensional necessity fixes its scaling:** `[c₂]=E/L`,
`[c₄]=E·L`, so `c₄/c₂` has dimension `L²`, and the only massive scale is the amplitude (Higgs)
mode with gap `2/ξ` — hence

```
c₄/c₂ = O(ξ²) ,     λ* = √(c₄ I₄ / c₂ I₂) = O(ξ) .        [PROVEN scaling]
```

With `ξ = 2.3175 a`, the natural knot size is `λ* ~ ξ ≈ 2.32 a`. **The gradient-expansion small
parameter is `(ξ ∂)²`; that this is *not* small at the scale of one cell (`ξ > a`) is the first
sign the whole reduction is being pushed outside its domain of validity.**

**Is `c₄` fixed by the geometry, with a stabilising sign?** The *magnitude* scaling `c₄ ~ c₂ξ²`
is geometry-fixed. The **sign and precise coefficient are not**: the leading induced quartic
from a single-condensate `δρ`-integration is the *negative* `[(∂n̂)²]²` term (destabilising —
it makes the energy prefer ever-spikier textures), not the positive antisymmetric Faddeev
combination `F²`. A genuinely positive `F²` term is **posited** in the Faddeev–Niemi model and
arises in two-*gap* GL only in specific coupling regimes (BFN). The BCT reduction, being a
one-component field promoted by hand to two components with no independent second-gap physics,
does not supply a geometry-fixed positive `c₄`. **This is tiered CONJECTURE (below): the scaling
is proven; the destabilising sign is argued schematically and from the BFN/Faddeev literature,
not from a full BCT integration.** Either way it is *not* a favourable input.

---

## STEP 1 — THE PERIODIC TOPOLOGY, THEN THE STABILITY

### 1a. Topology of a periodic texture (`kl_topology.py`)

The single-hopfion object of App JH lives on the domain **S³** (a Planck ball with constant
boundary value): `[S³,S²] = π₃(S²) = ℤ`, generator the Hopf map. The KL escape changes the
domain to the **3-torus T³** (one space-filling FCC-periodic texture). For a closed oriented
3-manifold `X`, Pontryagin/obstruction theory gives `[X,S²]` as a **primary** class in
`H²(X;ℤ)` (the preimage of a regular point, a framed link) plus a **secondary** "Hopf"
invariant in `H³(X;ℤ)/(2α ∪ H¹(X;ℤ))`. For `X = T³` (`H¹=ℤ³`, `H²=ℤ³`, `H³=ℤ`):

- **Primary:** `(m₁,m₂,m₃) ∈ ℤ³` — the three `π₂(S²)=ℤ` **sheet (baby-skyrmion) charges**
  through the coordinate 2-tori. These are the well-defined, protected charges.
- **Secondary:** the Hopf part collapses to `ℤ / 2·gcd(m₁,m₂,m₃)` whenever the sheet charges are
  nonzero — so **there is no independent integer "Hopf charge per cell."**

**Consequence (CN-KL-02):** a space-filling periodic S² texture carrying charge is
topologically a **stacked baby-skyrmion crystal**, characterised by `π₂` sheet charges — **not**
a hopfion crystal. Going periodic to dodge Derrick **sacrifices the very `π₃(S²)=ℤ` Hopf
structure that motivated the hopfion medium.** The "integer Hopf charge per cell" the gate's
premise asks for is not a topological invariant of the periodic map. [**PROVEN**]

### 1b. Below-uniform impossibility (`kl_step1_derrick.py`, Fact A)

`c₂,c₄ ≥ 0`, no odd-derivative term ⇒ integrand `≥ 0` pointwise ⇒ `E[uniform]=0` is the global
minimum in every sector. **No modulated crystal is below uniform.** SC-KL-3 requires
below-uniform; it is therefore unreachable. [**PROVEN**] — Contrast: real skyrmion-lattice
*ground* states (chiral magnets) drop below the uniform state **only** through a DMI term (odd
in derivatives, spin–orbit). GP has no such term and none may be invented (§0.4).

### 1c. Derrick in the fixed cell + size-vs-period (Facts B–E)

- **As written (`c₄=0`):** `E(λ) = c₂ I₂ λ` (3D) → minimised at `λ→0` → the lone knot
  **collapses**. This reproduces the JHF collapse result (contamination-declared) directly from
  the written functional. [**PROVEN**]
- **With a posited `c₄>0`:** 3D balance gives `λ* = √(c₄I₄/c₂I₂) ~ ξ ≈ 2.32 a`.
- **The periodic sheet charge is 2D:** the `c₂` sigma energy is scale-invariant (Belavin–Polyakov,
  `E₂ ≥ 4π c₂|m|` per cell), and a four-derivative term scales as `λ⁻²` — **monotonically
  decreasing**, so the texture wants to *grow*. There is **no `n̂`-potential** (the GP quartic at
  `|Ψ|=√ρ₀` is `n̂`-independent — a constant), hence **no geometry-set finite size.** The size is
  set only by where neighbours stop it — i.e. by the **period**, which must be **imposed**.
- **Self-consistency fails:** `λ*/period = 2.3175 ≠ 1`. The geometry-fixed size and the FCC
  period are different lengths. A self-consistent geometry-fixed crystal would need
  `λ* = a`; it comes out `2.32 a`. [**PROVEN**]

**Size-vs-period decision (the crux the woven picture rests on):** with `λ* ~ 2.3a` forced into
a cell of period `a`, neighbouring textures overlap ~2.3-fold. Overlap of that magnitude does
not "protect" a clean charge per cell — it is exactly the regime where the `π₃` Hopf label is
already gone (1a) and only a compressed `π₂` sheet charge survives, sitting **above** uniform at
an **imposed** period. The overlapping-knot-crystal analogy to a skyrmion lattice holds only in
the sense that both are metastable-above-uniform *without* a chiral term — which is the negative
reading, not the positive one.

---

## STEP 2 — SELF-CONSISTENCY AND THE PARAMETER COUNT

**Is the crystal self-consistent?** No. The geometry-fixed `c₄` (even granting its scaling and a
posited positive sign) yields `λ* ~ ξ = 2.32 a`, not `a`. The period must be imposed as an
independent length. The crystal is not "selected" by the geometry; it is *assumed* and then
*compressed* to fit.

**Free dimensionless numbers beyond the written S¹ theory** (which has none — `J` is a
normalisation, `ξ` is geometry):

1. **S² promotion** (premise, §0.5): the second condensate component / the S² order parameter —
   unwritten. `+1 structural`.
2. **A posited stabilising `c₄`** of the right sign and size — not delivered by the
   geometry-fixed reduction. `+1`.
3. **An imposed period** (a second length, since `λ* ≠ a`). `+1`.

**Honest cost:** the knot-lattice is a **≥3-input** construction relative to the zero-parameter
S¹ superfluid — and after paying all three it is still only *metastable*, never the vacuum. That
is the opposite of "zero free parameters."

---

## STEP 3 — THE STEELMAN (required)

**Strongest case that a stable, geometry-fixed, FCC-periodic S² knot crystal with integer charge
per cell exists:**

- **Skyrmion lattices are real ground states.** Mühlbauer *et al.*, *Science* **323** (2009) 915
  (MnSi A-phase); baby-skyrmion crystals are well established. A periodic charged texture *can*
  be the thermodynamic ground state.
- **Two-component condensates support knots.** Babaev, Faddeev, Niemi, *Phys. Rev. B* **65**
  (2002) 100512 — a Faddeev-type term and knotted textures arise in two-gap GL. Faddeev & Niemi,
  *Nature* **387** (1997) 58 — stable knots exist in the Faddeev model; Vakulenko & Kapitanskii's
  `E ≳ |Q|^{3/4}` bound guarantees a finite-size minimiser there.
- **High-charge stable knots are computed.** Sutcliffe, *Proc. R. Soc. A* **463** (2007) 3001 —
  explicit stable Hopf solitons to large `Q`.

**Where the steelman is decisive vs. where it fails for BCT:**

- Every skyrmion-lattice that is a *ground state below uniform* requires a **chiral/DMI term**
  (or a competing dipolar/frustration interaction). Remove it and the lattice is metastable,
  **above** the uniform state — established in the chiral-magnet literature. GP has no DMI and
  none is geometry-fixed in BCT. → **SC-KL-3 remains excluded even granting the steelman.**
- Sutcliffe's and Faddeev–Niemi's stable knots live in the **pure Faddeev model with a posited
  positive `c₄`** — not derived from GP. In BCT the `c₄` is unwritten (all variants) and not
  delivered with stabilising sign by the geometry-fixed reduction. → the crystal needs a
  **posited** coupling (SC-KL-2), exactly as found.
- Faddeev-model and BFN knot sizes are **several ξ** — matching `λ* ~ 2.3a` here — i.e. **larger
  than the cell**, so "one clean knot per cell" is not what the physics gives; severe overlap and
  the loss of the `π₃` label (1a) are.

**The steelman therefore does not overturn the verdict; it sharpens it.** A stable *ground state*
crystal exists in nature only via a mechanism (DMI) absent from and not permitted in the BCT
energy. The most the BCT energy can host is a posited-`c₄`, imposed-period, **metastable**
crystal — SC-KL-2, above uniform.

---

## CN-KL NOTICES (tiered)

- **CN-KL-01 [PROVEN].** The hopfion appendix has **three non-identical texts** and no canonical
  designation (`_FINAL`≡`(1)` ≠ `.tex` ≠ `_GRRRRRRRR`). No single written statement of the
  hopfion exists.
- **CN-KL-02 [PROVEN].** App JH's Eq. GP is one-component (S¹); its topology section silently
  uses a two-component (S²) field. The written dynamics do not support the written topology.
- **CN-KL-03 [PROVEN].** The written functional (all variants) is two-derivative GP with **no
  Faddeev term**: `c₄ = 0` as written; the appendix's "topologically protected ⇒ stable" claim
  ignores Derrick collapse.
- **CN-KL-04 [PROVEN].** For a positive-definite `c₂|∂n̂|² + c₄F²` with no chiral term, the
  uniform state is the global minimum in every sector; **no modulated crystal is below uniform.**
  SC-KL-3 is unreachable.
- **CN-KL-05 [PROVEN].** Cold: `ξ/a = 1/√(8π α₀) = 1/√(8 r_oct r_tet) = 2.31754…`; the two forms
  are exactly equal. `λ*/period = 2.3175 ≠ 1` ⇒ the FCC period is a second, imposed length.
- **CN-KL-06 [PROVEN].** `[T³,S²]` is classified by `π₂` sheet charges in `H²(T³)=ℤ³`; the Hopf
  part is only defined mod `2·gcd` once sheet charges are nonzero. A periodic charged texture is
  a **baby-skyrmion crystal, not a hopfion crystal** — the periodic escape discards `π₃(S²)`.
- **CN-KL-07 [CONJECTURE].** The geometry-fixed reduction does not deliver a **stabilising**
  `c₄`: the leading induced quartic from `δρ`-integration is the destabilising `[(∂n̂)²]²` term,
  not `+F²`; a positive Faddeev coefficient is posited (Faddeev–Niemi) or needs a genuine
  second-gap regime (BFN), which BCT's promoted single component does not obviously provide. The
  `c₄ ~ c₂ξ²` **scaling** is proven; the **sign** is argued, not fully computed.
- **CN-KL-08 [ASSERTED].** *Granting* a posited positive `c₄` and an imposed period, a metastable
  (above-uniform) stacked baby-skyrmion crystal with protected `π₂` charge per cell plausibly
  exists (steelman). This is the most favourable outcome available and it is still SC-KL-2, not a
  vacuum.

---

## PARAMETER COST (summary)

| input | fixed by geometry? | needed for what |
|---|---|---|
| S² order parameter (§0.5) | **no** (unwritten premise) | to ask the question at all |
| positive Faddeev `c₄` (sign+size) | **no** (posited) | to resist Derrick |
| lattice period `= λ*` | **no** (`λ*=2.32a ≠ a`) | to set the crystal size |

≥3 non-geometry inputs; result is metastable, not a ground state. Cf. "zero free parameters."

---

## CONTAMINATION STATEMENT

Findings that reached this session and were **re-derived, not inherited** (§0.3):

- **From the gate prompt itself:** the JHF result (App JH is two-derivative GP with no Faddeev
  term; lone hopfion collapses by Derrick; `ξ ≈ 2.3 a`; knot bigger than one sphere; `c₄ ~ ξ²`;
  the S¹/S² contradiction). Each was re-derived independently here: I **read** the functional
  (two-derivative GP, no Faddeev term — CN-KL-03), computed `ξ/a = 2.31754…` **cold** from the
  radii (CN-KL-05), re-derived the Derrick collapse from positive-definiteness/scaling
  (Step 1c), and read the S¹/S² switch directly in the `.tex` (CN-KL-02).
- **From `audit/MINIMAL_BCT.md` (an allowed read):** it *asserts* prior gate conclusions ("field
  is one-component [Gate RANK]", "π₂(S¹)=π₃(S¹)=0, no hopfions"). I used it **only** for the
  written field content and action (primary-source facts) and did **not** inherit its topological
  conclusions — I derived the periodic topology `[T³,S²]` myself (CN-KL-06), which is a different
  and more careful statement than its per-sphere remark.
- **From auto-loaded chat context:** general BCT programme facts (identity, infrastructure).
  These bear on none of the physics.

**Not consulted (quarantine):** `gate-jhf` and all `gate-*` memory/summaries; `audit/gates/*/`
(incl. `JHF/`, `RATIO/`); `audit/notes/`; the 9–15 Sep threads; BCT-X / Sandbox TOP; any
concurrent gate deliverable.

---

## §0.5 — THE PREMISE, STATED AS A COST (reproduced verbatim)

> The S² (two-component) order parameter is **not** the corpus's written field content —
> MINIMAL_BCT and App JH's own equation of motion (Eq. GP) are one-component (S¹). Promoting to
> S² is the premise of this gate and its first declared cost. A verdict of SC-KL-3 therefore
> establishes the ground for a *hypothetical* S² theory; it does **not** retroactively make App
> JH a written theory (that still owes a complete stabilised action). Record this explicitly.

*Recorded: the promotion is unwritten (Eq. GP is S¹, confirmed by direct read); it is cost #1.*

## §0.7 — WHAT SETTLING THIS BUYS (reproduced verbatim)

> This gate decides whether a woven, FCC-periodic S² knot-lattice is a stable geometry-fixed
> ground state of the standard Faddeev/BFN energy. It does **not** decide whether that lattice
> has a photon, fermions, or gravity — each is a separate, later gate. **A verdict of "stable
> geometry-fixed crystal" does not vindicate BCT** — it means the S² ground the photon question
> needs now exists, and asking the photon question is a separate and harder gate. It also does
> not supply App JH a written action; that remains owed. **A verdict of "no stable crystal" does
> not refute the geometry** — the void radii, the percolating interstitial network, and α₀ remain
> correct; what fails is the specific claim that a knot-lattice is the vacuum's ground state.

---

## WHAT THIS GATE DID **NOT** ESTABLISH

- It does **not** answer the photon question (SC-KL-3 not reached; and even a favourable verdict
  would leave the photon to a separate, harder gate).
- It does **not** supply App JH a written action. The written functional is two-derivative GP; a
  complete stabilised ℂ² action with a geometry-fixed Faddeev term remains **owed**.
- It does **not** refute the void geometry: `r_oct`, `r_tet`, `α₀`, the percolating interstitial
  network, and `ξ = 2.31754… a` all stand, cold-confirmed. What fails is only the claim that a
  knot-lattice is the vacuum's ground state.
- It does **not** address void-fermions or gravity.

---

## SCRIPTS (deterministic, re-runnable)

- `kl_step0_numbers.py` — void radii, `α₀`, `ξ/a` (both forms, equality check), `R_s`,
  `λ*/period` (60 dps, 40 reported).
- `kl_step1_derrick.py` — below-uniform impossibility; 3D Derrick (collapse at `c₄=0`, `λ*~ξ`
  otherwise); `c₄/c₂ ~ ξ²`; 2D baby-skyrmion "wants to grow / no potential"; period
  self-consistency.
- `kl_topology.py` — `[T³,S²]` sheet-charge classification and the mod-`2·gcd` Hopf reduction,
  vs `π₃(S²)=ℤ` for the S³ domain.

*Gate KL run and closed 15 September 2026. Verdict SC-KL-2 (SC-KL-3 excluded; SC-KL-1 under the
strict geometry-fixed reading). The woven knot-lattice is not the vacuum's ground state.*
