# Building the DL theory from scratch — scoping note

**Written:** 12 November 2026, Claude (Fable 5.1), in the SONO review thread, at Michel's request
("this first pls" — the DL door; "I'm flexible when it comes to the shape of the Model, I'm just
after the truth").
**Status:** SCOPING NOTE, same-session, **not a gate**. Everything favourable here is capped at
CONJECTURE. Its job is to say what "building DL" means, what it would cost, and which gate goes
first. Nothing below moves a tier.
**Sources read cold for this note:** `audit/gates/DL/gate_DL_RESULT.md`, `STIFF/STIFF_RESULT.md`,
`ICE/gate_ICE_RESULT.md`, `PROMOTE/gate_PROMOTE_result.md`, `audit/MINIMAL_BCT.md` — all at
`9114b6e`. Numbers below from mpmath at 30 digits.

---

## 1. What Gate DL actually established (15 Sep 2026, hypothetical-construction gate)

DL asked: put a U(1) gauge field on the links of the FCC void network, with a "double layer" on
the windows — is the photon massless, or does it Higgs?

- **PROVEN:** a double layer is a *neutral dipole*, so it gives no Meissner/Higgs mass (the mass is
  ∝ q²; q = 0). It only shifts the photon's speed (a dielectric constant). CN-DL-02/03.
- **PROVEN:** the void network is isotropic at leading order (edge tensor exactly I/3; O_h forces
  ε_ij ∝ δ_ij) and loop-rich (b₁ = 5 per primitive cell), so two isotropic transverse polarisations
  are available. CN-DL-01/04.
- **OPEN:** masslessness still needs the residual compact-U(1) theory to sit in its (3+1)D Coulomb
  phase, β > β_c. The dipole does nothing about that. DL did not derive β. CN-DL-06/07.
- **Stated in its own §0.5:** this is a new construction, not the corpus. A "massless" verdict
  identifies a theory worth writing, which then owes its action, its matter coupling and its α.

**A point DL makes that is easy to miss.** Its realisation (A) — a *fixed* dipole background — is
either pure gauge or a static flux; it has no dynamics and no effect on the photon. So the double
layer's only job in DL is to be *the thing that is not a charged condensate*. Strip the word away and
the construction is: **lattice Maxwell on the FCC void network, decoupled from the superfluid.**
That is what "building DL from scratch" builds. It is worth being clear about this before anyone
is disappointed later.

## 2. The obstacle before DL's obstacle

DL ran at 10:24 on 15 Sep on the premise that a window double layer exists. STIFF (12:19 the same
day) found that a neutral single-component GP condensate hosts **no well-defined double layer at
all**: its only local charge is particle number, the window is reflection-symmetric, so the dipole
is zero by symmetry — not small, absent (SC-STIFF-5). ICE (11:00/11:43) found that a double layer
put in by hand is a **soft** coupling: no hard Gauss law, hence no gauge structure, hence no
Coulomb phase at any occupation (SC-ICE-1, escape SC-ICE-2 unavailable). PROMOTE (15 Sep) found the
geometry selects **no** promotion of the field content beyond S¹, and that richer local degrees of
freedom could supply a hard Gauss law only with inputs the packing does not fix (SC-PROMOTE-1/5).

So the honest statement of the DL programme is: *the written medium cannot supply the gauge field;
it has to be added; what is the cheapest addition, and does geometry fix any of its parameters?*

## 3. Options for the addition, with costs

"Cost" counts inputs not fixed by the void geometry, in the style of TWIST's cost table.

| # | What is added | Window dipole? | Gauge field with a hard Gauss law? | Higgs mass? | β fixed by geometry? | Inputs | Status |
|---|---|---|---|---|---|---|---|
| A | A second condensate component (e.g. App JH's interior/exterior pair) with opposite number weight, so the two density profiles differ across a window | **Yes** — two profiles can give an odd (dipole) combination; this is exactly STIFF's row (c), which fails only for *one* component | **No** — a dipole is not a gauge field | n/a | n/a | second field, its coupling, the sign of the weight (3) | Supplies the dipole brick only; on its own does not reach a photon |
| B | A fundamental compact U(1) link field on the void network (Kogut–Susskind rotors; Gauss law imposed), with the superfluid neutral under it | not needed (DL realisation A) | **Yes, by construction** | **No** (DL, PROVEN) | **Open.** Candidate: see §4 | the field (1); β unless derived (1); what carries its charge (1); the α identification (1) | **DL's own construction. The live option.** |
| C | An *emergent* gauge field from a constraint on the window graph (an ice rule: divergence-free flux at every void node — 2-in-2-out at tet nodes of degree 4, 4-in-4-out at oct nodes of degree 8) | — | In principle (this is how quantum spin ice gets a photon) | — | would be | a hard constraint term and a ring-exchange dynamics on discrete window variables (2) | **Probably closed at desk level:** the only discrete window variable the superfluid offers is quantised vortex flux, whose dynamics is the dual 2-form theory — 1 degree of freedom (QED-DERIV, T2). PROMOTE already found FCC lacks the ice geometry for site variables. A gate could confirm; not recommended first. |
| D | Give the condensate genuine electric charge on a neutralising background (jellium) | yes | needs an added gauge field anyway | **Yes** — charged condensate ⇒ Meissner mass (LINK; DL's charged branch) | — | — | **Dead.** This is a superconductor, not a vacuum. |
| E | Two oppositely charged components (neutral plasma condensate) | yes | needs an added gauge field anyway | **Yes** — each component contributes q²ρ to the mass | — | — | **Dead.** |

Only B survives as a route to a photon; A is at most a supplement to B, and B does not need it.

## 4. The one place geometry might fix β (desk observation, CONJECTURE)

DL's unfilled brick is "derive β from the Gross–Pitaevskii stiffness J and the window geometry,
then compare with β_c". There is an identity worth putting on the table before any gate:

    1/(4π α₀)  =  1/(4 r_oct r_tet)  =  2 ξ²/a²  =  10.742018   (exact, by the definitions of α₀ and ξ)

So *if* the plaquette coupling of the added link field were identified with the dimensionless
phase stiffness of the medium — β = 2ξ²/a² — then β ≈ 10.74, against β_c ≈ 1.01 (hypercubic) or
0.615/1.230 (D4, CRIT2's two conventions). That is a factor of 10–17 inside the Coulomb phase, and
the 1.5 % α₀-vs-α gap is irrelevant to it (β = 10.90 at CODATA α). The corpus already uses this number
— App E.1 §3.3 writes J = 1/(4πα₀) = 10.74 as a monopole-action parameter (Gate QED, CN-QED-04 found
that section's arithmetic inconsistent, but the parameter is there).

**Why this is not yet a brick.** A gauge field's plaquette coupling is the energy of a loop of
*field*, not of a loop of superfluid phase. In the nearest laboratory analogue — a Josephson-junction
array — the link coupling is E_J (the phase stiffness) but the plaquette coupling is set by the loop
inductance, an independent scale. For β = 2ξ² to be *derived* rather than asserted, the added field
would have to be shown to inherit the medium's stiffness, and the medium is neutral under it in
option B. The forecast below is that it does not.

## 5. Gates, in order

1. **Gate DL-STIFF** (analytic; cheap; decides the parameter count). *Question:* in option B, is the
   plaquette coupling β of the added link field fixed by the medium — specifically, is β = 2ξ²/a²
   derivable from the action in MINIMAL_BCT §1.2 plus the void network — or is it a free input?
   *Codes:* SC-DLS-1 derived (with the derivation and its one-line kill test); SC-DLS-2 asserted /
   free; SC-DLS-3 derived but a different number (report it against β_c). *Forecast:* SC-DLS-2,
   about 70 %; SC-DLS-3 about 20 %. This gate settles whether DL is a zero- or one-parameter theory.
2. **Gate DL-BETA** (numerical; hours; publishable whatever the theory does). *Question:* β_c of
   compact U(1), Wilson action, on the (3+1)D lattice = FCC void network × time, with β_t = β_s
   pre-registered as the convention and the space–time anisotropy question recorded, not solved
   (CN-QED-09 echo). Reuse CRIT2/LATT machinery, but the simulator must be graph-based (nodes =
   voids, links = windows, plaquettes = minimal cycles plus temporal rectangles) — the void network
   is not a root lattice. Z4 calibration against 1.0111 and the D4 regression as in LATT.
   *Forecast:* β_c of order 1; the exact value is the result. Together with DL-STIFF it decides
   CN-DL-06.
3. **Gate DL-MATTER** (only if 1–2 survive): what carries the charge of the added field? The only
   BCT matter is vortex strings, neutral under a field the superfluid is neutral under. Assigning
   them charge is a fourth input. Without this step the photon couples to nothing.
4. **α** last, and honestly: the α question returns in exactly the form FWD/STAT/QED closed it
   (α₀ = 1/134.99, the correction map to 137.036 is a selected fit). DL changes nothing there.

## 6. What the prize is, said once

If all four steps come out favourably, the result is a **lattice gauge theory on the FCC void
network** whose BCT content is (i) the lattice — isotropy and two polarisations, PROVEN already —
and (ii) possibly its stiffness, if DL-STIFF surprises. It is not the written corpus, it is not
"one medium", and it is not zero-parameter unless step 1 returns SC-DLS-1. It would be a true thing
about whether a lattice superfluid can carry light, which is what was asked for.

## 7. Forecast and interest

Analyst's forecast: DL-STIFF returns SC-DLS-2 (free input) — the added field has no reason to
inherit the phase stiffness of a medium that is neutral under it. DL-BETA returns an O(1) number
with β_c for the void network somewhere between the D4 and hypercubic values. The programme then
stands as a one-parameter lattice-QED-on-a-void-network, with the lattice as its only geometric
content. Interest: the author of this note wrote the SONO card and the 12 Nov NEXT.md and has argued
in this thread that the written theory cannot carry a photon; the forecast is consistent with that
and should be read as such.
