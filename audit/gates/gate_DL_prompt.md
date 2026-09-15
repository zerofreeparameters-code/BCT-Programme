# GATE DL — DOES A DOUBLE-LAYER GAUGE FIELD ON THE FCC VOID NETWORK STAY MASSLESS, OR HIGGS?
## Cold Ledger gate. Fresh thread. Pre-register by SHA-256 **from the file the session receives.**
## HYPOTHETICAL-CONSTRUCTION gate — audits a proposed new theory, NOT the written corpus (see §0.5).

**The question.**

> The BCT audit closed the photon on the *sphere/site* picture: a single-phase (S¹) field gives one
> polarisation, not two (Gate G′). Gate LINK then tested generic *link* variables on the lattice and
> found they do give two polarisations — but the photon came out **massive** (an Abelian–Higgs /
> Meissner mechanism: a charged condensate screened the gauge field). The proposed reframe: put the
> active structure — the **double layer** — not on the spheres but on the **windows connecting the
> interstitial voids**, so the gauge field lives on the links of the *connected, loop-rich* FCC void
> network (cycle rank b₁ ≈ 1 per node, confirmed). A double layer is a **dipole** sheet (a
> potential jump / neutral charge configuration), not a **monopole** (net-charged) condensate — and
> a Meissner mass in the Anderson–Higgs mechanism comes from a *charged* condensate. **So: does a
> double-layer U(1) gauge field on the FCC void network stay MASSLESS (an unbroken U(1) → a genuine
> photon candidate with two isotropic polarisations), or does it Higgs to a MASSIVE photon like Gate
> LINK's, or confine (compact-U(1) confinement) to no propagating photon at all?** The decisive
> physics is whether the dipole (double-layer) structure avoids the charged-condensate Meissner mass
> that gapped LINK's photon.

Notices **CN-DL-01** onward.

## 0 — HANDOFF, QUARANTINE, SCOPE

**0.1 — HANDOFF.** Receive as a file at a commit-pinned `raw.githubusercontent.com` URL. `curl`
to disk, `sha256sum`, record the digest, **then** read. If pasted, claim no digest and say so.

**0.2 — QUARANTINE.** Do not consult the 9–15 Sep 2026 threads, BCT-X / Sandbox TOP, any `gate-*`
memory summary, or any concurrent gate. **Do not read `audit/notes/` or any `audit/gates/*/`
deliverable — in particular NOT `audit/gates/LINK/`.** You inherit only the single fact that Gate
LINK found generic link variables give *two polarisations but a MASSIVE photon (Abelian–Higgs)*, as
the benchmark this construction must beat; re-derive the mass question yourself. You **may** read
`audit/MINIMAL_BCT.md` for the written field content and constants, and standard references on
compact U(1) lattice gauge theory (Polyakov confinement in 3D), the Anderson–Higgs/Meissner
mechanism, and double-layer/dipole electrostatics.

**0.3 — INHERITANCE IS FORBIDDEN.** Derive yourself, cold: (a) the FCC void network as a graph
(nodes = octahedral + tetrahedral voids, edges = the triangular windows; its connectivity and
cycle rank b₁); (b) a **precisely defined** minimal U(1) link (lattice gauge) theory on that graph,
with the double layer given an explicit definition (a fixed dipole background on each window? a
dynamical dipole/condensate field coupled to the links? state which and justify); (c) the photon
mass by the standard criterion — is the U(1) unbroken (massless), Higgsed by a *charged* condensate
(massive, London/Meissner mass — compute it), or in the compact-U(1) confining phase (Polyakov,
no free photon)? If Gate LINK's mass value or mechanism, or the b₁ figure, reach you, declare and
re-derive.

**0.4 — SCOPE.** This gate defines and analyses a minimal double-layer gauge theory on the void
network and asks only whether its photon is massless / massive / confined, and whether the two
polarisations are isotropic. It does **not** ask whether the theory reproduces QED, couples to
matter, or gives the fine-structure constant — those are separate later gates. You may **not** tune
couplings to force masslessness; if masslessness requires a specific non-generic coupling, report it
as a cost (a parameter), not a success. Permitted outputs: "massless (unbroken U(1)),"
"massive (Higgsed — mass scale X)," "confined (no free photon)," or "the construction is
ill-defined."

## 0.5 — THE PREMISE, STATED AS A COST (reproduce verbatim; this is not the corpus).

> The written BCT corpus is sphere-centric and one-component (S¹): the double layer is a property of
> the *sphere* boundary (App J), and the field is a single complex scalar. Moving the double layer
> to the void *windows* and promoting the link field to a dynamical U(1) gauge theory is a
> **hypothetical new construction, not a repair of the written theory.** A verdict of "massless" does
> **not** vindicate BCT-as-written — it identifies a *new theory worth writing down*, which would
> then owe its own complete action, its coupling to matter, and a derivation of α (all separate,
> harder gates). A verdict of "massive" or "confined" closes this specific escape and, with Gate
> LINK, exhausts the audited link-variable routes to a massless photon on the BCT lattice.

## 0.6 — WHAT SETTLING THIS BUYS. Reproduce verbatim.

> This gate decides whether a double-layer U(1) gauge field on the FCC void network has a massless
> photon. It does not decide whether that photon couples correctly to matter, reproduces QED, or
> yields α — each a separate later gate. A verdict of "massless" is the first route in the whole
> audit to clear the representation wall that closed the sphere-picture photon (G′) — significant,
> but only the beginning of a new theory, not a vindication of BCT. A verdict of "massive/confined"
> does not refute the void geometry (the packing, the network, α₀, ξ stand) — it means the photon
> cannot be built this way either, and the S¹-and-its-link-extensions routes are exhausted.

## 1 — STEP 0: THE NETWORK AND THE GAUGE FIELD (build cold)

Construct the FCC (c/a=√2) void network as a graph: nodes = octahedral (coordination-to-tet 8) and
tetrahedral voids, edges = the triangular windows (nearest oct–tet separation). Report V, E,
components, and the cycle rank b₁ = E − V + C. Set up a U(1) link variable a_e ∈ (−π,π] on each
edge, plaquette flux on the independent cycles, and the Wilson/Villain action. Confirm b₁ > 0 (a
gauge field can carry independent fluxes) — necessary, not sufficient, for two polarisations.

## 2 — STEP 1: THE DOUBLE LAYER, DEFINED (the load-bearing modelling choice)

Give the double layer an explicit definition on the graph and state it plainly. Distinguish the two
physically distinct options and analyse the one(s) that correspond to a real double layer:
- **A fixed dipole background** on each window (a static potential jump): does it break U(1) at all,
  or is it a pure gauge / a fixed background flux? If it does not introduce a *dynamical charged
  condensate*, the U(1) is unbroken and the photon is massless — establish whether a genuine double
  layer is of this type.
- **A dynamical dipole (double-layer) condensate** coupled to the links: does the coupling carry
  **net charge** (→ Meissner mass, the LINK failure) or is it **charge-neutral / dipolar** (→ no
  Meissner mass, possibly a massless photon with modified short-range structure)? This is the
  decisive fork — derive which one a double layer realises.

## 3 — STEP 2: THE PHOTON MASS (the verdict computation)

By the standard criterion, determine the phase of the theory:
- **Massless (Coulomb phase):** U(1) unbroken; the gauge field propagates with two transverse
  polarisations and gapless dispersion. Confirm the dispersion is linear and gapless at long
  wavelength.
- **Massive (Higgs phase):** a charged condensate screens the field; compute the London/Meissner
  mass and compare to the FIRAS/masslessness bound (a nonzero photon mass at the condensate scale
  is falsified). This is Gate LINK's fate — does the double-layer share it?
- **Confined (compact-U(1), Polyakov):** in 3D compact U(1), monopole proliferation confines and
  gaps the photon; check whether the network theory is in this phase (does the double-layer/dipole
  structure suppress monopoles and protect a Coulomb phase, or not?).

State which phase the double-layer network theory is in, and why the dipole (vs monopole) structure
does or does not change the LINK outcome.

## 4 — STEP 3: POLARISATIONS AND ISOTROPY

If massless: confirm **two** transverse polarisations (not one, not three) and that the propagation
speed is **isotropic** — cross-check against the FCC stiffness isotropy (which holds uniquely at
c/a=√2; a photon with direction-dependent c is falsified by the same bound that constrains the
acoustic metric). A massless photon that is anisotropic still fails.

## 5 — STEP 4: THE STEELMAN

**Required.** Construct the strongest case that the double-layer network photon is massless: the
dipole structure carries no net charge, so no Meissner mass; the loop-rich network supports a
Coulomb phase; double layers are the natural home of a gauge potential jump. If it succeeds, say so
**prominently** — this gate must certify a massless photon if the construction genuinely gives one.

## 6 — STOP CONDITIONS

**SC-DL-1.** The photon is MASSIVE (a charged condensate / Meissner mass, as in Gate LINK, or the
double-layer coupling carries net charge). → The photon route closes again; report the mass scale.
**SC-DL-2.** The photon is CONFINED (compact-U(1) confinement; no free propagating photon). →
Report; no photon this way.
**SC-DL-3.** The photon is MASSLESS, propagating, with **two isotropic** polarisations, and the
masslessness is protected by the double-layer (dipole, uncharged) structure without a tuned
coupling. → **Favourable: the first route past the representation wall.** A new theory worth
writing; hand "couples to matter / reproduces QED / gives α" to separate later gates. Do not
overclaim.
**SC-DL-4.** The double-layer cannot be given a consistent gauge-theory definition on the network,
or masslessness requires a tuned non-geometry coupling. → Halt / report the parameter cost.

**If the outcome matches no stop condition, record it as a prompt defect.** **No stop condition
licenses a favourable conclusion, and none licenses an unfavourable one.**

## 7 — DELIVERABLE

Digest or refusal · search-space coverage first (the network build) · verdict first · the explicit
double-layer definition (§2) · the phase determination with the mass/confinement computation (§3) ·
the polarisation-count and isotropy check (§4) · the steelman · CN-DL notices tiered PROVEN /
CONJECTURE / ASSERTED / FALSIFIED · scripts (deterministic) · contamination statement · **§0.5 and
§0.6 reproduced verbatim** · what the gate did **not** establish (it does not give QED, matter
coupling, or α).

**Revise notices clause by clause.** **At close, produce a `git format-patch` adding the
deliverable, scripts and as-run prompt under `audit/gates/DL/`. Do NOT modify `audit/NEXT.md`.**

*Written 15 September 2026. Not executed. Pre-register before use. Hypothetical-construction gate.*
