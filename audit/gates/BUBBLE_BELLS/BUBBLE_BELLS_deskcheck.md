# Bubble Bells — desk-check (not a gate)

**Status:** non-gate, same-session, CONJECTURE-capped. 10 Nov 2026. Scripts: `bells_tortuosity.py`, `bells_resonator.py` (+ earlier `derive_interior_length.py`, `explore_interior_modes.py`). All inputs are corpus inputs (a = ℓ_P, R = a/2, ξ = a/√(8πα₀), App J's shell condition, App JH's surface term, App J's Josephson number). No new number is introduced anywhere.

## 0. The claim being checked

> The BCT spheres are depleted cavities ("bubbles") in a single-component superfluid filling the FCC void network. Each cavity has a fixed mode ladder (κ₀ = 3.39, then 5.69, 7.92, 10.11 …). The vacuum we observe is the sub-resonant response of that array.

Three things had to be true for this to be more than a caption: (1) the sub-resonant array has a definite, isotropic effective sound speed; (2) the bells sit far above everything observable and contribute nothing else below resonance; (3) the picture is self-consistent about what holds the bubbles open. All three were computed.

## 1. The effective medium: a superfluid in a rigid FCC superleak

A superfluid filling a rigid porous matrix carries **fourth sound** at c₄² = c_s²/α_∞, where α_∞ is the tortuosity of the pore space — equal to the electrical tortuosity, α_∞ = φ·F with F the formation factor (Johnson, Koplik & Dashen, J. Fluid Mech. 176, 379 (1987); this is how tortuosity is *measured* in He-II-filled porous media). So the whole effective-medium problem reduces to the DC conductivity of the FCC void network with the spheres insulating — a Laplace problem on the periodic cell.

Solved by finite differences on the conventional cubic cell (4 spheres, edge a√2), harmonic-mean face conductances, unit applied field, conjugate gradient; current conservation verified to 10⁻¹¹ at every grid. Convergence is first order in grid spacing because the spheres touch (contact-point singularities):

| N | σ_eff/σ₀ | α_∞ = φ/σ_eff | c₄/c_s |
|---|---|---|---|
| 64 | 0.1346 | 1.929 | 0.720 |
| 96 | 0.1441 | 1.801 | 0.745 |
| 128 | 0.1471 | 1.764 | 0.753 |
| 192 | 0.1511 | 1.718 | 0.763 |
| 224 | 0.1525 | 1.702 | 0.767 |
| **extrapolated** | **0.158 ± 0.003** | **1.64 ± 0.03** | **0.78 ± 0.01** |

Checks: porosity φ = 1 − π/(3√2) = 0.25952 exactly; σ_eff sits below the Hashin–Shtrikman/Maxwell–Garnett upper bound (1−f)/(1+f/2) = 0.189, as it must at touching; σ_xx = σ_yy = σ_zz to all printed digits (cubic symmetry makes the tensor a scalar; off-diagonals vanish by the mirror planes).

**Result 1 (derived, zero parameters, CONJECTURE until an independent method reproduces it):** the long-wavelength sound speed of a superfluid confined to the FCC void network is
  **c_eff = c_s/√α_∞ ≈ 0.78 c_s**, isotropic at O(k²),
with α_∞ ≈ 1.64 a pure geometric number of the touching-sphere FCC lattice. An independent cross-check exists in the literature (periodic-array conductivity: Sangani & Acrivos, Proc. R. Soc. A 386, 263 (1983); Cheng & Torquato, Proc. R. Soc. A 453, 145 (1997) for FCC) — I did not have the FCC-insulating-at-close-packing value in hand, so I quote mine with its grid-extrapolation error and recommend a multipole/BEM cross-check before any tier move.

**What it touches in the corpus.** Only the identification c = c_s. The ledger already records that identification as asserted (Gate LINK: "the phonon identification, c_s = c"). If the spheres are depleted (M1 of the derivation attempt) the sound that *is* light lives in the voids and moves at 0.78 c_s, not c_s. That shifts nothing observable — c_s is stiffness-set and unmeasured — but any corpus formula that silently sets c = ħ/(√2 mξ) now carries a factor 1/√α_∞. Worth a one-line note in App J/App F when they are next edited.

## 2. The bells

- **Note.** ω₀ = ħκ₀²/2m = 18.84 c_s/a. The host Bogoliubov mode resonant with it has k ≈ 3.36/a with kξ = 7.8 — a particle, not a phonon. The zone-boundary phonon is at ω(π/a) = 16.5 c_s/a, so **the bell sits only 14 % above the top of the lattice's own band**: the bells are part of the Planck-scale band structure (a locally-resonant metamaterial with its resonance at the zone edge), not an isolated line far above it. Everything observed is ≥ 13 orders of magnitude lower: (ω/ω₀)² ≈ 10⁻²⁸ for a PeV photon.
- **Below resonance they do nothing else.** A Liu-type local resonator corrects the effective compressibility by ~f(ω/ω₀)² ≈ 10⁻²⁸. So the sub-resonant vacuum *is* Result 1 and nothing more.
- **What could ring one.** Coupling to the host is App J's Josephson number g_J = α₀·4πR·tanh²(r_oct/ξ) = 3.7 × 10⁻⁴ (rough Q ~ 2700). Only a Planck-scale host quasiparticle is resonant. The bells are silent in the low-energy world — a consistent statement, and a limiting one.

## 3. Self-consistency: the bubbles must be rigid

A soft bubble fails in both directions, using the corpus shell tension σ_sh = α₀ħ²n₀/(2mR) = α₀ (Planck units):
- an **empty** cavity with no internal pressure undergoes Rayleigh collapse in τ ~ √(ρR³/σ_sh) ≈ 4 t_P;
- **one quantum** in the κ₀ mode exerts a zero-point pressure (2/3)E₀/V ≈ 7.3 against a capillary pressure 2σ_sh/R ≈ 0.030 — a factor 250.

So the spheres are a rigid prior structure. That is **Horn A** (lattice imposed; Gates U″, WHY√2, LH7) arrived at from the bubble side — consistent with the ledger, and it means the bubble-bells reading adds no new tension to the model's foundations. It also closes the door on the shell as a dynamical object once more (BC, STIFF, TWIST).

## 4. What this does and does not establish

Established (CONJECTURE, zero new parameters): a definite, isotropic, geometry-fixed sub-resonant sound speed c_s/√1.64; a bell ladder at the zone edge; rigidity of the spheres required; nothing observable from the bells themselves. Not established: that the void condensate is the medium of light (the identification c = c_s remains asserted); the absolute scale of c_s; any effect reachable by experiment. Not touched: α₀, the void radii, the percolating network, QED-DERIV, PROMOTE.

Honest caveats: the tortuosity is a grid extrapolation (±2 %); the "bell" is App J's linear cavity mode and inherits BC's fitted shell coefficient (κ₀ shifts 0.12 % if the shell is switched off — robust); the Liu-type estimate is dimensional, adequate for a 10⁻²⁸ conclusion.

## 5. Does it earn a pre-registered card?

Yes, a small one, with a check it can fail: **Gate BELLS** — (Q1) reproduce α_∞(FCC, touching, insulating) by an independent method (multipole expansion or BEM) and against the literature; PASS if within 3 % of 1.64; (Q2) determine whether any corpus prediction depends on c = c_s rather than c = c_s/√α_∞ and recompute it; (Q3) state the bell ladder κ₀…κ₃ with the exterior matching done properly for ℓ ≥ 1 (not inherited from the s-wave), PASS if the ℓ = 1 cost stays within 10 % of 2.81 E₀. Kill condition: an independent α_∞ outside 1.5–1.8, or a corpus prediction that moves outside its quoted error under the 0.78 factor. Cost: zero inputs beyond the corpus. I can write the card for a fresh thread.

## 6. 🦜 Baby-speak

We asked: if the spheres are bubbles in a superfluid, what does the superfluid *do*? Answer: sound threads through the gaps between the bubbles, and because the gaps are twisty, it goes slower — about 78 % of its straight-line speed. That number comes purely from the shape of the FCC lattice; nothing was chosen. Every direction gives the same number, which is the isotropy you need. The bubbles' bells ring at the very top of the lattice's own pitch range and no ordinary thing can strike them, so below that they are just rigid obstacles. And they *must* be rigid — a soft bubble would pop in four Planck ticks, and a rung one would burst. That is the same "the lattice is given, not grown" conclusion the audits reached from the other side, so the picture is consistent with everything standing. What it costs you: nothing new predicted, and "the light-speed is the superfluid sound speed" picks up a 0.78 you didn't have before.
