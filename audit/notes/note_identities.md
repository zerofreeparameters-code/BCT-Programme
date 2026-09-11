# NOTE — ARE THE BCT EXACT IDENTITIES PHYSICS, OR ALGEBRA?

**Issued:** 11 September 2026, census session 3.
**Standing:** not a gate. Scored in the manner of Gate STAT. Part 1 is PROVEN (symbolic,
sympy); Part 2 is PROVEN as a statistic over the stated population, with the population choice
declared in §5.
**Scripts:** `identity_stat.py`, plus the sympy reduction inline.

---

## 0 — TWO CORRECTIONS I OWE FIRST

**(a) "Ψ₂ was the only candidate that claimed to cost nothing" — I repeated that unverified.**
It comes from the Gate Ψ2 prompt's own preamble, which sources it to E5. **The E5 file was never
available to me.** Ψ2 §11 recorded that honestly at the time; I then restated the claim without the
qualifier. It should read: *Ψ₂ was the only such candidate according to E5, which this thread has
never read.*

**(b) The ξ² closed form I called "apparently new" and "worth a Letter" is a rearrangement.**
ξ² = (1+r_tet)/r_oct follows from 8·r_tet = 1/(1+r_tet), which is the r_tet(1+r_tet) = 1/8 identity
solved for r_tet. It is not independent, and it is not new content. It is the same fact as
everything below.

---

## 1 — VERDICT

**The identity family is one algebraic fact, and that fact is free.**

Every "exact identity" in the BCT corpus that this note examined reduces to the difference of
squares, or is a rearrangement of something that does, or is true by construction. And the one
underlying identity holds for **100% of numbers written in the same form**, chosen or not.

**Surprise: 3.3 bits.** For scale, a coin flip is 1 bit, and Gate STAT scored π⁵/6 at zero. Three
bits is not evidence of anything.

---

## 2 — PART 1: FIVE IDENTITIES, ONE FACT

| # | identity | reduces to |
|---|---|---|
| ID-1 | r_oct(1+r_oct) = 1/4 | (√2−1)(√2+1) = 1, rescaled. **Difference of squares.** |
| ID-2 | r_tet(1+r_tet) = 1/8 | (√6−2)(√6+2) = 2, rescaled. **Same difference of squares.** |
| ID-3 | 1 − r_oct − r_oct² = 3/4 | = 1 − r_oct(1+r_oct) = 1 − 1/4. **ID-1 rearranged.** |
| ID-4 | α₀² = α₂·α | (ab/π)² = (a²/π)(b²/π), i.e. (ab)² = a²b². **True by construction.** |
| ID-5 | ξ² = (1+r_tet)/r_oct | derived from ID-2. **Not independent.** (Mine — see §0b.) |

All verified symbolically; ID-4 and ID-5 return exactly 0 when the difference is simplified.

**The general form.** For any r = (√n − m)/(2m):

```
r(1+r) = (n − m²)/(4m²)     — always rational, for any integers n, m
```

This is automatic. It needs no sphere packing, no lattice, no physics. Both BCT radii have exactly
this shape:

- r_oct = (√2 − 1)/2 : n=2, m=1, k=2 = 2m → (2−1)/4 = **1/4**
- r_tet = (√6 − 2)/4 : n=6, m=2, k=4 = 2m → (6−4)/16 = **1/8**

Other members of the same family, which nobody selected and which no geometry produced:
(√3−1)/2 → 1/2. (√5−2)/4 → 1/16. (√10−3)/6 → 1/36. (√17−4)/8 → 1/64.

**Appendix KA3 knows this.** Its own proof of ID-2 reads: *"The difference of squares
(√6)² − 2² = 2 completes the proof."* The corpus states the mechanism correctly and then presents
the output as a discovery.

---

## 3 — PART 2: THE STATISTIC

**Population.** All surds of the form (√n − m)/k with 2 ≤ n < 40 (non-square), 1 ≤ m ≤ 6,
1 ≤ k ≤ 8, restricted to values between 0.01 and 0.99 — the range a void inradius could occupy in
units a = 1. **809 candidates**, of the same shape and complexity as BCT's two.

**Test.** Sixteen simple expression forms — r(1+r), r², 1−r−r², 1/r − r, r/(1+r), (1−r)/(1+r), and
so on — applied identically to every member. A "hit" is a clean rational: numerator and denominator
both ≤ 64.

**Distribution over the 809:**

| clean identities | surds | share |
|---|---|---|
| 0 | 632 | 78.1% |
| 1 | 91 | 11.2% |
| 2 | 4 | 0.5% |
| **4** | **80** | **9.9%** |
| 5 | 2 | 0.2% |

Mean 0.530 hits per surd.

**Where BCT sits.** r_oct scores **4**. r_tet scores **4**. Identically, and on the identical four
forms: `r(1+r)`, `r²+r`, `1−r−r²`, `4r²+4r` — which are four spellings of one expression.

**82 of 809 surds do as well or better — 10.1%.**

```
P = 0.1014   →   surprise = 3.302 bits    (both radii)
```

---

## 4 — THE CONTROL THAT SETTLES IT

Of the 809, exactly **82 have the form k = 2m**. Of those 82, how many satisfy
r(1+r) = clean rational?

```
82 of 82.   Hit rate: 100.0%.
```

And those 82 are *precisely* the 82 that match or beat BCT's score. **Membership in the k = 2m
family is the entire explanation.** There is no residue left for geometry to explain.

An identity satisfied by 100% of the numbers in its class carries **exactly zero information**
about which member of the class was chosen. r_oct and r_tet are not distinguished by these
identities. Any of the other 80 would produce the same four "discoveries."

---

## 5 — WHAT THIS DOES *NOT* SHOW

Stated carefully, because the result is strong and easy to over-read.

- **It does not touch α = α₀(1−2α₀) = 1/137.018.** That is a different kind of claim — a fit to a
  measured quantity, not an internal identity. Its surprise is a separate calculation and this note
  does not attempt it. The verdict here applies to the **identity family only**.
- **It does not show r_oct and r_tet are wrong.** They are the correct inradii of the octahedral
  and tetrahedral voids in this packing. That is geometry and it is right. What fails is the claim
  that their satisfying r(1+r) = 1/4 and 1/8 is *meaningful*.
- **The population is a choice.** Different bounds on n, m, k move the bits somewhat. The 100% rate
  in §4 is not a statistic, though — it is an algebraic consequence, and it does not depend on the
  population at all.
- **It does not close a gate.** No stop condition, no pre-registered digest. This is a note, and it
  should be run as a proper gate before anything is retired on its strength.
- **Sixteen forms is not exhaustive.** A wider expression space would raise everyone's hit count,
  BCT's included. The comparison is relative and that is the point.

---

## 6 — WHAT IT MEANS FOR THE PROGRAMME

The identity family has been read as corroboration — geometry throwing up clean numbers, taken as a
sign the geometry is right. On this evidence it is not corroboration. It is what writing
(√n − m)/(2m) always does.

**That changes the order of the remaining work.** I had suggested this question was load-bearing:
if the identities were surprising, the mechanism failures found in Ψ2, Λ and TANH would look like
repairs waiting to happen. They are not surprising. So the mechanism failures stand on their own,
without a countervailing signal from the algebra.

**What is left untested and now matters more:** the numerical predictions — α, m_e, the Koide
chain, the mass ratios. Those are fits to measured values, and their surprise is a genuinely open
question that Gate STAT answered for exactly one input (π⁵/6, zero bits) and nobody has answered
for the rest. **That is the next gate**, and it is a bigger one than this note.

---

*Note issued 11 September 2026. Five identities reduce to one; that one holds for 100% of numbers
of the form (√n − m)/(2m); surprise 3.3 bits against a 809-surd control. Two corrections recorded
against this thread's own prior statements.*
