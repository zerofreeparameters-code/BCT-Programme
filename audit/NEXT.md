# NEXT — what is queued, running, and closed

Last updated 14 September 2026 (ledger reconciliation). **Update this file at the close of every session.**
It exists because sessions have independently invented their own gate order, and
one spent a turn treating a committed prompt as a mystery file.

## The goal, as currently stated
Unification is the long aim. The working target is **any two of QM, GR, EM**.
Current reading: GR carries a representation obstruction the corpus states itself
(Letter 260's rank ladder, Gate N, Gate G'), so the reachable pair is **QM + EM**.
Gates MAD and LINK below test exactly that pair. This reading is a judgement, not
a result, and either gate may overturn it.

## Closed
| gate | run | verdict | deliverable |
|---|---|---|---|
| PSI2 | — | closed on SC-PSI2-2/4/5; Psi_2 supplies no second A1g Goldstone | `gates/PSI2/` |
| TANH | — | SC-TANH-3: alpha_0 and g are distinct objects, App J S3.1 conflates them. 0 published predictions moved | **MISSING** |
| INT | — | SC-INT-4: three distinct interior commitments, re-scoped to enumeration | **MISSING** |
| LAM, LAMBDA | — | run elsewhere; cross-audited from the PSI2 thread | `gates/crossaudits/` |
| C1 | 12 Sep | SC-C1-3: the interior healing length ξ₂ is not determined by the corpus; halt and report. SC-C1-4 not triggered at Step 0; SC-C1-5 triggered in part (symbol ξ overloaded) without blocking. §3 delivered both ways. | `gates/C1/` |
| RANK | 13 Sep | SC-RANK-3: the corpus does not determine the field content; halt. By written dynamics BCT is a scalar theory; by its claims about light and gravity it is a vector theory with no dynamics written. Both readings live. | `gates/RANK/` |
| MP | 13 Sep | SC-MP-1 (qualified: HF4's m_P = M_R/α₀² is an identity on GG2's M_R = m_P·α₀²; the −0.08% is input rounding) + SC-MP-3 (input set, M_R, G_BCT all inconsistent across documents). Scale a = ℓ_P is assumed and declared. JB6 and L128 "derivations" of m_P are inverted fits, not circular. 12 notices. | `gates/MP/` |
| PRED | 13 Sep | SC-PRED-1: observed matches are within chance expectation; 39/40 closed forms reproduce; 28 eligible sub-1% vs E≈100–130 by construction; best single item 1/α ≈ 6 bits; m_P = M_R/α₀² circular (CN-PRED-01); "92" not reconstructible (CN-PRED-02). Prompt as run: `7e7675da…` (see `gates/PRED/gate_PRED_prompt_asrun.md`). | `gates/PRED/` |
| MAD | 14 Sep | SC-MAD-1 (verdict recorded in-thread; deliverable not yet written) | **MISSING** |

## Queued, in order
1. **Gate LINK** — `gates/gate_LINK_prompt.md`. Site or link variables, and is
   the second photon polarisation reachable? Includes an itemised price tag for
   the reformulation. The only pinned prompt not yet run.
2. **Gate PRED2** — `gates/gate_PRED2_prompt.md` (`69b7b7ea…`, pre-registered at
   `23bf80b`, 13 Sep). Per-prediction surprise scoring under an enumerated grammar
   with look-elsewhere, correction-factor and date-order charges, and a Wyler
   benchmark. Distinct from PRED, which scored the collection. **MP residue:** the
   exponents S_e, S_QCD, S_R were each selected against ln(m_P^CODATA/X); score
   them as fits. Carry CN-MP-03 (two M_R values) and CN-MP-04 (three input sets)
   as corpus-consistency items to be resolved before scoring. Carry PRED's §7
   subset as the candidates worth scoring first.
3. **PRED follow-ups** (from `gates/PRED/gate_PRED_NEXT_patch.md`): (a) commit an
   itemised, formula-bearing 92-row table or withdraw the number; (b) pre-register
   the six untested predictions (Σm_ν, r, τ_p, d_n, m_DM, δ_CKM) with fixed values
   now; (c) correct the PRL C_p misprint and the α_s(m_Z) claim.
4. **Deliverable debt:** write and commit the MAD deliverable; recover or
   reconstruct the TANH and INT deliverables, or record them as lost.
5. **Census** — resume at `tex/BCT_Appendix_KA1.tex`, next id INV-0035.
   Coverage 6 of 134 .tex = 4.5%. See `inventory/inv_state.json`.

## Parked
- **Gate PV** — prompt lost; ledger holds digest `ca214df4...4062`. Find and
  verify, or rewrite. Its J->PV->E5 sequence predates the current priorities.

## Standing rules, learned the hard way
- Commit deliverables, scripts and prompts to `audit/` **at close, not at leisure**.
  On 14 Sep four closed gates (C1, RANK, MP, PRED) had no committed deliverable and
  RANK's committed file was 0 bytes. This file was wrong for three days.
- Gate prompts are pre-registered: commit, pin by commit SHA, fetch by raw URL,
  hash before reading.
- **One name, one gate.** `gate_PRED_prompt.md` was pre-registered at `23bf80b`
  (`69b7b7ea…`) and overwritten three hours later at `aa70943` (`7e7675da…`) by a
  different prompt, which is the one that ran. Never overwrite a pre-registered
  prompt file; give a rewritten gate a new name. The prereg record must be
  regenerated in the same commit as any prompt change.
- The handoff template's curl line must name the gate being run; PRED's handoff
  named RANK.
- Audit the search space before any negative claim. Both traps: 26 `.tex` sit at
  the repo root outside `tex/`; and of the mount files 33 are ZIP archives and
  **2 are raw text** that neither `pdftotext`, `pymupdf` nor `unzip` will open.
  Type every file with `file`. Gate MP found `audit/APPENDIX_INDEX.md` referenced
  but absent at `aa70943` (added at `c3c705d`), and Vol 1 Parts 1–2 are real PDFs
  in the repo (the raw-text note describes a mount). Check the pinned tree, not
  the mount, when writing §0.5.
- Revise notices **clause by clause**. An "unaffected" list is a set of claims.
- A gate prompt must be able to return a favourable verdict. If it cannot, it is
  not a gate.
