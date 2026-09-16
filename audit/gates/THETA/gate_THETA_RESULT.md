# Gate THETA — Result

**Question.** Does BCT structure *force* θ_QCD = 0 as a derived output, or is it imported?

**Verdict: SC-THETA-1 (negative). θ_QCD = 0 is IMPORTED / ASSERTED, not a derived output. It stays CONJECTURE.**
All three required resolutions fail; any one failing suffices. Null result = finding. Does **not** refute the geometry.

- Model: Claude Opus 4.8, chat-side (not repo-committed). Deliverable to Michel to commit under `audit/gates/THETA/`.
- Hash-before-read confirmed: Appendices Part2 `7a09746433339a1619ff450c5427af628dd39e0e94e3573c7271c55a5b270a54`; NPBS `03db3b10c6e989ef3d79d033db3fc392a879e66748deeeaa4c90fb6f5f5b3d47`; Monograph `b057829629c9fc31f3aafea1eaec427299f1bcf9266b86665e116dfd7ea67f69`.
- Sources read cold, in this order (EDM thread read only afterward, to reconcile): App DI/DJ/DM (Part2 text), Monograph Part V §11–13 and §9.3–9.4 (per-page `.txt` sidecars in the ZIP — no OCR), Monograph §10.4.

---

## One-sentence kill (the load-bearing one — the Barr criterion)

BCT's own headline prediction **J = Im(V_us V_cb V*_ub V*_cs) = 3.08×10⁻⁵ ≠ 0** (Monograph §9.4) and **δ_CKM = arccos(1/3) ≈ 70.5°** (§9.3) require complex, non-simultaneously-diagonalisable quark mass matrices, yet the θ̄ = 0 proof rests on **"all BCT Yukawa couplings are real"** (§11.2 Proof 2) — which forces J = 0 — so the same T_d cannot deliver both, no Nelson–Barr texture reconciling them is exhibited (indeed **no quark mass matrix M_q is written down anywhere**: the masses enter as real scalar orbit formulas m_q = m_t·exp(−S_Td·n_q/24) and the CKM phase is bolted on separately as a unitary matrix "from T_d group theory"), so **arg det M_q = 0 is imported, not derived.**

---

## The three required resolutions — each UNRESOLVED

### 1. Barr criterion (J_CKM ≠ 0 and θ̄ = 0 from one T_d) — the load-bearing one. FAILS.

- The proof of θ̄ = 0 (App DI steps; Monograph §11.2) requires the quark mass matrix to be **real** ("all BCT Yukawa couplings real"; "quark masses real ⇒ arg det M_q = 0").
- A **real** mass matrix is diagonalised by real orthogonal transformations ⇒ V_CKM is real orthogonal ⇒ δ_CKM = 0 ⇒ **J = 0**. This directly contradicts the *explicit* headline J = 3.08×10⁻⁵ (§9.4) and δ_CKM = arccos(1/3) (§9.3), and the maximal PMNS phase δ^PMNS_CP = −π/2 "from the imaginary unit of the quaternion algebra" (§10.4).
- The two facts (arg det M_q = 0) and (J ≠ 0) are extracted from **mutually exclusive** descriptions of the mass sector. The reconciliation that *would* make them compatible — a Nelson–Barr texture where CP-violating phases sit in blocks that don't contribute to det — is **not constructed**. There is no M_q, M_u, M_d exhibited to check. BCT's own leptogenesis appendix (Part2, App CW) even *admits* "an O(1) complex parameter in the Yukawa matrix… full treatment requires BCT representation theory for the Yukawa texture" — i.e. the texture is complex and unfinished, the opposite of "all real."
- **Status: the compatibility is asserted, never demonstrated. UNRESOLVED ⇒ CONJECTURE.**

### 2. θ ∈ {0, π} degeneracy — is π excluded? NO.

- Proof 1 (D4 Z₂ centre, §11.1): Z(θ) = Z(−θ) ⇒ θ a fixed point of θ → −θ. Fixed points mod 2π are **{0, π}**, not {0}.
- Proof 3 (D4 modular self-duality, §11.3): S : θ → −θ, self-consistency ⇒ same {0, π}.
- Both are CP-conserving, but **θ = π gives a large neutron EDM and is experimentally excluded** — so a symmetry that only lands on {0, π} does not by itself solve strong CP; you still need a structural or dynamical reason to pick 0 over π.
- The documents write "requires θ = 0" where the symmetry only requires θ ∈ {0, π}. π is neither addressed nor excluded. **UNRESOLVED.**

### 3. arg det M_q — genuinely zero from matrix structure, or asserted from real eigenvalues? ASSERTED (non-sequitur).

- §11.2 / App DI: "The quark mass matrix eigenvalues are therefore real positive, giving arg det M_q = 0."
- arg det M_q in θ̄ = θ_bare + arg det M_q is **basis-invariant** and equals the phase of the determinant in the Lagrangian (CP-violating) basis. Making the physical eigenvalues real-positive is a chiral rotation — and that rotation shifts θ_bare by the anomaly, so you cannot separately claim arg det = 0 (from real eigenvalues) *and* θ_bare = 0 (from Proof 1); the anomaly ties them.
- With a nonzero physical CKM phase present, arg det M_q is **generically nonzero** absent a texture that forces it. "Real eigenvalues ⇒ arg det = 0" uses the wrong object (eigenvalues, not the mass matrix) and is the exact non-sequitur flagged. **UNRESOLVED** (same knot as #1).

---

## Corroborating internal error (independent of the three, terminal-verified)

The one-loop "verification" (App DI "1-LOOP CHECK"; Monograph §12.1) computes
δθ_1-loop = J_BCT/(16π²) = α₀³·sin(arccos(1/3))/(16π²) = **2.427×10⁻⁹** (reproduced at 60 dps),
then labels it "≪ 10⁻¹⁰ [VERIFIED]" / "already below the experimental bound." It is **above** every bound the documents themselves quote:

| bound quoted in corpus | δθ / bound | direction |
|---|---|---|
| App DI < 1×10⁻¹⁰ | 24.3× | **ABOVE** |
| App DI < 5×10⁻¹¹ | 48.5× | **ABOVE** |
| Monograph §11 < 1.8×10⁻¹⁰ | 13.5× | **ABOVE** |

So the inequality is inverted: read literally, the corpus's own one-loop number would *falsify* "θ̄ = 0 exact to all loop orders," and it contradicts the 1×10⁻³² neutron-EDM floor stated elsewhere. (Separately, J/(16π²) is not the correct SM contribution to θ̄ — the true CKM-induced shift is ~10⁻¹⁶–10⁻¹⁹, entering at high loop order — so the estimate is wrong in method as well as sign of the inequality.)

Note also three different J values in circulation: J_physical = 3.08×10⁻⁵ (§9.4) vs J_loop = 3.833×10⁻⁷ (§12.1 formula) — a minor internal inconsistency, not load-bearing.

---

## Reconciliation with Gate EDM (read after forming the independent read)

Full convergence. This gate reproduced SC-EDM-2's three points **cold from the primary sources** and matched SC-EDM-3's arithmetic (δθ = 2.427×10⁻⁹, ~24–49× over the quoted bounds). Two sharpenings THETA adds beyond the EDM summary:

1. The Jarlskog contradiction is **explicit and citable**, not merely implied: Monograph §9.4 prints J = 3.08×10⁻⁵ as a headline "matched to 0.07%" prediction, so "all Yukawa couplings real" (§11.2) is contradicted by a numbered equation in the same document.
2. **No quark mass matrix M_q exists in the corpus.** Masses are real scalar orbit formulas; the CKM matrix is a separately-built unitary object. arg det M_q therefore has no evaluable referent — the claim isn't just a non-sequitur, it's applied to an object that was never written down.

Independent convergence of two cold reads on the same three failure points is a positive signal about the audit's self-consistency.

---

## Consequence

- **θ_QCD = 0 stays CONJECTURE** (legitimate parity / Nelson–Barr *class*; the Barr tightrope is the open gap).
- **The distinctive anti-prediction "BCT predicts no QCD axion"** (Monograph §13.2; ADMX/IAXO/IAXO-testable) rests on this same mechanism → **inherits CONJECTURE tier**.
- **Pre-registration:** consistent with Gate EDM — do **not** pre-register "θ_QCD = 0 exact" or "d_n = 0 exact." A CONJECTURE-tiered floor d_n ≲ 1×10⁻³⁰ e·cm (near-term detection ≳ 1×10⁻²⁸ still falsifies) is honestly pre-registrable **if** the Zenodo wording tiers it CONJECTURE. Before posting: pin the d_n floor to one defended value and fix/retract the δθ = 2.43×10⁻⁹ "below bound" line, which is arithmetically false.
- **Does NOT refute the geometry** (void constants, α₀, ξ, percolating network stand).

### What would close it (elevate to a genuine output)

Write down explicit BCT quark mass matrices M_u, M_d (from T_d representation theory, not scalar orbit formulas) and show, from that single texture: (a) arg det(M_u M_d) = 0, (b) a physical CKM phase δ_CKM ≠ 0, and (c) radiative protection of (a) — i.e. an exhibited, protected Nelson–Barr texture. Absent that construction, θ_QCD = 0 remains imported.
