# NEXT — what is queued, running, and closed

Last updated 14 September 2026 (ledger reconciliation; Gate RATIO closed). **Update this file at the close of every session.**
It exists because sessions have independently invented their own gate order, and
one spent a turn treating a committed prompt as a mystery file.

## The goal, as currently stated
Unification is the long aim. The working target is **any two of QM, GR, EM**.
Current reading: GR carries a representation obstruction the corpus states itself
(Letter 260's rank ladder, Gate N, Gate G'), so the reachable pair is **QM + EM**.
Gates MAD and LINK below test exactly that pair. This reading is a judgement, not
a result, and either gate may overturn it.

## Closed
| gate | run | verdict | deliverable |
|---|---|---|---|
| PSI2 | — | closed on SC-PSI2-2/4/5; Psi_2 supplies no second A1g Goldstone | `gates/PSI2/` |
| TANH | — | SC-TANH-3: alpha_0 and g are distinct objects, App J S3.1 conflates them. 0 published predictions moved | **MISSING** |
| INT | — | SC-INT-4: three distinct interior commitments, re-scoped to enumeration | **MISSING** |
| LAM, LAMBDA | — | run elsewhere; cross-audited from the PSI2 thread | `gates/crossaudits/` |
| C1 | 12 Sep | SC-C1-3: the interior healing length ξ₂ is not determined by the corpus; halt and report. SC-C1-4 not triggered at Step 0; SC-C1-5 triggered in part (symbol ξ overloaded) without blocking. §3 delivered both ways. | `gates/C1/` |
| RANK | 13 Sep | SC-RANK-3: the corpus does not determine the field content; halt. By written dynamics BCT is a scalar theory; by its claims about light and gravity it is a vector theory with no dynamics written. Both readings live. | `gates/RANK/` |
| MP | 13 Sep | SC-MP-1 (qualified: HF4's m_P = M_R/α₀² is an identity on GG2's M_R = m_P·α₀²; the −0.08% is input rounding) + SC-MP-3 (input set, M_R, G_BCT all inconsistent across documents). Scale a = ℓ_P is assumed and declared. JB6 and L128 "derivations" of m_P are inverted fits, not circular. 12 notices. | `gates/MP/` |
| PRED | 13 Sep | SC-PRED-1: observed matches are within chance expectation; 39/40 closed forms reproduce; 28 eligible sub-1% vs E≈100–130 by construction; best single item 1/α ≈ 6 bits; m_P = M_R/α₀² circular (CN-PRED-01); "92" not reconstructible (CN-PRED-02). Prompt as run: `7e7675da…` (see `gates/PRED/gate_PRED_prompt_asrun.md`). | `gates/PRED/` |
| MAD | 14 Sep | SC-MAD-1 (verdict recorded in-thread; deliverable not yet written) | **MISSING** |
| LINK | 14 Sep | SC-LINK-2: the U(1) sector's only canonical variable is site-valued (θ_i); the compact-U(1) link reformulation is available and nothing blocks it, but it costs the phonon identification, c_s = c, and the transfer-matrix derivation of α₀. Constructed link theory gives 2 transverse modes + 3 gapped + 1 gauge, continuum limit Maxwell. SC-LINK-5 does not fire: no obstruction exists. SC-LINK-4 fires at corpus level — three field contents live (θ_i, ξ_i, SU(3) links). Kalb–Ramond duality cannot supply the second polarisation. 11 notices. Prompt `d9dba4c8…`. | `gates/LINK/` |
| RATIO | 14 Sep | SC-RATIO-2: every observable of the minimal theory (one complex scalar, GP, §1.2) depends on r_oct, r_tet only via their product, through ξ = 1/√(8·r_oct·r_tet). Sharper than the stop condition — r_oct/r_tet = 1.8430 is a fixed FCC constant (both radii = R·const, verified 15 digits), not a free input; dimensionful content needs an external anchor (a = ℓ_P, assumed). Lattice route to the ratio (scalar phonon c_z/c_x = η) cancels at the FCC point the radii pin → isotropic; residual anisotropy a fixed O(k⁴) constant. Steelman (α₂ = r_oct²/π → v_BCT; x_EW ∝ r_oct; ξ/r_oct = 11.19) uses the radii separately but is unsupported by the minimal action — N-class. One open thread: CN-RATIO-07. 7 notices. Model Opus 4.8. Prompt `5a0c0877…`, corpus `e4f5baf1…`. | `gates/RATIO/` |

## Queued, in order
1. **Gate XI (new, proposed)** — the ξ_i reading. Gate LINK's CN-LINK-06: One
   Medium App C.1 gets the photon's 2 polarisations from a three-component
   octahedral-void *displacement* field, with no Hamiltonian written for it
   anywhere, and in tension with One Medium §5.3's own exclusion of an elastic
   vacuum. This is the third field content and the cheapest remaining route to 2
   polarisations. Write and pre-register before running.
2. **Gate PRED2** — `gates/gate_PRED2_prompt.md` (`69b7b7ea…`, pre-registered at
   `23bf80b`, 13 Sep). Per-prediction surprise scoring under an enumerated grammar
   with look-elsewhere, correction-factor and date-order charges, and a Wyler
   benchmark. Distinct from PRED, which scored the collection. **MP residue:** the
   exponents S_e, S_QCD, S_R were each selected against ln(m_P^CODATA/X); score
   them as fits. Carry CN-MP-03 (two M_R values) and CN-MP-04 (three input sets)
   as corpus-consistency items to be resolved before scoring. Carry PRED's §7
   subset as the candidates worth scoring first.
3. **PRED follow-ups** (from `gates/PRED/gate_PRED_NEXT_patch.md`): (a) commit an
   itemised, formula-bearing 92-row table or withdraw the number; (b) pre-register
   the six untested predictions (Σm_ν, r, τ_p, d_n, m_DM, δ_CKM) with fixed values
   now; (c) correct the PRL C_p misprint and the α_s(m_Z) claim.
4. **Deliverable debt:** write and commit the MAD deliverable; recover or
   reconstruct the TANH and INT deliverables, or record them as lost.
5. **Census** — resume at `tex/BCT_Appendix_KA1.tex`, next id INV-0035.
   Coverage 6 of 134 .tex = 4.5%. See `inventory/inv_state.json`.
6. **Gate RATIO-OBS (new, proposed)** — the CN-RATIO-07 thread, the one item
   Gate RATIO left open. Does the minimal action provide any observable that
   resolves r_oct from r_tet — i.e. is the substrate void radius in-principle
   observable? The minimal theory contains only ξ (the product); the corpus's
   ξ/r_oct = 11.19 "structural invariant" (Letter 19) depends on the radii
   separately and is testable, it claims, only by "a sub-Planckian probe of the
   electron's internal structure." **If no** — SC-RATIO-2 is final and the
   individual-radius citation family (CN-RATIO-06: α₂ = r_oct²/π → v_BCT,
   x_EW ∝ r_oct, x_SU(3) ∝ r_tet, cos θ_K = r_oct − ½, ξ/r_oct) retires with it,
   alongside the PRED2 §5 retirement list. **If yes** — the ratio does two
   numbers' work for a *non-minimal* theory that includes the substrate, but the
   ratio it fixes is FCC-determined, so it is a prediction, not a free parameter.
   Despite its position here it is the direct finaliser of Gate RATIO; slot by
   priority. Write and pre-register before running.

## Parked
- **Gate PV** — prompt lost; ledger holds digest `ca214df4...4062`. Find and
  verify, or rewrite. Its J->PV->E5 sequence predates the current priorities.

## Standing rules, learned the hard way
- Commit deliverables, scripts and prompts to `audit/` **at close, not at leisure**.
  On 14 Sep four closed gates (C1, RANK, MP, PRED) had no committed deliverable and
  RANK's committed file was 0 bytes. This file was wrong for three days.
- Gate prompts are pre-registered: commit, pin by commit SHA, fetch by raw URL,
  hash before reading.
- **One name, one gate.** `gate_PRED_prompt.md` was pre-registered at `23bf80b`
  (`69b7b7ea…`) and overwritten three hours later at `aa70943` (`7e7675da…`) by a
  different prompt, which is the one that ran. Never overwrite a pre-registered
  prompt file; give a rewritten gate a new name. The prereg record must be
  regenerated in the same commit as any prompt change.
- The handoff template's curl line must name the gate being run; PRED's handoff
  named RANK.
- Audit the search space before any negative claim. Both traps: 26 `.tex` sit at
  the repo root outside `tex/`; and of the mount files 33 are ZIP archives and
  **2 are raw text** that neither `pdftotext`, `pymupdf` nor `unzip` will open.
  Type every file with `file`. Gate MP found `audit/APPENDIX_INDEX.md` referenced
  but absent at `aa70943` (added at `c3c705d`), and Vol 1 Parts 1–2 are real PDFs
  in the repo (the raw-text note describes a mount). Check the pinned tree, not
  the mount, when writing §0.5.
- Revise notices **clause by clause**. An "unaffected" list is a set of claims.
- A gate prompt must be able to return a favourable verdict. If it cannot, it is
  not a gate.

---

## Gate PRED2 — closed 14 Sep 2026 (appended without reading this file; quarantine held)

Prompt SHA-256 `69b7b7ea242146581cc05cd4e6b08257e2d29794d29b43f8d02e117bd20477c9`,
repo commit `ec0592f9319ab5a61851018539ab2b6ff2eb72b3`.
Deliverable: `audit/gates/PRED2/gate_PRED2_RESULT.md`.

**Verdict: SC-PRED-1**, met by `m_p/m_e = 6π⁵` (+15.6 net bits) — a formula the corpus itself
classifies as underived, and which the gate's blind inverse-symbolic control rediscovers at the
same complexity. **No prediction claimed as derived nets ≥ 10 bits.** Maximum over derived
predictions: 6.70 (`β = arccos 2r_oct`).

Positive net bits, all four with no post-hoc correction factor:
`β = arccos(2r_oct)` +6.70 · `sin²θ₁₃ = 3α₀` +4.61 · `sin²θ₁₂ = ⅓ − r_tet r_oct` +4.02 ·
`sin²θ_W(tree)` +3.38.

Negative net bits (grammar noise after charges): α = α₀(1−2α₀) −1.77 · α all-orders −5.57 ·
m_e via (π⁵+π)/6 −2.70 · **m_e via the C.2 dressing −17.12** · Koide phase −3.66 · m_ρ −6.26 ·
λ −7.09 · A −10.17 · m_d −10.52 · m_u −8.89 · m_b −10.76.

Benchmark: **Wyler ≈25 ± 1 bits** — ten bits above anything BCT produces, and Wyler is a
coincidence. Control beats the published expression on **8 of 10** targets at equal or lower
complexity.

### Open items this gate created, in priority order

1. **CN-PRED-01 — One Medium App. A Eq. (15) is arithmetically wrong.** `172 000 × e^−7.5075 =
   94.42 MeV`, not 93.0. Printed error −0.43 % should read +0.98 %. Fix or withdraw the worked
   example; it is the one derivation shown in full.
2. **CN-PRED-02 — m_P/M_R circularity.** `M_R ≡ m_P α₀²` (App GG2) and `m_P ≡ M_R/α₀²`
   (Monograph §19.1). Gravity sector of Table B.9 carries no independent content. *May overlap a
   concurrent gate; not read.*
3. **CN-PRED-03..06 — four printed expressions do not reproduce their printed values:**
   `2π/x_lep` → 666.14 not 137.046 · `r_p = ℏc/m_ρ(1+α₀)` → 0.2563 fm not 0.8386 ·
   Phase 35A Koide NLO formula ≠ its own printed 0.04050025 · `m_ρ` needs m_π0 = 134.98 while the
   table inputs m_π = 139.6.
4. **CN-PRED-12/13 — two stated errors fail against current data.** η̄ = 3r_tet is −4.3 %, not
   −0.603 % · `δ_CKM = arccos(⅓) = 70.53°` is ~4.5σ from γ = 65.75 ± 1.07°: retire or reclassify.
5. **Retire from public citation** (One Medium §10/§13, Monograph Tables 2 and B.9): α, G, m_P,
   the Wolfenstein set, m_d/m_u/m_b, m_ρ, r_p, and the −0.014 % electron mass. Deliverable §7
   names the sentences.
6. **Census coverage gap:** ~38 of the 92 claimed predictions cite appendices outside the search
   space (Vol. 1 only is mounted). A re-run with Vols. 2+ mounted would complete the census; the
   6.52-bit look-elsewhere charge applies unchanged.
7. **Recommended next gate:** derivation audit of the three uncorrected mixing predictions
   (`3α₀`, `⅓ − r_tet r_oct`, tree-level `sin²θ_W`) — they score positively for the right reason.
   A derivation audit of `6π⁵` is **not** recommended: the corpus already disclaims it and the
   control shows it is the grammar's own optimum at C = 4.

### Prompt defect recorded
SC-PRED-1 does not anticipate the case that fired — the single ≥10-bit result is disclaimed by the
corpus and reproduced by a blind control. Future PRED-class prompts should split the census into
*claimed-as-derived* vs *published-with-disclaimer*, and require the control result to be reported
alongside the score.

---

## Gate RATIO — closed 14 Sep 2026

Prompt SHA-256 `5a0c08773431c4b9de7fd69a7346c2cb087a283c49b8c1c256431b6a27aec2f3`
(matched pre-registration, 7008 B). Corpus tarball
`e4f5baf1e2e13ec53192bb47c6552052a674c1d36c92d66831d0255abe66ed64` at commit
`68ffd73641f237f5eb1de0a41785ca940a707881`. Deliverable:
`audit/gates/RATIO/gate_RATIO_deliverable.md`. Model: Claude Opus 4.8.

**Verdict: SC-RATIO-2.** Every observable of the minimal theory (one complex scalar, GP action,
MINIMAL_BCT §1.2) depends on r_oct and r_tet only through their product, via ξ = 1/√(8·r_oct·r_tet).
The geometry supplies one number — one length scale.

**Sharper than the stop condition.** The ratio r_oct/r_tet = 1.8430 was never a free datum:
r_oct = (√2−1)R and r_tet = (√(3/2)−1)R are the octahedral and tetrahedral interstitial inradii of
a *single* sphere radius R = a/2 (verified to 15 digits), so the ratio is a fixed FCC constant,
identical at any scale. The model has one scale and one packing choice (FCC), not two independent
radii. Dimensionful content additionally needs an external anchor — a = ℓ_P, assumed (App JH4
"single-point calculation at a=ℓ_P"; the corpus ties Λ_QCD to the same choice). Same epistemic
situation as INV-0120 (Λ_QCD as input).

**The lattice route, closed by calculation.** The continuum GP action is rotation-invariant →
isotropic dispersion, no ratio. A scalar phonon on the lattice gives c_z/c_x = η (axial ratio) in
the coordination-8 regime — so if the shape were free the ratio would do genuine work. But the
model's radii pin η = √2 (FCC); at that point close-packing brings the in-plane bonds into the same
shell → 12-fold cubic coordination → the sound tensor is exactly isotropic (D_xx=D_yy=D_zz).
Residual anisotropy is a fixed O(k⁴) FCC constant with no independent r-content. The model cannot
hold the shape fixed (zero parameters) AND have the ratio do observable work; the specific radii
choose the inert horn.

**Steelman, reported and failed for the minimal theory.** The full corpus uses individual radii
extensively — α₂ = r_oct²/π → v_BCT = 246.22 GeV (Volume2); x_EW ∝ r_oct, x_SU(3) ∝ r_tet
(Letter127); cos θ_K = r_oct − ½ (Monograph); and ξ/r_oct = 1/(√8·r_oct^{3/2}·r_tet^{1/2}) = 11.19
(Letter19), which does depend on the radii with unequal powers. None is derivable from the minimal
GP action, whose sole geometric input is ξ (the product); each is a standalone geometry→observable
posit layered with α₀/α₂/NLO factors and external scales — structurally the N-class scored ≈0 bits
by PRED2.

### Open items this gate created, in priority order

1. **CN-RATIO-07 [CONJECTURE] — is the substrate radius r_oct in-principle observable?** The one
   thread the gate left open, and the direct finaliser of the verdict. See queued Gate RATIO-OBS.
   If the minimal theory provides no operator that resolves r_oct from r_tet, SC-RATIO-2 is final.
   Even if the substrate is observable, r_oct/r_tet is FCC-fixed → a prediction, not a parameter.
2. **CN-RATIO-06 [ASSERTED] — retire or reclassify the individual-radius citations** (α₂ = r_oct²/π
   → v_BCT, x_EW ∝ r_oct, x_SU(3) ∝ r_tet, cos θ_K = r_oct − ½, ξ/r_oct = 11.19). They use the
   radii separately but are not consequences of the minimal action; resolve alongside the PRED2 §5
   "retire from public citation" list, not separately — same N-class family.
3. **Naming for the reachable claim.** Per MINIMAL_BCT §4 the publishable statement is "a lattice
   superfluid whose coupling is fixed by void geometry" — one geometric number (ξ/a = 2.3175) plus
   an external scale. SC-RATIO-2 is the evidence for that framing; "two radii, zero parameters"
   should not be used as stated.

### Notices
CN-RATIO-01..05 PROVEN (product-only dependence; FCC-constant ratio; continuum isotropy; lattice
cancellation at η=√2; external-scale requirement). CN-RATIO-06 ASSERTED (corpus individual-radius
formulas, unsupported by minimal action). CN-RATIO-07 CONJECTURE (substrate observability). Full
tiering and scripts in the deliverable.

### Queue reconciliation noticed while filing (not acted on here)
- **PRED2** appears both as queued item 2 and as a closed block above — it has closed (SC-PRED-1).
- **Gate XI** appears as queued item 1 "(new, proposed)", but MINIMAL_BCT §0 cites "Gate XI,
  SC-XI-3" as run. Looks like a stale queue entry.
Both left for a deliberate reconciliation pass rather than edited blind.
