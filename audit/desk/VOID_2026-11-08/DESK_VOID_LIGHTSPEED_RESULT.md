# Desk-check VOID-LIGHTSPEED: can interactions pull the speeds of light and charges together?

**Date:** 8 November 2026, evening (Melbourne). Claude Opus 5.5, same chat as Gate TWIST and VOID-Q1/Q2.
**Status:** desk-check, **not a gate**. Same-session work is capped at **CONJECTURE**; re-run it cold before moving any tier.
**Script:** `desk_VOID_lightspeed.py`, output in `desk_VOID_lightspeed_output.txt`. Runtime about 1 s.

## The question
VOID-Q2 found that if a Coulomb phase is granted in the void-network liquid, charges outrun the emergent photon by **R₀ = v_charge / c_photon = 2.8×10⁴** (at the edge of the liquid) up to **1.5×10¹²**.

In the real world, electrons and photons share one limiting speed. Accelerator data give −5.8×10⁻¹² ≤ κ̃_tr − (4/3)c_e⁰⁰ ≤ 1.2×10⁻¹¹ (Hohensee et al. 2009). Astrophysics gives |η| ≲ 10⁻¹⁴ (Altschul, as quoted by Anber & Donoghue).

The known escape is renormalisation-group running. Chadha & Nielsen (Nucl. Phys. B 217, 125, 1983) showed that equal speeds are the low-energy end-point of gauge interactions. Anber & Donoghue (PRD 83, 105027, 2011) worked out the β-functions for the speeds. **Does that escape work here?**

## A. In the void Coulomb phase there is no running window
For the speeds to run, there must be energies where the charges are dynamical (above their gap) **and** the photon exists (below its band top).

- The photon band top is ≈ π J_ring, with J_ring ~ t^L / U^(L−1).
- The charges cost the Mott gap Δ ~ U.
- So Δ / (π J_ring) = (U/t)^L / π.

| U/t | L | Δ / (π J) | window |
|---|---|---|---|
| 70 (edge) | 3 | 1.1×10⁵ | none |
| 70 | 4 | 7.6×10⁶ | none |
| 310 | 3 | 9.5×10⁶ | none |
| 1241 | 4 | 7.6×10¹¹ | none |
| 6421 | 4 | 5.4×10¹⁴ | none |

**The photon's whole band lies below the charge gap.** Charges never run as light particles while the photon exists, so nothing pulls the speeds together. The photon's stiffness J_ring is itself the effect of virtual charges hopping round loops, and that effect is already counted.

A window opens only near the Mott edge, where the gap closes as Δ/U ~ (distance)^(1/2) in 3+1 D. The distance must then be ≤ (π J/U)² e^(−2ℓ): 8×10⁻¹¹ × e^(−2ℓ) at the most favourable row. There the charges are about to condense, and condensed charges **Higgs the photon**, which gives it a mass. That is the TWIST outcome again.

## B. Granting a window anyway: one loop drags the photon up, slowly
Suppose the charges were light, as electrons are, and grant the largest window physics offers: Planck energy down to the electron mass, **51.5 e-folds**.

**Photon side.** This is derived here and agrees with Anber & Donoghue eq. 33. A charge loop induces a Maxwell term that is Lorentz-invariant in the **charge's** metric. Per e-fold, for a Dirac charge, the photon coefficients grow by d a_E = 1/(6π² v) and d a_B = v/(6π²).

**Charge side.** Anber & Donoghue eq. 33.

| R₀ | α₀ | R after 51.5 e-folds | photon sped up | α at the end |
|---|---|---|---|---|
| 2.8×10⁴ | 1/137 | **587** | 47× | 1.6×10⁻⁴ |
| 2.8×10⁴ | 0.08 (spin-ice-like) | **174** | 154× | 5.2×10⁻⁴ |
| 2.8×10⁴ | 1 | **46** | 525× | 1.9×10⁻³ |
| 1.5×10¹² | 1/137 to 1 | 4.3×10⁶ to 3.7×10⁵ | — | ≤ 2.5×10⁻⁷ |

- **Why so slow.** Fast charges speed the photon up, but the same charges screen the coupling: α·c stays fixed, because the electric coefficient barely moves. The pull therefore weakens as it works, and R falls only as 1/√ℓ.
- **Time needed.** Reaching even R = 2 from R₀ = 2.8×10⁴ takes 3×10⁴ to 4.5×10⁶ e-folds, against 51.5 available.
- **A second inconsistency.** The surviving coupling ends **4× to 50× below 1/137**. Over-screening by fast charges leaves light coupled too weakly to matter.
- **Is one loop trustworthy here?** Fast charges are weakly coupled to each other, with strength ∝ α/R, so one loop is a fair guide. The α₀ = 1 rows are illustrations only.
- **Robustness.** Switching the charge-side running off changes R by 1% to 11%. The result rests on the photon side, which was derived independently.

## C. The last stretch is logarithmic, whatever the start
Near equal speeds, δ = v/c − 1 obeys dδ/dℓ = −(2α/π)δ while dα/dℓ = −(2/3π)α². So **δ_IR / δ_UV = (α_IR / α_UV)³**, checked numerically. The low-energy α is measured at 1/137.

- **Best case at weak coupling** (α_UV ≈ 1): a factor (1/137)³ = **3.9×10⁻⁷**. That needs 641 e-folds, 12× more than exist. It falls short of 10⁻¹¹ (lab) by **4.5 orders** and of 10⁻¹⁴ (astro) by **7.4 orders**.
- **The real 51.5 e-folds:** factor **0.78**, short by 11 to 14 orders.
- To end at 10⁻¹⁴ at weak coupling, the mismatch at the emergence scale would already have to be ≤ 2.6×10⁻⁸.

This matches the literature. Anber & Donoghue conclude that simple systems converge only logarithmically, so the emergence scale would have to be exponentially far away. Collins et al. (PRL 93, 191301, 2004) add that a Planck-scale preferred frame feeds Lorentz violation into low energies at about the percent level unless the bare parameters are fine-tuned.

## Score (desk): **FAIL**. The Chadha–Nielsen escape does not rescue VOID-Q2.
1. In the void Coulomb phase there is **no window** at all: virtual charges make the photon, and nothing is left to run. Opening a window means tuning to the Mott edge, where the photon is Higgsed.
2. Even with light charges granted, weak-coupling running closes a 10⁴ mismatch **too slowly** (1/√ℓ, then logarithmically) by 11 to 14 orders of magnitude. It also leaves α too small.

**The only doors in the literature, not supplied by the void model:**
- strong coupling, or very many interacting species, giving power-law running (Anber & Donoghue sec. 8);
- a symmetry that forbids the dimension-4 Lorentz-violating terms outright.

Either would be a new input, and neither has a visible mechanism in BCT.

## The pattern, now four times
Light has failed by the same two exits each time: it **gets a mass** (knot twist; superconducting medium; Mott-edge Higgsing here), or it **gets outrun** (void liquid, Q2). The running escape does not close the outrun gap, and the only place it could start is the mass exit.

**Survives as a structural fact:** in any lattice Coulomb phase, light's stiffness comes from virtual charges. So charges that are heavy enough to leave light alone are also too heavy to make light keep pace.

## Sources
- [Chadha & Nielsen, Lorentz invariance as a low energy phenomenon, Nucl. Phys. B 217, 125 (1983)](https://doi.org/10.1016/0550-3213(83)90081-0)
- [Anber & Donoghue, The emergence of a universal limiting speed, PRD 83, 105027 (2011)](https://arxiv.org/abs/1102.0789)
- [Collins, Perez, Sudarsky, Urrutia, Vucetich, PRL 93, 191301 (2004)](https://arxiv.org/abs/gr-qc/0403053)
- [Hohensee, Lehnert, Phillips, Walsworth, PRL 102, 170402 (2009)](https://arxiv.org/abs/0904.2031)
- [Pace, Morampudi, Moessner, Laumann, Emergent fine structure constant of quantum spin ice is large, PRL 127, 117205 (2021)](https://arxiv.org/abs/2009.04499)
