# NEXT — what is queued, running, and closed

Last updated 13 September 2026 (Gate MP closed). **Update this file at the close of every session.**
It exists because sessions have independently invented their own gate order, and
one spent a turn treating a committed prompt as a mystery file.

## The goal, as currently stated
Unification is the long aim. The working target is **any two of QM, GR, EM**.
Current reading: GR carries a representation obstruction the corpus states itself
(Letter 260's rank ladder, Gate N, Gate G'), so the reachable pair is **QM + EM**.
Gates MAD and LINK below test exactly that pair. This reading is a judgement, not
a result, and either gate may overturn it.

## Closed
| gate | verdict | deliverable |
|---|---|---|
| PSI2 | closed on SC-PSI2-2/4/5; Psi_2 supplies no second A1g Goldstone | `gates/PSI2/` |
| TANH | SC-TANH-3: alpha_0 and g are distinct objects, App J S3.1 conflates them. 0 published predictions moved | **MISSING** |
| INT | SC-INT-4: three distinct interior commitments, re-scoped to enumeration | **MISSING** |
| LAM, LAMBDA | run elsewhere; cross-audited from the PSI2 thread | `gates/crossaudits/` |
| MP | SC-MP-1 (qualified: HF4's m_P = M_R/α₀² is an identity on GG2's M_R = m_P·α₀²; the −0.08% is input rounding) + SC-MP-3 (input set, M_R, G_BCT all inconsistent across documents). Scale a = ℓ_P is assumed and declared. JB6 and L128 "derivations" of m_P are inverted fits, not circular. 12 notices. | `gates/MP/` |

## Queued, in order
1. **Gate C1** — `gates/gate_C1_prompt.md`. Does the interior carry its own
   healing length? Decides whether site-local structure is available at all,
   and therefore how much of the corpus is being defended. One session.
2. **Gate MAD** — `gates/gate_MAD_prompt.md`. Does BCT derive quantum mechanics,
   or restate it via Madelung? Four-bin discrimination against the standard
   GP/NLSE correspondence. External literature permitted and expected.
3. **Gate LINK** — `gates/gate_LINK_prompt.md`. Site or link variables, and is
   the second photon polarisation reachable? Includes an itemised price tag for
   the reformulation.
4. **Gate PRED** — not yet written. **MP residue for PRED:** the exponents S_e, S_QCD, S_R were each selected against ln(m_P^CODATA/X); score them as fits. Also carry CN-MP-03 (two M_R values) and CN-MP-04 (three input sets) as corpus-consistency items to be resolved before scoring. Score the numerical predictions (alpha, m_e,
   Koide, mass ratios) for surprise, as Gate STAT did for pi^5/6. The identity
   family scored 3.3 bits (`notes/note_identities.md`); the predictions are
   unscored and are what the programme stands on.
5. **Census** — resume at `tex/BCT_Appendix_KA1.tex`, next id INV-0035.
   Coverage 6 of 134 .tex = 4.5%. See `inventory/inv_state.json`.

## Parked
- **Gate PV** — prompt lost; ledger holds digest `ca214df4...4062`. Find and
  verify, or rewrite. Its J->PV->E5 sequence predates the current priorities.

## Standing rules, learned the hard way
- Commit deliverables, scripts and prompts to `audit/` **at close, not at leisure**.
- Gate MP found `audit/APPENDIX_INDEX.md` referenced but absent at `aa709432`, and Vol 1 Parts 1–2 are real PDFs in the repo (the raw-text note describes a mount). Check the pinned tree, not the mount, when writing §0.5.
- Gate prompts are pre-registered: commit, pin by commit SHA, fetch by raw URL,
  hash before reading.
- Audit the search space before any negative claim. Both traps: 26 `.tex` sit at
  the repo root outside `tex/`; and of the mount files 33 are ZIP archives and
  **2 are raw text** that neither `pdftotext`, `pymupdf` nor `unzip` will open.
  Type every file with `file`.
- Revise notices **clause by clause**. An "unaffected" list is a set of claims.
- A gate prompt must be able to return a favourable verdict. If it cannot, it is
  not a gate.
