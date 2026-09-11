# GATE Ψ2 — ADDENDUM v2.1

**Issued:** 11 September 2026, same execution thread.
**Trigger:** re-reading the reconstructed v1 alongside CORRECTION v2.
**Scope:** two residual errors in v1 that CORRECTION v2 did **not** catch. Verdict unchanged.

---

## A — PROVENANCE OF THE RECONSTRUCTED v1

The `GATE Ψ2 — RESULT` file supplied for cross-check is **this thread's own v1 deliverable**,
rebuilt from the execution transcript with retraction banners added. It is not an independent
execution and carries **no corroborative weight**. Every figure in it is one I produced; agreement
between it and my run is agreement of a document with itself.

Recorded so the ledger does not later mistake it for a replication. **Gate Ψ2 has been executed
once.**

## B — THE SCRIPTS ARE NOT LOST

The reconstruction note states the three scripts "were not recoverable in full from the transcript
and are not reproduced alongside this file." In this thread they are intact and still execute:

| script | sha256 (first 16) | status |
|---|---|---|
| `gate_PSI2_step1_2.py` | `a5a213e1c9e82bfa` | re-runs, reproduces |
| `gate_PSI2_step3_5.py` | `6b8a00faa439ec60` | re-runs, reproduces |
| `gate_PSI2_corpus_scan.py` | `6494b10359b00523` | re-runs — **but see §D** |

They should be attached to the archived v1. Note the erratum already recorded in v1 §13: the
prose line in `step3_5` says "0.6%"; the computed figure two lines above it, and the correct one,
is **0.118%**.

---

## C — RESIDUAL ERROR 1: CN-Ψ2-05's CLOSING CLAUSE IS FALSE

v1 CN-Ψ2-05 ends: *"The corpus states the locked horn itself, with a number, **and has never
connected it to Ψ₂**."*

**The second clause is wrong, and v2 let it stand.** App I §2.2 connects the Josephson splitting
directly to the interior–exterior relative phase — θ₁−θ₂ *is* the Ψ₁/Ψ₂ relative phase, by App I
§2.1's own definition (Ψ₁ = void space, Ψ₂ = sphere interior). App I §5.1 then states the
connection explicitly: the coupling splits only the out-of-phase mode. The corpus connected the
locked horn to Ψ₂ in App I, several appendices before App J.

**CN-Ψ2-05R [PROVEN].** Letter 36 (D4-qubit) eq (3) states E_J/E_C = 1/α₀ = 134.99, "the transmon
regime"; rms phase spread (2α₀)^¼ = 0.349 rad. This is a *second* corpus statement of the locked
horn, independent of App I's. **Delete the claim that the corpus never connected it to Ψ₂** — App I
did, and CN-Ψ2-22/23 record it.

## D — RESIDUAL ERROR 2: CN-Ψ2-01's PROPAGATION LIST WRONGLY NAMES App I

v1 CN-Ψ2-01 closed: *"The name has propagated to App I, App J, App JH, both Letter 36s and App AZ."*

Beyond the retracted universal claim, the **list itself is wrong about App I**. App I does not
mis-name anything: it uses "Josephson coupling" correctly, for a term that splits the out-of-phase
mode and not the in-phase mode — which is what a Josephson coupling does. Listing App I as a
carrier of the error inverted the one appendix that had it right.

**Corrected list.** The mis-naming (a phase-independent ∮|Ψ|² surface integral called a Josephson
coupling) is confined to **App J §3.1 and App JH eq (13)**. App I is removed from the list. Letter
36 (D4-qubit) and App AZ use the word for genuine couplings and are removed as well; CN-Ψ2-19's
complaint against Letter 36 eq (2) is about a broken algebraic chain, not about the name.

Net: CN-Ψ2-01R stands as written in v2 §2, with the propagation list reduced from six documents to
two.

## E — WHY BOTH SURVIVED v2

Both errors sit in clauses appended to notices whose **main claims were correct**. v2 audited the
headline claim of each notice and passed over the trailing qualifiers. The pattern is worth
recording: a retraction pass that checks only the load-bearing sentence of a notice will leave
intact the incidental claims attached to it, and those are exactly where unchecked assertions
accumulate.

**Method note for the ledger, alongside CN-Ψ2-27:** when a notice is revised, revise the *whole*
notice, clause by clause, not the finding it is named for.

---

## F — WHAT IS UNCHANGED

Verdict, all stop conditions, and every other notice stand as in v2:

- **SC-Ψ2-2** fires on App I §2.2's mode table, gap 2α₀m_P = 0.0148161 (App AG.2).
- **SC-Ψ2-4** fires. **SC-Ψ2-5** fires; Gate PT remains blocked.
- **SC-Ψ2-3** does not fire as worded.
- **CN-Ψ2-24** stands: θ₁−θ₂ is already spent on the Higgs and the electron mass, so a favourable
  verdict was never available without breaking the BCT mass mechanism.

Gate Ψ2 remains **closed, unfavourably, on both interiors**, executed once, on a confirmed digest.

---

*Addendum issued 11 September 2026. Read v1 → CORRECTION v2 → this, in that order.*
