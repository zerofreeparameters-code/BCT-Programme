# NEXT — what is queued, running, and closed

Last updated 11 September 2026. **Update this file at the close of every session.**
It exists because three sessions have independently invented their own gate
order, and one spent a turn treating a committed prompt as a mystery file.

## Closed
| gate | verdict | deliverable |
|---|---|---|
| PSI2 | closed on SC-PSI2-2/4/5; Psi_2 supplies no second A1g Goldstone | `gates/PSI2/` |
| TANH | SC-TANH-3: alpha_0 and g are distinct objects, App J S3.1 conflates them. 0 published predictions moved | **deliverable MISSING** |
| INT | SC-INT-4: three distinct interior commitments, re-scoped to enumeration | **deliverable MISSING** |
| LAM, LAMBDA | run elsewhere; cross-audited from the PSI2 thread | `gates/crossaudits/` |

## Queued, in priority order
1. **Gate C1** — does the interior carry its own healing length xi_2?
   *The highest-leverage open question.* If xi_2 = xi, the granular half of BCT
   (OHC, Hopfions, site-local chemistry) is unavailable. If xi_2 << a, it returns
   and `notes/note_healing_length.md` collapses. Prompt not yet written.
2. **Gate PRED** — score the numerical predictions (alpha, m_e, Koide, mass
   ratios) for surprise, as Gate STAT did for pi^5/6. The identity family has
   been scored at 3.3 bits (`notes/note_identities.md`); the predictions are
   unscored and are what the programme stands on. Prompt not yet written.
3. **Census** — resume at `tex/BCT_Appendix_KA1.tex`, next id INV-0035.
   Coverage 6 of 134 .tex = 4.5%. See `inventory/inv_state.json`.

## Parked
- **Gate PV** — prompt is lost; ledger holds its digest `ca214df4...4062`.
  Find the file and verify against that digest, or rewrite. Its J->PV->E5
  sequence predates the current priorities.

## Not recommended yet
Gravity and QM sectors, and new appendices. Gravity carries a
representation obstruction the corpus states itself (Letter 260's rank ladder,
Gate N, Gate G'). New appendices add to what needs auditing while the census
sits under 5%.

## Standing rules, learned the hard way
- Commit deliverables, scripts and prompts to `audit/` **at close, not at leisure**.
- Gate prompts are pre-registered: commit, pin by commit SHA, fetch by
  raw URL, hash before reading.
- Search space must be audited before any negative claim. Both traps:
  26 `.tex` sit at the repo root outside `tex/`; and of the mount files, 33 are
  ZIP archives and **2 are raw text** that neither `pdftotext`, `pymupdf` nor
  `unzip` will open. Type every file with `file`.
- Revise notices **clause by clause**. An "unaffected" list is a set of claims.
