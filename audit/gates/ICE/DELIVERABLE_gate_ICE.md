# GATE ICE — DELIVERABLE
## Is the double layer a HARD local constraint (Gauss law) or a SOFT coupling on the FCC void network?
### Cold Ledger gate. Hypothetical-construction gate. Run 15 September 2026.

---

## 0. HANDOFF / DIGEST / CONTAMINATION

**Handoff.** The gate prompt was delivered **pasted** as an in-context document, **not**
fetched from a commit-pinned `raw.githubusercontent.com` URL. Per §0.1, I therefore **claim no
repo-verified SHA-256 digest** for the received file. (A digest of the pasted text is not a digest
of a repository object and would prove nothing about provenance; I do not fabricate one.)

**Contamination statement.**
- I did **not** open any `gate-*` memory summary, `audit-findings` (Cold Ledger), the 9–15 Sep
  threads, BCT-X/Sandbox, or any `audit/gates/*/` deliverable — in particular not `DL/` or `LINK/`.
- **Disclosed leak (unavoidable, ambient):** the auto-injected memory *listing* contains one-line
  descriptions that name prior verdict *codes* (e.g. that LINK and JHF closed). I have seen those
  strings. I have **not** read their contents, and nothing in them supplied physics to this gate.
  The two benchmark facts were **re-derived** below, not imported.
- `audit/MINIMAL_BCT.md` was **not available** to this session (not in the mount, and I did not
  break quarantine to hunt for it). I therefore worked the phase determination **symbolically** in
  J, ξ, a, n̄ and did not use any corpus numerical value. This makes the derivation more cold, not
  less; the numeric-occupation question is flagged as a parameter cost in §5.
- The two inherited benchmark facts, **re-derived independently** (not trusted): (i) a neutral
  double layer carries no net monopole and acquires no Anderson–Higgs/Meissner mass — confirmed,
  a dipole sheet has zero net charge, its far field is O(1/r³) with no massive-photon Yukawa
  screening term to generate; (ii) with that mass absent the residual link object is a **compact**
  U(1) phase theory on the void windows, massless iff deconfined (Coulomb), gapped otherwise —
  confirmed by construction, the phase θ on each window is 2π-periodic, so the gauge group is
  compact U(1) and Polyakov's confinement question applies.

---

## VERDICT (first): **SC-ICE-1** — a genuine double layer is **SOFT**; at natural occupation the theory is a lattice **superfluid whose single gapless mode is the corpus phonon**. No new photon, no second polarisation.

Subsidiary, load-bearing findings:
- The double layer is a **potential jump = a background connection**, not a Gauss-law constraint on
  the dynamical flux. This is the decisive determination (§2).
- The soft phase is controlled by **r = 2 n̄²(ξ/a)²**; the GP stiffness **J cancels exactly** (§3).
  At natural occupation r ≳ O(1) ⇒ superfluid ⇒ one Goldstone phonon.
- The **only** route to a massless photon is the HARD branch, which is reachable only by making the
  double layer **stiff** (large potential jump), i.e. pushing into the **small-r Mott/ice regime** —
  a **non-geometry occupation/strength input**. That is at best **SC-ICE-2 (parameter cost)**, and
  it rests on an **unfilled brick**: a proof that a real double layer *is* that hard constraint. It
  does **not** reach SC-ICE-3.
- Consequence (as §0.5 states): with LINK (massive) and DL (no Higgs mass, phase undetermined),
  **this exhausts the audited link-variable routes to a massless two-polarisation photon on the
  BCT lattice.**

This verdict is licensed by the physics, not by a wish for either sign; the steelman (§6) is given
its strongest form and its one missing brick is named exactly.

---

## 1. SEARCH-SPACE COVERAGE — THE NETWORK AND RING-EXCHANGE GEOMETRY (built cold)

FCC (≡ BCT at c/a=√2). Nodes = octahedral + tetrahedral voids; edges = shared triangular windows
(exactly 3 common bounding atoms). `build_network.py`, deterministic, 5×5×5 cells, deep-interior
audit. Results:

| quantity | value | check |
|---|---|---|
| oct coordination | 6 atoms at r=a/2 | ✓ |
| tet coordination | 4 atoms at r=√3·a/4 | ✓ |
| windows are oct–tet only | oct–oct=0, tet–tet=0 | **bipartite** |
| oct degree | **8** | ✓ (octet-truss) |
| tet degree | **4** | ✓ |
| V per conventional cell | **12** (4 oct + 8 tet) | ✓ |
| E per conventional cell | **32** | = (4·8+8·4)/2 |
| components C | **1** | connected |
| cycle rank b₁ = E−V+C | **21** per cell (1.75/node) | b₁>0 ✓ |
| **girth** | **4** | oct–tet–oct–tet squares |
| shortest loops / oct | **12** | ring-exchange plaquettes |
| shortest loops / tet | **6** | " |

This is the **tetrahedral–octahedral (octet-truss) honeycomb**. The natural **Gauss-law candidate**
is the signed sum of window fluxes at each node (lattice divergence) — degree-8 at oct, degree-4 at
tet. b₁=21>0 and girth 4 confirm a rich short-loop structure: the ring-exchange, *if* a hard
constraint existed, would run at 4th order and be comparatively strong. **This geometry does not by
itself decide hard vs soft** — that is set by the physics of the double layer (§2), not the graph.

---

## 2. STEP 1 — HARD vs SOFT: THE DECISIVE DETERMINATION → **SOFT**

**Definitions.**
- **HARD:** the double layer fixes the lattice divergence at each node — a local Gauss law /
  ice-rule, Σ_{windows∈node} E = q̄ (fixed) — enforced with a large penalty, projecting simple
  condensation out and leaving a loop-only ("ice") manifold.
- **SOFT:** the double layer sets a fixed **background link phase** θ⁰_ij on each window (or a
  weakly-coupled dynamical field) that shifts, but does not forbid, condensation.

**What a double layer physically is, and what it therefore realises.**
A double layer is a **dipole sheet**: two opposed charge sheets a distance d apart, dipole surface
density P. Its defining electrostatic signature is a **discontinuity — a jump — in the scalar
potential** across the sheet, ΔΦ = P/ε₀, with **no net charge** and (away from its rim) **no net
field**. A potential *jump* across a window maps, in the link/phase language, onto a **fixed value
of the connection integrated across that window** — i.e. a **background link phase θ⁰**. A prescribed
background connection is a **c-number inhomogeneous term**, not a projector: it is **removable by a
gauge/phase redefinition** everywhere except at the sheet's rim (where flux concentrates like a
Dirac string). It penalises nothing and forbids nothing about the node divergence. **A genuine
double layer is therefore SOFT.** It is a boundary condition on the *potential*, not a constraint on
the *dynamical flux divergence*.

The would-be hard reading requires fixing the node divergence with a large **energy penalty**. A
double layer supplies such a penalty only if it is **stiff** — if the potential jump ΔΦ is so large
that moving net charge across a window costs ≫ the hopping scale (a Coulomb-blockade / Mott pinning
of the void occupation). That is a statement about the **magnitude** of the double layer, and it is
exactly the small-r regime of §3, reached only away from natural occupation. So: the hard reading is
not *false as physics*, but it is **not what "a double layer" gives by default** — it is what a
*specially stiff* double layer would give, and stiffness is a separate input, not a consequence of
the dipole-sheet definition. The fork is decided, with the soft branch physically realised; the hard
branch is quarantined to §6 with its cost.

(This is not `SC-ICE-5`: both definitions are perfectly consistent and the physics **does** decide
between them for a *generic* double layer — soft — with the hard case pinned to a nameable
stiffness/occupation condition.)

---

## 3. STEP 2 — THE PHASE (SOFT branch): J CANCELS; r = 2 n̄²(ξ/a)²

Gross–Pitaevskii on the void lattice, ψ_i=√(n̄/a³)·e^{iφ_i}. `phase_analysis.py` (sympy):

- Phase-coherence (Josephson) scale per window: **E_J = ℏ²n̄/(m a²)** — favours the superfluid.
- On-site charging scale: **E_C = g/a³** — favours number localisation (Mott/ice).
- Both are ∝ ℏ²/m (the GP stiffness "J"). Eliminating g via the healing length
  ξ² = ℏ²/(2mgρ):

  **E_C = ℏ²/(2 m n̄ ξ²)**, and

  **r ≡ E_J/E_C = 2 n̄² (ξ/a)²** — the ℏ²/m (=J) scale **cancels exactly** (verified: the ratio
  contains no ℏ and no m).

**J-cancellation test: PASSED — J cancels.** The overall stiffness sets the *speed* of the phonon
but plays **no role** in which phase the system is in. The controlling dimensionless ratio is the
pure combination **n̄²(ξ/a)²** (equivalently n̄·ξ/a).

**Which phase at natural occupation?** Superfluid (phase-coherent) when r exceeds the 3D
boson-Hubbard threshold, which with coordination z∈{4,8} sits at z·r ≳ ~0.25, i.e.
n̄²(ξ/a)² ≳ ~0.02 — comfortably satisfied for any n̄≳1 with ξ~a. So at **natural occupation the
theory is a superfluid**, and its **single gapless mode is the U(1) Goldstone phonon — the mode the
corpus already has.** There is **no second polarisation and no emergent photon** on this branch
(`SC-ICE-1`). Only by driving n̄²(ξ/a)²≪1 (small occupation and/or ξ≪a — a **non-geometry** choice)
could one leave the superfluid; that is the parameter-cost regime (§5), not a geometry-fixed photon.

---

## 4. STEP 3 — POLARISATIONS / ISOTROPY, WITH THE FALSE-POSITIVE GUARD

On the realised (soft/superfluid) branch there is **one** gapless mode: the **scalar Goldstone
phonon** of the broken U(1). It is a **single compressional/scalar** excitation — **not** a
transverse vector. The gate's false-positive guard is therefore decisive here and points the
*correct* way: the gapless sector is **one scalar mode, not two transverse vector polarisations**;
there is no relabelling under which it becomes a genuine photon. A genuine two-polarisation
transverse vector would require the **hard** Coulomb phase (an emergent E-field on links with a
Gauss law and a ring-exchange B-field) — which this branch does not realise.

For completeness (conditional): *were* a Coulomb phase reached, O_h cubic symmetry guarantees a
rank-2 response tensor ∝ δ_ij, so such a photon **would** be isotropic. But we do not reach it, so
isotropy is moot for the verdict.

---

## 5. STEP 4 — OCCUPATION / PARAMETER AUDIT

The phase is controlled by **r = 2 n̄²(ξ/a)²**.
- **ξ/a**: plausibly geometry-fixed (a healing length tied to the packing), *if* the corpus fixes
  it — unavailable to this quarantined session, so treated as a symbol.
- **n̄ (void occupation)**: a **NEW INPUT** unless the corpus derives it from geometry. The gate's
  own product-vs-ratio test: the geometry (network, girth, O_h) does **not** by itself place the
  system on either side of the transition — the **occupation decides it**. At natural occupation
  the geometry lands the system in the superfluid (no photon). To reach a Coulomb/photon regime one
  must set n̄²(ξ/a)²≪1 **by hand** ⇒ **parameter cost** (`SC-ICE-2`), the same epistemic situation
  the census closed for any dimensionful input fixed after the fact.

**Net: no branch yields a geometry-fixed massless two-polarisation photon.** Superfluid side → one
scalar phonon (SC-ICE-1). Coulomb side → needs a tuned occupation/stiffness (SC-ICE-2). The photon
is never *free*.

---

## 6. STEP 5 — THE STEELMAN (required)

**Strongest hard case.** Take the double layer to be **stiff**: a large potential jump ΔΦ per
window. Then transferring net charge across a window is Coulomb-blockaded; each void's occupation is
pinned; the node divergence is frozen — an effective **hard Gauss law**, a genuine **ice manifold**.
On this constrained manifold the girth-4 squares (12 per oct, 6 per tet, b₁=21/cell) carry a
**strong ring-exchange** (4th-order), generating an emergent magnetic term. The constraint gaps the
"electric charges" (occupation defects). 3+1D compact U(1) **does** possess a deconfined Coulomb
phase (Polyakov: unlike 3D, 4D/3+1D is not always confining), and short girth / strong ring-exchange
pushes toward the deconfined side, exactly as quantum spin ice on pyrochlore realises an emergent
gapless photon. **If** the stiff double layer's strength were itself fixed by the void geometry and
**if** the constrained network sat on the deconfined side, the outcome would be a massless,
two-transverse-polarisation, O_h-isotropic photon **with no free parameter** — the first route in
the audit past the representation wall without a parameter (`SC-ICE-3`). If that succeeded it would
be reported prominently.

**Why it does not close — the exact unfilled brick(s).**
1. **The load-bearing brick:** a proof that a **real** double layer *is* the hard local Gauss-law
   constraint. What is established above is the opposite for a *generic* layer: a dipole sheet is a
   **potential jump = removable background connection = SOFT**. The hard reading needs the layer to
   be **stiff** (ΔΦ ≫ E_J), and stiffness is **not** part of the definition of a double layer — it
   is an extra magnitude that must be **derived from the void geometry**, not assumed. No such
   derivation exists here.
2. Even granting stiffness, its magnitude sets r, and r must land **sub-threshold** — an
   **occupation/strength condition**, not a geometric identity (§5). At natural occupation r≳O(1)
   ⇒ superfluid, i.e. the layer is *not* stiff enough to constrain.
3. Even granting a hard constraint at sub-threshold r, that the **specific** octet-truss network is
   on the **deconfined** (not confined) side of its compact-U(1) transition is asserted by analogy
   to pyrochlore, **not** demonstrated for this lattice.

Brick (1) is the one that matters and is the one the whole hard route rests on. Named exactly:
**"a genuine (geometry-strength) double layer imposes the hard local Gauss law on the window flux."**
Absent that proof, the honest default is SOFT ⇒ SC-ICE-1.

---

## 7. CN-ICE NOTICES (tiered)

- **CN-ICE-01 [PROVEN, cold]** FCC void network = octet-truss honeycomb: V=12, E=32, C=1, b₁=21 per
  cell; bipartite oct(deg 8)–tet(deg 4); **girth 4**; 12 shortest loops/oct, 6/tet. (`build_network.py`)
- **CN-ICE-02 [PROVEN, re-derived benchmark]** A neutral double layer has no net charge ⇒ no
  Anderson–Higgs/Meissner mass; residual object is **compact** U(1) on windows, massless iff
  deconfined.
- **CN-ICE-03 [PROVEN, physical + symbolic]** A genuine double layer is a **potential jump = a
  background link connection = SOFT**, not a Gauss-law constraint on the flux divergence.
- **CN-ICE-04 [PROVEN, symbolic]** Soft branch: **J cancels**; controlling ratio **r = 2 n̄²(ξ/a)²**.
  (`phase_analysis.py`)
- **CN-ICE-05 [PROVEN → verdict]** At natural occupation r≳O(1) ⇒ superfluid ⇒ **single Goldstone
  phonon = the corpus mode**; no second polarisation. **SC-ICE-1.**
- **CN-ICE-06 [CONJECTURE]** A **stiff** double layer could realise a hard ice constraint whose
  girth-4 ring-exchange yields a deconfined Coulomb photon — *conditional* on bricks (1)–(3) of §6.
- **CN-ICE-07 [ASSERTED, not proven]** That the octet-truss constrained theory sits on the
  deconfined side of compact-U(1) (by pyrochlore analogy).
- **CN-ICE-08 [FALSIFIED as a free-parameter route]** "Geometry alone fixes a photon on the
  windows." No: the phase depends on n̄; superfluid at natural occupation, tuned otherwise.

---

## §0.5 — THE PREMISE, STATED AS A COST (verbatim)

> This continues a **hypothetical new construction**, not a repair of the written theory. The
> corpus is a single S¹ complex scalar on the sphere picture; putting a *constrained* U(1) gauge
> field on the void windows is a new theory. A verdict of "hard constraint → massless photon" does
> **not** vindicate BCT-as-written — it identifies a *new theory worth writing down*, which would
> then owe (1) a **derivation that a genuine double layer actually imposes that hard local
> constraint** — not an assumption that it does — and, separately and later, (2) its coupling to
> matter and (3) a derivation of α. A verdict of "soft → single phonon" means the window route
> collapses to the one gapless mode the corpus already has, and — with Gate LINK (massive) and Gate
> DL (no Higgs mass, phase undetermined) — **exhausts the audited link-variable routes to a
> massless two-polarisation photon on the BCT lattice.** A verdict of "needs a tuned occupation" is
> the same epistemic situation the census closed for any dimensionful input fixed after the fact.

## §0.6 — WHAT SETTLING THIS BUYS (verbatim)

> This gate decides whether the double-layer link theory has a massless photon or collapses to the
> corpus phonon, and whether any massless outcome is fixed by geometry or bought with a new input.
> It does not decide whether that photon couples correctly to matter, reproduces QED, or yields α —
> each a separate later gate. A geometry-fixed "hard constraint → massless photon" verdict is the
> first route in the whole audit to clear the representation wall (G′) **without a free parameter** —
> significant, but only the beginning of a new theory, not a vindication of BCT, and still owing the
> proof that a double layer really is that constraint. A "soft → phonon," "confined," or "needs a
> tuned occupation" verdict does not refute the void geometry (the packing, the network, α₀, ξ
> stand) — it means the photon cannot be built on the windows either, and the link-variable routes
> are exhausted.

---

## 8. WHAT THIS GATE DID **NOT** ESTABLISH

- It did **not** prove a double layer *is* the hard constraint (the opposite is the default; the
  hard route's one load-bearing brick is unfilled).
- It did **not** address coupling to matter, reproduction of QED, or the value of α — separate later
  gates.
- It did **not** use any corpus numerical value (MINIMAL_BCT unavailable under quarantine); the
  determinations are structural/symbolic. A numeric n̄, ξ/a would only *locate* the (superfluid)
  system relative to the r-threshold; it cannot manufacture a geometry-fixed photon.
- It did **not** refute the void geometry: packing, network, α₀, ξ are untouched. The finding is
  narrow — **the photon cannot be built on the windows this way; the link-variable routes are
  exhausted.**

*Outcome matches stop condition **SC-ICE-1** (primary), with the hard route documented as reaching
at best SC-ICE-2. No prompt defect.*
