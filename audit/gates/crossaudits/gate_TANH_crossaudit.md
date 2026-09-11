# GATE TANH — CROSS-AUDIT

**Issued:** 11 September 2026, Gate Ψ2 execution thread.
**Standing:** not a re-run. Independent recomputation of TANH's load-bearing numbers, plus the
corrections TANH makes to this thread's own prior work.
**Method:** mpmath, 30–50 dps. Scripts not reviewed — see §6.

---

## 0 — PROVENANCE, CORRECTED

Gate TANH was commissioned as a **model comparison**: run on Claude Fable 5.1, cross-audited from
an Opus 5 session, to see whether the difference showed up where it should. **The model was not
switched. TANH ran on Opus 5.**

**The comparison did not happen, and the result is more useful than the one intended.** TANH is a
markedly better gate deliverable than this thread's own Ψ2 run — better search-space handling,
a real steelman, a precise contamination statement — and it was produced by the same model. **The
difference is entirely the prompt.**

That matters for how the programme allocates effort. Three rounds of errors in the Ψ2 thread were
paid to learn: audit the search space, name the traps by path, mandate the steelman, require
coverage before conclusions, revise clause by clause. The TANH prompt encodes all five. The next
gate prompt should encode whatever TANH costs to learn, and so on. **Prompt quality is the cheaper
lever, and on this evidence the larger one.**

A model comparison remains untested. If it is still wanted, it needs the same prompt run twice.

---

## 1 — VERIFIED INDEPENDENTLY

Recomputed here from r_oct = (√2−1)/2, r_tet = (√6−2)/4, R = ½, ξ = 1/√(8πα₀), without reference
to TANH's working:

| TANH claim | this session |
|---|---|
| g = 0.000369750648412782161 | ✓ |
| α₀ = 0.007408055727547908080 | ✓ |
| ratio α₀/g = 20.03527447307598548 | ✓ |
| discarded factor 4πR·tanh²(r_oct/ξ) = 0.04991196907952674072 | ✓ |
| steelman: factor at ξ = R is 0.965719 | ✓ 0.965718617 |
| near-identity tanh(√2−1) vs 1/√(2π) | ✓ 0.392044502 vs 0.398942280 |
| CN-TANH-08: 2α₀m_P = 1.80888423144×10¹⁷ GeV | ✓ against App AG.2's printed …×10¹¹ — twelve-digit mantissa identical, exponent off by exactly 10⁶ |

**CN-TANH-08 is a new finding and is independent of this gate's question.** It would stand if the
box were correct. It should be logged separately rather than folded into the TANH entry.

---

## 2 — TANH CORRECTS THIS THREAD. TWICE.

**(a) "Two orders of magnitude" is mine, and it is wrong.**

TANH §9 records that a matched line characterises the discrepancy as two orders of magnitude, notes
its own figure of 20.035 is 1.30 orders, and **declines to adopt or adjudicate it**. Correct on
both counts.

The line is `audit/gates/crossaudits/gate_LAM_crossaudit.md` line 24 — this session's own file. It
originates in Gate LAM's CN-LAM-03 ("it is two orders of magnitude") and **this session repeated it
without checking, inside the sentence acknowledging the miss.** log₁₀(20.035) = 1.3018.

**CN-TANH-11 [PROVEN, raised here].** The discrepancy is **1.30 orders of magnitude**, not two.
CN-LAM-03's wording is an overstatement; the LAM cross-audit propagated it while verifying the
underlying number correctly. Both should read 20.035× or 1.30 orders.

That a session which *saw* the wrong figure refused to take it is the cross-audit mechanism working
as designed.

**(b) The mount file formats — third diagnosis, and the first two were mine.**

| when | claim | status |
|---|---|---|
| Ψ2 v1, CN-Ψ2-27 | 35 of 49 mount PDFs do not extract locally; reachable only via indexed search | **wrong** |
| Ψ2 CORRECTION v2 §1 | they are ZIP archives; `unzip` opens them | **wrong for the two that matter** |
| TANH §1 | 33 are ZIPs, 14 are true PDFs, **2 are raw UTF-8 text** that `file` reports as `data` | **correct** |

Confirmed here: `Part1` and `Part2_compressed` are plain text beginning "The BCT Superfluid Lattice
Model / Complete Derivation…" and "BCT Appendix CU / Phase 21 Review…". Neither `pdftotext`,
`pymupdf` nor `unzip` will touch them.

**They contain App J, App K, App AG, App AN, App AT and App AY** — the entire subject matter of
Gate TANH, and most of the mass sector. A ZIP heuristic skips them silently.

**CN-TANH-12 [PROVEN, raised here].** The corrected instruction for all future gates: **type every
mount file with `file` and handle each by its actual type.** Do not infer format from extension,
and do not infer "unreadable" from extractor failure. Two wrong diagnoses were issued from this
thread before the right one, and the second was issued with confidence.

---

## 3 — THE STEELMAN IS THE BEST WORK IN THE DELIVERABLE

TANH §3 constructs the strongest available case *for* the corpus — a convention (ξ = R) under which
the boxed value is right to 3.4%, resting on a genuine near-identity, used at six cited sites — and
only then resolves it against the corpus, using App F's own explicit retirement of that convention
and App J's own use of ξ_GP in §2.2 and §3.1.

It also supplies §3.6, which closes the question independently of the convention: two factors must
vanish, not one, and granting tanh → 1 leaves g = 2πα₀, which is 6.283× *above* α₀. No single limit
does both.

This thread's Ψ2 run attempted nothing equivalent. §2 of the TANH prompt mandated it; that is the
whole difference.

---

## 4 — EFFECT ON THIS THREAD'S LEDGER

- **CN-Ψ2-26 is refined, not overturned.** It recorded a real collision in the symbol J and in the
  "Josephson coupling = α₀" claim. CN-TANH-04 locates it precisely: α₀ is correct as σ_s/J
  (verified by reproducing κ₀ = 3.390462) and g is correct as the §3.1 object; the box equates two
  distinct quantities. **Conflation, not error** — a sharper reading than either CN-Ψ2-26 or the
  LAM cross-audit reached.
- **CN-Ψ2-29** (the notice this thread owed to CN-LAM-03) should be logged with the corrected
  magnitude per CN-TANH-11.
- **CN-Ψ2-27 is retracted and replaced by CN-TANH-12.**

---

## 5 — NOT DISPUTED

The two-tally separation of §6, and its zero-published-predictions result stated first, is the
right shape and correctly resists overstating itself. §9's contamination statement — exact
ordering, files not opened, `audit/` excluded thereafter, and the seen-but-not-adopted disclosure
— is the most precise in the programme to date. §10's list of what was not established, including
the unexplained use of r_oct as the tanh argument for an amplitude at r = R, is honest and flags a
real open question.

---

## 6 — SECOND PASS: THE SCRIPTS, REVIEWED

All five artefacts received and executed. **The four Python scripts run and reproduce every number
in the deliverable**, including the two this cross-audit could not previously check:

| previously unverified | now |
|---|---|
| CN-TANH-06: c·t² = 2.73431e-6, short by 7314× | ✓ reproduced |
| CN-TANH-07: implied C_A(16) = 2.13178e9, a₁₆ = 1.62617e-47 | ✓ reproduced |

**A self-check the deliverable does not claim but should.** `step3` run with t = α₀ gives
c·t² = 0.00109759, short by **18.22×** — which is what App K reports as "a factor of 20 too weak."
The DOS slope c = 20 is therefore not assumed; it is validated by reproducing App K's own printed
conclusion. That strengthens CN-TANH-06 and should be stated in it.

**Three defects in the artefacts. None changes a verdict.**

**CN-TANH-13 [PROVEN]. `gate_TANH_step3_downstream.py` §4 carries a hardcoded narration line that
contradicts its own computed output.** The script computes `2·g·m_P = 9.0285e+15 GeV`, then prints
the literal string *"recomputed 9.03e9 GeV is still ~7e7 x the observed 125 GeV."* Both figures are
wrong by ~10⁶: the value is 9.0285e15 GeV and the ratio to 125 GeV is **7.223e13**. The
**deliverable §5.1 row 6 is correct** (9.0285e15, 7.2e13); only the script's prose is wrong. But the
script is the archived artefact, so anyone re-running it reads a wrong line two lines under the
right number. Fix the string or delete it.

**CN-TANH-14 [PROVEN]. `gate_TANH_step2_dims.py` mislabels a print.** The line ending
`" = 2 pi alpha0 ="` prints `6.2831853…`, which is 2π, not 2πα₀ = 0.046546. The computed value
immediately before it is correct. Cosmetic, but it is the kind of mislabelling this gate exists to
catch in the corpus.

**CN-TANH-15 [PROVEN, and this one matters]. `gate_TANH_downstream_scan.sh` as committed cannot
reproduce §5.** Its `grep -rlE "$PAT" BCT-Programme-… --include='*.tex' --include='*.md'
--include='*.py' unz mounttxt` applies the `--include` filters to **every** path, `unz` and
`mounttxt` included. Those directories hold `.txt` page layers, which the filter excludes.
Confirmed by construction here: an identical file under a `.txt` extension is matched without the
filters and missed with them.

As written, the scan therefore searched the **repo only**. The deliverable's §5 results
nonetheless cite App J §3.2, App K §1.2/§5/§6, App AG.2, App AN.2 and App AT.3 — **all of which
live only in the mount plain-text volumes**. So the actual search did reach the mount and the
archived script is an **incomplete record of it**, not a wrong result.

The distinction matters for the archive rather than the verdict: **§5 is not reproducible from the
committed artefacts.** Either commit the additional searches or fix the filter, and note that the
"63 files matched" figure cannot be checked until then.

## 7 — WHAT THIS CROSS-AUDIT STILL DID NOT CHECK

- **The §5 downstream trace was not re-run** — and per CN-TANH-15 it cannot be, from what is
  committed. TANH tiers its unaffected list ASSERTED and names what it did not re-derive
  (Letter 57, App AB, App D). That tiering is correct and the gap is real: **if any "independent
  route" in §5.2 in fact routes through §3.1, the zero in §6.1 moves.**
- **CN-TANH-07's back-out carries an unflagged assumption.** C_A(16) is inferred from App K's
  printed a₁₆ = 1.0962e-26 by dividing out α₀¹⁶ — which assumes App K computed that value with
  t = α₀. Reasonable, and almost certainly right given App K cites App J's box, but it is an
  assumption and CN-TANH-07 should say so.
- **CN-TANH-09's √2 convention** remains open; this session adds nothing to it.
- **No judgement is offered** on SC-TANH-3 versus SC-TANH-1. TANH states the arithmetic and tallies
  are identical either way, which is correct.

---

*Cross-audit issued 11 September 2026, second pass same day after the scripts arrived. Findings: model comparison did not occur and the gain was
prompt-only; two corrections accepted against this thread (CN-TANH-11, CN-TANH-12); CN-Ψ2-26
refined by CN-TANH-04; CN-Ψ2-27 retracted. Scripts reviewed: all four Python files reproduce; three artefact defects raised (CN-TANH-13/14/15), of which CN-TANH-15 leaves §5 non-reproducible from what is committed.*
