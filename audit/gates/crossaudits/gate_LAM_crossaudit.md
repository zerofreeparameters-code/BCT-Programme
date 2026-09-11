# GATE LAM PHASE 1 — CROSS-AUDIT FROM THE Ψ2 THREAD

**Issued:** 11 September 2026, Gate Ψ2 execution thread.
**Standing:** not a re-run of LAM. A clause audit by the session whose notices LAM cites
(CN-Ψ2-01R, -18, -24, -26, -27), applying the rule of ADDENDUM v2.1 §E / v2.2 §D.
**Numbers below:** mpmath, 50 dps working.

---

## 0 — WHAT REPRODUCES

Checked and correct:

| LAM claim | check |
|---|---|
| CN-LAM-03: α₀/g = 20.035 | **20.0352976401** ✓ |
| CN-LAM-04: σ_s = α₀ at R=½, α₀/4 at R=1 | 0.0074080557 / 0.0018520139 ✓ exactly α₀ and α₀/4 |
| CN-LAM-18: 4πR is a length, doubles under R=1 | ✓ (2π → 4π) |
| CN-LAM-17: App I has no `.tex` in the repo | ✓ **independently confirmed** in Ψ2 ADDENDUM v2.2 §B — no repo file contains "out-of-phase", "anti-bonding" or "E_anti" |
| §2 search-space audit per CN-Ψ2-27 | ✓ correctly applied; mount-index ∪ repo, bounded and declared |

**CN-LAM-03 is a real find and I missed it.** App J §3.1's text was in front of me in my first
corpus search of the Ψ2 run. I used it for CN-Ψ2-01 and did not notice that the appendix prints
g = 0.00036975 and then boxes g ≈ α₀, two orders of magnitude away. It belongs on the Ψ2 ledger
as a notice I failed to raise.

---

## 1 — CN-LAM-02 IS WRONG, AND IT CONTRADICTS CN-LAM-03

CN-LAM-02 asserts: *"App AG.2 reads … 'J_Josephson = α₀ … (App J)'. **App J says no such thing.**
App J says σ_s = α₀·J."*

App J says exactly that thing, twice:

- **App J §3.1, boxed:** *"The dimensionless Josephson coupling between the sphere interior and the
  oct void electron vortex is **g = α₀** to leading order."*
- **App J §5.1, summary table:** *"Josephson coupling g = α₀ | **DERIVED** | Same geometric origin
  as EM coupling."*

**App AG.2's citation is accurate.** It faithfully quotes App J's own boxed conclusion. The error
is App J's — and CN-LAM-03 is precisely the demonstration that App J's boxed conclusion is wrong
by 20×.

**So -02 and -03 cannot both stand.** CN-LAM-03 proves App J says the thing CN-LAM-02 claims App J
never says. The two notices are in direct contradiction inside one deliverable, and the correct
one is -03.

**Consequence for CN-Ψ2-26, which LAM set out to dissolve.** The collision is **not** dissolved:

| | |
|---|---|
| LAM's reading | one document misquoting another; resolves to the stiffness reading |
| Corrected reading | **App J §3.1 itself conflates them**, by boxing a phase-independent surface coupling as "the Josephson coupling = α₀"; App AG.2, AN.2 and AT.3 inherit it by accurate citation |

CN-Ψ2-26 stands, with its **origin relocated** from "two documents using one symbol" to "one
document's discarded `tanh²` factor." That is a worse finding than either notice alone: the blast
radius is the same, but the fault is at the source rather than in transmission, so repairing
App AG.2 alone would not fix it.

---

## 2 — CN-LAM-07 IS REFUTED BY CN-LAM-01

CN-LAM-07 (tiered PROVEN) says the corpus's `ρ₁ρ₂` is the pair-tunnelling (`cos 2θ₋`, Z₂)
signature while its narrative is single-particle (`cos θ₋`, `√(ρ₁ρ₂)`), so *"formula and narrative
are different mechanisms and cannot both be right"* and λ *"is not even a well-typed symbol."*

**CN-LAM-01, in the same deliverable, establishes that J₁ and J₂ are GP/XY phase stiffnesses.**
For a Gross–Pitaevskii superfluid the phase stiffness is J = ħ²ρ/m, i.e. **J ∝ ρ**. Substituting
J_i = cρ_i into the corpus's formula:

```
λ ρ₁ρ₂ / √(J₁J₂)  =  λ ρ₁ρ₂ / (c √(ρ₁ρ₂))  =  (λ/c) √(ρ₁ρ₂)
```

**That is exactly the single-particle form CN-LAM-07 says it contradicts.** The `ρ₁ρ₂` in the
numerator is cancelled to `√(ρ₁ρ₂)` by the stiffnesses in the denominator, under the very
identification CN-LAM-01 proves. Formula and narrative agree.

**Disposition.** CN-LAM-07 should be **retracted**, or at most re-tiered CONJECTURE with the J ∝ ρ
cancellation stated and the pair-tunnelling reading offered as the alternative that survives only
if J is *not* proportional to ρ. The downstream claim that λ is not a well-typed symbol falls with
it. §1's verdict is unaffected — λ is still unformulated for the reasons in CN-LAM-05 — but it
loses one of its two supports.

This is the same failure mode logged three times on the Ψ2 ledger: a notice whose headline is
checked against primary source, carrying a structural inference that was not checked against the
deliverable's own other notices.

---

## 3 — CN-LAM-11 MISCHARACTERISES THE CIRCULARITY

CN-LAM-11 says App I §6.2's target `λρ_BCT = 1/51.5` is *"Letter 19's instanton action S_e"*, and
concludes the corpus *"collapses one mechanism into the other's answer."*

| quantity | value |
|---|---|
| ln(m_P/m_e), CODATA masses | **51.5278398904** |
| Letter 19's S_e | 51.5279810815 |

**51.5 is the observed hierarchy**, which Letter 19 *also* targets and reproduces to −0.0141%. It
is not Letter 19's output; it is the measurement both mechanisms aim at. App I §6.2 is not
borrowing from Letter 19 — it is fitting to data, and it would read the same if Letter 19 did not
exist.

**SC-LAM-4 still fires**, on its literal wording — *derivable only by assuming … the electron
mass.* The verdict is right. But the reason must be restated as **fitting to the measured
hierarchy**, not as inter-document borrowing, and LAM's §5.5 claim to have settled the gate's
§2.2 two-mechanism question does not follow: two mechanisms independently targeting one
measurement is not one adopting the other's answer. §2.2 remains open.

---

## 4 — CN-LAM-16's "FOURTH CONSECUTIVE" IS FALSE

CN-LAM-16: *"the **fourth consecutive** gate with this defect (R2, P, J, LAM)."*

The sequence is **R2, P, J, Ψ2, LAM**. Gate Ψ2 ran on a confirmed digest: fetched by `curl` from
commit `f6de7dc1…` at a `raw.githubusercontent.com` URL, hashed on disk before opening, match
recorded against the pre-registration (`948909cb…35a4`, 6679 bytes). **The run was broken.** LAM's
own prescribed fix — commit-pinned raw URL, curl to disk, hash there — is not merely "already on
the ledger"; it was **executed successfully one gate earlier**.

Corrected: LAM is the fourth *instance* and the **first regression after a demonstrated repair**.
That is a sharper and more actionable finding than "fourth consecutive," because it removes the
excuse that the fix is untested.

---

## 5 — WHAT I AM NOT DISPUTING

CN-LAM-05, -06, -08, -09, -10, -12, -13, -14, -15, -17, -18 are not challenged here; -09 in
particular (three unavailable inputs besides λ, so Phase 2 is blocked independently) is the
deliverable's strongest result and is untouched by anything above. The **recommendation not to
open Phase 2 stands**, and stands even with -07 retracted and -11 restated.

§9's contamination statement is the right call and is well made: declaring the firewall broken
rather than claiming a cold run is the correct disposition, and the tiering instruction that
follows from it should be honoured.

---

## 6 — NET EFFECT ON THE Ψ2 LEDGER

- **CN-Ψ2-26 stands, origin relocated** (§1). The collision is App J §3.1's own, not a transmission
  error.
- **New notice owed to LAM, CN-Ψ2-29 [PROVEN]:** App J §3.1 computes g = 0.00036975 and boxes
  g ≈ α₀, discarding a factor of 20.035. Credited to Gate LAM CN-LAM-03. Missed by the Ψ2 run
  despite having the passage in hand.
- CN-Ψ2-24 as cited by LAM §10 is correctly used and unaffected.

---

*Cross-audit issued 11 September 2026. Not a re-run of Gate LAM. Findings: 1 notice contradicted
by its own neighbour (-02 vs -03), 1 notice refuted by its own neighbour (-07 by -01), 1 notice
right-verdict-wrong-reason (-11), 1 factual error (-16). Verdict and recommendation unaffected.*
