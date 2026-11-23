# Desk-check BUBBLE_BELLS2: the bell as a resonance, the lattice of bells, and the condensate mass

**Date:** 23 November 2026, evening (Melbourne). Claude Fable 5.1, chat thread inside the BCT Project.
**Status:** desk-check, **not a gate**. Same-session, one instance, not blind; **memory and past-chats were ON** for this thread (the 10 Nov Bubble Bells record and Gate BUBBLE_BELLS' result were in context). Everything below is capped at **CONJECTURE**; re-run cold before any tier moves.
**Asked by:** Michel — "should we look into the bubble bells more… I have an intuition … a sense there's something to be found there in favour." Three computations were agreed: (1) treat the bell as a resonance, not a bound state; (2) a lattice of bells, not one bell; (3) the condensate-mass sweep queued in `audit/NEXT.md` item 6.
**Inputs:** corpus only — a = ℓ_P, R = a/2, α₀ = 0.0074081, ξ = a/√(8πα₀) = 2.31754 a (CN-C1-04, used as given), App J's δ-shell condition and exterior, μ = gn₀ = ħ²/(2mξ²), FCC geometry. No comparison with α, 137 or any measured constant anywhere (no-fit clause of the BUBBLE_BELLS card carried over).
**Scripts:** `bb2_resonance.py` → `bb2_resonance.txt`; `bb2_lattice.py` → `bb2_lattice_N48_64.txt`, `bb2_lattice_N96.txt`, `bb2_lattice_N128.txt`, `bb2_lattice_N160.txt` (Γ, X only), with `bb2_lattice_extrap.py` → `bb2_lattice_extrap.txt`; `bb2_mass_sweep.py` → `bb2_mass_sweep.txt`. Units in the scripts: ħ²/2m = 1, a = 1 (so a single-particle energy is κ² and μ = 1/ξ² = 0.18618).

## Verdict in one paragraph

The *bubbles* do not ring; the *voids* do. In the only Hamiltonian the corpus supplies, App J's interior mode is not a resonance of the sphere at all — the sphere is transparent to a quasiparticle at the bell energy, the inherited κ-ladder is an artefact of matching to a static tail at the wrong energy, and a wall strong enough to make a bell would move the ground rung to κ₀ = 2π/a and seal it. Gate BUBBLE_BELLS' N5–N7 and N10 should be retired as a physical spectrum. What survives, and is new, is the lattice: the FCC void network read as a superleak is a **phononic crystal with a complete band gap** — an acoustic band slowed by the tortuosity that flattens toward the zone edge and tops out at a geometry-fixed maximum (λ_X ≈ 9.6 /a², ω_max ≈ 3.1 c_s/a), a complete gap (ratio ≈ 1.6), then chamber (void-resonator) bands from ≈ 15 /a². All of it zero-parameter. That is the honest content of "bells" in the model as written, and it is the thing to card. Separately, the sweep finds the corpus carrying two incompatible values of the GP boson mass (m = m_P in Letter 20; 0.305 m_P forced by AZ6's c_s = c with App E.3's ξ), not in the ledger.

## 1. The bell is not a resonance (`bb2_resonance.py`)

**A. Where the inherited ladder comes from.** With interior j_ℓ(κr), exterior k_ℓ(r/ξ) at the same energy and App J's δ-jump, the rungs κ_ℓa = 3.3905, 6.3050, 8.9920, 11.5289 reproduce. But R/ξ = 0.216 is small, and k_ℓ(x) ~ x^−(ℓ+1) there: the "exterior at the same energy" is the **static (Laplace) multipole tail**, and the matching collapses to κ j_{ℓ−1}(κR)/j_ℓ(κR) ≈ −1/ξ + α₀ = −0.424, i.e. κ_ℓR sits just above a zero of j_{ℓ−1} (cos for ℓ = 0):

| ℓ | κ_ℓa | κ_ℓR | zero of j_{ℓ−1} | κ_ℓR − zero | E_ℓ/μ | fraction of |ψ|² **inside** the sphere |
|---|---|---|---|---|---|---|
| 0 | 3.3905 | 1.6952 | π/2 = 1.5708 | 0.124 | 61.7 | **0.19** |
| 1 | 6.3050 | 3.1525 | 3.1416 | 0.011 | 213.5 | 0.40 |
| 2 | 8.9920 | 4.4960 | 4.4934 | 0.0026 | 434.3 | 0.61 |
| 3 | 11.5289 | 5.7644 | 5.7635 | 0.0010 | 713.9 | 0.72 |

App J's own higher s-wave roots (9.5139, 15.762) reproduce as the n = 2, 3 solutions of the same condition. So the ladder is "the interior matched to an exterior at energy ≈ 0 while the interior is at 62–714 μ". **81 % of the ℓ = 0 "interior" mode lies outside the sphere.**

**B. What that exterior contains.** Within R + ξ = 2.82 a of a sphere centre there are **134 other sphere centres**; within R + 2ξ, 790. The packing fraction is 0.7405, so the region the mode is normalised over is three-quarters other bubbles' interiors — the regions the construction itself declares depleted. The single-cavity exterior is not a self-consistent object (this is CN-TWIST-12, ξ = 4.6 R, from the bell side).

**C. The consistent problem.** A quasiparticle at the bell energy with a free (depleted) interior, a Bogoliubov exterior in the void condensate (ε² = k²(k² + 2μ)), and App J's α₀ shell:
- reflectivity at the surface, normal incidence: Bogoliubov step |r|² = 1.6 × 10⁻⁵, α₀ shell |r|² = 1.2 × 10⁻⁶, combined 1.8 × 10⁻⁵ — **the sphere is transparent**;
- phase shifts δ_ℓ(E), ℓ = 0…3, μ ≤ E ≤ 20 E₀: |δ_ℓ| ≤ 0.017 rad everywhere, no rise through π/2 anywhere; the largest Wigner delay is at threshold E → μ (0.011), not at any rung (a width Γ = E₀/10 would give 1.74);
- S-matrix poles, systematic search (160 starts per ℓ, 1 ≤ Re κ ≤ 20, −12 ≤ Im κ ≤ −0.05): every pole has |Im κ|R > 3 and Γ/E between 2 and 50. **No rung survives as a resonance.** (The desk-check's "Q ~ 1/g_J ≈ 2700" was a dimensional guess; the scattering problem gives Q ≲ 0.02.)

**D. What shell would make a bell.** Same δ-shell form, strength V: Q = 10 needs V = 22 = **3.0 × 10³ α₀**; Q = 100 needs 72 = 9.7 × 10³ α₀; Q = 2700 needs 370 = 5.0 × 10⁴ α₀. In every case the ground rung sits at κR → π, i.e. **κ₀ → 2π/a = 6.28**, E/μ → 212, not App J's 3.39 / 61.7 μ. A confining shell gives the Dirichlet ladder, not the inherited one.

**E. Hard wall (Horn A: rigid, sealed sphere).** κ_ℓa = 6.283, 8.987, 11.527, 13.976; E_ℓ/E₀ = 1, 2.046, 3.366, 4.948; Γ = 0 and coupling 0 exactly. A sealed empty box has no mode to ring; it holds one only if a quantum is **put** in it (an input). The empty sealed sphere is precisely the excluded volume of the Q1 tortuosity picture.

**Consequence for the Gate BUBBLE_BELLS number list (recommendation, not a tier move):** N5, N6 (the κ_ℓ ladder and its ratios), N7 (bell note vs host) and N10 (sub-resonant correction from the bells) describe a spectrum that does not exist in any Hamiltonian the corpus supplies → **retire** (the N5 falsifier "a different exterior decay law" has fired, from inside). N1–N4 (porosity, tortuosity, c_eff, isotropy), N8 (rigidity) and N9 (implied mass) are void-superleak statements and stand, N2 still awaiting BB-ALPHA. The 10 Nov audit notes in App J, App JH FINAL and Letter 73 that call the interior "a cavity mode κ₀ = 3.3905" inherit this note; the AZ6/AZ7 notes (tortuosity) do not.

## 2. The lattice: the voids ring (`bb2_lattice.py`)

**Model (BUBBLE_BELLS §1 as given):** rigid depleted spheres R = a/2 on FCC, touching; uniform-density superfluid in the void network; phase (sound) mode with the Neumann (no-flow) condition on the sphere surfaces. Bloch eigenvalues λ_n(K) of −∇² on the void network give the dispersion: hydrodynamic ω² = c_s²λ; with the Bogoliubov correction ε(λ) = √(λ(λ + 2μ)) (exact for uniform density with Neumann walls).

**Numerics:** finite differences on the conventional cubic cell (edge a√2, 4 spheres), N³ cells; the FCC translations are exact grid shifts for even N, so the eigenproblem is reduced to **one primitive cell** with Bloch phases on every bond leaving it — no band unfolding. Shift-invert Lanczos, 8 lowest bands. Hermiticity verified to machine precision at every K. First-order convergence (contact-point staircase), as for `bells_tortuosity.py`. Eigenvalues in 1/a².

| N | throat / cells | K → 0 slope \|K\|²/λ₀ (ζ = 0.1) | λ_ac(X) | λ_ac(L) | λ_ac(W) | 2nd band at X | 2nd band at Γ (first chamber mode) | 3rd at Γ | triplet at Γ |
|---|---|---|---|---|---|---|---|---|---|
| 32 | 1.8 | 2.356 | 5.614 | 3.720 | 5.614 | 12.03 | 22.66 | 23.01 | 37.11 |
| 48 | 2.6 | 2.058 | 6.953 | 4.393 | 6.953 | 13.21 | 22.95 | 31.64 | 39.34 |
| 64 | 3.5 | 1.943 | 7.476 | 4.676 | 7.476 | 13.89 | 23.59 | 34.99 | 41.21 |
| 96 | 5.3 | 1.813 | 8.352 | 5.103 | 8.352 | 14.18 | 23.79 | 38.71 | 42.85 |
| 128 | 7.0 | 1.770 | 8.636 | 5.245 | 8.636 | 14.36 | 23.84 | 39.61 | 43.86 |
| 160 (Γ, X only) | 8.8 | — | 8.820 | — | — | 14.50 | 24.03 | 40.31 | 44.40 |
| **extrapolated** (linear on the two finest grids vs quadratic on the three finest; `bb2_lattice_extrap.py`) | — | *not extrapolated (BB-ALPHA)* | **9.55–9.65** | 5.4–5.7 | = X | **15.1–15.3** | 24.8–26.0 (irregular; take ≈ 24–25) | — | 46.0–46.5 |
| free space | — | 1 | 19.739 | 14.804 | 24.674 | — | — | — | — |

*The K → 0 slope is the FD tortuosity on the same grid family as the gate's `bells_tortuosity.py` (1.929 at N = 64 there vs 1.943 here, Bloch vs applied field). It is printed for consistency and **deliberately not re-extrapolated**: Gate BB-ALPHA is pre-registered to anchor that number by a non-FD method, and nothing here is independent of FD.*

**What the spectrum looks like** (finest grids plus the 1/N extrapolations; the acoustic top rises at first order — its last two increments, +0.28 and +0.18 per step, are consistent with a + b/N, the earlier ones irregular as in the gate's tortuosity table — so take its extrapolation as ±5–10 %; the gap bottom is converged to ≈ 3 %, the chamber mode at Γ and the flat triplet to ≈ 5 %):

1. **Acoustic band.** λ₀(K) ≈ |K|²/α_∞ at small K, then flattening: |K|²/λ₀ rises from 1.77 at ζ = 0.1 to 2.24 at X (N = 160: 19.74/8.82). The band **tops out at X and W** (degenerate there) at λ_X = 8.82 on the finest grid, **≈ 9.6 ± 0.5 extrapolated**, against a free-space 19.74: the void network compresses the zone-edge sound frequency by a factor √(19.74/λ_X) ≈ 1.43 (more than the √α_∞ ≈ 1.3 of the long-wavelength tortuosity — the band flattens further toward the edge). So the sound in the void condensate has a **derived maximum frequency** ω_max = c_s √λ_X ≈ 3.1 c_s/a (free zone-edge sound would be 4.44 c_s/a), fixed by geometry alone. Along Γ–L the band reaches only 5.4–5.7 at L.
2. **A complete gap.** Nothing between the acoustic top (8.82 → 9.55–9.65) and the bottom of the second band, which is at X (14.50 → 15.1–15.3; at L 15.9, at W 16.7, at Γ 24.0). Gap ratio bottom/top = 1.56–1.61 on the extrapolations and 1.64 on the finest grid: the gap is complete at every resolution (ratio 2.14 at N = 32, 1.66 at 128, 1.64 at 160) and is settling at about 1.6, not closing. In Bogoliubov energy: acoustic top ε ≈ 53 μ, gap bottom ε ≈ 83 μ.
3. **Chamber bands.** Second band 15.2 (X) → ≈ 24–25 (Γ): the lowest void-chamber mode, dispersing because chambers talk through throats; then a band near 43–47 with a **three-fold degenerate, nearly flat** level at Γ (44.4 at N = 160, → ≈ 46; 42.4 at X, 42.9 at L: bandwidth ≈ 4 % of its value) — a localised p-like chamber mode, flat because it barely couples through the throats. These are the honest "bells": the octahedral and tetrahedral **voids** are the resonators, ringing at ε ≈ 83–135 μ (lowest band) and ≈ 250 μ (flat triplet), Planck-scale, in a medium with zero inputs beyond the geometry.
4. **Where the old bells sit.** App J's κ₀² = 11.5 /a² (61.7 μ) falls inside the gap; the hard-wall bell (2π)² = 39.5 falls just below the flat triplet. Neither is a mode of this system (§1), so neither placement means anything; recorded only so nobody later reads a coincidence into it.

**Reading.** As a superleak the void network is a locally-resonant acoustic metamaterial, exactly the Liu-type picture the 10 Nov desk-check invoked — but with the resonators where the construction actually allows them: in the voids, not in the sealed spheres. The "bubble bells" become **void bells**. Michel's long-standing expectation that the interesting objects live in the octahedral and tetrahedral voids (8 Nov) is at least the right address; this does not make any of it a particle.

**Caveats.** (i) The uniform-density Neumann treatment is the BUBBLE_BELLS §1 assumption; the void channels (throat 0.077 a, chamber 0.21 a) are 10–30× smaller than ξ = 2.32 a, the regime in which a GP condensate's density would be strongly suppressed by confinement if the walls were Dirichlet. CN-TWIST-12 again; the gate inherited it and so does this. (ii) First-order convergence with an irregular early history (the staircase at the contact points): the acoustic top moved +0.88, +0.28, +0.18 over the last three grid steps, the last two consistent with a + b/N; take its extrapolation as ±5–10 %, the gap bottom's as ±3 %, the chamber mode's and triplet's as ±5 %. N = 160 was run for Γ and X only (the memory-light solver; 15 min). (iii) Nothing here is observable: the whole spectrum is at the Planck scale, and the sub-resonant correction from chamber resonators at observed frequencies is (ω/ω_chamber)² ≲ 10⁻²⁸ as before. The gap is a statement about the vacuum's **own** spectrum, not a prediction. (iv) No comparison with any constant was made; none is implied.

## 3. The condensate mass across the corpus (`bb2_mass_sweep.py`)

Three conventions coexist:

| where | statement | implied m | implied App J bell energy |
|---|---|---|---|
| Letter 20 (GR to all orders) ll. 66, 230, 317; Monograph App AI | m = m_P, ρ₀ = ρ_Planck, c_s = c | **m_P** | ħ²κ₀²/2m = 5.75 m_P c² (the gate's `bells_resonator.py`) |
| AZ6 l. 353 (g = mc²/n₀ ⇒ c_s = c) with AZ6 l. 168–169 / AZ7 l. 113 (ξ = ħ/√(2mgn₀) = 2.32 ℓ_P, App E.3) | both together | **0.305 m_P** (= ℓ_P/(√2 ξ)) — Gate BUBBLE_BELLS N9; 0.238 m_P with c_eff = c | 18.84 m_P c² |
| App J table l. 208 | E_n = ħcκ_n (linear dispersion, no m) | — | 3.39 m_P c² |

m = m_P with g = mc²/n₀ gives ξ = ℓ_P/√2 = 0.707 ℓ_P, a factor **3.28** below App E.3's 2.32 ℓ_P. Any corpus number that uses both m = m_P and ξ = 2.32 ℓ_P (or c_s = c) carries that factor somewhere. Gate MP's notices CN-MP-01…09 cover other m_P inconsistencies, not this one; checked `audit/gates/MP/`. **Candidate notice for the queued INVENTORY-style sweep** (`audit/NEXT.md` item 6), provisional until re-derived cold. Letter 20's α_GB = ħ²ρ₀/32m = ħ²n₀/32 happens not to depend on m; its printed m_P/ρ_Planck still conflicts with App E.3.

## 4. What this does and does not establish

Established (CONJECTURE, zero inputs beyond the corpus): the sphere-interior κ-ladder is not a spectrum of any consistent model (§1); the void network has an acoustic band with a geometry-fixed top, a complete gap and chamber bands (§2); the corpus carries two incompatible GP boson masses (§3).
Not established: that the void condensate is the medium of light (c = c_eff stays asserted); any observable; anything about α₀, the void radii, QED-DERIV, PROMOTE, JHF, TWIST or KL. Not touched: BB-ALPHA's number (the K → 0 slope is printed, not re-extrapolated).
In favour, in the structural sense Michel asked about: the "bells" reading survives as a derived property of the void network — a maximum sound frequency and a gap that nobody put in — and it fails as a property of the spheres. The construction got sharper, not weaker; what it lost was the part that was never consistent.

## 5. Does it earn a card?

Yes, one small gate with a check that can fail, after BB-ALPHA (one gate per thread; BB-ALPHA first because N2 feeds the acoustic slope):

**Gate VOID_BELLS (proposed).** (Q1) Reproduce the acoustic-band top λ_ac(X) and the gap bottom min_K λ₁(K) by a method sharing no discretisation with this FD solve (plane-wave/Fourier–Galerkin with the sphere indicator, or a boundary-element Neumann solve), ≥ 2 resolutions and a stated extrapolation; PASS if λ_ac(X) agrees with the FD extrapolation within 10 % **and** the gap is complete (min λ₁ > λ_ac,max by more than 20 %); FAIL if the gap closes. (Q2) The flat triplet: PASS if its Γ value agrees within 3 % and its bandwidth across Γ–X–L is < 10 % of its value (localised chamber mode), else PARTIAL. (Q3) Check against the literature on the Neumann spectrum / acoustic bands of fluid in close-packed sphere arrays (phononic crystals of touching rigid spheres; "porous FCC" fourth-sound band structure), recording any value found. (Q4) Write the number list: λ_X, gap edges, triplet, all in 1/a² and in μ. Kill: an independent λ_ac(X) outside 7.5–11 /a², or no gap. No-fit clause as before. Not a gate on whether void sound is light.

Also to carry: the κ-ladder retirement (§1) as a one-paragraph audit note in App J / App JH FINAL / Letter 73 beneath the 10 Nov notes, and the mass notice (§3) into the INVENTORY sweep card.

## 6. 🦜 Baby-speak

We asked whether the bubbles really ring. We let a Planck-scale particle hit a bubble's wall using only the wall the model actually gives it: it goes straight through — about two parts in a hundred thousand bounce back. A bell you can't bounce off isn't a bell. The old ladder of notes came from gluing the inside of the bubble to an outside that was sitting still, and four-fifths of that "inside" note was actually outside, overlapping a hundred other bubbles. To get even a dull bell you'd need a wall three thousand times stronger than the model has, and then the note would be a different one anyway. So: the bubbles are silent boxes.

But the *gaps between* the bubbles sing. Sound threading through the twisty void network slows down (that was the 10 Nov result), and now we see the whole tune: it climbs to a top pitch set purely by the lattice shape, then there's a band of pitches the network simply cannot carry at all, then the little chambers between the spheres ring on their own. Nothing was chosen; the FCC geometry does all of it. That is the real "bells" result — the voids are the bells. It's a statement about the vacuum's own Planck-scale spectrum, not something we can measure.

Side find: the papers disagree with each other about how heavy the superfluid's particle is — one place says a Planck mass, another set of equations forces a third of that. Worth a line in the inventory sweep.
