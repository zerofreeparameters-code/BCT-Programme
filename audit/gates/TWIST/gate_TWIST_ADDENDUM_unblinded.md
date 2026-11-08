# Gate TWIST — Unblinded addendum: the run compared with the 8 Nov desk-checks

**Written:** 8 November 2026, after the blind run closed. RESULT §§3–8 were fixed and checked first, and Michel switched the settings back on at 12:33.
**Status:** not a gate. Same-session, so capped at **CONJECTURE**. It does **not** change any blind score or the verdict SC-TWIST-1. Where it corrects the RESULT, it does so here, as errata (§5). The RESULT file itself is left as it was run.
**Script:** `scripts/twist_addendum_checks.py` → `output/twist_addendum_output.txt`.

---

## 0. What was opened now, and what could not be

**Opened** (via past-chat search, after the run): this morning's chat "Lost physics chat" (08:44–11:43). From it:
- desk-checks A, B and C as written there (the text of `DESK_hopfion_in_sphere_RESULT.md`);
- the source of `partA_neutral.py`, `partB_spheromak.py`, `rings.py` and `rings2.py` as quoted in the chat;
- the build text of the session record (its §§11–14);
- the discussion about voids and alignment.

**Not reachable:**
- The session-record PDF and the desk scripts' raw outputs lived in that chat's own workspace. Only the transcript survives, so desk-check C's numbers are taken as that chat reported them; I did not re-run them.
- The memory file `areas/hopfion-interior-idea.md`: this session has no memory tool.

**Reading of "spheres aligning along a particular axis".** In the earlier chat this meant the *spatial* axis of each knot (its hourglass throat) pointing along the BCT c-axis. That chat compared "all aligned" with "alternating up and down". TWIST §9 had read it as an *internal* axis (n → ẑ) or as pinning; §3 below covers the spatial reading.

---

## 1. Where the two agree

| Item | 8 Nov desk / session record | TWIST | Check now |
|---|---|---|---|
| Energy of a one-twist knot filling the sphere (same medium, ℂ²) | 191 (n-only) to 287 (with flow) ε_c ℓ_P³; **366–548×** the condensation energy in the sphere | 369× (n-only) | 193.0 / 289.5 → **369× / 553×**. The desk used a 181³ grid and comes out ~1% low. Same construction, independent code: **agree** |
| Static knot pulls inward (Derrick) | yes | yes (CN-TWIST-07) | **agree** |
| Shell term can't grip the twist (U(2)-symmetric); with a free edge there is no topological protection | yes | yes (Q4(iv); "H" slides 1 → 0) | **agree** |
| Relaxed knot pushes out; the wall must supply ū/3 | yes (exact) | 1.00000000 (CN-TWIST-13) | **agree** |
| Pressure at the equator = ū/2; centre = 4.71 ū; inner half-ball holds 36% | stated | — | **0.5000000000; 4.709; 36.31%: confirmed.** The ū/2 is exact: B² at the wall ∝ sin²θ, and its average is ⅔ |
| A fixed-charge (voltage-step) double layer exerts no magnetic pressure; currents are needed | yes | Q4(i) ASSERTED, (ii) ABSENT | **agree** |
| A superconducting exterior gives light a mass | yes (same-day correction) | Q2 FAIL (Anderson–Higgs) | **agree** |
| Touching shells form a Planck-scale mesh that blocks all light; the contacts must insulate | qualitative (microwave-door analogy) | quantitative: ω_p ≈ 0.3–1.7 ω_Planck; ~72-order gap (CN-TWIST-17) | **agree**; TWIST quantifies it |
| Interior would need to be ~370–550× denser (ξ₂ ≤ R/4–R/5) to afford a knot | yes | counted as the free input ξ′ (cost row 5) | **consistent** |
| Void geometry: 6 octahedral + 8 tetrahedral voids per sphere; each octahedral void opens into 8 tetrahedral, each tetrahedral into 4 octahedral; no tetrahedral–tetrahedral windows | exact geometry | void radii and positions used in Q2 (checked) | **agree** |

---

## 2. Where they differ, and which is right

| # | Point | 8 Nov | TWIST | Settled now |
|---|---|---|---|---|
| D1 | **Where the construction dies** | Session record §11: "question 2 is the likely kill" | Kill at **Q1** (the twist field is slaved; c_F ≤ 0 at all orders), and Q2 fails too | Both are right that Q2 fails. TWIST shows the earlier question is already fatal. |
| D2 | **Does EM rescue the knot's stability?** | Session record §11 says EM is needed "for the knot's stability"; §12 says "adding the flow fixes the shrinking … only for a charged system" | Post-blind §9: once the supercurrent is relaxed, there is no stable knot at any coupling | **TWIST is right.** It also agrees with Speight (2010) and Jäykkä & Speight (2011): in the charged two-component model, restoring the supercurrent coupling makes the knots shrink and disappear. The §12 caveat is too generous: **neither the neutral nor the charged two-condensate model holds a knot.** The 15 Sep JHF follow-on note should carry the stronger caveat. |
| D3 | **Unwinding barrier** | ~23 ε_c ℓ_P³ (bulk plus gradient on scale R), "far below" the knot's 191–287 | "Unwinding costs at most u_c·V, 1/369 of the knot" (CN-TWIST-15/16) | **Both numbers are wrong as barriers.** Radial minimisation of the corpus functional: letting the density respond lowers the knot from 193 to **51** ε_c ℓ_P³. Shrinking the knot inside the sphere then lowers it *monotonically*: 51 → 39 → 28 → 18 → 8.4 → 3.8 → 2.1 for L = R → 0.05R (values at L ≤ 0.1R are grid-limited). **There is no barrier at all on the shrink path.** The knot collapses and unwinds at a point. So the conclusion (no protected knot) is *stronger* than either said, and TWIST's "369× cheaper" wording is wrong (erratum E1). |
| D4 | **Is the condensate destroyed inside the knot?** | "the density dips and the knot unwinds" | "W̃ > 1 over 100% of the ball, so the condensate is destroyed (s = 0)" (CN-TWIST-15) | **The desk's wording is better.** TWIST's s = 0 came from a local criterion that ignores density-gradient cost, which is large on the sphere scale. The actual response is strong depletion, to ρ ≈ 0.17–0.37 n₀ inside, not zero (erratum E2). |
| D5 | **"Alternating knots ease the light-speed worry"** | Desk C and the session record: alternating up/down has no net direction, so no preferred-direction problem | not addressed | **Only half right.** Alternating removes the net direction (⟨m_z⟩ = 0) but keeps the axis: the nematic order is Q_zz = 1, the maximum. A two-way speed-of-light anisotropy along an axis (a cos 2θ signal) is exactly what rotating-cavity Michelson–Morley experiments look for, at Δc/c ~ 10⁻¹⁷–10⁻¹⁸. That observational constraint still applies. |
| D6 | **Desk C's ring model** | Each knot is a thin vortex ring of radius 0.6106 R (Biot–Savart, unbounded fluid) | — | The ring radius is 0.305 a = **0.13 ξ**. Gross–Pitaevskii vortex rings exist only down to radii of order ξ; smaller solutions lose their zeros and become vortex-free rarefaction pulses (Jones & Roberts 1982). So desk C's flow pattern describes knots that this medium cannot form. It is conditional on knots existing, and TWIST shows they don't. |
| D7 | **"The version that works is the spheromak"** | yes, given EM and a current-carrying shell | The field configuration is confirmed (virial). In this medium it needs ~11 counted inputs, and even with EM the knot is unstable (D2). | Agree on the shape. TWIST shows it is not reachable from this medium at any price that leaves the knot inside one sphere. |

---

## 3. The axis-alignment idea: what TWIST §9 covered, and what it didn't

**Covered in §9 (internal axis):**
- An alignment potential adds nothing to c_F and cannot stop collapse.
- Pinning n is the grip term.
- Each knot's twist field integrates to zero over its sphere (|∫f dV| / ∫|f| dV ~ 10⁻¹⁵).

**Not covered in §9, checked now (spatial axis, the earlier chat's meaning):**

1. **A knot carries impulse, like a smoke ring.** For the pinned one-twist knot, ∫f dV = 0, but the impulse P = ½∫x×f dV = **0.93ẑ** (|P|/(R∫|f|dV) = 0.17). So the outside flow is dipolar, which is consistent with desk C's dipolar void flows. It has two consequences:
   - **A free knot translates.** Holding one at a lattice site needs a pinning force from the shell. That is a further input, not in the corpus and not in TWIST's cost table.
   - **An all-aligned array carries a net momentum density n·P along c,** a built-in "aether wind". The alternating pattern cancels it.

   So §9's "aligned knots give no macroscopic twist field" holds for f, but it is incomplete for the flow.
2. **Alternating still has an axis** (D5): the observational constraint at 10⁻¹⁷–10⁻¹⁸ applies.
3. **"Octahedral voids open, tetrahedral calm"** (desk C, alternating pattern: octahedral flow 0.514 against tetrahedral 0.0014) rests on the ring model of D6. It is a statement about knots the medium cannot hold. It may still be a useful picture of what a *bought* knot lattice would do, but it is not a result of the model.

**Net effect on the gate:** nothing changes in Q1–Q4 or the verdict. The spatial-axis idea adds at least **two more inputs** (a pinning force per sphere, and the choice of alignment pattern) and **one observational constraint** (axis anisotropy at 10⁻¹⁷–10⁻¹⁸).

---

## 4. Plain-language summary for Michel

This morning's quick checks and the blind gate agree on almost every number. The knot energy matches to within 1%. The wall-pressure rule (a third of the average, a half at the equator) is confirmed exactly. Both found that the shell can't grip the twist, and both found the Planck-mesh problem with touching shells.

They differ in three places, and in each the comparison makes the picture sharper, not kinder:
- **Adding EM doesn't save the knot.** This morning's record said EM would fix the shrinking in the charged case. It doesn't: once the electric current in the medium is allowed to respond, the knot still shrinks away. Published work on exactly this model found the same.
- **There is no barrier at all.** Both today's quick check and the gate quoted a cost for the knot to unwind. Recomputing it properly shows the knot can just shrink, with its energy falling all the way down, and untie at a point. Nothing holds it back.
- **"Alternating up and down" still picks out a direction in space.** It removes a net direction but keeps a preferred axis, and experiments rule that out for light to 1 part in 10¹⁷–10¹⁸.

One new finding: each knot carries momentum, like a smoke ring, so it would drift unless the shell held it. A lattice of knots all pointing the same way would have a built-in wind running through it.

---

## 5. Errata

**To `gate_TWIST_RESULT.md`** (left unedited as run; read with these corrections):
- **E1 (CN-TWIST-15/16; Q3 §5).** Replace "unwinding … costs at most u_c·V, 1/369 of the knot's energy" and "the cost is ≤ u_c·V" with: *the knot has no barrier against shrinking. With the density free, its energy falls monotonically from 51 ε_c ℓ_P³ (L = R) towards zero, and it unwinds at a point. 369× is the knot's energy over the sphere's bulk condensation energy.* JH's "infinite energy" claim remains false.
- **E2 (CN-TWIST-15).** Replace "the condensate is destroyed (s = 0) in 100% of the ball" with: *the density is strongly depleted (ρ ≈ 0.17–0.37 n₀ throughout the sphere); the local W̃ > 1 criterion overstates this because it ignores gradient cost.*
- **E3 (CN-TWIST-28; §9).** Add: *a pinned knot has nonzero impulse (P = 0.93ẑ in the units of the script), so aligned knots carry net momentum along the axis. "No macroscopic twist field" refers to f only.*
- **E4 (§11 summary).** "about 370 times what it would cost to destroy the superfluid there, so the superfluid gives way" should read: *about 370 times the superfluid's condensation energy in that sphere. The density gives way and the knot simply shrinks and unties.*

**To the 8 Nov desk-check and session record:**
- §12's BFN caveat: the charged case fails as well (D2).
- Desk A's ~23 ε_c ℓ_P³ is not the operative barrier; its Derrick line is (D3).
- Desk C: the rings are below the GP vortex-ring minimum (D6). "Alternating eases the light-speed worry" holds only for a net direction (D5).
- Session record §11: the kill is at Q1 (with Q2 also failing), not Q2 alone (D1).

---

## 6. Updated status of the 8 Nov items

| Item | Before (session record §13) | Now |
|---|---|---|
| Knot energy ratio 366–548× | CONJECTURE (desk-check) | **Reproduced independently (369× / 553×)**; still CONJECTURE (same day) |
| Wall pressure ū/3, ū/2 at the equator | exact (textbook) | confirmed numerically to 10⁻¹⁰ |
| Void geometry and connectivity | exact geometry | unchanged |
| Octahedral open / tetrahedral calm (alternating) | CONJECTURE (simple model) | **conditional only**: rests on rings smaller than the medium allows (D6) |
| EM from a two-component interior | OPEN, gate to be written | **closed negative: SC-TWIST-1** (CONJECTURE, same-session) |
| EM as the knot stabiliser | implied in §11–12 | **negative** (post-blind §9 and Jäykkä–Speight) |
| Alignment (spatial axis) | alternating proposed | adds a pinning force and a pattern choice as inputs; a residual axis is constrained at 10⁻¹⁷–10⁻¹⁸ |
| Neutrinos in tetrahedral voids; quarks' home | picture / OPEN | unchanged: not tested |

**References added:** J. M. Speight, J. Geom. Phys. 60, 599 (2010); J. Jäykkä & J. M. Speight, Phys. Rev. D 84, 125035 (2011); C. A. Jones & P. H. Roberts, J. Phys. A 15, 2599 (1982); S. Herrmann et al., Phys. Rev. D 80, 105011 (2009); M. Nagel et al., Nat. Commun. 6, 8174 (2015).

| File | SHA-256 |
|---|---|
| `scripts/twist_addendum_checks.py` | `db999a7aa1c5b1f3f42defeadc538c740bcbe9f63425872d509134228a1dd8e1` |
| `output/twist_addendum_output.txt` | `159272a5e00e59c10a1fbf452f1d7827d7dd9bdda622347bfde0c77e4a947a5f` |
