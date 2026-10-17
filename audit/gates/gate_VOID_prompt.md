# Gate VOID — pre-registration

**Do the corpus's void-volume and void-eigenvalue formulas survive the true void geometry?**

Drafted 17 Oct 2026 for M. R. Cabrié by Claude (Fable 5.1), warm thread, at Michel's request after he asked whether the concavity of the interstitial voids had ever been factored in. Status: PRE-REGISTERED, UNRUN. Commit to `audit/gates/gate_VOID_prompt.md`, digest in `audit/gates/PREREG_20261017_VOID.sha256`, run in a fresh thread with memory paused. One gate per thread. Independent of Gate LATT; the two may run concurrently in separate threads.

---

## 0. Background (stated, not a result of this card)

The BCT/FCC interstitial voids are named "octahedral" and "tetrahedral" after the arrangement of the sphere centres around them. The void itself is bounded by the sphere surfaces: every wall is concave as seen from inside the void, the walls meet in cusps at sphere–sphere contact points, and each chamber opens through windows into its neighbours (every octahedral chamber shares a window with eight tetrahedral chambers, every tetrahedral chamber with four octahedral ones). The interstitial space is one connected region.

Where the corpus needed a void volume or a void mode it used neither the polyhedron of the centres nor the true chamber. It used the inscribed ball of radius R (R = r_oct or r_tet): V = (4π/3)R³ and the Dirichlet ground-state eigenvalue of that ball, μ₀ = π²/R². Found by grep on 17 Oct 2026 in `tex/BCT_Letter127_EWQCDScales_v2.tex` (§"The Gross-Pitaevskii Void Integral", x = μ₀·V/S_bare = 4π³R/(3 S_bare)), `BCT_GP_STATE_SAVE.md` (x_EW = μ_oct·V_oct/S_EW·(1+NLO) = 0.33917 against a back-solved 0.33934; x_SU3 = 2μ_tet·V_tet/S_QCD·(1−NLO)), and `BCT_Master_State_v35_update.md` (the QCD row "GP eigenvalue × void volume").

Warm-thread arithmetic on 17 Oct, with touching spheres 1 apart (sphere radius ½): the true tetrahedral chamber (the regular tetrahedron of centres minus four sphere sectors) has volume 0.02597 against the inscribed ball's 0.00594; the true octahedral chamber 0.13157 against 0.03721; one octahedral plus two tetrahedral chambers sum to 0.18351, the FCC interstitial volume per sphere. These numbers are the analyst's forecast, not the gate's result; the run re-derives them cold.

Ledger status of the affected claims, as recorded in `audit/NEXT.md` (Gate RATIO): x_EW ∝ r_oct and x_SU(3) ∝ r_tet (Letter 127) sit in CN-RATIO-06 [ASSERTED], an individual-radius citation family marked for retirement with the PRED2 §5 list, as N-class posits scoring ≈0 bits. This gate does not reopen that; it measures how far the numbers move when the geometry is corrected, so the retirement carries a quantitative reason.

## 1. Questions

1. What are the exact volume and wall area of the true octahedral and tetrahedral chambers of the FCC packing (BCT at c/a = √2), with cusps and windows accounted for, and how do they compare with the inscribed-ball values the corpus used?
2. What is the lowest Dirichlet eigenvalue of the Laplacian on the true interstitial region, (a) on the full periodic network and (b) per chamber with the window planes treated as symmetry planes, and how does each compare with π²/R² for the inscribed ball?
3. Recomputed with the true volume and eigenvalue, by how much do x_EW and x_SU3 of Letter 127 move, and does either still land within its stated match of the back-solved target?
4. What is p_void = 0.370974707016 (App AU, "void fraction lock", Letters 243–244) a fraction *of*? Is it ever compared with the geometric interstitial fraction 1 − π/(3√2) = 0.25952, and if so does that comparison survive?

## 2. Fixed rules

**2.1 Geometry.** FCC, sphere radius ½, nearest-neighbour distance 1, exact arithmetic in sympy for everything expressible in closed form (sector solid angles: regular tetrahedron vertex Ω_t = arccos(23/27), regular octahedron vertex Ω_o = 4 arcsin(1/3)); mpmath at 60 dps for evaluation. Chamber = polyhedron of the surrounding centres minus the sphere sectors inside it; window = the triangular face of that polyhedron minus the three sphere caps crossing it. Wall area of a chamber = Σ over its spheres of R²·Ω_sector. Checks that must pass before anything else is reported: V_oct + 2 V_tet = 1/√2 − π/6 exactly; a Monte Carlo volume estimate (10⁷ points, fixed seed 17) agrees with the exact values to within 3σ.

**2.2 Eigenvalues.** Finite-difference Laplacian on a uniform grid over the conventional cubic cell (edge √2), periodic boundaries, Dirichlet (ψ = 0) at every grid point inside a sphere; lowest eigenvalue by sparse eigensolver (scipy, shift-invert), at three grid spacings h = √2/48, √2/64, √2/96, with Richardson extrapolation and the three values reported. Per-chamber values: same operator restricted to one chamber with Neumann conditions on its window planes (the symmetric partition of the network), same three spacings. Validation that must pass first: the same code on a single ball of radius ½ in a box reproduces π²/R² = 4π² to within 1 % at h = √2/96 after extrapolation.

**2.3 Recomputation.** Letter 127's x is re-evaluated three ways, with everything else in the formula (S_EW, S_QCD, NLO factors, the factor 2 for the two tetrahedral voids) held exactly as the corpus states them: (i) corpus (ball μ₀ and ball V), reproducing 0.33917 and the x_SU3 value; (ii) true chamber V with ball μ₀; (iii) true chamber V with the per-chamber eigenvalue from 2.2. No NLO factor, coefficient or scale may be adjusted to restore the match; any such adjustment is a new posit and is listed as one.

**2.4 p_void.** Read Letters 243 and 244 and App AU as committed. Record the definition of p_void verbatim, every statement that calls it a void fraction, and whether a geometric void fraction is ever cited beside it. Compute tanh²(1/√2) + r_tet²·r_oct/π² to 40 digits and confirm the printed value.

**2.5 No repair.** The gate does not propose a corrected x formula, a new void model or a new coupling. It reports shifts.

## 3. Deliverables

- `void_geometry.py` (sympy + mpmath + Monte Carlo), `void_eigen.py` (finite-difference eigensolver), `void_x.py` (Letter 127 re-evaluation), unit tests.
- `void_numbers.txt`: every quantity in §1, hashed before any comparison with corpus targets.
- `gate_VOID_RESULT.md`: a table of ball / polyhedron / true chamber for volume, wall area and eigenvalue; the three x evaluations with their distance from the back-solved targets; the p_void finding; the ledger cross-reference; a "what this does not show" section; scored forecast.
- Correction notice text CN-VOID-01 for `audit/` stating in one paragraph what the inscribed-ball shorthand hid and which claims used it.

## 4. Verdicts (fixed now)

- **SC-VOID-1 (no standing claim moves).** The geometry checks pass; the shifts in x_EW and x_SU3 are reported; every claim that used V_void or μ₀ is already RETIRED, CONJECTURE or in a retirement list in the ledger, so the correction changes the archive but not the ledger's standing claims. CN-VOID-01 is filed.
- **SC-VOID-2 (a standing claim moves).** The geometry checks pass and some claim not yet retired changes by more than its stated error under (ii) or (iii). The claim is named and its tier is lowered to CONJECTURE pending a repair gate.
- **SC-VOID-3 (p_void misdescribed).** Independent of 1/2: p_void is presented in the corpus as the geometric void fraction, or is compared with it, and the comparison fails. CN-VOID-02 is filed naming the Letters.
- **SC-VOID-0 (halt).** The volume sum check or the ball eigenvalue validation fails. Nothing is reported; the code is fixed and the gate re-registered.

**Forecast, disclosed.** True chamber volumes larger than the ball by ×4.4 (tet) and ×3.5 (oct), matching the warm-thread arithmetic. Network eigenvalue well below π²/r_oct² = 230.0 (the connected region is far larger than any inscribed ball): guess 40–90. Per-chamber values between the network value and the ball value. Under (ii) alone x_EW rises by ×3.5 to about 1.2 and x_SU3 by ×4.4; under (iii) the eigenvalue drop pulls both back down by a comparable factor, so (iii) lands within a factor of 2 of the corpus value but outside its 0.052 % match. Verdict SC-VOID-1, because Letter 127's x values are already in CN-RATIO-06's retirement family. p_void: the formula is a condensate-fraction posit, not a geometric fraction, and the corpus does not compare it with 0.2595, so SC-VOID-3 is not triggered; low confidence on this item.

## 5. What this gate does not do

It does not test whether a condensate exists in the voids (closed by RANK, JHF, PILOT, PROMOTE). It does not reopen the 1/137 route. It does not change r_oct or r_tet, which are inscribed-ball radii and are unaffected by wall shape (Gate GEO). It does not model the Gross–Pitaevskii nonlinearity; eigenvalues are linear Dirichlet values, as in the corpus's own g = 0 limit.

## 6. Pre-registration record

- Prompt: `audit/gates/gate_VOID_prompt.md`; digest: `audit/gates/PREREG_20261017_VOID.sha256`.
- Inputs the run may read: `tex/BCT_Letter127_EWQCDScales_v2.tex`, `BCT_GP_STATE_SAVE.md`, `BCT_Master_State_v35_update.md`, `BCT_L244_ZenodoKit.md`, `BCT_AppAB2_Zenodo_Kit.md`, `BCT_SessionHandover_June2026.md` (for p_void and App AU as described there; Letters 243–244 and App AU are not in the repository, so the run fetches their public Zenodo records under ORCID 0009-0007-9561-9859 if they exist, and records "not found" otherwise), `audit/NEXT.md`, `audit/PREREGISTRATION.md`, `audit/gates/RATIO/`. Gate GEO's result is not in the repository; its r_oct, r_tet confirmation is taken as stated in `audit/NEXT.md`. Nothing else from the corpus.
- Run thread: fresh; memory paused; expected under one hour of compute.
