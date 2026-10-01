# Gate ALTER-R — Operator comparison record

**Programme:** The BCT Superfluid Lattice Model (ZeroFreeParameters, ORCID 0009-0007-9561-9859)
**Recorded:** 2026-10-01 (Barrys Reef, AEST)
**Operator:** Michel Robert Cabrié. Committing this file is the operator's ruling.
**Prepared with:** Claude (Fable 5.1), in the session that wrote the ALTER-R card. That session had read the first run's result and is not blind; it did not run the gate.

## 1. The two runs

| | Gate ALTER (first run) | Gate ALTER-R (replication) |
|---|---|---|
| Runner | Opus 5.5, fresh context | `claude-fable-5-1`, fresh session |
| Card | `gate_ALTER_prompt.md`, SHA-256 `3cf882a6…5882` | `gate_ALTER_R_prompt.md`, SHA-256 `3d157c7e…0054`, committed `6c7d23c` |
| Result commit | `dc9fbbf` | `3f4f20a` |
| Corpus | tree at `0d9600a`, `audit/` excluded | same |
| Files counted outside `audit/` | 272 (148 primary + 124 secondary) | 290 (159 primary + 127 secondary + 4 images) |
| Verdict | SC-ALTER-2 (KILL — absent) | SC-ALTER-2 (KILL — absent), with one qualification |

ALTER-R deliverables as committed: `gate_ALTER_R_RESULT.md` SHA-256 `7e4ceede85cf50fc3aa7a0f88d5aac38ee13a1a26a394e96a7fdc407d6069f51`; `alter_r_check.py` SHA-256 `18e37fdaa3da8f47b9dec693ed8178f76289cf1d9e61f8ac52f181beca87d2b4`.

## 2. Comparison outcome

**MATCH-WITH-DIFFERENCE.** Same verdict. The one near-miss common to both runs received the same space group. The replication found and derived near-misses the first run did not log.

## 3. Differences

1. **App L §4.3 (right-handed on A, left-handed on B) — agrees.** Both runs: P4/nnc (No. 126), degenerate by an A→B inversion, no screw axis. ALTER-R adds a second admissible reading (labels as plain colours): P4/mmm (No. 123), also degenerate.
2. **App Q.5 — new.** Two tetrahedral voids labelled "up-type and down-type", "related by the C₄v rotation" (Volume 1 Part 1, PDF pp. 150–151). Not logged by the first run. Derived in ALTER-R as NM-5: the two tet sets are exchanged by inversion; every 4-fold is a pure rotation; the body-centring remains a pure translation. I-4m2 (No. 119) at generic c/a, F-43m (No. 216) at √2. Degenerate.
3. **Oct versus tet labelling — new as a derivation (NM-4).** The two void types are symmetry-inequivalent sets, so no compensated pair exists. ALTER-R also records that the corpus is inconsistent about which void carries u and d.
4. **A/B naming (NM-1) and the oct-void c-director (NM-3)** were noted by the first run without a space-group derivation. ALTER-R derives both: I4/mmm (No. 139), or Fm-3m (No. 225) at √2. Degenerate by translation.
5. **Verdict wording.** SC-ALTER-2's sentence "every void, hopfion and winding assignment is translation-invariant under the body-centring vector" holds for those three kinds only. App L §4.3 is not translation-invariant; it is inversion-related. The accurate statement is: every per-site assignment in the pinned tree is either translation-invariant or inversion-related.
6. **Search gap.** Symmetry symbols written with Unicode subscripts (D₄h, C₄v and similar) were not matched by the initial patterns. ALTER-R closed the gap with a further pass (768 blocks) and found nothing staggered. Whether the first run had the same gap was not checked.
7. **File counts differ** (272 versus 290). Not reconciled. Both runs used the same pinned tree.

## 4. Rulings on the runner's three open items

1. **Memory snapshot present in context.** Accepted as BLINDED, with the deviation recorded. The snapshot showed the BCT project only as a collapsed folder name and contained no ALTER outcome. This rests on the runner's disclosure. The run was not made in a no-memory chat as the card intended.
2. **Control assertion that failed on first run.** SC-R-1 ruled NOT FIRED. The defining control test (translation fails, inversion fails, 4₂ screw succeeds on MnF₂) passed on the first run. The failed assertion was the runner's own expected count of screw/glide operations for P4₂/mnm (8 written, 6 correct).
3. **Hash source.** Accepted. The original card's hash was compared against the digest printed in ALTER-R §1, because ALTER-R forbids reading `audit/gates/PREREG_20261001.sha256`.

## 5. Independent verification of the deliverables

Done in the preparing session, outside the runner's context:

- `alter_r_check.py` re-run: 69 / 69 exact assertions pass.
- With spglib installed, 12 / 12 operation sets are identical to the tabulated groups, including the MnF₂ control (No. 136).
- The patch applied to an empty repository reproduces both files byte for byte.

Not verified: the corpus search. The absence finding rests on the runner's search and its internal checker.

## 6. Status

- Gate ALTER stays closed at SC-ALTER-2, now replicated.
- No prediction moves. Nothing is un-killed.
- **Reopen tripwire:** App Q.5 (NM-5) and the oct/tet labelling (NM-4) are logged here as degenerate. Rediscovering either, or App L §4.3, does not trigger a reopen.
- **Coverage unchanged:** the verdict covers the pinned tree only. The Project-attached PDFs outside the repository remain unsearched, as do Letters the tree cites but does not contain (Letter 18 among them).

## 7. Addendum, 2026-10-01

File-count difference (§3 item 7) reconciled. `git ls-tree` on `0d9600a` excluding `audit/` gives 290 files: 138 tex, 9 pdf, 1 zip (= 148) and 123 md, 1 txt (= 124), total 272 documents, plus 18 non-document files (4 py, 4 png, 3 html, 2 yml, .gitignore, LICENSE, CNAME, main, Sync Zenodo DOIs). The first run counted documents only. Totals match; file lists were not compared.
