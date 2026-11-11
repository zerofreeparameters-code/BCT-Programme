# NEXT — what is queued, running, and closed

Last updated 12 November 2026 (full reconciliation against every result directory under
`audit/gates/` at commit `36edda3`; Gate SONO closed). **Update this file at the close of every
session.** It exists because sessions have independently invented their own gate order, and one
spent a turn treating a committed prompt as a mystery file. The previous version (14 September
2026, Gate RATIO closed) is in git history; its queue is reconciled in §"Queue reconciliation"
below.

## How this version was built (12 Nov 2026)

- **Source of record for "closed":** a result file under `audit/gates/<NAME>/` in the tree at
  `36edda3`. Every row in the Closed table was read from that file — its own run date and its
  own verdict line — not from memory, chat, or the Project.
- **"Pre-registered, no result directory":** a `gate_<NAME>_prompt.md` in `audit/gates/` with a
  `PREREG_*.sha256` line and no `<NAME>/` directory. Nine of these exist.
- **"Run, result not in the tree":** gates the Cold Ledger or the claude.ai Project record as run,
  whose deliverable never reached this repository. Listed so the debt is visible; their verdicts
  are quoted from where they live and are not the tree's claims.
- Dates are run dates as printed in the result (AEDT/AEST where the result says so).

## The goal, as currently stated

Unification is the long aim; the working target was any two of QM, GR, EM. Where that stands
after the gates below: GR is closed along every audited route (N, F/Fb, T, IG/BZ, QP, AM, R2;
ledger); the photon is closed along every audited route and by field content (G′/PH, LINK, XI,
PSI2, ICE, STIFF, PROMOTE, PV, QED, QED-DERIV; ledger); QM is inherited, not derived (MAD, PILOT,
SINGLET). The numeric layer scores as fits (PRED, PRED2, MIX, FWD/STAT; FORK and FWD7 run but not
in the tree). What survives is the void geometry (r_oct, r_tet, α₀ as a number, ξ/a = 2.3175,
the percolating network) plus one live CONJECTURE for the sphere interiors (BUBBLE_BELLS), which
BB-ALPHA is queued to anchor. This paragraph is a reading, not a result; any gate may move it.

## Closed — result committed under `audit/gates/` (34 directories at `36edda3`)

| gate | run | verdict (from the result file) | deliverable |
|---|---|---|---|
| PSI2 | 11 Sep | Closes: Ψ₂ supplies no second independent A₁g Goldstone on either interior — the corpus contains no Josephson coupling at all (zero `cos(θᵢ−θⱼ)` in 108 `.tex`). SC-Ψ2-5 (two interiors not adjudicable from the corpus) fires at Step 0; SC-Ψ2-3 does not fire as worded. CN-Ψ2-01…21. | `gates/PSI2/` (RESULT, CORRECTION v2, ADDENDA v2.1/v2.2 — read in that order) |
| C1 | 12 Sep | SC-C1-3: the interior healing length ξ₂ is not determined by the corpus; halt and report. SC-C1-4 not at Step 0; SC-C1-5 in part. | `gates/C1/` |
| RANK | 13 Sep | SC-RANK-3: the corpus does not determine the field content; halt. Scalar by written dynamics, vector by its claims about light and gravity. | `gates/RANK/` |
| MP | 13 Sep | SC-MP-1 (qualified: HF4's m_P = M_R/α₀² is an identity on GG2's M_R = m_P·α₀²) + SC-MP-3 (inputs, M_R, G_BCT inconsistent across documents). a = ℓ_P assumed and declared. | `gates/MP/` |
| PRED | 13 Sep | SC-PRED-1: observed matches within chance expectation; 39/40 closed forms reproduce; "92" not reconstructible (CN-PRED-02). | `gates/PRED/` |
| INT | 14 Sep | SC-INT-3: exactly two interiors (A: Ψ₂ ∈ ℂ, S¹, App I/J; B: Ψ₂ ∈ ℂ², S², App JH), the corpus does not adjudicate; halt. SC-INT-4 **excluded** (CN-INT-02) — the 14 Sep table's "SC-INT-4" was wrong. | `gates/INT/` (result now present; `README_MISSING.md` is stale — delete) |
| TANH | 14 Sep | SC-TANH-3 (local SC-TANH-1 reading): App J §3.1's computed g = 0.00036975 (overlap Josephson coupling) and its boxed g ≈ α₀ = 0.00741 (surface/boundary coupling) are two correct numbers for two different objects conflated under one name (ratio 20.04); numeric-prediction tally zero. | `gates/TANH/` (result now present; `README_MISSING.md` is stale — delete) |
| LINK | 14 Sep | SC-LINK-2: the only canonical variable is site-valued; link reformulation available but costs the phonon identification; SC-LINK-4 fires at corpus level; SC-LINK-5 does not. | `gates/LINK/` |
| MAD | 14 Sep | SC-MAD-1: every adjudicable quantum claim is bin A, C or D; bin B empty. | `gates/MAD/` (deliverable now present; 14 Sep "MISSING" cleared) |
| PRED2 | 14 Sep | SC-PRED-1 met only by m_p/m_e = 6π⁵ (+15.6 net bits), which the corpus itself disclaims and a blind control rediscovers; no derived prediction ≥ 10 bits. | `gates/PRED2/` (block below) |
| RATIO | 14 Sep | SC-RATIO-2: every observable of the minimal theory depends on r_oct, r_tet only via their product; r_oct/r_tet = 1.8430 is a fixed FCC constant; no absolute scale. | `gates/RATIO/` (block below) |
| XI | 14 Sep | SC-XI-3: ξᵢ is notation (Group A — appearances with written dynamics — empty). | `gates/XI/` |
| YM2 | 14 Sep | SC-YM2-4 primary: the public DOI 10.5281/zenodo.21781545 ("Complete Proof") overstates the current appendix, which disclaims a Clay-sense proof. SC-YM2-2 secondary: fixed-spacing gap essentially proven by the standard route; continuum limit open. | `gates/YM2/` |
| JHF | 15 Sep | SC-JHF-1: App JH is not a complete, stabilised S² field theory (stabiliser cited only; Derrick; EOM one-component). | `gates/JHF/` |
| KAUDIT | 15 Sep | SC-KAUD-1: App K Theorems T1/T2/T3 fail on the correct c/a = √2 FCC lattice; m_e not protected. | `gates/KAUDIT/` |
| PROMOTE | 15 Sep | SC-PROMOTE-1 (primary), SC-PROMOTE-5 (fallback): geometry selects no promotion of M beyond S¹. | `gates/PROMOTE/` |
| CA-FLAVOUR | 16 Sep | SC-CAFLAV-1: at c/a = √2 any T_d-invariant M is block-scalar, [M_u, M_d] = 0, no physical mixing without a new T_d-breaking input. | `gates/CA-FLAVOUR/` |
| HERM | 16 Sep | SC-HERM-1: Hermiticity needs new fermion fields; θ_QCD = 0 stays imported. | `gates/HERM/` |
| PV | 16 Sep | SC-PV-2, SC-PV-4, SC-PV-1: vector-charge fracton route closed on three grounds. | `gates/PV/` (new card `0fb236e3…`; the 14 Sep "parked" PV is superseded) |
| THETA | 16 Sep | SC-THETA-1: θ_QCD = 0 is imported/asserted; CONJECTURE. | `gates/THETA/` (+ `strong_cp_correction_inventory.md`) |
| ALTER | 1 Oct | SC-ALTER-2 (kill, absent): no sublattice-alternating decoration in the corpus. REOPEN trigger recorded. | `gates/ALTER/` |
| ALTER_R | 1 Oct | Blinded replication of ALTER: SC-R-3 completed, SC-ALTER-2 confirmed; 69/69 assertions. | `gates/ALTER_R/` |
| SPECTRUM | 7 Oct | Two fresh-thread runs agreeing to 40 digits. S1–S5 figures closed by replication; SC-SPEC-1 recorded as run, tolerance-decided, not promoted; "whole vector-like generations complete induced light" OPEN → SPECTRUM2; the N_V = 3 at 9.089 × 10¹² GeV proposal FALSIFIED. | `gates/SPECTRUM/` holds the **ledger entry only**; both run results are Project docs (debt, below) |
| SPECTRUM2 | 8 Oct | SC-SPEC2-1 (requirement map): G+T and G+Q menus survive C0–C3 (20 rows each); G+L none. A surviving row is a requirement, not evidence. | `gates/SPECTRUM2/` |
| CRIT | 8 Oct | β_c (compact U(1), Wilson action, D4, L = 8) = 0.610 ± 0.005, CONJECTURE; SC-CRIT-2: the Bennett–Nielsen–Froggatt route to 1/α(0), moved to D4, misses by ≈ +11.5 — kill. | `gates/CRIT/` |
| CRIT2 | 8 Oct | SC-CRIT2-1 (replicated): β_∞ = 0.6150 ± 0.00125 (card convention), β_KN = 1.2300 ± 0.0025. | `gates/CRIT2/` |
| PILOT | 9 Oct | SC-PILOT-3 (IMPORT): no-added-structure branch 2b on the GP law, 2a on the wave law, 2c by counting. | `gates/PILOT/` |
| PLASMOID | 24 Oct | SC-PLASMOID-3 HALT: no qualifying dataset obtainable; pilot results exploratory only. SC-PLASMOID-5 open (Stenhoff 1999 unread). | `gates/PLASMOID/` |
| SINGLET | 25 Oct | SC-SINGLET-2 (IMPORT): the singlet curve needs the signed-measure ingredients added on the written S¹ phase. | `gates/SINGLET/` |
| TWIST | 8 Nov (+ blind replication 9 Nov) | SC-TWIST-1, kill at Q1: no Maxwell-type term for the twist field (c_F ≤ 0), a slaved to the texture; Q2–Q4 fail; 0/4 shell properties derived. | `gates/TWIST/` (+ `replication_2026-11-09/`, unblinded addendum) |
| BUBBLE_BELLS | 10 Nov | SC-BB-2: construction holds, with repairs (α_∞ = 1.64 ± 0.03, c_eff = 0.78 c_s, κ_ℓ ladder). Same-session, non-blind, **CONJECTURE cap**. | `gates/BUBBLE_BELLS/` |
| BULK | 11 Nov | SC-BULK-1, all four variants: no K_BCT is a G-free output of the equation of state; every chain ends in ρ_Planck, m_P or a = ℓ_P. CN-BULK-01…07. | `gates/BULK/` |
| SONO | 12 Nov | SC-SONO-1: Letter 110's #154/#155 reproduce arithmetically, but both comparison values are the letter's own (200 nm = water's absorption edge; no SBSL peak at 350–370 nm; 380 nm not a biophoton band). Net −6.0 / −9.5 bits under PRED2. CN-SONO-01…13. | `gates/SONO/` |
| LAM, LAMBDA | — | run elsewhere; cross-audited from the PSI2 thread. | `gates/crossaudits/` |

Not in this table because it is not a gate result: `gates/PT/` holds only the PT card and its
PREREG line (result is Project-side — debt, below).

## Pre-registered in the tree, no result directory (9)

| gate | card committed | state |
|---|---|---|
| **BBALPHA** | 10 Nov 2026 (`95172ce8…`, `PREREG_20261110_BBALPHA`) | **NOT RUN. Next to run** — fresh thread, memory and past-chats off, commit-pinned raw URL. Anchors BUBBLE_BELLS' α_∞ = 1.64 ± 0.03 by literature (Sangani–Acrivos 1983, Cheng–Torquato 1997) + an independent method. |
| VOID | 17 Oct 2026 (`e04f69db…`) | Pre-registered, unrun (do the void-volume / void-eigenvalue formulas survive the true concave void geometry?). |
| LATT | 17 Oct 2026 (`1dccde5b…`) | **Run** per the run thread (17 Oct; ~11.7 h; verdict SC-LATT-1 for the β_∞ table, transition order undetermined, CN-LATT-01/02) — result + patch never applied. Debt. |
| FORK | 11 Oct 2026 (`c21bc5d6…`) | **Run** 11 Oct, SC-FORK-2 (base rate; CN-FORK-02: the 14 non-geometric atoms alone reach 48/48 at 0.1 %) — result patch 0001 + ledger patch 0002 never applied. Debt. |
| FWD7 | 11 Oct 2026 (`d169a13e…`) | **Run** 11 Oct, SC-FWD7-2 (no GO; P7 DEAD by CN-RANK-06; Zenodo pre-registration list empty) — patches 0001/0002 never applied. Debt. |
| DYN | 10 Oct 2026 (`973815e0…`) | Analogue-gravity dynamics census. Run requested 3 Nov; **no result located** anywhere. Run or withdraw. |
| LOG | 7 Oct 2026 | **Run** 7 Oct (SC-LOG-3; superseded by SPECTRUM/SPECTRUM2) — result is a Project doc only. Debt. |
| KL | 15 Sep 2026 (`9ae6e37b…`) | **Run and closed** 15 Sep per the ledger (SC-KL-2; SC-KL-3 provably excluded) — "committed audit/gates/KL/ (patch to Michel)" was never applied. Debt. |
| DL | 15 Sep 2026 (`3c05f64a…`) | Hypothetical-construction card (double-layer gauge field on the FCC void network). **No run located.** Its question was overtaken by ICE/STIFF (ledger); run or withdraw. |

## Run, result not in the tree (deliverable debt)

Verdicts here are quoted from the Project docs or the Cold Ledger, not from this repository.

- **PT** — 19 Sep, SC-PT-1 (Round Periodic Table structurally void on M = S¹; CN-PT-01) + same-day
  red-team addendum. Project docs `claude/gate_PT_RESULT.md`, `claude/gate_PT_RESULT_REDTEAM.md`.
  `gates/PT/` has the card only.
- **D4** — 19 Sep. Project docs `claude/gate_D4_RESULT.md`, `claude/gate_D4_prompt.md`; never
  committed (card not in the tree either).
- **LOG** — 7 Oct. `claude/gate_LOG_RESULT.md`, `claude/gate_LOG_run.py`.
- **SPECTRUM runs 1 and 2** — 7 Oct. `claude/gate_SPECTRUM_RESULT.md`,
  `claude/gate_SPECTRUM_RESULT_run2.md` (+ scripts). Only the ledger entry is in the tree.
- **FORK, FWD7** — 11 Oct; **LATT** — 17 Oct; **KL** — 15 Sep: patches delivered, never applied
  (see table above).
- **FORK2** — card written and pre-registered 10 Nov as a patch (`PREREG_20261110_FORK2`); never
  applied, so **not in the tree and not pre-registered in any sense this file recognises**.
- **PQCD** — card exists only as a Project draft (`claude/gate_PQCD_prompt.md`); not committed.
- **DIPOLE** — card requested 9 Oct; no card in the tree.
- Older chat-side gates (FWD, GEO, STAT, KND, OP, R2, P, J, MIX, ICE, STIFF, EDM, QED, QED-DERIV,
  BC, WHY√2, LH7, R8, SYM, AM, QP, N, F/Fb, T, IG, BZ, SCR, PH, G′, U″) have no directory here;
  their record is the Cold Ledger. `audit/desk/routeC_reconciliation.md` (+ ADDENDUM) is the one
  piece of that work committed.

## Queued, in order

1. **Run Gate BB-ALPHA** (pre-registered 10 Nov; card and run prompt as above). The one favourable
   CONJECTURE on the board depends on it.
2. **Clear the deliverable debt in one sitting** — apply and push what already exists: FORK 0001 +
   0002, FWD7 0001 + 0002, LATT, KL, the FORK2 card; commit PT (result + red-team), D4 (card +
   result), LOG, SPECTRUM run 1/run 2 from the Project docs; delete `INT/README_MISSING.md` and
   `TANH/README_MISSING.md`. Each item is a result that currently does not exist as far as this
   tree is concerned.
3. **Gate VOID** (pre-registered 17 Oct, unrun).
4. **Gate DYN** — run or withdraw (card 10 Oct; no run located).
5. **Gate DL** — run or withdraw (card 15 Sep; overtaken by ICE/STIFF).
6. **From BUBBLE_BELLS (10 Nov):** a dispersion gate (bells at the zone edge vs the O(k⁴) Lorentz
   term, CN-QED-09) and an INVENTORY-style sweep of the condensate mass m used across the corpus vs
   the implied 0.24 m_P. Both still to be carded.
7. **From SONO (12 Nov):** CN-SONO-13 — `BCT_Volumes_Zenodo_Guide.md` L40 should stop describing
   #154/#155 as errors of −0.3 % / +0.65 % against observation; CN-SONO-08 — before the next
   fit audit, write down a comparison-value charge rule (the card cited a "PRED2 drift rule" that
   exists only as a Gate PRED finding).
8. **PRED follow-ups** (carried from 14 Sep): (a) commit an itemised 92-row table or withdraw the
   number; (b) **closed by FWD7** — nothing is pinned and geometry-specific enough to pre-register
   (SC-FWD7-2), so (b) is no longer "pre-register the six"; (c) correct the PRL C_p misprint and the
   α_s(m_Z) claim. CN-PRED-01 (One Medium App. A Eq. (15) arithmetic) still open.
9. **Census** — resume at `tex/BCT_Appendix_KA1.tex`, next id INV-0035 (`inventory/inv_state.json`).
10. **Gate RATIO-OBS** (proposed 14 Sep, never written): is the substrate void radius in-principle
    observable? Direct finaliser of SC-RATIO-2 (CN-RATIO-07). Write and pre-register before running.
11. **PQCD** — decide: commit and pre-register the Project draft, or drop it.

## Parked
- **DIPOLE** — card never written into the tree.
- **FORK2** — card written 10 Nov, delivered as a patch, not applied (item 2).
- **PQCD** — Project draft only (item 11).

## Queue reconciliation (14 Sep → 12 Nov)
- 14 Sep item 1 "Gate XI (new, proposed)" — XI had already run (14 Sep, SC-XI-3); row above.
- 14 Sep item 2 "Gate PRED2" — closed 14 Sep; row above and block below.
- 14 Sep item 4 "Deliverable debt: MAD, TANH, INT" — all three now in the tree; replaced by the
  current debt list (item 2).
- 14 Sep "Parked: Gate PV (prompt lost)" — PV ran 16 Sep on a new card; the old `ca214df4…` card is
  superseded, not lost.
- Items 3, 5, 6 carried as 8, 9, 10.

## Standing rules, learned the hard way
- Commit deliverables, scripts and prompts to `audit/` **at close, not at leisure**. On 14 Sep four
  closed gates (C1, RANK, MP, PRED) had no committed deliverable and RANK's committed file was
  0 bytes. This file was wrong for three days.
- **A patch that is never applied is a result that does not exist.** KL (15 Sep), FORK and FWD7
  (11 Oct) and LATT (17 Oct) were all run and none reached the tree; this file was wrong for two
  months. "Pushed" is the close of a gate, not "delivered". Verify from a fresh clone.
- The claude.ai Project is a mirror, not the record. Anything that matters is in this tree.
- Gate prompts are pre-registered: commit, pin by commit SHA, fetch by raw URL, hash before reading.
  The `PREREG_*.sha256` line in the tree is the authority — a run prompt's digest can be truncated
  in transit (SONO: 40 of 64 hex characters arrived).
- **One name, one gate.** `gate_PRED_prompt.md` was pre-registered at `23bf80b` (`69b7b7ea…`) and
  overwritten three hours later at `aa70943` (`7e7675da…`) by a different prompt, which is the one
  that ran. Never overwrite a pre-registered prompt file; give a rewritten gate a new name. The
  prereg record must be regenerated in the same commit as any prompt change.
- A fresh blind thread is not "same-session". SONO capped itself at CONJECTURE on the same-session
  rule although it ran blind in a fresh thread; the cap belongs to card-writing threads and
  non-blind runs (BUBBLE_BELLS, TWIST's first run). Say which applies.
- The handoff template's curl line must name the gate being run; PRED's handoff named RANK.
- Audit the search space before any negative claim. Both traps: 26 `.tex` sit at the repo root
  outside `tex/`; and of the mount files 33 are ZIP archives and **2 are raw text** that neither
  `pdftotext`, `pymupdf` nor `unzip` will open. Type every file with `file`. Gate MP found
  `audit/APPENDIX_INDEX.md` referenced but absent at `aa70943` (added at `c3c705d`), and Vol 1
  Parts 1–2 are real PDFs in the repo (the raw-text note describes a mount). Check the pinned tree,
  not the mount, when writing §0.5.
- `.gitignore` excludes `*.pdf`; a letter or volume that a card pins must be `git add -f`'d (nine
  PDFs are tracked that way; Letter 110 was added so for SONO).
- Revise notices **clause by clause**. An "unaffected" list is a set of claims.
- A gate prompt must be able to return a favourable verdict. If it cannot, it is not a gate.

---

## Gate PRED2 — closed 14 Sep 2026 (appended without reading this file; quarantine held)

Prompt SHA-256 `69b7b7ea242146581cc05cd4e6b08257e2d29794d29b43f8d02e117bd20477c9`,
repo commit `ec0592f9319ab5a61851018539ab2b6ff2eb72b3`.
Deliverable: `audit/gates/PRED2/gate_PRED2_RESULT.md`.

**Verdict: SC-PRED-1**, met by `m_p/m_e = 6π⁵` (+15.6 net bits) — a formula the corpus itself
classifies as underived, and which the gate's blind inverse-symbolic control rediscovers at the
same complexity. **No prediction claimed as derived nets ≥ 10 bits.** Maximum over derived
predictions: 6.70 (`β = arccos 2r_oct`).

Positive net bits, all four with no post-hoc correction factor:
`β = arccos(2r_oct)` +6.70 · `sin²θ₁₃ = 3α₀` +4.61 · `sin²θ₁₂ = ⅓ − r_tet r_oct` +4.02 ·
`sin²θ_W(tree)` +3.38.

Negative net bits (grammar noise after charges): α = α₀(1−2α₀) −1.77 · α all-orders −5.57 ·
m_e via (π⁵+π)/6 −2.70 · **m_e via the C.2 dressing −17.12** · Koide phase −3.66 · m_ρ −6.26 ·
λ −7.09 · A −10.17 · m_d −10.52 · m_u −8.89 · m_b −10.76.

Benchmark: **Wyler ≈25 ± 1 bits** — ten bits above anything BCT produces, and Wyler is a
coincidence. Control beats the published expression on **8 of 10** targets at equal or lower
complexity.

### Open items this gate created, in priority order

1. **CN-PRED-01 — One Medium App. A Eq. (15) is arithmetically wrong.** `172 000 × e^−7.5075 =
   94.42 MeV`, not 93.0. Printed error −0.43 % should read +0.98 %. Fix or withdraw the worked
   example; it is the one derivation shown in full.
2. **CN-PRED-02 — m_P/M_R circularity.** `M_R ≡ m_P α₀²` (App GG2) and `m_P ≡ M_R/α₀²`
   (Monograph §19.1). Gravity sector of Table B.9 carries no independent content. *May overlap a
   concurrent gate; not read.*
3. **CN-PRED-03..06 — four printed expressions do not reproduce their printed values:**
   `2π/x_lep` → 666.14 not 137.046 · `r_p = ℏc/m_ρ(1+α₀)` → 0.2563 fm not 0.8386 ·
   Phase 35A Koide NLO formula ≠ its own printed 0.04050025 · `m_ρ` needs m_π0 = 134.98 while the
   table inputs m_π = 139.6.
4. **CN-PRED-12/13 — two stated errors fail against current data.** η̄ = 3r_tet is −4.3 %, not
   −0.603 % · `δ_CKM = arccos(⅓) = 70.53°` is ~4.5σ from γ = 65.75 ± 1.07°: retire or reclassify.
5. **Retire from public citation** (One Medium §10/§13, Monograph Tables 2 and B.9): α, G, m_P,
   the Wolfenstein set, m_d/m_u/m_b, m_ρ, r_p, and the −0.014 % electron mass. Deliverable §7
   names the sentences.
6. **Census coverage gap:** ~38 of the 92 claimed predictions cite appendices outside the search
   space (Vol. 1 only is mounted). A re-run with Vols. 2+ mounted would complete the census; the
   6.52-bit look-elsewhere charge applies unchanged.
7. **Recommended next gate:** derivation audit of the three uncorrected mixing predictions
   (`3α₀`, `⅓ − r_tet r_oct`, tree-level `sin²θ_W`) — they score positively for the right reason.
   A derivation audit of `6π⁵` is **not** recommended: the corpus already disclaims it and the
   control shows it is the grammar's own optimum at C = 4.

### Prompt defect recorded
SC-PRED-1 does not anticipate the case that fired — the single ≥10-bit result is disclaimed by the
corpus and reproduced by a blind control. Future PRED-class prompts should split the census into
*claimed-as-derived* vs *published-with-disclaimer*, and require the control result to be reported
alongside the score.

---

## Gate RATIO — closed 14 Sep 2026

Prompt SHA-256 `5a0c08773431c4b9de7fd69a7346c2cb087a283c49b8c1c256431b6a27aec2f3`
(matched pre-registration, 7008 B). Corpus tarball
`e4f5baf1e2e13ec53192bb47c6552052a674c1d36c92d66831d0255abe66ed64` at commit
`68ffd73641f237f5eb1de0a41785ca940a707881`. Deliverable:
`audit/gates/RATIO/gate_RATIO_deliverable.md`. Model: Claude Opus 4.8.

**Verdict: SC-RATIO-2.** Every observable of the minimal theory (one complex scalar, GP action,
MINIMAL_BCT §1.2) depends on r_oct and r_tet only through their product, via ξ = 1/√(8·r_oct·r_tet).
The geometry supplies one number — one length scale.

**Sharper than the stop condition.** The ratio r_oct/r_tet = 1.8430 was never a free datum:
r_oct = (√2−1)R and r_tet = (√(3/2)−1)R are the octahedral and tetrahedral interstitial inradii of
a *single* sphere radius R = a/2 (verified to 15 digits), so the ratio is a fixed FCC constant,
identical at any scale. The model has one scale and one packing choice (FCC), not two independent
radii. Dimensionful content additionally needs an external anchor — a = ℓ_P, assumed (App JH4
"single-point calculation at a=ℓ_P"; the corpus ties Λ_QCD to the same choice). Same epistemic
situation as INV-0120 (Λ_QCD as input).

**The lattice route, closed by calculation.** The continuum GP action is rotation-invariant →
isotropic dispersion, no ratio. A scalar phonon on the lattice gives c_z/c_x = η (axial ratio) in
the coordination-8 regime — so if the shape were free the ratio would do genuine work. But the
model's radii pin η = √2 (FCC); at that point close-packing brings the in-plane bonds into the same
shell → 12-fold cubic coordination → the sound tensor is exactly isotropic (D_xx=D_yy=D_zz).
Residual anisotropy is a fixed O(k⁴) FCC constant with no independent r-content. The model cannot
hold the shape fixed (zero parameters) AND have the ratio do observable work; the specific radii
choose the inert horn.

**Steelman, reported and failed for the minimal theory.** The full corpus uses individual radii
extensively — α₂ = r_oct²/π → v_BCT = 246.22 GeV (Volume2); x_EW ∝ r_oct, x_SU(3) ∝ r_tet
(Letter127); cos θ_K = r_oct − ½ (Monograph); and ξ/r_oct = 1/(√8·r_oct^{3/2}·r_tet^{1/2}) = 11.19
(Letter19), which does depend on the radii with unequal powers. None is derivable from the minimal
GP action, whose sole geometric input is ξ (the product); each is a standalone geometry→observable
posit layered with α₀/α₂/NLO factors and external scales — structurally the N-class scored ≈0 bits
by PRED2.

### Open items this gate created, in priority order

1. **CN-RATIO-07 [CONJECTURE] — is the substrate radius r_oct in-principle observable?** The one
   thread the gate left open, and the direct finaliser of the verdict. See queued Gate RATIO-OBS.
   If the minimal theory provides no operator that resolves r_oct from r_tet, SC-RATIO-2 is final.
   Even if the substrate is observable, r_oct/r_tet is FCC-fixed → a prediction, not a parameter.
2. **CN-RATIO-06 [ASSERTED] — retire or reclassify the individual-radius citations** (α₂ = r_oct²/π
   → v_BCT, x_EW ∝ r_oct, x_SU(3) ∝ r_tet, cos θ_K = r_oct − ½, ξ/r_oct = 11.19). They use the
   radii separately but are not consequences of the minimal action; resolve alongside the PRED2 §5
   "retire from public citation" list, not separately — same N-class family.
3. **Naming for the reachable claim.** Per MINIMAL_BCT §4 the publishable statement is "a lattice
   superfluid whose coupling is fixed by void geometry" — one geometric number (ξ/a = 2.3175) plus
   an external scale. SC-RATIO-2 is the evidence for that framing; "two radii, zero parameters"
   should not be used as stated.

### Notices
CN-RATIO-01..05 PROVEN (product-only dependence; FCC-constant ratio; continuum isotropy; lattice
cancellation at η=√2; external-scale requirement). CN-RATIO-06 ASSERTED (corpus individual-radius
formulas, unsupported by minimal action). CN-RATIO-07 CONJECTURE (substrate observability). Full
tiering and scripts in the deliverable.

### Queue reconciliation noticed while filing (14 Sep) — resolved 12 Nov, see above
- **PRED2** appeared both as queued item 2 and as a closed block — it had closed (SC-PRED-1).
- **Gate XI** appeared as queued "(new, proposed)" although MINIMAL_BCT §0 cited "Gate XI, SC-XI-3"
  as run — a stale queue entry.
