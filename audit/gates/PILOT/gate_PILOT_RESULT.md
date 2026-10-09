# Gate PILOT — RESULT

**Verdict: SC-PILOT-3 (IMPORT).** No-added-structure branch: **2b** on the first-order (Gross–Pitaevskii) law, **2a** on the second-order (wave / XY / Klein–Gordon) law, **2c** by counting on both. SC-PILOT-4 is not triggered: the corpus does not choose its dynamical law, but the primary verdict is the same on both branches.

Run 9 Oct 2026 (Barrys Reef, AEDT), fresh thread, one gate. Runner: Claude Opus 5.5. Tier cap: none (fresh thread).

---

## 0. Digests and run record

| Item | Value |
|---|---|
| Card URL | `https://raw.githubusercontent.com/zerofreeparameters-code/BCT-Programme/34acd40cd8d44221fdf94f775d1e3368c0e6bd46/audit/gates/gate_PILOT_prompt.md` |
| Card bytes on disk | 12,581 |
| **SHA-256 computed on disk, before reading** | `df9a4be17a9f359af6134651f011ced7203741590d6ef68266e4ff7518b29546` |
| **SHA-256 recorded in `audit/gates/PREREG_20261006.sha256` @ 34acd40** | `df9a4be17a9f359af6134651f011ced7203741590d6ef68266e4ff7518b29546` |
| Match | yes — card opened only after the match |
| SHA-256 of the PREREG file itself | `334583bcd45d3571f86689306cbeb994c1c1900af52de7e15987a554e8450e97` |
| Corpus pin | `0305526015460b2c90d6cbcb6ca9d0e56d82f64e` (clone over HTTPS, `git rev-parse HEAD` confirmed); `audit/` excluded |
| Volume text layers | `pdftotext -layout` of Vol. 1 Parts 1–3 and Vol. 2 (from the `.zip`): 1,457 pages |
| As-run prompt | `gate_PILOT_prompt_asrun.md` = the card, byte-identical (same SHA-256) |

**Quarantine disclosure (card §5).** Before opening the card, the runner read the `gate-pilot` memory summary (it holds the card's file metadata, the verdict bins and the stated prior — all of which the card itself states) and a `ways-of-working` memory file (protocol and tooling notes). A memory listing with one-line descriptions of other gate files (some including verdict codes) and a project document list with gate-result file names were in context from the start. None of those files, the Cold Ledger, the 6 Oct drafting chat, or anything under `audit/` other than the PREREG digest named in Step 1 was opened.

**The question (verbatim).**

> On the field content and dynamics the BCT corpus actually writes, is there any channel that propagates faster than the model's own c, and can any structure built from the written field content alone carry correlations between two separated defects that violate the CHSH inequality, independent of their separation, without permitting signalling?

**Short answer.** Yes, there is a faster-than-c channel — on the first-order GP law (and in Letter 73's continuum GW formula, which becomes subluminal on the lattice). It is an ordinary classical signal (≤ 6.56c on the lattice, unbounded in the continuum) that weakens with distance and is excluded by experiment. No structure built from the written field content alone violates CHSH. Every route in the corpus to a Bell violation runs through a quantum state (superposition, wavefunction, Bose–Hubbard Fock space) that the corpus postulates rather than derives.

---

## 1. Dynamics table (Step 2)

Every action or equation of motion the pinned corpus writes for the vacuum field. "Order" = order in time of the field equation.

| # | Written law | Primary source (location) | Order | Stated symmetries / notes |
|---|---|---|---|---|
| D1 | GP action S = ∫[(iħ/2)(Ψ*∂ₜΨ − Ψ∂ₜΨ*) − (ħ²/2m)\|∇Ψ\|² − (g/2)(\|Ψ\|²−n₀)²] | AZ6 eq:SGP, eq:Vgp (l.130–141); copied Vol 1 p.264 | **1st** | U(1); P₀ = 0; ξ = ħ/√(2mgn₀); g = mc²/n₀ ("Josephson condition") ⇒ c_s = c |
| D2 | iħ∂ₜΨ = [−(ħ²/2m)∇² + g\|Ψ\|²]Ψ | Letter 60, unlabelled (l.70) | **1st** | named "the Gross–Pitaevskii equation" governing the OHC |
| D3 | Madelung split of D1/D2: continuity + quantum Euler with Bohm potential | AZ6 eq:kin1–2; Letter 60 (l.~92–98); Letter 20 (l.~127) | 1st in (ρ,θ) | quantum pressure Q kept or dropped |
| D4 | Thomas–Fermi action S_SF = ∫[−ρ(∂ₜθ + v²/2) − ε(ρ)] and its quadratic part S⁽²⁾ (wave equation for δθ) | AZ6 eq:SSF, eq:S2; Letter 20 | 2nd for δθ after eliminating δρ | valid only for kξ ≪ 1 (quantum pressure dropped) |
| D5 | Hydrodynamics: ∂ₜρ + ∇·(ρv) = 0, ρ(∂ₜv + v·∇v) = −∇P (+ f_lattice) ⇒ ∂ₜ²δρ = c_s²∇²δρ | Vol 1 App E.3 §1.2 p.70; App E.0 p.50 | **2nd** | "c_s = c from the O_h phonon dispersion argument of App E.0" |
| D6 | XY / sine-Gordon: L = (J/2)[(1/c²)θ̇² − \|∇θ\|²] + λ cos θ, continuum of H = −J Σ cos(θᵢ − θⱼ); Lorentz form L = (ρ_s/2)η^μν∂_μθ∂_νθ | Vol 1 App E.1 §2.1 p.47, §1.1 p.52; lattice H p.33 | **2nd** | Lorentz claimed; λ cos θ breaks the θ-shift symmetry the same section gauges |
| D7 | S[Ψ₂] = ∫[J(∂_μΨ)² + (J/ξ²)(\|Ψ\|² − Ψ₀²)²/4] | App J eq:action (l.134–137); Vol 1 p.114 | **2nd** | Lorentz; App J calls this "the same GP action as the exterior" |
| D8 | (1/c_s²)∂ₜ²φ − ∇²φ = 0; covariant □_g φ = 0 | Vol 2 p.177 (acoustic metric) | **2nd** | acoustic Lorentz |
| D9 | ω² = c²\|k\|², "isotropic", source of Minkowski metric | Letter 129 eq:dispersion (l.~139) | 2nd (dispersion only) | exact linearity asserted |
| D10 | Bogoliubov ω(k) = c_s k √(1 + (kξ)²) | Letter 64 (l.95) | from D2 | different ξ convention from AZ6 (§2) |
| D11 | GW: ω² = c²k²[1 + α₀(kℓ_P)² + O(α₀²)] | Letter 73 (l.65–66) | 2nd (dispersion only) | plus sign ⇒ superluminal in the continuum |
| D12 | Two-band tight binding H(k) = α₀[[0, γ],[γ, 0]], γ = 8 cos(kₓ/2)cos(k_y/2)cos(k_z/√2); S_BCT = ∫[ψ*∂ₜψ − ψ*H_BCTψ] | Vol 1 App R.2 p.153 (citing App K/N); App W.4.2 p.179; AZ7 Lemma 1; Letter 39 eq:dispersion | **1st** | 8 neighbours (z = 8), bipartite; the +α₀\|γ\| band is labelled "photon/Goldstone"; no factor i in the written action |
| D13 | Bose–Hubbard H_BH = −t Σ(â†ᵢâⱼ + h.c.) + (U/2)Σ n̂ᵢ(n̂ᵢ−1) − μΣn̂ᵢ, t = α₀, U = μ = ħ²/(2mξ²) | AZ7 eq:BH (l.128–132); Letter 27 §I (stated, not written) | **1st** (quantum) | the only written second-quantised object in the corpus |
| S1 | Static only: −ξ²∇²Ψ + (g/J)\|Ψ\|²Ψ = Ψ; free energy F[Ψ_int] with Ψ_int ∈ ℂ²; vortex profile f″ + f′/r − H²f/r² + (1−f²)f = 0 | App J eq:GP; App JH eq:GP, eq:free-energy; Letter 60 | none | static; App JH is the only source of a two-component (S²-capable) field |

**Does any primary source choose between them?** No. Vol 2 §3 (p.463, "A3: Why the Gross–Pitaevskii equation? (The dynamics postulate)") names GP as an assumed postulate, and the only explicit time-dependent GP writings (D1, D2) are first order. But the same corpus writes second-order Lorentz-covariant laws for the same field (D6, D7) and App J calls its second-order action "the same GP action". Vol 2 A6 (p.463) states that time is added by hand. Vol 1 App E.0 §3.1 (p.48) states that the lattice has a preferred frame and that exact linearity of the lattice dispersion is "an unproven conjecture". So the corpus uses the name "GP" for both orders, and nothing adjudicates beyond the long-wavelength limit, where both reduce to ω = c_s k.

---

## 2. Dispersion, computed cold (Step 3)

Code: `pilot_dispersion.py` (full output `pilot_dispersion_output.txt`). mpmath 60 dps working, 40 reported. Units: nearest-neighbour distance a = 1, k → 0 sound speed c = 1 (the corpus's c_s = c). Any dimensionful statement inherits **a = ℓ_P** (Vol 2 A2).

### 2.1 ξ/a re-derived from r_oct, r_tet

The corpus's own formula is ξ = a/√(8πα₀) with α₀ = r_oct·r_tet/π (Vol 1 §4.3 p.82; Vol 1 p.104; AZ6 and AZ7 quote 2.32 ℓ_P "App E.3"). It is the textbook dilute-gas healing length (8πn a_s)^(−1/2) with n·a_s set to α₀; the sources read do not derive that identification.

| Quantity | Value (40 digits) |
|---|---|
| r_oct = (√2 − 1)/2 | 0.2071067811865475244008443621048490392848 |
| r_tet = (√6 − 2)/4 | 0.1123724356957945245493210186764728479915 |
| α₀ = r_oct r_tet / π | 0.007408055727547908079640101104499873415571 |
| **ξ/a = 1/√((√2−1)(√6−2))** | **2.317543794911664963039020806144813022013** |
| **ξ²/a² (exact)** | **1 + √2 + √3 + √6/2** = 5.371009241333561391427777103068516141495 |

Cross-checks against printed corpus numbers: 2/ξ = 0.86298261 (App J prints 0.8630); −1/ξ + α₀ = −0.42408325 (App J prints −0.424083); ξ/r_oct = 11.190091 (Vol 2 prints 11.1901).

**Conventions relating ξ to the coupling — the sources differ, so each is computed:**

| Code | Source | Definition | Bogoliubov law (β ≡ coefficient of k⁴/k²) | β |
|---|---|---|---|---|
| C1 | AZ6, AZ7 | ξ = ħ/√(2mgn₀) = ħ/(√2 m c_s) | ω = ck√(1 + (kξ)²/2) | ξ²/2 = 2.68550462066678069571 |
| C2 | Letter 64 dispersion | ω = c_s k√(1 + (kξ)²) ⇒ ξ = ħ/(2mc_s) | as written | ξ² = 5.37100924133356139143 |
| C3 | Letter 64 text (l.199) | ξ = ħ/(m c_s) | ω = ck√(1 + (kξ)²/4) | ξ²/4 = 1.34275231033339034786 |
| GW | Letter 73 | — | ω² = c²k²[1 + α₀(kℓ_P)²] | α₀ |

### 2.2 The lattice

The 12 nearest neighbours at c/a = √2 are the 8 body vectors (±½, ±½, ±1/√2) and the 4 in-plane vectors (±1,0,0), (0,±1,0), all at distance a (this lattice is fcc; Vol 2 Phase 67C, p.56, uses the same 12). Graph Laplacian normalised so λ(k) → |k|²:

λ(k) = ½ Σ_d (1 − cos k·d) = |k|² − |k|⁴/16 + (Σᵢ Kᵢ⁴)/48 + O(k⁶)  (Kᵢ = cubic-axis components)

- The k² term is isotropic (Σ d dᵀ = 4·I). The 8 body vectors alone — the corpus's γ(k), z = 8 — are **not** isotropic (Σ d dᵀ = diag(2,2,4)).
- Exact quartic: Σ_d (k·d)⁴ = 3|k|⁴ − Σ Kᵢ⁴. The k⁴ coefficient of λ is **−1/24 along [001], −5/96 along [110], −1/18 along [111]**: nonzero and direction-dependent.
- **This settles the corpus's open conjecture (App E.0 §3.1, p.48) negatively.** O_h symmetry does not make the quartic term vanish on the nearest-neighbour lattice. More generally, exact linearity is impossible for *any* finite-range lattice operator: ω²(k) is then a trigonometric polynomial (real-analytic and periodic), and if it equalled c²|k|² on a neighbourhood of k = 0 it would equal it everywhere, contradicting periodicity. Letter 129's ω² = c²|k|² can only hold as k → 0.

### 2.3 Maximum group velocity over the Brillouin zone

Method: 96³ grid over a primitive reciprocal cell, then Nelder–Mead in 3D, then a 60-dps solve of dv/ds = 0 along the located line, then a 60-dps check that perpendicular displacements lower v. Every finite-k maximum was re-derived from the closed Γ–X line formula λ = 4(1 − cos u), |∇λ| = 2√2 sin u, u = |k|a/√2, and agrees to 25 digits. An independent agent that had not seen this code reproduced all values below to 17 digits.

| Law | Continuum ω(k) | Continuum max v_g; front | Lattice max \|∇ₖω\| / c | Where |
|---|---|---|---|---|
| **W** — D4, D5, D6 (Goldstone), D8, D9 | ck | c; **strict front at c** | **sup = 1, approached only as k → 0, never exceeded** (v_g = c[1 + (3/2)c₄k²], c₄ ∈ [−1/18, −1/24]) | Γ (limit) |
| KG — D7 amplitude mode, m = 1/ξ (from the written action, Ψ₀ = 1) | c√(k² + m²) | < c; front c | 0.859014404253093980903638756 | \|k\|a = 1.0476979075, cubic ⟨100⟩ axis |
| KG — m = 2/ξ (App J's printed gap) | as above | < c; front c | 0.740400151567981142578553204 | \|k\|a = 1.4009127884, cubic ⟨100⟩ axis |
| **B-C1** — D1/D2, AZ6 ξ | ck√(1 + β k²) | **unbounded** (∝ k); **no front** | **4.63968713561952724031851567** | \|k\|a = 2.2187484302, cubic ⟨100⟩ axis (0.4994 of Γ–X) |
| **B-C2** — L64 dispersion ξ | as above | unbounded; no front | **6.55670061415945919348401597** | \|k\|a = 2.2207251302, cubic ⟨100⟩ axis |
| **B-C3** — L64 text ξ | as above | unbounded; no front | **3.28952755197413963517788682** | \|k\|a = 2.2118098304, cubic ⟨100⟩ axis |
| GW — D11 | ck√(1 + α₀k²) | unbounded; no front | **sup = 1 at k → 0**; the lattice quartic (≤ −1/24) outweighs +α₀ (it would need β > 1/24 to exceed c: near Γ from the series, and on a 120³ grid in the independent check) | Γ (limit) |
| TB — D12, corpus γ(k), z = 8 | (lattice-only law) | — | 4√2 α₀ = (2−√2)(√6−2)/(2π) = **0.04190629152285575009660609** (absolute, units of c) | k = (0, 0, π/√2), nodal plane |
| BH — D13 mean-field Bogoliubov, t = U = α₀, n₀ = 1 | (lattice-only law) | — | **0.04217007657817007676** (absolute) | k_z = 2.2052354491 |

For the z = 8 laws there is no isotropic k → 0 sound speed: BH gives √2α₀ = 0.0104765729c along x and 2α₀ = 0.0148161115c along z (exact). Its maximum is 4.03× (x) and 2.85× (z) its own sound speed, but 24× *below* c in absolute units. These laws are anisotropic at O(k²) and inconsistent with the corpus's c_s = c.

None of the written laws, on the corpus's lattice or in the continuum, has a maximum group velocity of 6.78c (the closest is B-C2 at 6.5567c). The 6.78c of App JH is an interior phase velocity κ₀/R (§4, K5).

### 2.4 Front velocity

- **Continuum:** W and KG are hyperbolic, with a strict front at c. B-C1/2/3 and GW have unbounded group velocity and no front — the first-order GP response is nonzero everywhere for t > 0.
- **Lattice:** no law has a strict front. Continuous-time evolution under a bounded nearest-neighbour operator gives a Green's function G(r,t) that is entire in t and nonzero at every r for t > 0. Outside the max-group-velocity cone the tails decay faster than any exponential. FFT on a 128³ primitive lattice, G = IFFT[sin(ωt)/ω] along a₁:

| Law | t (a/c) | Cone v_max·t | \|G\|/max\|G\| just outside | Fit outside cone |
|---|---|---|---|---|
| W | 8 | 8.0 a | 1.7×10⁻³ at r = 10; 1.4×10⁻¹⁶ at r = 20 | ln\|G\| = −2.65 r ln r + 6.70 r − 15.0 |
| B-C1 | 4 | 18.6 a | 2.1×10⁻³ at r = 20; 8.6×10⁻¹³ at r = 34 | ln\|G\| = −1.71 r ln r + 5.87 r − 25.9 |
| GW | 8 | 8.0 a | 2.2×10⁻³ at r = 10; 3.9×10⁻¹⁵ at r = 18 | ln\|G\| = −5.58 r ln r + 16.6 r − 46.7 |

The negative r ln r coefficient is the superexponential (Bessel / Lieb–Robinson-type) decay law. These precursors fall with distance and are signals, so they fail T2 and T3 by construction.

---

## 3. Search table (Step 4)

Scope: all 138 `.tex` files in the pinned tree outside `audit/` (top-level and `tex/`), plus the four Volume PDF text layers. Proper nouns and acronyms (Bell, Born, Bohm, Fock, CHSH, Tsirelson) are matched as case-sensitive whole words. Everything else is matched as a case-insensitive substring. Code: `search.py` (JSON in `search_*.json`).

| Term | .tex hits / files | Volume PDF hits | Files (.tex unless noted) and notes |
|---|---|---|---|
| entangle | 51 / 7 | 13 | L201 (18), L254 (17), L72_Measurement (8), AZ6 (3), L72_MeasurementProblem (2), L137 (2), L125 (1); Vol 1 & 2 (black-hole "vortex entanglement entropy") |
| Bell | 20 / 3 | **0** | L201 (10), L254 (9), L101 (1, "Bell bronze" — not Bell's theorem). All 25 PDF "Bell" strings are "Belle" |
| CHSH | 2 / 1 | 0 | L254 only |
| Tsirelson | 4 / 1 | 0 | L254 only |
| nonlocal | **0** | 0 | absent everywhere |
| non-local | 10 / 9 | 0 | KA2, L103, L105 (×2 copies), L106, L201, L254, L64, L72 |
| pilot | 3 / 2 | 0 | L106 (2), L72 (1) |
| Bohm | 12 / 4 | 14 | L106 (8), L20 (2, "Bohm potential"), L254 (1), L60 (1); PDF hits are Aharonov–Bohm / Bohm potential |
| de Broglie | 0 | 2 | Vol 1 Pt 2, Vol 2: "de Broglie wavelength" only |
| hidden variable | 5 / 4 | 0 | L72 ×2 versions, L106, L254 |
| configuration space | 1 / 1 | 2 | L64 (Theorem I); Vol 1 p.52 ("configuration space of the BCT lattice admits vortex defects") |
| Born | 2 / 1 | 0 | L72_MeasurementProblem ("Born rule … deferred to Appendix JH6") |
| collapse | 122 / 25 | 1 | mostly wavefunction collapse (L72 ×2, L201, L204 series, L254); some unrelated senses |
| superposition | 38 / 7 | 0 | L72 ×2, L201, L254, AppL204b, L137, L104 |
| **wave functional** | **0** | **0** | **absent everywhere — a finding** |
| **Fock** | **0** | **0** | **absent everywhere — a finding** |
| **second quantis** | **0** | **0** | **absent** (but "second-quantised" appears once, in AZ7) |

Supplementary terms, searched to find written quantisation: `\hat{a}` 7 hits, all in AZ7 (eq:BH); `Bose-Hubbard` 8 (AZ7, L27, L128); `path integral` 8 tex + 22 PDF (App J invokes "the BCT lattice path integral" but never writes it); `wavefunction` 25 tex + 47 PDF; `commutat` 15 (App JH/L36/L72: [x̂,p̂] = iħ "from Hopf topology").

Dynamics-term counts (Step 2) are in `search_dyn.txt`: `\partial_t` 12/3 (+23 PDF), `i\hbar` 13/8, `\partial_\mu` 7/3 (+44 PDF), `Bogoliubov` 16/6, `dispersion` 35/12 (+63 PDF), `omega(k)` 4/4 (+10 PDF), `group velocity` 4/4 (all App JH copies: "a phase velocity, not a group velocity"), `phase velocity` 33/13, `superlumin` 21/7, `v_{\rm ph}` 9/5, `healing` 9/5 (+18 PDF), `\dot` 0, `\Box` 0 in .tex (25 PDF, mostly checkbox glyphs; `\square` 19, mostly end-of-proof marks).

### Every hit read in context: the objects claimed to carry a joint state

| Mechanism | Claimed carrier of the joint state | Governing equation written? |
|---|---|---|
| **L254** "entanglement = one Hopf configuration" | a single extended Hopf-charge configuration H = (1/16π²)∫F·A, "fixed at creation, not at measurement"; each wing "reads the local projection" | **none** — H is defined, no dynamics; singlet ↔ "H = 0 configuration" asserted |
| **L64** Theorem II (redundancy) | H readable "by a local measurement of the condensate field" anywhere | none beyond the H integral (with a different prefactor, 1/4π²) |
| **L72, L72_MeasurementProblem, L201** | "the wavefunction is the superposition state of Hopf charge windings"; collapse at N_c = 1/α₀ ≈ 135 | standard QM (Schrödinger equation referred to, not written in BCT variables); measurement postulate added |
| **AZ7** Bose–Hubbard | Fock-space state of lattice bosons âᵢ | H_BH (eq:BH) — postulated ("are described by"), with t = α₀, U = t_kin |
| **KA2, L103, L105, L70** | phase imprint δφ = α₀(ℓ_P/r) f(t − r/v_ph) "propagates at 6.78c throughout the global OHC" | asserted; no equation of motion produces it. KA2 cites "Letter 59", which contains no "6.78"; App JH and L36 call 6.78c a phase velocity that carries no signal |
| **L106** | "the pilot wave IS the Hopf fibration structure guiding quantum propagation" | none — no beable, no wave, no guidance equation |
| AZ6, Vol 1 p.264, Vol 2 | entanglement entropy of vortex pairs across a horizon (S_BH) | Bogoliubov quantum fluctuations — imported quantisation; not a two-defect Bell carrier |

---

## 4. Candidate carriers and T1–T5 (Step 5)

Supporting code: `pilot_tests.py` (output `pilot_tests_output.txt`). Defects A and B are separated by L ≫ ξ.

**Topology before topological invariants (guard 4).** The written time-dependent field (D1, D2, D7, S1-App J) is one complex scalar: Ψ/|Ψ| ∈ S¹, with π₁(S¹) = ℤ (vortex lines) and **π₃(S¹) = 0** (no Hopf charge). The only written field that can carry a Hopf charge is App JH's two-component Ψ_int ∈ ℂ² (n̂ ∈ S², π₃(S²) = ℤ). It is written only as a static field inside each sphere of radius ℓ_P/2 (domain B³(R)), not as an extended field joining separated defects. Letter 64 writes the map Ψ/|Ψ|: ℝ³ → S² for a field that Letters 27 and 60 make a single complex scalar — an S¹/S² inconsistency.

| # | Candidate | T1 CHSH, setting term | T2 no signalling | T3 L-independence | T4 Mermin / counting | T5 speed | Outcome |
|---|---|---|---|---|---|---|---|
| **K1** | GP / Bogoliubov field channel (D1, D2, D10) | The only term coupling B to A is the field's own propagation (the ħ²∇²/2m kinetic term ⇒ G(r,t)). It can make A depend on B's setting only by **carrying a signal**. | **FAIL** — A's local field, hence A's statistics, depend on B's setting whenever the channel acts; nothing written enforces marginal independence | **FAIL** — G decays with L (dispersive spreading; superexponential outside the lattice cone) | not reached | Lattice v_max/c = 4.640 (C1), 6.557 (C2), 3.290 (C3); continuum unbounded. Salart Eq. 3 (worst case \|β∥\| = β, no Earth-rotation gain) excludes it as the carrier of the 18-km correlations for every privileged frame with Earth speed **β < 0.2155 (C1), 0.1525 (C2), 0.3040 (C3)**. Bancal: any finite v permits signalling (4 parties). | **2b** |
| **K2** | Wave / XY / KG branch (D4–D9, D7) | Same structure as K1 | precursors only: FAIL | FAIL | not reached | Nothing exceeds c in group velocity (continuum: strict front c; lattice: sup c, not attained). Only superexponential precursors. | **2a** |
| K3 | GW dispersion (D11) | as K1 | FAIL (continuum) | FAIL | — | Continuum superluminal (unbounded); lattice sup = c | 2b continuum / 2a lattice |
| K4 | Tight-binding band (D12), Bose–Hubbard mean field (D13) | as K1 | — | — | — | 0.0419c and 0.0422c: subluminal in absolute units | 2a |
| **K5** | KA2 phase imprint at 6.78c | not exhibited (no setting term) | **FAIL** as a signal | **FAIL** (amplitude ∝ 1/r) | — | 6.78c: Salart excludes it for every frame with β < 0.1475 (worst case); Salart's own result is > 10⁴c for β ≤ 10⁻³. And if it is a phase velocity (App JH, L36), it is not a channel at all (guard 1). | **2b**; not derived from any written law |
| **K6** | L254 / L64 "one Hopf configuration, fixed at creation, read locally" | **FAIL.** No term by which B's setting enters A's outcome. A quantity fixed at creation and read locally is a local hidden variable (guard 2). Computed: local readout of a shared orientation gives E = −(1 − 2\|a−b\|/π) and \|S\| = **2.000000000000** at the Tsirelson settings (quantum singlet: 2.828427124746); max over 3,000 random setting sets = 2.000000000000. | passes trivially | passes trivially | **FAIL**: every local deterministic strategy gives \|M\| ≤ 2 (enumerated, 64 strategies) | n/a | **no carrier (2)** |
| K6′ | L254 eq:tsirelson, 1/(2r_oct + 1) = 1/√2 = cos(π/4) | True as algebra (2r_oct + 1 = √2), but it supplies no correlation function, no setting term and no bound | — | — | — | — | **scored zero** (guard 5) |
| **K7** | L72 / L201 superposition of Hopf states; AZ7 Fock space | Inherited from the quantisation postulate. No two-defect state or measurement model is written. L72_MeasurementProblem's postulate "the outcome is determined by the pre-existing integer Hopf charge of the coupled condensate region", read literally, is a local-value rule and gives S ≤ 2 — in tension with L201's claimed Bell violation up to 16 pairs. | QM no-signalling (imported) | QM (imported) | GHZ ⟨M⟩ = **4.000000000000** — only with an imported 3-qubit Hilbert space | — | **SC-PILOT-3** (guard 7) |
| K8 | L106 "pilot wave = Hopf fibration" | nothing to test: no beable, no wave, no equation | — | — | — | — | NONE FOUND |

**T4 counting (2c).** The written fields supply 2 real numbers per site (complex Ψ), 1 per site (XY θ), or 4 per sphere (App JH ℂ²): 2N_s reals for N_s sites. A pure joint state of N defects on N_s sites needs 2N_s^N − 2 reals. For N_s = 10³ that is 2.0×10⁶ (N = 2) and 2.0×10⁹ (N = 3), against 2.0×10³ from the field. Three qubits: a product state has 6 parameters, a general pure state 14. A mean-field condensate is a product state: max |⟨M⟩| over 2,000 random product states was 0.975, against 4 for GHZ. The only known escape — Norsen's exclusively-local-beable construction, extended by Norsen–Marian–Oriols — reproduces configuration-space information in physical-space fields only with an infinite network of added interacting fields. That is added structure, not the written field.

**T5 frame assumption, stated exactly.** Salart et al.'s >10⁴c figure assumes a privileged frame in which Earth's speed is β ≤ 10⁻³ and uses Earth's rotation to bound β∥. Their Eq. 3, (V/c)² ≥ 1 + (1−β²)(1−ρ̄²)/(ρ̄ + |β∥|)² with ρ̄ = 5.4×10⁻⁶, holds for any β; the β* thresholds above use the worst case |β∥| = β. **The corpus never identifies its preferred frame with any observable frame.** Vol 1 p.48 says only "the rest frame of the lattice", and the two "lattice frame" search hits are "Lattice framework". So the corpus cannot say whether Salart's condition holds. Every finite v_max it writes is nevertheless excluded for any frame in which Earth moves slower than ≈ 0.15c.

---

## 5. Pilot-wave readings (Step 6)

### Reading P — defects are the beables (de Broglie–Bohm)

- **Beable:** defect positions X₁…X_N (vortex cores / Hopf solitons).
- **Wave:** Φ(X₁,…,X_N, t) on configuration space ℝ^{3N} (dimension 3N); on the lattice, a function on N_s^N discrete configurations.
- **Guidance:** dX_k/dt = (ħ/M_k) Im[∇_k Φ / Φ], with iħ∂ₜΦ = [Σ_k −(ħ²/2M_k)∇_k² + V(X₁…X_N)]Φ. On a lattice a velocity field is unavailable, and a discrete (jump-rate) guidance law would itself be added structure.
- **Vortex-core check:** the condensate cannot be its own defects' pilot wave. Solving Letter 60's profile equation (H = 1; converged; core slope f′(0) = 0.583189) gives |Ψ|²/n₀ = 3.4×10⁻⁵ at r = 0.01ξ and 3.4×10⁻³ at 0.1ξ. The equilibrium weight inside r < 0.1ξ is 1.7×10⁻³ of bulk, and the Madelung velocity (ħ/m)/r diverges at the core. If Ψ guided a core beable, quantum equilibrium ρ = |Ψ|² would assign almost zero probability to the beable being where the defect is. Φ must be a separate object, and the corpus does not write it.
- **Order in time of a defect's equation of motion** (from Ψ(X(t), t) = 0):
  - First-order GP: Ẋ·∇Ψ = −(iħ/2m)∇²Ψ at the node, so Ẋ is fixed by Ψ alone — **first order**, de Broglie-like in form. But the guiding object is the 3D field, so defect velocities are local functionals of Ψ, and correlations travel only through K1.
  - Second-order law: Ẋ·∇Ψ = −∂ₜΨ, and ∂ₜΨ is independent Cauchy data, so Ẋ is extra initial data — **second order**. A Reading P there is Bohm's second-order form, whose equilibrium Colin and Valentini argue is unstable, unlike de Broglie's first-order dynamics.
- **Left free by standard pilot-wave theory, and whether BCT fixes it:**

| Free quantity | Fixed by r_oct, r_tet, ξ/a or the lattice? |
|---|---|
| Φ₀ (the initial entangled state itself) | no |
| initial distribution (equilibrium \|Φ\|² or non-equilibrium ρ₀) | no |
| defect inertial masses M_k | no (L64's m = H·E_D4/c² needs Λ_QCD as an input) |
| interaction potential V | no |
| preferred foliation | lattice supplies "a" frame, but its velocity is unspecified |

### Reading F — field configurations are the beables (Bohm 1952 II, Valentini, Struyve)

- **Beable:**
  - First-order GP branch: Ψᵢ and iħΨᵢ* are canonically conjugate, so the configuration is one half — e.g. {ρᵢ} with θᵢ conjugate, or {Re Ψᵢ}. Configuration space ℝ^{N_s} (dimension N_s).
  - Second-order branch: {θᵢ} ∈ T^{N_s} (XY, dimension N_s) or {Ψᵢ} ∈ ℂ^{N_s} = ℝ^{2N_s} (App J, dimension 2N_s), with conjugate momenta πᵢ.
  - Either way the dimension is independent of N; defects are particular field configurations.
- **Wave:** a wave functional Ξ[φ, t] on that configuration space, with iħ∂ₜΞ = Σᵢ[−(ħ²/2μ)∂²/∂φᵢ²]Ξ + V[φ]Ξ (μ = stiffness × cell volume / c² per site, cell volume a³/√2; the corpus mixes J and ρ_s = J/a).
- **Guidance:** dφᵢ/dt = (1/μ) ∂S/∂φᵢ, with Ξ = |Ξ|e^{iS/ħ}. Entanglement of two separated defects is a non-factorisable Ξ.
- **Does any primary source write the wave functional or the quantisation?**
  - Wave functional: **no** (0 hits for "wave functional" or "Fock").
  - Quantisation: **yes, once, as a postulate.** AZ7 eq:BH writes the Bose–Hubbard Hamiltonian with bosonic âᵢ — Fock-space quantisation of the lattice bosons, equivalent to a wave functional in the occupation basis. It is asserted ("are described by"), uses z = 8 (not the 12-neighbour lattice), and its parameters give a sound speed of 0.0105c–0.0148c, not c. L72 and L201 use a Hilbert space of Hopf states with no Hamiltonian in field variables.
  - So the quantum structure Reading F needs is added, or postulated where present.
- **Left free by standard pilot-wave theory, and whether BCT fixes it:**

| Free quantity | Fixed by r_oct, r_tet, ξ/a or the lattice? |
|---|---|
| Ξ₀ | no |
| beable choice (which conjugate half) | no |
| equilibrium \|Ξ\|², or non-equilibrium + relaxation scale | no |
| preferred frame / foliation | lattice supplies "a" frame; its velocity is free (3 numbers) |
| UV cutoff | lattice supplies a; a = ℓ_P is assumed (A2), not derived |
| beable density | √2/a³ (the cutoff again) |

**Does the lattice geometry fix any quantity that standard pilot-wave theory leaves free (SC-1 ii)?** No.
- ξ/a = 2.3175 fixes β in the Bogoliubov law — a dynamics parameter that is identical in standard lattice QFT.
- The anisotropic quartic (−|k|⁴/16 + ΣKᵢ⁴/48) is a closed-form, Planck-suppressed, in-principle measurable dispersion correction. But it belongs to the runner's nearest-neighbour operator (the corpus writes no lattice operator for the 12-neighbour graph), and it is interpretation-independent.
- In non-equilibrium pilot-wave theory, signals are instantaneous in the preferred frame (Valentini). A lattice v_max would bound nothing there.

---

## 6. Literature opened (card §6)

All read through a fetch tool that summarises pages; "full text" means the tool read the full text and returned a summary or extract.

| Reference | Opened | Depth | Used for |
|---|---|---|---|
| Bell, Physics 1, 195 (1964) | PDF copy (univaq.it) | full text, summary | local outcome A(a,λ); guard 2 |
| Clauser, Horne, Shimony, Holt, PRL 23, 880 (1969) | PDF copy (informationphilosopher.com) | full text, summary; citation confirmed | CHSH local bound 2 |
| Mermin, PRL 65, 1838 (1990) | **not opened directly** (APS fetch failed) | citation and the 2-vs-4 bound confirmed via a secondary source (arXiv quant-ph/0202139); value 4 recomputed here | T4 |
| Bancal et al., Nat. Phys. 8, 867 (2012), arXiv:1110.3795 | arXiv abstract + ar5iv full text | full text, summary; DOI 10.1038/nphys2460 (volume/page from the card) | 4 parties; any finite v ⇒ signalling; bipartite case only by bounding v |
| Salart et al., Nature 454, 861 (2008), arXiv:0808.3316 | arXiv abstract + ar5iv full text | full text, summary; DOI 10.1038/nature07121 (volume/page from the card) | Eq. 3; ρ̄ = 5.4×10⁻⁶; >10⁴c for β ≤ 10⁻³ |
| Valentini, PLA 156, 5 and 158, 1 (1991) | **primaries not opened** | citations (156: 5–11; 158: 1–8) confirmed from Valentini's review arXiv quant-ph/0104067 (opened) and a catalogue page; content (equilibrium hides nonlocality; non-equilibrium gives instantaneous signals; H-theorem relaxation) from that review | Readings P and F; cost statement |
| Colin & Valentini, Proc. R. Soc. A 470, 20140288 (2014), arXiv:1306.1576 | arXiv abstract | abstract; DOI 10.1098/rspa.2014.0288 matches the cited article number | Bohm second-order equilibrium unstable; de Broglie first-order relaxes |
| Struyve, Rep. Prog. Phys. 73, 106001 (2010), arXiv:0707.3685 | arXiv abstract + ar5iv | abstract and section headings only; the foliation and regularisation sections were not reached | field beables for bosonic fields, incl. the Schrödinger field; no specific claim cited beyond the abstract |
| Norsen, Found. Phys. 40, 1858 (2010), arXiv:0909.4553 | arXiv abstract | abstract; DOI 10.1007/s10701-010-9495-2 (Found. Phys. prefix), volume/page not separately confirmed | exclusively-local-beable construction (T4 caveat) |
| Norsen, Marian, Oriols, Synthese 192, 3125 (2015), arXiv:1410.3676 | arXiv abstract | abstract (lists "to appear in Synthese"; volume and page not confirmed) | the infinite-network cost (T4 caveat) |

Nothing else is cited.

---

## 7. One-sentence kill (Step 7)

> **Every carrier the corpus writes is either a quantity fixed at creation and read locally — a local hidden variable, so CHSH ≤ 2 — or a classical field signal that weakens with distance and is bounded on the lattice by v_max ≤ 6.56c, so it signals and is experimentally excluded; the only route in the corpus to S = 2√2 is a quantum state (superposition, wavefunction, or Bose–Hubbard Fock space) that the corpus postulates rather than derives from r_oct, r_tet or the lattice.**

**True.** It closes the gate at SC-PILOT-3.

## 8. Verdict

**SC-PILOT-3 (IMPORT).**
- Bell violation is obtainable only through a wave or wave functional on configuration space — or the equivalent Fock-space quantisation that AZ7 postulates.
- The lattice supplies a preferred frame (velocity unspecified) and a cutoff (a = ℓ_P assumed).
- Nothing is derived from geometry; the r_oct ↔ cos 45° identity scores zero.

**No-added-structure branch:**
- **2b** on the first-order GP law: a faster channel exists (continuum unbounded; lattice 3.29c / 4.64c / 6.56c by ξ convention) but fails T2, T3 and T5.
- **2a** on the second-order law: nothing exceeds c.
- **2c** by counting on both: 2N_s versus 2N_s^N − 2.

**SC-PILOT-4 is not triggered.** The corpus does not choose the law, but the primary verdict is SC-PILOT-3 on both branches. The stated prior (SC-PILOT-3 with 2b or 2c) is confirmed. The runner had seen it (card and disclosure above), and every element of the verdict rests on the citations and computations in §§1–5.

**Reopen conditions (card §8)** apply unchanged:
- SC-3 reopens only if a written source is shown to force the configuration-space wave or wave functional with zero remaining freedom. AZ7's Bose–Hubbard Hamiltonian is asserted, not forced, and the initial state stays free.

## 9. Cost statement (Step 8)

**What must be added** to obtain Bell-violating correlations:
- **Reading P:** a wave Φ on ℝ^{3N}, its Schrödinger equation, defect inertial masses, a defect–defect potential, and the equilibrium postulate.
- **Reading F:** a wave functional Ξ on ℝ^{N_s} (first-order branch) or ℝ^{N_s}–ℝ^{2N_s} (second-order branch), i.e. quantising the lattice field (AZ7 already postulates this for its z = 8 bosons), plus a beable choice and the equilibrium postulate.
- In both: the entangled initial state itself.

**Free inputs:**
- the initial state — infinite-dimensional, and the entanglement lives in it rather than coming out of geometry;
- the equilibrium hypothesis (or ρ₀ and a relaxation scale);
- the velocity of the lattice frame (3 numbers; the corpus is silent);
- a discrete beable choice;
- every SI-scale statement inherits a = ℓ_P.

**What it does to c_s = c:**
- *First-order (GP) branch.* Quantisation leaves the Bogoliubov dispersion intact. c_s = c holds only as k → 0. The spectrum is superluminal at k ≳ 1/ξ: unbounded in the continuum, up to 4.64c (C1) / 6.56c (C2) / 3.29c (C3) on the lattice. Commutators then have no strict light cone, only a lattice cone near v_max with superexponential tails. AZ7's own one-loop depletion (C_n α₀) would shift n₀, hence c_s, at O(α₀); the sources read do not compute its effect on c_s.
- *Second-order branch.* c_s = c survives exactly in the continuum. On the lattice, c is the k → 0 supremum, with a Planck-suppressed, direction-dependent subluminal correction: ω² = c²k²[1 + c₄(ka)²], c₄ ∈ [−1/18, −1/24], i.e. v_g = c[1 + (3/2)c₄(ka)²].
- *Either branch.* Pilot-wave guidance is instantaneous in the lattice frame. At equilibrium it cannot signal, so c_s = c survives operationally. Out of equilibrium (Valentini), instantaneous signals violate the c-cone outright.

---

## 10. Side findings recorded for the corpus (not part of the verdict)

1. **Exact lattice linearity is false.** App E.0 §3.1's conjecture is false on the nearest-neighbour lattice (quartic −1/24 … −1/18) and impossible on any finite-range lattice. Letter 129's ω² = c²k² holds only as k → 0.
2. **Letter 73's superluminal correction disappears on the lattice.** The +α₀(kℓ_P)² term is outweighed by the lattice's own quartic, so GW group velocity is ≤ c on the lattice (it would need β > 1/24 to exceed c).
3. **Three ξ conventions coexist** (AZ6/AZ7; L64 equation; L64 text), differing by factors √2 and 2.
4. **The z = 8 laws (γ(k), Bose–Hubbard) are anisotropic at O(k²)** at c/a = √2 (c_s(z)/c_s(x) = √2) and run at ~0.01c. The 12-neighbour graph is isotropic.
5. **KA2's citation is wrong.** KA2 cites Letter 59 for 6.78c, and Letter 59 contains no "6.78". App JH and L36 call 6.78c a non-signalling phase velocity, which KA2 then uses as a propagation speed.
6. **App J's Higgs gap is off by a factor of 2.** Its written action gives an amplitude-mode mass Ψ₀/ξ; App J prints 2/ξ.
7. **Hopf-charge normalisation differs** between L64 (1/4π²) and L254 (1/16π²).

---

## 11. 🦜 Baby-speak

Imagine the vacuum is a huge trampoline made of tiny balls. The question was: can a wobble at one end ever "know" what you did at the far end faster than light, in the special way quantum twins do? BCT writes down two different rules for how the trampoline wobbles, and never says which is the real one. With the "wave" rule, nothing ever moves faster than light. With the "Schrödinger" rule, little ripples can outrun light — on the ball-lattice they top out around 3 to 6.5 times light speed — but that is just an ordinary message being sent. It fades with distance, it would let you send real signals, and experiments already show quantum twins agree at least 10,000 times faster than light. The other idea in the corpus — "the twins share one knot tied when they were born" — is exactly the kind of shared secret that John Bell proved can never beat the score of 2, and the quantum score is 2.83. The only way BCT gets to 2.83 is by borrowing ordinary quantum mechanics and putting it on top: the lattice gives it a floor to stand on and a smallest step, but nothing about the balls' shapes creates the quantum twins. That is the "import" verdict — an honest null, logged as a finding.
