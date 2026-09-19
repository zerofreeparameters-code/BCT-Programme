# Gate PT — pre-registration prompt (Round Periodic Table)

**Run in a FRESH thread with fresh context (Whopper Protocol). One gate, that thread only. Hash-before-read (curl the prompt to disk, do not paste). Adversarial: one-sentence-kill rule applies; null results are findings. CONJECTURE-capped if run same-session as any other gate. Terminal-verify every load-bearing claim (mpmath 60 dps work / 40 dps report; topology/homotopy/group facts computed or cited, not asserted).**

## Question

The Round Periodic Table classifies its entries by a **topological charge** carried by the vacuum field. The corpus's actual derived field content is a single-component order parameter with vacuum manifold **M = S¹** (established: Gates F/Fb, G′, PT-01, PROMOTE). The Hopf charge the Round PT needs lives in **π₃(S²) = ℤ**, but **π₃(S¹) = 0**.

**Does the Round Periodic Table have any zero-parameter topological foundation on the corpus's actual field (M = S¹) — or is its classifying charge identically zero on every configuration, so the table labels nothing that exists on the field, reopening only if a promotion M → S² is DERIVED (which Gates PROMOTE / JHF / KL have already closed along the geometry-fixed route)?**

If the charge is identically zero and no S¹-native invariant reproduces the assignments, the Round PT is **structurally void on the actual field** (SC-PT-1). If a different, S¹-native invariant carries some of the structure with zero free inputs, report exactly which assignments survive (SC-PT-2). If a zero-parameter foundation genuinely exists, exhibit it (SC-PT-3, the prize) — but it must not smuggle in the S² promotion PROMOTE closed.

## Background (established — do not re-derive; reconcile against, after forming an independent read)

- **CN-PT-01:** the Round PT's load-bearing axiom requires π₃(S²) = ℤ; BCT's one-component field has M = S¹ with π₃(S¹) = 0, so Hopf charges are identically zero on the actual field content.
- **Gate PROMOTE (SC-PROMOTE-1):** the derived BCT geometry selects NO promotion of M beyond S¹ under either bar (FORCE or PREFER); the promotion is a free input. FCC ≠ pyrochlore; an O_h irrep in a character table is not selection.
- **Gate JHF (SC-JHF-1) + Gate KL (SC-KL-2):** the hopfion/OHC medium is not a stabilised (JHF: Derrick collapse) or ground-state (KL) theory along the geometry-fixed route. KL's sharp result (CN-KL-06, PROVEN): for a periodic map [T³, S²] the protected charge is the **π₂ sheet (baby-skyrmion) charge in H²(T³) = ℤ³**; the Hopf integer is defined only mod 2·gcd once sheet charges ≠ 0 — a woven periodic texture is a baby-skyrmion crystal, NOT a hopfion crystal. The Hopf integer does not survive weaving.
- **Gate MIX / FWD / STAT:** the numeric-prediction layer is fits; proximity of a geometric-alphabet number to a target carries ≈0 bits after look-elsewhere. Any numeric coincidence the Round PT leans on must be scored, not asserted.
- Corpus sources to check: the Round PT documents (`BCT_PeriodicTable_Round_v12_1.pdf`, the interactive HTML) and whichever appendix states the charge/axiom (App PT and its dependencies; check the repo, which is fuller than the mount).

## The things it must resolve (any one unresolved in favour of a foundation ⇒ SC-PT-3; all confirmed ⇒ SC-PT-1)

1. **Identify the classifying invariant, cold.** Read the Round PT source and state precisely which topological invariant labels the entries (Hopf charge / linking number / a shell-and-period index built from it). **One-sentence kill:** if the labelling invariant is the Hopf charge π₃(S²) and the derived field is S¹, then the invariant is identically 0 on every field configuration, and the classification is a labelling of the empty set on the actual field.

2. **S¹-native alternatives (enumerate; do not wave away).** Compute which invariants ARE nonzero on M = S¹: winding π₁(S¹) = ℤ (1-dimensional — can it index a 2-parameter table?); the π₂ sheet charge H²(T³) = ℤ³ that KL showed survives weaving. **One-sentence kill:** if no S¹-native invariant has the rank/structure to reproduce the Round PT's period-and-group assignments with zero free inputs, then the table has no topological foundation on the actual field.

3. **Does it need the closed promotion?** Confirm whether any working version of the Round PT requires M → S² (or richer). **One-sentence kill:** if it does, it inherits PROMOTE (no derived promotion) + JHF/KL (no stabilised/ground-state hopfion medium), and the foundation is closed, not open.

## Escape routes (enumerate and evaluate each)

- (i) **π₂ baby-skyrmion sheet charge** (from KL): survives on the actual field but is NOT the Hopf integer — does it reproduce the Round PT's actual element/shell assignments, or a different (smaller) classification? Report which assignments it can and cannot carry.
- (ii) **π₁(S¹) winding**: 1D; test whether a 2-index table can be built from it plus geometry with zero parameters.
- (iii) **A derived promotion to S²**: forfeits nothing new to test — closed by PROMOTE/JHF/KL; report the trade explicitly.
- **Requirement:** any claimed foundation (SC-PT-3) must (a) use an invariant that is nonzero on the derived S¹ field OR exhibit a zero-parameter, OP/R2/P/PROMOTE-obstruction-free promotion, and (b) reproduce the Round PT's actual assignments with no free inputs. Otherwise SC-PT-2/1.

## Hash-before-read targets (shasum -a 256; confirm before reading)

- Round PT: `BCT_PeriodicTable_Round_v12_1.pdf`, `BCT_PeriodicTable_Round_Interactive*.html`, and the App PT source in the repo.
- Field-content anchors: the App(s) defining M = S¹ (App E.0 L_BCT; App J interior = one complex scalar S¹ — reconstructed `tex/BCT_Appendix_J_SphereAction.tex`).
- Cross-check digests (recompute locally; the repo is the source of record): Appendices Part1 `5656f763…`, Part2 `7a097464…`, Part3 `27f4c8b1…`, Monograph v21 `b057829…`, NPBS `03db3b10…`.

## Guards

- Do NOT accept "particles are knots / Hopf solitons" as evidence the Hopf charge is nonzero on the field: π₃(S¹) = 0 is a theorem, independent of the physical story.
- Do NOT let a promotion to S² enter through the back door (an assumed ℂ²/S² order parameter): PROMOTE requires it be DERIVED, and it was not.
- Do NOT treat "there are N periods / N shells" as a constraint (same class as KND §5.1's "there must be three sectors").
- Do NOT let a numeric coincidence (a geometric-alphabet number landing on a table entry) count as a foundation (FWD/MIX base-rate trap).
- Terminal-verify the homotopy facts (π₁(S¹)=ℤ, π₂(S¹)=0, π₃(S¹)=0; π₂/π₃(S²); H²(T³)=ℤ³) — cite standard results, don't assert from memory.

## Expected outcomes (all are findings)

- **SC-PT-1 (most likely):** the classifying charge is the Hopf invariant, identically 0 on M = S¹; no S¹-native invariant reproduces the assignments; a working version needs the closed promotion ⇒ the Round PT is **structurally void on the actual field**, and this is a corpus-wide correction (the Round PT and its downstream claims).
- **SC-PT-2:** a different S¹-native invariant (π₁ winding or the π₂ sheet charge) carries PART of the structure — deliver the exact survive/fail list of assignments.
- **SC-PT-3 (the prize):** a derived, zero-parameter, promotion-free topological foundation reproduces the Round PT assignments ⇒ triple-check under fresh brain, terminal-verified, before any tier movement.

## Standing note

The void-geometry numeric layer (α₀, r_oct, r_tet, ξ, percolating network, isotropic acoustic metric) is not the subject of this gate and is untouched regardless of outcome. Gate PT tests only whether the Round PT's topological classification has a foundation on the corpus's actual field content.
