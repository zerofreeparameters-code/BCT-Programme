# Gate SINGLET — ledger entry (tier decision)

**Date:** 25 October 2026. **Recorded by:** Claude, in a separate thread after the run, at Michel's instruction.
**Card:** `audit/gates/gate_SINGLET_prompt.md`, commit `fc4b632`, SHA-256 `272dca3d…ed16e`.
**Run:** one fresh thread, 25 October 2026 (Claude Opus 5.5). Result: `gate_SINGLET_RESULT.md`, committed at `10e8739`.

## Checks made on the result in this thread

- **Digest and scope.** The as-run card in `10e8739` hashes to `272dca3d…ed16e`, the value in
  `PREREG_20261025_SINGLET.sha256`. The commit adds only the 15 files under `audit/gates/SINGLET/`.
  `audit/NEXT.md` was not touched, as the card requires.
- **Same code, re-run.** The run's scripts were re-run with the same package versions (numpy 2.5.3,
  scipy 1.18.1, mpmath 1.4.1, matplotlib 3.11.2). All four output files and `singlet_E_theta.png`
  reproduce byte for byte. This confirms the run was done as reported. It is not a replication.
- **Own code, written without opening the run's scripts** (`singlet_ledger_check.py`, output beside it):
  - Built from the card's description alone (lazy walk on the 2m-site cover, antiperiodic projection,
    second walker half a turn away, squared readout), at m = 24, p = ½, t = 800, over all 576 setting
    pairs: max |E + cos θ| = 1.1×10⁻¹⁵, CHSH = −2.828427124746190, marginal spread 1.0×10⁻¹⁵,
    normalisation flat to 1.9×10⁻¹⁵. Dropping the Z₂ sign gives |S| = 8×10⁻¹⁷.
  - At t = 3200 this direct form loses five digits to cancellation (2.6×10⁻¹¹). That is the reason the
    run used the seam form, as its §2 says.
  - Closed forms in mpmath (60 digits): λ₃/λ₁ = 0.9660722070828949…; (2/π)² = 0.4052847345…, so the
    site-complete readout's limit is |S| = 1.1463183365…; the closed form for Σ|M|^q is
    setting-independent only at q = 2 (relative variation 0.45, 0.33, 0.17, 3×10⁻⁶¹, 0.34, 0.67 at
    q = 0.5, 1, 1.5, 2, 3, 4). All match the result's §2 and §6.
  - The c/a = √2 lattice has 12 nearest neighbours at one distance, so it is fcc. Of the 8 spin
    structures, O_h leaves only the trivial one invariant; D₄h on the bct cell leaves two. This matches
    CN-SINGLET-06(c) and -12.
- **Citations spot-checked** at `10e8739`. Each says what the result says it says:
  - Letter 64 l.86–89: Theorem I states that no Markovian stochastic process can reproduce the OHC dynamics.
  - OneMedium l.361–363: ħ, superposition and the Hilbert-space postulates are inputs.
  - App JH FINAL l.194–198: Ψ₂ is declared ℂ²-valued, and the unit field is said to map S³ → S².
  - AZ7 l.359–364: Lemma "Spinor excluded" calls the E representation of C₄ᵥ a spinor doublet.
- **Not checked here:** the 53.908 coefficient in CN-SINGLET-11(b) (only the scaling law, which is
  Derrick's), the outputs of Hsieh's scripts, and the literature readings in §6.
- **Contamination.**
  - The run's disclosed overreach (§11) exposed CN-MAD-05 and CN-MAD-06. They concern Letter 81's
    hopfion capacity rule and Letter 72's tier. Neither bears on SINGLET.
  - The run session received the project memory listing (file names and one-line descriptions; no file
    was opened). The standing step for gate runs is to switch memory and past-chat search off first.
    Either the step was not applied this time, or it does not suppress the listing; this is worth
    checking before the next run. The verdict codes it exposed are PILOT's, which the card permitted,
    and those of unrelated gates. No effect on the verdict was found.

## Tier movements

| # | Statement | Tier | Basis |
|---|---|---|---|
| 1 | Verdict SC-SINGLET-2: written BCT supplies neither (i) a non-negative local process on the phase nor (iii) a squared readout; (ii) the Z₂ sign is absent on the S¹ branch, and present but connected to nothing on the ℂ² branch | **Recorded as run. IMPORT.** | search output reproduced; the four load-bearing citations checked |
| 2 | Letter 254: a single extended Hopf configuration reproduces the Bell violations | **RETIRED.** Stays withdrawn, as since `9c1953e` | CN-SINGLET-10 re-traces CN-MAD-04: a value fixed at creation and read locally is a local hidden variable, so \|S\| ≤ 2 |
| 3 | BCT explains entanglement | **RETIRED** as a derivation. Entanglement is imported into BCT | every Bell exit the audit has posed ends in import: local hidden variables (MAD, CN-MAD-04), faster-than-c channels and added structure such as superdeterminism (PILOT, SC-PILOT-3; PILOT card l.77), and now the signed measure (SINGLET) |
| 4 | Positive control, ablations, readout exponent, no BCT number in E(θ) (CN-SINGLET-01, -02, -03, -09) | **PROVEN**, reproduced | same code reproduces byte for byte; own code and closed forms agree. Same model family, so not a different-analyst replication |
| 5 | Under its own constraint \|Ψ₂\|² = ρ₀, App JH's free energy selects no H = 1 ground state (CN-SINGLET-11(b)) | **PROVEN. Active correction to App JH** | agrees with Gate JHF (SC-JHF-1: Derrick-unstable, no stabilising term), reached from a different starting point by a quarantined thread that could not read JHF |
| 6 | AZ7's Lemma "Spinor excluded" mislabels the E representation of C₄ᵥ, which is single-valued, and the c/a = √2 lattice's point group is O_h, not C₄ᵥ (CN-SINGLET-12) | **PROVEN. Active correction to AZ7.** AZ7's scalar conclusion stands as a stated commitment, not a theorem | standard group theory; lattice check above |
| 7 | The same Ψ₂ is written as one complex scalar (App J, AZ7) and as a ℂ² field (App JH) (CN-SINGLET-08(c)) | **OPEN** as a corpus decision. No action needed for SINGLET | the verdict is the same on both branches; consistent with Gate PROMOTE (SC-PROMOTE-1: S¹ stands; a richer target is an unselected free input) |
| 8 | On the ℂ² branch, the SU(2) double cover supplies the antiperiodic sign automatically | **PROVEN. No movement** | the one steelman-for point that succeeded. It is the datum Hsieh had to add, but (i) and (iii) are still missing |
| 9 | Two findings about the prior construction (CN-SINGLET-03, -04): the square is fixed by completeness, not by non-negativity; the readout used in Hsieh's Proposition 7 demonstration gives \|S\| → 1.146, below the local bound | **PROVEN (computation)**, about outside work. No BCT movement | result §2 ablation 4 and §6; closed forms rechecked here |
| 10 | BCT void geometry | **No movement** | CN-SINGLET-09: no BCT number enters E(θ) |

## Standing sentences

- An import does not refute the rest of BCT. It means entanglement has to be added to BCT rather than
  explained by it (card §0.6).
- The gate could have passed. The positive control found the survivor whenever the ingredients were present.
- The stated prior (SC-SINGLET-2) was right. The verdict rests on the citations and computations, not on the prior.

## What would move these items

- **Item 1** moves only if a written stochastic rule on the phase and a written readout turn up in a source
  outside the card's list. Volumes 1–2, Appendices E.2 and G, and Letters 27 and 72 were not searched.
  PILOT's search of the volumes found no "Born", "Fock" or "wave functional" hits.
- **Item 7** needs a decision about the corpus's field content, not another gate.
