# GATE PRED — RESULT
## Are the predictions surprising?  Cold Ledger gate, executed 13 September 2026.

**Model that ran this gate: Claude Fable 5.1** (Anthropic; Mythos-class, shares weights with Claude Mythos 5.1).
The handoff message instructed "MODEL: Claude Opus 5 — record this". That is not the model that ran; the running model is Fable 5.1 and is recorded as such. Nothing else in the handoff was altered.

---
## §1 — Digest (pre-registration)

| item | value |
|---|---|
| fetched | `audit/gates/gate_PRED_prompt.md` @ commit `aa709432f55b5424435551ceafea93398776439e` (raw.githubusercontent.com) |
| SHA-256 of fetched file | `7e7675da8dca7219ea2957410d037f59c3b13e76d3a04214fe35f23372ea1eba` (8548 bytes) |
| pre-registered (handoff) | `7e7675da8dca7219ea2957410d037f59c3b13e76d3a04214fe35f23372ea1eba` (8548 bytes) |
| **verdict** | **MATCH.** Hashed before reading. Gate run. |
| corpus tarball | `codeload.github.com/…/tar.gz/aa709432…` → SHA-256 `3729ad1fea39d94a0555c698cef2ad7a3a6c8b7cbc4259dff162400af5546f07` (45,461,432 bytes) — pinned corpus state |

**Handoff defects recorded (did not affect the run):**
1. The literal `curl` line in the handoff named `gate_RANK_prompt.md`; the header and trailing note named PRED. I fetched both and hashed both without reading either. `gate_RANK_prompt.md` → `72865268c30c1a06d9dac94c46a0d958b27a46fcac27b1e8d3a94d05e8e698e4` (8043 B) — no match; not read; deleted.
2. `audit/gates/PREREG_20260913.sha256` **inside the pinned tree** lists `gate_PRED_prompt.md` as `69b7b7ea…477c9`. The file at the same commit hashes to `7e7675da…`. The in-tree prereg file is stale relative to the file it pins. The handoff line, not the in-tree file, was the pre-registration of record for this run.
3. Handoff said Vol 1 Parts 1–2 are "raw text despite .pdf". `file` typed them as real PDFs (v1.7, 425 pp each). Read with pymupdf. Part 3: PDF, 25 pp. Vol 2: zip → 582-page PDF.

---
## §2 — Search-space coverage (reported before any other number)

| gate §0.5 said | found at `aa709432` |
|---|---|
| 134 `.tex`, 26 at root outside `tex/` | **134 `.tex`; 26 at root; 108 in `tex/`** ✓ |
| Vol 1: three PDFs, 240,670 words, 137 appendices | three PDFs, 875 pp, **251,691 words** (pymupdf) |
| Vol 2: zip → 18 MB PDF, 582 pp, 151,710 words, 108 appendices | zip → 18,123,373-byte PDF, **582 pp, 160,381 words** |
| `audit/APPENDIX_INDEX.md` lists 245, flags 82 self-erroring | **file does not exist at this commit.** Vol 1's own index states **457 technical appendices** (D0–LN7 + supplementary); PRL Letter says 473. Candidate list built by me (below). |

**What was read in full:** `tex/BCT_PRL_Letter.tex` (1,441 w); the Part XI + appendix stubs of `tex/BCT_Monograph_PLB.tex`; `BCT_Volume1_Foundations.tex` summary table; all four appendix volumes were text-extracted and searched exhaustively by pattern (every "Prediction #N", every "Nth sub-1%", every "★ sub-1%", every "= … MeV … err" line for the quantities in the prediction set), and ~40 appendices were read in full around each hit (D.3/D.4, CZ.2, DO, GR, GG2, GK2, HF4, HI4, HL4, HK2, HS2, HP4, GE2, GX2, JB6, KL6, LC7, LF7, LG7, LK6, LL7, LO6, LP6, LU6, LV6, LX6, LZ6, Phase 82D, Phase 83B, Phase 85C, Phase 88C, and the Strategic Review "57 quantities" table and the "Complete Index"). Not read: the ~400 appendices outside those hits. **Coverage of the corpus by word count: ~25% read in full, 100% pattern-searched.**

**Candidate list.** The corpus contains **no itemised 92-row prediction table.** The Monograph's "Master Parameter Table" (`app:parameters`) is an empty stub pointing to `BCT_MasterParameterTable_Final.pdf`, which is not in the corpus. The corpus's own ordinal ledger collides ("50th sub-1%" claimed by Phase 49B and Phase 59C; "66th" by both m_t/m_c and G_N; "65th" twice). **The number 92 cannot be reconstructed from the corpus's own count.** The prediction set below was therefore built from (i) the PRL Letter's named claims, (ii) the explicitly numbered #76–#93 hadronic ledger (Vol 2), (iii) the Phase-25 and Strategic-Review tables (which carry printed formulas). It covers 40 formulas / ~45 of the 92 headline entries. The remaining ~47 entries either have no printed closed form (multi-loop numerics), or I could not locate a formula for them in the search above (Δm²₂₁, Δm²₃₂, σ₈, R_τ, f₊(0), R(D*), B_K, quarkonia, GLS, g_A=1.276, μ_p, Γ(ρ→ee) chain, V_cb/V_ub tight-binding base, θ₂₃, the "exact" phases).

---
## §3 — Recomputation (reported before any scoring)

Script: `pred_step0_recompute.py` (mpmath, 30 dp, deterministic). Full table §9.

| result | count |
|---|---|
| formulas evaluated | 40 |
| reproduce their printed value (≤0.2%) | **39** |
| do not reproduce | **1** (r_n²: printed "(Q_u r_oct² − 2Q_d r_tet²)" is sign-ambiguous; the printed number needs \|Q_d\|; excluded) |
| cannot be evaluated in closed form (3-loop RGE, tight-binding bases, "BCT fixed point" α_s) | m_W, sin²θ_W(RGE), v(3L), α_s(m_Z), V_cb, V_ub — not scored |

Three transcription traps in the corpus, resolved before scoring: the PRL Letter prints C_p = (1+r_tet−r_oct)/π = 0.90527, but the value 0.90527 **is** 1+r_tet−r_oct (the "/π" is a misprint; every appendix uses the un-divided value); the hadron sector's m_π is **135.0 MeV (π⁰, rounded)**, not π±; the Koide "M₀²" is the quantity in MeV.

**Measurement vs BCT-chosen input (load-bearing).** Of the 40:
- **GEO** (geometry only, dimensionless, vs measurement): 7 rows → 1/α (×2 variants), sin²θ₁₃, sin²θ₁₂, n_s, sin²θ_W tree (fails 1%), sin²θ_W×(1+9α₀/4).
- **LAM+MEAS** (chosen anchor Λ=220 MeV + measured m_π/ħc): 18 rows → mesons, baryon tower, r_p, r_π, T_c, Koide(3).
- **V_BCT** (depends on v(3L)=244.4 GeV, an unrecomputable BCT 3-loop value at −0.64%): 7 rows → m_t, m_H, m_b, m_c, m_s, m_d, m_u.
- **MEAS-INPUT / CIRCULAR — excluded from scoring:** 8 rows → m_P = M_R/α₀² **(circular: M_R := m_P(obs)·α₀², App GG2 Phase 45A; "triple unification" is the same number)**; m_P = Λe^{S_QCD} (S_QCD fixed-point uses α_s input); m_e = m_P(obs)e^{−(π⁵+π)/6}; V_us (measured m_d, m_s inside); H₀ = H₀(Planck)(1+δ/2) (**the observed value times a correction, compared to itself**); Y_p = Y_p(SM)+4×10⁻⁷; m_K* = √(m_ρ m_φ(obs)); r_n² (Pauli term from measured κ_n, m_n). Also found but not tabulated: τ_n = τ_n(obs)·(g_A ratio)², m_Z "input-calibrated", V_ud and V_tb from unitarity of the other elements, α_s(m_Z)=0.1180 "[input]" (Phase 62) while the two derivations shown give +15.2% and +14.4%.

**Comparison-value drift.** Same quantity, different "observed" value across phases: Y_p 0.2470 (+0.04%) vs 0.2449 (+0.90%); θ₂₃(PMNS) "45.0° obs" (<0.03%) vs PDG ~49°; Δ*(1600) 1600 vs PDG Breit-Wigner ~1570 (+2.1% → fails 1%); m_t 173.3 vs PDG-2024 172.57 (0.0017% → +0.42%); N*(1535) 1535 vs 1530.

---
## §4 — Verdict

**SC-PRED-1: observed matches are within chance expectation.** The collection carries little evidential weight as a collection. §7's subset is the remaining result. No SC-PRED-5 item was found (no prediction published before its measurement and later confirmed; the m_W "post-CDF-II" and H₀ "sides with Planck" statements postdate the measurements they cite).

SC-PRED-3 was **not** triggered: the null could be bounded (alphabet and complexity read off the corpus's own printed formulas), and the bound is stated. The score is insensitive to the bound because coverage saturates, not because the bound is tight.

---
## §5 — Ingredient set (Step 1, derived from the corpus)

**Constants:** π, √2, √3, √6, r_oct=(√2−1)/2, r_tet=(√6−2)/4, α₀=r_oct r_tet/π, S_D4=π⁵/6, S_Td=S_D4(r_tet/r_oct)², N_c=3, small integers {1,2,3,4,5,6,8,9,12,17,18,24}, small rationals {1/4,3/8,1/2,3/4,3/2,9/4}; dimensionful anchor Λ=220 MeV (chosen); measured inputs used inside formulas: m_π, ħc, m_φ, κ_n, m_n, m_d, m_s, m_P, H₀, Y_p, τ_n, g_A, v (via BCT 3-loop).
**Operations:** + − × ÷, √, ∛, x², exp(−·), ln, arctan, cos, small powers.
**Patterns actually in use:**
- P1 **X·(1 + N·α₀)** — the "N-class". Printed N values: 3/8, 3/4, 1, 3/2, 2, 9/4, 3, 5, 8, 9, −1, −3/2, −2, −3, −4, −5, −6(=−2N_c). New N added when needed ("N=5 ★ NEW", "N=−5 ★ NEW", "N=−4=−(N_c+1)"). Base is typically a standard physics relation (GOR, GMO, VMD, Fritzsch, Koide, Regge, Yukawa y_t=1, seesaw) within 0.3–8% of target.
- P2 **m_t·exp(−S_Td·n/24)** with n = integer + geometric fraction chosen per quark (arctan(r_tet/π), r_tet(1+r_tet/r_oct), r_tet²/2r_oct, r_tet−r_tet²/r_oct).
- P3 **m_B² = m_ρ² + 2πΛ²·C_B**, C_B ∈ {C_p, C_p+2α₀, πC_p(1+8α₀), C_Δ+2C_n, C_Δ+3C_n, C_1535−C_n/4, 2C_Δ+C_p/2}.
- P4 ratios/products of void radii, /π, (1/α₀)^{1/3}, √(m₁m₂).
- P5 **measured value × (1+small)** and SM formulae fed with measured inputs.

---
## §6 — Null model (Step 2), score (Step 3), search-effort correction (Step 4)

Scripts: `pred_step2_nullmodel.py`, `pred_step3_multiplicity.py`, `pred_step4_sensitivity.py`, `pred_step5_score.py`. Enumerated, not sampled.

**Alphabet (J1):** 17 atoms = integers {1,2,3,4,5,6,8,9,12}, π, √2, √3, √6, r_oct, r_tet, α₀, S_D4.
**Complexity bound (J2):** ≤3 atoms, ≤2 binary ops, ≤1 unary op at a leaf (√,∛,x²,1/x,e^{−x},ln) and ≤1 at root (√,1/x,x²). Chosen because every core formula in §9 fits it ((1−5α₀)/π, 1−12/π⁵, α₀(1−2α₀), m_π/(2√α₀), α₀^{−1/3}/√2, πC_p(1+8α₀)…). Distinct values: 102 (1-atom), 90,755 (2-atom), **20,158,524 (3-atom)**.
**Correction layer (J3):** optional ×(1+Nα₀), N from the 24-value printed menu ±{3/8,3/4,1,3/2,2,9/4,3,4,5,6,8,9}. Reported with and without.
**Targets (J4, fixed before enumeration):** 48 dimensionless measured quantities across the sectors the corpus addresses (listed in the script: 1/α, sin²θ_W, PMNS angles, n_s, α_s, Ω_Λ, Y_p, lepton/quark mass ratios, Koide Q, meson & baryon ratios to m_π⁰/m_ρ/Λ, r_p·m_ρ/ħc, m_H/v, m_t/v, m_W/m_Z, g_A, μ_p, CKM, ln(m_P/·), σ₈, H₀, Ω_m).
**Tolerance (J5):** 1% and 0.1%.

**Hit rate — probability that a random expression lands within tolerance of *some* target:**

| set | tol | no N-layer | with N-layer | targets covered |
|---|---|---|---|---|
| 2-atom | 1% | 0.109 | 0.501 | 48/48 |
| 2-atom | 0.1% | 0.012 | 0.230 | 47/48 → 48/48 |
| 3-atom | 1% | 0.108 | 0.503 | 48/48 |
| 3-atom | 0.1% | 0.012 | 0.230 | 48/48 |

**Multiplicity — number of distinct expressions within tolerance of a *given* target (median over 48):** 2-atom: ~250 @1%, ~23 @0.1%. 3-atom: ~55,000 @1%, ~5,600 @0.1%. Every target has ≥5 two-atom expressions within 0.1% except m_μ/m_e (0 at 2-atom, 714 at 3-atom).

**N-layer reach:** a base within ±8.2% of target can be brought sub-1% by the printed menu with probability 0.77 per use, sub-0.1% with probability 0.25; a quarter-integer menu (which the corpus's on-demand extensions approach) makes sub-0.1% certain for any base within ±8.9%.

**Score.** Let T = quantities attempted, n = attempts per quantity, q = per-attempt sub-1% success (0.77 with the menu on a base within 8%).

| T | n | E[sub-1%] | observed | P(X ≥ obs) | bits |
|---|---|---|---|---|---|
| 130 | 3 | 128 | 92 (all claimed) | 1.0 | **0.00** |
| 130 | 3 | 128 | 28 (eligible) | 1.0 | **0.00** |
| 130 | 1 | 100 | 92 | 0.96 | 0.06 |
| 180 | 3 | 178 | 92 | 1.0 | 0.00 |
| **100** | **1** | **77** | **92** | **7×10⁻⁵** | **13.8** |

**Sensitivity (gate §4 clause): the score swings from 0 to 13.8 bits under one alternative — T=100, single attempt, all 92 counted.** That alternative is contradicted by the corpus's own record on both counts (revisits ≥3 documented for most headline quantities; ≥8 of the 92 are circular or measured-input constructions), so I read the score as ~0 bits, but the swing is reported as the gate requires. Alphabet variants (10–21 atoms) and tolerance 0.5% leave coverage at 48/48 and the hit rate within 0.11–0.13 (no layer) / 0.50–0.55 (with layer): **the null is robust, not fragile.**

**Search-effort estimate (Step 4).** From the corpus: 94 phases, 457–473 appendices, "100+ total predictions" at Phase 49 with 31 sub-1% then, 92 at Phase 94; an explicit "Level-1 (1–5%) → sub-1%" pipeline; distinct printed formulas per quantity: T_c ≥9, m_DM ≥6 (14.97 → 24.6 → 30 → 63 GeV → 4×10⁻¹² eV), r_p ≥6, m_e ≥6, m_p ≥4, sin²θ_W ≥4, Koide angle ≥4, m_ρ ≥4, v 4 loop-orders (−9.8% → −0.64%), 1/α 3, m_b 3, m_K 2, M_R 2 (values 10⁴ apart). **Estimate: ~130 quantities attempted (range 100–180), median ≥3 formula attempts each, ~400–1,500 formula trials total.** The 82 self-erroring appendices the gate expected map onto this pipeline. Uncertainty: a factor ~2 on T, a factor ~3 on trials. Under any value in those ranges except the corner (T≤100, n=1) the score is 0.

**Counterfactual upper bound (not the corpus's procedure):** if the 28 eligible hits had each been a single pre-fixed 3-atom expression, no correction layer, one attempt — 90 bits (28 × 3.2). If the 11 eligible sub-0.1% hits had been so fixed — 71 bits. The corpus has no pre-registered formulas; each formula appears in the same appendix as its comparison, after Level-1 predecessors.

---
## §7 — Strongest case for the corpus (Step 5) — **the real result of this gate**

Scored separately. Criteria: closed form from geometry, genuine measurement with small error, fewest documented predecessors.

| rank | prediction | formula | error | measurement σ | predecessors found | assessed bits (generous) |
|---|---|---|---|---|---|---|
| 1 | **1/α** | 1/[α₀(1−2α₀)], α₀=r_oct r_tet/π | −0.013% | 2×10⁻⁸ % | 3 (137.046 App E; one-loop; all-orders (1−3α₀)/(1−α₀)) | **~6** |
| 2 | **n_s** | 1 − 12/π⁵ | −0.43% | 0.44% (1.0σ) | 2 (0.9663 Phase 53) | ~2 |
| 3 | **sin²θ₁₃** | 3α₀ | +0.9% | 2.6% (0.3σ) | 2 (8.50° App BZ) | ~2 |
| 4 | m_Δ(1232) | √(m_ρ²+2πΛ²·πC_p(1+8α₀)) | −0.008% | 0.16% | 2 (Phase 87C, 88C); N=8 chosen on the spot; Λ chosen | ~1 |
| 5 | Koide (M₀², θ) | √2Λ(1+α₀); 2atan(r_tet)(1−α₀) | −0.13%, −0.055% | ~10⁻⁵ | ≥4 angle formulas | ~1 |
| 6 | m_ρ | m_π/(2√α₀)(1−3α₀/2) | +0.035% | 0.03% | ≥4 | ~0 |

**Reading of rank 1.** α₀ = r_oct r_tet/π is a 3-atom expression sitting +1.5% from α; the factor (1−2α₀) is one N-class choice. Given the base, the chance the needed N lies within 0.013% of a menu value is ~14% (2.8 bits); the base is one of ~10 natural void-radius combinations (3.3 bits). **~6 bits** is the most generous defensible credit, and it is the best single item in the corpus. It is not nothing; it is also not "the fine-structure constant derived". Three loop-order variants of the same formula, each with its own residual, show the correction being tuned after the comparison.

**Ranks 2–3** are two-atom formulas within 1σ of broad cosmological/neutrino measurements; ~130 two-atom expressions sit within 1σ of n_s, ~60 within 1% of sin²θ₁₃.

**Pre-fixed-then-confirmed (SC-PRED-5):** none. The corpus's untested predictions (Σm_ν ≈ 59 meV, r = 0.0046, τ_p ≈ 10^35.9 yr, d_n = 0, m_DM = 62.9 GeV, δ_CKM = arccos(1/3)) are the only place where genuine evidential weight could still be earned; note m_DM has already moved five times and δ_CKM is stated both as −π/2 "exact" and as arccos(1/3) = 70.5°.

---
## §8 — CN-PRED notices (tiered)

**CN-PRED-01 [PROVEN].** m_P = M_R/α₀² (PRL: "Planck mass derived, not input, −0.08%") is circular. App GG2 (Phase 45A, Vol 1 p. 690) defines M_R := m_P(obs)·α₀² = 6.695×10¹⁴ GeV using m_P = 1.22×10²⁸ eV; App HF4 (Phase 60C) divides the same number by α₀². The −0.08% is the rounding of 1.22 vs 1.22089. The "triple unification" M_R of Phase 47/55 is this number. **Clause: the Planck-mass claim, the "hierarchy M_R/m_P = α₀²" claim, and the "51st sub-1%" entry are withdrawn as evidence.**

**CN-PRED-02 [PROVEN].** The prediction count "92" is not reconstructible from the corpus: no itemised table exists (Monograph stub; referenced PDF absent), and the ordinal ledger collides (50th ×2, 65th ×2, 66th ×2). **Clause: any statement of the form "N sub-1% predictions" is ASSERTED until an itemised, formula-bearing table is committed.**

**CN-PRED-03 [PROVEN].** At least eight headline entries compare a measured value (or SM value with measured inputs) against itself plus a correction: H₀ = H₀(Planck)(1+δ/2); Y_p = Y_p(SM)+4×10⁻⁷; τ_n = τ_n(obs)(g_A ratio)²; m_Z input; V_ud, V_tb from unitarity; m_e = m_P(obs)e^{−(π⁵+π)/6}; m_K* = √(m_ρ m_φ(obs)). **Clause: excluded from any surprise count.**

**CN-PRED-04 [PROVEN].** α_s(m_Z) = 0.1180 "sub-0.01%" (Phase 16) has no derivation in the corpus reaching sub-1%: App HS2 gives +14.4%, the 1-loop appendix +15.2%, and Phase 62 lists α_s(m_Z) "[input]". **Clause: withdrawn.**

**CN-PRED-05 [PROVEN].** The C_p formula in the PRL Letter is misprinted ((1+r_tet−r_oct)/π ≠ 0.90527); the value used is 1+r_tet−r_oct. The Letter's seven baryon numbers are otherwise reproduced.

**CN-PRED-06 [PROVEN, this gate's construction].** Within the corpus's own alphabet and complexity, every one of 48 pre-fixed measured targets is reachable to 0.1% by a ≤3-atom expression, with median multiplicity ~5,600; with the printed N-menu, a random expression matches *some* target to 1% half the time. **Clause: sub-1% agreement, per se, carries ≈0 bits in this framework; sub-0.1% carries ≈0 bits once one correction factor is permitted.**

**CN-PRED-07 [CONJECTURE].** The corpus performed ~400–1,500 formula trials over ~130 quantities (evidence: revisit counts above; "Level-1 → sub-1%" pipeline; on-demand N additions). The exact number is not recoverable; the direction (n ≥ 3 per headline quantity) is documented.

**CN-PRED-08 [CONJECTURE].** The most generous defensible credit for the best item, 1/α = 1/[α₀(1−2α₀)], is ~6 bits; the next two (n_s, sin²θ₁₃) ~2 bits each. The remainder of the eligible set adds ≈0 given the correction layer and documented iteration.

**CN-PRED-09 [ASSERTED, for correction].** The v(3L) = 244.4 GeV chain (m_t, m_H, m_b, m_c, m_s, m_u; m_d fails at −1.2% vs PDG-2024) could not be recomputed; its status is inherited from an unverified 3-loop computation whose own error is −0.64%.

---
## §0.6 — reproduced verbatim

> A high surprise score would mean the predictions are **unlikely to arise from undirected search**.
> It would **not** establish that BCT's mechanisms are correct, that its derivations are valid, or
> that any particular appendix is sound — gates have already found mechanism failures that a good
> score would not repair. Conversely a low score would **not** show any individual prediction is
> wrong; it would show the collection carries little evidential weight. **Gate PRED measures
> evidential weight, not truth.** Either verdict leaves the mechanism questions exactly where they
> are.

---
## §9 — Prediction table (recomputed; comparison values PDG-2024/CODATA-2022/Planck-2018 unless the corpus's differs, then both)

| quantity | BCT formula as printed | printed | recomputed | observed (σ) | err % | class | sub-1%? |
|---|---|---|---|---|---|---|---|
| 1/α | 1/[α₀(1−2α₀)] | 137.018 | 137.018 | 137.035999 (2e-8) | −0.013 | GEO | Y |
| 1/α (all-orders) | (1−α₀)/[α₀(1−3α₀)] | 137.0336 | 137.034 | same | −0.002 | GEO | Y (same target) |
| sin²θ₁₃ | 3α₀ | 0.02222 | 0.022224 | 0.02203 (0.00058) | +0.88 | GEO | Y |
| sin²θ₁₂ | (1−5α₀)/π | 0.30652 | 0.30652 | 0.307 (0.013) | −0.16 | GEO | Y |
| n_s | 1−12/π⁵ | 0.9608 | 0.96079 | 0.9649 (0.0042) | −0.43 | GEO | Y |
| sin²θ_W tree | r_tet²/(r_oct²+r_tet²) | 0.2274 | 0.22744 | 0.23122 | −1.64 | GEO | N |
| sin²θ_W ×(1+9α₀/4) | | — | 0.23123 | 0.23122 | +0.004 | GEO | Y |
| m_ρ | m_π/(2√α₀)(1−3α₀/2), m_π=135.0 | 775.530 | 775.530 | 775.26 (0.23) | +0.035 | LAM | Y |
| m_K | m_π α₀^{−1/3}/√2 | 489.686 | 489.686 | 493.677 | −0.81 | LAM | Y |
| m_η | √(m_GMO²(1−6α₀)) | 547.455 | 547.455 | 547.862 | −0.074 | LAM | Y |
| m_η' | √(m_GMO²(1+6/π)) | 955.338 | 955.338 | 957.78 | −0.26 | LAM | Y |
| m_ω | m_ρ√(1+(r_oct²+r_oct r_tet−r_tet²)/π) | 782.111 | 782.111 | 782.66 | −0.070 | LAM | Y |
| m_K* | √(m_ρ m_φ) | 889.169 | 889.170 | 891.67 | −0.28 | MEAS-INPUT | excl. |
| m_p | √(m_ρ²+2πΛ²C_p), C_p=1+r_tet−r_oct | 936.35 | 936.346 | 938.272 | −0.21 | LAM | Y |
| m_n | C_n=C_p+2α₀ | 938.749 | 938.749 | 939.565 | −0.087 | LAM | Y |
| m_Δ(1232) | C_Δ=πC_p(1+8α₀) | 1231.90 | 1231.90 | 1232 (2) | −0.008 | LAM | Y |
| N*(1440) | C_Δ+2C_n | 1441.24 | 1441.24 | 1440 (30) | +0.086 | LAM | Y |
| N*(1535) | C_Δ+3C_n | 1535.25 | 1535.25 | 1530 (10) [corpus 1535] | +0.34 | LAM | Y |
| N*(1520) | C_1535−C_n/4 | 1512.29 | 1512.29 | 1515 (5) | −0.18 | LAM | Y |
| Δ*(1600) | 2C_Δ+C_p/2 | 1603.54 | 1603.54 | 1570 (70) [corpus 1600] | +2.14 | LAM | N (Y vs corpus) |
| r_p | (ħc/m_ρ)√(12C_p) | 0.83862 | 0.83862 | 0.84075 fm | −0.25 | LAM | Y |
| r_π | √6ħc/m_ρ(LO)(1+9α₀) | 0.66164 | 0.66164 | 0.659 (0.004) | +0.40 | LAM | Y |
| r_n² | Pauli+Dirac−α₀r_p² | −0.11692 | −0.10639 | −0.1155 | — | NO-REPRO | excl. |
| T_c | Λ/√2(1+3α₀/8) | 155.996 | 155.996 | 156.5 (1.5) | −0.32 | LAM | Y |
| m_τ | Koide M₀²=√2Λ(1+α₀), θ=2atan(r_tet)(1−α₀) | 1774.60 | 1774.60 | 1776.93 | −0.13 | LAM | Y |
| m_e | Koide k=1 | 0.512255 | 0.512255 | 0.510999 | +0.25 | LAM | Y |
| m_μ | Koide k=2 | 105.479 | 105.479 | 105.658 | −0.17 | LAM | Y |
| m_t | v_BCT/√2(1+3α₀/8) | 173297 | 173297 | 172570 (290) [corpus 173300] | +0.42 | V_BCT | Y |
| m_H | v_BCT/2(1+3α₀) | 124916 | 124916 | 125200 | −0.23 | V_BCT | Y |
| m_b | r_oct r_tet m_t(1+5α₀) | 4182.55 | 4182.55 | 4183 | −0.011 | V_BCT | Y |
| m_c | m_t e^{−S_Td(8+atan(r_tet/π)−δn_d)/24} | 1266.25 | 1266.23 | 1273 | −0.53 | V_BCT | Y |
| m_s | m_t e^{−S_Td(12+r_tet²/2r_oct)/24} | 93.33 | 93.328 | 93.5 | −0.18 | V_BCT | Y |
| m_d | m_t e^{−S_Td(17−δn_d)/24} | 4.644 | 4.6436 | 4.70 | −1.20 | V_BCT | N |
| m_u | m_t e^{−S_Td(18+δn_u)/24} | 2.158 | 2.1582 | 2.16 | −0.09 | V_BCT | Y |
| m_P | M_R/α₀², M_R:=m_P(obs)α₀² | 1.21995e22 | 1.22089e22 | 1.22089e22 | 0 | CIRCULAR | excl. |
| m_P | Λe^{S_QCD}, S_QCD=45.461 | 1.2185e22 | 1.2184e22 | 1.22089e22 | −0.20 | MEAS-INPUT | excl. |
| m_e | m_P(obs)e^{−(π⁵+π)/6} | 0.51112 | 0.51149 | 0.510999 | +0.10 | MEAS-INPUT | excl. |
| V_us | √(m_d/(m_s−m_d))(1−1.5α₀m_s/Λ) | 0.224534 | 0.224534 | 0.22453 | +0.002 | MEAS-INPUT | excl. |
| H₀ | H₀(Planck)(1+δ/2) | 67.670 | 67.670 | 67.4 (0.5) | +0.40 | MEAS-INPUT | excl. |
| Y_p | Y_p(SM)+(dY/dτ)Δτ | 0.24710 | 0.24710 | 0.245 (0.003) | +0.86 | MEAS-INPUT | excl. |

Eligible sub-1% (GEO+LAM+V_BCT, distinct targets, vs standard comparison values): **28** (11 of them sub-0.1%).

---
## §10 — Contamination statement

- Quarantine honoured: no `conversation_search`, no `recent_chats`; `audit/notes/`, `audit/gates/LINK/`, `audit/gates/C1/` not read; project-knowledge files not opened; memory files not read.
- **Declared:** `audit/NEXT.md` (not quarantined) contains the sentence "The identity family scored 3.3 bits (`notes/note_identities.md`)". I saw that headline number. I did not open the note and did not use the number; this gate's baseline was built independently (§6), on a different object, as §0.3 requires.
- The Cold Ledger memory files exist in the listing (`/projects/…/audit-findings.md` etc.). **Not read.**
- `audit/README.md` read (not quarantined).
- Comparison values: taken from the corpus where printed, otherwise from my own knowledge of PDG-2024/CODATA-2022/Planck-2018 (no web search was used; none was permitted by the quarantine as I read it). Where my value and the corpus's differ, both are shown.

---
## §11 — What this gate did NOT establish

- That any individual BCT prediction is wrong. Every closed-form headline number except r_n² reproduces.
- That BCT's mechanisms are wrong or right (§0.6).
- The true value of T or n; only their documented lower bounds.
- Anything about the ~47 headline entries whose formulas could not be located or evaluated.
- That no future pre-registered prediction could earn weight: Σm_ν, r, τ_p, d_n, m_DM, δ_CKM remain open — if fixed now and confirmed later, SC-PRED-5 applies to them.

---
## §12 — Files
`gate_PRED_prompt_asrun.md` (7e7675da…), `gate_PRED_RESULT.md` (this), `pred_step0_recompute.py`, `pred_step2_nullmodel.py`, `pred_step3_multiplicity.py`, `pred_step4_sensitivity.py`, `pred_step5_score.py`, `step2_out.txt`, `step3_out.txt`, `step4_out.txt`, `NEXT_patch.md`.
**Commit status: NOT committed.** This session has no push credentials for `zerofreeparameters-code/BCT-Programme`. Files are laid out as `audit/gates/PRED/` for you to commit; the NEXT.md edit is supplied as a patch.
