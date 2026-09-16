# Strong-CP claim — correction inventory (repo-grounded worklist)

Companion to Gate THETA. Maps every place θ_QCD = 0 / d_n = 0 / "no axion" is asserted, and the fix each needs. **Now grounded in the live GitHub repo** (`zerofreeparameters-code/BCT-Programme`, cloned this session) — so the list is the *editable source files*, not just compiled PDFs. Verdict unchanged: SC-THETA-1 (θ_QCD = 0 imported / CONJECTURE).

## Two findings from the repo fetch

**(A) HIGHEST PRIORITY — `audit/PREREGISTRATION.md` pre-registers d_n = 0.** Lines 73–75 list "BCT value: **d_n = 0** (App DM; App HO4)"; line 120 calls "P-4 d_n = 0 … **the strongest entry**." This is exactly what Gate EDM ruled out. It already half-knows (lines 146–147 note the SM also predicts d_n below sensitivity, so a null is "weakly" confirming) — but still headlines d_n = 0. **Fix per EDM:** replace with the CONJECTURE-tier floor **d_n ≲ 10⁻³⁰ e·cm** (detection ≳ 10⁻²⁸ at n2EDM/TUCAN falsifies), pinned to one value, tiered CONJECTURE — *not* d_n = 0 exact.

**(B) Smoking gun — App HO4 (Phase 62B).** The programme's own geometric formula: **θ_QCD = r_tet/r_oct × α₀ = 4.04×10⁻³**, annotated *"or… 0?"* The geometry's natural output is *nonzero* and ~10⁸× over the bound (5×10⁻¹¹); θ = 0 was then selected to satisfy the bound. Direct evidence θ = 0 is imported/selected, not derived — the strongest single instance in the corpus. Log it in the THETA record.

## Correction to THETA sub-question 2 (my earlier error, corrected)

THETA RESULT said "π is neither addressed nor excluded." **Too strong — corrected.** App CE (and HN4) address it: the symmetry gives θ ∈ {0, π} and π is excluded by *observation* ("not observed in nature"), not by the symmetry. Accurate finding: **geometry narrows to {0, π}; observation selects 0** — so θ = 0 is not a pure geometric output even on the corpus's own reasoning. Cleaner, not weaker. SC-THETA-1 stands.

## Editable SOURCE files to correct (from the repo — this is the worklist)

| File (repo path) | What it carries | Fix |
|---|---|---|
| **`audit/PREREGISTRATION.md`** | d_n = 0 as "strongest entry" (finding A) | → CONJECTURE-tier floor d_n ≲ 10⁻³⁰; pin one value |
| **`tex/BCT_Monograph_PLB.tex`** | Monograph Part V three "proofs", §12.1 δθ, §13 d_n / no-axion, §9.3–9.4 | → tier→CONJECTURE; retract false δθ inequality; fix arg-det wording |
| **`tex/BCT_OneMedium_JournalEdition_v2.txt`** | "θ̄ = 0 exact", "d_n ≈ 10⁻³²", "no QCD axion exists" (public journal edition) | → CONJECTURE + honest floor |
| **`BCT_Volume1_Foundations.tex`** | strong-CP claim + cites Zenodo 18885628 (line 326) | → CONJECTURE; update cite context |
| **`BCT_Volume2_Electroweak.tex`** | strong-CP claim + cites 18885628 (line 290) | → CONJECTURE |
| **`BCT_Volume3_QCD.tex`** | strong-CP claim | → CONJECTURE |
| **`audit/APPENDIX_INDEX.md`** | index rows for CE, FZ, GT2, HN4, HO4, HR4, HX2 | → annotate tier once corrections land |

## Compiled-PDF appendices carrying the claim (source = the Vol bundles/compile scripts)

- **Vol 1** (bodies verified): **CE** (p385, Phase 18D, origin), **DI** (p460, "all loop orders" — false δθ + arg-det non-sequitur), **DM** (p471, d_n=0), **EU** (p574, EDM), **FZ** (p658, S₄ argument), **GT2** (p756, "no axion").
- **Vol 2** (FETCHED from repo `BCT_Appendices_Volume2_2026_compressed.zip`, bodies now read): **HN4** (Vol2 p44, Phase 62A — same "real masses ⇒ arg det = 0" non-sequitur; writes `arg(det M_q)=arg(m_u·…·m_t)=0` while also placing CP in off-diagonal CKM — incoherent), **HO4** (p54, Phase 62B — the θ=4.04e-3 "or 0?" note, finding B), **HR4** (p83, Phase 62 review), **HX2** (p136, Phase 53D — d_n=0, d_e~0; d_n^EW ~10⁻³² floor).
- **No per-appendix `.tex` exists for HN4/HX2** — they live only in the compiled Vol 2 PDF, so body corrections must go through whatever builds that bundle (a master doc / generation script), not a standalone source edit.

## Public / published (needs erratum or version note)

- **Zenodo 18885628** — standalone Letter "Geometric Resolution of the Strong CP Problem without an Axion". Cited from at least 7 repo files (Vol 1/2 .tex, Monograph_PLB, Letters 19/20/25/27). A live DOI asserting the claim → erratum or new version tiering it CONJECTURE.
- **pi2.institute** public pages (per ledger) — not in repo; correct directly.

## The single correction, stated once (reuse verbatim)

> BCT narrows θ_QCD to the CP-conserving fixed set {0, π} via the D4 Z₂ / T_d improper-rotation structure and selects θ = 0 by observation. This is a geometrically-motivated **conjecture** (parity / Nelson–Barr class), not a proven theorem: the load-bearing step — one T_d texture giving both arg det M_q = 0 and J_CKM ≠ 0 with radiative protection — is not constructed (written textures are real ⇒ J = 0; the CP phase is assigned to V_CKM separately; the geometry's own natural output, r_tet/r_oct·α₀ ≈ 4×10⁻³, is nonzero and was set aside). The neutron-EDM prediction is a CONJECTURE-tier floor d_n ≲ 10⁻³⁰ e·cm (detection ≳ 10⁻²⁸ falsifies), not d_n = 0 exact. "No QCD axion" inherits this tier. Retract the 1-loop line "δθ = 2.4×10⁻⁹ ≪ 10⁻¹⁰": the number is 13–49× *above* the quoted bound.
