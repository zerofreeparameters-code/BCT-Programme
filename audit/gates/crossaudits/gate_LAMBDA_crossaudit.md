# GATE Λ — CROSS-AUDIT AND RESPONSE TO CN-Λ-21

**Issued:** 11 September 2026, Gate Ψ2 execution thread — the session Λ could not locate.
**Standing:** not a re-run of Λ. A clause audit plus the primary-source response CN-Λ-21 asks for.

---

## 1 — CN-Λ-22 IS RIGHT, AND IT IS FIXED HERE

Λ could not verify Gate Ψ2 because the deliverable is unarchived. Correct, and my fault. The files
exist in this session and are attached:

| file | sha256 (first 16) |
|---|---|
| `gate_PSI2_prompt_asrun.md` | `948909cbd49a3fdf` |
| `gate_PSI2_RESULT.md` (v1) | `4b0e6bf23defa8df` |
| `gate_PSI2_CORRECTION_v2.md` | `455a2df414873c8b` |
| `gate_PSI2_ADDENDUM_v2_1.md` | `2d8707feb84b9dc0` |
| `gate_PSI2_ADDENDUM_v2_2.md` | `edda899037497f3e` |
| `gate_PSI2_step1_2.py` | `a5a213e1c9e82bfa` |
| `gate_PSI2_step3_5.py` | `6b8a00faa439ec60` |
| `gate_PSI2_corpus_scan.py` | `6494b10359b00523` |

Commit these before the next gate.

---

## 2 — CN-Λ-21: THE AMENDMENT IS ACCEPTED, THE RETRACTION IS NOT

**What Λ gets right.** CN-Ψ2-24's word *spent* is too strong. Λ is correct that nothing in the
corpus spends the relative phase, because no coupling is written for it to be spent on. The right
word is **committed**: the corpus *claims* θ₁−θ₂ is the Higgs (App AG.1) and the electron mass
(App I §2.3). A claim is not an expenditure. **CN-Ψ2-24 is amended accordingly.**

**Why it does not retract.** The notice was a dilemma about the corpus's own commitments, and
Λ's finding closes the second horn rather than opening it:

| horn | outcome for Ψ2 |
|---|---|
| App I's claims stand | θ₁−θ₂ is gapped → no Goldstone → Ψ2 closes |
| App I's claims fall (CN-Λ-01, CN-Λ-07) | the mode does not exist at all → no Goldstone → Ψ2 closes |

**CN-Ψ2-24R [PROVEN].** The corpus has committed θ₁−θ₂ to the mass sector. Ψ2's favourable outcome
requires those commitments to be false — and if they are false, Λ shows the mode is absent, not
free. Gate Ψ2 closes on both horns. Λ has made the closure *stronger*.

**CN-Λ-07 is CN-Ψ2-02, reached independently.** Λ calls it "the deepest finding of this gate."
Ψ2 v1 §4 and CN-Ψ2-02 state it from the same two sentences of App J §§1.1–1.2 — one field
everywhere, continuous at R, so θ₂ is not an independent degree of freedom. Λ could not know this
because of CN-Λ-22. **This is corroboration by an independent route, and it should be logged as
such rather than as a new finding.**

**On the verdict.** Λ correctly declines to settle it and asks for a primary-source check. Supplied:
Ψ2's verdict never rested on CN-Ψ2-24. **SC-Ψ2-2** fired on App I §2.2's own mode table with
App AG.2's gap; **SC-Ψ2-4** on the (n,ϑ) canonical pair, where ϑ's conjugate momentum is a density
variable — one pair, one mode, and it is the gapped one; **SC-Ψ2-5** on the homotopy separation
between App J's S¹ and App JH's S². CN-Ψ2-24 was a corollary, not a support. **The Ψ2 verdict
stands, and now stands on four grounds instead of three.**

---

## 3 — WHAT Λ FOUND THAT Ψ2 MISSED

Credited, verified, and adopted:

- **ξ = 1/√(8πα₀)** — a closed form. Ψ2 reconstructed ξ from App J's printed −0.424083 and got
  2.31754514195868; the closed form gives **2.31754379491166**. Mine was right to six digits;
  theirs is exact. **Adopt the closed form.**
- **CN-Λ-09** — the gap formula needs the *reduced* stiffness J₁J₂/(J₁+J₂), not the geometric mean.
  Verified: m² = λρ₁ρ₂(J₁+J₂)/(J₁J₂), ratio to the printed form (J₁+J₂)/√(J₁J₂) ≥ 2 by AM–GM,
  equality only at J₁ = J₂. The printed formula is never right. Ψ2 never examined that formula.
- **CN-Λ-18** — App J §3.2 and §4.1 already computed this failure and reported it (δE ~ 10⁻⁵ m_P,
  "18 orders too large"; Kondo "ruled out"), and App I's opposite conclusion is the one that
  propagated downstream. Strong, and new to me.
- **CN-Λ-17** — the mode cannot be both electron and Higgs. Verified: (m_H/m_e)² = **5.995 × 10¹⁰**
  against Λ's 6.008 × 10¹⁰. This is a sharper form of what CN-Ψ2-24 was reaching for, and it does
  not depend on λ.
- **CN-Λ-16** — verified end to end: ρ₁ = 0.0079437, ρ₂ = 0.0231859, m_gap = 1.168 × 10⁻³ m_P,
  10^19.446 over m_e, 10^14.057 over m_H. Matches Λ's printed 19.45 / 14.06.

---

## 4 — THREE ERRORS IN Λ

**(a) CN-Λ-08 runs two different claims together, and only one is adjudicated.**

*Which J* — stiffness, not Josephson coupling — **is** adjudicated by the corpus, on the four
citations Λ gives. Correct.

*J₁ = J₂ = 1* is **not**. App J's "in units where J = 1" fixes the **exterior** stiffness; App I
§6.1's own table lists **J₂ as still to be computed**, "from sphere interior GP action." Setting it
to 1 is an assumption imported from the other component.

It is also in tension with the GP physics Λ relies on elsewhere: the GP phase stiffness is
J = ħ²ρ/m, so **J ∝ ρ** — and Λ's own Step 2 gives ρ₁ = 0.0079 against ρ₂ = 0.0232, so J₁ ≠ J₂.
Under J_i = cρ_i, Λ's corrected formula becomes

```
m² = λρ₁ρ₂(J₁+J₂)/(J₁J₂) = λ(ρ₁+ρ₂)/c
```

— the standard Leggett-mode result, which is a good consistency check on CN-Λ-09 and a bad one for
J₁ = J₂ = 1. **Disposition:** split CN-Λ-08. Keep the symbol adjudication; drop the value claim to
an assumption and say so. SC-Λ-2 correctly does not fire either way, and §5's 10^19 is untouched.

**(b) "Fourth consecutive" is false, and this is now the second gate to print it.**

Λ §0: *"the fourth consecutive gate with a broken pre-registration chain (R2, P, J, Λ)."* Gate LAM
printed the identical claim with LAM in the last slot. The sequence is **R2, P, J, Ψ2, LAM, Λ**.
**Ψ2 ran on a confirmed digest** — curl from commit `f6de7dc1…`, hashed on disk before opening,
match recorded against `948909cb…35a4`, 6679 bytes. The run was broken there.

Λ is the **fifth instance** and the **second regression after a demonstrated repair**. The fix is
not merely "on the ledger"; it has been executed successfully, once, and skipped twice since. Both
misstatements trace to CN-Λ-22 — neither session could see that Ψ2 had a digest. The archiving gap
is now producing factual errors in other gates' deliverables, which raises its priority.

**(c) CN-Λ-02 is a string match presented as a concept claim.**

*"θ₁ − θ₂ occurs exactly once in either corpus."* True of that exact string. But App I §5.1 writes
the same object as **φ₁ − φ₂**, and App AG.1 writes it as **(Ψ₁−Ψ₂)/√2**. The conceptual claim —
never written into an action, Lagrangian or Hamiltonian — survives and is correct. The count does
not support it, and a reader checking the count will find the notice fails. Restate as the
conceptual claim with the three notations listed.

---

## 5 — NOT DISPUTED

CN-Λ-01, -03, -04, -05, -06, -07, -09, -10 (correctly tiered CONJECTURE), -11, -12, -13, -14,
-15, -16, -17, -18, -19, -20, -22 stand. **CN-Λ-20 is the deliverable's best work** — separating
"nine structural claims lost" from "zero published numbers lost," and saying so plainly rather
than letting the verdict read as bigger than it is. The three stop conditions fire.

§9 is the right shape: the ZIP-page-image caveat, the UNLOCATED-not-phantom tiering of Song &
Foreman, and the untouched private repo are all declared before anyone asks.

---

*Cross-audit issued 11 September 2026. CN-Ψ2-24 amended to CN-Ψ2-24R, not retracted; Ψ2 verdict
stands on SC-Ψ2-2, -4, -5 and is now archived. Findings against Λ: one notice conflating an
adjudication with an assumption, one factual error shared with Gate LAM, one miscounted string.*
