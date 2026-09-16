# Gate HERM — Result

**Question.** Can BCT's vacuum symmetry be recast so the quark mass matrix is *Hermitian* (M → M†) rather than *real* (M → M\*), from **minimal or zero added structure** — such that arg det M_q = 0 and J_CKM ≠ 0 both follow from the same T_d, θ = 0 is selected over θ = π, and α₀ survives? If yes, θ_QCD = 0 upgrades from imported (Gate THETA, SC‑THETA‑1) to a genuine geometric output.

**Verdict: SC‑HERM‑1 (negative). Reaching Hermiticity requires new fermion fields (a right‑handed SU(2)_R / W_R sector, or mirror quarks). Gate HERM fails at the recast. θ_QCD = 0 stays imported / CONJECTURE (SC‑THETA‑1 unchanged).**
The one‑sentence kill fires at resolution 1; resolutions 2 and 4 fail independently. Null result = finding. Does **not** refute the geometry.

- Model: Claude Opus 4.8, chat‑side. Deliverable to Michel to commit under `audit/gates/HERM/`.
- **Provenance / PASTE‑DEFECT:** the HERM pre‑registration prompt arrived as an in‑context document (inlined), not curl‑to‑disk, so there is **no authoritative prompt digest** (pre‑registration chain broken for this prompt, as with gates ICE/STIFF/MIX). The result is byte‑provenanced against the sources below and independently reproduced cold, so it is believed; a clean curl re‑run would prompt‑hash it.
- **Hash‑before‑read confirmed (curl/local):** Appendices Part1 `5656f76387be0aa9f00bef574e5d99de0635acb49eb66122b135d06b821548c7`; Part2 `7a09746433339a1619ff450c5427af628dd39e0e94e3573c7271c55a5b270a54`; Monograph `b057829629c9fc31f3aafea1eaec427299f1bcf9266b86665e116dfd7ea67f69`; NPBS `03db3b10c6e989ef3d79d033db3fc392a879e66748deeeaa4c90fb6f5f5b3d47`. Gate THETA record fetched by curl and hashed: `audit/gates/THETA/gate_THETA_RESULT.md` `56a0b7a3e90ec3a973492a4f9e16b941c49dbdb9f83a1ae33277cb301e32f8b9` (read **after** forming the independent read; Part2/NPBS/Monograph digests inside it match the above — same canonical sources).
- Sources read cold: App AD (democratic mass matrix), App Y (SU(2)_L / parity violation / left‑handedness), App K (bipartite PH / chirality assignment), App DI (strong‑CP mechanism), App CU/DI headers (Part2). Independent numeric check: `herm_step0_texture_check.py`.

---

## One‑sentence kill (load‑bearing)

BCT assigns chirality structurally — SU(2)_L couples **only** to the left‑handed oct‑void doublet, the right‑handed component is **decoupled** from the Chern‑Simons gauge field, and parity violation is *derived* from k_bulk = +1 (App Y) — so left‑ and right‑handed quarks are inequivalent under BCT's own gauge structure; a symmetry exchanging Q_L ↔ Q_R (the only thing that turns M → M\* into M → M†) is therefore **not** a symmetry of BCT, and manufacturing one requires a right‑handed weak sector (SU(2)_R / W_R with g_R, right‑handed doublets incl. ν_R, and an enlarged Higgs sector) or mirror quarks — **new fermion fields ⇒ BCT becomes a different theory ⇒ zero‑new‑fields forfeited.**

---

## The four required resolutions

### 1. The recast — does T_d act as reality (M → M\*) or chirality parity (M → M†)? **REALITY. SC‑HERM‑1.**

- **What the corpus actually commits to is M → M\*** (the reality branch), stated verbatim in App DI: *"D4 Z₂ symmetry: n → −n (orbit number reflection); Physical action: parity P on T_d crystal **orbits**; Under D4 Z₂: M_q → M_q\* … det(M_q) is REAL ⇒ arg(det M_q) = 0."* The operation acts on the **T_d orbit / flavour** structure (orbit‑number sign flip), not on Dirac chirality. This is generalised‑CP / reality, and — per Gate THETA and the cold check below — it forces **J_CKM = 0**, contradicting BCT's own headline J = 3.08×10⁻⁵.
- **Hermiticity (M → M†) requires the symmetry to swap Q_L ↔ Q_R.** In BCT that swap is obstructed by BCT's *own* construction (App Y): the weak SU(2)_L generators T₊,T₋,T₃ "only act within the LEFT‑handed subspace"; "the right‑handed component … is not coupled to the CS gauge field"; "there is no BCT void state available for a right‑handed neutrino." The k_bulk = +1 that BCT uses to **derive** parity violation is exactly what removes the L↔R parity. You cannot keep App Y's derived parity violation **and** have an L↔R parity to Hermitise M.
- **Sharpening (from Gate THETA, reconciled):** BCT writes down **no quark mass matrix M_q at all** — masses are real scalar orbit magnitudes m_q = m_t·exp(−S_Td·n_q/24), and the CKM matrix is a separately‑asserted unitary. So there is no matrix object on which "T_d acts as M→M\* vs M→M†" can even be posed at source; the only committed statement is App DI's M → M\* (reality). The Hermitian texture is a *reconstruction* the audit built to test the mechanism — not something BCT's fields supply.
- **Kill fires.** Reaching M → M† needs a right‑handed weak sector or mirror quarks. **SC‑HERM‑1.**

### 2. The {0, π} sign — does the geometry select 0 over π? **NO (independent failure).**

- A Hermitian M gives **real** det ⇒ arg det ∈ {0, π}, sign free. Cold check (`herm_step0_texture_check.py`, 2000 random Hermitian pairs): det is real to machine precision, **but 50% land on arg det = π**, not 0. Selecting 0 over π needs an even number of negative mass eigenvalues — a physical/observational input, **not** a geometric output.
- This reproduces Gate THETA resolution 2 and Gate EDM SC‑EDM‑2 (both proofs land on {0, π}; θ = π gives a large, excluded d_n). So **even granting the extension**, θ = 0 is not geometrically selected. Second, independent reason HERM cannot deliver a pure output.

### 3. α₀ survival — does α₀ = r_oct·r_tet/π survive the added structure? **YES — but this does not rescue HERM.**

- α₀ lives in the void‑geometry layer: r_oct·r_tet is packing‑determined (stacking‑blind; Gate RATIO CN‑RATIO‑02), the /π is stiffness‑set. This layer is **disjoint** from the quark flavour/chirality sector; nothing done to the mass matrix perturbs it. So α₀ survives the recast per se → the failure mode is **not** SC‑HERM‑2 (α₀ death).
- The obstruction is entirely the **field cost** (resolution 4), not α₀. α₀ surviving is necessary, not sufficient.

### 4. Zero‑new‑fields / zero‑free‑parameters tally. **COST ≫ 0.**

Minimal extension that *would* deliver a parity‑enforced Hermitian M (Beg‑Sirlin / Babu‑Mohapatra left‑right parity class):

| Added structure | Count | Note |
|---|---|---|
| Gauge factor SU(2)_R (W_R±, Z_R) | +1 group, +2 bosons | restores the L↔R parity App Y breaks |
| Gauge coupling g_R (+ exact P ⇒ g_L = g_R) | +1 coupling, +1 discrete sym | parity imposed as an exact symmetry |
| L‑R breaking scale v_R | +1 dimensionful scale | new hierarchy v_R ≫ v_EW |
| Higgs bidoublet Φ + SU(2)_R triplets/doublets | +≥2 scalar multiplets | to break SU(2)_R and set the texture |
| Right‑handed doublets incl. ν_R | +RH fermion multiplets | App Y explicitly has **no** RH slot |

Tally ≫ 0. This is honestly **BCT + left‑right parity** — a parity‑class strong‑CP solution grafted onto BCT — a **distinct theory**, not a zero‑parameter upgrade. (Radiative protection of arg det = 0 in the L‑R model is a further, separate burden; not reached, and the corpus's existing δθ = 2.427×10⁻⁹ "below bound" line is a **false inequality** — 24–49× over the quoted bounds, Gate THETA — and must not be inherited.)

---

## Guards — checked

- **Three generations not counted as L‑R partners.** The x/y/z nodal planes (App AD) transform as an E‑doublet + A₁‑singlet under the point group — a **flavour** structure. Chirality is assigned separately (bipartite A/B staggered, right on A / left on B, App K; SU(2)_L selection, App Y). No nodal plane transforms as Q_L ↔ Q_R.
- **"Improper rotation ⇒ Hermiticity" not assumed.** Determined from the fields: BCT's reflections/orbit‑reflections act on flavour/orbit space (App DI: M → M\*); the chirality parity needed for M → M† is precisely what k_bulk = +1 removes.
- **α₀ survival proven, not assumed** (resolution 3: disjoint layer).
- **Same‑session cap:** this is the only gate in this thread ⇒ citable (not CONJECTURE‑capped), subject to the PASTE‑DEFECT provenance note above.

---

## Independent cold check (reproduced, not inherited from `nelson_barr_attempt.py`)

`herm_step0_texture_check.py`, seed 20260916, 2000 random pairs each:

| texture | max/median |J_CKM| | arg det ∈ {0,π}? | sign fixed? |
|---|---|---|---|---|
| **Real** (M → M\*) | max |J| = **0** (exact) | yes (|sin arg| ≤ 1.2e‑16) | no — 51% arg = π |
| **Hermitian** (M → M†) | median |J| = 2.6e‑2; **100%** > 1e‑6 | yes (|sin arg| ≤ 1.3e‑13) | no — 50% arg = π |

Confirms: the mechanism exists (Hermitian → both Barr conditions reachable), matching the THETA construction attempt's summary; **and** that Hermiticity alone leaves the {0, π} sign free (resolution 2).

---

## Reconciliation with Gates THETA and EDM

Full convergence — a **third** independent cold read landing on the same knot. THETA/EDM found θ_QCD = 0 is imported because (a) BCT's committed reality mechanism (M → M\*) forces J = 0, contradicting its own J = 3.08×10⁻⁵, and (b) the symmetry only reaches θ ∈ {0, π}. HERM adds the structural reason the natural fix (Hermiticity) is unavailable: **BCT's derived parity violation (App Y) forbids the L↔R parity that Hermiticity needs, so the fix costs a right‑handed weak sector.** THETA's "what would close it" (exhibit M_u, M_d with arg det = 0 **and** δ_CKM ≠ 0 **and** radiative protection) is reachable only in that extension. Triple convergence (EDM/THETA/HERM) is a positive signal about the audit's self‑consistency.

---

## Consequence

- **θ_QCD = 0 stays CONJECTURE** (legitimate parity / Nelson‑Barr *class*; the Barr tightrope is the open gap). SC‑THETA‑1 unchanged.
- **The minimal theory that would upgrade it is BCT + left‑right parity** (SU(2)_L × SU(2)_R × U(1)_{B−L}, exact P) — a well‑defined, distinct extension, reportable as such. It is *not* a zero‑new‑fields output of the BCT geometry.
- **Pre‑registration:** unchanged from EDM/THETA — do not pre‑register "θ_QCD = 0 exact." The honestly pre‑registrable statement remains a CONJECTURE‑tiered floor d_n ≲ 1×10⁻³⁰ e·cm (near‑term detection ≳ 1×10⁻²⁸ still falsifies).
- **Does NOT touch the void geometry** (α₀, void radii, ξ, percolating network stand) — as the prompt anticipated.

## Files
- `gate_HERM_RESULT.md` (this file)
- `herm_step0_texture_check.py` (real‑vs‑Hermitian texture check; deterministic, seed 20260916)
- as‑run prompt to be committed alongside (note PASTE‑DEFECT: no authoritative prompt digest for this run)
