# GATE RATIO — DELIVERABLE

**Model executing this gate: Claude Opus 4.8** (`claude-opus-4-8`).
**Executed: 14 September 2026. Cold Ledger, single thread.**

---

## 0 — DIGESTS

| artifact | sha256 | size |
|---|---|---|
| `gate_RATIO_prompt.md` (received, verified) | `5a0c08773431c4b9de7fd69a7346c2cb087a283c49b8c1c256431b6a27aec2f3` | 7008 B |
| pre-registered digest (matched) | `5a0c08773431c4b9de7fd69a7346c2cb087a283c49b8c1c256431b6a27aec2f3` | 7008 B |
| corpus tarball `68ffd73…` (pinned state) | `e4f5baf1e2e13ec53192bb47c6552052a674c1d36c92d66831d0255abe66ed64` | 45,759,479 B |

Hash matched before reading. Handoff via commit-pinned `raw.githubusercontent.com`. Not pasted.

---

## 1 — SEARCH-SPACE COVERAGE (reported first, per §0.5)

- Corpus extracted from the pinned tarball. **135 `.tex`** files total, **26 at tree root** (gate stated ~134 / 26 — consistent).
- Appendices Vol 1 = 3 genuine PDFs; Vol 2 = a `.zip` holding an 18 MB PDF; navigation via `audit/appendix_index.csv` (the `.md` index is a `data`-typed blob; the CSV is the usable index). Every file typed with `file` before use.
- Radius notation in corpus: `roct` (154), `rtet` (163), `r_{oct}` (9), `r_{tet}` (4).
- **Explicit ratio usage `roct/rtet`: none found** in 135 `.tex` (grep empty).
- Read: `gate_RATIO_prompt.md` (verified), `audit/MINIMAL_BCT.md` (permitted), `audit/appendix_index.csv`, and targeted `.tex` bodies (Volume1/2, Monograph_PLB, PRL_Letter, Letter19, Letter127, Letter129, Appendix JH4). **Not read: `audit/notes/`, any `audit/gates/*/` deliverable** (quarantine).

---

## 2 — VERDICT (first)

**SC-RATIO-2. Every observable of the minimal theory depends on r_oct and r_tet only through their product. The geometry supplies one number — one length scale — and computing anything measurable additionally requires an external scale, which the corpus supplies by assumption (a = ℓ_P).**

Sharpened beyond the stop condition's wording: **the ratio r_oct/r_tet = 1.8430 was never a free datum.** It is a fixed mathematical constant of FCC close-packing, `(√2−1)/(√(3/2)−1)`, identical for any sphere radius. So the model does not have "two radii" as independent inputs at all: it has **one scale** and **one packing choice (FCC)**, the latter fixing the ratio with zero freedom. "Two radii, zero parameters" is, epistemically, one number fixing one length scale — the same situation the census closed for Λ_QCD.

This does **not** refute the geometry (§0.6). The void inradii are the correct inradii of the packing. What fails is the claim that the model extracts two numbers' worth of content from them.

---

## 3 — STEP 0: OBSERVABLE TABLE (with the product/ratio column)

The minimal action (MINIMAL_BCT §1.2) is
`S = ∫d⁴x [ J(∂Ψ)*(∂Ψ) − (J/4ξ²)(|Ψ|²−Ψ₀²)² ]`, one complex scalar, with the **only** geometric input being `ξ = 1/√(8·r_oct·r_tet)`. Writing each observable as `∝ r_oct^p · r_tet^q`, dependence is product-only iff `p = q`.

| observable | form | (p, q) | depends on |
|---|---|---|---|
| healing length ξ | `1/√(8 r_o r_t)` | (−½, −½) | **product** |
| sound speed c_s | `∝ 1/ξ` | (+½, +½) | **product** |
| amplitude (Higgs) gap | `2/ξ = 0.8630` | (+½, +½) | **product** |
| phonon dispersion (continuum) | `ω=c_s k`, correction scale ξ | (−½, −½) | **product** |
| vortex core size | `∼ ξ` | (−½, −½) | **product** |
| vortex energy / length | `∝ ln(R/ξ)` | (−½, −½) | **product** |
| circulation quantum | `2π` (integer, topological) | (0, 0) | **neither** |
| vortex–vortex interaction | `∝ ln(r/ξ)` + core at ξ | (−½, −½) | **product** |
| c_s anisotropy (continuum) | 0 (rotational invariance) | — | **neither** |
| condensate depletion at a void | *not in the minimal action* | — | not an observable of the minimal theory |
| α₀ | `r_o r_t/π` | (+1, +1) | **product** |

Every observable that the minimal action actually possesses depends on the radii only through the product. The two entries that could break this — anisotropy and void depletion — are **absent from the minimal action** (isotropic continuum GP with no void potential). Verified numerically in `ratio_step0_arithmetic.py`.

---

## 4 — STEP 1: THE LATTICE DISPERSION (where the ratio could enter)

The continuum GP action is rotation-invariant, so its dispersion is isotropic and carries no ratio. The lattice is the only candidate. Scalar phonon, harmonic n.n. coupling, sound tensor `D_ij = Σ_δ K_δ δ_i δ_j`; results from `ratio_step1_lattice_dispersion.py`:

**Geometry.** The BCT lattice has one shape parameter η = c/a and one scale a. The model's radii, `r_oct=(√2−1)/2`, `r_tet=(√6−2)/4`, are exactly the FCC interstitial inradii of spheres of radius a/2 — i.e. **they pin η = √2 (FCC), point group Oₕ (cubic), coordination 12.** Confirmed to 15 digits: `(√2−1)R = r_oct`, `(√(3/2)−1)R = r_tet` with `R = ½`.

**Anisotropy vs shape.**

- Coordination-8 regime (η < √2, spheres touch along the body diagonal): `c_z/c_x = η` **exactly** (checked η = 1.0, 1.1, 1.2247, 1.3, 1.4142 → ratio = η to 5 digits). *If the shape were free, the scalar sound speed would read out η directly, and the ratio would do genuine work.*
- FCC point η = √2: close-packing brings the four in-plane bonds to the same distance → 12-fold coordination, cubic symmetry. `D_xx = D_yy = D_zz = 4.0000`, off-diagonal `= 0`. **Exactly isotropic.** The shape's imprint on the leading dispersion cancels.
- Residual anisotropy appears only at O(k⁴): `ω² ≈ 4.000 k² − 0.2083 k⁴` along [100] vs `−0.2037 k⁴` along [111] — a fixed pure FCC constant, no independent r_oct/r_tet content.

**The dilemma this exposes.** The model cannot simultaneously (a) hold the shape fixed at zero cost (zero free parameters) and (b) have the ratio do observable work. Fixing the shape to FCC — which the specific radii do — makes the leading dispersion isotropic and the ratio inert. Letting the shape float would make the ratio do work but reintroduces η as a genuine free geometric parameter. The specific radii choose the pinned horn: **isotropic, ratio inert.**

The void *positions* (as distinct from radii) add nothing: at fixed FCC they are determined by the same single scale a, so they carry no information the radii do not.

---

## 5 — STEP 2: THE COUNTING

- **Dimensionless numbers the geometry supplies:** exactly one non-trivial — `ξ/a = 2.3175` (from the product). The ratio `r_oct/r_tet = 1.8430` supplies **zero** (fixed by FCC). So dimensionless content = **1**.
- **Dimensionful scales, and what fixes them:** the geometry fixes only ratios; it cannot produce a length in physical units. **a = ℓ_P is supplied externally, by assumption.** The corpus states this outright — App JH4: "a single-point calculation at a = ℓ_P"; Monograph_PLB: the "parameter that anchors the lattice spacing to physical units." The corpus even ties `Λ_QCD = 220 MeV` to this single anchor, which is precisely the equivalence the gate flags.
- The dynamical GP constants J (stiffness) and Ψ₀² (density) are not fixed by void geometry either; they are additional inputs setting energy and amplitude scales.

**Plainly: to compute a pure length ratio, the minimal theory needs zero external numbers. To compute any measurable (dimensionful) quantity, it needs at least one external scale (a = ℓ_P), plus J and Ψ₀² for energetic/dynamical observables.** The geometry's own contribution to measurable content is one dimensionless number (ξ/a), delivered through the product.

---

## 6 — STEP 3: THE STEELMAN (required; this gate must be able to find "two")

I constructed the strongest case for two-parameter content and report it prominently.

**S1 — The corpus uses individual radii everywhere.** The full corpus does *not* restrict to the product. Documented, individual-radius formulas:
- `α₂ = r_oct²/π`, feeding `f_oct = ¾ + (α₀/2)(1+α₀) − α₂²/32` → `v_BCT = 246.2198 GeV` (Volume2).
- `x_EW = (4π³ r_oct/3S_EW)(1+NLO)` and `x_SU(3) = (8π³ r_tet/3S_QCD)(…)` (Letter127).
- `cos θ_K = r_oct − ½` (Monograph_PLB); `ℓ_oct = r_oct·ℓ_P` (Letter129).

If these were consequences of the theory under test, the ratio would do enormous work and the verdict would be SC-RATIO-1.

**Why S1 fails for the minimal theory.** None of these is derivable from the minimal GP action, whose sole geometric input is ξ (the product). Each is a *separate posited map* from geometry to a Standard-Model observable, layered with α₀/α₂ correction terms and a "universal NLO correction" `NLO = α₀(4π+1)/π²`, and anchored by external scales (Λ_QCD, the D4 instanton actions S_EW, S_QCD). Volume2 itself flags that "all five audited holes… are formally closed in Volume XX," i.e. the derivation is admitted-incomplete. Structurally these are the **N-class** constructions — (geometric value)·(1 + N·α₀) with N chosen after the fact — that MINIMAL_BCT §0(3) records as scored ≈0 bits against a null model. They use the radii separately, but not in a way the minimal theory can support.

**S2 — The structural invariant ξ/r_oct = 11.19 (Letter19).** Because `8π·α₀ = 8·r_oct·r_tet`, this equals `1/(√8·r_oct^{3/2}·r_tet^{1/2})` — genuinely dependent on the radii with unequal powers (−3/2, −½), hence on the ratio. This is the single cleanest candidate for SC-RATIO-1. It fails the bar because it requires **r_oct as an independently observable length**, and the minimal action contains no such length — only ξ. The corpus concedes this: it is testable only by "any sub-Planckian probe of the electron's internal structure," i.e. by probing the substrate the minimal theory abstracts away. And even granting substrate access, r_oct/r_tet is FCC-fixed, so the invariant encodes a *prediction of the packing*, not a *free parameter*.

**S3 — Lattice anisotropy.** Would carry the ratio if the shape were free (Step 1: `c_z/c_x = η`), but the radii pin FCC and the leading anisotropy cancels. Fails.

**S4 — Two void species with distinct occupation/coupling; void-volume observables.** Not in the minimal action (single quartic coupling, no void potential, no free-volume term). Any such term is a modification that adds parameters. Fails as content of the minimal theory.

**The steelman does not succeed for the theory under test.** It succeeds only for the full corpus, and only by using maps that other gates in this audit have already closed.

---

## 7 — CN-RATIO NOTICES (tiered)

- **CN-RATIO-01 [PROVEN].** In the minimal GP action, the void radii enter only through ξ = 1/√(8 r_oct r_tet); every observable of that action is a function of {ξ, J, Ψ₀²} (plus topological integers) and so depends on the radii only through the product.
- **CN-RATIO-02 [PROVEN].** r_oct = (√2−1)R and r_tet = (√(3/2)−1)R are the FCC interstitial inradii of a single sphere radius R = a/2 (verified to 15 digits). The ratio r_oct/r_tet = (√2−1)/(√(3/2)−1) = 1.8430 is scale-independent and carries no information. The geometry has one scale, not two independent radii.
- **CN-RATIO-03 [PROVEN].** The continuum GP action is rotation-invariant; its dispersion is isotropic. Anisotropy requires lattice gradient terms not present in MINIMAL_BCT §1.2.
- **CN-RATIO-04 [PROVEN].** Scalar phonon on BCT: `c_z/c_x = η` in the coordination-8 regime; at η = √2 (FCC, which the radii pin) the sound tensor is exactly isotropic (D_xx=D_yy=D_zz=4.0000, off-diagonal 0). Residual anisotropy is a fixed O(k⁴) FCC constant. The lattice does not deliver ratio-dependence at the model's own geometry.
- **CN-RATIO-05 [PROVEN].** The minimal theory fixes only dimensionless numbers; a dimensionful observable requires an external scale, supplied in the corpus as a = ℓ_P by assumption (App JH4; Monograph_PLB), which the corpus itself equates to the Λ_QCD-input situation.
- **CN-RATIO-06 [ASSERTED — as content of the minimal theory].** The corpus's individual-radius formulas (α₂=r_oct²/π→v_BCT; x_EW∝r_oct; x_SU(3)∝r_tet; cos θ_K=r_oct−½) use the radii separately but are standalone geometry→observable posits with α₀/α₂/NLO factors and external scales; not derivable from the minimal action, and structurally the N-class closed elsewhere in the audit.
- **CN-RATIO-07 [CONJECTURE].** ξ/r_oct = 11.19 depends on the radii separately and is the strongest SC-RATIO-1 candidate, but its status as an observable of the minimal theory is unestablished (it needs r_oct as an independent length, which the minimal action lacks); if substrate-observable, the ratio it encodes is still FCC-fixed, hence not a free parameter.

---

## 8 — SCRIPTS

- `ratio_step0_arithmetic.py` — inputs, FCC-interstitial identities, ratio scale-invariance, observable power-structure table (mpmath, 40 dps).
- `ratio_step1_lattice_dispersion.py` — BCT scalar-phonon sound tensor vs axial ratio η; c_z/c_x = η; FCC isotropy; O(k⁴) cubic anisotropy.
- `ratio_step2_corpus_audit.sh` — search-space audit and corpus grep (radius notation, absence of explicit ratio usage, a=ℓ_P anchoring, the Letter19 invariant).

All three run clean on the pinned corpus. Outputs reproduced inline above.

---

## 9 — CONTAMINATION STATEMENT

I did not use `conversation_search` or `recent_chats`. I did not read `audit/notes/` or any `audit/gates/*/` deliverable. Files read: `gate_RATIO_prompt.md` (hash-verified), `audit/MINIMAL_BCT.md`, `audit/appendix_index.csv`, and specific `.tex` bodies for the observable/steelman audit.

Per §0.3 (inheritance forbidden): MINIMAL_BCT.md is a construction, treated as a claim set to check, not inherited. Its §3 already states the product-collapse hypothesis and the figure 1.843; **I re-derived both independently** and did not take them on trust. The load-bearing new content of this run — that r_oct and r_tet are the FCC interstitial radii of a *single* sphere radius (so the ratio is a fixed constant, not a datum), and that the lattice anisotropy which could carry the ratio cancels exactly at the FCC point the radii pin — is original to this execution. I also hold background memory summaries of earlier gates in this project; I deliberately did not open or rely on them for this gate. MINIMAL_BCT §1's field content (one complex scalar) and action are consistent with what §1.2 literally writes; no SC-RATIO-4 correction is triggered.

---

## 10 — §0.6 REPRODUCED VERBATIM

> This gate decides how many independent numbers the minimal theory contains. It does **not**
> decide whether the theory is correct, whether it predicts anything, or whether the void
> geometry is physically motivated. **A verdict of "two" does not vindicate BCT** — it means one
> claim survives that has not yet been scored, and scoring it is a separate and harder gate.
> **A verdict of "one" does not refute the geometry** — the void radii remain the correct
> inradii of that packing; what fails is the claim that the model extracts two numbers' worth of
> content from them.

---

## 11 — WHAT THIS GATE DID NOT ESTABLISH

- **Not** that BCT is wrong, or that the FCC void inradii are wrong geometry — they are correct (CN-RATIO-02).
- **Not** that the minimal theory predicts anything: verdict "one" says its geometric content is one length scale requiring an external anchor; scoring predictive content is a separate matter.
- **Not** a ruling on the full corpus's individual-radius formulas as physics — only that they are not consequences of the minimal action; whether any survives on its own terms is for other gates.
- **Not** a resolution of whether the substrate radii are in-principle observable (CN-RATIO-07 left CONJECTURE); if they were, the invariant they satisfy is still an FCC prediction, not a free parameter.
- **Not** a claim that the O(k⁴) FCC anisotropy is unmeasurable in principle — only that it carries no independent r_oct/r_tet content.

*Gate RATIO closed by Claude Opus 4.8, 14 September 2026. Verdict SC-RATIO-2.*
