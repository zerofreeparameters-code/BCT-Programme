# BCT AUDIT ARCHIVE

Produced 11 September 2026. Commit this tree as-is.

## Why this exists
Gate deliverables have been living in chat windows. Three consequences already:
 1. Gate FWD's deliverable exists only in chat.
 2. Gate Ψ2's deliverable was unarchived, so Gates LAM and Λ both printed the
    false claim "fourth consecutive gate with a broken pre-registration chain".
    Ψ2 had a confirmed digest. They could not see it.
 3. The inventory pass lost its state file, 115 claims and five CSVs, and had
    to restart from zero.

Unfiled work is now producing factual errors in later work. That is the reason
to commit this, not tidiness.

## Contents

    gates/PSI2/          Gate Ψ2: prompt as run, result v1, correction v2,
                         addenda v2.1 and v2.2. Read in that order.
    gates/crossaudits/   Clause audits of Gate LAM Phase 1 and Gate Λ.
    inventory/           Census session 2: coverage, claims, phantom refs,
                         versions, DOIs, and a RESUMABLE state file.
    scripts/             Ψ2 verification scripts. Deterministic, mpmath, no seeds.

## Digests at time of archiving

    gate_PSI2_prompt_asrun.md   948909cbd49a3fdf…   (= the pre-registration; MATCH)
    gate_PSI2_RESULT.md         4b0e6bf23defa8df…
    gate_PSI2_CORRECTION_v2.md  455a2df414873c8b…
    gate_PSI2_ADDENDUM_v2_1.md  2d8707feb84b9dc0…
    gate_PSI2_ADDENDUM_v2_2.md  edda899037497f3e…
    gate_LAM_crossaudit.md      0205577c5fdd306d…
    gate_LAMBDA_crossaudit.md   e505796e566bd31b…

Repo state audited: tarball SHA-256
86aca2692650dd66fb2464c0825e7c9a160c1bc278666e6fd65796a85c2584d7

## Next session

Read inventory/inv_state.json. Resume at tex/BCT_Appendix_KA4.tex, next id
INV-0019. Coverage stands at 3 of 134 .tex read in full (2.2%). Report coverage
before any other number.

## Outstanding, and not fixed by this archive

 - inventory_prompt.md (SHA 49607bc7…) is not recoverable. The census currently
   runs without a pre-registered digest. Commit a fresh prompt and pin it.
 - Gate deliverables should be committed at close, not at leisure.
