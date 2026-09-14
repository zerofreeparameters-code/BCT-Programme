# GATE INT — WHICH INTERIOR DOES THE CORPUS HAVE?
## Cold Ledger deliverable · as-run

**Executing model:** Claude Opus 4.8 (`claude-opus-4-8`).
**Run date:** 14 September 2026.

---

## 0. DIGESTS (pre-registration honoured)

| artefact | SHA-256 | size | status |
|---|---|---|---|
| gate prompt `gate_INT_prompt.md` (hashed **before** reading) | `15e2094d0bfc02294eaa665f76ad03b08186a246534e3ad9e0245bbdbbd75ce7` | 7938 B | **MATCH** to pre-registered digest |
| corpus tarball `BCT-Programme@60bc92b` (pinned state) | `597f7f8152873c4b9af9ec6e50ac7963b29f140d4b9d176558c6117b23d12d61` | 45 674 182 B | recorded |

Both digests obtained by `curl`→`sha256sum` on disk, not from chat text. Pre-registration is therefore real (cf. §0.1: the repair "has been skipped twice").

---

## 1. SEARCH-SPACE COVERAGE (stated before any other number)

Every negative claim below ("no third interior", "corpus does not adjudicate") is made over **this** space.

**Repo corpus** `zerofreeparameters-code/BCT-Programme@60bc92b`:
- **134 `.tex`** — verified: **26 at tree root** + **108 in `tex/`**. The `tex/*.tex` glob (108) is *not* the corpus; all 26 root files were read/greppable. ✔ (arithmetic reproduced; §0.5's known error avoided.)
- **Appendices Vol.1** = 3 genuine PDFs (`file`→PDF v1.7), **425 + 425 + 25 = 875 pages**, extracted with **pymupdf** to 1.66 MB text. App I, App J, App K, App AT live here.
- **Appendices Vol.2** = `.zip` → one 18 MB PDF (`file`→PDF), **582 pages**, pymupdf → 1.05 MB text.

**Mount corpus** `/mnt/project/`:
- Every `.pdf` typed with `file`. **33 are ZIP archives** (per-page images + a per-page `.txt` layer), 16 are genuine PDFs, 2 are raw `data`. This matches §0.5 exactly (a prior gate wrongly called these unreadable from two extractor failures).
- All **33 ZIP-PDFs `unzip`-ed**; **33/33 carry text layers**, **387 text pages total**. Page-level coverage per doc recorded in `int_page_coverage.txt`. Two low-coverage caveats: **Round Periodic Table v12 = 1 text page**; **Monograph v21 = 57 pages but OCR text layer is sparse** on the interior sections. Conclusions about those two rest on what their text layers expose and are flagged where used.

Coverage gaps that bound the negatives: the Round-PT and Monograph OCR layers are partial, and the keyword footprint counts in §5 are proxies (verified by hand only for the named documents). No claim below depends on an unread region.

---

## 2. VERDICT (first)

**SC-INT-3 — both interiors are internally tenable as objects, and the corpus does NOT adjudicate between them. HALT and hand the decision to Michel.** The §7 consequence map is delivered for exactly this purpose.

There are **exactly two** interiors (not more → not SC-INT-4; not one-in-two-notations → not SC-INT-5; no explicit adjudication → not SC-INT-1).

**Qualification the stop conditions do not enumerate (recorded, not folded):** the two interiors are **not symmetric in provenance.** Interior A is genuinely *derived* (modulo its own still-open electron-mass problem). Interior B (App JH) is **asserted**, not derived: its stated derivation *from* App J is void, because App J's field cannot carry a Hopf charge (CN-INT-05), and its energy law is quantitatively wrong for a hopfion (CN-INT-07). This is a **tiering fact about Interior B**, and per SC-INT-2's own caution I do **not** present it as the corpus having chosen Interior A. It rides on top of the SC-INT-3 verdict; it does not change it, because Interior B remains a *coherent object* that productively underwrites a large downstream sector (the Round Periodic Table). A repair must still be a decision made by Michel, not by this gate.

---

## 3. STEP-0 TABLE — every interior field-content commitment in the corpus

| # | location (primary text) | field content | target / vacuum manifold + π₂,π₃ | normalisation | BC at r=R | tier in its own doc | date / DOI |
|---|---|---|---|---|---|---|---|
| **A** | **App I** §2.1 (Vol.1 p.104): "Ψ₁=ρ₁e^{iθ₁} [exterior], Ψ₂=ς₂e^{iφ₂} [interior]"; **App J** §1–2 (Vol.1 pp.113–118): "S[Ψ₂] is the same GP action as the exterior … derivative jump at r=R" | **Ψ₂ ∈ ℂ** (one complex component; dual-phase *pair* {Ψ₁,Ψ₂} each ℂ) | vacuum **S¹** (mexican-hat \|Ψ\|²−Ψ₀²); pair vacuum T²=S¹×S¹. **π₂=0, π₃=0** | **\|Ψ₂\|² dynamical** (soft (\|Ψ\|²−Ψ₀²)² term) | **derivative jump** [∂_rΨ]=−(σ_s/J)Ψ(R), Ψ continuous | App J: "S[Ψ₂]=same GP action **DERIVED**"; κ₀ **COMPUTED**; App I: structural | App I/J undated drafts inside compendium **zenodo.18885133** |
| **B** | **App JH** §JH.3.1 (all 4 tex variants): "Let Ψ₂: B³(R_s)→**ℂ²** … \|Ψ₂\|²=\|ψ₊\|²+\|ψ₋\|²=ρ₀ (constant bulk density) … Ψ̂₂ maps S³→S² … classified by π₃(S²)=ℤ" | **Ψ₂ ∈ ℂ²** (two complex components ψ₊,ψ₋) | target **S²** (=ℂP¹); **π₂(S²)=ℤ, π₃(S²)=ℤ** (Hopf) | **\|Ψ₂\|²=ρ₀ fixed** (constant bulk density) | derivative jump **+** Hopf-flux matching Eq.(JH hopf-matching) selecting **H=1** | "**Derivation**" (§JH.3 title); six results as derived | **March 2026**, **doi:zenodo.18975018** |

**No third interior.** Searched all 134 `.tex`, Vol.1 (875 pp), Vol.2 (582 pp), 33 mount ZIP-PDFs (387 pp): every `S³→S²` / hopfion / Hopf-charge / OHC commitment traces to the **App JH lineage** (JH ×4 variants; Letter 36-OHC; Letters 60, 69; App AG; Round PT; chemistry letters); every other interior reference is **Interior A**. → SC-INT-4 does not apply. (The four JH variants — `JH.tex`, `JH (1).tex`≡`JH_FINAL.tex`, `JH_GRRRRRRRR.tex` — differ only in a citation record number and title formatting; all assert the *same* ℂ²/S² content.)

**Symbol collision worth flagging.** "Two-component" is used in two incompatible senses: App I means the **dual-phase pair {Ψ₁ exterior, Ψ₂ interior}, each ℂ**; App JH means the **interior Ψ₂ *itself* ∈ ℂ²**. App JH takes App I/J's single-component interior symbol and silently promotes it to two internal complex components. App I's own mention of "S² topological objects" refers to the **geometric sphere surfaces r=R**, not an order-parameter target — it is not an Interior-B commitment.

---

## 4. THE SEPARATING INVARIANT (with computation)

Per §2 of the prompt, distinctness must be shown by an invariant notation cannot change, not by the documents disagreeing in words. Steelman of the null hypothesis ("one object, two notations", e.g. a component frozen): **it fails.**

**Invariant: π₃ of the order-parameter target manifold.**
- Interior A target **S¹**: universal cover ℝ (contractible) ⇒ **π_{n≥2}(S¹)=0**, so **π₃(S¹)=0**. Even the dual-phase *pair* has vacuum T² with **π₃(T²)=0**.
- Interior B target **S²**: **π₃(S²)=ℤ** (Hopf), generator η:S³→S² — the very integral App JH writes, H=1/16π²∫A∧dA.

A Hopf charge H is *by definition* an element of π₃(target). On S¹ it is **not definable** (π₃=0); on S² it is ℤ-valued. Freezing one component of ℂ² collapses the target to a point/S¹ and **destroys π₃** — you cannot recover a Hopf charge, so the two are not the same object re-notated. A secondary invariant agrees: **norm status** (dynamical for A vs fixed for B) is a physical, not notational, difference. → **SC-INT-5 does not apply.**

**Numeric confirmation that the shared number κ₀ is A's, not B's.** Re-solving App J's own eigenvalue equation κ·cot(κR) = −1/ξ + α₀ with α₀=0.00740806, ξ=1/√(8πα₀)=2.3175, R=0.5 (Planck units) reproduces App J's spectrum **exactly**: **κ₀=3.3905**, κ₁=9.5139, κ₂=15.7618. This is the *single-component Bessel* eigenvalue. App JH's ε₀=ℏ²κ₀²/(2mR²) reuses it for the ℂ²/S² hopfion — a different radial eigenproblem (CN-INT-06). Script: `int_separating_invariant.py`.

---

## 5. STEP-2 — DOES THE CORPUS ADJUDICATE? (findings)

- **Explicit supersession:** **none.** App JH frames itself as *extending* App J — "What Appendix J left open is the topology of Ψ₂" — not replacing its field content. No document states "JH replaces J §x" or the reverse.
- **Canonical marker / version field:** none preferring one interior. App JH has a DOI (zenodo.18975018) and a date (March 2026); App I/J carry no independent DOI (they sit inside compendium zenodo.18885133). `ZENODO_DOIS.md` is a **stale auto-registry: "Total records: 0" (2026-09-12)** — it adjudicates nothing.
- **Chronology — order or supersession?** **Order only.** App JH postdates and *cites* App J, yet **does not retract it**, and App I/J remain live in the current compendium. A later, DOI'd document that leaves the earlier interior in place and in downstream use is evidence of sequence, not of replacement.
- **Mutual acknowledgement:** **one-directional.** App JH cites App J; App I and App J do **not** mention App JH or hopfions (grep of Vol.1 for "hopfion/OHC/App JH" is empty).
- **Downstream usage (§3's decisive test):** **split and entangled — not "eleven vs none".**
  - *Interior-A machinery* (dual-phase modes; Higgs = (Ψ₁−Ψ₂)/√2 amplitude mode; m_e/m_P≈α₀^{21/2}): **App I, App J, App K, App AG (Higgs), App AT (Higgs), electron/proton-mass letters (19,28–31)**.
  - *Interior-B structure* (H∈ℤ classification): **App JH, Letter 36-OHC, Letters 60 & 69, Round Periodic Table v12, Volume 3/4 hopfion content, chemistry Letters 78–85**. The **Round PT axiom is literally Interior B**: "H∈ℤ: π₃(S²)=ℤ → Hopf charge integer-valued; |H|≤n per OHC mode → Pauli exclusion (L81)".
  - *Hybrid* (the tell): **App AG** *names* the interior "the OHC" (Interior B) but *computes* with **Bessel modes j₁,₁** (Interior A). Interior B's **vocabulary** propagated widely; Interior A's **equations** stayed underneath.
  - Keyword footprint (proxy, not per-doc adjudication): B-language **65–89 / 134** tex (depending on OHC match strictness); A-markers **21 / 134**. Both non-zero; neither interior is unused. Script `int_search_and_count.sh`.

**Conclusion of §5:** the corpus is **silent** on which interior is canonical, while **both** carry heavy, non-overlapping downstream load. → SC-INT-1 does not apply; SC-INT-3 does.

---

## 6. WHY THIS ISN'T SC-INT-2 (kept honest)

SC-INT-2 needs one interior **untenable / incapable of its own claimed results**. Interior A is internally consistent (its electron-mass mechanism is *open*, not *contradictory*). Interior B, taken as a **postulate** (Ψ₂∈ℂ², fixed norm, hopfion ground state), is a coherent physical object and it successfully underwrites the Round PT. So neither is globally untenable → not SC-INT-2. What *is* wrong with B is its **provenance and one energy law** (CN-INT-05, -07), which downgrade its **tier**, not its coherence. Recording that as a rider on SC-INT-3 (rather than reclassifying) follows the prompt's "if the outcome matches no stop condition, say so" clause.

---

## 7. CONSEQUENCE MAP — both columns filled

Each interior taken canonical **in turn**; what fails, by document/section.

| item | **If Interior A canonical** (ℂ, S¹, dynamical, jump-BC) | **If Interior B canonical** (ℂ², S², fixed, H=1) |
|---|---|---|
| **interior spectrum κ₀** | **SURVIVES.** κ₀=3.3905 is A's own Bessel eigenvalue (re-derived, §4). | **BREAKS as inherited.** 3.39 is the single-component result; B's ℂ²/S² radial problem is different. App J §2 does not transfer; B must re-derive its scale (CN-INT-06). |
| **App JH ε₀ & N_H=1** | **DIE.** π₃(S¹)=0 ⇒ H undefined ⇒ "H=1 ground state" meaningless; ε₀ loses its role. App JH §JH.3–4 fail. | **SURVIVE by construction**, but ε₀ carries the illegitimate κ₀, and E_H=H·ε₀ (linear) contradicts the hopfion bound E≳c\|H\|^{3/4} (CN-INT-07): quantitatively wrong even within B. |
| **Round Periodic Table axiom** | **DIES.** "H∈ℤ: π₃(S²)=ℤ; \|H\|≤n Pauli" has no referent on S¹. Round PT v12 (118-element Hopf classification), noble-gas closed multiplets, L81 Pauli theorem, L82 life-axis S_H=1, L83 d-anomalies (Cr,Mo,Cu,Ag,Au) lose their foundation. | **SURVIVES** — native to B; the strongest B payoff. |
| **App I two-component mode table** | **SURVIVES** — the dual-phase in-phase(Goldstone)/out-of-phase(Higgs) branch table is A-native. | **DIES/REINTERPRETED.** The θ₁,θ₂ independent-phase branches presume the {Ψ₁,Ψ₂} pair, not a single ℂ² fixed-norm S²-field. App I §2.2 fails as stated. |
| **Higgs identification** (App AG/AT: Higgs=(Ψ₁−Ψ₂)/√2 amplitude mode) | **SURVIVES** — dual-phase, A-native. | **DIES/REINTERPRETED.** Presupposes A's pair; under B the interior isn't that pair, so App AT §AT.1 / App AG Higgs must be rebuilt. |
| **published numeric prediction touching interior** | m_e/m_P≈α₀^{21/2} (App J, 2.4%): **SURVIVES** as A's (still unproven). Round-PT chemical assignments: **DIE**. | m_e≈α₀^{21/2} (built on A's Josephson g=α₀ single-component interior): **DIES / needs rebuild**. Round-PT chemical assignments: **SURVIVE**. |

**Net:** each choice kills a large, *different* sector. **A ⇒ the topological-chemistry sector dies; B ⇒ the mass/Higgs/dual-phase-mode sector dies.** This is precisely why a repair aimed at the wrong interior is wasted work, and why the choice is Michel's.

---

## 8. CN-INT NOTICES (tiered)

- **CN-INT-01 [PROVEN].** The corpus commits to exactly two mutually exclusive interiors: A (App I §2.1 / App J §1–2) Ψ₂∈ℂ, vacuum S¹, dynamical norm, derivative-jump BC, spectrum κ₀=3.3905 (re-derived); B (App JH §JH.3.1, all variants) Ψ₂∈ℂ², fixed norm, target S², H∈ℤ.
- **CN-INT-02 [PROVEN].** No third interior over the stated search space (134 tex / 875+582 PDF pp / 387 mount txt pp). Every S²/hopfion commitment is App JH-lineage; all else is Interior A. SC-INT-4 excluded.
- **CN-INT-03 [PROVEN].** Null hypothesis false: separating invariant π₃(target) = 0 (A) vs ℤ (B); norm status differs. SC-INT-5 excluded.
- **CN-INT-04 [PROVEN].** No explicit adjudication: no supersession statement; JH extends (not replaces) J; App I/J do not cite JH (one-directional); DOI registry empty/stale; chronology is order, not supersession — the later document neither retracts nor removes the earlier interior. SC-INT-1 excluded.
- **CN-INT-05 [PROVEN].** App JH's claim to *derive* B from App J's Ψ₂ is void: App J's Ψ₂ has target ℂ (π₃(S¹)=0) and cannot host a Hopf charge; JH substitutes Ψ₂∈ℂ². **Interior B's tier is ASSERTED, not DERIVED.** This is not the corpus choosing A.
- **CN-INT-06 [PROVEN].** App JH's ε₀=ℏ²κ₀²/(2mR²) reuses κ₀=3.3905, the single-component Bessel eigenvalue (App J §2), for a different (ℂ²/S²) radial problem — inheritance without justification.
- **CN-INT-07 [CONJECTURE].** App JH's E_H=H·ε₀ (linear in H) is inconsistent with the Vakulenko–Kapitanskii hopfion bound E≳c\|H\|^{3/4}; "quantisation from topology" is qualitatively motivated, quantitatively unsupported. *Tier CONJECTURE:* rests on an external theorem not re-derived in-session.
- **CN-INT-08 [PROVEN].** Downstream usage is split and entangled, not 11-vs-0: A-machinery in App I/J/K, AG-Higgs, AT-Higgs, mass letters; B-structure in App JH, L36-OHC, L60, L69, Round PT v12, Vol3/4, chemistry L78–85. **App AG is a hybrid** (names "OHC", computes Bessel j₁,₁). Footprint proxy: B-language 65–89/134, A-markers 21/134 (named docs verified by hand; counts are keyword proxies).
- **CN-INT-09 [PROVEN].** Consequence map §7: A-canonical kills Round-PT topological chemistry (L81/L82/L83 + 118-element Hopf scheme), App JH, L36-OHC/60/69; B-canonical kills App I §2.2 mode table, App AG/AT Higgs identification, App J's m_e≈α₀^{21/2} and κ₀-transfer. Each clause is individually evidenced above; no "unaffected" clause is asserted without its own evidence.

---

## 9. §0.6 REPRODUCED VERBATIM

> Adjudicating the interior does **not** validate either appendix, repair the mass sector, or
> supply a graviton. Gate Ψ2 closed the second-A₁g question and Gate Λ found the mass coupling
> unwritten; neither turns on which interior wins. **What this gate buys is the right to write a
> repair that is aimed at the object the corpus actually contains**, and the unblocking of
> Gate PT, which was assessed against a field content the corpus may not uniquely have. A verdict
> here is a precondition for other work, not a result about physics.

---

## 10. WHAT THIS GATE DID **NOT** ESTABLISH

- It did **not** choose the interior. SC-INT-3: the choice is handed to Michel.
- It did **not** validate either appendix, repair the mass sector, or supply a graviton (§0.6).
- It did **not** prove Interior B *false* — B is a coherent postulate; only its *derivation from J* and its *linear energy law* fail (CN-INT-05/07). Equally it did **not** find Interior A false: A survives this gate.
- It did **not** re-verify the Round-PT chemistry, the m_e≈α₀^{21/2} numerics beyond App J's own 2.4%, or the Monograph's interior stance (OCR text layer too sparse — coverage caveat, §1).
- It did **not** inherit CN-Ψ2-* or CN-Λ-* notices; §4's κ₀ and the homotopy facts were re-derived at primary source in-session (§0.3). Anything not re-derivable was dropped.

---

## 11. CONTAMINATION STATEMENT

- **Quarantine honoured:** no `conversation_search`, no `recent_chats`; did **not** read `audit/notes/`, any `audit/gates/*/` deliverable, `audit/NEXT.md`, or `audit/gates/INT/README_MISSING.md`. Did not consult 9–11 Sep commissioning threads or BCT-X / Sandbox TOP. Did not read the project memory files.
- **Auto-load disclosure (per §0.2).** The session's memory system auto-injected a *listing* (one-line descriptions only, not file bodies) that included prior-gate summary lines: `gate-link.md` ("verdict SC-LINK-2"), `gate-mad.md` ("verdict SC-MAD-1"), `gates-rank-mp-pred.md` (described as carrying a "field-content … verdict"), and `audit-findings.md`/`overview.md` (Cold-Ledger state). **I read none of these files' contents.** The `gates-rank-mp-pred` description is topically adjacent to this gate (field content); I did not open it and used nothing from it. Every finding here was re-derived from the pinned corpus. If any of those one-line descriptions constitutes disallowed inheritance, this notice is the declaration §0.2 requires.
- **Corpus provenance:** all conclusions rest on `BCT-Programme@60bc92b` (tarball `597f7f81…d12d61`) and the typed mount, nothing else.

---

## 12. SCRIPTS (in this directory)

- `int_separating_invariant.py` — homotopy/component invariant + re-derivation of κ₀=3.3905 (needs numpy, scipy).
- `int_search_and_count.sh` — search-space arithmetic + A/B footprint + App-AG hybrid check (run from repo root).
- `int_page_coverage.txt` — per-doc text-page coverage for the 33 mount ZIP-PDFs.
- `gate_INT_prompt_asrun.md` — the pre-registered prompt as executed.
