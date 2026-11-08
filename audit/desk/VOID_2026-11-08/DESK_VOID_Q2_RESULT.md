# Desk-check VOID-Q2: does the void-network liquid carry light?

**Date:** 8 November 2026, 16:37 (Melbourne), Claude Opus 5.5, in the same chat as Gate TWIST and VOID-Q1.
**Status:** desk-check, **not a gate**. Same-session, so capped at **CONJECTURE**. Re-run it cold before moving any tier.
**Script:** `desk_VOID_Q2.py` → `desk_VOID_Q2_output.txt`. It runs in under a second.

## Starting point (from VOID-Q1)
With the spheres sealed, the network fluid's low-energy states sit in the **octahedral voids**. They form an FCC lattice in which each site has 12 neighbours.
- Hopping between sites: t = 2.9×10⁻⁵ to 1.5×10⁻⁴ (units ħ²/2m = 1, a = 1).
- On-site repulsion: U = g n₀ / n̄, with g n₀ = 0.186, where n̄ is the number of particles per octahedral void.
- The fluid is a non-condensed liquid if U/t ≳ 70 (at n̄ = 1).

## Requirements for light
1. massless;
2. two transverse polarisations;
3. the same in every direction;
4. **the fastest signal**: photons and electrons are observed to share one limiting speed to very high precision.

## A. Gauge structure: not supplied by the model
Emergent light of this kind needs a Gauss law, with an "electric" field living on the links of a **bipartite** lattice. Pyrochlore spin ice gets one because each site sits in exactly **2** tetrahedra, so a site works as a link between them.

| Check | Result |
|---|---|
| Is the octahedral-site lattice bipartite? | **No.** It has 24 triangles per site (FCC). |
| Tetrahedral voids touching each octahedral site | **8**, not 2 |
| Do the bipartite oct–tet links (the windows) carry low-energy freedom? | **No.** The tetrahedral voids are barriers (Q1). |

So the model Q1 found has no Gauss law. A Coulomb phase would have to be **added**: extra interactions that impose a rule on every tetrahedral void and make it resonate. Those are new inputs.

## B. Speeds: fails even if a Coulomb phase is granted
In lattice Coulomb phases, light and matter move at very different orders in the hopping:
- **Light** comes only from ring exchange around the smallest loop: J_ring ~ t^L / U^(L−1), with L = 3 for triangles and L = 4 for the smallest even loops. Its speed is about J_ring · a / ħ.
- **Charges** (violations of the rule, sitting on voids) move by single hops, at up to 5.66 t a / ħ on this lattice.
- So v_charge / c_photon ≈ 5.66 (U/t)^(L−1).

| t | n̄ | U/t | L = 3 | L = 4 |
|---|---|---|---|---|
| 2.9×10⁻⁵ | 1 | 6421 | 2.3×10⁸ | 1.5×10¹² |
| 2.9×10⁻⁵ | 4 | 1605 | 1.5×10⁷ | 2.3×10¹⁰ |
| 1.5×10⁻⁴ | 1 | 1241 | 8.7×10⁶ | 1.1×10¹⁰ |
| 1.5×10⁻⁴ | 4 | 310 | 5.4×10⁵ | 1.7×10⁸ |
| at the edge of the liquid | — | 70 | 2.8×10⁴ | 1.9×10⁶ |

**Light would be the fastest signal only if U/t ≲ 1.** Q1's liquid needs U/t ≳ 70. **The two requirements exclude each other**: charged particles in the voids would outrun light by 10⁴ to 10¹². This is a known feature of lattice Coulomb phases, such as quantum spin ice, where the charges are faster than the emergent photon.

## C. What would pass, if a Coulomb phase were granted
- Two transverse polarisations: yes.
- Massless: yes.
- Isotropy: cubic symmetry makes the long-wavelength photon isotropic. Corrections are about (a/λ)² ~ 10⁻⁵⁷ for visible light at Planck spacing, far inside the 10⁻¹⁷ to 10⁻¹⁸ limits.

## Score (desk): **FAIL**
- The gauge structure is not supplied by the medium; it would be a bought input.
- Even with it, **light cannot be the fastest signal**. The liquid that question 1 needs makes matter faster than light by at least four orders of magnitude.

An escape would need a construction in which charges move only at the same order as the photon. Nothing in the corpus suggests one, so it would be a further input with no visible mechanism.

## Where this leaves the void-network route
| Question | Desk result |
|---|---|
| Q1: void-scale structure, quantum-liquid regime | **BOUGHT, 2 inputs** (sealed spheres; filling per void). Better than expected: BCT's own ξ suffices. |
| Q2: light | **FAIL**: no Gauss law in the model, and a speed-ordering contradiction with Q1 |
| Q3 gravity, Q4 particles | not run (light failed first) |

**Survives as a geometric fact:** the octahedral voids are the active sites and the tetrahedral voids the barriers, once the spheres are sealed.
