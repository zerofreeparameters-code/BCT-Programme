# Desk-check VOID-Q1: can BCT's void network be a quantum liquid?

**Date:** 8 November 2026, 15:36–16:20 (Melbourne), Claude Opus 5.5, in the same chat as Gate TWIST.
**Status:** desk-check, **not a gate**. Same-session, so capped at **CONJECTURE**. Re-run it cold before moving any tier.
**Script:** `desk_VOID_Q1.py` → `desk_VOID_Q1_output.txt`. Deterministic, no fitted inputs. Run with `python3 -I desk_VOID_Q1.py 48:3000 64:3000 64:10000`.

## The question (Michel, 15:36)
"This only works when the network fluid is a quantum liquid … worth investigating … run question 1."

The route under test is the standard way of getting light out of a network (Hermele, Fisher & Balents, PRB 69, 064404 (2004), and related work). It needs three things:
- a fluid on a 3-D **bipartite** network, obeying a local rule at every node;
- in a **non-condensed** (quantum-liquid, Mott-like) state: the repulsion U between particles sharing a site beats the hopping t between sites;
- then an emergent U(1) gauge field appears, with a gapless photon and charges sitting on the nodes.

**Q1:** does BCT give the void network (a) the right shape and (b) the right regime?

## A. Shape: yes
- **Nodes:** octahedral voids (radius 0.20711 a, 6 neighbouring spheres) and tetrahedral voids (0.11237 a, 4 spheres). Per sphere: 1 octahedral, 2 tetrahedral.
- **Links:** the triangular windows between voids, inscribed radius 0.07735 a (0.1547 R).
  - Each octahedral void has 8 windows, all into tetrahedral voids.
  - Each tetrahedral void has 4 windows, all into octahedral voids.
  - There are no oct–oct or tet–tet windows, so the network is **bipartite**.
- **Smallest loops:** oct–tet–oct–tet 4-cycles. Every one of them rings a **sphere–sphere contact point**: one loop per contact, so 6 per sphere. All 120 loops found near the origin passed this check.
- **Reading, if the Coulomb picture applied:**
  - "electric" field on the 8 windows per sphere;
  - Gauss's law at the 3 voids per sphere;
  - "magnetic" flux through the 6 contact-loops per sphere;
  - charges are rule-violations sitting **on voids**, which matches Michel's "particles live in the voids".

## B. Regime: yes, if the spheres keep the network fluid out
**Calculation.** I took the lowest energy states of the fluid confined to the pore space. The spheres are treated as walls, using BCT's own geometry and its ξ = 2.31754 a (units ħ²/2m = 1, lengths in a). Method: spectral Hamiltonian on the cubic FCC cell, subspace iteration, then LOBPCG refinement to relative accuracy ~10⁻⁷. I used three settings (48³ and 64³ grids, wall heights 3000 and 10000) to check sensitivity.

**What it shows.**
- The lowest four states sit **one in each octahedral void**. The next states are about **120 units higher**: the tetrahedral voids act as **barriers**, not sites.
- So the low-energy network is a lattice of **octahedral sites**: an FCC lattice with 12 neighbours each.
- The three states at the X points are degenerate to 3×10⁻¹³, as FCC tight-binding requires, which is a symmetry check on the calculation.

**Numbers** (splitting = 16 t):

| Grid, wall | Lowest levels (oct band) | Splitting | Hopping t |
|---|---|---|---|
| 48³, 3000 | 130.5724; 130.5747 ×3 | 0.00237 | 1.5×10⁻⁴ |
| 64³, 3000 | 127.2300; 127.2320 ×3 | 0.00203 | 1.3×10⁻⁴ |
| 64³, 10000 | 137.1616; 137.1621 ×3 | 0.00046 | 2.9×10⁻⁵ |

- Stiffer walls give smaller hopping, and a true hard wall would give smaller still.
- Interaction scale: g n₀ = ħ²/(2m ξ²) = 0.186, so **g n₀ / t ≈ 1,200 to 6,500**.
- Size of one octahedral-site state: V_w ≈ 0.031 a³, close to the void's own volume (0.037 a³).

**Liquid or condensed?**
- The on-site repulsion is U = g/V_w = g n₀ / n̄, where n̄ is the number of particles per octahedral void. **The corpus does not fix n̄.**
- Mean-field Mott criterion on 12 neighbours: U/(12t) > (2n̄+1) + 2√(n̄(n̄+1)), which is 5.83 at n̄ = 1.
- **At n̄ = 1 the margin is about 18–90 times.** The network stays non-condensed for up to about **4–11 particles per octahedral void**.

**A new length scale is not needed.** BCT's own healing length, combined with the void geometry, already lands in the liquid regime once the spheres are sealed. I expected the opposite: that Q1 would need an extra short length. The sealed spheres plus the narrow windows suppress the hopping by about four orders of magnitude.

**A side result:** octahedral voids end up as the active sites and tetrahedral voids as quiet barriers. That is Michel's "octahedral open, tetrahedral calm" picture, arrived at by a different mechanism from this morning's flow model.

## Score (desk): **BOUGHT, 2 inputs**, and better than expected
1. **The spheres are impermeable to the network fluid.** This is structural, and it matches Michel's "contained spheres". *Correction (17:08):* the earlier statement that "the superfluid passes through the shells" was Michel's speculation, not a derived result, so there is no conflict with the record. It is still an input, though. The corpus shell term (α₀/R = 0.0148/a) lets 99.99996% of the void-state flux through, so it is effectively transparent. Sealing to 0.1% transmission needs a shell about 50,000 times stronger, or a different kind of wall.
2. **Filling per octahedral void, n̄ ≲ 4–11.** A free number, since n₀ is not fixed by the corpus.

A note on what this changes: in this picture the vacuum in the voids is **not a superfluid**. It is a Mott-like quantum liquid. That is a real change to the "superfluid lattice" premise for the network, though the sealed sphere interiors can stay superfluid.

## Caveats
- The hopping is the octahedral–octahedral tunnelling through the tetrahedral barriers, and it is exponentially sensitive to window geometry and wall softness. The three settings bracket it at 3×10⁻⁵ to 1.5×10⁻⁴. The conclusion holds over the whole bracket.
- The Mott boundary used is mean-field. It is good to roughly a factor of 2, well inside the margin found.
- **A Mott liquid is necessary, not sufficient.** A plain Mott insulator has no photon.

## What Q2 must face (next)
1. **A local rule with the right structure.** The low-energy sites form an FCC lattice, which is *not* bipartite. The gauge structure would have to come from a constraint carried by the tetrahedral voids (each touches 4 octahedral sites) or by the full oct–tet network. Q2 must show that the constraint exists, and that a Coulomb phase rather than some ordered state wins.
2. **Speed of light.** An emergent photon moves at roughly (ring-exchange energy) × a / ħ. Ring exchange comes in at higher order in t, which is small here (t/g n₀ ~ 10⁻³–10⁻⁴), so the emergent light would be very slow unless the overall energy scale is enormous. Light must also be the *fastest* signal: no other excitation, such as sound in the sealed sphere interiors, may outrun it.
3. **Isotropy.** Cubic symmetry makes the long-wavelength photon isotropic, with corrections of order (a/λ)². At Planck spacing that is far below the 10⁻¹⁷–10⁻¹⁸ limits. That one looks safe.
4. **Charges on voids.** Their charge, mass and Coulomb law come out of the same theory. Matching them to the electron is a later question, under the no-fit rule.
