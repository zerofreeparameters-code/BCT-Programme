# Gate TWIST — RESULT

**Programme:** BCT Superfluid Lattice Model, Cold Ledger
**Run:** 8 November 2026 (Australia/Melbourne), Claude Opus 5.5, attached to the BCT project
**Card:** `audit/gates/gate_TWIST_prompt.md`, pinned at commit `c3e7cde80e3c0ef55057256d98009fd019f95c26`
**Tier cap:** same-session run → every finding below is capped at **CONJECTURE** until it is independently re-run.

---

## 0. Hash check (done before the card was opened)

| | Pre-registered | Measured | |
|---|---|---|---|
| SHA-256 | `7863d39d83dd607aafa46e85a44dccdcff39ae31beea1504473a3aaf19a3b01f` | `7863d39d83dd607aafa46e85a44dccdcff39ae31beea1504473a3aaf19a3b01f` | match |
| Size | 11055 bytes | 11055 bytes | match |

Fetched with `curl -sL -o gate_TWIST_prompt.md <raw URL at the pinned commit>` into an empty directory, hashed with `sha256sum`, sized with `stat`, and both values reported to Michel before the file was read. The repository clone at the same commit also holds `audit/gates/gate_TWIST_prompt.md`.

---

## 1. Contamination statement

**Settings step (§3).** I cannot switch the "Search and reference past chats" or "Generate memory from chats" settings from inside a session. In this session memory is reported as not enabled, and no past-chat search tool or project-memory tool was available or used. **After-run step closed:** at 12:33 Michel reported switching memory back on after the run. The past-chat tools became available in this session only at that point. That fits with them being off throughout the run.

**Blocked items (§3): none opened.**
- `BCT_SessionRecord_2026-11-08.pdf`, `DESK_hopfion_in_sphere_RESULT.md`, `partA_neutral.py`, `partB_spheromak.py`, `rings.py`, `rings2.py` and `areas/hopfion-interior-idea.md` were not opened.
- A filename-only scan (`git ls-files | grep`) showed none of them in the repo at the pinned commit. None appears by name in the project's doc list.
- No project memory was read.
- `project_search` was deliberately **not** used, because knowledge-base search can return snippets from any doc.
- A Google Drive search for the closed-gate results was run on titles only, with content snippets switched off.

**Mid-run exposure (disclosed, minor).** At 12:03 local time, after Q1 had been computed and before Q2–Q4 were scored, Michel sent a one-line message about the blocked 8 Nov chat: *"there was talk of requiring EM and the way the spheres would align along a particular axis."* It contained no results. Q2–Q4 were scored without reference to it. Its subject is answered only in the clearly separated post-blind section §9. **Flag:** minor exposure. I am not claiming the run is clean on this point, and the call is Michel's.

A second message at 12:13 ("requiring EM; spheres aligning along a particular axis — recompute 1 pls") arrived after §§3–8 had been written and checked; the scripts had been re-run and their outputs were byte-identical. It is answered in §9 as a post-blind recompute, with its own script and notices (CN-TWIST-24…28). It does not alter the blind scores.

**Read (permitted).**
- `tex/BCT_Appendix_J_SphereAction.tex` (App J).
- `tex/BCT_Appendix_JH_FINAL.tex` (App JH; byte-identical to `BCT_Appendix_JH (1).tex`).
- `tex/BCT_Letter36_OHC_tex.tex` (Letter 36).
- `audit/gates/PROMOTE/gate_PROMOTE_result.md` in full.
- `audit/gates/LINK/gate_LINK_RESULT.md`: header, verdict and the CN table, via grep.
- `audit/gates/C1/gate_C1_RESULT.md`: grep for the verdict, the CN table and the ξ convention, l. 255–260.
- Literature, through search results only: Babaev–Faddeev–Niemi (arXiv listing and PDF snippet), Pendry et al. 1996, Motrunich–Vishwanath 2004, LHAASO photon energies.

**Read (not on the permitted list, not blocked — disclosed).** `audit/MINIMAL_BCT.md`. It carries a one-line closed-gate summary: "ξ > a … Closes: … the hopfion" (from Gate C1). I read it before computing Q3-C, so Q3-C is not independent of that prior.

**Anchoring.** The card's §9 forecast is part of the card and was read with it. Agreement with the forecast (§8) is therefore not independent confirmation.

**Closed gates not locatable.** No results file for QED-DERIV, KL, BC, STIFF or ICE was found in the repo at the pinned commit, in the project docs, or by Drive title search. For those gates only the card's own one-line characterisations were used (CN-TWIST-21).

---

## 2. Conventions declared (the card fixes the model; these only fix notation)

- Lengths are in units of the nearest-neighbour distance a = ℓ_P.
  - R = a/2, r_oct = 0.207107 a, r_tet = 0.112372 a.
  - α₀ = r_oct·r_tet/π = 0.00740806.
  - ξ = a/√(8πα₀) = **2.31754 a**, used as given (CN-C1-04).
- The healing length enters V0 as **ξ² = ħ²/(2m g n₀)**. This is the corpus's App AZ6 form, quoted in Gate C1 RESULT l. 255–260, and App J eq. (1) has the same dimensionless form. Every Q2 conclusion was re-checked with ξ² → ξ²/2.
- **K_s ≡ (ħ²/2m)n₀** is the stiffness. **u_c = g n₀²/2 = K_s/(2ξ²)** is the condensation energy density.
- Ψ = √ρ χ and χ = e^{iφ}ζ.
  - a = −iχ†∇χ = ∇φ + a_ζ.
  - The gauge-invariant objects are the superflow combination v = ∇φ + a_ζ and f = ∇×a.
- Shell term (card): (α₀ħ²/2mR)∮|Ψ|² dA. This is repulsive, with jump [∂_rΨ] = (α₀/R)Ψ.

---

## 3. Q1 — Does the twist field get its own Maxwell-type energy from the medium? → **FAIL**

**(a) Identity.**
- |∇χ|² = ¼|∇n|² + a² was checked on 5 random smooth ℂ² fields × 2000 points, using exact symbolic derivatives.
- **Worst relative residual 9.1×10⁻¹⁶** against the threshold 1×10⁻¹⁰.
- Re(χ†∂χ) ≤ 1.7×10⁻¹⁴ everywhere.
- The full decomposition |∇Ψ|² = (∇√ρ)² + ρ[¼|∇n|² + (∇φ + a_ζ)²] holds to 1.2×10⁻¹⁴ (CN-TWIST-01).

**Mermin–Ho with its exact coefficient.**
- f_ij ≡ ∂_i a_j − ∂_j a_i = ½ n·(∂_i n × ∂_j n). In vector form, (∇×a)_k = ¼ ε_kij n·(∂_i n × ∂_j n). Both hold to 2.6×10⁻¹⁵.
- The card's "∇×a = ½ n·(∂n×∂n)" is shorthand for the 2-form statement.
- Normalisation check: H = (1/4π²)∫a·(∇×a) = **1.00000000** on the standard Hopf map. This is consistent with App JH's (1/16π²)∫A∧dA, because the pulled-back area form is A = 2a (CN-TWIST-02).

**(b) Slaved or independent?** Slaved.
- V0 depends on a only through v = ∇φ + a, and ∇×a is fixed identically by n through the Mermin–Ho identity.
- The field content is (ρ, φ, n) = 4 real numbers = ℂ². a adds no variable.
- The Bogoliubov spectrum of V0 for ℂ² has exactly two branches per k:
  - the phonon, ω = √(ε_k(ε_k + 2gn₀));
  - a quadratic magnon, ω = ε_k.
- The 126 numerical modes match the analytic forms to 5.8×10⁻¹¹. There is no third branch and no linear transverse doublet (CN-TWIST-03).

**(c) Is c_F (∇×a)², with c_F > 0, generated?** No. The induced coefficient is zero or negative at every level checked.
- **Tree level:** no (∇×a)² term exists in V0, so c_F(tree) = 0 exactly (CN-TWIST-04).
- **Density integrated out (saddle point).**
  - The exact local elimination is min_s[W̃s² + ½(s²−1)²] = W̃ − W̃²/2 for W̃ < 1, and ½ for W̃ ≥ 1, where W = ¼|∇n|² + v². It is verified to 10⁻¹⁶.
  - The induced quartic is **−(ξ²/2)K_s W²**.
  - The gradient kernel C(q) = 2s₀²/(q²ξ² + 2s₀²) was verified by an exact 1-D solve at five values of q.
  - Projected with ((∂n)²)² = F_ijF_ij + (∂_i n·∂_j n)² and F_ijF_ij = 8|∇×a|² (both verified to ~10⁻¹⁵), this gives:
    **c_F = −(ξ²/4)K_s = −1.343 a²K_s**, with every other quartic piece ≤ 0 (CN-TWIST-05).
  - Sign: **negative.** Scaling: c_F ∝ −K_s ξ² = −K_s a²/(8πα₀).
  - This independently reproduces the card's summary of Gate KL: the GP reduction gives a destabilising quartic.
- **One loop (Gaussian amplitude fluctuations).**
  - The W̃² coefficient is −t·I₂, with I₂ = 1/(8√2π) = 0.0281349 (checked numerically) and t = T/(g n₀² ξ³). The tree value is −½.
  - It has the same sign as the tree term.
  - **All orders:** W enters the density sector linearly, so E₀[W] is a minimum of affine functionals and therefore concave. Integrating out density fluctuations cannot produce a positive W² at any order (CN-TWIST-06).
- **Consequence (Derrick):** with c₂ = ∫¼|∇n|² = 8π² and c₄ = ∫(¼|∇n|²)² = 8π² for the standard map, E(L)/(K_sξ) = 8π²(L/ξ − ½ξ/L). This decreases monotonically as L → 0, so the induced term speeds collapse rather than stopping it (CN-TWIST-07).

**Score: FAIL.** c_F > 0 is not fixed by corpus quantities, and a carries no independent propagating degrees of freedom. Neither PASS condition is met.

**BOUGHT variant (BFN).** Babaev–Faddeev–Niemi obtain the stabilising (n·∂n×∂n)² term with a coefficient ∝ 1/e². It comes from the electromagnetic field of a **charged** two-condensate system, and the vector field gains a Meissner–Higgs mass (CN-TWIST-22). Buying it costs rows 2–3 of the cost table. Even then a stays slaved: the propagating vector is the bought field, and it is massive. Q2–Q4 below are answered conditionally on this purchase.

---

## 4. Q2 — Massless, two transverse polarisations, in the voids? → **FAIL** (conditional on Q1 BOUGHT)

**Uniformly condensed medium, with −(1/4e²)f² granted** (e counted; a promoted to an independent connection minimally coupled to the overall phase).
- The static kernel in (φ, a) has one zero mode (the gauge direction). Its two transverse eigenvalues are K_s(1 + k²λ²), numerically confirmed for λ = 0.1, 1, 10.
- Screening mass m_a² = 2e²K_s, i.e. λ_L = (2e²K_s)^{−1/2}.
- With the time-dependent terms granted, the transverse modes disperse as ω² = c_a²(k² + λ_L⁻²), and the longitudinal mode is the gapped plasmon.
- Result: **3 massive polarisations, 0 massless** (Anderson–Higgs/Meissner). The only massless limit is e → 0, where a decouples from the medium (CN-TWIST-08).

**Does the model supply "condensed in the shells, not in the voids"?** No.
- V0 plus the card's shell term was solved on the FCC lattice in two ways: linear response with exact δ-shells (reciprocal-lattice sum, |hkl| ≤ 60), and a full nonlinear solve on a 112³ grid (smoothed shell, w = 0.025a, residual < 10⁻¹¹).
- The density is uniform to **0.56 %** (global max − min over mean).
- The voids are slightly *more* condensed than the shells: ρ_oct-centre − ρ_shell = **+0.0006 n₀**.
- The repulsive shell lattice depletes the condensate uniformly, to ⟨ρ⟩ = 0.646 n₀.
- The four variants give the same picture:

| Variant | Contrast | Void − shell |
|---|---|---|
| card term | 0.56 % | +0.0006 |
| App J sign (attractive) | 0.56 % | −0.0012 |
| App JH BC strength α₀ | 0.28 % | +0.0004 |
| ξ²→ξ²/2 | 0.56 % | +0.0007 |

  (CN-TWIST-09, -12)
- Structural reason: ξ/r_oct = 11.2 and ξ/r_tet = 20.6. Emptying a void costs gradient energy ~250× (octahedral) and ~850× (tetrahedral) the condensation energy it would release. The model has no length short enough to shape the voids (CN-TWIST-10).
- **Polarisation count in the voids: 0 massless transverse.**

**Score: FAIL.** The medium is the same everywhere (App J: same GP action inside and out), so a uniformly condensed medium gives a massive a, exactly as the card anticipates.

Side finding: App J §J.3.1 uses |Ψ(R)|/Ψ₀ = tanh(r_oct/ξ) = 0.089. Solving App J's own functional gives 0.80 (card term), 0.91 (JH strength) or 1.16 (App J sign). The tanh value is not a solution (CN-TWIST-11).

---

## 5. Q3 — Is the field screened in the shells, so they can hold the knot? → **FAIL** (conditional; Q2 failed)

**Penetration depth.**
- In V0, a has no dynamics of its own (Q1), so λ_shell is undefined.
- With the purchase, λ ∝ ρ^{−1/2} and the density is uniform to 0.6 %. So **λ_shell = λ_void = λ_interior to ≈0.3 %**. The shell has no screening of its own; it screens exactly as much as the interior where the knot's field is supposed to live.
- λ's value is set entirely by the bought e.
- Comparison: corpus shell thickness d = 0 (δ-shell), or App J's input d = √(r_oct r_tet) = 0.153a. The shell's density-profile width is ξ/√2 = 1.64a, larger than R = 0.5a.

**Virial check.**
- The lowest force-free state in a ball with B·n = 0 (spheromak, kR = 4.493409) was built and checked: div B ≤ 10⁻¹³, B·n at the wall ≤ 10⁻¹⁵, curl B = kB to 4×10⁻⁵.
- Mean wall pressure / (ū/3) = **1.00000000**, and the Arnold bound W = (k/2)K is saturated (CN-TWIST-13). The card's ū/3 statement is confirmed.

**Can the shell supply ū/3?**
- **Corpus shell term:** no. It is a U(2)-symmetric scalar density penalty and exerts no force on a, so it supplies zero pressure.
- **Bought route, Hopf-1:** wall P/u_c = **606.6 (λ_L/R)²**. A wall made of the same condensate holds at most about u_c (the critical-field limit). That requires λ_L ≤ 0.041R (κ = λ_L/ξ ≤ 0.009, extreme type I), which can only be reached by **choosing e**, and the no-fit clause forbids that. The interior would also have to be normal for the field to sit there, and Q2 shows the model supplies no such phase (CN-TWIST-14).
- **V0 alone, wall pinned (grip granted):**
  - A Hopf-1 texture filling the ball (H = 1.000000) carries texture energy density **369 u_c**.
  - The local W̃ = ξ²·¼|∇n|² averages 184 and exceeds the condensate-destruction threshold W̃ = 1 (exact, Q1-F1) in **100 %** of the ball.
  - Unwinding through a normal interior costs at most u_c·V, which is 1/369 of the knot's energy.
  - The knot's natural core size (~ξ) is 4.6 sphere radii. **The hopfion does not fit in the sphere** (CN-TWIST-15).

**Score: FAIL.** Neither the screening nor its strength follows from the model.

---

## 6. Q4 — Does a current-carrying shell follow from the medium? → **FAIL** (0 of 4 DERIVED)

| Item | Score | Basis |
|---|---|---|
| **(i) Real charge** in the shell | **ASSERTED** | App J (abstract, §J.1.3) names a "surface-charge double layer" and obtains σ_s = α₀ from a charge Q = 1 and a thickness d = √(r_tet r_oct), which App J itself labels inputs. V0 is neutral; its only charge is total particle number. This agrees with Gate STIFF as the card summarises it. (CN-TWIST-18) |
| **(ii) Counter-moving layers** | **ABSENT** | No layer velocities or tangential currents appear in App J, JH or Letter 36. The only current condition (JH eq. hopf-matching) demands a net *radial* superfluid flux α₀ρ₀·4πR² out of each sphere. That is a stationary source, which continuity forbids (∮J·n = −dN/dt), and it is not counter-motion. (CN-TWIST-19) |
| **(iii) Insulating contacts** at the 12 touching points | **ABSENT; the wire-medium argument holds** | The corpus never treats sphere–sphere contacts; JH's "Josephson junction" is interior–exterior, across a shell. Pendry's thin-wire cutoff ω_p² = 2πc²/(a² ln(a/r)) at a = ℓ_P gives ω_p = 0.30–1.65 ω_Planck for contact radii 10⁻³⁰a to 0.1a (ω_Planck = 1.85×10⁴³ s⁻¹; rows with r/a ≥ 0.1 lie outside the thin-wire regime and are only indicative). The medium is opaque below ω_p, and every observed photon lies below it: ~3.7 PeV gamma rays (LHAASO) sit at 3×10⁻¹³ ω_P, and 10 MHz cosmic radio at 3×10⁻³⁶ ω_P. Transparency down to 10 MHz would need a Pearl length Λ ≳ 10⁷¹ a, while holding the knot needs Λ ≲ R. The gap is ~72 orders of magnitude, and it closes only with contacts narrower than R·e^{−10⁷¹}, i.e. insulating contacts. The static limit fails too: a connected screening network expels static magnetic fields. (CN-TWIST-17) |
| **(iv) Grip term** | **ABSENT** | The corpus shell term ∝ \|Ψ\|² is U(2)-invariant and cannot pin n. Without pinning, the ball's edge is free: a one-parameter family runs "H" = 1 → 0.994 → 0.909 → 0.500 → 0.091 → 0 continuously, because B³ is contractible. App JH §JH.3.4 says changing H "costs infinite energy". In fact a normal core costs at most u_c·V, which is finite and here tiny, and JH's "interior of a Planck sphere = S³" holds only when the boundary is pinned. (CN-TWIST-16) |

**Score: FAIL** (PASS needs all four DERIVED).

---

## 7. Verdict and cost table

### **VERDICT: SC-TWIST-1 — kill at Q1** (tier: CONJECTURE, same-session cap)

The medium generates no Maxwell-type term for the twist field: c_F is zero at tree level and negative once the density is integrated out (at all orders, by concavity), and a stays slaved to the texture. Answered conditionally on buying charge plus a Maxwell term, the chain fails at every later step:
- **Q2 fails** (Anderson–Higgs: massive everywhere; this would also trip SC-TWIST-2).
- **Q3 fails** (no shell-specific screening; the knot is 369 u_c and does not fit inside ξ).
- **Q4 fails** (0/4 derived).

### Cost table (mandatory)

| # | Input | Free number? | Where needed | Status in this run |
|---|---|---|---|---|
| 1 | A1: ℂ² order parameter | — (structural) | all | declared by the card |
| 2 | Charge: gauge the overall U(1); promote a from composite to an independent connection | — (structural) | Q1 (BFN route), Q2, Q3 | **granted conditionally** |
| 3 | Maxwell coupling e in −(1/4e²)f² | **yes** (e; the propagation speed c_a in its electric term is a further number, noted but not counted separately, per the card's Q2 wording) | Q1 (BFN F² ∝ 1/e²), Q2, Q3 | **granted conditionally** |
| 4 | Location-dependent phase: shells condensed, voids normal | — (structural phase assumption) | Q2, Q3 | needed, not supplied (and contradicted by ξ ≫ r_void) |
| 5 | A second, short length ξ′ ≲ r_tet to make #4 possible | **yes** | Q2, Q3 | needed |
| 6 | Shell screening strength λ_L ≤ 0.041R (κ ≤ 0.009) | constraint on #3 (a fit of e) | Q3 | needed, and forbidden by the no-fit clause |
| 7 | Real shell charge Q and thickness d (App J: Q = 1, d = √(r_oct r_tet)) | **yes** (2) | Q4(i) | asserted in the corpus as inputs |
| 8 | Counter-moving layer currents (velocity profile) | structural + **yes** (≥1) | Q4(ii) | needed |
| 9 | Insulating contacts at the 12 touching points per sphere | — (structural) | Q4(iii) | needed |
| 10 | Grip term γ∮(1 − n·n₀) and its pinned pattern n₀ on each shell | structural + **yes** (γ) | Q4(iv) | needed |

**Total:** 1 declared (A1), 2 granted conditionally (#2, #3), and **8 more identified as needed for a working picture**. Beyond A1 that is **11 counted items: 5 structural assumptions and 6 free numbers** (e, ξ′, Q, d, a layer velocity, γ), plus one forbidden fit (#6).

---

## 8. Analyst's disclosure, scored

| Forecast (card §9) | Outcome | Hit? |
|---|---|---|
| Q1: FAIL for neutral V0; BFN = BOUGHT | FAIL; c_F ≤ 0 at all orders; BFN = BOUGHT | ✔ |
| Q2: FAIL in a uniform medium; passes only with location-dependent condensation, not supplied | FAIL; density uniform to 0.56 %, voids slightly *denser* | ✔ |
| Q3: conditional on Q2; not reachable | FAIL conditionally (computed anyway) | ✔ |
| Q4: (i) ABSENT/ASSERTED; (ii) ABSENT; (iii) ABSENT, wire argument holds; (iv) ABSENT | (i) ASSERTED; (ii) ABSENT; (iii) ABSENT, holds; (iv) ABSENT | ✔ (4/4) |
| Verdict SC-TWIST-1; cost ≥ 3 inputs | SC-TWIST-1; 11 counted items beyond A1 (3 if counted the forecast's way: charge/Maxwell, a location-dependent phase, a grip term) | ✔, and the cost is higher than forecast |

**Not in the forecast:**
1. The sign result holds at all orders (concavity), not just at one loop.
2. The knot cannot fit: texture energy 369 u_c, and the condensate is destroyed throughout the ball.
3. The corpus shell term depletes the shells, the opposite of what is needed.
4. The wire-medium gap is ~72 orders of magnitude.
5. Corpus-internal inconsistencies: App J's BC sign, JH's BC strength, and App J's tanh value is not a solution.

Because the forecast was visible to the run (§1), the 100 % hit rate is not independent evidence.

---

## 9. POST-BLIND — Q1 recomputed with "EM required" and "spheres aligned along an axis" (Michel, 12:13)

Written after §§3–8 were fixed; the blind scores and verdict are unchanged. I have not seen the earlier chat and work only from Michel's one-line description. Script: `twist_q1b_postblind_EM_axis.py`.

**Inputs declared for this recompute (all counted):**
- **EM:** gauge the overall U(1) with an independent field A of charge q (structural), plus a Maxwell term (1/2μ)|∇×A|² (one free number). Together these give a London length λ, with κ_em = 1/(2μq²) = K_sλ².
- **AXIS:** n aligned to a common axis ẑ. This is either a potential D(1 − n_z²) or h(1 − n_z) (one free number), or pinning n = ẑ on every shell, which is the Q4(iv) grip term (γ plus the pattern).

**(a) Identity.** Still exact in gauge-covariant form: |(∇ − iqA)Ψ|² = (∇√ρ)² + ρ[¼|∇n|² + C²], with C = ∇φ + a − qA (residual 2×10⁻¹⁴), and q∇×A = f[n] − ∇×C (residual 4×10⁻¹⁶).

**(b) Independent degrees of freedom.** The twist field is **still slaved**: ∇×a = f[n] identically. The new independent field is A, or equivalently the supercurrent C, and it is London-screened (massive, Q2). So EM supplies an independent vector, but it is the bought field, not the twist field, and it is not massless.

**(c) Is c_F > 0 generated?**
- **Locally, yes.** Eliminating C exactly gives a twist-field kernel κ_em/(1 + k²λ²), verified against direct numerical minimisation to 7×10⁻¹⁶. For textures much larger than λ this is the BFN Faddeev term +K_sλ²|∇×a|².
- **The net local sign depends on the bought coupling.** c_F,net = K_s(λ² − ξ²/4). The Derrick coefficient on the standard map is λ² − ξ²/2, so local stabilisation needs **λ > ξ/√2 = 1.64a = 3.3R**. That is fixed by q and μ, not by the corpus.
- **No stable knot once the supercurrent is allowed to relax.** I scanned the knot size L with the full non-local EM and density kernels, for λ/ξ from 0.1 to 20.
  - E(L) has **no minimum** for any λ.
  - With the density held fixed, so that no negative term enters at all, E(L) → 0 linearly as L → 0. Below λ the field penetrates and the supercurrent cancels the twist cost, so the H = 1 sector has energy infimum 0.
  - This agrees with Speight (J. Geom. Phys. 60, 599 (2010)) and Jäykkä & Speight (PRD 84, 125035 (2011)): BFN knots shrink and disappear once the supercurrent coupling is restored. The scaling test shows there is no global minimiser; other-shaped local minimisers are not excluded by it.
- **Size floor.** A knot whose core keeps its superfluid must have L > ξ√8 = 6.6a = **13 sphere radii**.

**AXIS.**
- A zero-derivative alignment potential adds nothing to c_F. It scales as L³, so it cannot stop collapse; it only caps the knot size from above. It gaps the magnon, still with no photon-like mode.
- Pinning n = ẑ on the shells makes H well-defined per sphere: it buys Q4(iv). It changes nothing in Q1.
- Each pinned knot's twist field integrates to zero over its own sphere (|∫f dV| / ∫|f| dV = 2×10⁻¹⁵). So aligning every knot along one axis produces **no macroscopic twist field** and no long-range mode.
- Aligning the knot axes in real space is a vector order, which means lattice anisotropy (Gate PROMOTE, CN-PROMOTE-02).

**Post-blind Q1 score with EM + AXIS: still FAIL.**
- c_F > 0 is now BOUGHT locally, but its net sign is set by the free coupling.
- The twist field still has no degrees of freedom of its own.
- The bought term does not stabilise a knot once the supercurrent relaxes.
- Any surviving knot is more than 13 sphere radii across.

The downstream Q2 kill (the Higgs mass of A) is untouched, and the verdict SC-TWIST-1 stands. Post-blind extra cost: q (structural), μ (free number), D or γ (free number) plus the alignment pattern (structural). That is 4 items on top of §7, and 2 of them (charge and Maxwell) are already rows 2–3 there.

---

## 10. Notices CN-TWIST

All tiers are capped at **CONJECTURE** (same-session). "Internal grade" says what kind of check backs each one.

| ID | Internal grade | Notice |
|---|---|---|
| CN-TWIST-01 | derivation + numeric | \|∇χ\|² = ¼\|∇n\|² + a² holds to 9.1×10⁻¹⁶ (threshold 10⁻¹⁰); the full (ρ, φ, n, a) decomposition of \|∇Ψ\|² holds to 1.2×10⁻¹⁴. |
| CN-TWIST-02 | derivation + numeric | Exact Mermin–Ho: f_ij = ½ n·(∂_i n×∂_j n), i.e. (∇×a)_k = ¼ε_kij n·(∂_i n×∂_j n); the card's form is shorthand. H = (1/4π²)∫a·∇×a = 1.00000000 on the standard Hopf map, consistent with App JH's normalisation (A = 2a). |
| CN-TWIST-03 | derivation + numeric | a is slaved: V0 sees a only via v = ∇φ + a, and ∇×a ≡ f[n]. The ℂ² Bogoliubov spectrum is phonon + quadratic magnon (126 modes to 6×10⁻¹¹): a has no propagating degrees of freedom. |
| CN-TWIST-04 | derivation | c_F(tree) = 0. |
| CN-TWIST-05 | derivation + numeric | Integrating out the density gives −(ξ²/2)K_sW², hence c_F = −(ξ²/4)K_s = −1.343 a²K_s; every other quartic piece is ≤ 0. Independently reproduces Gate KL's destabilising quartic (as the card states KL). |
| CN-TWIST-06 | derivation + numeric | One loop gives the same sign (−t/(8√2π) against tree −½). Concavity of E₀[W] forbids a positive W² at any order. |
| CN-TWIST-07 | derivation + numeric | Derrick: E(L) ∝ 8π²(L/ξ − ½ξ/L) is monotone, so V0 hopfions collapse. |
| CN-TWIST-08 | derivation + numeric | With a Maxwell term granted: Anderson–Higgs mass m² = 2e²K_s, 3 massive polarisations, 0 massless; the only massless limit is e → 0 (decoupled). |
| CN-TWIST-09 | numeric | FCC + corpus shell term: density uniform to 0.56 %, voids +0.0006 n₀ denser than shells, ⟨ρ⟩ = 0.646 n₀. Robust across 4 variants. |
| CN-TWIST-10 | derivation | ξ/r_oct = 11.2 and ξ/r_tet = 20.6: no void-scale phase is possible (gradient cost 250–850× the condensation energy gained). |
| CN-TWIST-11 | numeric | App J §J.3.1's tanh(r_oct/ξ) = 0.089 is not a solution of App J's own functional (0.80–1.16). |
| CN-TWIST-12 | reading | Shell-term inconsistencies in the corpus: App J's BC sign is attractive, against its own V = +σ_sδ; JH's BC strength α₀ against JH's surface term α₀/R (a factor 2 at R = ℓ_P/2). The card fixes JH's surface term; the conclusions do not depend on the choice. |
| CN-TWIST-13 | numeric | Virial confirmed: spheromak (kR = 4.493409) wall pressure = ū/3 (ratio 1.00000000); the Arnold bound is saturated. |
| CN-TWIST-14 | derivation | Bought route: wall P/u_c = 606.6(λ_L/R)². Holding the knot needs λ_L ≤ 0.041R, which only a chosen e achieves (forbidden). λ_shell = λ_bulk to 0.3 %. |
| CN-TWIST-15 | numeric | V0, wall pinned: a Hopf-1 texture in the sphere has energy density 369 u_c; W̃ > 1 over 100 % of the ball, so the condensate is destroyed; unwinding is ~369× cheaper. The knot does not fit in a sphere of radius R = 0.216ξ. |
| CN-TWIST-16 | numeric + reading | With a free edge the "Hopf number" varies continuously (1 → 0). JH §JH.3.4's "infinite energy" protection claim is false (the cost is ≤ u_c·V). JH's B³ = S³ identification needs a pinned boundary. |
| CN-TWIST-17 | estimate | Wire medium: ω_p ≈ 0.3–1.7 ω_Planck, opaque to all observed light (radio to PeV); transparency would need Λ ≳ 10⁷¹a against Λ ≲ R for screening (a ~72-order gap); static fields are expelled too. The argument holds. |
| CN-TWIST-18 | reading | Q4(i) ASSERTED: the double-layer charge is App J's own declared input (Q = 1, d = √(r_oct r_tet)). |
| CN-TWIST-19 | reading + derivation | Q4(ii) ABSENT. JH's hopf-matching condition requires a net radial outflow from a stationary sphere, which continuity forbids. |
| CN-TWIST-20 | reading | Q4(iii) and Q4(iv) are ABSENT from App J, JH and Letter 36. |
| CN-TWIST-21 | process | The results of QED-DERIV, KL, BC, STIFF and ICE were not locatable in this session; only the card's one-line summaries were used. |
| CN-TWIST-22 | literature | BFN eq. (11): the (n·∂n×∂n)² coefficient is ∝ 1/e² and comes from the EM field, and the vector field is Meissner–Higgs massive. This confirms the BOUGHT classification and that the bought vector is massive. |
| CN-TWIST-23 | literature (not counted) | The only neutral route to an emergent photon from CP¹ is the disordered, hedgehog-suppressed phase (Motrunich–Vishwanath, PRB 70, 075104 (2004), D = 2+1, higher D discussed). It is the opposite of a condensed superfluid, consistent with CN-PROMOTE-04. Out of scope (card §10). |
| CN-TWIST-24 | POST-BLIND, derivation + numeric | With EM: \|(∇−iqA)Ψ\|² = (∇√ρ)² + ρ[¼\|∇n\|² + C²] and q∇×A = f[n] − ∇×C hold exactly. The twist field stays slaved; the independent field is A/C (London-massive). |
| CN-TWIST-25 | POST-BLIND, derivation + numeric | London elimination gives the twist-field kernel κ_em/(1+k²λ²) (to 7×10⁻¹⁶). Net local c_F = K_s(λ² − ξ²/4); local Derrick stability needs λ > ξ/√2 = 3.3R, which is set by the bought coupling. |
| CN-TWIST-26 | POST-BLIND, numeric + literature | Full non-local size scan: no minimum for any λ/ξ ∈ [0.1, 20]; E(L) → 0 as L → 0 even with the density frozen. Inf E = 0 in the H = 1 sector, so there is no globally stable knot. Agrees with Speight (2010) and Jäykkä–Speight (2011). |
| CN-TWIST-27 | POST-BLIND, numeric | Condensate survival in the knot core needs L > ξ√8 = 6.6a = 13R: no superfluid knot fits in a sphere. |
| CN-TWIST-28 | POST-BLIND, derivation + numeric | Axis alignment: a zero-derivative potential adds nothing to c_F and cannot stop collapse; pinning is the grip term; ∫f dV = 0 per sphere (2×10⁻¹⁵), so aligned knots give no macroscopic twist field; spatial alignment is anisotropy. |

---

## 11. Plain-language summary for Michel

Your picture needs two things from the medium. First, the "twist" that every two-component knot carries should behave like real light. Second, the sphere walls should be able to hold the knot in place.

**Light.** The twist field's swirl is always exactly fixed by how the knot is wound. That is a mathematical identity, which I checked to 15 decimal places. So the field has no freedom of its own: it can't wave or travel independently. The medium also doesn't give it the extra stiffness term that would make it light-like. When the density is allowed to adjust, the term that appears has the wrong sign, and I showed it has the wrong sign at every level of approximation, not just the first. You can add the missing piece by hand: make the medium electrically charged and give it a Maxwell term, as Babaev, Faddeev and Niemi did. But the medium is the same superfluid everywhere, so a charged superfluid then expels that field (the Meissner effect). The "light" gets a mass and goes nowhere.

**Voids versus shells.** For light to survive in the gaps between spheres, the gaps would have to be non-superfluid while the shells stay superfluid. I solved the model on the actual FCC lattice. The density is the same everywhere to about half a percent, and the gaps come out marginally *denser* than the shells. The reason is simple: the medium's healing length is 11–21 times larger than the gaps, so it can't tell them apart.

**Holding the knot.** The knot's natural core is about 4.6 times the size of a sphere. Squeezed inside one sphere, the knot's energy density is about 370 times what it would cost to destroy the superfluid there, so the superfluid gives way and the knot unties. The wall can't grip the knot either. Its term in the energy only sees the density, not the direction of the twist. With an unpinned edge, the knot's winding number can slide smoothly from 1 to 0, so nothing protects it. Making the shells conducting doesn't help, because connected conducting shells at Planck spacing would make the vacuum opaque to every kind of light ever observed.

**Your follow-up: EM required, spheres aligned along an axis.** I recomputed Q1 with both as declared inputs (§9). Adding EM does produce the stiffening term, but only for knots much larger than the screening length. Once the supercurrent is allowed to respond, the knot can always lower its energy by shrinking, and no stable size exists for any value of the coupling. This matches what Jäykkä and Speight found for the Babaev–Faddeev–Niemi model. Aligning the spheres along an axis can pin each knot's twist, which is the "grip" from Q4, but it adds no stiffness. Each knot's twist field also adds up to zero over its own sphere, so aligned knots give no large-scale field. A knot that keeps its superfluid core would need to be about 13 sphere radii across.

**Bottom line.** Verdict **SC-TWIST-1**: the construction dies at the first question. A working version needs about 11 extra ingredients beyond the two-component field: 5 structural assumptions and 6 free numbers, none of which the geometry supplies. This is a same-session result, so it stands as CONJECTURE until someone re-runs it independently. It is not evidence for or against the void geometry itself.

---

## 12. Files (committed under `audit/gates/TWIST/`)

| File | SHA-256 |
|---|---|
| `scripts/twist_q1_twistfield.py` | `919497cbc0234004c5b1c91f2ae63124db3718d4807c98a95c58e92f0986591d` |
| `scripts/twist_q2_mass_and_density.py` | `92d617d194aef676966817d4ad3092404b41ab7d30721d46171653fdccd3e720` |
| `scripts/twist_q3q4_shell.py` | `7af5f7f60bf420a937a6eb06acba4b75e88013f50fc46243a3b37c07eb21e937` |
| `output/twist_q1_output.txt` | `139c21bacf34b19e3d23586805a729472a8be63323edf3a4741e559ad53c5e27` |
| `output/twist_q2_output.txt` | `bb488607236be1c5db6ae974b9379719d5daefe08439fe4814737584197fc9c4` |
| `output/twist_q3q4_output.txt` | `ec41b1c65140d0fbd453f0cc538bec2da5a5e00e72f1927019f17b124ee62179` |
| `scripts/twist_q1b_postblind_EM_axis.py` (post-blind) | `bf6848916cca1a6d59ef3deb87a8facee1ce4e3a90c908ecc54c0503b2401004` |
| `output/twist_q1b_postblind_output.txt` (post-blind) | `b8ccbd4d2896192d6d91577e62b6debd1fe605b60300b8b0569a6c502d2c5289` |

Run each script with `python3 -I <script>` (needs numpy, scipy and sympy). Runtimes: Q1 about 2.5 min, Q2 about 16 s, Q3/Q4 about 12 s, post-blind about 1 min.

**What this gate did not do:** richer order parameters (rank-2, ³He-like); non-perturbative CP¹ monopoles and compactness; finite-thickness shells beyond the λ comparison; any comparison with α or 137 (no-fit clause).
