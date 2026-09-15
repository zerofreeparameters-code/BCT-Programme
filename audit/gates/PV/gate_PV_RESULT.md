# GATE PV — RESULT

**Does a vector-charge (higher-rank / fracton-class) gauge theory on the O_h void
lattice deliver a massless 2-polarisation transverse Maxwell photon, or does it
fail like the scalar-charge case (Gate P)?**

Cold Ledger gate · hypothetical-construction · run 16 September 2026.

---

## DIGEST

Received file: `audit/gates/gate_PV_prompt.md` at commit `b588f1b`, curled to disk.
SHA-256 = `0fb236e368b90300aa5220c9a2be86ba92ba4d4e76d2026fe33056d495ca9bfa`
(19,627 bytes). Hash is of the file the run session received, not chat text.
`audit/MINIMAL_BCT.md` read for constants only (SHA-256
`8beb83da715f53a4f9bc7de594bc7f6d3225a3e5d06dc410cad952eb24c0cd70`).

---

## VERDICT — FIRST

**PV CLOSES. No photon by the higher-rank route.** The gate closes on **three
independent grounds**, in the order §0.4 evaluates them:

- **SC-PV-2 (Step 1, P-transfer holds).** The vector-charge charge–charge coupling,
  derived cold, is `V(k) = 2(q·p)/k² − (q·k)(p·k)/k⁴`: an intrinsic **vector inner
  product** `q·p` (orientation-dependent sign) plus a dipolar orientation-dependent
  term. This is structurally *not* the isotropic scalar Coulomb `q₁q₂/r` of Maxwell,
  and *not* a mass. Gate P's failure **transfers**; the one-derivative Gauss law does
  not escape it.
- **SC-PV-4 (Step 2, crux).** Even granting the structure and a deconfined phase, the
  gapless spectrum is **not** the 2-polarisation transverse Maxwell vector. The full
  vector-charge theory has **3** physical modes (Maxwell has 2): two transverse plus a
  **physical longitudinal** (compressional) mode that Maxwell does not possess. The
  traceless variant has 2 modes, but they sit in the `E_g ⊕ T_{2g}` tensor sector, not
  the `T_{1u}` transverse-vector doublet. These are generalised-photon / fractonic
  (elastic-dual) modes — the exact false positive guard (iii) of §3d.
- **SC-PV-1 (Step 3, not formally reached but decisive if it were).** A symmetric
  rank-2 tensor gauge field with dipole/angular-charge-conserving matter is **not a
  function of a single S¹ complex scalar** (one helicity-0 Goldstone). Nothing in the
  FCC void connectivity forces it. The whole structure is a **free input**.

The three are not redundant: PV would close on **any one** of them. The single S¹
scalar's one phonon stands as the field content. **The geometry is untouched** — the
packing, the network, `r_oct·r_tet`, `ξ`, and √2-isotropy all stand. α does **not**
re-derive by this route (Step 4 not reached).

---

## SEARCH-SPACE COVERAGE (what was actually examined)

The object under test is Pretko's **vector-charge** rank-2 U(1) gauge theory: a
symmetric tensor gauge field `A_{ij}` with gauge transformation
`A_{ij} → A_{ij} + ∂_(i λ_j)` (vector gauge parameter `λ_j`) and generalised Gauss
law `∂_i E^{ij} = ρ^j` (**one** spatial derivative — where the scalar-charge fracton
of Gate P has two: `∂_i∂_j E^{ij} = ρ`). Its conserved quantities are the vector
charge `Q^j = ∫ρ^j` and the angular charge `∫(x×ρ)`; its matter is **lineon** (1-D
mobile). Examined cold: the O_h irrep content of `A_{ij}` (§1); the static
charge–charge coupling (§2, the P-transfer test); the physical gapless-mode count,
sector and dispersion (§3, the crux, with all three false-positive guards); and the
provenance/geometry-hosting question (§4). This exhausts the vector-charge member;
larger-coset and multi-field members remain formally untouched (see CN-PV-05).

---

## §1 — STEP 0: THE HIGHER-RANK STRUCTURE ON O_h (derived cold)

**Irrep content.** Computed from the explicit 48 signed-permutation matrices of O_h
(`pv_step0_irreps.py`), the symmetric rank-2 tensor decomposes as

```
A_{ij}  =  A_1g  ⊕  E_g  ⊕  T_2g            (dim 1 + 2 + 3 = 6)
```

`⟨χ_sym², χ_sym²⟩ = 3` (three distinct irreps), `mult(A_1g)=1` (the trace `δ_ij`).
**Crucially `mult(T_1u in Sym²) = 0`:** the Maxwell vector potential transforms as
`T_1u` (polar vector), and it does **not** appear in the tensor gauge field. The
gauge field carries no vector component. (This is a statement about the *gauge field*;
the physical-mode identity is settled independently in §3, because duality can carry
physical modes into a `T_1u`-labelled elastic sector — see the honest caveat there.)

**Gauge structure.** `A_{ij} → A_{ij} + ½(∂_i λ_j + ∂_j λ_i)`; `∂_i E^{ij} = ρ^j`;
conserved `Q^j` and angular charge; lineon mobility. Contrast with scalar-charge
(Gate P): `A_{ij} → A_{ij} + ∂_i∂_j λ`, `∂_i∂_j E^{ij} = ρ`, conserved charge **and
dipole**, fully-immobile fractons. PV inherits **no** P verdict; the derivations below
are independent.

## §2 — STEP 1: THE P-TRANSFER TEST — IS THE COUPLING A MASS?

Static: `E^{ij} = −∂^(i φ^j)`; Gauss `∂_i E^{ij} = ρ^j` gives, in Fourier space,
`½(k² φ^j + k^j (k·φ)) = ρ^j`. Solving (`pv_step1_potential.py`, sympy, exact):

```
V(k) = 2 (q·p)/k²  −  (q·k)(p·k)/k⁴
```

for two point vector charges `q`, `p`. **Two structural facts, both fatal to a Maxwell
reading:** (1) the leading term is a **vector inner product** `q·p`, whose sign
depends on the relative orientation of the charge vectors — this is Maxwell's `q₁q₂`
only if the charges were scalars, which they are not; (2) the second term is an
orientation-dependent dipolar kernel `(q·k)(p·k)/k⁴` → real-space `~[(q·p) −
3(q·r̂)(p·r̂)]/r`. Neither is a mass; neither is isotropic scalar Coulomb. This is the
same structural signature §0.2 records for Gate P (charge–charge coupling = vector
inner product, orientation-dependent sign, not a mass). **P transfers → SC-PV-2.**
The one-derivative Gauss law changes the *power counting* of the fields but not the
inner-product character of the coupling.

## §3 — STEP 2: THE CRUX — TRUE MAXWELL MODE + DECONFINEMENT (load-bearing)

**(a) Mode spectrum.** Hamiltonian (Dirac) counting (`pv_step2_modecount.py`): each
first-class Gauss constraint removes 2 phase-space DOF. Vector-charge full symmetric:
config 6, **3 first-class** Gauss constraints → `(12 − 6)/2 = 3` physical modes.
Traceless variant → 2. Maxwell (config 3, 1 constraint) → 2. Dispersion of the
gapless branches is linear `ω ∝ |k|` (the modes *are* gapless — they clear that bar),
but generically with **two speeds** `c_L ≠ c_T` (longitudinal vs transverse),
non-Maxwell.

**(b) Is any gapless mode a true transverse Maxwell vector? NO.**
- Full theory: 3 modes = 2 transverse + **1 physical longitudinal**. The Maxwell
  photon has exactly 2, with its longitudinal component **pure gauge** (unphysical).
  The extra physical compressional mode is the tell: this is the acoustic spectrum of
  the fracton-elasticity dual, not a photon. A `T_1u`-labelled elastic phonon triplet
  is *not* a Maxwell photon precisely because all three branches are physical.
- Traceless theory: 2 modes, but in the `E_g ⊕ T_2g` **tensor** sector — quadrupolar
  polarisation, not the transverse polar-vector doublet, and still coupling by the
  orientation-dependent inner product of §2.

Either way the gapless mode is a **generalised-photon / fractonic mode**, distinct
from the 2-polarisation transverse Maxwell vector. → **SC-PV-4.**

**(c) Deconfinement / stability.** Secondary to (b), but noted: the *compact*
vector-charge U(1) is not guaranteed a stable deconfined phase on a lattice. Gapless
higher-rank U(1) phases are non-generic — prone to confinement (monopole/instanton
proliferation) or instability to lattice-scale perturbations. On the O_h lattice with
geometry-fixed couplings this would need to be *shown*, not assumed. Because (b)
already closes the gate, PV does not rest on this; but it is a further obstruction,
consistent with **SC-PV-3** had (b) not fired.

**(d) The three false-positive guards, explicitly:**
- (i) **Not** the single scalar phonon relabelled — the corpus has one Goldstone; this
  posits a 2–3-mode structure, strictly larger.
- (ii) **Not** a Kalb–Ramond 2-form (dual of the 3+1-D superfluid, 1 polarisation) —
  the vector-charge spectrum has 2–3 modes, not the single dual-superfluid mode.
- (iii) **IS** a generalised-photon / fractonic mode — which is exactly why it is
  **not** the photon. This guard fires; it is PV's central determination.

## §4 — STEP 3: GEOMETRY-HOSTED OR FREE INPUT (conditional — not formally reached)

Recorded because it is independently decisive. The corpus field content, re-derived
from MINIMAL_BCT, is a single S¹ complex scalar `Ψ = √ρ e^{iθ}` with one gapless
Goldstone (the phonon) and a gapped Higgs-like amplitude mode. A symmetric rank-2
tensor gauge field is **not** a function of one complex scalar; the vector-charge /
lineon matter and the `∂_i E^{ij}=ρ^j` Gauss law are additional postulates. The FCC
void connectivity (oct voids → FCC sublattice; tet voids → diamond-like sublattice;
oct–tet bipartite window graph) supplies a *graph on which fields could live*, but no
mechanism forcing a rank-2 tensor gauge field or dipole/angular-charge conservation.
It is a **free input** — the same parameter cost PROMOTE/P/ICE were charged.
→ **SC-PV-1** would hold. No no-selected-fit coupling was posited to land a photon
(that would be the selected-fit fallacy; zero weight).

## §5 — STEP 4: DOES α SURVIVE (conditional — not reached)

Not reached (Step 2 unfavourable). For the record: in `α₀ = r_oct·r_tet/π`, the
packing ratio `r_oct·r_tet` is a fact of the O_h/FCC packing and is
gauge-structure-independent (it **survives** as geometry). But the `/π` and the
identification of that ratio as the EM coupling both presuppose a Maxwell photon,
which this route does not deliver. So there is **no** forward derivation of α here;
neither 5a nor 5b is earned.

## §6 — PARAMETER AUDIT & STEELMAN

**Parameter audit — free inputs (each not a pure function of the geometry):**
1. The rank-2 symmetric tensor gauge field `A_{ij}` itself — not in a single scalar.
2. The vector-charge Gauss law `∂_i E^{ij}=ρ^j` and lineon (dipole/angular-charge-
   conserving) matter — additional postulates.
3. The tensor stiffness(es) setting `c_L`, `c_T` — no geometry derivation offered
   (and none may be posited to fit a mode: selected-fit fallacy).
4. The assumption of a stable deconfined phase — non-generic, unshown on this lattice.
5. The identification of any resulting coupling with EM — blocked by §2 and §3.
**Nothing about the higher-rank route is a pure function of the void geometry.**

**Steelman (required).** Strongest pro-photon case: the vector-charge theory is dual
to elasticity (Pretko–Radzihovsky), and an isotropic elastic medium has **two
transverse acoustic modes** with linear isotropic dispersion `ω = c_T|k|` — could
those two *be* the photon? **It fails on the exact unfilled brick:** the two transverse
phonons are inseparable from a **third, physical longitudinal** phonon `c_L` (a
Goldstone of translation, ungappable without breaking the symmetry that protects it),
so the spectrum is 3-fold, not the 2-fold gauge-protected transverse Maxwell doublet;
the charges couple by an **orientation-dependent vector inner product** (§2), not
isotropic Coulomb; and the whole elastic/tensor structure is a **free input** on a
single-scalar corpus (§4). The steelman identifies a real, interesting theory
(fracton-elasticity) — but not a Maxwell photon, and not one the BCT geometry forces.

**Exact unfilled brick:** *the deconfined gapless spectrum is a fractonic/elastic
mode set (2–3 modes, physical longitudinal, orientation-dependent inner-product
coupling), not the 2-polarisation transverse Maxwell vector; and the rank-2 structure
is a free input the single S¹ scalar does not supply.*

---

## CN-PV NOTICES

- **CN-PV-01 [PROVEN].** Symmetric rank-2 tensor on O_h = `A_1g ⊕ E_g ⊕ T_2g`;
  `mult(T_1u) = 0`. (script pv_step0_irreps.py)
- **CN-PV-02 [PROVEN].** Vector-charge static coupling `V(k)=2(q·p)/k²−(q·k)(p·k)/k⁴`
  — vector inner product with orientation-dependent sign; not a mass, not isotropic
  Coulomb. Gate P's failure transfers. (script pv_step1_potential.py) → SC-PV-2.
- **CN-PV-03 [PROVEN].** Physical gapless modes: 3 (full) / 2 (traceless), vs Maxwell 2.
  The full theory carries a physical longitudinal mode Maxwell lacks; the traceless
  modes are `E_g⊕T_2g` tensor modes, not the `T_1u` transverse doublet.
  (script pv_step2_modecount.py) → SC-PV-4.
- **CN-PV-04 [PROVEN].** The rank-2 tensor gauge field + vector-charge/lineon matter
  are not a function of a single S¹ complex scalar; the void connectivity forces no
  such structure. Free input. → SC-PV-1 (recorded; Step 3 not formally reached).
- **CN-PV-05 [ASSERTED].** Only the **vector-charge** member was audited. Larger-coset
  and multi-field higher-rank members remain formally untouched — but each faces the
  same two generic obstructions surfaced here (extra physical modes beyond the Maxwell
  doublet; provenance from a single scalar). Named, not closed.
- **CN-PV-06 [CONJECTURE].** The compact vector-charge U(1) likely lacks a stable
  deconfined phase on the O_h lattice with geometry-fixed couplings (SC-PV-3 territory).
  Not the load-bearing closure; flagged for any future higher-rank gate.
- **CN-PV-07 [FALSIFIED].** "The two transverse elastic modes are the photon" — false:
  a physical longitudinal partner and orientation-dependent coupling distinguish them.

---

## §0.5 — THE PREMISE, STATED AS A COST (reproduced verbatim)

> This audits whether a higher-rank (vector-charge / fracton-class) gauge theory on the BCT geometry can host a Maxwell photon, not whether such a photon would be convenient. The corpus as written is a single S¹ complex scalar; a rank-2 tensor gauge field with dipole-conserving matter is a **new theory**, and this gate asks only whether the void geometry forces or naturally hosts it without a fit, and whether its gapless spectrum genuinely contains the 2-polarisation transverse Maxwell vector. A favourable verdict ("geometry-hosted higher-rank gauge structure, deconfined, with a true transverse Maxwell mode") does **not** vindicate BCT-as-written — it identifies a *new theory worth writing down*, which would then still owe, separately and later: the complete higher-rank action, the photon's coupling to matter, QED, the mass spectrum, and α if not re-derived here. An unfavourable verdict ("coupling still not a mass," "gapless mode is fractonic not Maxwell," "structure is a free input," "confines / unstable on this lattice," or "unauditable") does **not** refute the void geometry (packing, network, packing ratio r_oct·r_tet, ξ, isotropy at √2 stand) — it means the photon cannot be built from the packing via a higher-rank gauge structure either, and the single S¹ scalar stands as the field content.

## §0.6 — WHAT SETTLING THIS BUYS (reproduced verbatim)

> This gate tests the one structurally-distinct photon route left open after the scalar-charge fracton (Gate P), the rank-1 link/window routes (LINK/ICE/STIFF), and the order-parameter promotion (PROMOTE): a higher-rank / vector-charge gauge theory. It does **not**, on its own, deliver EM, QED, or the mass spectrum; each remains a separate later gate even on a favourable verdict. A favourable verdict would reopen the photon question on a genuinely new (fracton-class) footing — significant, but the beginning of a new theory, not a vindication of BCT. An unfavourable verdict, combined with P / LINK / ICE / STIFF / PROMOTE, **exhausts the audited routes to a massless 2-polarisation photon on the BCT lattice** — scalar-charge, rank-1 link/window, order-parameter promotion, and higher-rank alike — leaving the single S¹ scalar's one helicity-0 phonon as the field content, and the photon reachable, if at all, only by a mechanism not yet imagined. It does not refute the geometry.

---

## CONTAMINATION STATEMENT

Run in a fresh thread. **Not consulted:** the 9–16 Sep threads; scoping/synthesis
threads; BCT-X/Sandbox; any `gate-*` memory summary; any concurrent gate; and no
`audit/gates/*/` deliverable (P, PROMOTE, OP, R2, ICE, STIFF, LINK, PH) nor
`audit/notes/`. **Read:** the pre-registered prompt (hashed) and `audit/MINIMAL_BCT.md`
(constants + field-content benchmark, permitted by §0.2); standard higher-rank/fracton
gauge theory (Pretko; fracton-elasticity duality), Goldstone/gauge mode counting, and
compact U(1) lattice-gauge facts as **mathematical machinery only**. **Disclosed
leakage:** the session's memory *listing* (one-line descriptions only, bodies unread)
exposed some gate names and verdict labels (e.g. SC-LINK-2, SC-JHF-1, SC-MAD-1); none
of their content was used, and the §0.2 benchmarks (single S¹ scalar; one Goldstone;
isotropy at √2; P's coupling character) were re-derived here, not trusted. MINIMAL_BCT
states prior-gate conclusions about the photon; these were **not** inherited — the
vector-charge case was derived cold and independently. No P/PROMOTE/OP/R2 number
(coupling sign, mode count, irrep list, deconfinement claim) reached this run.

## WHAT THIS GATE DID NOT ESTABLISH

It did not test whether a higher-rank photon (had one existed) couples to matter,
reproduces QED, or yields the mass spectrum — each a separate later gate. It did not
close the larger-coset or multi-field higher-rank members (CN-PV-05), only named them.
It did not refute the void geometry: `r_oct·r_tet`, `ξ`, the network, and √2-isotropy
stand. It did not resolve SC-PV-3 (deconfinement) definitively — it showed the gate
closes without needing to.

*Run 16 September 2026. Vector-charge higher-rank route: closed. With P / LINK / ICE /
STIFF / PROMOTE, the audited routes to a massless 2-polarisation photon on the BCT
lattice are exhausted; the single S¹ scalar's one helicity-0 phonon stands as the
field content. The geometry is untouched.*
