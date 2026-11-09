# Gate TWIST — RESULT (blind replication run, 9 November 2026)

**Programme:** BCT Superfluid Lattice Model, Cold Ledger
**Card:** `audit/gates/gate_TWIST_prompt.md` @ commit `c3e7cde80e3c0ef55057256d98009fd019f95c26`
**Run:** 9 Nov 2026, 20:00–21:00 AEDT, fresh thread inside the BCT Project, Claude Fable 5.1 (`claude-fable-5-1`)
**Tier cap:** CONJECTURE (same-session result; card §11)

---

## 0. Hash check (before reading)

| | pre-registered | measured |
|---|---|---|
| SHA-256 | `7863d39d83dd607aafa46e85a44dccdcff39ae31beea1504473a3aaf19a3b01f` | `7863d39d83dd607aafa46e85a44dccdcff39ae31beea1504473a3aaf19a3b01f` |
| bytes | 11055 | 11055 |

Fetched by `curl -sL -o` to disk from the commit-pinned raw URL, hashed with `sha256sum`, compared, **then** opened. Byte-exact. The same file in the fresh shallow clone (HEAD `ef24df3`, "Auto-sync Zenodo DOIs", 8 Nov 2026 12:35 UTC) hashes identically.

## 1. Contamination statement

Answering the three items Michel asked for mid-run, plus the card's §3 list:

1. **Past-chat search and memory.** No past-chat search tool was called at any point. The Project's memory *listing* (file paths + one-line auto-summaries) is injected into the session by the platform and was visible from the first turn; it includes a one-line summary of the blocked file `areas/hopfion-interior-idea.md` ("same OHC medium as outside, confined by the double layer, moving as a hopfion/EM-like toroidal vortex …"). That file was **not opened**. Memory files that were read, all permitted under §3 as closed findings or process notes: `preferences.md`, `ways-of-working.md`, `audit-findings.md` (the Cold Ledger: QED-DERIV, QED, BC, PROMOTE, STIFF, ICE, LINK, KL, JHF entries), `gates-closed-archive.md` (KL, ICE, STIFF, PROMOTE detail), `gate-jhf.md`, `gate-link.md`. The "Generate memory from chats" setting cannot be verified from inside the session; no memory *writes* were made during the run.
2. **Project.** Yes — this thread runs inside the BCT Superfluid Lattice Model Project (the memory subtree and Project docs confirm it).
3. **Model.** Claude Fable 5.1 (`claude-fable-5-1`). The card §11 asks for an "Opus-class model"; this is a deviation from the run protocol as written, recorded here for Michel to judge.

§3 blocked material: the 8 Nov session record, `DESK_hopfion_in_sphere_RESULT.md`, `partA_neutral.py`, `partB_spheromak.py`, `rings.py`, `rings2.py` — **none opened**, none present in the clone's `tex/` or `audit/desk/` listings that were viewed. **Additional disclosure:** the repo clone already contains `audit/gates/TWIST/gate_TWIST_RESULT.md`, `gate_TWIST_ADDENDUM_unblinded.md`, `SHA256SUMS`, `output/` and `scripts/` — a **prior run of this gate**. None of those files were opened; this run is therefore a blind replication, and its files are committed in a separate subfolder so nothing of the prior run is overwritten. Michel can compare the two verdicts.

Card §9 (the author's forecast) is part of the card and was read before the run, as the card intends; it is scored in §8 below.

**Status: not contaminated** with respect to §3's list, with the one-line listing summary disclosed above.

## 2. Model as run (card §4, unchanged)

FCC (BCT at c/a = √2), a = ℓ_P, R = a/2, r_oct = (√2−1)/2·a, r_tet = (√6−2)/4·a; V0 = ∫[(ħ²/2m)|∇Ψ|² + (g/2)(|Ψ|²−n₀)²], Ψ = √ρ χ, χ ∈ ℂ²; ξ = a/√(8πα₀) = 2.31754 a used as given (CN-C1-04); shell term (α₀ħ²/2mR)∮|Ψ|²dA; no charge unless bought. Conventions: K := ħ²n₀/2m (stiffness), ξ := ħ/√(2mgn₀), F_ij := n·(∂_in×∂_jn), (∇×a)² = F_ijF_ij/8. Where a number needs K's scale, the Planck normalisation n₀a³ = 1, m = m_P (App J's J = 1) is **declared**: K a² = ½.

## 3. Q1 — Does the twist field get its own Maxwell-type energy from the medium? **FAIL**

**(a) Identities** — `twist_q1a_identity.py`, exact sympy derivatives of random 3-mode trigonometric ℂ² fields, mpmath 60 dps, 3 fields × 7 points:

| identity | max residual |
|---|---|
| |∇χ|² = ¼|∇n|² + a² | 6.3 × 10⁻⁶⁰ |
| ∂_ia_j − ∂_ja_i = ½ n·(∂_in × ∂_jn) (Mermin–Ho) | 6.3 × 10⁻⁶⁰ |
| |∇Ψ|² = (∇√ρ)² + ρ|∇χ|² | 3.0 × 10⁻⁶⁰ |
| gauge: n invariant, a → a + ∇λ | ≤ 9.2 × 10⁻⁶¹ |

All pass the 10⁻¹⁰ bar.

**(b) Is a slaved?** Writing χ = e^{iφ}ζ, a = −iζ†∇ζ: (ħ²/2m)|∇Ψ|² = (ħ²/2m)(∇√ρ)² + ρ·X̃ with X̃ = (ħ²/2m)[(∇φ + a)² + ¼(∇n)²]. The connection enters V0 **only** through the superflow v = ∇φ + a, and ∇×v = ∇×a = ½ n·∂n×∂n is fixed by n. a has no gradient energy of its own and no canonical momentum: it is slaved to the texture (plus gauge). No independent propagating degrees of freedom.

**(c) Is c_F(∇×a)², c_F > 0, generated?** — `twist_q1bc_induced.py`
- *Tree level:* V0 is quadratic in gradients; (∇×a)² is quartic. **c_F(tree) = 0.**
- *Density fluctuations:* ρ = n₀ + δρ; the quadratic form is ½δρ[g − (ħ²/4mn₀)∇²]δρ + δρ·X̃; the fluctuation determinant is texture-independent at this order, so "one loop" adds nothing texture-dependent beyond the Gaussian elimination. Kernel inverse in gradient expansion: g⁻¹[1 − (ξ²/2)k² + (ξ⁴/4)k⁴ − …]. Induced terms:
  - 4-derivative: **−(1/2g)X̃² = −(Kξ²/32)[(∇n)²]² − (Kξ²/8)(∇n)²v² − (Kξ²/2)v⁴** — every piece negative;
  - 6-derivative: +(Kξ⁴/4)(∇X̃/K)² — positive, but not a function of F_ij, and outside the expansion's validity for textures smaller than ξ = 2.3a (the sphere is R = 0.5a).
  - Projection on the Faddeev invariant: [(∇n)²]² = F_ijF_ij + (∂_in·∂_jn)² (verified numerically to 2 × 10⁻⁵⁹, both invariants ≥ 0), so the coefficient of F_ijF_ij is −Kξ²/32, i.e. **c_F = −Kξ²/4 = −1.34275 K a²** at ξ/a = 2.317543794911664963039020806144813022013 (40 dps). **Sign negative; scaling ∝ −ξ²** (= −ħ²n₀ξ²/8m). This reproduces CN-KL-07 (GP reduction gives a destabilising quartic, not +F²) by explicit computation.
- *Phase mode:* eliminating φ at uniform ρ leaves K a_i P^T_ij a_j with P^T = δ_ij − k_ik_j/k² — a **k⁰ transverse (London/Meissner) term**, equivalently K|∇×a|²/k² (infrared-enhanced), the opposite power of k from Maxwell's k²P^T/e². The medium generates a mass term for a, not a kinetic term. Same wall as CN-LINK-10 and Gate QED (ii).

PASS needed c_F > 0 fixed by corpus quantities **and** independent propagating DOF for a; neither holds. **Q1: FAIL.** The BFN route (an F² from B² in a *charged* two-condensate system) is **BOUGHT**: it needs a charge e and a Maxwell term as inputs (cost rows 2–3).

## 4. Q2 — Massless with two polarisations in the voids? **FAIL** (conditional on Q1 BOUGHT)

`twist_q2_mass.py`. Granting (1/4e²)f_ijf_ij with e counted:

- **Uniform medium (the corpus medium — App J §1.1–1.2: "Ψ fills all of space", "same J, same ξ", App JH §3.1: constant ρ₀; card A1):** after φ is eliminated the transverse quadratic form is (k²/e² + 2K)P^T → **m_a² = 2Ke²**, λ_L = 1/√(2Ke²) = a/e in Planck normalisation. m_a = e·m_P ≠ 0 for every e ≠ 0; φ is eaten; **3 polarisations** (2 transverse + 1 longitudinal). No corpus number sets m_a = 0 (only e → 0, which removes the Maxwell term). **FAIL**, as the card's own clause anticipates.
- **Shells condensed, voids empty:** the corpus supplies **no** location-dependent condensation (quotes above); the branch is not reached without a new input (cost row 4). Even if bought, the void network is a set of sub-Planck cavities (r_oct = 0.207a, r_tet = 0.112a) joined through triangular windows of inscribed radius (2/√3−1)R = 0.0774a; the aperture cutoff k_c ≈ 1.84/r_win ≈ 24/a and the lowest cavity modes k ~ π/r ≈ 15–28/a put every propagating mode at ≳10 Planck frequencies. Locally two transverse cavity polarisations exist, but there is no massless propagating mode at any wavelength longer than ℓ_P. **FAIL on geometry alone.**

## 5. Q3 — Screened in the shells so they hold the knot? **FAIL** (conditional)

`twist_q3_shell.py`.

- **λ_shell.** The corpus shell is a δ-potential on |Ψ|² with Ψ *continuous* across it (App J §1.2) — it carries no areal superfluid density of its own, so it screens nothing (Pearl length Λ = 2λ_L²/d → ∞ as d → 0). The bulk London length λ_L = a/e is the same inside the sphere as outside (same medium, A1), so the knot's own field is Meissner-screened *in the interior*; "screened at the shell, free inside" requires the interior and exterior to differ, which A1 and App J deny. Buying a shell of App J's own asserted thickness d = √(r_tet r_oct)a = 0.1526a with areal density n₀d gives Λ = 13.1a/e², Λ/R = 26.2/e²: a closed shell with Λ ≫ R screens only ~R/Λ of the field. Screening at R needs e² ≳ 26 — choosing e to pass is fitting (§8). **Screening does not follow from the model.**
- **Virial budget.** Mean wall pressure of a relaxed force-free Maxwell-type knot with B·n̂ = 0: ū_B/3 (derived: W = R∮(B²/2)dA ⇒ ⟨P⟩ = ū/3). Shell supply from the corpus surface term E_s = 4πα₀KR: P_s = α₀K/R²; in condensation-energy units ε_c = gn₀²/2 = K/2ξ², **P_s/ε_c = 2α₀ξ²/R² = 1/π exactly** (an identity of the card's fixed inputs ξ² = a²/8πα₀, R = a/2 — no fit). Knot field energy from the H = 1 Hopf map at scale R integrated over |x| < R (exact derivatives, mpmath quadrature): R⁴⟨(∇×a)²⟩ = c₁ = 13.4248, so ū_B/ε_c = c₁ξ²/(e²KR⁴) = 2.31 × 10³/e² and **needed/available = πc₁ξ²/(3e²KR⁴) = 2.42 × 10³/e²**. At counted O(1) coupling the shell is short by **three orders of magnitude**; it holds the knot only for e² ≳ 2.4 × 10³ (fitting). The texture part ū_tex/ε_c = 147 pulls inward (Derrick) and is the collapse of Gate JHF, not a pressure the shell can resist. **Q3: FAIL.**

## 6. Q4 — Does a current-carrying shell follow from the medium? **FAIL**

`twist_q4_shell_current.py`.

| item | score | corpus evidence |
|---|---|---|
| (i) real charge in the shell | **ASSERTED** | App J §1.1 "surface-charge double layer", §1.3 "charge Q = 1 (one Planck charge unit)" — labelled an input to the identification by App J itself; V0 and App J's action are neutral (U(1) particle number only). Gate STIFF: a neutral GP hosts no well-defined double layer; Gate BC: σ_s is a two-input fit. Nothing derives a second charge. |
| (ii) counter-moving layers | **ABSENT** | No text in App J, App JH or Letter 36 describes two layers with opposite velocities; the only current named is the single superfluid current J_Hopf (App JH eq. hopf-matching), and the shell is a δ-sheet of one potential. Co-moving layers carry cancelling currents, as the card notes. |
| (iii) insulating contacts | **ABSENT**; wire-medium argument **HOLDS** | Nothing in the sources mentions the 12 contacts. Pendry et al. (1996): ω_p² = 2πc²/(a² ln(a/r)) → ω_p = 1.6–1.8 c/a for r = 0.08–0.15a, and still 0.5 c/a at r = 10⁻¹⁰a (the log is weak): ω_p ~ 10⁴³ rad/s vs ω ≲ 10³⁰ rad/s for the hardest observed photons (ω/ω_p ~ 10⁻¹³). Connected conducting shells at Planck spacing are opaque to all observed light. Contrast: *insulated* conducting spheres give a Maxwell–Garnett dielectric ε_eff = (1+2f)/(1−f) = 9.56 at f = 0.7405 — transparent, no cutoff. The transparency of the vacuum therefore rides entirely on an insulating-contact property the corpus never states. |
| (iv) grip term pinning n on the shell | **ABSENT** | The shell term is (α₀ħ²/2mR)∮|Ψ|²dA — a function of ρ only, U(2)-symmetric; it does not see n. On B³ with free boundary all maps to S² are homotopic (B³ contractible); the Hopf number is protected only with n fixed on ∂B³ (B³/∂B³ ≅ S³). App JH's "topologically protected" (§3.4) assumes the compactification it never supplies. |

PASS needed four DERIVED; result 0 DERIVED, 1 ASSERTED, 3 ABSENT. **Q4: FAIL.**

## 7. Verdict and cost table

### **SC-TWIST-1 — kill at Q1.** No Maxwell-type term for the twist field arises from the medium; a stays slaved to the texture (c_F(tree) = 0; density integration gives c_F = −Kξ²/4 < 0; phase mode gives a London k⁰ term, not Maxwell k²). Q2 also fails conditionally (Meissner mass m_a = e·m_P for every e ≠ 0; no location-dependent condensation in the corpus; the void network cuts off at ~10 Planck frequencies). Q3 and Q4 fail conditionally (shell has no screening of its own; pressure budget short ×2.4 × 10³ at e² = 1; 0/4 shell properties derived).

| # | Input | Free number? | Where needed |
|---|---|---|---|
| 1 | A1: ℂ² order parameter inside and out | — (structural; a free input per Gate PROMOTE) | all |
| 2 | Electric charge coupling the condensate to a gauge field (BFN route) | yes, e | Q1 (to BUY an F² term), Q2, Q3 |
| 3 | Maxwell term (1/4e²)f² for a | — (structural; e already counted) | Q1 BOUGHT, Q2, Q3 |
| 4 | Location-dependent condensation (shells condensed, voids empty) | yes (a confining potential/second phase and its strength) | Q2 branch (ii), Q3 |
| 5 | Shell areal superfluid density (finite thickness d, e.g. App J's asserted d = √(r_tet r_oct)a) | yes, d (App J labels d an input) | Q3 screening |
| 6 | Real shell charge Q beyond particle number | yes (App J: Q = 1 asserted) | Q4(i) |
| 7 | Counter-moving double layer (two velocity fields) | structural + ≥1 number | Q4(ii) |
| 8 | Insulating contacts at the 12 touching points | structural | Q4(iii) |
| 9 | Direction-dependent shell ("grip") term pinning n | yes (its coefficient) | Q4(iv) |

Minimum to reach a working picture along the card's own path: rows 1–4 and 9 (≥ 5 inputs, ≥ 3 of them free numbers), before the pressure budget (row 5 / large e) is even addressed. Nothing was fitted; every coupling is counted (§8 honoured; no α, 137 or measured-constant comparison entered any score — the Planck-frequency vs observed-light comparison in Q4(iii) is the order-of-magnitude the card asks for, not a fit).

## 8. Disclosure scored (card §9)

| forecast | outcome | score |
|---|---|---|
| Q1 FAIL for neutral V0; BFN BOUGHT | FAIL; BFN BOUGHT | **correct** |
| Q2 FAIL (Meissner mass); pass only with location-dependent condensation the corpus lacks | FAIL; corpus lacks it; **and** the void geometry cuts the branch off anyway | **correct, strengthened** |
| Q3 conditional, not reachable without location-dependent condensation | FAIL; shell has no screening of its own; budget short ×2.4 × 10³ at e² = 1 | **correct, quantified** |
| Q4 (i) ABSENT/ASSERTED (ii) ABSENT (iii) ABSENT + wire argument holds (iv) ABSENT | (i) ASSERTED (ii) ABSENT (iii) ABSENT, holds (iv) ABSENT | **correct** |
| Verdict SC-TWIST-1; ≥ 3 inputs | SC-TWIST-1; ≥ 5 inputs counted | **correct; cost higher** |

The author's forecast is confirmed on every item. Because the forecast was in the card, this run cannot claim independence from it on the *verdict codes*; the independent content is the computations (c_F's value and sign, the London-vs-Maxwell kernel, m_a = e·m_P, P_s/ε_c = 1/π, c₁ = 13.42, ω_p ≈ 1.7 c/a) and the two findings the forecast did not contain (void-network cutoff; interior self-screening).

## 9. Notices

- **CN-TWIST-01.** In V0 the CP¹ connection a enters only through the superflow ∇φ + a; its curl is fixed by n (Mermin–Ho, verified to 10⁻⁶⁰). a carries no independent degrees of freedom. [PROVEN, elementary]
- **CN-TWIST-02.** Integrating out density fluctuations in V0 generates −(1/2g)X̃² + (ξ²/4g)(∇X̃)² + …; the quartic's projection on the Faddeev invariant is **c_F = −Kξ²/4 < 0** (−1.34275 Ka² at the corpus ξ). No positive Maxwell/Faddeev term arises from the neutral medium at this order; this makes CN-KL-07's "sign argued" into a computed sign. [PROVEN within the gradient expansion]
- **CN-TWIST-03.** Eliminating the overall phase leaves K a_T² = K|∇×a|²/k² — a London (mass) term for a, infrared-enhanced; the neutral medium generates the *opposite* k-power from a Maxwell term. Any Maxwell term must be imported (BFN: charge + F²), and then CN-TWIST-04 applies. [PROVEN]
- **CN-TWIST-04.** With an imported Maxwell term and coupling e, the uniformly condensed corpus medium gives m_a² = 2Ke² (m_a = e·m_P in Planck normalisation), three polarisations, for every e ≠ 0 — the Meissner wall of CN-LINK-10 / Gate QED (ii) / QED-DERIV T3, now on the ℂ² field. [PROVEN]
- **CN-TWIST-05.** The corpus supplies no location-dependent condensation (App J: same condensate, same J, same ξ everywhere; App JH: constant ρ₀; A1). A void-confined massless mode is therefore not available without a new input; and even then the FCC void network (cavities ≤ 0.21a, windows 0.077a) has its lowest propagating modes at ≳ 10 c/a — no long-wavelength photon lives in the voids. [PROVEN geometry; CONJECTURE as to the exact cutoff constant]
- **CN-TWIST-06.** Because the medium is the same inside and outside (A1), the bulk London screening acts *inside* each sphere too: the knot's own twist field is Meissner-screened in the interior, so "an EM-like knot held by a screening shell" is self-contradictory under A1. [PROVEN given CN-TWIST-04]
- **CN-TWIST-07.** The corpus shell is a δ-potential on |Ψ|² with Ψ continuous (App J §1.2): zero areal superfluid density, zero screening of its own. Buying App J's asserted thickness d = √(r_tet r_oct)a gives a Pearl length 13.1a/e² ≫ R unless e² ≳ 26. [PROVEN]
- **CN-TWIST-08.** The corpus surface term supplies a confining pressure **P_s/ε_c = 2α₀ξ²/R² = 1/π exactly** (identity of the card's inputs ξ² = a²/8πα₀, R = a/2); the virial requirement for an H = 1 Maxwell knot of size R is ū_B/3 = (πc₁/3)·ε_c·ξ²/(e²KR⁴) with c₁ = 13.42, i.e. **2.4 × 10³/e² times** the supply. [PROVEN at order-of-magnitude; c₁ computed for the standard Hopf map, not a relaxed force-free knot]
- **CN-TWIST-09.** Shell properties: real charge ASSERTED (App J Q = 1, self-labelled input), counter-moving layers ABSENT, insulating contacts ABSENT, grip term ABSENT (shell term is U(2)-symmetric). 0/4 derived. [verified against App J, App JH FINAL, Letter 36 OHC]
- **CN-TWIST-10.** Pendry wire-medium estimate: connected conducting shells at Planck spacing have ω_p ≈ 1.6–1.8 c/a (0.5 c/a even at r = 10⁻¹⁰a) ~ 10⁴³ rad/s ≫ any observed photon (≲ 10³⁰ rad/s): opaque. Insulated conducting spheres instead give a transparent Maxwell–Garnett dielectric (ε_eff ≈ 9.6 at FCC filling). The vacuum's transparency rides on an insulating-contact property the corpus never states. [PROVEN at order of magnitude]
- **CN-TWIST-11.** Hopf number on a ball with free boundary is not protected (B³ contractible); protection needs n pinned on ∂B³. App JH §3.4's "topologically protected" presupposes a compactification no corpus term supplies — the same type-error family as CN-JHF (flux ≠ π₃ charge). [PROVEN, elementary]
- **CN-TWIST-12 (structural, propagates).** ξ/R = 4.635 (= 2ξ/a, CN-JHF) means the condensate cannot vary on the scale of the sphere/shell/void partition at all: "shell", "void" and "interior" are all inside one healing length. Every question in this card that needed the medium to *differ* between those regions (Q2 branch ii, Q3 screening) is blocked by this single number before any dynamics is computed. [PROVEN; consequence of CN-C1-04's asserted ξ]
- **CN-TWIST-13 (protocol).** The run was made on Claude Fable 5.1, not an Opus-class model as §11 specifies; a prior result for this gate exists in `audit/gates/TWIST/` and was not opened — this run is a blind replication of it. Michel to compare.

## 10. What this gate does and does not touch

Does not reopen QED-DERIV (the S¹ theorem stands; this is the modified, ℂ² theory). Does not refute the void geometry (α₀ as a number, r_oct, r_tet, ξ, the percolating void network — §8). It closes the "twist field = light" reading of Michel's sphere-interior picture along the minimal two-component route with geometry-fixed couplings, and prices the alternative: ≥ 5 added inputs, ≥ 3 free numbers, plus either a large coupling (e² ~ 10³) or a new confining mechanism for the pressure. Richer order parameters (CN-OP-14 residue) are out of scope, as §10 of the card says.

## 11. Plain-language summary for Michel 🦜

You asked whether the twisting inside each sphere — the two-component field's built-in "connection" a — could *be* light, and whether the sphere skins could then hold the knot. Four questions, taken in order:

1. **Does the medium give the twist its own light-like energy?** No. In the plain superfluid the twist has no energy of its own — it only ever appears glued to the flow and to the direction field n, and its "magnetic field" is fixed by n. I tried the standard trick of letting the density wobble and integrating that out: it produces a term with the *wrong sign* (−Kξ²/4, a term that makes knots want to shrink, which is exactly what Gate KL suspected and JHF saw as collapse). Letting the phase wobble gives the twist a *mass*, not a kinetic energy — the Meissner effect again. To get real Maxwell light you have to add a charge and a Maxwell term by hand (the Babaev–Faddeev–Niemi route). That's bought, not derived. **Kill at Q1.**
2. **If we buy it, is it massless in the voids?** No. Your medium is the same everywhere (App J says so, and so does your A1), so the light is massive everywhere — mass = e × Planck mass for any charge e. Making the shells superconducting and the voids empty would need a new ingredient the corpus doesn't have, and even then the voids are Planck-sized cavities joined by tiny windows: nothing with a wavelength longer than the Planck length can travel through them.
3. **Can the skins screen and hold the knot?** No. The skin in the corpus is a zero-thickness potential bump — it has no superfluid of its own to screen with, and the bulk screening it would borrow acts inside the sphere just as much as outside (so it would squash the knot's own field). The skin does supply a pressure — a neat exact number, 1/π in condensation-energy units — but a Planck-sized Maxwell knot pushes back about 2,400× harder (at unit coupling).
4. **Does a current-carrying skin follow from the medium?** None of the four needed properties is derived: the charge is asserted (App J's Q = 1), nothing describes two counter-flowing layers, nothing says the 12 contact points are insulating — and if they conduct, the whole lattice is a Planck-scale metal opaque to all light we have ever seen (Pendry's wire-medium argument holds) — and the skin term doesn't grip the direction field, so the Hopf number isn't protected on a ball with a loose edge.

**Verdict: SC-TWIST-1, kill at Q1**, Q2–Q4 failing conditionally — exactly the card's forecast, now with numbers. The good news to name: (i) the direction-field algebra you need (Mermin–Ho, the CP¹ connection) all checks out to 60 digits, so the *language* of the picture is sound; (ii) the shell pressure comes out as an exact 1/π of the condensation energy — a clean identity of your own inputs, not a fit; (iii) the audit is now sharp about the price list: add a charge, a Maxwell term, a confining mechanism for the condensate, and a direction-dependent skin term, and the picture can be written down as a *different* theory. The geometry is untouched.

**One structural number does most of the killing: ξ = 4.6 R.** The condensate can't change across a sphere, so it can't tell "skin" from "void" from "inside". Any future interior picture has to get past that first.

Protocol notes for you: I ran on Fable 5.1, not Opus; and there is already a `gate_TWIST_RESULT.md` plus an unblinded addendum in the repo from a prior run that I did not open — mine is filed beside it as a blind replication, so compare the two.

## 12. Files

```
audit/gates/TWIST/replication_2026-11-09/
  gate_TWIST_RESULT.md                 (this file)
  gate_TWIST_prompt_asrun.md           (byte-exact copy of the card, SHA-256 7863d39d…a3b01f)
  scripts/twist_q1a_identity.py        (identities, 60 dps)
  scripts/twist_q1bc_induced.py        (V0 in (ρ,n,φ,a); density integration; London kernel; c_F)
  scripts/twist_q2_mass.py             (Meissner mass, polarisations, void-network cutoff)
  scripts/twist_q3_shell.py            (Pearl length; virial budget; Hopf-map c₁, c₂)
  scripts/twist_q4_shell_current.py    (Pendry wire medium; Maxwell–Garnett contrast)
  output/*.txt                         (as-run outputs)
  SHA256SUMS                           (digests of every file above)
```

Python 3.13, sympy 1.14.0, mpmath 1.3.0. Runtimes: q1a ≈ 2¼ min, q3 ≈ 4 min, others seconds.
