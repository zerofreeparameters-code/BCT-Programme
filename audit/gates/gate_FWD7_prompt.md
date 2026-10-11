# Gate FWD7 — pre-registration

**Which forward predictions of the BCT corpus are still standing, and which of them would a geometry-free grammar also make?**

Drafted 11 Oct 2026 for M. R. Cabrié by Claude (Fable 5.1), warm thread. Status: PRE-REGISTERED, UNRUN. Commit to `audit/gates/gate_FWD7_prompt.md`, record the digest in `audit/gates/PREREG_20261011_FWD7.sha256`, run in a fresh thread with memory paused and past-chat search off. One gate per thread. Same-session results capped at CONJECTURE.

---

## 0. Why this gate exists

Gates PRED, PRED2 and FORK have between them closed the retrodiction layer. Every number the corpus matched to an already-measured constant is reproducible by short formulas from a small alphabet, with or without the void geometry (FORK CN-FORK-02; a pilot on 11 Oct showed the same for minimum-complexity and best-two-atom-error statistics). No scoring rule applied to known constants can come out in the geometry's favour, because the grammar hits everything.

PRED2 §5 identified the only place evidential weight can still be earned: **seven out-of-sample predictions** whose tests lie in the future. It listed them and stopped. It did not check them against gates closed since (EDM, THETA, D4, CRIT), did not fix a single defended value for each, and did not ask the FORK question of them: would the same numbers fall out of a grammar with the geometry removed?

This gate does those three things and nothing else. Its output is a list of zero or more pre-registrable predictions, each with one value, one test, one date, and a base-rate statement, ready for Zenodo. An empty list is a finding.

## 1. What is fixed before the run

Everything in §§2–5. Digest of this file is the record. No prediction is added to or removed from the list in §2 during the run; a prediction found elsewhere in the corpus is logged in §8 as "not pre-registered here" and goes nowhere else.

## 2. The seven (verbatim from PRED2 §5, repo commit `bc5c87dc` or later)

| # | prediction | printed value | test | date |
|---|---|---|---|---|
| P1 | neutron EDM | d_n ≈ 10⁻³² e·cm; falsified if \|d_n\| > 3×10⁻³¹ | n2EDM (PSI) | ~2028 |
| P2 | no QCD axion (anti-prediction) | discovery falsifies | ADMX / IAXO | ongoing |
| P3 | tensor-to-scalar ratio | r = 8/S_D4² = 0.0046 | LiteBIRD, CMB-S4 | 2028–2033 |
| P4 | dark-matter scalar | 62.9 GeV, D4 Z₂-stable | LZ / XENONnT | 2025–2030 |
| P5 | leptonic CP phase | δ_CP = −π/2 exact | Hyper-K, DUNE | 2027+ |
| P6 | proton lifetime | τ_p ~ 10³⁵·⁹ yr | Hyper-K | 2027–2045 |
| P7 | c_GW = c exactly | any confirmed deviation falsifies | LVK O5+ | ongoing |

The run also records, without scoring, the CKM-phase pair PRED2 flagged (`arccos(1/3)` vs `arccos(2r_oct)`) as an example of a prediction already contradicted at ~4.5σ, to calibrate what "falsified" looks like in this corpus.

## 3. Three questions, asked of each of the seven in order

**Q-A — Is it still standing on the ledger?** For each Pn, locate its derivation in the corpus (volume, appendix, equation) and list every Cold Ledger verdict that touches an ingredient of that derivation. Known dependencies to check, not exhaustive:

- P1, P2 rest on θ_QCD = 0. Gate EDM (SC-EDM, 16 Sep) found all three θ = 0 derivations assume the conclusion, the d_n floor quoted three ways across two orders of magnitude, and the corpus's own δθ = 2.4×10⁻⁹ inconsistent with its own floor. Gate THETA exists in the repo; read its verdict.
- P3, P4 rest on D4 / S_D4 = π⁵/6. Gate D4 (19 Sep) found the lattice FCC, not D4. Gate STAT scored the π⁵/6 identity family at 3.3 bits.
- P5 rests on the CP sector. Gates HERM / CA-FLAVOUR found no single quark mass matrix (THE KNOT); check whether δ_CP = −π/2 is derived from a lepton structure that survives or is asserted.
- P6 depends on the unification scale; check which gates touch it.
- P7 rests on the acoustic metric (Gate N: h^TT ≡ 0; prior art per CN-QP-04). Check whether c_GW = c is a BCT output or a property of every acoustic-metric model.

Classify each: **STANDING** (no closed gate removes an ingredient), **WOUNDED** (an ingredient is CONJECTURE-tier or inconsistent but the number can be stated with that tier declared), **DEAD** (an ingredient is closed; the prediction has no derivation left in the corpus as written).

**Q-B — One defended value.** For each STANDING or WOUNDED prediction, fix exactly one numerical statement that the corpus supports, with the falsification threshold. Where the corpus quotes several values (P1 has three), take the one the most recent appendix defends and record the others as superseded. Where the prediction is "exact" (P5, P7), state the precision at which the test can refute it and whether the corpus's claim survives at a weaker precision.

**Q-C — The base rate, FORK-style.** For each STANDING or WOUNDED prediction with a numerical value, ask: from the PRED grammar **with r_oct, r_tet, α₀ removed** (the 14 non-geometric atoms, J1–J3 as in `pred_step2_nullmodel.py`, copied byte-for-byte), how many distinct 2-atom and 3-atom expressions land within the falsification window of the predicted value? Report the count and the fraction of the grammar's range it represents. For "exact" predictions (P5 = −π/2, P7 = c), the base-rate question is instead: how many other simple exact values would the same reasoning have permitted (for P5: the set {0, ±π/2, π, ±π/4, …} the corpus's symmetry argument allows)? For anti-predictions (P2), the base-rate question is the prior probability of the null in the current literature, cited.

## 4. Verdicts (fixed now)

Per prediction:

- **FWD7-Pn-GO.** STANDING or WOUNDED, one defended value, and the geometry-free grammar reaches the falsification window with fewer than 1 in 10⁴ of its 3-atom values (or, for exact/anti-predictions, the base-rate statement shows the value is not the generic default). → Pre-registrable. Goes to the Zenodo list with its tier (PROVEN / CONJECTURE) declared.
- **FWD7-Pn-GENERIC.** Standing, but the geometry-free grammar reaches the window at ≥ 1 in 10⁴, or the value is what any model in its class would give (e.g. c_GW = c for every acoustic metric). → Not evidential for BCT even if confirmed. Not listed.
- **FWD7-Pn-DEAD.** A closed gate removes a load-bearing ingredient. → Withdrawn; the corpus text is flagged for a retraction note.
- **FWD7-Pn-UNFIXED.** The corpus does not support a single value (contradictory appendices, no threshold). → Not listed until the corpus is corrected; the correction needed is stated.

Gate-level:

- **SC-FWD7-1.** At least one GO. The programme has a live, pre-registrable, non-generic bet. The GO list is the programme's evidential currency and is filed to Zenodo verbatim, tiered.
- **SC-FWD7-2.** No GO. The programme currently has no forward prediction that is both standing and non-generic. This is the honest state and is filed as such; it says where new evidential weight could come from (a corrected derivation of a DEAD or UNFIXED item) and nothing else.

## 5. Guards

- The run does not repair a derivation. If P1's floor needs the δθ line fixed, the run says so and classifies UNFIXED; it does not pick a floor.
- The run does not add predictions. The CRIT/CRIT2 number (β_c = 0.615 on D4) is a lattice result, not a corpus prediction, and is out of scope here.
- Q-C is run with the FORK-verified no-geometry alphabet exactly; the run reports the alphabet's SHA-256 and the FORK commit it was taken from.
- A prediction is GO only if Q-A, Q-B and Q-C all pass. A borderline Q-C (within a factor of 3 of 10⁻⁴) is reported as GENERIC with the number shown, not rounded to GO.
- Forecast, disclosed now so the run can't be credited with it: my expectation is P1 UNFIXED (three floors), P2 WOUNDED→GENERIC or DEAD via THETA, P3 and P4 DEAD via Gate D4, P5 WOUNDED with a base rate of order 1 in 4–8 (few allowed exact phases), P6 UNFIXED, P7 GENERIC. Expected gate verdict SC-FWD7-2, with P5 the only candidate for GO. If the run finds otherwise, that disagreement is the result.

## 6. Verification

- Hash-before-read on this prompt; halt on mismatch.
- All arithmetic in mpmath 60 dps working, 40 reported. Grammar enumeration deterministic, no sampling.
- An independent sub-agent, not shown the run's working, re-derives the Q-A classification for each Pn from the gate deliverables alone and the Q-C counts from the alphabet alone; disagreements are reported, not reconciled silently.
- Deliverables under `audit/gates/FWD7/`: `gate_FWD7_RESULT.md`, `fwd7_table.csv` (one row per Pn: class, value, threshold, test, date, base-rate count, verdict), `fwd7_zenodo_list.md` (the GO list formatted for deposit, empty file if none), `gate_FWD7_run.py`. Patch bundle; commit SHA-1 and prompt SHA-256 recorded inside the result.

## 7. What this gate does not do

It does not evaluate whether BCT is true. It does not re-open any closed gate. It does not score retrodictions. It asks only: of the seven bets the corpus has placed on the future, which are still placed, at what value, and would a model with no geometry have placed the same bet?

## 8. Pre-registration record

- Prompt: `audit/gates/gate_FWD7_prompt.md`
- Digest: `audit/gates/PREREG_20261011_FWD7.sha256`
- Inputs read by the run: PRED2 result (§5 table), EDM / THETA / D4 / STAT / HERM / CA-FLAVOUR / N deliverables in the repo, the corpus appendices each Pn cites, `audit/gates/PRED/scripts/pred_step2_nullmodel.py`, `audit/gates/FORK/gate_FORK_RESULT.md` §8 (CN-FORK-02 only).
- Run thread: fresh; memory paused; past-chat search off.

