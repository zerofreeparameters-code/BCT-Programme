# GATE YM2 — IS THE FINITE-LATTICE MASS GAP PROVEN?
## Cold Ledger deliverable

**Executing model:** Claude Opus 4.8 (`claude-opus-4-8`), web/app chat surface.
**Date:** 14 September 2026.

---

## 0 — DIGESTS (handoff)

| Object | SHA-256 | Size | Status |
|---|---|---|---|
| Gate prompt (pre-registered) | `ada82fc1969fc1a2eb14d0bf5aeea60fe992b2413470b10a88495f1dadb5c922` | 7313 B | — |
| Gate prompt (computed on disk) | `ada82fc1969fc1a2eb14d0bf5aeea60fe992b2413470b10a88495f1dadb5c922` | 7313 B | **MATCH → proceeded** |
| Corpus tarball @ `12ae196` (computed) | `1b5924484b84aef2bb8253183f02d2ef8142ce64aa57fbccf70aa6455b8a43cc` | 45,712,225 B | **pinned corpus state** |

No refusal. The prompt was received as a file at a commit-pinned `raw.githubusercontent.com`
URL and hashed before reading.

---

## 1 — SEARCH-SPACE COVERAGE (before any other number)

- **`.tex` files:** 135 total (109 under `tex/`, 26 at tree root). The prompt states 134/26.
  The tree-root count matches; the total is **off by one (135 vs 134)** — recorded as a
  search-space discrepancy, immaterial to the verdict.
- **JH4 itself — every reachable version:**
  1. **Repo copy** — `tex/BCT_Appendix_JH4_YangMills_v2_CORRECTED.tex` (9,471 B, 185 lines).
     The only JH4 file in the corpus. **Read in full.**
  2. **Public Zenodo deposition** `10.5281/zenodo.21781545`. **Could not be loaded**
     (see §7 coverage limit). Its metadata is taken from the repo's own `ZENODO_DOIS.md`.
  3. **Appendix volumes** (Vol 1 Parts 1–3 = genuine PDFs, 425+425+25 pp; Vol 2 = a `.zip`
     holding an 18 MB, 582 pp PDF — all typed with `file`, read with pymupdf). **No standalone
     JH4 copy** lives in the volumes; they discuss the Yang–Mills mass gap in prose (Vol 2
     §§2.4, and the benchmark tables) and tier it — see §3 consistency finding.
- **JH-family siblings are a different appendix.** `BCT_Appendix_JH.tex`, `…JH (1).tex`,
  `…JH_FINAL.tex`, `…JH_GRRRRRRRR.tex` are all *"Partially Dual Variables in SU(2)
  Yang–Mills Theory"* — **not** JH4 (SU(3), Clay-problem) drafts. They are not version
  history for this gate.
- **JH4 string also appears in** `ZENODO_DOIS.md` (used) and in `audit/gates/LINK/` and
  `audit/gates/C1/` deliverables (**not opened** — quarantine).

Coverage is complete except for the live Zenodo page (§7).

---

## 2 — VERDICT (first)

**Primary verdict — SC-YM2-4 (reported first, as the prompt requires).**
The versions disagree about what is claimed, and **the public record overstates the current
version.** The current internal appendix (repo v2, 27 Jul 2026) and the current appendix
volumes (Vol 2, Jul 2026) both **disclaim** a Clay-sense proof; the public-facing DOI
`10.5281/zenodo.21781545` (dated 2026-08-03, i.e. *after* the correction) is titled
*"Yang–Mills Existence and Mass Gap — **Complete Proof** from BCT D4."* This is a matter of
the public record, not of mathematics, and it is the first thing this gate reports.
*(Rests on the repo's own DOI table; the live record could not be loaded — §7.)*

**Secondary verdict — SC-YM2-2 (the mathematics of the current version, v2).**
- **(b) the spectral gap at every fixed spacing is essentially PROVEN** — but by the standard
  transfer-matrix + Perron–Frobenius/Jentzsch route, which JH4 correctly invokes. JH4's
  *additional* justification via "a convergent cluster expansion because u = 0.624 < 1" is
  **not** rigorous (u < 1 is not a cluster-expansion convergence criterion), yet the gap at
  fixed *a* does not need it. **(b) survives.**
- **(a) "satisfies the OS axioms at every lattice spacing" is only PARTIAL.** Exactly one OS
  axiom — **OS3 reflection positivity** — genuinely holds at finite spacing and is all the
  construction needs. **OS2 Euclidean invariance is claimed beyond its scope** (a fixed
  lattice has only the discrete point group, not E(4)); **OS0 analyticity is asserted via a
  category error** (a lattice theta/eta modular form, which is not the gauge partition
  function); OS1/OS4 are not addressed (OS4 is implied by the gap). **The gap survives the
  removal of the overstated axioms**, because it rests on OS3 + Perron–Frobenius alone.

**Net:** the *minimal, correctly stated* finite-lattice result — *a fixed-coupling SU(3)
Wilson theory on the D4 lattice is reflection-positive and has a positive transfer-matrix gap
at every finite spacing* — **is sound and is real (if standard) mathematical physics.** JH4
v2's own tier line (finite-lattice **PROVEN** / continuum **OPEN**) is defensible for the
gap and for existence; its "**satisfies the OS axioms**" clause overstates by naming axioms
(OS0, OS2) it does not establish. The continuum limit is correctly marked **OPEN** and is not
in dispute.

---

## 3 — STEP 0: WHAT IS CLAIMED, BY WHICH VERSION

| Version | Date | Title | Abstract/claim | Tier statement |
|---|---|---|---|---|
| **JH4 v1** | 13 Mar 2026 | *Appendix JH4 (v1): Yang–Mills Existence and Mass Gap* | Presented as **a complete proof of the Clay Millennium Problem** (per v2's Notice of Correction, quoting it). Not present as a file in the corpus. | (complete existence + mass gap) |
| **JH4 v2** (repo copy; public record?) | authored 13 Mar 2026, **correction issued 27 Jul 2026** | *Appendix JH4 (v2): A Geometrically-Fixed Lattice Gauge Theory for the D4-Superfluid Vacuum — **Scope Corrected*** | Finite-lattice existence + gap proven at every fixed spacing; **rigorous continuum limit NOT proven**; "not a solution to the Millennium Problem." | **Finite-lattice: PROVEN. Continuum: OPEN.** Clay problem "remains unsolved by this appendix." |
| **Public Zenodo DOI** `10.5281/zenodo.21781545` | **2026-08-03** (per `ZENODO_DOIS.md`) | *BCT Appendix JH4: Yang–Mills Existence and Mass Gap — **Complete Proof** from BCT D4* | (title asserts a complete proof) | — (could not load live record) |
| **Appendix Vol 2** | Jul 2026 | (prose, §2.4 + benchmark tables) | Quark-confinement/YM listed **"Conjectured (Clay Millennium Problem)"** (p451); YM mass gap is *"a physical derivation, **not** a mathematical proof in the Clay sense"* (p551). | consistent with v2 (not a Clay proof) |

**Which is the public record?** The one a reader following the DOI receives is the Zenodo
deposition. Per the programme's own DOI table it carries the **"Complete Proof"** title dated
**after** the 27 Jul correction. **The public record does not match the most recent version.**
It also does not match the current appendix volumes, which tier the same result as conjectural.
This is the SC-YM2-4 finding.

---

## 4 — STEP 1: OS AXIOMS, AXIOM BY AXIOM

JH4 v2 uses a non-standard OS numbering; mapped here to the prompt's standard OS0–OS4.

| Standard axiom | What JH4 does | Does the cited tool cover *this* case? | Tier |
|---|---|---|---|
| **OS0 analyticity** | Asserts it "holds because `Z_BCT = Θ_{D4}(τ)/η(τ)^8` is a modular form, hence analytic." | **No — category error.** `Θ_{D4}/η^8` is the number-theoretic partition function of the D4 lattice (a free-field/CFT object), **not** the SU(3) Wilson gauge partition function `Z=∫∏dU e^{-S_W}`. Modularity of the former says nothing about analyticity of the gauge Schwinger functions. (The *true* finite-lattice statement — correlators are finite integrals of analytic integrands — is trivial but is **not** the argument made.) | **ASSERTED** (invalid justification) |
| **OS1 regularity** | Not addressed. | Trivial for a finite lattice (bounded correlators), but not stated. | not addressed |
| **OS2 Euclidean invariance** | Claims it "holds by the isotropy of the 24 equal-length D4 roots." | **No.** On a fixed lattice the symmetry group is the discrete point group (Aut(D4) ≅ Weyl(F4), order 1152), **not** the continuous Euclidean group E(4). Root isotropy gives the point group, not rotational invariance. **Full Euclidean invariance is a continuum-limit statement only** — exactly the case the prompt flags. Claimed **beyond its scope.** | **ASSERTED / incorrect at finite a** |
| **OS3 reflection positivity** | Osterwalder–Seiler criterion; justified by "D4 self-duality (D4*=D4) makes time-reflection a symmetry." | **Conclusion yes, stated reason no.** Osterwalder–Seiler (1978) does give RP for the Wilson action on a lattice **with a reflection-hyperplane symmetry** — which D4 possesses. But **self-duality ≠ reflection symmetry**; the stated justification is a non-sequitur. The correct property (a reflection plane + link/site-reflection split of the action) is available, so the conclusion stands. | **PROVEN (conclusion); flawed derivation** |
| **OS4 ergodicity/clustering** | Not addressed. | Follows from unique vacuum + spectral gap (item 5), so implied, not stated. | implied |
| *"gauge invariance = OS3"* | Item labelled "OS3 gauge invariance holds by construction." | Gauge invariance is **not** one of the five OS axioms; true of the Wilson action but mislabelled. | mislabel |

**Reconstruction framing.** Item 4 invokes "the Osterwalder–Schrader reconstruction theorem"
to obtain `H ≥ 0`, vacuum, Hilbert space. The full OS reconstruction of a *relativistic*
theory requires OS2. At finite spacing the correct tool is the **Osterwalder–Seiler
transfer-matrix reconstruction from RP alone**, which yields `H ≥ 0`, a vacuum and a gap
without Euclidean invariance. The *conclusion* is right via the correct tool; the *named*
tool is over-powered. This is why (a) can be "partial" while (b) still stands.

---

## 5 — STEP 2: THE SPECTRAL GAP, RECOMPUTED

JH4 item 5: `δ_latt = -a^{-1} ln(λ1/λ0) > 0` at every fixed `a`, "via a convergent cluster
expansion at `g²=π⁵/24` (expansion parameter `u = e^{-144/π⁵} ≈ 0.624 < 1`)."

Recomputed (`gate_YM2_numerics.py`, mpmath, 40 dp):

| Quantity | JH4 | Recomputed | |
|---|---|---|---|
| `π⁵` | — | 306.019684785 | |
| `g² = π⁵/24` | 12.750820… | **12.7508201994** | MATCH |
| implied `S_D4 = π⁵/6` | (via `g²=S_D4/4`) | 51.0032807975 | |
| `β = 6/g² = 144/π⁵` | — | **0.4705579646** | |
| `u = e^{-144/π⁵}` | ~0.624 | **0.624653636** | MATCH |
| `-ln(u) = β` | — | 0.4705579646 | a-independent at fixed g² |

**Mechanism.**
1. **Existence of a gap at each fixed `a` is sound and does not need the cluster expansion.**
   For a finite lattice with compact gauge group, the transfer matrix is a positive integral
   operator with a strictly positive continuous kernel; Perron–Frobenius/**Jentzsch** (which
   JH4 correctly cites) gives a simple largest eigenvalue strictly above the rest, hence
   `λ1/λ0 < 1` and `δ_latt > 0`. **This is the real content of (b), and it holds.**
2. **The cluster-expansion justification as stated is not rigorous.** "`u = 0.624 < 1`" is
   **not** a cluster/polymer-expansion convergence criterion. Convergence (Kotecký–Preiss /
   Dobrushin) requires activity × a geometric connectivity factor `μ ≫ 1` to be below a
   threshold *strictly less* than 1; the number of size-`n` plaquette polymers through a fixed
   plaquette in 4D grows like `μ^n`. `β = 0.47` is deep strong coupling and **plausibly**
   inside the true strong-coupling analyticity domain (Osterwalder–Seiler prove convergence
   for `β` small), but **JH4 does not establish this** — it substitutes `u<1` for the actual
   criterion. **Premise carried without proof.**
3. **Uniformity in `a`.** Because `u = e^{-β}` with `β` **fixed**, `-ln(λ1/λ0) ≈ β` is
   **a-independent**, so `δ_latt ∝ a^{-1}` would **diverge** as `a→0`. The gap is therefore
   **not** uniform toward the continuum at fixed coupling — which is expected and is precisely
   why the continuum limit is a separate, open problem. JH4 v2 does not claim uniformity.

**Corroboration (external, opened).** An independent honest treatment of *this same problem*
(De Ceuster, Zenodo `10.5281/zenodo.16858240`, Aug 2025) constructs the lattice transfer
matrix, proves reflection positivity and a **positive spectral gap in the strong-coupling
regime on finite lattices**, and isolates the *single* remaining leap as "a **uniform lower
bound on the lattice mass gap along a renormalisation trajectory** reaching a continuum limit
that satisfies the OS axioms." This is the identical division of labour: finite-lattice gap =
standard/achievable; uniform-in-`a` continuum bound = the open problem.

---

## 6 — STEP 3: THE COUPLING

`g² = π⁵/24` is stated as `S_D4/4`, "the action of an SU(3) instanton traversing the six
positive roots of the A2 ⊂ D4 subsystem," implying `S_D4 = π⁵/6 = 51.003…`.

- **Derived or chosen (within JH4)?** **Asserted with a one-line geometric story; not derived
  in this appendix.** The value `π⁵/6` does recur in the corpus as a *topological entropy /
  action of the D4 lattice* (Vol 2 p550: `S_QCD = π⁵/6 × (1−r_tet+α₀/2)` for the strong-CP
  problem), so it has provenance elsewhere, but its first-principles derivation is **not**
  shown in JH4. Tier within-appendix: **ASSERTED (provenance out-of-appendix).**
- **One coupling or a range?** JH4 is explicit: the construction is at the **single bare value**
  `g²(a=ℓ_P) = π⁵/24`, a single-point calculation, **not** a renormalisation trajectory
  `g(a)`. The dimensional-transmutation line `Λ_QCD = m_P exp[-g²/(1-x)] = 220 MeV` is a
  one-point evaluation, not a flow. *(The corpus elsewhere carries a dressed form
  `S=(π⁵/24)/(1−4α_s/π)` — Vol 1 Part 1 p317 — hinting a running coupling exists outside JH4,
  but JH4's finite-lattice object is the fixed bare value.)*
- **Verdict on §4's question:** JH4 has **a theory at one fixed coupling**, and says so. This
  is consistent with (b) (gap at each fixed `a`) and is exactly why the continuum limit — which
  needs a trajectory — is open.

---

## 7 — CN-YM2 NOTICES (tiered)

Revised clause by clause.

- **CN-YM2-01 — public-record overstatement.** *PROVEN (documentary):* the repo v2 text
  disclaims a Clay proof while `ZENODO_DOIS.md` records the public DOI `…21781545`
  (2026-08-03) as *"…Complete Proof from BCT D4."* *CONJECTURE (pending live load):* that the
  live Zenodo page currently *serves* the overclaiming version. **Action implied:** the public
  deposition title should be brought into line with v2 and Vol 2.
- **CN-YM2-02 — finite-lattice existence.** The Wilson partition function is a well-defined
  probability measure on `SU(3)^|Λ|` (compact group, bounded action). **PROVEN.**
- **CN-YM2-03 — reflection positivity.** RP holds for the Wilson action on D4 via
  Osterwalder–Seiler. **PROVEN (conclusion).** Stated justification via self-duality is a
  non-sequitur — **ASSERTED (derivation)**; the needed reflection-plane property is available.
- **CN-YM2-04 — positive gap at fixed `a`.** `δ_latt > 0` at every fixed spacing via strict
  positivity of the transfer matrix (Perron–Frobenius/Jentzsch). **PROVEN.**
- **CN-YM2-05 — cluster-expansion convergence.** "Converges because `u≈0.624<1`." **ASSERTED**
  — `u<1` is not the Kotecký–Preiss/Dobrushin criterion. Does not sink CN-YM2-04.
- **CN-YM2-06 — OS0 analyticity via modular form.** Rests on a category error
  (`Θ_{D4}/η^8` ≠ gauge `Z`). **ASSERTED (invalid).**
- **CN-YM2-07 — OS2 Euclidean invariance at finite `a`.** Only the discrete point group holds;
  full E(4) invariance is a continuum statement. Claimed beyond scope. **ASSERTED/incorrect.**
  The gap survives its removal.
- **CN-YM2-08 — "OS reconstruction theorem" framing.** Over-powered name; correct tool is the
  Osterwalder–Seiler transfer-matrix reconstruction from RP. Conclusion correct. **ASSERTED
  (framing).**
- **CN-YM2-09 — coupling `g²=π⁵/24`.** Single fixed coupling. **PROVEN (documentary)** that it
  is single-coupling; value derivation **ASSERTED (out-of-appendix provenance).**
- **CN-YM2-10 — continuum limit.** Correctly marked **OPEN** by v2; not claimed. **CONJECTURE
  / OPEN**, consistent.

---

## 8 — SCRIPTS

- `gate_YM2_numerics.py` — coupling, `β`, `u`, and the a-dependence of the gap (mpmath, 40 dp).
- `gate_YM2_corpus_scan.py` — `.tex` counts, JH4/JH-family location, appendix-volume tiering scan.
- `gate_YM2_prompt_asrun.md` — as-run prompt with recorded digests + verbatim gate text.

---

## 9 — EXTERNAL CITATIONS (each actually opened this session)

- **K. Osterwalder & E. Seiler**, *Gauge field theories on a lattice*, Ann. Physics **110**
  (1978) 440–471 — the reference for Wilson-action reflection positivity and the finite-lattice
  transfer-matrix framework JH4 relies on. (Seen in the reference lists of the lattice-YM
  papers opened via search: arXiv:2511.07297, arXiv:1907.05549.)
- **A. Jaffe & E. Witten**, *Quantum Yang–Mills theory*, in *The Millennium Prize Problems*,
  Clay Math. Inst. (2006), pp. 129–152 — official statement: a non-trivial theory on **ℝ⁴**
  with OS-strength axioms and a mass gap. Confirms the finite-lattice result is not the prize.
- **P. De Ceuster**, *Yang–Mills Existence and Mass Gap in Four Dimensions: hints and clues*,
  Zenodo `10.5281/zenodo.16858240` (13 Aug 2025) — **fetched in full (landing page + abstract)**;
  independent corroboration that the finite-lattice strong-coupling gap is the standard part and
  the uniform-in-`a` continuum bound is the open conjecture.
- Balaban's RG programme (Commun. Math. Phys. **119** (1988) 243; **122** (1989) 175) — cited
  by JH4 and named by the field as substantial-but-incomplete; **not opened directly** this
  session (cited here only as JH4 cites it and as the secondary literature characterises it).

---

## 10 — CONTAMINATION STATEMENT

- **No** `conversation_search`, **no** `recent_chats`.
- **Did not open** `audit/notes/`, any `audit/gates/*/` deliverable, or any other gate prompt.
  Their existence and the fact that JH4 is *mentioned* in the LINK and C1 deliverables were seen
  via `find`/`grep -l` (paths only); contents were not read.
- **Cold Ledger auto-load:** the session context carries a memory *listing* of one-line file
  summaries. I **saw** these one-line summaries but **did not open** any file. The summaries
  visible included prior-gate files (MAD, LINK, RANK/MP/PRED), an `audit-findings` file
  ("Cold Ledger audit results — closed sectors… active correction ledger… open problems"),
  and BCT overview/ways-of-working files. **None of these one-line summaries names JH4, YM2,
  the finite-lattice gap, or the OS-axiom question.** No prior finding about JH4, its tier, or
  its version history reached me. **My assessment of JH4 was formed from the primary files and
  preceded (and is independent of) anything in those summaries.**
- **Inheritance:** none. JH4 was assessed on its own mathematics.

---

## 11 — §0.6, REPRODUCED VERBATIM

> A sound finite-lattice existence-and-gap result is **real mathematical physics** and is worth
> having on its own terms. It is **not** the Clay Millennium Problem, which requires a continuum
> measure on ℝ⁴ and a non-perturbative control of a → 0 that has resisted proof for seventy years.
> **Gate YM2 can confirm or refute the finite-lattice claim only.** A favourable verdict does not
> solve Yang–Mills, does not earn a prize, and must not be reported as if it did. An unfavourable
> one does not show the construction is worthless — it locates where the argument stops.

---

## 12 — WHAT THIS GATE DID NOT ESTABLISH

- It did **not** load the live Zenodo record `10.5281/zenodo.21781545`; the public-record
  overstatement (CN-YM2-01) rests on the repo's own `ZENODO_DOIS.md` table. A direct fetch is
  the one open coverage item.
- It did **not** re-derive `g²=π⁵/24 = S_D4/4` from first principles (the derivation is not in
  JH4; its provenance is elsewhere in the corpus).
- It did **not** determine the exact strong-coupling radius of convergence for SU(3) on the D4
  lattice, only that JH4's stated criterion (`u<1`) is not the correct one and that `β=0.47` is
  plausibly, but not provenly, inside the true domain.
- It did **not** assess the continuum limit — correctly OPEN, and out of scope by §0.6.
- It made **no** judgement on the wider BCT programme; scope was JH4's finite-lattice claim and
  its version history only.
