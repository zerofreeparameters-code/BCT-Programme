# BCT — PRE-REGISTRATION OF UNTESTED PREDICTIONS

**Registered:** 13 September 2026.
**Author:** Michel Robert Cabrié (ORCID 0009-0007-9561-9859).
**Repo state at registration:** commit and tarball digest recorded in §5 below.

---

## 0 — WHY THIS DOCUMENT EXISTS

Gate PRED closed on **SC-PRED-1**: the corpus's ~92 retrospective sub-1% predictions carry
approximately zero evidential weight *as a collection*. The reason is not that the numbers are
wrong — 39 of 40 recomputed correctly — but that sub-1% agreement is cheap in the corpus's own
alphabet: with ≤3 atoms and one correction factor, a random expression matches *some* measured
target about half the time.

Gate PRED also found **no SC-PRED-5 item**: not one prediction in the corpus was fixed before its
measurement and later confirmed.

That is the gap this document closes. **A prediction registered before the measurement, with its
formula fixed and its digest public, carries evidential weight that no retrospective fit can.**
Gate PRED's own counterfactual makes the size of the prize explicit: had the eligible hits been
pre-fixed single expressions, the corpus would have scored ~90 bits instead of ~0.

**This is the only route by which BCT can now earn evidential weight.** Everything below is
therefore stated so that it can fail.

---

## 1 — THE REGISTERED PREDICTIONS

Each entry fixes: the quantity, the **exact closed form**, the numerical value, the experiment that
will test it, and — critically — **the condition under which the prediction is wrong.**

No entry may be amended after registration. If a formula is revised, the revision is a **new**
entry with a new date, and the original remains on the record as registered and superseded.

### P-1 — Neutrino mass sum

| | |
|---|---|
| Quantity | Σm_ν |
| BCT value | **≈ 59 meV** |
| Source | Vol 1, seesaw scale argument: *"predicts that the neutrino mass sum will be measured at approximately 59 meV"* |
| Tests it | DESI / Euclid / CMB-S4 cosmological bounds; long-baseline + KATRIN-class direct limits |
| **Fails if** | Σm_ν measured **< 50 meV or > 70 meV** at 2σ. Current cosmological bounds already press near the lower edge; a firm sub-50 meV result kills it. |
| Status of the formula | The corpus states the value, not a unique closed form. **Before this counts, the closed form must be written and its digest added here.** Until then P-1 is registered as a *number*, which is weaker. |

### P-2 — Tensor-to-scalar ratio

| | |
|---|---|
| Quantity | r |
| BCT value | **r = 0.004624** (printed: (4α₀/π)²·S_D4/(1−x)²) |
| Tests it | CMB-S4, LiteBIRD, Simons Observatory |
| **Fails if** | r measured outside **0.003–0.007**, or a detection at r > 0.01, or an upper limit below 0.003. |
| Note | A second-order variant 0.004668 is also printed in the corpus. **Registering the first; the existence of two values is itself recorded.** |

### P-3 — Proton lifetime

| | |
|---|---|
| Quantity | τ(p → e⁺π⁰) |
| BCT value | **≈ 10^35.9 yr**, from M_R = 6.695×10¹⁴ GeV (App HP4) |
| Tests it | Hyper-Kamiokande |
| **Fails if** | proton decay observed at **τ < 10^35 yr**, or excluded above **10^37 yr**. |
| **Registered caveat** | **Two independent gates — MP and PRED2 — found M_R is defined as M_R ≡ m_P·α₀² in App GG2, with m_P supplied as an input. Substituting gives m_P = m_P: an identity, not a derivation.** P-3's input is therefore circular, and the gravity sector has no independent content. Recorded at registration, not discovered later. **A prediction resting on a circular input should arguably not be registered at all; it is retained here only because τ_p is independently testable and the caveat is visible.** |

### P-4 — Neutron electric dipole moment

| | |
|---|---|
| Quantity | d_n |
| BCT value | **d_n = 0** (App DM; App HO4) |
| Tests it | n2EDM at PSI, TUCAN, SNS nEDM |
| **Fails if** | any nonzero d_n measured at ≥3σ. |
| Note | This is the **sharpest** entry: an exact zero, falsifiable by a single positive detection, with no correction factor available to rescue it. **It is the best prediction in the corpus by this criterion.** |

### P-5 — CKM CP-violating phase — **WITHDRAWN, ALREADY FALSIFIED**

| | |
|---|---|
| Quantity | δ_CKM |
| BCT value | arccos(1/3) = 70.5288° (App BY) |
| Measured | γ = 65.75 ± 1.07° (LHCb / Belle II global fits) |
| **Status** | **FALSIFIED — 4.5σ.** Identified by Gate PRED2, 14 September 2026, after this document was drafted and before it was deposited anywhere. |

**This entry is withdrawn and retained on the record rather than deleted.**

It was drafted as a live prediction on 13 September. Gate PRED2 found the next day that
arccos(1/3) sits 4.5σ from the measured γ. It was therefore already dead at the moment of
drafting — not falsified *by* a later measurement, but falsified by a measurement that
already existed and had not been checked against.

Retaining it visibly is the point. A pre-registration that quietly drops a failed entry is
worth nothing, because a reader cannot tell what else was dropped. **The record must show what
was registered, what failed, and when it was found to fail.**

The corpus also states δ = −π/2 elsewhere. That conflict is now moot for registration purposes:
neither value is registered, and both require a Cold Ledger gate before either is claimed again.

### Not registered — and why

**m_DM.** The corpus's dark-matter mass has moved at least five times (14.97 → 24.6 → 30 →
63 GeV → 4×10⁻¹² eV). A quantity that has taken five values is not a prediction. **It is excluded
until one value is fixed and registered.** Recording the exclusion is part of the registration.

---

## 1b — REVIEW AGAINST GATE PRED2 (14 September 2026)

This document was drafted 13 September. Gate PRED2 closed the following day and its findings
are applied here rather than left to be discovered by a reader.

| entry | PRED2 finding | action |
|---|---|---|
| P-1 Σm_ν | no closed form located; registered as a bare number | **stands, weakened** — must not be counted as a formula-level prediction |
| P-2 r | two printed values (0.004624, 0.004668) | **stands**; the first is registered, the conflict is on the record |
| P-3 τ_p | M_R circular, confirmed by two gates | **stands with an explicit warning** — see the caveat above |
| P-4 d_n = 0 | no correction factor available; nothing to tune | **stands, and is the strongest entry** |
| P-5 δ_CKM | 4.5σ from measured γ | **WITHDRAWN — falsified** |

**The general lesson PRED2 supplies, and the reason it belongs in a registration document:**
the four BCT expressions that scored positively were exactly the four carrying **no post-hoc
correction factor**. Every expression with a dressing term scored negatively, the worst at
−17.1 bits because 126,661 grammar candidates were available to it. Rule 3 below is therefore
not a formality — it is the difference between a prediction and a fit.

## 2 — THE RULES THIS REGISTRATION BINDS ITSELF TO

1. **No amendment.** A changed formula is a new entry, dated, with the original retained.
2. **No post-hoc tolerance.** The failure conditions above are the failure conditions. They are not
   to be widened after data arrives.
3. **No correction factors.** The N-class pattern X·(1+Nα₀) that Gate PRED identified as the
   corpus's fitting mechanism **may not be applied to any entry here** after registration.
4. **A miss is reported.** If a prediction fails, that is published as prominently as a hit would
   be. This is the condition that makes a hit mean anything.
5. **One quantity, one entry.** Where the corpus states two values (P-2, P-5), one is registered
   and the conflict is declared.

---

## 3 — WHAT A HIT WOULD BE WORTH, HONESTLY

**P-4 is the strongest.** An exact zero with no free parameter, falsifiable by one detection. If
n2EDM reaches 10⁻²⁷ e·cm and finds nothing, that is a genuine confirmed prediction — though note
the Standard Model also predicts d_n far below current sensitivity, so a null result is **weakly**
discriminating. It becomes strong only if the SM prediction and BCT's differ measurably.

**P-2 and P-5 are the most discriminating** — both are specific numbers in ranges where competing
theories predict differently, and both are testable this decade.

**P-1 and P-3 are the weakest.** P-1 lacks a closed form. P-3 rests on a circular input.

**None of these individually rescues the programme.** Gate PRED's ~0 bits stands on the
retrospective set regardless of what happens here. What a confirmed pre-registered prediction
buys is **new** evidential weight, earned honestly, which is the only kind BCT does not currently
have.

---

## 4 — HOW TO REGISTER THIS PROPERLY

Committing this file to the repo is necessary but **not sufficient** — a repo can be rewritten.
For the registration to be worth anything to a sceptical reader:

1. Commit this file. Record the commit SHA and the file's SHA-256 in §5.
2. **Deposit it on Zenodo**, which issues an immutable DOI with a timestamp you cannot alter.
   Note the corpus's `ZENODO_DOIS.md` currently reads "Total records: 0" — that sync is broken and
   should be fixed first.
3. Optionally post the SHA-256 somewhere publicly timestamped and outside your control.

**Step 2 is the one that matters.** A prediction is only pre-registered if a third party can verify
it predates the measurement.

---

## 5 — DIGESTS AT REGISTRATION

To be completed at commit time:

```
this file, SHA-256 :  __________________________________________________
repo commit        :  __________________________________________________
Zenodo DOI         :  __________________________________________________
date registered    :  13 September 2026
```

---

*Registered 13 September 2026, following Gate PRED (SC-PRED-1) and Gate MP (SC-MP-1 with
circularity). Five predictions registered, one excluded. Failure conditions stated. No amendment
permitted.*
