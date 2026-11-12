# Gate DL-STIFF — three-run comparison and ledger entry

**Recorded:** 12 November 2026, evening (Australia/Melbourne).
**Operator:** Michel Robert Cabrié. Committing this file is the operator's ruling (as for ALTER-R).
**Prepared with:** Claude Opus 5.5, in the REP3 thread, after REP3's result had been committed and
pushed (`a2d47c9`). That thread was blind while it ran REP3 and is **not blind now**: for this record
it read the original result, the post-gate note, REP2's result, `audit/NEXT.md`, and three precedent
files (`ALTER_R/gate_ALTER_R_COMPARISON.md`, `SPECTRUM/gate_SPECTRUM_LEDGER_ENTRY.md`,
`TWIST/gate_TWIST_ADDENDUM_unblinded.md`). It did not run the gate again. All three result files
are left exactly as run; corrections are recorded here (§6).

---

## 1. The three runs

| | Original | REP2 (blind) | REP3 (blind) |
|---|---|---|---|
| Model | Claude Fable 5.1, switched to Claude Opus 5 before any kill test | Claude Opus 5.5 | Claude Opus 5.5 |
| Thread | fresh, 12 Nov | fresh, from 18:09 | fresh, from 19:04 |
| Sources | clone at `9993a23` (parent `9114b6e` checked) | `9993a23` alone, depth 1 | `9993a23` alone, depth 1 |
| Card / record / desk-check digests | match | match | match |
| Eleven §4.1 hashes verified before reading | yes | yes | yes |
| Result commit | `d67f5ca` (+ post-gate note `35d5898`) | `4a1a83d` | `a2d47c9` |
| Verdict | **SC-DLS-2**, CONJECTURE | **SC-DLS-2**, CONJECTURE | **SC-DLS-2**, CONJECTURE |

## 2. Outcome

**MATCH.** Same verdict code, same load-bearing argument, and identical values for every number two
or more runs report. No run contradicts another on any finding. The differences (§4) are a counting
convention, how one unpinned pointer was coded, which extra inputs R4 was charged with, and which
routes each run found for the open R6 slot. None moves the verdict.

## 3. What all three runs agree on

- **The load-bearing reason.** With the medium neutral under `a_e`, the pinned action splits into
  `S_GP[Ψ] + S_W[a]`, the partition function factorises, and the medium cannot set or renormalise β
  (original CN-DLS-01; REP2 verdict and CN-DLS-03; REP3 verdict and CN-DLS-05).
- **The trade.** The only coupling-free way to tie the medium to `a_e` is a charge `q ≠ 0`, which is
  the Meissner mass (original CN-DLS-02; REP2 CN-DLS-01; REP3 CN-DLS-02). REP2 and REP3 add that even
  then the tree-level term is a link mass and contributes no plaquette (β) term.
- **R1–R5** closed in every run, for the same reasons.
- **R4's code.** All three code R4 *closed*, not SC-DLS-4, because the sphere-surface → window-link
  step fails on its own; all three record SC-DLS-4 as the charitable reading and note that card §5
  makes the parameter count identical.
- **The near-miss.** Each run found, without seeing the others, that Gate ICE's
  `E_J/E_C = 2n̄²(ξ/a)²` equals the candidate 10.74201848 at `n̄ = 1` (original R6b, REP2 R6a, REP3
  under R3), and each rejected it for the same two reasons: it is a ratio inside the superfluid's own
  sector, with `a_e` in neither factor, and `n̄ = 1` is asserted.
- **Shared numbers** (`dls_comparison_checks_output.txt` §1; each run's own outputs agree):

| quantity | value | reported by |
|---|---|---|
| β_geom = 1/(4πα₀) = 1/(4 r_oct r_tet) | 10.74201848 | all three |
| β_geom / β_c: Z4 1.0111, D4 0.6150, D4 1.2300 | 10.62409107, 17.46669672, 8.73334836 | all three |
| App J g = α₀·4πR·tanh²(r_oct/ξ) | 0.0003697506484 | all three |
| α₀ / g | 20.03527447 | all three |
| R5 ln(Λ/m) for β_geom: card coefficient / Dirac / complex scalar | 1272.233675 / 636.1168374 / 2544.467349 | original (card), REP2 (Dirac, scalar), REP3 (all) |
| E_J/E_C at n̄ = 2 | 42.96807393 | original, REP3 |

## 4. Differences, and the ruling on each

**D1 — Q5 total.** Original: **3** (the α identification scored 0, because with β free, fitting α
*is* setting β). REP2 and REP3: **4** in the card's form, each footnoting 3 as the merged count.
*Ruling:* the DL theory has **three free inputs** — the added link field, β, and the charge carrier.
The α identification is the act of choosing β, not a further number. In the card's Q5 form this is
written 4. Both are correct under their stated conventions; the ledger quotes 3 (as `NEXT.md` already
does: "≥ 3 inputs").

**D2 — App E.1 §3.3 (`J = 1/(4πα₀)`).** Original: "not evaluable", SC-DLS-5 for that sub-route only,
with a recommended follow-up card. REP2 and REP3: not read either, but argued that R3's kill test
closes it whatever value J has, because no term lets `a_e` see J. The post-gate note (PGN-01) read the
section afterwards and found the value *assumed* ("Taking J = 1/g₀²"). *Ruling:* closed as an
assertion, as already recorded. REP2 and REP3 show the closure never depended on reading App E.1, so
no follow-up card is owed for the β question (consistent with PGN §3).

**D3 — R4's inputs beyond Q and d.** All three found more than App J's two, and named different extras:
original, the unit identification `ℓ_P = a = 1` (σ_s/J has dimension 1/length); REP2, ε₀ and J (one
equation, four inputs; Gaussian units break the match); REP3, ε₀ (Gaussian units give 4πα₀).
*Ruling:* App J's `σ_s = α₀` uses **Q = 1, d = √(r_tet r_oct), ε₀ = 1 (rationalised units), J = J₀ = 1
and ℓ_P = a = 1**. Gate BC's "two-input fit" should be cited with this list.

**D4 — the open R6 slot.** Eight distinct routes were found across the three runs; every one closed.

| R6 route | Original | REP2 | REP3 |
|---|---|---|---|
| ICE's E_J/E_C | R6b | R6a | (under R3) |
| App E.1's J value | R6d | recorded; closed by R3's test | R6c |
| Particle–vortex duality (2-form) | — | R6b | R6a |
| Network geometry / plaquette matching | — | R6c | R6d |
| Speed matching (fixes β_t/β_s only) | R6c | — | — |
| "One-number" form c/(r_oct r_tet) (an observation) | R6a | — | — |
| STIFF's e*/ε₀ | — | R6d | — |
| Charge quantisation | — | — | R6b |

**D5 — duality normalisation.** REP2 writes the 2-form coefficient as 1/(8π²K); REP3 writes
β_dual = 1/(4π²K) with S = (β/2)ΣH². Same action (checks §3). No ruling needed.

**D6 — the card's R5 coefficient.** The card writes `(1/12π²) Σq² ln(Λ/m)`. REP2 notes this is the
Dirac coefficient written for ln(Λ²/m²); read literally it is half the Dirac value (checks §2). The
original used the card's form, REP3 tabulated all three. The card is pre-registered and is not edited;
the ambiguity is recorded here and moves nothing (every reading needs a tuned hierarchy of at least
10²⁷⁶).

## 5. Findings made by only one run

| finding | run | checked here | status |
|---|---|---|---|
| Any geometric β has the form c/(r_oct r_tet); β_geom ⇔ c = 1/4 exactly; β > β_c needs only c > 0.02353 (Z4), 0.01431 (D4 card), 0.02863 (D4 K–N) | original CN-DLS-03/04 | reproduced (checks §5) | stands |
| A derived β would have predicted 1/α = 134.9881854, the 1.5 % gap FWD/STAT closed as a selected map | original CN-DLS-10 | reproduced | stands |
| Speed matching fixes only the anisotropy β_t/β_s | original CN-DLS-07 | not re-derived | stands as recorded |
| **Units:** 2ξ²/a² = 10.742 only with a = sphere diameter; 5.371009241 (Gate DL cubic edge), 28.64538262 (oct–tet link), 28.15205249 (per-void cell) | REP2 CN-DLS-08 | **reproduced** (checks §4) | **adopted as ledger convention** (§7) |
| The classical lattice coupling of the rotor model is √(E_J/E_C) = 3.277501866, not E_J/E_C | REP2 R6a | reproduced | stands |
| On any complex the Wilson action is homogeneous of degree 1 in β; geometry fixes only relative plaquette weights κ_p | REP2 R6c (REP3 CN-DLS-12 qualitatively) | — | two runs agree |
| STIFF's charitable double layer leaves e*/ε₀ free | REP2 R6d | not re-derived | stands as recorded |
| MINIMAL §1.2's amplitude mode has m = Ψ₀/ξ; §1.4 prints 2/ξ (needs Ψ₀ = 2) | REP2 CN-DLS-10 | **reproduced** (checks §6) | outside the gate; add to MINIMAL §4's list of undeclared conventions. REP3's analyst noticed it during the run and did not record it |
| App J ll.143–145 ("no new free parameter") contradicted by ll.172–173, 385–386 | REP2 CN-DLS-11 | — | stands |
| STIFF's P = 0 and bias-linear response re-derived with an independent GP solver | REP3 CN-DLS-04 | re-run, identical | stands |
| Charge quantisation fixes e·g_m, not e | REP3 R6b | — | stands |
| Card cites "App J §1.3–1.4, lines 147–168"; no §J.1.4 exists and the input caveat is at ll.172–173 | REP3 CN-DLS-13 | — | stands |

## 6. Errata (the result files are left as run; read them with these)

- **E1 — REP3, R3 row and CN-DLS-05; original R6b and CN-DLS-06.** "E_J/E_C at n̄ = 1 equals β_geom
  (to 30 digits / identically)" holds only with `a` = the sphere diameter, MINIMAL's unit. With the
  void-network spacing the same expression is 28.645 (REP2 CN-DLS-08). The closure of the route is
  unaffected; it now fails a third way.
- **E2 — any statement of the candidate as "2ξ²/a²" without naming `a`.** Read it as
  `1/(4 r_oct r_tet)`.
- **E3 — original CN-DLS-09** ("the one place a future gate could still disturb this verdict"):
  superseded by PGN-01 and D2 above.

## 7. Independent verification of the deliverables

Done in the preparing thread, at `main` = `a2d47c9`, Python 3.13.18, sympy 1.14.0, mpmath 1.3.0,
numpy 2.5.3, every script run with `python3 -I` from outside the tree (transcript:
`dls_comparison_rerun_transcript.txt`):

- All eight result scripts of the three runs (original: `dls_q1_factorisation.py`,
  `dls_q1_r2_r4.py`, `dls_q1_r3_r5_r6.py`, `dls_q3_q5.py`, `e1_33_check.py`; REP2:
  `dls_rep2_routes.py`; REP3: `rep3_routes.py`, `rep3_r2_gp_throat.py`) reproduce their committed
  outputs **byte for byte**.
- REP2's `SHA256SUMS`: all seven lines OK.
- REP3's patch was checked to apply cleanly on `9993a23` and to add nothing outside `REP3/`.
- The cross-run claims in §3–§5 are recomputed in `dls_comparison_checks.py`.

**Not verified:** each run's reading of the pinned sources. The agreement in §3 is three readings
agreeing, not a check of the reading.

## 8. What the replication covers

Same card, same eleven pinned sources, three fresh threads; the two replications fetched the
pre-registration commit alone and saw nothing of the original or of each other. This replicates the
reading of the card and of the pinned action, the kill-test arithmetic, and the verdict. It is an
analytic gate: there is no second method to replicate.

**Independence is weaker than "three runs" suggests.** REP2 and REP3 were the same model (Opus 5.5)
in the same harness, about an hour apart. What they share and the original lacks — Q5 = 4, the
duality and network-matching routes, ε₀ as R4's third input — may be one habit seen twice, so it is
counted here as one confirmation, not two. The cross-model check is the original (Fable 5.1 → Opus 5)
against the replications, and it covers the verdict and every load-bearing notice (§3).
For future blind replications: where two are run, use different models.

## 9. Tier movements

| # | Statement | Tier | Basis |
|---|---|---|---|
| 1 | Verdict **SC-DLS-2**: in option B with the pinned action, β is a free input of the DL theory | **Replicated** (two blind runs). **Same-session cap lifted.** | `NEXT.md` named the blind replication as the binding requirement; met twice, cross-model on the verdict |
| 2 | Neutral medium ⇒ Z factorises ⇒ β_eff = β_bare | **PROVEN** (identity of the pinned option-B action), replicated | all three runs |
| 3 | The only coupling-free link between medium and a_e is q ≠ 0, which is the Meissner mass | **PROVEN**, replicated | all three runs |
| 4 | ICE's E_J/E_C = 1/(4 r_oct r_tet) at n̄ = 1 and a = d_nn; not a route to β | **Replicated** (found and closed independently three times); unit caveat E1 | §3, §6 |
| 5 | The DL theory has three free inputs (four in the card's Q5 form) | **Recorded**; convention fixed by D1 | §4 |
| 6 | Findings in §5 made by one run | **Unchanged**: each keeps the tier its run gave it; the arithmetic ones are reproduced | §5 |
| 7 | β > β_c, i.e. a massless photon for the DL construction | **No movement. OPEN** — Gate DL-BETA | none of the three runs addresses it |
| 8 | BCT void geometry | **No movement** | card §3 |

## 10. Standing sentences

- Quote the candidate as **β_geom = 1/(4πα₀) = 1/(4 r_oct r_tet) = 10.74201848**, a value of 1/e².
  "2ξ²/a²" is that number only when `a` is the sphere diameter.
- When DL-BETA's β_c is set against this candidate, convert through DL-BETA's own β ↔ 1/e² matching
  for the void network; do not compare 10.742 with β_c directly.
- The analyst's §9 forecast (SC-DLS-2 at 70 %) was right. All three runs scored it identically
  (Brier 0.125, log score ln 0.70).
- With the blind replication no longer pending, the DL-STIFF results may go into the claude.ai
  Project (standing rule on replications).

## 11. Plain-language summary

Three separate runs of the same test, two of them unable to see any earlier answer, all reached the
same conclusion for the same reason: the coupling strength of the proposed new light-carrying field is
a free choice, because the medium is deliberately uncharged and so never touches that field. All three
found the same tempting near-miss in the old results and rejected it the same way, and every number
they share is identical. The re-runs also turned up one useful correction: the "10.742" only comes out
if lengths are measured in sphere diameters, so the number should be quoted in a form that doesn't
depend on the unit. The two replications came from the same model, so they count for a bit less than
two fully independent checks. Whether the new field actually carries light freely is the next test's
job (DL-BETA).

---

| file | SHA-256 |
|---|---|
| `dls_comparison_checks.py` | `0d7bf47e7aab85083502430c1eeebf3fe8cb0954ab2b81cb5556d830723903d4` |
| `dls_comparison_checks_output.txt` | `8ba157a2de8d280948f302c822428d5c2df3bdf79e93d70bf089f26dc382edd8` |
| `dls_comparison_rerun_transcript.txt` | `aa678333e8620642f94cc981469311739569647faa10d06ec506d016287c1a8f` |
