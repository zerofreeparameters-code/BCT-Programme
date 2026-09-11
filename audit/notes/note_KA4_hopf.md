# NOTE — APPENDIX KA4's |H| ≤ n, AND THE "INFINITE ENERGY" CLAIM

**Issued:** 11 September 2026, census session 3.
**Standing:** not a gate. A follow-up on two census findings (INV-0020, INV-0021), requested
because both are load-bearing for BCT chemistry.
**Script:** `ka4_hopf_analysis.py`. mpmath, 30 dps. Planck units throughout (ħ = c = m = ℓ_P = 1,
ρ₀ = 1).

---

## 1 — VERDICTS

**Q1 — can |H| ≤ n be proved?** **No, and not by any route constructed here. Status OPEN, leaning
FALSE.** KA4's proof is an identity in disguise. The nearest genuine bound has the wrong character,
the wrong exponent, and requires a term the corpus does not contain. A sympathetic reading of the
mode index yields a bound of the form 2np, not n. A counterexample at n = 1 is sketched but **not
verified**, so the claim is not retired — it is unsupported.

**Q2 — does changing the Hopf charge cost infinite energy?** **No. False three separate ways, and
the strongest refutation is inside App JH itself.** In the free energy App JH actually writes, the
barrier is not infinite but **zero**.

---

## 2 — Q1: THE THEOREM

### 2.1 The proof is an identity

KA4's argument, restated:

> a Hopf excitation of charge H requires phase winding H·2πα₀;
> the n-th mode sustains winding up to n·2πα₀;
> therefore H ≤ n.

**α₀ and 2π appear identically on both sides and cancel.** The argument has the form
Hk ≤ nk ⟹ H ≤ n, true for *any* nonzero k. It holds equally for k = 1, k = 137, or k = π⁵/6. No
property of α₀, of the Josephson coupling, or of the Bessel spectrum enters anywhere.

Whatever supports |H| ≤ n, it is not this. **The result may still be true; it is not proved.**

### 2.2 The two halves of KA4 contradict each other in kind

The load-bearing premise — *"the mode can sustain phase winding up to 2πnα₀ without exceeding the
Josephson energy barrier"* — is unsourced, and its **form is energetic**: a barrier is exceeded.

KA4 §4 then insists the constraint is **topological**, and draws the entire force of the appendix
from that: *"Pauli exclusion admits no exceptions and noble gas inertness is absolute: they are
topological theorems."*

**A barrier argument cannot deliver a homotopy obstruction.** Energetic bounds are violable at
sufficient energy; topological ones are not. KA4 argues the first and claims the second.

### 2.3 The nearest genuine bound is the wrong shape

The real result in this area is the Vakulenko–Kapitanskii bound for the Faddeev–Skyrme model:

```
E ≥ c·|H|^(3/4)     ⟹     |H| ≤ (E/c)^(4/3)
```

Three differences, each fatal to KA4's claim as stated:

1. **Energetic, not topological.** It bounds H at fixed energy and says nothing about what is
   reachable by smooth deformation.
2. **Wrong exponent.** H grows as E^(4/3). Nothing here is linear in a mode index.
3. **Requires the quartic.** The Faddeev–Skyrme term is absent from the BCT corpus — established
   independently during Gate Ψ2 and not contradicted since.

### 2.4 Does the Bessel index constrain H at all?

KA4 indexes modes by `j_n(κ₀r/R)` — that is **angular momentum** n, not radial node count. But the
Hopf charge of a two-component field is fixed by the phase and angular structure of the map to S²,
not by its radial profile. Standard axially symmetric hopfions carry **H = m·p**, with m the
toroidal and p the poloidal winding.

A field with angular content ℓ ≤ n has |m| ≤ n, so the **relative** azimuthal winding between the
two components reaches |m₊ − m₋| = 2n. With poloidal winding p, that permits **H up to 2np**.

Even the most sympathetic reading gives a bound of the wrong form. |H| ≤ n is not recovered.

### 2.5 Candidate counterexample — SKETCH ONLY, NOT VERIFIED

At n = 1, take ψ₊ ~ Y₁,₊₁ ~ sinθ·e^{+iφ} and ψ₋ ~ Y₁,₋₁ ~ sinθ·e^{−iφ}. The relative azimuthal
winding is 2; with poloidal winding 1 this is **H = 2 inside an ℓ = 1 mode**.

If that configuration is smooth and normalisable, |H| ≤ n is false at n = 1. **This has not been
checked.** It is recorded so that the next session starts from a concrete target rather than a
general doubt. Verifying or killing it is a contained piece of work.

---

## 3 — Q2: THE "INFINITE ENERGY" CLAIM

App JH §3.4 and KA4 §4 both assert that changing the Hopf charge requires passing through a nodal
configuration, *"which costs infinite energy in the superfluid."*

### 3.1 The nodal object invoked cannot exist in the field App JH defines

Zeros of a single complex field in 3D are generically **lines** — codimension 2, since Re and Im
must both vanish. Nodal *surfaces* are non-generic and unstable to perturbation.

For App JH's **two**-component field Ψ_int : B³ → ℂ², |Ψ|² = 0 requires **four** real conditions in
three dimensions — codimension 4, **generically empty**. And App JH §3.1 fixes |Ψ_int|² = ρ₀
exactly, so its field can never vanish anywhere, at any dimension.

**The mechanism §3.4 invokes cannot occur in the theory §3.1 defines.**

### 3.2 Real vortices cost finite energy — and cannot fit in a BCT sphere

For a singly quantised GP vortex, E/L = πρ₀(ħ²/m)·ln(b/ξ):

| region | ln(b/ξ) | E/L (m_P c² per ℓ_P) |
|---|---|---|
| b = R (one sphere) | −1.53366 | −4.81812 |
| b = 2R (unit cell) | −0.840508 | −2.64053 |
| b = 10R | +0.76893 | +2.41566 |

All finite. The negative entries are the formula reporting b < ξ — and that is itself a result
worth keeping:

> **ξ/R = 4.635.** The healing length is 4.6× the sphere radius, so a vortex core is ~4.6× wider
> than the whole sphere. **A BCT sphere fits inside a single core.** No nodal structure can be
> localised inside one, so the configuration §3.4 describes has nowhere to live.

Taking the core scale rather than the logarithm, E_core ~ πρ₀·2R = **3.14159 m_P c²**. Planck
scale. Finite.

### 3.3 The decisive refutation is App JH's own free energy

With |Ψ_int|² = ρ₀ fixed and the surface term constant (both established during Gate Ψ2), the only
configuration-dependent term in App JH eq. (13) is the σ-model gradient energy. For a texture of
linear size a:

```
E₂(a) ~ a  →  0   as a → 0
```

The H = 1 texture **shrinks to a point** and the charge is lost at the singular point, at energy
tending to **zero**. That is Derrick's theorem, and it is the exact opposite of §3.4's claim.

**So the barrier is not infinite. It is zero.** App JH §3.3 refutes App JH §3.4, one section apart.

### 3.4 Where a finite barrier would come from

Adding the Faddeev–Skyrme quartic E₄ ~ 1/a stabilises the soliton size at a* = √(κ_FS/c₂) and makes
hopfion transitions cost a **finite** barrier — which is what Faddeev–Skyrme simulations show.
Finite, never infinite. And κ_FS is a new coupling the corpus does not have.

---

## 4 — WHAT THIS COSTS THE PROGRAMME

**The infinite-energy claim is retired.** It carries no numeric prediction, but it is the stated
reason why several results are *absolute* rather than *typical*:

| claim | location | what it loses |
|---|---|---|
| N_H = 1 is "topologically protected" | App JH §3.4 | the protection argument; the charge may still be conserved for other reasons |
| Pauli exclusion "admits no exceptions" | KA4 §4, Letter 81 Thm 1 | the reason for absoluteness, not the exclusion itself |
| Noble gas inertness "is absolute" | KA4 §4, Letter 81 Thm 2 | same |
| shell capacity 2n² | KA4 §3, Letter 78 | rests on |H| ≤ n, which §2 leaves unproved |

**Nothing numeric moves.** These are structural claims about *why* results hold, not the results.
Pauli exclusion is not in doubt; BCT's derivation of it is.

---

## 5 — WHAT THIS NOTE DID NOT ESTABLISH

- **|H| ≤ n is not disproved.** §2.5 is a sketch. It needs the configuration written explicitly,
  checked for smoothness, and its Hopf invariant computed. Until then the claim is unsupported,
  not false.
- **Letter 81 and Letter 78 were not read.** The theorems said to rest on |H| ≤ n were assessed
  only through KA4's summary table. They may carry independent arguments.
- **App K's bipartite-lattice result was not re-derived**, and is not used here.
- **Whether Hopf charge is conserved in BCT for some other reason** is untouched. This note removes
  one argument; it does not show the conclusion is wrong.

---

*Note issued 11 September 2026. Q1: unproved, leaning false, counterexample sketched. Q2: false,
and refuted internally by App JH §3.3 against App JH §3.4.*
