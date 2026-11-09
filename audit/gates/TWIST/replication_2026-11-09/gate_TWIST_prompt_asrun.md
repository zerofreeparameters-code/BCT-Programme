# Gate TWIST — pre-registration card

**Programme:** BCT Superfluid Lattice Model, Cold Ledger
**Card written:** 8 November 2026, Claude, at Michel's request ("start with 1 and proceed in order")
**Status:** PRE-REGISTERED, NOT RUN.
**Type:** construction attempt with kill conditions (theory gate: derivation plus symbolic and numeric checks).
**Depends on:** Gates QED-DERIV, PROMOTE, JHF, KL, C1, BC, STIFF, ICE, LINK (all closed). The motivating desk-checks are in the 8 Nov 2026 session record, which is blocked for this run (section 3).

---

## 1. Why this gate

Gate QED-DERIV proved that a single compact scalar field (vacuum manifold S¹) cannot produce a photon. Gate PROMOTE showed the geometry does not select a richer field. So electromagnetism cannot be derived from BCT as written.

Michel's picture of the sphere interiors needs a richer field anyway. Each sphere holds a hopfion: the same superfluid as outside, moving as a toroidal vortex with an hourglass throat, held by the sphere's double layer. A Hopf knot needs a two-component field (ℂ², unit direction n ∈ S²).

A two-component field carries a built-in, EM-like connection

  a = −i χ†∇χ,  with ∇×a = ½ n·(∂n × ∂n)  (Mermin–Ho),

and the knot's Hopf number is that connection's helicity, H = (1/4π²) ∫ a·(∇×a).

**This gate asks whether that twist field can be real light, and whether the sphere shells can then hold the knot.** The four questions are taken in order, as Michel asked.

## 2. The added assumption (declared up front)

- **A1 (declared input):** the medium carries a two-component order parameter Ψ = √ρ χ, with χ ∈ ℂ² and |χ| = 1, inside and outside the spheres (Michel: "the interior is exactly the same as the OHC").
- This is a promotion beyond S¹. By Gate PROMOTE it is a **free input**, and it is counted as one in the cost table (section 7).
- The result is a modified BCT. Nothing in this gate reopens QED-DERIV, which stands as a theorem for the one-component field.

## 3. Blinding and contamination

Before starting, switch off "Search and reference past chats" and "Generate memory from chats" in Settings. Switch them back on after the run.

Until Step 4 is complete and its answers are written down, the run must **not** open:

- the 8 Nov 2026 session record (`BCT_SessionRecord_2026-11-08.pdf`)
- `DESK_hopfion_in_sphere_RESULT.md`
- the desk-check scripts `partA_neutral.py`, `partB_spheromak.py`, `rings.py`, `rings2.py`
- the memory file `areas/hopfion-interior-idea.md`

It **may** read:

- the gate results of QED-DERIV, PROMOTE, JHF, KL, C1, BC, STIFF, ICE and LINK (closed findings)
- App J, App JH and Letter 36 (the interior sources)
- the literature, including Babaev, Faddeev & Niemi, Phys. Rev. B 65, 100512 (2002), arXiv:cond-mat/0106152

If blocked material is seen early, say so in the deliverable. The run continues but is marked contaminated.

## 4. The model (fixed for the whole run)

- **Lattice:** FCC (BCT at c/a = √2), nearest-neighbour distance a = ℓ_P. Sphere radius R = a/2. There are 6 octahedral voids (r_oct = (√2−1)/2 · a) and 8 tetrahedral voids (r_tet = (√6−2)/4 · a) around each sphere, and each sphere touches 12 neighbours.
- **Bulk functional (V0):** the App JH §3.1 bulk terms for Ψ ∈ ℂ²:
  F = ∫ [ (ħ²/2m)|∇Ψ|² + (g/2)(|Ψ|² − n₀)² ] d³r.
  - Use the corpus healing length ξ = a/√(8πα₀) = 2.31754 ℓ_P as given. Per CN-C1-04 it is asserted, not derived; use it, don't repair it.
- **Shell term:** the App J/JH surface term (α₀ħ²/2mR)∮|Ψ|² dA at r = R. As written it is U(2)-symmetric (Gate BC: its coefficient is fitted).
- **Variables:** Ψ = √ρ χ, n = χ†σχ, a = −iχ†∇χ (the CP¹ connection), φ = overall phase.
- **Charge:** none, unless a question below explicitly grants it as a counted input.

## 5. The questions, in order

Each question is scored **PASS** (follows from the model with no new input), **FAIL** (does not follow, and cannot without changing the model), or **BOUGHT** (follows only after adding an input; each input is listed and counted). A later question may be answered conditionally on an earlier one having been BOUGHT; it must say so.

### Q1. Does the twist field get its own Maxwell-type energy from the medium itself?

- **(a)** Write |∇Ψ|² in (ρ, n, φ, a) variables and verify the identity |∇χ|² = ¼|∇n|² + a² on random smooth fields (numerically, to 1e-10).
- **(b)** Determine whether a enters V0 only through the superflow combination (∇φ + a), i.e. whether it is slaved to the texture or carries independent degrees of freedom.
- **(c)** Determine whether a term c_F (∇×a)², i.e. c_F (n·∂n×∂n)², with **c_F > 0**, is generated:
  - at tree level, and
  - after integrating out density fluctuations in a gradient expansion (one loop is enough).
  - Give the sign, and the scaling with ξ and a.
- **PASS** only if c_F > 0 is fixed by corpus quantities **and** a carries independent propagating degrees of freedom.
- The BFN mechanism (an F² term arising from a magnetic B² term in a **charged** two-condensate system) counts as BOUGHT here, because it needs charge plus a Maxwell term as inputs.

### Q2. Does it stay massless, with two polarisations, in the voids?

- For the action from Q1 (if BOUGHT, grant the minimal Maxwell term −(1/4e²) f² and count e as a new coupling), find the mass of a:
  - in a uniformly condensed medium (Higgs/Meissner: a mass set by the superfluid stiffness)
  - in a medium that is condensed in the shells and not in the voids, if and only if the model supplies such a location-dependent phase
- Count transverse polarisations.
- **PASS** only if a is massless with two transverse polarisations **in the voids**, using corpus geometry and densities alone.
- If the corpus medium is the same everywhere (App J: same density inside and out), a uniformly condensed medium gives a massive a: **FAIL**.

### Q3. Is it screened in the shells, so they can hold the knot?

- Give the penetration depth λ_shell of a's field in the shell region and compare it with the shell thickness, and with R.
- For a relaxed (force-free) knot inside a sphere with B·n = 0 at the wall, the virial theorem fixes the mean wall pressure at ū/3. Check whether the shell can supply it (order of magnitude), with ū in condensation-energy units.
- **PASS** only if the screening and its strength follow from the model.

### Q4. Does a current-carrying shell follow from the medium, or must it be added?

Score each of the following DERIVED / ASSERTED / ABSENT, citing the corpus:

- **(i) Real charge** in the shell, beyond particle number (Gate STIFF: a neutral single-component GP hosts no well-defined double layer).
- **(ii) Counter-moving layers.** The two layers of a double layer moving together carry cancelling currents.
- **(iii) Insulating contacts** at the 12 touching points per sphere. Check the argument that connected conducting shells at Planck spacing form a wire medium with a plasma cutoff near the Planck frequency, opaque to all observed light (Pendry et al., Phys. Rev. Lett. 76, 4773, 1996). Give an order of magnitude and say whether it holds.
- **(iv) A grip term:** a direction-dependent shell term that pins n on the shell, without which the Hopf number is not protected per sphere (a ball with a free edge).
- **PASS** only if all four are DERIVED.

## 6. Verdict codes

- **SC-TWIST-0 (card defect).** The model or questions cannot be evaluated as written. Say what is missing; no physics verdict.
- **SC-TWIST-1 (kill at Q1).** No Maxwell-type term for the twist field arises from the medium; it stays slaved to the texture.
- **SC-TWIST-2 (kill at Q2).** A Maxwell-type term arises or is granted, but a is massive or has fewer than two polarisations in the voids.
- **SC-TWIST-3 (kill at Q3/Q4).** Light survives in the voids, but the shell cannot screen the field or hold the knot without added inputs (list them).
- **SC-TWIST-4 (survivor).** All four questions PASS with no input beyond A1. The construction moves to CONJECTURE and a quantitative follow-on gate is opened.

Every verdict reports the full cost table.

## 7. Cost table (mandatory)

List every input used beyond the BCT corpus as written:

| # | Input | Free number? | Where needed |
|---|---|---|---|
| 1 | A1: ℂ² order parameter | — (structural) | all |
| … | | | |

Add one row for each coupling, charge, surface term or phase assumption introduced along the way.

## 8. No-fit clause

- No coupling may be tuned to make a question PASS. A needed coupling is counted, not fitted.
- No numerical comparison with α, 137, or any measured constant is part of this gate.
- The lattice, ξ, R and the void radii are fixed by section 4 and do not change during the run.
- This gate is not evidence for or against the void geometry.

## 9. Analyst's disclosure (this card is not blind on its author's side)

The author ran same-session desk-checks on 8 Nov 2026 (blocked in section 3) and has read the BFN abstract and equations. Forecast, recorded so it can be scored:

- **Q1:** FAIL for the neutral V0, consistent with Gate KL's finding that the GP reduction gives a destabilising quartic, not +F². BFN's stabilising term needs charge plus a Maxwell input, so it would be BOUGHT.
- **Q2:** FAIL for a uniformly condensed medium (a Meissner/Higgs mass, the same wall as LINK and QED). It could pass only if the medium is condensed in the shells and not in the voids, which the corpus does not supply.
- **Q3:** conditional on Q2. Not reachable without location-dependent condensation.
- **Q4:** (i) ABSENT/ASSERTED; (ii) ABSENT; (iii) ABSENT, and the wire-medium argument holds; (iv) ABSENT.
- **Forecast verdict:** SC-TWIST-1, with Q2 also failing conditionally. A cost of at least 3 inputs (A1, a charge/Maxwell coupling, a location-dependent phase or a grip term) to reach a working picture.

## 10. Known limitations

- Only the minimal two-component extension is tested. Richer order parameters (rank-2, ³He-like) are out of scope; Gate OP and CN-OP-14 cover those.
- Gradient expansion only. Non-perturbative effects (monopoles of the CP¹ field, compactness) are noted, not computed.
- The shell is the corpus's delta-shell. A finite-thickness shell is out of scope unless needed to state λ_shell.

## 11. Run protocol

- Fresh thread inside the BCT project. One gate per thread. Opus-class model.
- Settings step from section 3, before and after.
- Fetch this card by commit-pinned raw URL with curl to disk, compute its SHA-256, and compare it with the pre-registered digest **before reading it**.
- **Deliverable:** `gate_TWIST_RESULT.md`, containing:
  - the hash check
  - a contamination statement
  - Q1–Q4 with their scores
  - the verdict and the cost table
  - notices CN-TWIST-01…
  - the disclosure scored
  - a plain-language summary for Michel
- Save the scripts. Commit under `audit/gates/TWIST/` as a patch for Michel to apply.
- Same-session results are capped at CONJECTURE.
