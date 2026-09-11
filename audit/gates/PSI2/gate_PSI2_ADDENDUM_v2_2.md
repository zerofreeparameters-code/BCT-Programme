# GATE Ψ2 — ADDENDUM v2.2

**Issued:** 11 September 2026, same execution thread.
**Scope:** clause-by-clause audit of `CORRECTION v2`, applying the rule v2.1 §E set. v2 had not
been put through it. Verdict unchanged.

---

## A — ERROR FOUND: CN-Ψ2-06 WAS WRONGLY LISTED "UNAFFECTED"

v2 §5 lists CN-Ψ2-06 among the notices unaffected by the correction. **It is affected, and its
numbers are now wrong.**

CN-Ψ2-06 reads: *"range 0.159–1.440 ℓ_P; at 1 mm the suppression is e^(−4.30×10³¹) at the most
generous gap."* Both figures were computed from the six routes v1 had. v2 then added a seventh —
App AG.2's 2α₀m_P = 0.0148161 — which is **smaller than every route in v1's bracket** and whose
range, 67.494 ℓ_P, falls **outside** the stated 0.159–1.440 ℓ_P. v2 introduced the number in §3
and did not carry it into the notice that states the bracket.

**Corrected set, all seven routes:**

| route | gap (m_P c²) | range (ℓ_P) |
|---|---|---|
| **App AG.2, corpus's own** | **0.0148161** | **67.4941** |
| constructed √(E_C E_J) | 0.694278 | 1.44035 |
| transmon √(8E_C E_J) | 1.96371 | 0.509239 |
| Letter 36 1/α₀, √(E_C E_J) | 2.06568 | 0.484102 |
| App J's printed κ₀ | 3.39046 | 0.294945 |
| Letter 36 1/α₀, √(8E_C E_J) | 5.84262 | 0.171156 |
| hard-wall κR = π | 6.28319 | 0.159155 |

**CN-Ψ2-06R [PROVEN].** Gap bracket **[0.0148161, 6.28319] m_P c²**; Yukawa range
**[0.159155, 67.4941] ℓ_P**. At r = 1 mm the suppression at the **most generous** gap is
**e^(−9.17×10²⁹)**, not e^(−4.30×10³¹). The mode still mediates nothing at any observable
distance, so the verdict is untouched — but the notice as written understates the range by a
factor of 47 and overstates the suppression exponent by a factor of 47. Use the corrected figures.

## B — CLAIM VERIFIED THAT v2 ASSERTED WITHOUT CHECKING

v2 §1 states App D.3, App I, App AG and App AT are "none of which is in the repo." **True, now
checked rather than assumed:** no repo `.tex` matches D.3/D3, App I, or App AT, and no repo file
anywhere contains "out-of-phase", "anti-bonding" or "E_anti". App I's mode table and App AG's
E_gap exist only on the mount.

**One rider.** `tex/BCT_Appendix_AG1_VacuumLuminescence.tex` (and a `_final` copy) **does** sit in
the repo. It is a different appendix from the App AG that carries Higgs criticality and
E_gap = 2α₀m_P. A future scan matching on "AG" will hit it and may wrongly conclude App AG is
repo-resident. Flag for the naming-collision list alongside the two Letter 36s and the four App JH
copies.

## C — LOAD-BEARING CONVENTION, NOW VERIFIED

CN-Ψ2-22 and CN-Ψ2-24 depend on App I's θ₁/θ₂ meaning the same as the gate's. v2 assumed it.
Checked: App JH defines `\Psiext = \Psi_1` and calls it "the exterior void condensate"; App I §2.1
has Ψ₁ in void space, Ψ₂ inside the spheres. **Ψ₁ = exterior, Ψ₂ = interior throughout, matching
the gate.** App I's out-of-phase mode θ₁−θ₂ is therefore exactly the gate's ϑ, and CN-Ψ2-22/24
rest on the correct identification.

## D — THE PATTERN, THIRD INSTANCE

v1's failure was a corpus-wide claim from an unaudited search space. v2.1's two findings were
trailing clauses on notices whose headlines were checked. **v2's failure is the same shape again:
its "unaffected" list was asserted, not audited.** Marking eighteen notices unaffected is eighteen
claims, and I made them in one line without re-reading the notices against the new number.

**Method note, superseding the softer version in v2.1 §E:** when a correction introduces a new
quantity, every notice that states a bound, bracket or range must be re-evaluated against it
explicitly, one at a time. An "unaffected" list is a set of findings, not a formality, and it
needs the same standard of evidence as the finding that prompted the correction.

---

## E — UNCHANGED

Verdict, all stop conditions, CN-Ψ2-22/23/24/25/26/27/28, and the retraction of CN-Ψ2-01 all
stand. Gate Ψ2 remains **closed, unfavourably, on both interiors**, executed once, on a confirmed
digest. Read order: v1 → v2 → v2.1 → v2.2.

---

*Addendum issued 11 September 2026.*
