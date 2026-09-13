# GATE RANK — RESULT
## Scalar or vector? What is the BCT field? — Cold Ledger gate, executed 13 September 2026

**Model.** Claude Fable 5.1. The thread header initially said "Claude Opus 5"; the author corrected this in-thread on 13 September 2026. Claude Fable 5.1 is the model that executed every step of this gate.

---

## §1 — HANDOFF AND DIGESTS

| item | value |
|---|---|
| Gate file | `audit/gates/gate_RANK_prompt.md` at commit `aa709432f55b5424435551ceafea93398776439e`, fetched by `curl` to disk |
| Pre-registered SHA-256 | `72865268c30c1a06d9dac94c46a0d958b27a46fcac27b1e8d3a94d05e8e698e4` (8043 bytes) |
| Computed SHA-256 (before reading) | `72865268c30c1a06d9dac94c46a0d958b27a46fcac27b1e8d3a94d05e8e698e4` (8043 bytes) — **MATCH** |
| Corpus tarball | `codeload.github.com/…/tar.gz/aa709432…` |
| Pinned corpus SHA-256 | `3729ad1fea39d94a0555c698cef2ad7a3a6c8b7cbc4259dff162400af5546f07` (45,461,432 bytes) |

The gate file was not opened until the digest was computed and matched.

**Handoff note (author correction, 13 Sep 2026).** The author reports that a handoff header for this gate was mis-composed with Gate MP's digest against the RANK URL, and confirms the correct pre-registration is the digest above. In *this* thread the header already carried `72865268…` (8043 bytes, commit aa709432); it matched on first fetch and **no halt occurred** — the gate ran end to end. Both the pre-registered and computed digests are identical and are recorded above.

## §0.5 — SEARCH-SPACE COVERAGE (reported before any conclusion)

| item | gate §0.5 says | found at this commit |
|---|---|---|
| `.tex` files | 134; 26 at root | **134; 26 at root** ✓ |
| Appendices Vol 1 Parts 1, 2 | "raw UTF-8 text despite .pdf extension" | **Real PDFs** (`file`: PDF 1.7, 425 + 425 pages). Read with pymupdf. 133,330 + 112,079 words. 0 low-text pages. |
| Appendices Vol 1 Part 3 | "ZIP of page images with .txt layers" | **Real 25-page PDF**, text layer present, 6,282 words. |
| Appendices Vol 2 | .zip → 18 MB PDF, 582 pp, 151,710 words | ✓ zip → PDF, **582 pages**, 160,381 words by pymupdf count. 0 low-text pages. |
| `audit/APPENDIX_INDEX.md` | "maps all 245 appendices" | **Does not exist anywhere in the tree.** Citations below are by volume + page + extracted-text line. |
| Other PDFs | — | `BCT_NPB_Paper_v1.pdf` (5 pp), five `BCT_SMOKE_*.pdf` (1–8 pp), all text-extracted. |
| Page-level coverage | — | Every page of every PDF yielded text; no OCR needed. |

Three §0.5 statements are wrong for this commit (file types of Vol 1 Parts 1–3; existence of `APPENDIX_INDEX.md`). Recorded as a prompt defect on the search-space description; it did not affect coverage.

Search method: `search.sh` (pattern counts across all `.tex`/`.md`/`.html` + extracted PDF text, quarantined paths excluded) followed by `step0_enum.py` (533 line hits with file/page/line, filed as `gate_RANK_step0_hits.txt`), then manual reading of every hit that names a field, an action, a mode count, a point group, or a coordination number.

---

## §VERDICT — **SC-RANK-3: the corpus does not determine the field content. Halt.**

**But the halt is asymmetric, and the asymmetry is the finding (gate §1):**

- **Every written action or Hamiltonian in the corpus is for a one-component compact scalar** (θ ∈ S¹, or the phase of a complex GP scalar Ψ). Four independent documents write it down.
- **Every vector commitment is prose-only.** No document writes an elastic energy, a rotor Hamiltonian, or a 3×3 dynamical matrix. The one document that says "the dynamical matrix is a 3×3 matrix" (HO5) then performs a scalar calculation.
- The corpus's central published number, α = α₀(1−2α₀), the photon's two polarisations, the "transverse-traceless" graviton, and "transverse" gravitational waves **all require the vector content the written actions do not contain.**
- The exclusion theorem (HO5) does **not** exclude the vector field. Re-derived, its central number is the scalar-field result; applied to a vector field it would exclude c/a = √2 itself.

So: by written dynamics, BCT is a scalar theory (SC-RANK-1 would hold on that reading); by the claims that make it a theory of light and gravity, it is a vector theory with no dynamics written. Both readings are live in the corpus and are not reconciled anywhere. That is SC-RANK-3. What would settle it is stated in §9.

---

## §2 — STEP 0: ENUMERATION OF FIELD-CONTENT COMMITMENTS

### Group A — commitments with a WRITTEN action or Hamiltonian

| # | location | quoted | rank | components/site | action written? | target | tier assigned by own document |
|---|---|---|---|---|---|---|---|
| A1 | Vol 1 Pt 1, **p. 33**, L2402–2410 (Appendix D.2) | "H_lattice = −J ∑_{<i,j>} cos(θ_i − θ_j) where θ_i is the rotation angle of sphere i … This is the standard quantum XY model, whose spin-wave modes (phonons/magnons) are the BCT photons." | scalar | **1** | **Yes** (Hamiltonian) | S¹ | none stated; presented as "established in Appendix H of the main paper" (see phantom note below) |
| A2 | Vol 1 Pt 1, **p. 47**, L3011–3021 | "L_BCT = (J/2)[(1/c²)(dθ/dt)² − \|∇θ\|²] + λ cos(θ) where θ(x,t) is the rotation angle field of the BCT sphere … This is the massless scalar field Lagrangian — a good starting point, but photons are vector fields, not scalars. The vector structure must emerge from the topology." | scalar | 1 | **Yes** (Lagrangian) | S¹ (called "a PHASE — it lives on a circle (U(1))", L3023) | document frames itself as "what must be derived" — not DERIVED |
| A3 | Vol 1 Pt 1, **p. 52**, L3222–3245 (Appendix E.1) | "The BCT phase field θ(x,t) — the rotation angle of the sphere lattice — is a compact (U(1)-valued) scalar field … L_BCT = (ρ_s/2) η^μν (∂_μθ)(∂_νθ) … This is the massless scalar field Lagrangian." | scalar | 1 | **Yes** | S¹ (θ ∼ θ+2π, §1.2) | claims "ALL FOUR MAXWELL EQUATIONS are derived" (p. 57) — self-assigned DERIVED |
| A4 | `tex/BCT_Appendix_AZ6.tex` L197–210 | "S_SF^(2) = ∫d⁴x[−δρ²/(2c_s²ρ₀) + ρ₀(−(∂_tδθ)²/c_s² + \|∇δθ\|²)] … This is the action for a scalar field φ = ρ₀δθ/c_s propagating in the acoustic metric" | scalar | 1 (phase) + 1 (density, non-propagating after elimination) | **Yes** (superfluid action) | S¹ phase of Ψ | acoustic-metric derivation, presented as derived |
| A5 | `tex/BCT_Letter27_GPAxiom.tex` L42, L124–134; `tex/BCT_Appendix_AZ7.tex` | "the QCD vacuum is described by a Gross-Pitaevskii (GP) order parameter Ψ with a \|Ψ\|⁴ potential … Ψ ∈ A₁ ⟺ Ψ is a spin-0 scalar." | complex scalar | 2 real (amplitude + phase); phase sector = A1–A3 | **Yes** (GP functional, Bose–Hubbard H with z = 8) | ℂ; Goldstone sector S¹ | "elevate the GP axiom to a theorem" — self-assigned DERIVED (from C₄ᵥ) |
| A6 | `tex/BCT_Appendix_JH*.tex` L125–200 | exterior condensate Ψ_ext (GP, eq:GP); "Ψ_int : B³ → ℂ², the two-component interior condensate field … maps S³ → S² and is classified by π₃(S²) = ℤ" | complex scalar (exterior) + ℂ² doublet (interior of each sphere) | exterior 2 real; interior 4 real, constrained \|Ψ_int\|² = ρ₀ → 3 | **Yes** (GP equation + interior free energy) | ℂ / S³→S² | computed |

Note on A6: the ℂ² interior field lives inside each Planck sphere, not on the lattice; the propagating lattice field in JH is the exterior scalar Ψ_ext (Letter 73: "The exterior condensate Ψ₁ propagates at speed c (the Goldstone mode)"). It is therefore recorded as internal structure of the scalar branch, not as a third lattice field content. SC-RANK-4 is **not** triggered on this reading; if a future gate wishes to count it as a distinct field content, SC-RANK-4 would have to be revisited.

**Phantom origin.** A1, A2, A3 all attribute the XY Hamiltonian to "Appendix H of the main paper". Vol 1's Appendix H ("The Lattice of Resonance — Draft", p. 105 ff.) mentions "the XY model" once (L5332) and contains no Hamiltonian. `BCT_Monograph_PLB.tex` contains no XY Hamiltonian. The first written form in the corpus is Appendix D.2 itself.

### Group B — commitments in PROSE ONLY (no action, no Hamiltonian, no dynamical matrix written)

| # | location | quoted | rank | components/site | action written? | target | tier by own document |
|---|---|---|---|---|---|---|---|
| B1 | Vol 1 Pt 1, **p. 36**, L2535–2551 (Appendix D.4.4) | "these correspond to the two independent transverse rotation modes of the spheres — rotations about the two axes perpendicular to the propagation direction. The octahedral void has O_h point-group symmetry. Under O_h, the T1u irreducible representation (which transforms as a vector, i.e., like a photon field) is triply degenerate. For propagation along the c-axis, exactly two of the three T1u modes are transverse." | vector (rotation vector) | **3** | **No** — and contradicted by A1 three pages earlier, which gives each sphere one angle | SO(3) (implied) | "This is not an assumption — it follows from the O_h symmetry" — self-assigned DERIVED |
| B2 | `tex/BCT_Monograph_PLB.tex` L1525–1533 | "The electromagnetic field is identified with the irrotational (longitudinal) phonon mode of the octahedral void condensate … the inhomogeneous equations arise from the Euler–Lagrange equations of the octahedral void displacement field." | vector (displacement) | 3 | **No** (Euler–Lagrange equations invoked, none written) | ℝ³ | asserted |
| B3 | `tex/BCT_Monograph_PLB.tex` L1554–1556 | "The spin-2 graviton is identified with the transverse-traceless phonon mode of the lattice displacement field." | vector (displacement) | 3 | No | ℝ³ | asserted |
| B4 | Vol 2, **p. 56–57** (Appendix HO5 §2.2) | "For a BCT crystal with nearest-neighbour spring constant K, the dynamical matrix is: D(k) = (K/m) × M(k) where M(k) is a 3×3 matrix" | vector (displacement) | 3 | **No** — M(k) is named, never written; the arithmetic that follows is one-component (see §5) | ℝ³ | "proven" |
| B5 | `tex/BCT_Letter73_GravitationalWaves.tex` L57–61, L77–80 | "Gravitational waves are transverse oscillations of this condensate [Ψ₁], identical to GR tensor modes at leading order … Beyond the two standard GR tensor polarisations (h₊ and h×), BCT predicts a third polarisation mode: an isotropic scalar 'breathing' mode" | vector/tensor modes attributed to a scalar Ψ₁ | 3+ | No | — | prediction (asserted) |
| B6 | `tex/BCT_Letter128_ChainOfNecessity.tex` L438–443 | "phonons in a BCT lattice propagate with speed c_s(k̂) = c_s^(0)√A(k̂) … Isotropy (A = const) … This is a result of linear algebra applied to the BCT dispersion relation." (attributed to "Letter 18") | unspecified | — | No; "Letter 18" not in corpus | — | "Proven in Letter 18" |
| B7 | Vol 1 Pt 1, **p. 15**, L1620–1626 | "The model requires an anisotropic lattice (to distinguish the c-axis from the basal plane, explaining the difference between longitudinal/gravitational and transverse/electromagnetic wave propagation). This rules out BCC (c/a = 1), which is perfectly isotropic." | vector (L and T modes assigned to different forces) | 3 | No | — | asserted |
| B8 | `tex/BCT_Monograph_PLB.tex` L120–124 | "the long-wavelength excitations of the superfluid are phonons that propagate isotropically … these phonons are identified with the gauge bosons of the Standard Model" | unspecified | — | No | — | hypothesis |

**The asymmetry:** Group A (written dynamics) is entirely scalar; Group B (prose) is entirely vector. No document writes a vector action. No document that writes an action claims more than one component per site.

### Internal contradictions found in enumeration (not just between documents — within them)

1. **Appendix D, pp. 33 vs 36:** one angle per sphere (A1) → "two independent transverse rotation modes … about the two axes perpendicular to propagation" (B1). The written Hamiltonian has no such modes.
2. **Monograph L1525–1533 vs Vol 1 p. 36:** EM is the **longitudinal** (irrotational) phonon (B2) vs EM has **two transverse** polarisations (B1). An irrotational field is a gradient of a scalar and has no transverse modes.
3. **Vol 1 p. 15 vs HO5 (Vol 2 p. 56):** the model "requires an anisotropic lattice" at c/a = √2 (B7) vs "c/a = √2 is the UNIQUE value for which the long-wavelength phonon spectrum is acoustically isotropic" (HO5). Vol 1 p. 15 itself notes the c/a = √2 lattice "is geometrically identical to the FCC structure" and then calls it "anisotropy-capable"; FCC is cubic.
4. **Three point groups for one lattice:** D₄h (HO5, Monograph L225), C₄ᵥ (Letter 27 §III), O_h (Appendix D.4.4). At c/a = √2 the lattice is FCC and its point group is O_h; C₄ᵥ is not the point group of any Bravais lattice (no inversion).
5. **Letter 73:** a scalar Goldstone mode Ψ₁ is said to have "transverse oscillations … identical to GR tensor modes".

---

## §3 — STEP 1: RECONCILIATION ATTEMPTED, THEN THE SEPARATING INVARIANT

### Steelman

**(a) Vector with two components frozen.** Freezing two components of u ∈ ℝ³ leaves a field valued in ℝ, not S¹. A non-compact scalar has no vortices (π₁(ℝ) = 0). Appendix E itself says so: "a non-compact scalar field would give only a massless scalar boson, not electromagnetism" (p. 53, L3264). So this reconciliation destroys the vortex-matter identification. Rejected.

**(b) Scalar as one component of a vector — the longitudinal sector.** The Monograph's "irrotational (longitudinal) phonon" is u = ∇φ: one degree of freedom, a non-compact scalar, and by construction it has zero transverse polarisations. This reconciles B2 with Group A but is incompatible with B1 (two transverse polarisations) and with the factor 2 in α. Rejected as a reconciliation of the whole; it does reconcile B2 alone.

**(c) Rotor field SO(3) with a scalar sector.** Take each sphere's orientation R_i ∈ SO(3) and restrict to rotations about the c-axis: θ_i ∈ SO(2) ≅ S¹. This is the *only* reading that makes "the rotation angle of sphere i" both compact and one-component, and it is consistent with Letter 27's use of C₄ᵥ (a fixed axis). But: (i) it breaks O_h to C₄, so Appendix D.4.4's O_h/T₁ᵤ argument is unavailable; (ii) the full rotor has π₁(SO(3)) = ℤ₂ — a 4π winding is contractible — so integer vortex charge (Appendix E: "2π winding of the phase field θ around the vortex core") is not topologically protected unless the two transverse rotations are dynamically frozen, which returns us to the scalar. Partial reconciliation only; it makes the scalar reading coherent and the vector reading unavailable.

**(d) Anisotropic elasticity with transverse modes identified as photons, longitudinal as graviton (B7).** This is the one reading on which a single vector field carries both EM and gravity. It requires anisotropy at c/a = √2 (B7) and is therefore incompatible with HO5 and with the emergent-Lorentz argument (§5). It also fails the helicity test (§6): longitudinal phonons have helicity 0, not ±2.

No reconciliation dissolves the conflict cheaply. The two readings are genuinely distinct.

### The separating invariants (three, all notation-independent)

**(i) Degree-of-freedom count per site.** Group A: 1 real (θ) [or 2 with the GP amplitude, of which 1 propagates]. Group B: 3 real. Verified by constructing both Hamiltonians (`rank_dispersion.py`): the scalar dynamical matrix is 1×1, the vector one is 3×3 with three acoustic branches.

**(ii) Transformation under the point group.** At c/a = √2 the lattice is FCC; the correct point group is **O_h** (HO5's D₄h is the generic-c/a group; Appendix D's O_h is right for the void *and* the lattice at √2). Scalar θ: **A₁g** (one-dimensional). Vector u: **T₁ᵤ** (three-dimensional). Under the generic-c/a group D₄h: A₁g vs A₂ᵤ ⊕ Eᵤ. Under Letter 27's C₄ᵥ: A₁ vs A₁ ⊕ E. In every group the scalar is one-dimensional and the vector is not; no relabelling maps one into the other.

**(iii) Homotopy of the target.** S¹: π₁ = ℤ — integer-charged vortex lines exist and are stable. ℝ³ (displacement): π₁ = 0 — no line defects; "matter = vortex" is impossible. SO(3) (rotor): π₁ = ℤ₂ — only one non-trivial line defect class; no ℤ charge quantisation. This is the invariant that makes the choice consequential: **only the compact scalar supports the vortex identification of matter that the whole programme rests on.**

Computation for (i)–(ii) is in `rank_dispersion.py` (branch counts) and the character assignments above are standard: the trace of a rotation by φ on the scalar is 1, on the vector is 1 + 2cos φ; these differ for every φ ≠ 0, so the two representations are never isomorphic under any subgroup.

---

## §4 — STEP 2: WHAT EACH FIELD CONTENT DELIVERS (both columns worked)

Both columns computed on the BCT Bravais lattice a₁=(a,0,0), a₂=(0,a,0), a₃=(a/2,a/2,c/2), nearest-neighbour couplings, harmonic order, from `rank_dispersion.py`. J = K = m = a = 1.

| property | **SCALAR** θ ∈ S¹, H = (J/2)Σ(θᵢ−θⱼ)² | **VECTOR** u ∈ ℝ³, central springs K |
|---|---|---|
| Hamiltonian used | written in corpus (A1) | **constructed here** (none in corpus): D_ab(k) = (2K/m)Σ_b(1−cos k·d_b) d̂_a d̂_b |
| Propagating dof per site | **1** | **3** |
| Acoustic branches | 1 | 3 (1 L + 2 T) |
| Point group at c/a=√2 (FCC) | O_h; mode ∈ **A₁g** | O_h; modes ∈ **T₁ᵤ** |
| Point group at generic c/a | D₄h; A₁g | D₄h; A₂ᵤ ⊕ Eᵤ (L along c splits from the E-doublet) |
| Helicity in continuum limit | **0 only** | **0 (L), ±1 (T)**. No ±2. (`rank_helicity.py`: TT components of the strain of any k∥z plane wave vanish identically) |
| Long-wavelength velocity tensor, z=12 graph | diag(4a², 4a², 2c²) (J/m)/a² → v²(z)/v²(x) = **(c/a)²/2**; isotropic **iff c/a = √2**; at √2, v = √2 in *every* direction (rank-2 tensor + cubic ⇒ isotropic) | rank-4 tensor; at c/a = √2: v²_L = 1.00 (BCT-z = FCC[100]), 1.25 (BCT-x = FCC[110]), 1.333 (FCC[111]); v²_T = 0.5/0.5, 0.25/0.5, 0.333/0.333. **Anisotropic at √2**: v_T varies by √2, v_L by 15%. Longitudinal x/z equality would need c/a = 1.5175 (root of γ⁴−γ²−3=0); transverse x/z equality is never reached. |
| Long-wavelength velocity tensor, z=8 graph (body-centring bonds only) | diag(2a², 2a², 2c²) → isotropic **iff c/a = 1 (BCC)**; at √2, v(z)/v(x) = √2 (41% anisotropy) | at √2: v_L² 0.5 (x) vs 1.0 (z); a **zero-frequency shear mode** along [110]_BCT (graph is mechanically floppy); at c/a=1 also floppy |
| Anisotropy beyond leading order at √2, z=12 | present at O(k⁴): ω²/k² along x vs z = 1.8987 vs 1.9180 at \|k\| = a⁻¹ (cubic harmonic k_x⁴+k_y⁴+k_z⁴). HO5 §4.1's "exact at all orders" is false. | present already at O(k²) (above) |
| Vortex lines (π₁) | ℤ — yes | 0 — none (ℝ³); ℤ₂ only if rotor |
| Gauge field | A_μ = ∂_μθ/e is pure gauge on smooth configurations (Appendix E L3334: L → (ρ_s e²/2)A_μA^μ, a **mass term**, not a Maxwell term); F_μν ≠ 0 only on vortex worldsheets. **No propagating transverse photon.** | two transverse phonons available as helicity-±1 carriers, but they are not gauge fields (no gauge redundancy; a longitudinal massless mode remains) |
| What the branch can deliver | one massless helicity-0 mode; vortex matter with ℤ charge; isotropic sound at √2 (z=12) | three massless modes, helicities 0, ±1; no vortex matter; anisotropic sound at √2; no helicity ±2 |

---

## §5 — STEP 3: THE EXCLUSION THEOREM, RE-DERIVED

**Located.** Appendix HO5, Vol 2 pp. 56–58 ("The BCT Lorentz Invariance Uniqueness Theorem, Phase 67C, February 2026"). Restated in `BCT_Monograph_PLB.tex` L233–296 (eq. `isotropy`), `BCT_Letter128` L92–105 and L437–444 (attributed to "Letter 18"), `BCT_Letter88` L155–157 (attributed to "Letter 1"), `BCT_Volume1_Foundations.tex` L69, L143, L170–172. Letters 18 and 1 are **not in the corpus**; HO5 is the only proof.

**Quoted (Vol 2 p. 56–57):**
> "Among all BCT crystals with nearest-neighbour interactions, the axial ratio c/a = √2 is the UNIQUE value for which the long-wavelength phonon spectrum is acoustically isotropic. At c/a = √2: v_sound(z) = v_sound(x) = v_sound(y) [isotropic] … For a BCT crystal with nearest-neighbour spring constant K, the dynamical matrix is: D(k) = (K/m) × M(k) where M(k) is a 3×3 matrix … v_s²(z)/v_s²(x) = K_z/K_x = γ²/2 = (c/a)²/2. Isotropy requires v_s(z) = v_s(x), which means: (c/a)²/2 = 1 ⟺ c/a = √2 QED"

**Premises, exactly:** (P1) BCT Bravais lattice with **12** nearest-neighbour bonds (4 in-plane at distance a, 8 body-centring at √(a²/2+c²/4)) — the **z = 12 graph**; (P2) equal spring constant K on all 12 bonds *for all c/a* (although the two bond classes have unequal length except at √2); (P3) "nearest-neighbour" central-force springs on a 3-component displacement; (P4) isotropy is tested **only between the x and z axes**.

**Independent re-derivation (`rank_dispersion.py`):**

*Scalar field on z=12:* long-wavelength ω² = (J/m)Σ_b (k·d_b)² over all 12 bonds = (J/m)[4a²(k_x²+k_y²) + 2c²k_z²]. Hence v²(z)/v²(x) = 2c²/4a² = **(c/a)²/2**. Isotropic iff c/a = √2, and then isotropic in all directions at O(k²) because a symmetric rank-2 tensor invariant under O_h is a multiple of the identity. **HO5's printed number is reproduced exactly — for the scalar field.**

*Vector field on z=12:* v²_L(z)/v²_L(x) = C_zzzz/C_xxxx = [2γ⁴/(2+γ²)] / [2 + 2/(2+γ²)] = **γ⁴/(3+γ²)**, which is **0.8 at γ = √2**, not 1, and equals 1 at γ = 1.5175. The transverse ratio v²_T,min(z)/v²_T,min(x) = 2 at √2. At c/a = √2 the model is the FCC nearest-neighbour central-force crystal with C₁₁ = 2C₁₂ = 2C₄₄ (Cauchy), Zener anisotropy A = 2C₄₄/(C₁₁−C₁₂) = 2. It is not isotropic and no c/a makes it so. **HO5's number is wrong for the vector field.** Its error: it projects each bond's K onto z and x with cos²θ and sin²θ, drops the in-plane bonds from the x-channel, and never forms the rank-4 elastic tensor; the resulting expression coincides with the scalar (rank-2) computation.

*Both fields on z=8 (the loop-counting graph):* scalar isotropy selects **c/a = 1 (BCC)**, the value Vol 1 p. 15 "rules out"; at √2 the scalar has v(z)/v(x) = √2. The vector on z=8 has a zero-frequency shear mode — the body-centring graph alone cannot hold the lattice rigid.

**Coordination-graph consistency (finding).** HO5 and the Monograph use z = 12 with in-plane bonds. Letter 27 (t/U, Mott boundary), AZ7, Letter 127 (NNLO "z = 8"), and the bipartite loop coefficient C_n = n(n−1)·3/2 of Letter 27 §II use z = 8 (body-centring bonds only, "bipartite"). The two arguments cannot share a coordination graph: the z=12 graph is not bipartite (in-plane bonds connect same-sublattice sites), and on the z=8 graph the isotropy theorem selects BCC. Elsewhere z = 6 (Vol 1 Pt 2 p. 161, p. 185, "octahedral coordination") and z = 12 "coordination number of the BCT lattice" (Letter 207 L84; Vol 1 Pt 1 p. 29 "z=12") also appear. **The corpus uses at least three coordination numbers for the same lattice, and the isotropy proof and the loop counting require different ones.**

**What the theorem excludes.** As printed, nothing about rank: it is a one-component computation presented as a three-component one. Correctly applied: it shows that **only the scalar field is acoustically isotropic at c/a = √2**, and only on z = 12. It therefore does not exclude the vector field by Lorentz invariance *in the corpus*; done correctly it would — a vector displacement field at c/a = √2 has direction-dependent sound speeds (up to 41% in the transverse branch) and cannot yield an emergent Lorentz-invariant theory with a single light speed. The theorem is thus narrower than cited (x-vs-z, harmonic, z=12) and, when widened, cuts against the vector reading rather than the scalar one. Its §4.1 all-orders claim is false in both branches (cubic k⁴ anisotropy survives at √2 for the scalar; O(k²) anisotropy for the vector).

---

## §6 — STEP 4: CONSEQUENCE MAP

| question | **if SCALAR** (Group A is the theory) | **if VECTOR** (Group B is the theory) |
|---|---|---|
| **Photon polarisation count** | 0 transverse. Appendix E (Vol 1 pp. 52–59) gets F_μν only from vortex singularities; on smooth configurations L_BCT = (ρ_se²/2)A_μA^μ (p. 54 L3335) — a Proca mass term with A pure gauge, not a Maxwell kinetic term. No propagating photon at all. Appendix D §4.4 (p. 36) fails. | 2 transverse helicity-±1 phonons available. Not gauge bosons; a third (longitudinal) massless mode remains and is not observed. Appendix D §4.4's O_h/T₁ᵤ count becomes coherent but its Hamiltonian must be rewritten. Monograph L1525 ("EM = irrotational longitudinal mode") fails. |
| **α = α₀(1−2α₀)** (Vol 1 pp. 32–39, Monograph, Letter 27, NPB paper) | the factor 2 is unavailable; the written Hamiltonian's one mode gives α₀(1−α₀) → 1/α = 135.996 (−0.76%) instead of 137.018 (−0.013%). The headline 0.013% agreement depends on a polarisation count the scalar cannot supply. | factor 2 available in principle; still requires the loop integral I_BCT = α₀ on a bipartite z=8 graph that the vector's isotropy needs to be z=12 (§5). |
| **Graviton** (Monograph L1554–1556 "TT phonon of the displacement field") | no candidate: helicity 0 only. Letter 20/AZ6 acoustic-metric route gives a *scalar* wave equation in an effective metric (a valid analogue-gravity statement), not a spin-2 field. | **also fails**: `rank_helicity.py` — no plane-wave mode of a 3-component displacement field has TT (helicity ±2) strain. "Transverse-traceless phonon mode" does not exist in any elastic solid with a displacement field alone. Would need a genuinely tensor (6-component) field. |
| **Emergent-Lorentz argument** (HO5; Monograph §uniqueness; L128 Step 1; L88 constraint iii; Vol1 Foundations) | **survives at harmonic order on z=12**, with the printed number correct; fails at O(k⁴) (cubic anisotropy), and fails on z=8. | **fails at c/a = √2**: v_T varies by √2 with direction, v_L by 15%. The chain "Lorentz ⇒ √2 ⇒ D4 ⇒ …" (L128) has no first link. |
| **Matter = vortices** (Appendix D.3, E §2–3, Monograph §Dirac, Letter 64/68) | **survives**: π₁(S¹) = ℤ, integer winding, vortex lines. | **fails**: π₁(ℝ³) = 0; no vortex lines. (SO(3) rotor: ℤ₂ only — no integer charge.) |
| **Vol 1 p. 15 (anisotropy required at √2; BCC ruled out)** | fails: scalar is isotropic at √2 on z=12, and on z=8 isotropy *selects* BCC | coherent with the vector's anisotropy at √2 but then contradicts HO5 |
| **Letter 73 GW predictions** (breathing mode h_s/h_t = α₀/v_ph² = 1.61×10⁻⁴; topological memory) | no tensor modes to be "beyond"; the breathing mode is the only mode | tensor modes still absent (no helicity ±2); prediction ill-posed in both branches |
| **Letter 20 "purely tensor polarisation … non-trivial consistency check"** | no tensor modes exist; the "check" is empty | same |
| **Weinberg angle, PMNS, quark masses, Λ_QCD** (Monograph Parts II–IV) | do not invoke a polarisation count; unaffected **by this gate** (other gates govern them). They do inherit the α₀ input; if the α correction factor changes, anything using α (not α₀) shifts. | same |
| **Letter 27 GP-axiom "theorem"** | consistent (scalar), but its C₄ᵥ is not the lattice point group and its z=8 graph contradicts HO5 | fails outright (A₁ is one-dimensional) |

---

## §7 — CN-RANK NOTICES (tiered; revised clause by clause)

**CN-RANK-01 — PROVEN (by enumeration of the pinned corpus).** Every action or Hamiltonian written in the corpus for the lattice field is for a one-component compact scalar (Vol 1 Pt 1 pp. 33, 47, 52; AZ6 L197–210; Letter 27/AZ7 GP functional; JH exterior GP). No document writes an action, Hamiltonian, or dynamical matrix for a three-component field. Every vector commitment (Monograph L1525–1533, L1554–1556; Vol 1 p. 36 §4.4; HO5 §2.2; Letter 73; Vol 1 p. 15) is prose.

**CN-RANK-02 — PROVEN (computation, `rank_dispersion.py`).** The number printed in Appendix HO5, v²(z)/v²(x) = (c/a)²/2, is the long-wavelength result for a **scalar** phase field with equal nearest-neighbour coupling on the 12-bond graph. For a three-component displacement field with 12 equal central springs the longitudinal ratio is γ⁴/(3+γ²) = 0.8 at c/a = √2, and the transverse branches are anisotropic by a factor 2 in v². HO5 does not compute what it says it computes.

**CN-RANK-03 — PROVEN (computation).** A displacement field at c/a = √2 is the FCC nearest-neighbour central-force crystal (Cauchy relations, Zener A = 2) and is not acoustically isotropic in any direction pairing except those related by cubic symmetry. The emergent-Lorentz argument holds at harmonic order **only in the scalar branch and only on the z = 12 graph**.

**CN-RANK-04 — PROVEN (computation).** On the z = 8 body-centring graph used by Letter 27, AZ7 and Letter 127, scalar isotropy selects c/a = 1 (BCC), and at c/a = √2 the sound speed along c exceeds that along a by √2. The isotropy theorem and the loop-counting arguments require different coordination graphs; the z=12 graph is not bipartite.

**CN-RANK-05 — PROVEN (Appendix D internal).** The factor 2 in α = α₀(1−2α₀) (Vol 1 p. 36) is derived from "two independent transverse rotation modes" of a T₁ᵤ vector, while the Hamiltonian from which the same appendix says it derives α (p. 33) assigns each sphere a single angle. Under the written Hamiltonian the correction is (1−α₀), giving 1/α = 135.996 (−0.76%).

**CN-RANK-06 — PROVEN (computation, `rank_helicity.py`).** No mode of a three-component displacement field carries helicity ±2; the "transverse-traceless phonon mode of the lattice displacement field" (Monograph L1556) does not exist in either branch. The graviton identification fails independently of the rank verdict.

**CN-RANK-07 — PROVEN (homotopy).** The vortex identification of matter (π₁ = ℤ) is available only for the S¹-valued scalar. A displacement field admits no line defects; a rotor field admits only ℤ₂ defects.

**CN-RANK-08 — ASSERTED (by the corpus; contradicted).** Vol 1 p. 15's requirement of anisotropy at c/a = √2 to separate "longitudinal/gravitational" from "transverse/electromagnetic" propagation is incompatible with HO5's isotropy at the same c/a and with the FCC identity the same page states.

**CN-RANK-09 — ASSERTED (by the corpus; unsupported).** HO5 §4.1's claim that isotropy is "exact at all orders in the long-wavelength expansion" is false for the scalar (cubic k⁴ term, computed) and for the vector (O(k²) anisotropy, computed).

**CN-RANK-10 — CONJECTURE (this gate's reading of intent).** The most coherent single reading of the corpus is the rotor-restricted scalar (c-axis rotation angle per sphere, target SO(2) ≅ S¹). It makes Group A, the vortex identification, and Letter 27's fixed-axis C₄ᵥ mutually consistent, at the cost of every two-polarisation and every graviton claim. Whether the programme accepts that cost is a decision, not a finding.

**CN-RANK-11 — ASSERTED (phantom references).** "Appendix H of the main paper" (origin of the XY Hamiltonian), "Letter 18" (origin of the uniqueness theorem) and "Letter 1: Emergent Lorentz Invariance" are cited as proofs and are absent from the corpus at this commit.

---

## §8 — CONTAMINATION STATEMENT

- The gate file was fetched and digest-verified before reading. Corpus fetched by tarball, digest recorded.
- **Auto-loaded context declared:** the session's memory listing displayed one-line descriptions for `/projects/…/audit-findings.md` ("Cold Ledger audit results — closed sectors by proof, what survives, active correction ledger, and open problems in priority order"), `overview.md` ("…current audit state (Cold Ledger, Aug–Sep 2026)") and `ways-of-working.md` ("Cold Ledger protocol…"), plus non-project files (`/areas/bct-programme.md` etc.). **None of their contents were read.** The project-files panel also listed `claude_Gate_C1_Result___Interior_Healing_Length.md` and `claude_Gate_Session_Prompts.md` and several BCT PDFs at `/mnt/project/`; none were opened. Fourteen documents were attached to the message with **empty** content blocks; nothing was read from them.
- `conversation_search` and `recent_chats` were not called. `audit/notes/`, `audit/gates/LINK/`, `audit/gates/C1/` were not read (LINK and C1 do not exist at this commit). `audit/gates/PSI2/*`, `audit/gates/crossaudits/*`, `audit/gates/INT/`, `audit/gates/TANH/` were listed by name only and not read. Other gate prompt files were excluded from the enumeration script.
- **§0.3:** no prior finding about rank, degree-of-freedom counts, or a "Superfluid Necessity Theorem" reached this session. The phrase "Superfluid Necessity" occurs nowhere in the corpus (searched all text); the theorem the gate refers to was identified from primary source as HO5. The derivation in §§3–6 preceded any reading of `audit/NEXT.md`, which was opened only afterwards to append the RANK entry.
- `audit/NEXT.md` was read **after** §§1–9 were written, to append the RANK entry. It contains one-line verdicts for PSI2 ("Psi_2 supplies no second A1g Goldstone"), TANH ("alpha_0 and g are distinct objects") and INT ("three distinct interior commitments"). These are declared as seen; they postdate the derivation and did not alter it. NEXT.md's standing rule that "2 are raw text" refers to the *mount* files, which explains the §0.5 defect: the gate carried the mount typing over to the tarball.
- **Handoff composition:** the author states the initial handoff for this gate was mis-composed (Gate MP's digest on Gate RANK's URL) and that a halt on that mismatch was correct. That mismatch did not reach this thread: the header received here carried the correct RANK digest and the check passed. Recorded so the ledger shows one pre-registration for RANK, verified once, with no second version of the prompt in play.
- Web search was not used.

## §0.6 — REPRODUCED VERBATIM

> Fixing the field content does **not** supply a photon, a graviton, or any prediction. A vector field would make two transverse polarisations *available*; it would not make them *derived*, and it would not by itself repair any mechanism a gate has already closed. A scalar field would settle several open counts at once, but downward. **What this gate buys is the single most upstream fact about the theory: how many components its field has.** Every degree-of-freedom dispute in the programme reduces to it. A verdict here is a precondition for other work, not a result about physics.

## §9 — WHAT WOULD SETTLE IT, AND WHAT THIS GATE DID NOT ESTABLISH

**What would settle SC-RANK-3.** One document, tiered by the programme, that (a) states the target space of the lattice field (S¹, ℝ³, or SO(3)); (b) writes its harmonic action on a **named** coordination graph; (c) diagonalises the dynamical matrix and reports the branch count and directional speeds at c/a = √2; and (d) either retracts the two-polarisation and TT-graviton claims (scalar) or retracts the vortex-matter identification and the emergent-Lorentz theorem (vector). Until (a)–(c) exist the question is a decision awaiting the author, not a fact awaiting discovery.

**Not established by this gate.**
- Whether any field content yields a photon or a graviton (§0.6 forbids the inference; §6 shows neither branch does as written).
- The correctness of any downstream number not invoking a polarisation count (Weinberg angle, masses, Λ_QCD, PMNS) — outside scope.
- Whether the ℂ² interior condensate of Appendix JH should be counted as a third lattice field content (recorded as sub-structure of the scalar branch; SC-RANK-4 not invoked).
- Whether the loop integral I_BCT = α₀ is correct on any graph — only that its graph (z=8) and the isotropy theorem's graph (z=12) differ.
- Anything about the anharmonic or nonlinear sector beyond the single k⁴ check.
- Whether "Letter 18", "Letter 1", or "Appendix H of the main paper" exist outside this commit.

## §10 — SCRIPTS (filed in `audit/gates/RANK/`)

- `search.sh` — corpus-wide pattern counts (quarantine-aware).
- `step0_enum.py` — Step-0 enumeration; output `gate_RANK_step0_hits.txt` (533 hits with file/page/line).
- `rank_dispersion.py` — scalar and vector dynamical matrices on z=12 and z=8 graphs; directional speeds; HO5 number re-derived; k⁴ check; FCC elastic branches.
- `rank_helicity.py` — helicity decomposition of displacement-field plane waves.
- `gate_RANK_prompt_asrun.md` — byte-identical copy of the verified gate file.

Reproduction: `python3 rank_dispersion.py && python3 rank_helicity.py` (numpy only).

*Executed 13 September 2026 against commit aa709432. Halt under SC-RANK-3.*
