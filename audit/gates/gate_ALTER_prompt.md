# Gate ALTER — Does the BCT corpus contain a sublattice-alternating orientation?

**Programme:** The BCT Superfluid Lattice Model (ZeroFreeParameters, ORCID 0009-0007-9561-9859)
**Pre-registered:** 2026-10-01 (Barrys Reef, AEST)
**Protocol:** Cold Ledger, single-gate thread, fresh context. Hash-before-read. URL not paste.
**Tier cap:** none (fresh thread). Same-session re-runs are capped at CONJECTURE.
**Scorecard status:** geometry-to-geometry integrity gate. A kill moves no prediction; a survivor un-kills nothing.

---

## 0. Why this gate exists

Altermagnetism (Šmejkal, Sinova, Jungwirth, PRX 12, 031042 and 040501, 2022; signatures review Nature 649, 837, 2026) is a collinear magnetic phase with zero net moment and spin-split bands. The classifying criterion is purely crystallographic: the two opposite-spin sublattices must be related by a proper or improper **rotation** (possibly with a fractional translation, i.e. a screw or glide) and **not** by a lattice translation or by inversion. The textbook d-wave altermagnets (rutile RuO₂, MnF₂) have their magnetic atoms on a **body-centred tetragonal** lattice; the altermagnetic element is the 4₂ screw that survives when the oxygen octahedra around corner and body-centre sites are mutually rotated by 90° about c.

A Bravais lattice of identical sites can never be altermagnetic (theorem: the sublattices are always related by a translation). The BCT sphere lattice at c/a = √2 is FCC, a Bravais lattice. Therefore the bare spheres cannot be altermagnetic, and neither can the octahedral voids on their own (they form an FCC translate) nor the tetrahedral void pair (related by inversion). These three facts were verified 2026-10-01 in exact rational arithmetic (`alter_check.py`) and are **not** in question in this gate.

The only route to altermagnetism on the BCT lattice is a **decoration**: something occupying or oriented within the voids whose pattern around a corner sphere is the pattern around a body-centre sphere rotated by 90° about c, so that the body-centring translation is demoted to a 4₂ screw and the point symmetry drops from O_h to D₄h.

**The one question this gate asks:** does anything already written in the BCT corpus specify such a decoration, without its being chosen for this purpose?

---

## 1. The question (verbatim, do not paraphrase in the deliverable)

> On the BCT/FCC sphere lattice as the corpus specifies it, does any primary source (Letter, Appendix, or Volume section, dated on or before 2026-09-30) assign to the octahedral voids, tetrahedral voids, OHC hopfions, S¹ phase windings, or any other per-site or per-void degree of freedom a pattern that alternates between the two BCT sublattices under a 90° rotation about the tetragonal axis, such that the corner→body-centre operation is a screw or glide rather than a pure translation or inversion?

Three sub-questions, each answered YES/NO with a citation or NONE FOUND:

1. **Void orientation.** Is any orientation, occupancy asymmetry, or anisotropic shape assigned to the oct or tet voids that differs between the two sublattices? (A global c/a ≠ √2 is NOT a decoration: it changes every site identically.)
2. **Hopfion / vortex handedness.** Is the OHC or any vortex lattice given a per-site chirality, and if so, is it staggered between sublattices? (A global ± sign choice with all sites the same is NOT staggered.)
3. **S¹ winding pattern.** Are the integer windings the corpus uses as abelian charges (App X, App G) ever arranged in a sublattice-alternating pattern that is not a pure translation image of itself?

---

## 2. Success criteria (pre-committed, choose exactly one)

- **SC-ALTER-1 (SURVIVOR).** A sublattice-alternating orientation is found in a primary source dated on or before 2026-09-30, stated for reasons internal to that source, with no free choice of which sublattice carries which orientation beyond the global ±. The corner→body-centre operation on the decorated structure is verified in the terminal to be a rotation or screw/glide and NOT a translation or inversion.
- **SC-ALTER-2 (KILL — absent).** No such pattern exists. Every void, hopfion and winding assignment in the corpus is sublattice-symmetric (translation-invariant under the body-centring vector). Altermagnetism is a possible *extension* requiring one new structural input, not a BCT result.
- **SC-ALTER-3 (KILL — imported).** A pattern exists but was introduced to match a target, has a free orientation parameter, or first appears after 2026-09-30. Same failure class as App J (Gate JHF/TANH) and the σ_s normalisation trap (Gate R8).
- **SC-ALTER-4 (unauditable).** The corpus is ambiguous in a way the auditor cannot resolve from primary sources; state exactly what is missing.

**Honest prior, stated before the run:** SC-ALTER-2. Gates KND and SYM found the realised vacuum at c/a = √2 has full O_h symmetry with no generation split; a hidden D₄h decoration would contradict that finding and is unlikely to be present.

---

## 3. Method (required steps, in order)

1. **Hash before read.** Fetch this file by its commit-pinned raw.githubusercontent.com URL to disk. Compute SHA-256. Compare with the digest in `audit/gates/PREREG_20261001.sha256`. Open only on match. Record both digests in the deliverable.
2. **Independent re-derivation of the obstruction.** Before searching the corpus, re-verify in the terminal (exact arithmetic, `fractions` or sympy):
   - the BCT body-centring vector at c/a = √2 is an FCC lattice vector;
   - the oct voids form an FCC translate of the sphere sites;
   - the tet voids at (¼,¼,¼) and (¾,¾,¾) are related by inversion, not translation;
   - in rutile (metal at (0,0,0),(½,½,½); O at ±(u,u,0), (½±u,½∓u,½), any 0<u<½), the body-centring translation does NOT map the O set to itself and the 4₂ screw {C₄z | ½,½,½} DOES.
   Report all four. If any fails, stop and report SC-ALTER-4.
3. **Corpus search.** Clone the repo (HTTPS, read-only). Search every `.tex` and every mounted Volume PDF for, at minimum: `orient`, `rotat`, `stagger`, `sublattice`, `alternat`, `chiral`, `handed`, `screw`, `glide`, `4_2`, `P4_2`, `D_{4h}`, `D4h`, `decorat`, `occupan`, `void` within 3 lines of any of the preceding, `hopfion` within 3 lines of `sign` or `±` or `handed`, `winding` within 3 lines of `pattern` or `arrang`. Report hit counts per term and read every hit in context. A term absent everywhere is a finding: report it.
4. **For each candidate pattern found**, construct the decorated point set explicitly and test in the terminal which operations map sublattice A onto sublattice B. Classify: translation → degenerate; inversion → degenerate; rotation/screw/glide → altermagnetic-allowed. Report the space group of the decorated structure.
5. **Provenance check on any survivor.** Date of first appearance; whether the orientation is derived from something else in that source or posited; whether the assignment of orientations to sublattices is forced or free; whether any post-2026-09-30 text introduced it.
6. **One-sentence kill.** State the single sentence that, if true, closes the gate at SC-ALTER-2 or -3, and say whether it is true.
7. **Cost statement.** If SC-ALTER-2: state exactly what one structural input would have to be added, and what symmetry (O_h → D₄h) it would break, and note the interaction with Gate WHY√2 (√2 selected not forced) and Letter 18 Req 1 (O(k⁴) anisotropy). If SC-ALTER-1: state what the decoration predicts (chirality-split lattice dispersion, field-free transverse response) and flag the prediction as OPEN pending a spectrum calculation.

---

## 4. Guards against false positives

- A **global** tetragonal distortion, a global ± sign on all hopfions, or a global choice of winding sense is sublattice-symmetric and does NOT count.
- The SU(3) flag manifold F(1,2;3) and its two CP¹ cycles (NPBS / Monograph §28) are internal colour-gauge space, not real-space decoration. Do not count them.
- Prose that *mentions* alternation or chirality without a positional assignment does not count. The pattern must be placeable as points or vectors in the unit cell.
- The interior S²/S¹ dispute (Gate INT: two interiors, unreconciled) is out of scope unless one interior explicitly specifies a sublattice-dependent orientation.
- Do not construct a decoration and then look for it. Search first; construct only what the corpus states.
- Do not consult this gate's author, the 2026-10-01 doc "Altermagnetism and the BCT Lattice", or any session that has read the full ledger. Those are contaminated for this question.

---

## 5. Deliverable

`audit/gates/ALTER/gate_ALTER_RESULT.md` containing, in this order: both SHA-256 digests; the four terminal obstruction checks with code; the corpus search table (term, hits, files); each candidate with its point set, symmetry test and classification; provenance table; the one-sentence kill; the verdict code; the cost statement; a 🦜 baby-speak paragraph. Plus `alter_gate_check.py` (or `.ipynb`) and a `git format-patch` bundle. Repo cannot be pushed from the gate session: return the patch for local application.

Null result is a finding. Report it straight.

---

## 6. Reopen conditions

SC-ALTER-2 reopens only if a primary source dated on or before 2026-09-30 is later found to specify a sublattice-alternating orientation that the search in §3.3 missed. SC-ALTER-3 reopens only if the free orientation parameter is shown to be forced by something already in the corpus with zero remaining freedom.
