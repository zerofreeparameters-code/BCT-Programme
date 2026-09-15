# GATE ICE — RESULT
## Is the double layer a HARD local constraint (Gauss law) or a SOFT coupling on the FCC void network?
**Cold Ledger gate · hypothetical-construction · run 15 September 2026 · one gate, one thread.**

---

## VERDICT (first)

**SC-ICE-1 — SOFT.** A genuine (neutral) double layer on the void windows is a **soft coupling**, not a
hard local Gauss-law constraint. In the realised soft branch the theory is an ordinary lattice
superfluid on the FCC void network; at natural (condensate) occupation its **single** gapless mode is
the **corpus phonon**. There is **no new photon and no second polarisation.**

**Strengthened beyond SC-ICE-1:** the parameter-cost escape (SC-ICE-2) is **not available** in the soft
branch. In three dimensions a soft compact-U(1)/rotor theory has **no deconfined Coulomb phase**
(Polyakov confinement); its only phases are superfluid (condensed → Goldstone phonon) and Mott
(gapped). **No occupation and no coupling value buys a massless photon on the windows.** A Coulomb
phase would require the HARD branch, and the HARD branch requires a brick the physics refuses to
supply (see Steelman, §6).

**Consequence for the audit.** With Gate LINK (massive photon) and Gate DL (no Higgs mass, phase left
open), this closes the last open link-variable route: **the audited link/window routes to a massless
two-polarisation photon on the BCT lattice are exhausted.** This does **not** refute the void
geometry — the packing, the network built below, and the healing length ξ stand untouched. It means
the photon cannot be built on the windows either.

---

## 0 — HANDOFF, QUARANTINE, CONTAMINATION

**Digest / refusal.** The gate arrived as **pasted context** (a chat-inlined document), **not** as a
commit-pinned `raw.githubusercontent.com` file curled to disk. Per §0.1, **no canonical digest is
claimed.** A SHA-256 of the as-run text is recorded in `gate_ICE_prompt_asrun.md`'s companion line
for provenance only; it is the digest of the as-run transcript, **not** of the canonical pinned file.
To pre-register properly, hand me the commit-pinned URL and I will hash the checkout file.

**Contamination statement.** I did **not** read `audit/notes/`, any `audit/gates/*/` deliverable
(in particular not `DL/` or `LINK/`), any `gate-*` memory summary, the Cold Ledger, or any concurrent
gate. Format/toolchain conventions (patch-bundle delivery, deterministic-script discipline) were the
only project context consulted, and they carry no gate physics. The two benchmark facts named in the
gate were **re-derived** here, not trusted (§CN-ICE-02). No DL/LINK number (mass value, b₁, girth,
coupling ratio, or occupation threshold) reached this session; every network number, the coupling
ratio, and the hard-vs-soft determination were derived cold. Standard references used, per §0.2:
Polyakov compact-U(1) confinement in 3D; the quantum-spin-ice / emergent-U(1) Coulomb-phase
construction and its ice-rule Gauss law; the boson-Hubbard / Josephson-array phase diagram; and
double-layer / dipole electrostatics.

---

## 1 — SEARCH-SPACE COVERAGE: THE NETWORK + RING-EXCHANGE GEOMETRY (built cold)

`net_ice.py` builds the FCC (c/a=√2) interstitial graph from first principles: nodes = octahedral (O)
+ tetrahedral (T) voids; an edge exists iff two voids **share a triangular window = a face = exactly
three common bounding atoms** (computed, not assumed). Deterministic; run on a 3×3×3 periodic supercell.

| Quantity | Value (per conventional cell) | Tier |
|---|---|---|
| Voids V | **12** (4 octahedral + 8 tetrahedral) | PROVEN |
| Windows E | **32** | PROVEN |
| Degrees | O: **8**, T: **4** (handshake 4·8 = 8·4 = 32 ✓) | PROVEN |
| Edge types | **100 % O–T** → graph is **bipartite** | PROVEN |
| Components C | 1 (connected) | PROVEN |
| Cycle rank b₁ = E−V+C | **→ 20 per cell** (finite-size 20.04 at L=3) | PROVEN |
| Girth | **4** (bipartite squares O–T–O–T) | PROVEN |
| Shortest (4-)loops | **24 per cell** | PROVEN |

Verified by hand: O(½,½,½) and O(½,0,0) share the two T neighbours (¼,¼,¼) and (¾,¼,¼), closing an
O–T–O–T square → girth 4. T–T pairs share only an **edge** (2 common atoms), never a face, which is
why the graph is strictly bipartite O–T. The **Gauss-law candidate** a hard constraint would fix is
the signed sum of window fluxes at each node (the lattice divergence). b₁ ≫ 0 and the very short
girth (4) with 24 shortest loops per cell mean the network is **richly loopy** — ring-exchange, if it
were the leading dynamics, would be strong. This favours the HARD steelman geometrically; it does not
rescue it (§6).

---

## 2 — THE DECISIVE DETERMINATION: HARD vs SOFT  (CN-ICE-03)

**Both defined precisely.**
- **HARD** — the double layer fixes the **flux divergence** at every node: a local Gauss law /
  ice rule, `Σ_{j~i} E_{ij} = q_i` (fixed), enforced as an infinite-energy projector. This projects
  out simple condensation and leaves a constrained loop-only manifold whose leading dynamics is
  ring-exchange on the shortest loops — the quantum-spin-ice route to an emergent photon.
- **SOFT** — the double layer is a fixed **background link phase** `A_{ij}` (a frustration / offset)
  or a weakly-coupled field: it shifts the Josephson term `−J cos(φ_j − φ_i − A_{ij})` but does
  **not** forbid condensation.

**What a double layer physically is, and why it is SOFT.** A double layer is a **dipole sheet**: a
+σ / −σ pair separated by a small gap, carrying **no net charge**. Its defining electrostatic effect
is a **jump in the potential**, `ΔV = σd/ε₀`, with the **field continuous** across it (Gauss's law
sees zero enclosed charge). Translated into the emergent gauge language, a fixed potential jump across
a window is precisely a **fixed value of the connection on that link** — a background `A_{ij}`. It is
a boundary condition on the **potential difference**, i.e. on the connection.

A **hard Gauss law is a boundary condition on the flux *divergence*** — a different object. The two
are not interchangeable: fixing `A_{ij}` (a potential offset) neither quantises nor pins
`Σ_{j~i} E_{ij}` (the divergence), and it supplies **no energy gap** separating a constrained
manifold from its violations. A projector onto an ice manifold needs a **large local energy scale**
(a strong on-site/repulsion term, or geometric frustration + strong coupling) to gap out violations;
a neutral dipole sheet supplies a finite potential step, not that gap. **The double layer sets `A`,
not the Gauss law.** Electrochemically this is the familiar statement that a double layer is a
**capacitor** — a soft, `½CV²` energy store — not a constraint.

**Determination: a genuine neutral double layer realises the SOFT coupling.** PROVEN at the level of
electrostatics (neutral dipole sheet fixes the potential difference, not the divergence) together
with the standard identification (potential offset on a link = background connection = soft). The one
modelling premise is that the emergent structure is the rotor/link theory the gate posits; granting
that, softness follows. This is **not** `SC-ICE-5`: the object is perfectly well-defined; it is simply
**soft**, decidably so.

---

## 3 — THE PHASE (soft branch)  (CN-ICE-04, CN-ICE-05)

**J-cancellation test (`ratio_ice.py`, symbolic).** Map the Gross–Pitaevskii lattice superfluid to a
quantum-rotor / Josephson model with Josephson energy `E_J = 2 t n̄` and charging energy `E_C = U`.
With the tunnelling scale `t = ℏ²/(2ma²)`, the on-site interaction `U = g/a³`, and the healing length
`ξ² = ℏ²/(2mgn)` (density `n = n̄/a³`):

> **E_J / E_C = 2 n̄² (ξ/a)².**

**ℏ and m cancel exactly** — the microscopic stiffness and mass drop out (this is the sense in which
"J cancels"), leaving a pure dimensionless ratio of the **occupation n̄** and the **geometric ratio
ξ/a**. The theory is a **superfluid** — one gapless Goldstone mode — when `E_J/E_C ≳ 1`, i.e.
`n̄·(ξ/a) ≳ 1/√2 ~ O(1)`, and a **Mott insulator** (gapped) otherwise.

A BCT vacuum posited as a coherent condensate has `ξ ≳ a` and `n̄ ≳ 1`, hence sits **deep in the
superfluid regime**: its single gapless mode **is the corpus phonon**. No second polarisation, no
photon. → **SC-ICE-1.**

**Why softness forecloses the Coulomb phase entirely (the stronger result).** A pure **3D compact-U(1)**
gauge theory is, by **Polyakov's theorem, always confined**: magnetic monopoles proliferate and gap
the photon; there is **no deconfined Coulomb phase in 3D** without a mechanism that suppresses
monopoles. A soft double layer supplies **no such mechanism** — a background `A_{ij}` does not
suppress monopoles. So the soft branch has exactly two possibilities: **condensed** (Goldstone phonon,
the corpus mode) or **pure-gauge residual** (3D-confined, gapped). **Neither is a free two-polarisation
photon, at any occupation.** The DL-inherited "pure compact-U(1)" is real, but in 3D-and-soft it lives
in its confined/condensed regime, never a Coulomb phase. This removes the SC-ICE-2 escape from the
soft branch.

---

## 4 — POLARISATIONS, ISOTROPY, AND THE SCALAR-PHONON FALSE-POSITIVE GUARD  (CN-ICE-06)

No masslessness-with-a-vector arises in the realised branch, so §4's photon checks do not trigger —
but the false-positive guard is exactly the point. The soft gapless mode is the **phase Goldstone of a
complex scalar** `ψ = √n e^{iφ}`: **one** degree of freedom, a **scalar** (the density–phase mode),
with dispersion `ω = c_s|k|`. It is **not** a transverse vector and there is **no second mode** to
pair it into a two-polarisation photon. Any claim of a "photon" here would be the single scalar phonon
relabelled — the precise false positive §4 warns against. Guard **passes by exclusion**: the count is
one scalar, not two transverse vectors. (O_h isotropy — a rank-2 response ∝ δ_ij — would be relevant
only for a genuine vector sector, which is absent.)

---

## 5 — OCCUPATION / PARAMETER AUDIT  (CN-ICE-08)

The phase is controlled by `n̄²(ξ/a)²`. **ξ/a is geometry-fixed** (packing + healing length — a pure
function of the void structure). **n̄ (void occupation) is not fixed by the void geometry** — it is an
independent thermodynamic input. But the audit outcome does **not** depend on tuning it: across the
**entire** physically sensible range the soft branch delivers either the single phonon (condensed) or
a gap (Mott), **never a photon**. So the verdict SC-ICE-1 needs **no new input** to reach; and no
choice of n̄ converts it to a favourable one. By the corpus's own product-vs-ratio test, geometry does
not do the work of making a photon here — and neither does any fresh number.

---

## 6 — THE STEELMAN (required)

**Strongest case for a favourable (SC-ICE-3) verdict.** Grant, hypothetically, that the double layer
imposes a **hard** local Gauss law. Then the FCC void network is an unusually good host for an emergent
photon: girth **4** with **24 shortest loops per cell** gives dense, short ring-exchange; the ice
Gauss law would **suppress the monopoles** that otherwise confine 3D compact U(1); and a **deconfined
Coulomb phase** with a gapless emergent photon — geometry-fixed, no tuned occupation — could follow, as
in quantum spin ice. If that hard constraint held, this **would** be the first route in the audit to
clear the representation wall (G′) without a free parameter, and I would certify it prominently. The
geometry genuinely cooperates.

**The one unfilled brick, named exactly.** The steelman needs the double layer to **be** that hard
local Gauss-law projector. It is not. A neutral dipole sheet is a **potential jump = a fixed background
connection `A_{ij}`** (soft), which pins the potential difference, not the flux divergence, and gaps
nothing (§2, CN-ICE-03). Turning it "hard" requires a **separate large energy scale** (a strong
on-site repulsion or geometric frustration) that the double layer **does not supply** and that would
be a **new ingredient**, not a consequence of the dipole sheet. So the steelman's load-bearing brick
is precisely the one §0.5 flags: *"a derivation that a genuine double layer actually imposes that hard
local constraint — not an assumption that it does."* The honest physics supplies the opposite: a
derivation that it imposes a **soft** background instead. Brick status: **ASSERTED and false.** The
steelman fails.

---

## 7 — CN-ICE NOTICES (tiered)

- **CN-ICE-01 — PROVEN.** FCC void network (cold): V=12/cell (4 O + 8 T), E=32/cell, degrees O:8 T:4,
  100 % O–T (bipartite), connected, b₁→20/cell, girth 4, 24 shortest 4-loops/cell. (`net_ice.py`.)
- **CN-ICE-02 — PROVEN (benchmarks re-derived).** (i) A neutral double layer carries no net charge, so
  there is no charged condensate to Higgs the gauge field → no Anderson–Higgs/Meissner mass. (ii) The
  residual pure compact-U(1) is massless iff in a deconfined Coulomb phase, gapped (confined) otherwise.
- **CN-ICE-03 — PROVEN.** A genuine neutral double layer is a **soft** coupling: a potential jump =
  a fixed background connection `A_{ij}` (fixes the potential difference), **not** a hard Gauss law
  (which fixes the flux divergence and needs an energy gap the dipole sheet does not supply).
- **CN-ICE-04 — PROVEN.** Soft phase controlled by `E_J/E_C = 2 n̄²(ξ/a)²` (ℏ, m cancel); superfluid
  single Goldstone phonon for `n̄(ξ/a) ≳ 1/√2`; = the corpus phonon at condensate occupation.
- **CN-ICE-05 — PROVEN.** 3D compact-U(1) confines (Polyakov) absent monopole suppression; the soft
  branch supplies none, so it has no Coulomb phase — no occupation/coupling yields a massless photon.
- **CN-ICE-06 — PROVEN.** The single soft gapless mode is a scalar (density–phase Goldstone), one
  mode; it cannot masquerade as a two-polarisation transverse photon. False-positive guard passes.
- **CN-ICE-07 — CONJECTURE (branch) + PROVEN (refutation).** *If* the double layer were a hard Gauss
  law, the FCC network's short girth and dense ring-exchange plausibly give a geometry-fixed Coulomb
  photon (CONJECTURE — full ice computation not performed, unnecessary). *That* the double layer is
  **not** that hard constraint is PROVEN (CN-ICE-03). The steelman's brick is ASSERTED and false.
- **CN-ICE-08 — PROVEN.** ξ/a is geometry-fixed; n̄ is a non-geometry input; but the soft verdict is
  robust across all n̄ (phonon or gap, never photon), so no tuning is invoked and none rescues it.

No FALSIFIED notices (nothing in the corpus's void geometry is contradicted; the geometry stands).

---

## §0.5 — THE PREMISE, STATED AS A COST (verbatim)

> This continues a **hypothetical new construction**, not a repair of the written theory. The corpus
> is a single S¹ complex scalar on the sphere picture; putting a *constrained* U(1) gauge field on the
> void windows is a new theory. A verdict of "hard constraint → massless photon" does **not** vindicate
> BCT-as-written — it identifies a *new theory worth writing down*, which would then owe (1) a
> **derivation that a genuine double layer actually imposes that hard local constraint** — not an
> assumption that it does — and, separately and later, (2) its coupling to matter and (3) a derivation
> of α. A verdict of "soft → single phonon" means the window route collapses to the one gapless mode
> the corpus already has, and — with Gate LINK (massive) and Gate DL (no Higgs mass, phase
> undetermined) — **exhausts the audited link-variable routes to a massless two-polarisation photon on
> the BCT lattice.** A verdict of "needs a tuned occupation" is the same epistemic situation the census
> closed for any dimensionful input fixed after the fact.

## §0.6 — WHAT SETTLING THIS BUYS (verbatim)

> This gate decides whether the double-layer link theory has a massless photon or collapses to the
> corpus phonon, and whether any massless outcome is fixed by geometry or bought with a new input. It
> does not decide whether that photon couples correctly to matter, reproduces QED, or yields α — each a
> separate later gate. A geometry-fixed "hard constraint → massless photon" verdict is the first route
> in the whole audit to clear the representation wall (G′) **without a free parameter** — significant,
> but only the beginning of a new theory, not a vindication of BCT, and still owing the proof that a
> double layer really is that constraint. A "soft → phonon," "confined," or "needs a tuned occupation"
> verdict does not refute the void geometry (the packing, the network, α₀, ξ stand) — it means the
> photon cannot be built on the windows either, and the link-variable routes are exhausted.

---

## WHAT THIS GATE DID NOT ESTABLISH

- It did **not** prove a double layer *is* a hard constraint — it proved the opposite (it is soft),
  which is the disposal of the steelman, not a construction.
- It did **not** address QED reproduction, coupling to matter, or the fine-structure constant α —
  each a separate later gate, and all moot on the windows once the photon route is exhausted.
- It did **not** refute the BCT void geometry: the packing, the network built in §1, and ξ are
  untouched. Only the *window/link route to a photon* is closed.
- It did **not** rule out a photon arising by some entirely different mechanism (not link variables);
  it closes the audited link-variable family (LINK, DL, ICE), nothing beyond it.

*Run 15 September 2026. Scripts deterministic. One gate, one thread. Same-session status capped at
CONJECTURE per Whopper Protocol where a notice is tiered CONJECTURE; PROVEN notices are graph-theoretic
or standard-theorem facts independent of this session.*
