# Gate PILOT — Can anything BCT has written carry Bell correlations?

**Programme:** The BCT Superfluid Lattice Model (ZeroFreeParameters, ORCID 0009-0007-9561-9859)
**Pre-registered:** 2026-10-06 (Barrys Reef, AEDT)
**Protocol:** Cold Ledger, single-gate thread, fresh context. Hash-before-read. URL not paste.
**Tier cap:** none (fresh thread). Same-session re-runs are capped at CONJECTURE.
**Corpus pin:** repo tree at commit `0305526015460b2c90d6cbcb6ca9d0e56d82f64e` (HEAD, 2026-10-05), `audit/` excluded. Primary sources only.
**Scorecard status:** structure gate on the quantum sector. A kill moves no prediction. Notices **CN-PILOT-01** onward.

---

## 0. Why this gate exists

Two things have never been asked of the corpus.

**(a) Which dynamical law is BCT's?** The card author observed (to be re-verified in Step 1, not trusted) that the corpus writes two different laws for the same field. One is first order in time (Schrödinger type). The other is second order in time (wave type). They differ in exactly the property the nonlocality question turns on. A second-order wave equation has a strict maximum speed. A first-order Schrödinger-type equation has none in the continuum, and on a lattice has a finite maximum that is not the sound speed. "A superfluid is instantaneous" is true or false depending on which law is meant.

**(b) What is the pilot-wave reading of BCT?** There are two standard ones. **Reading P:** particles are the beables, guided by a wave on configuration space (de Broglie–Bohm). **Reading F:** the field configuration is the beable, guided by a wave functional (Bohm 1952 II; Valentini; Struyve). Neither has been tested against BCT's written field content.

---

## 1. The question (verbatim, do not paraphrase in the deliverable)

> On the field content and dynamics the BCT corpus actually writes, is there any channel that propagates faster than the model's own c, and can any structure built from the written field content alone carry correlations between two separated defects that violate the CHSH inequality, independent of their separation, without permitting signalling?

Three sub-questions, each answered with a citation, a computation, or NONE FOUND:

1. **Dynamical law.** For every action or equation of motion the corpus writes for the vacuum field: its order in time, its dispersion relation, its maximum group velocity and its front velocity, in the continuum and on the lattice. Does any primary source choose between them?
2. **Carrier.** For every faster-than-c channel found in (1), and for every entanglement mechanism the corpus states, apply tests T1–T5 of §3.
3. **Pilot-wave reading.** Is Reading P or Reading F consistent with the written field content? What does each add that the corpus does not write? Does the lattice geometry fix any quantity that standard pilot-wave theory leaves free?

---

## 2. Success criteria (pre-committed; choose exactly one primary verdict)

- **SC-PILOT-1 (SURVIVOR).** Either (i) a construction using only the written field and written dynamics, with no wave functional, no added field and no added coupling, passes T1–T4 by explicit proof or simulation; or (ii) a pilot-wave reading in which the lattice geometry fixes a quantity that standard pilot-wave theory leaves free, that quantity is measurable in principle, and its closed form is written down before any comparison with data.
- **SC-PILOT-2 (KILL — no carrier).** Nothing written passes T1–T4. State the sub-code: **2a** nothing travels faster than c on the governing law; **2b** a faster channel exists but fails T2, T3 or T5; **2c** the field cannot hold a joint state for N parties (T4, counting).
- **SC-PILOT-3 (IMPORT).** Bell violation is obtainable only by adding a wave or wave functional on configuration space, that is, standard pilot-wave theory applied to a lattice scalar. The lattice supplies a preferred frame and a cutoff; nothing is derived from geometry.
- **SC-PILOT-4 (UNDETERMINED).** The corpus does not choose between the dynamical laws AND the primary verdict differs between them. Report every branch in full and state exactly what must be decided.

**Honest prior, stated before the run:** SC-PILOT-3, with 2b or 2c on the no-added-structure branch. Reasons: Bell's theorem excludes any mechanism in which each wing's outcome depends only on local field values and the local setting; a field on a 3D lattice has one value per site while an N-party state needs a function on the N-fold product; a mean-field condensate is a product state. Where a positive could come from: the lattice gives pilot-wave field theory its preferred frame and its regulator for free (Reading F), and a finite lattice maximum speed is a hard number that experiment can exclude or not (T5).

---

## 3. The tests

A candidate carrier is any written structure claimed or able to link two defects A and B separated by L ≫ ξ.

- **T1 — CHSH.** S > 2, reaching 2√2, with each wing's setting chosen freely after the pair has separated. The candidate must exhibit the term in the written equations by which the setting at B enters the outcome at A.
- **T2 — No signalling.** The outcome statistics at A are independent of the setting at B.
- **T3 — Distance independence.** The correlation strength does not fall with L.
- **T4 — Three parties.** The Mermin value reaches 4 (local bound 2) for a three-defect GHZ configuration. State the number of real functions the field supplies and the number the state requires.
- **T5 — Speed.** If the carrier has a finite maximum speed v_max in the lattice frame, report v_max/c. Apply the finite-speed theorem of Bancal et al. and the experimental lower bound of Salart et al., stating exactly what frame assumption that bound carries.

---

## 4. Method (required steps, in order)

1. **Hash before read.** Fetch this file by its commit-pinned raw.githubusercontent.com URL to disk. Compute SHA-256. Compare with `audit/gates/PREREG_20261006.sha256`. Open only on match. Record both digests.
2. **Inventory of written dynamics.** Clone the repo (HTTPS, read-only) at the pinned commit. Search every `.tex` and every Volume PDF text layer for, at minimum: `partial_t`, `\dot`, `i\hbar`, `partial_\mu`, `\Box`, `Bogoliubov`, `dispersion`, `omega(k)`, `group velocity`, `phase velocity`, `superlumin`, `v_{\rm ph}`, `healing`. Tabulate every distinct action or equation of motion: source, equation label, order in time, stated symmetries. Minimum reading list, not exhaustive: `tex/BCT_Appendix_AZ6.tex`, `tex/BCT_Appendix_J_SphereAction.tex`, `tex/BCT_Letter27_GPAxiom.tex`, `tex/BCT_Letter64.tex`.
3. **Dispersion, computed cold.** Re-derive ξ/a from r_oct and r_tet. For each distinct law in the table, linearise about the uniform ground state and give ω(k) in the continuum. Then put it on the 12-neighbour lattice at c/a = √2 with the nearest-neighbour graph Laplacian, normalised to reproduce the continuum operator as k→0. Report max|∇ₖω| over the Brillouin zone in units of the k→0 sound speed, the k at which it occurs, and the front velocity (strict, or tails outside the cone and their decay law). State the convention relating ξ to the coupling; if sources differ, compute each. mpmath 60 dps working, 40 reported for closed forms; numerical maxima to at least 10 digits.
4. **Corpus search for the quantum-sector claims.** Search for: `entangle`, `Bell`, `CHSH`, `Tsirelson`, `nonlocal`, `non-local`, `pilot`, `Bohm`, `de Broglie`, `hidden variable`, `configuration space`, `Born`, `collapse`, `superposition`, `wave functional`, `Fock`, `second quantis`. Report hit counts per term; a term absent everywhere is a finding. Read every hit in context. For each mechanism, name the object that is claimed to carry the joint state and the equation that governs it.
5. **Apply T1–T5** to each candidate carrier from Steps 3 and 4.
6. **Pilot-wave readings.** For P and for F, write the guidance equation explicitly on BCT's variables. State the beable, the wave, the space the wave lives on and its dimension for N defects and for N_s sites. For P: check a vortex-core beable against the fact that the condensate density vanishes at the core, and derive the order in time of a defect's equation of motion under each law from Step 2. For F: state whether any primary source writes the wave functional or the quantisation; if none does, it is added structure. List every quantity each reading leaves free and test whether r_oct, r_tet, ξ/a or the lattice fixes it. Any dimensionful result inherits the assumption a = ℓ_P; say so.
7. **One-sentence kill.** State the single sentence that, if true, closes the gate at SC-PILOT-2 or -3, and say whether it is true.
8. **Cost statement.** State exactly what must be added to the written theory to obtain Bell-violating correlations, what it costs in free inputs, and what it does to the phonon identification c_s = c.

---

## 5. Guards against false positives

- A **phase velocity** above c is not a channel. Only group and front velocities count.
- A quantity fixed when the pair is created and read off locally at each wing is a **local hidden variable** by Bell's definition, whatever its topological character. "Global invariant" is not a mechanism until T1's setting dependence is exhibited.
- **Phase coherence is not entanglement.** A condensate described by one classical field is a product state.
- Do not use a Hopf charge unless the source writes a field that can carry one; state the target manifold of the written field and the relevant homotopy group before using any topological invariant.
- An **algebraic identity** between a void radius and a Bell-test angle is not a derivation of a bound. Score it zero.
- **Superdeterminism**, retrocausality or a setting-dependent initial state, if invoked, is added structure. Classify under SC-PILOT-3.
- If a source writes the field as a **quantum** field, entanglement is inherited from the quantisation postulate. That is SC-PILOT-3, not SC-PILOT-1.
- Search first; construct only what the corpus states. A steelman construction is permitted after Step 5 and must be labelled as the runner's own.
- **Quarantine.** Do not read `audit/`, any `gate-*` memory summary, the Cold Ledger, or the 2026-10-06 chat in which this card was written. That session had read the ledger and the Gate MAD summary and held the prior above; it is contaminated for this question. If a memory snapshot is in context, disclose it.

---

## 6. Literature to open (cite none that you did not open)

The six entries carrying an arXiv number were confirmed to exist by web search by the card author on 2026-10-06, as was Valentini's 156, 5. The remaining entries and all volume and page numbers are from the card author's memory: confirm each before citing. Content was NOT verified for any of them; a real paper may not support the use made of it. Record which were opened and to what depth.

Bell, Physics 1, 195 (1964) · Clauser, Horne, Shimony, Holt, PRL 23, 880 (1969) · Mermin, PRL 65, 1838 (1990) · Bancal et al., Nature Physics 8, 867 (2012), arXiv:1110.3795 · Salart et al., Nature 454, 861 (2008), arXiv:0808.3316 · Valentini, Phys. Lett. A 156, 5 and 158, 1 (1991) · Colin and Valentini, Proc. R. Soc. A 470, 20140288 (2014), arXiv:1306.1576 · Struyve, Rep. Prog. Phys. 73, 106001 (2010), arXiv:0707.3685 · Norsen, Found. Phys. 40, 1858 (2010), arXiv:0909.4553 · Norsen, Marian, Oriols, Synthese 192, 3125 (2015), arXiv:1410.3676.

---

## 7. Deliverable

`audit/gates/PILOT/gate_PILOT_RESULT.md` containing, in this order: both SHA-256 digests; the dynamics table; the dispersion results with code; the search table (term, hits, files); each candidate carrier with its T1–T5 results; the two pilot-wave readings with guidance equations and free-quantity lists; the literature-opened record; the one-sentence kill; the verdict code; the cost statement; a 🦜 baby-speak paragraph. Plus `pilot_dispersion.py`, the as-run prompt, and a `git format-patch` bundle. The repo cannot be pushed from the gate session: return the patch for local application.

Null result is a finding. Report it straight.

---

## 8. Reopen conditions

SC-PILOT-2 reopens only if a primary source in the pinned tree is found to write a carrier the Step 4 search missed. SC-PILOT-3 reopens only if the added wave or wave functional is shown to be forced by something already written, with zero remaining freedom. SC-PILOT-4 closes when a primary source, or a new dated Letter, fixes the dynamical law; the gate is then re-run under a new name.
