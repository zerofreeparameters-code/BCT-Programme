# Gate VOID — RESULT

**Do the corpus's void-volume and void-eigenvalue formulas survive the true void geometry?**

Run 17 Oct 2026 (18:51–~20:30 AEDT) by Claude (Fable 5.1), cold thread, memory paused, one gate per thread.
Cold Ledger discipline: nothing beyond the pre-registered verdicts is asserted above CONJECTURE.

| Item | Value |
|---|---|
| Repository commit | `e734f933f20d518823bd6a1e46a83ce8fbd9a498` ("Pre-register Gate VOID") |
| Prompt | `audit/gates/gate_VOID_prompt.md`, fetched by raw URL with curl to disk before reading |
| Prompt SHA-256 | `e04f69db573dc8f1e3f45884508fe4cb7a75abbaf9c4cfc5f333419484b969a0` — `sha256sum -c audit/gates/PREREG_20261017_VOID.sha256`: **OK** (fetched copy byte-identical to the checkout copy) |
| `void_numbers.txt` SHA-256 | `2cefa0a8fa87aad9cc52211bb0ab8148e7eb1ba7e1f0439ed72e24cbbe08aa0c` — hashed 08:14:15 UTC, before any comparison with corpus targets |
| Inputs read | exactly the §6 list: `tex/BCT_Letter127_EWQCDScales_v2.tex`, `BCT_GP_STATE_SAVE.md`, `BCT_Master_State_v35_update.md`, `BCT_L244_ZenodoKit.md`, `BCT_AppAB2_Zenodo_Kit.md`, `BCT_SessionHandover_June2026.md`, `audit/NEXT.md`, `audit/PREREGISTRATION.md`, `audit/gates/RATIO/`. Nothing else from the corpus; the project's attached PDFs were not opened. |
| Tools | sympy 1.14 (exact), mpmath 1.3 at 60 dps, numpy 2.5 / scipy 1.18 (finite differences, `eigsh` shift-invert about σ = 0 with the inverse applied by AMG-preconditioned CG to 10⁻¹² — a direct LU of the N = 96 grids exceeded the sandbox's time budget), pyamg 5.3 |
| Deliverables | `void_geometry.py`, `void_eigen.py`, `void_x.py`, `test_void.py` (19 tests, all pass), `void_numbers.txt` (+ `.sha256`), this file, `CN-VOID-01.md` — all under `audit/gates/VOID/` |

---

## 0. Pre-conditions (§2.1, §2.2) — both PASS, so the gate reports

**§2.1 volume sum.** V_oct + 2 V_tet = 1/√2 − π/6 holds **exactly**. The sympy proof reduces it to the solid-angle identity 8 Ω_t + 6 Ω_o = 4π, i.e. arccos(23/27) = π/2 − 3 arcsin(1/3), which is sin(3α) = 3 sin α − 4 sin³α = 23/27 at sin α = 1/3 with 3α < π/2; both sides agree at 60 dps (0.18350800558824865132…). Monte Carlo, 10⁷ points, seed 17: tet z = −0.48, oct z = −0.10, full-cell interstitial per sphere z = −0.74 — all within 3σ.

**§2.2 ball validation.** Same code, single ball R = ½ in the cell: λ_h = 38.1384, 38.4079, 38.8198 at N = 48, 64, 96; extrapolated 39.6435 vs 4π² = 39.4784 → **0.42 %** (< 1 %). The three-point fitted order fell outside [0.5, 3] (staircase noise), so the pre-coded fallback — two-point, p = 1, finest pair — was used; the same rule is applied to every domain below.

---

## 1. Geometry: ball / polyhedron / true chamber (Q1)

Units: sphere diameter = 1 (sphere radius ½, NN distance 1). Exact forms in `void_numbers.txt` to 50 digits.

| Quantity | Inscribed ball (corpus) | Polyhedron of centres | True chamber | chamber / ball |
|---|---|---|---|---|
| r (tet) | r_tet = √6/4 − ½ = 0.112372 | — | — | — |
| r (oct) | r_oct = 1/√2 − ½ = 0.207107 | — | — | — |
| **V_tet** | 4πr³/3 = 0.0059439 | √2/12 = 0.117851 | √2/12 − arccos(23/27)/6 = **0.0259702** | **4.3693** |
| **V_oct** | 4πr³/3 = 0.0372110 | √2/3 = 0.471405 | √2/3 − arcsin(1/3) = **0.1315676** | **3.5357** |
| V_oct + 2V_tet (per sphere) | 0.049099 | 0.707107 | 1/√2 − π/6 = **0.1835080** (exact interstitial volume) | 3.737 |
| wall area, tet | 4πr² = 0.158683 | √3 = 1.732051 | arccos(23/27) = **0.551286** | 3.4741 |
| wall area, oct | 4πr² = 0.539012 | 2√3 = 3.464102 | 6 arcsin(1/3) = **2.039021** | 3.7829 |
| window (per face) | — | √3/4 = 0.433013 | √3/4 − π/8 = **0.040314** | — |
| interstitial fraction | — | — | 1 − π/(3√2) = **0.259520** | — |

The inscribed balls account for 27 % of the interstitial volume; the rest lies in the cusps and the windows. Each tetrahedral chamber opens through four windows (one per face) and each octahedral chamber through eight; the window area is 9.3 % of the polyhedron face.

---

## 2. Eigenvalues (Q2)

Finite-difference −∇² on the periodic cell, Dirichlet at every grid point inside a sphere, h = √2/N. Chambers: same operator restricted to one chamber with Neumann (dropped-neighbour) conditions on its window planes. Residuals ‖Lv − λv‖/‖v‖ ≤ 1.1×10⁻⁹ in every case.

| Domain | N = 48 | N = 64 | N = 96 | extrapolated (gate value) | ball μ₀ = π²/R² | true / ball |
|---|---|---|---|---|---|---|
| validation ball R = ½ | 38.1384 | 38.4079 | 38.8198 | 39.644 | 39.478 (4π²) | 1.0042 |
| (a) full periodic network | 129.713 | 142.307 | 143.583 | **146.13** | 230.097 (oct ball) | **0.635** |
| (b) oct chamber, Neumann windows | 129.957 | 142.275 | 143.596 | **146.24** | 230.097 | **0.636** |
| (b) tet chamber, Neumann windows | 373.335 | 382.564 | 400.035 | **434.98** | 781.592 | **0.557** |

Reading. The network ground state lives in the octahedral chambers: the oct-chamber Neumann-window value and the network value coincide to 0.07 %, and the tet value is three times higher, so the tetrahedral chambers are, for the ground mode, dead ends. The consistency bound min(λ_oct^N, λ_tet^N) ≤ λ_network holds at every grid.

Supplementary (outside the pre-registered grids; not a gate value): oct chamber N = 128 → 148.19, N = 192 → 149.82; network N = 128 → 148.22; tet N = 128 → 413.70, N = 192 → 421.61. The raw values converge from below and the two-point p = 1 extrapolation from the N = 128/192 pair gives ≈153 (oct) and ≈437 (tet), so the gate's oct/network value 146 is probably 3–6 % low and the tet value is good to ~2 %. None of the conclusions below depends on this: the shifts are factors of 1.6–2.4, not percent.

---

## 3. Letter 127 re-evaluated (Q3)

Held exactly as the corpus states: S_EW = π⁵/12, S_QCD = π⁵/24, α₀ = r_oct r_tet/π, NLO = α₀(4π+1)/π², the factor 2, and the NNLO factor 1 − NLO(1 − 8α₀)/4. Only μ and V are substituted. Targets (read after hashing): App AY back-solved x_EW = 0.33934 (`BCT_GP_STATE_SAVE.md`) and 0.33663 (Letter 127 v2); x_SU3 = 0.71959.

| Evaluation | x_EW | vs 0.33934 | x_SU3 (NLO) | x_SU3 (NNLO) | vs 0.71959 | v = m_P e^{−S_EW/(1−x_EW)} | Λ_QCD = m_P e^{−S_QCD/(1−x_SU3)} |
|---|---|---|---|---|---|---|---|
| (i) corpus: ball μ₀, ball V | **0.339168** | −0.051 % ✓ reproduces 0.33917 | **0.721265** ✓ (0.72127) | **0.719538** ✓ (0.71954) | +0.233 % / −0.007 % | 212.4 GeV (= Letter 127's v₀) | 219.83 MeV (= Pred #168) |
| (ii) true V, ball μ₀ | 1.19920 | +253 % | 3.15139 | 3.14384 | +337 % | undefined (x > 1) | undefined (x > 1) |
| (iii) true V, true per-chamber μ | 0.76214 | +125 % | 1.75383 | 1.74963 | +143 % | 3×10⁻²⁸ GeV | undefined (x > 1) |
| for the record: Letter 127 v2 boxed x_EW = ⅓ + πα₀/7 (not a void integral) | 0.336658 | +0.75 % (−0.008 % vs 0.33663) | — | — | — | 245.80 GeV (= Pred #169) | — |

Neither x survives in either corrected evaluation. Under (ii) the volume correction alone multiplies x by 3.54 (EW) and 4.37 (QCD); under (iii) the lower eigenvalue pulls both back by 0.64 and 0.56, leaving net factors of **2.25** and **2.43**. The claimed matches (0.052 % and 0.233 %/0.007 %) are properties of the inscribed-ball shorthand, not of the void. In case (iii) x_SU(3) > 1, so the hierarchy formula has no value at all for Λ_QCD; x_EW = 0.76 sends v to 10⁻²⁸ GeV. No NLO factor, coefficient or scale was adjusted (rule 2.3); any adjustment that restored the match would be a new posit and none is proposed (rule 2.5).

Note on the Letter's own inconsistency: Letter 127 v2's abstract gives the GP form x_EW = (4π³r_oct/3S_EW)(1+NLO) while its boxed Eq. (xEW) gives ⅓ + πα₀/7 = 0.33666 and calls the GP value 0.33575 only "close to ⅓". Prediction #169 (v = 245.80 GeV) as printed in the boxed equation and in Master State v35 therefore does **not** use the void integral; only its abstract-level form and `BCT_GP_STATE_SAVE.md`'s x_EW = 0.33917 do. Prediction #168 (Λ_QCD) uses it throughout.

---

## 4. p_void (Q4)

**Definition, verbatim from the permitted files.** `BCT_L244_ZenodoKit.md`: "the BCT void fraction p_void = tanh²(1/√2) + r_tet²·r_oct/π² = 0.370974707015939…"; "The BPS kink evaluated at x = r_oct gives tanh(r_oct/ξ) = tanh(1/√2) … The floor p_floor = tanh²(1/√2) = 0.370709726… follows from geometry alone"; "The NLO correction is identified as the cross term δp = 2α₀·Ψ_A·Ψ_B between two independently saturated condensates". `BCT_AppAB2_Zenodo_Kit.md`: "APPENDIX AU — THE VOID FRACTION LOCK … p_void = tanh²(1/√2) + r_tet²·r_oct/π² = 0.370974707015939… Status: LOCKED". `BCT_SessionHandover_June2026.md`: "p_void = 0.370974707015939 (Python-verified)" in the locked-constants list, with no definition.

**What it is a fraction of.** By its own construction p_void is the squared BPS kink amplitude of the condensate at the oct-void radius, tanh²(r_oct/ξ) with ξ = √2 r_oct, plus an O(α₀) cross term between two condensate amplitudes — a condensate-density (superfluid-fraction-type) quantity, not a volume fraction of anything.

**Comparison with the geometric fraction.** In the three permitted files the geometric interstitial fraction 1 − π/(3√2) = 0.25952 is never cited beside p_void, and p_void is never compared with any volume fraction (p_void/0.25952 = 1.4295 would be the comparison, and it is not made). The name "void fraction" is the only point of contact.

**Arithmetic.** tanh²(1/√2) + r_tet² r_oct/π² = 0.3709747070159393351875407849212764086918 (40 digits); tanh²(1/√2) = 0.3707097263651463325…; r_tet² r_oct/π² = 2.649806507930026747×10⁻⁴. The printed 0.370974707015939… is confirmed.

**Zenodo.** Letters 243, 244 and App AU are not in the repository. The public Zenodo records under ORCID 0009-0007-9561-9859 were **not retrieved**: `zenodo.org` is refused by this run's egress allowlist and the in-app fetch permission lapsed before it was answered; two web searches did not surface the records. Recorded as "not found (not reachable)". The Q4 finding therefore rests on the three kit/handover files, which paraphrase the Letters. Confidence: low, as forecast.

---

## 5. Ledger cross-reference

From `audit/NEXT.md` (14 Sep 2026) and `audit/gates/RATIO/gate_RATIO_deliverable.md`:

- **CN-RATIO-06 [ASSERTED]** — "retire or reclassify the individual-radius citations (α₂ = r_oct²/π → v_BCT, **x_EW ∝ r_oct, x_SU(3) ∝ r_tet** [Letter 127], cos θ_K = r_oct − ½, ξ/r_oct = 11.19)… resolve alongside the PRED2 §5 'retire from public citation' list". The RATIO deliverable names the formulas explicitly: "x_EW = (4π³ r_oct/3S_EW)(1+NLO) and x_SU(3) = (8π³ r_tet/3S_QCD)(…) (Letter127)" — these are exactly the μ₀V/S_bare expressions tested here. Every claim that used V_void or μ₀ (Letter 127 §2/AZ10, `BCT_GP_STATE_SAVE.md`, Master State v35 "GP eigenvalue × void volume") is this family.
- **Pred #168 (Λ_QCD = 219.83 MeV)** is the direct output of x_SU(3) and has no other BCT content; it is not named in NEXT.md's PRED2 §5 list (α, G, m_P, Wolfenstein set, m_d/m_u/m_b, m_ρ, r_p, −0.014 % m_e), but its sole input is in CN-RATIO-06. The ledger also records Λ_QCD = 220 MeV as an *input* elsewhere (INV-0120; RATIO: "the corpus ties Λ_QCD = 220 MeV to the same anchor"). **Recommendation (not a verdict):** when CN-RATIO-06 is executed, name Pred #168 and Letter 127's abstract-level x_EW in it explicitly, so the retirement reaches the printed prediction and not only the formula.
- **Pred #169 (v = 245.80 GeV)** rests on ⅓ + πα₀/7, which this gate does not touch (it is a different posit in the same N-class family, per RATIO).
- **Gate GEO:** NEXT.md has no entry under that name; the r_oct, r_tet confirmation the card refers to is in the RATIO entry ("r_oct = (√2−1)R and r_tet = (√(3/2)−1)R … verified to 15 digits"). Taken as stated. This gate confirms the same radii exactly (r_tet = √6/4 − ½, r_oct = 1/√2 − ½) and does not change them.
- `audit/PREREGISTRATION.md` contains no VOID, Letter 127, x_EW, x_SU3, Λ_QCD or v entry.

---

## 6. Verdict

**SC-VOID-1 (no standing claim moves).** The geometry checks pass; the shifts are reported (§3); every claim that used V_void or μ₀ — Letter 127's x_EW and x_SU(3) in all their printed forms, and `BCT_GP_STATE_SAVE.md`/Master State v35's restatements — is in the CN-RATIO-06 [ASSERTED] retirement family. The correction changes the archive, not the ledger's standing claims. **CN-VOID-01 is filed** (`audit/gates/VOID/CN-VOID-01.md`, for `audit/`).

SC-VOID-2 is not triggered on the reading that Pred #168 is covered by CN-RATIO-06 through its only input. If the ledger keeper reads "in a retirement list" as requiring the prediction to be named, then SC-VOID-2 fires for Pred #168 alone (x_SU(3) moves by +143 % against a stated 0.007 % error) and its tier drops to CONJECTURE pending a repair gate; §5 recommends naming it either way. **SC-VOID-3 is not triggered**: in the permitted inputs p_void is not presented as, or compared with, the geometric void fraction — with the stated caveat that Letters 243–244 and App AU themselves were not retrieved. SC-VOID-0 did not fire.

---

## 7. What this does not show

- It does not test whether a condensate exists in the voids, reopen 1/137, change r_oct or r_tet, or model the GP nonlinearity (card §5). Eigenvalues are linear Dirichlet values.
- The per-chamber eigenvalues are defined by the card's symmetric-partition convention (Neumann on the window planes). The {111} window planes are not mirror planes of FCC, so this is a bounding construction, not the exact chamber mode; for the oct chamber it coincides with the network value anyway.
- The finite-difference boundary is a staircase (first order). The pre-registered three grids give the oct/network value to perhaps ±5 % and the tet value to ±2 % (§2 supplementary). The ball validation at 0.42 % is a check of the code, not of the chamber accuracy, because the chambers have fewer grid points across them (r_oct ≈ 14h, r_tet ≈ 7.6h at N = 96).
- It does not say what x "should" be. Evaluation (iii) multiplies an eigenvalue by a volume as the corpus does; whether μ·V is the right functional of a non-spherical connected region is not addressed (rule 2.5).
- The p_void item was checked against three secondary files, not the Letters. If Letter 243/244 or App AU compares p_void with 0.2595, SC-VOID-3 would need to be re-examined with those records in hand.
- Zenodo access was unavailable; no claim is made about what the public records contain.

---

## 8. Forecast, scored

| Forecast item (card §4) | Outcome | Score |
|---|---|---|
| True chamber volumes ×4.4 (tet), ×3.5 (oct) | 4.369, 3.536 | hit |
| Network eigenvalue well below 230; guess 40–90 | 146 (below 230; the guess 40–90 was too low by a factor ~1.6–2) | half: direction right, range missed |
| Per-chamber values between network and ball values | oct 146.2 ≈ network 146.1 (not between; equal within noise); tet 435 lies between network 146 and its ball 782 | half |
| (ii) x_EW ≈ 1.2, ×3.5; x_SU3 ×4.4 | 1.199, ×3.54; ×4.37 | hit |
| (iii) within a factor of 2 of corpus, outside 0.052 % | factors 2.25 (EW) and 2.43 (QCD); outside the match | near miss (factor >2) |
| Verdict SC-VOID-1 | SC-VOID-1 | hit |
| p_void a condensate posit, no comparison with 0.2595, SC-VOID-3 not triggered; low confidence | as forecast, on the permitted files | hit (low-confidence item) |

---

## 9. Independent recomputation

A separate agent with no access to this gate's working files recomputed the chamber volumes, the three x evaluations and the extrapolated eigenvalues from the card's conventions. Its report:

Script and full report: `audit/gates/VOID/independent_check/check.py`, `report.txt`. Agreement with this gate's values:

| Quantity | gate | independent | agreement |
|---|---|---|---|
| V_tet, V_oct, wall areas, r, V_ball, μ_ball, ratios | §1 | identical closed forms; 30 digits | exact |
| V_oct + 2V_tet = 1/√2 − π/6 | proven via sin 3α = 23/27 | proven via cos 3β = −23/27 (β = arccos ⅓), residual 2×10⁻⁶² | exact, different route |
| Monte Carlo (2×10⁶ pts, own seed) | — | tet z = +1.52, oct z = −0.28 | within 3σ |
| ball validation extrapolated | 39.6435 (0.418 %) | 39.6435 (0.418 %) | 10 digits |
| network extrapolated | 146.1349 | 146.1347 | 2×10⁻⁶ |
| oct chamber extrapolated | 146.2365 | 146.1159 | 0.08 % — the checker counts 5387 / 12399 / 41901 chamber unknowns against this gate's 5369 / 12399 / 41883, i.e. a different tie-break for grid points lying exactly on the window planes; the difference is below the method's resolution |
| tet chamber extrapolated | 434.9772 | 434.9772 | 10 digits |
| x_EW (i) / (ii) / (iii) | 0.33917 / 1.19920 / 0.76214 | 0.33917 / 1.19920 / 0.76151 | (iii) differs by 0.08 %, from the oct value above |
| x_SU3 NNLO (i) / (ii) / (iii) | 0.71954 / 3.14384 / 1.74963 | identical to 10 digits | exact |

No number in §§1–3 moves at the precision the verdict uses.

---

## 10. Reproduction

```
cd audit/gates/VOID
python3 -I void_geometry.py                     # §2.1 exact + Monte Carlo (≈12 s)
PYTHONPATH=. python3 void_eigen.py              # §2.2 validation, network, oct, tet (≈75 s, 2 cores)
python3 -I void_x.py 146.236549832 434.977196795   # §2.3, §2.4
PYTHONPATH=. python3 -m unittest -v test_void   # 19 tests (≈3 s)
sha256sum -c void_numbers.sha256
```
