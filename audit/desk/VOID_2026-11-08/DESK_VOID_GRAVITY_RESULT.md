# Desk-check VOID-GRAVITY: is gravity the Bjerknes pull between spheres breathing in step?

**Date:** 8 November 2026, evening (Melbourne). Claude Opus 5.5, same chat as Gate TWIST and the VOID checks.
**Status:** desk-check, **not a gate**. Same-session work is capped at **CONJECTURE**; re-run it cold before moving any tier.
**Script:** `desk_VOID_gravity.py`, output in `desk_VOID_gravity_output.txt`. Runtime about 1 s.

## The idea
Bjerknes (1875; *Fields of Force*, 1906) found that in an incompressible ideal fluid, spheres pulsating **in phase attract** and spheres in opposite phase repel. The force goes as the product of the pulsation strengths over the distance squared. That would make the breathing spheres a candidate for gravity.

**BCT premises used** (corpus, Appendices Vol. 1 §1):
- the medium is **compressible**, with sound speed **c_s = c**, because light is the medium's sound;
- its density is the **Planck density**, 5.16×10⁹⁶ kg/m³;
- it obeys continuity, so medium is neither created nor destroyed.

## A. The law: right at short range, wrong at long range
I derived the time-averaged force between in-phase breathers in a compressible fluid and checked it by direct quadrature, which agrees to every printed digit:

**⟨F⟩ = −(ρ q₀² / 8π r²) · [cos kr + kr sin kr],  with k = ω / c_s.**

- **Near (kr ≪ 1):** attractive inverse-square, which is Bjerknes's result.
- **Beyond kr = 2.798** (0.445 wavelengths): the attraction **turns into repulsion**. Further out the force oscillates in sign and falls as 1/r.
- **The force alternates.** The body's undisplaced volume feels a zero-mean force of **2/ε times the mean pull**, where ε = ΔV/V ≤ 1. So "gravity" would shake at least twice as hard as it pulls, at the breathing frequency.

## B. Strength
Matching Newton's law gives q₀ = m √(8πG/ρ). In Planck units a Planck mass must breathe **√(8π) ≈ 5 Planck volumes per Planck time**.

## C. Equivalence principle: forces the frequency above the Planck frequency
- A body of volume V moving through the fluid carries added mass ρV/2, so its inertial mass is at least ρV/2.
- It can breathe at most q₀ ≤ ωV.
- Requiring gravitational mass to equal inertial mass for every body then gives **ω ≥ √(2πGρ)**.

For BCT's density that is ω ≥ 4.65×10⁴³ s⁻¹ = **2.5 / t_P**. With c_s = c the attraction then **reverses beyond 1.1 Planck lengths**. For the pull to reach even the Sun's galactic orbit, the medium would need ρ ≤ 3×10⁻¹⁴ kg/m³, about 10¹¹⁰ times thinner than BCT's.

## D. The frequency window is empty, even ignoring density

| Bound | ω (s⁻¹) | Why |
|---|---|---|
| lower | 1.2×10⁻³ | the at-least-2× alternating force must average out over a low-Earth orbit |
| lower | 4.7×10⁴³ | equivalence principle, Planck-density medium (C) |
| upper | 9.4×10⁻⁶ | inverse-square to 1% out to Neptune |
| upper | 3.4×10⁻¹² | still attractive at the Sun's galactic orbit |
| upper | 5.2×10⁻¹² | Sun and Earth stay in phase for 4.5 Gyr, if breathing redshifts like every other clock (Δω/ω = 2.1×10⁻⁶) |

- **Most lenient pairing:** empty by a factor of **123**.
- **With BCT's own density:** empty by **49 orders of magnitude**.

The lenient gap would close only if the medium's sound ran at ≥ 123 c, but BCT identifies that sound with light.

## E. The VOID-Q1 liquid cannot carry the flow
Q1's network liquid is a Mott state, so mass currents are blocked and a push spreads only by virtual hops. Its range is a / ln(U/zt) = **0.16 to 0.57 void spacings**. Michel's "the void network does the work" therefore cannot be done by Bjerknes flow through that liquid. It would need the gapless superfluid, which brings back the limits in D.

## F. Breathing bodies radiate
Monopole radiation gives P = G m² ω² / c_s, whatever the density. In BCT, sound is light.
- At the most lenient frequency, the Sun would emit **1.2×10³⁶ W, 3×10⁹ times its luminosity**, and lose its rest energy in about **4,800 years**.
- The Earth would lose its rest energy in 1.6 Gyr.

## G. No light bending
The 1/r part of the force is ⟨q₁q₂⟩. It vanishes for anything that does not breathe at ω, and light does not breathe at ω. The time-averaged pressure around a breather is second order, ~1/r⁴. So light sees **no 1/r potential**: no deflection and no Shapiro delay.

Even if light were somehow made to breathe in step, a scalar force gives at most the Newtonian half. Cassini measured γ = 1 + (2.1 ± 2.3)×10⁻⁵, which is full GR bending to about 10⁻⁵.

## Score (desk): **FAIL**
The sign and the inverse square at short range are right; that is Bjerknes's genuine result. Everything else fails:
- the equivalence principle drives the frequency above the Planck frequency, where the pull reverses within a Planck length;
- even without that, steady gravity and an inverse square over the solar system exclude each other when c_s = c;
- the void liquid cannot carry the flow;
- breathing bodies would radiate their mass away as light;
- light would not bend.

**Doors, all closed by BCT's own premises:**
- sound faster than light (BCT: c_s = c);
- a medium far thinner than Planck density (BCT: Planck);
- bodies that create and destroy medium (BCT: continuity);
- a breathing clock that gravity does not slow (this would break the universality of the gravitational redshift).

None of these fixes light bending.

## Noticed in passing (corpus, not this check)
Appendices Vol. 1 §AI.4 writes G_eff = c⁴/(16π ρ_BCT) and, with ρ = ρ_Planck, G_eff = ħG²/(16πc). Neither has the units of G: both are m⁷ kg⁻¹ s⁻⁴. ħG²/c equals G·(ℓ_P c)², so the stated "G_eff ~ G up to a numerical coefficient" is off by a factor carrying units, not a number. Worth fixing before anyone cites it.

## Sources
- [Bjerknes force: in-phase pulsators attract, opposite phase repel](https://en.wikipedia.org/wiki/Bjerknes_force)
- [Bertotti, Iess & Tortora, Nature 425, 374 (2003): γ = 1 + (2.1 ± 2.3)×10⁻⁵](https://doi.org/10.1038/nature01997)
- [Ida (2003), sign reversal of the Bjerknes force between bubbles (resonance mechanism; context only)](https://arxiv.org/abs/physics/0109005)
