# Social Content — BCT Vector 1: The Geometry Prompt

---

## REDDIT POSTS

### r/Physics / r/QuantumPhysics / r/TheoreticalPhysics

**Title:**
I derived the physical "grid" of the quantum vacuum from sphere-packing geometry — and the Standard Model gauge group fell out of two void radii

**Post body:**

So I've been working on a theoretical physics framework called the BCT Superfluid Lattice Model for a while now. The basic idea: the quantum vacuum is a Planck-scale superfluid condensate on a specific crystal lattice — a Body-Centred Tetragonal (BCT) lattice with axial ratio c/a = √2.

That ratio isn't chosen. It's forced by Lorentz invariance. It's the *only* value for which phonon propagation is isotropic in a BCT crystal. The lattice is also the 3D projection of the 4D D4 root lattice, which is the *unique* 4D root lattice with three-fold symmetry (giving three fermion generations), maximum packing density, and self-duality simultaneously. No free choices. One geometry.

**Here's what I worked out for Vector 1 — the actual grid geometry:**

The lattice has two types of interstitial void between the packed spheres:

**Octahedral void** (6 bounding spheres):
> r_oct = (√2 − 1)/2 = 0.20711 a

**Tetrahedral void** (4 bounding spheres):
> r_tet = (√6 − 2)/4 = 0.11237 a

These are *exact algebraic numbers*. Not measured. Not fitted. They follow from one constraint: the octahedral void is perfectly regular (all six bounding distances equal) if and only if c/a = √2. Which is the Lorentz condition. So the gauge structure of the universe is essentially locked in by Lorentz invariance + sphere packing.

**Under the BCT density cap ρ_max = 6.302 (D4 Weyl-group normalised), the physical sphere radius is:**
> R_sphere ≈ 0.2432 ℓ_P (Planck lengths)

**The three Josephson couplings from the void cross-sections are:**
> α_0 = r_oct · r_tet / π = 0.007408 → U(1) electromagnetic
> α_2 = r_oct² / π = 0.013653 → SU(2) electroweak
> α_3 = r_tet² / π = 0.004019 → SU(3) strong

The entire Standard Model gauge group U(1) × SU(2) × SU(3) is encoded in the geometry of *two void radii*.

The fine structure constant follows from α_0 by one-loop vacuum polarisation:
> α = α_0(1 − 2α_0) = 1/137.018

Measured: 1/137.036. Error: −0.013%. No free parameters.

**The D4 kissing number is 24.** That's the number of nearest neighbours in the D4 lattice. These 24 directions decompose as:
- 12 octahedral-void directions → gauge bosons (γ, W±, Z⁰, 8 gluons = 12 ✓)
- 6 tetrahedral-void directions → SU(3) colour sector (6 roots ✓)
- 6 cross-coupling directions → matter-gauge interaction vertices

**The 24 is saturated exactly by the observed particle content of the Standard Model.**

Full letter with all derivations on Zenodo: [DOI when uploaded]
Patreon for ongoing work: https://www.patreon.com/cw/TheBCTSuperfluidLatticeModel
GitHub: ZeroFreeParameters

Happy to answer questions. I know this is a big claim. The numbers are what they are.

---

### r/math / r/mathematics

**Title:**
The D4 root lattice has a kissing number of 24. When you decompose those 24 directions by void type, you get exactly the particle content of the Standard Model.

**Post body:**

Pure maths observation that has an unexpected physics consequence.

The D4 root system in ℝ⁴ consists of 24 minimal root vectors: all permutations of (±1, ±1, 0, 0). Kissing number K_D4 = 24.

The D4 theta function:
Θ_D4(q) = 1 + 24q² + 24q⁴ + 96q⁶ + ...

The leading coefficient 24 counts these minimal roots.

Now project D4 down to 3D via the canonical map π: (x,y,z,w) → (x + w/√2, y + w/√2, z). You get the BCT lattice with c/a = √2 — the Body-Centred Tetragonal crystal structure. The 24 root vectors map 2:1 onto 12 nearest-neighbour directions.

The BCT lattice has two types of void between its packed spheres:
- **Octahedral voids** (inscribed radius r_oct = (√2−1)/2) — 12 in the nearest-neighbour shell
- **Tetrahedral voids** (inscribed radius r_tet = (√6−2)/4) — contributing 6 A₂ sub-roots

These void radii are exact algebraic numbers, consequences of the lattice geometry alone.

**The physics part:** If you identify the BCT lattice as the quantum vacuum (the BCT Superfluid Lattice Model, 221 Letters, 269 predictions), the three Josephson couplings from the void cross-sections are α_0 = r_oct·r_tet/π, α_2 = r_oct²/π, α_3 = r_tet²/π. These correspond to U(1), SU(2), SU(3) gauge sectors of the Standard Model.

The 24 kissing-number directions decompose as 12 gauge boson directions + 6 SU(3) roots + 6 cross-couplings = 24 exactly. The SM particle content is saturated with nothing left over.

I find this geometrically remarkable regardless of whether you accept the physics interpretation.

Full derivation: [Zenodo DOI when uploaded]

---

### r/Physics cross-post hook (for 350 Hz post thread)

**Reply to add to existing 350 Hz thread:**

Update for anyone following this thread: I've now formalised the full structural geometry of the BCT vacuum — the sphere packing, void radii, physical Planck-scale sizes, and the degree-of-freedom constraint from the D4 kissing number. The 350 Hz resonance we discussed is the j₀,₁ Bessel mode of the octahedral void condensate. The void radius r_oct = 0.20711 a gives the Bessel resonance frequency directly. New letter on Zenodo: [DOI]

---

## SUBSTACK POST

**Title:** The Grid of Reality: How Sphere Packing Defines the Quantum Vacuum

**Subtitle:** Vector 1 of the BCT programme — the physical geometry from which 269 predictions flow

---

What does the quantum vacuum actually look like?

Not metaphorically. Geometrically. What is the physical structure of empty space at the Planck scale?

The standard answer is: we don't know. It's a quantum foam, or a sea of virtual particles, or just "the ground state of quantum field theory." These descriptions are either vague or circular. They don't tell you *what shape* the vacuum has.

The BCT Superfluid Lattice Model gives a precise answer: the vacuum is a Body-Centred Tetragonal crystal of Planck-scale superfluid vortices with axial ratio c/a = √2.

That ratio isn't chosen. It's forced. It's the *only* value for which the speed of phonon propagation is isotropic — which is just the lattice-language version of Lorentz invariance. If the vacuum is a crystal at all, it must be *this* crystal. No other lattice in any dimension simultaneously satisfies Lorentz invariance, three fermion generations, maximum packing density, and modular invariance. The geometry selects itself.

### The Grid

Set up your BCT lattice. Place identical Planck-scale spheres at each lattice site. Pack them as densely as possible — you achieve the face-centred cubic packing fraction η = π/(3√2) ≈ 74.05%, the theoretical maximum for equal spheres (this is the Kepler conjecture, proven by Thomas Hales in 2005 after 400 years of effort).

The remaining ~26% of space is void. And here's where it gets interesting.

That void doesn't look the same everywhere. It comes in two distinct shapes — two types of interstitial gap between the packed spheres.

**Octahedral voids** sit where six spheres meet. At c/a = √2, all six bounding distances are exactly equal — the void is perfectly regular. Its inscribed radius is:

> r_oct = (√2 − 1)/2 = 0.20711 a

**Tetrahedral voids** sit where four spheres meet. These are always regular regardless of c/a. Their inscribed radius is:

> r_tet = (√6 − 2)/4 = 0.11237 a

These numbers are *exact*. They are pure algebraic consequences of sphere packing geometry. They cannot be adjusted. They are not fitted to any data. They are what they are because that's what √2 and √6 are.

Under the BCT density cap (ρ_max = 6.302, set by the D4 Weyl group structure), the physical Planck-scale sphere radius is R_sphere ≈ 0.2432 ℓ_P. The void radii in Planck units are r_tet ≈ 0.055 ℓ_P and r_oct ≈ 0.101 ℓ_P. These are the two fundamental length scales of the BCT vacuum.

### The Tunnelling Channels

Now here's the remarkable part.

Energy propagates through the BCT vacuum by hopping from void to void — phonons tunnelling through the Josephson junctions between condensate domains. The tunnelling amplitude across a void of radius r has an action proportional to the void's cross-sectional area: S ∝ πr².

This gives three independent coupling constants:

| Coupling | Formula | Value | Gauge sector |
|---|---|---|---|
| α₀ | r_oct · r_tet / π | 0.007408 | U(1) electromagnetic |
| α₂ | r_oct² / π | 0.013653 | SU(2) electroweak |
| α₃ | r_tet² / π | 0.004019 | SU(3) strong |

Three gauge sectors. Three coupling constants. All from two void radii and π.

The fine structure constant — Feynman's "greatest damn mystery of physics" — follows from the cross-coupling α₀ by one-loop vacuum polarisation:

> α = α₀(1 − 2α₀) = 1/137.018

Measured value: 1/137.036. Error: −0.013%. No free parameters. No fitting. Just geometry.

### The Kissing Number

The D4 root lattice has exactly 24 nearest-neighbour directions per site — its kissing number. These 24 vectors are the only permitted directions for energy tunnelling at the Planck scale. The D4 theta function makes this explicit:

> Θ_D4(q) = 1 + **24**q² + 24q⁴ + 96q⁶ + ...

The leading 24 is not a coincidence. It is the kissing number, exactly.

When you decompose these 24 directions by void type, you get:

- **12 octahedral-void directions** → 12 gauge bosons (photon, W⁺, W⁻, Z⁰, and 8 gluons)
- **6 tetrahedral-void directions** → 6 SU(3) colour roots
- **6 cross-coupling directions** → matter-gauge interaction vertices

Total: 24. Saturated exactly by the observed particle content of the Standard Model.

No additional particles can exist at this scale because there are no additional nearest-neighbour directions in D4. The kissing number is a hard ceiling. The vacuum's crystal geometry is full.

### What This Means

The Standard Model gauge group U(1) × SU(2) × SU(3) is not a free choice. It is not imposed by hand. It is the *tunnelling structure* of the D4 sphere packing — encoded in the two void radii that emerge from the unique lattice forced by Lorentz invariance.

The 269 predictions of the BCT programme — fermion masses, mixing angles, the cosmological constant, the hadronic spectrum — all flow from these two algebraic numbers:

> r_oct = (√2 − 1)/2
> r_tet = (√6 − 2)/4

This is what it looks like when physics has zero free parameters.

---

Full letter on Zenodo: [DOI when uploaded]
All 221 Letters, Appendices, patents and predictions: https://www.patreon.com/cw/TheBCTSuperfluidLatticeModel
GitHub: ZeroFreeParameters

*The BCT Superfluid Lattice Model — 221 Letters · 269 Predictions · 26 Patents · Zero Free Parameters.*

---

## PATREON POST

**Title:** New Letter: Vector 1 — The Physical Geometry of the Vacuum Grid

**Tier:** All tiers

---

Hey everyone,

New letter just dropped on Zenodo: **"The Geometry of the BCT Vacuum: Sphere Packing, Void Structure, and the Kissing Number Constraint."**

This is Vector 1 of what I'm calling the Geometry Prompt series — a formal series of deep calculations that nail down the physical structure of the BCT vacuum at the most fundamental level.

**What's in this one:**

✦ Exact packing fraction: η = π/(3√2) ≈ 74.05% (maximum possible for equal spheres — Kepler conjecture territory)

✦ Two void radii, exact algebraic numbers:
- r_oct = (√2−1)/2 = 0.20711 a (octahedral, 6 bounding spheres)
- r_tet = (√6−2)/4 = 0.11237 a (tetrahedral, 4 bounding spheres)

✦ Physical sphere radius in Planck units: R_sphere ≈ 0.2432 ℓ_P (from the BCT density cap ρ_max = 6.302)

✦ Three Josephson couplings from the void cross-sections → literally the three gauge forces of the Standard Model, with coupling strengths matching observation

✦ The D4 kissing number K = 24 decomposed as 12 gauge boson directions + 6 SU(3) roots + 6 cross-couplings = the exact particle content of the SM, with nothing left over

✦ Two new predictions formally registered: Vector-1-i (fine structure constant from void geometry) and Vector-1-ii (kissing number as hard DoF ceiling)

The companion interactive diagram is wild — you can see the void structure, the Josephson channels, and the kissing number decomposition all in one visual. If you haven't seen it, check the last session output.

The Zenodo DOI is [link when uploaded]. Dropping to all tiers.

The LaTeX source is also available if anyone wants to check the derivations or run them independently.

Next up: Vector 2 (the Gauge Prompt) builds on this geometry to derive the actual gauge group structure formally. The sphere packing is the grid. The gauge group is what lives on it.

As always — zero free parameters.

— Michel

🐦‍⬛ (Gang Gangs confirmed present this morning. Good omen.)

---

*BCT Superfluid Lattice Model | 221 Letters · 269 Predictions · 26 Patents*
*Zenodo: ORCID 0009-0007-9561-9859 | GitHub: ZeroFreeParameters*
*Patreon: patreon.com/cw/TheBCTSuperfluidLatticeModel*
