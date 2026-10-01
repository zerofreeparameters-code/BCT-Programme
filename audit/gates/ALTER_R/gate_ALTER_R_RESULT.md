# Gate ALTER-R — RESULT

| Field | Value |
|---|---|
| Runner model | `claude-fable-5-1` (configured identifier; the serving model can differ) |
| Run date | 2026-10-01 (AEST) |
| Blinding | **BLINDED** to the earlier ALTER outcome. One protocol deviation is disclosed in §2 (a memory snapshot was present in context). |
| ALTER-R card SHA-256 (computed before reading) | `3d157c7e88f4bbd1cea6248508a4911aa411f772cc39455468ea483a70c10054` — matches |
| Original ALTER card SHA-256 (computed before reading) | `3cf882a66d83c503a54a6aa5731c4da0ee7b50fccf019605423bd947bfe35882` — matches card §1 |
| Corpus | tree at `0d9600a895289d35dd1c789a37a1ff21fb8f3ef2` (committed 2026-09-30 11:44 UTC), `audit/` never checked out |
| Script | `alter_r_check.py`, SHA-256 `18e37fdaa3da8f47b9dec693ed8178f76289cf1d9e61f8ac52f181beca87d2b4`, 69 / 69 exact assertions pass |
| Stop conditions | SC-R-0 not fired · SC-R-1 not fired (see §9 for one run-log item you may wish to rule on) · SC-R-2 not fired · **SC-R-3 fired** |
| Verdict under the original card | **SC-ALTER-2 (KILL — absent)**, with one qualification stated in §8 |

The original card's method step 1 asks for a comparison with `audit/gates/PREREG_20261001.sha256`. The ALTER-R card forbids reading anything under `audit/` except the two cards and governs on this point, so the comparison was made against the digest printed in ALTER-R §1 instead.

---

## 1. Runner's stated prior

Written to disk before the corpus was fetched. UTC timestamp: 2026-09-30T23:40:09Z.

> Expected: **SC-ALTER-2**. Reason, from the original card alone: a D4h decoration that demotes the body-centring translation to a 4_2 screw is a very specific structural statement (two inequivalent sphere environments, mutually rotated by 90 deg about c); a corpus built on an FCC (Bravais) sphere packing with O_h voids has no internal reason to have written one down, and prose about chirality or winding usually carries a global sign, not a positional staggering.

## 2. Blindness and protocol disclosures

- I did not learn the earlier ALTER outcome from any source. I did not open `alter_check.py`, `alter_gate_check.py`, or any file with `ALTER` and `RESULT` in its name. No file in the pinned tree outside `audit/` has `ALTER` in its name.
- **Deviation from "fresh context, no memory".** The session was started with a system-delivered memory snapshot in context: a short profile of the operator and a listing of memory file names (including names of BCT project files). It says nothing about Gate ALTER or its outcome. I did not call any memory tool or past-chat search, and nothing from the snapshot was used as evidence. It is reported because the card says "no memory"; the operator decides whether it matters.
- The original card itself states an "honest prior" of SC-ALTER-2 and says three of the four obstruction facts were verified on 2026-10-01 with `alter_check.py`. That is card text, not an outcome.
- Eight files in the pinned tree outside `audit/` mention other gates or "Cold Ledger" corrections: `gate.md`, `gate PSI2 prompt.md`, `BCT_Volume1_Foundations.tex`, `BCT_Volume3_QCD.tex`, `tex/BCT_Appendix_FG_ElectronMass.tex`, `tex/BCT_Appendix_K_GreenFunction.tex`, `tex/BCT_Monograph_PLB.tex`, `tex/BCT_OneMedium_JournalEdition_v2.txt`. The gates they name are KND, KAUDIT, THETA, STAT, EDM, PT, R2, M21 and G′. None is ALTER, and none states an ALTER outcome. No statement about another gate was used as evidence: where a lattice fact was needed it was derived in the script. One such statement is quoted in §7 (NM-1) and is labelled there as an audit addition, not as the author's text.
- Git: only commit `0d9600a` and its ancestors were fetched (324 commits, first dated 2026-03-25). No later commit was fetched, checked out, diffed or logged. The two cards were fetched by raw URL at their pinned commits.
- Forbidden action 5: no BCT expression, decoration, order parameter or Lagrangian was written. Every structure built in the script is either a textbook structure (rutile, FCC voids) or a literal transcription of a labelling the corpus states.

## 3. Obstruction checks (original card §3.2) and control

All in exact arithmetic (`fractions.Fraction`; an exact ℚ(√2) class for the one place √2 appears). The code is `alter_r_check.py`; the full output is in Appendix B.

| # | Statement | Result |
|---|---|---|
| 1 | The BCT body-centring vector at c/a = √2 is an FCC lattice vector | **PASS.** In the cubic frame it is a_c(½, 0, ½), with a_c = c = √2·a. Gram matrices of BCT and FCC primitive vectors are identical. The bare lattice has 48 point operations, all symmorphic: Fm-3m (No. 225). |
| 2 | The oct voids form an FCC translate of the sphere sites | **PASS.** Each is 6-coordinated at a_c/2; the void set equals the sphere set shifted by (½,½,½)_c and is closed under FCC translations. The two oct voids of the BCT cell are exchanged by the body-centring translation. |
| 3 | The tet voids at (¼,¼,¼) and (¾,¾,¾) are related by inversion, not translation | **PASS.** Both 4-coordinated at (√3/4)a_c. Their difference (½,½,½)_c is not an FCC vector. Inversion about a sphere exchanges them. |
| 4 | Rutile: the body-centring translation does not map the anion set to itself; the 4₂ screw {C₄z \| ½,½,½} does | **PASS.** Proved symbolically for generic u, and by exhaustive sweep over all 550 rationals u = p/q with 0 < u < ½, q ≤ 60. (screw)⁴ = translation by 2c, so the axis is 4₂. Whether an operation is a screw or glide is decided exactly: an operation is point-type for some lattice representative if and only if −P·t lies in the integer span of the projected lattice generators (P the projector onto the invariant subspace). |

None failed, so the original card's "stop and report SC-ALTER-4" did not apply.

**Positive control (ALTER-R §3.4): MnF₂**, rutile structure, P4₂/mnm (No. 136), Mn on 2a (0,0,0), (½,½,½) — a body-centred tetragonal magnetic lattice — F on 4f with u = 61/200, moments antiparallel on the two Mn sites.

- translation exchanges the two Mn sublattices: **NO**
- inversion about any point exchanges them: **NO**
- rotation with fractional translation exchanges them: **YES** — 8 exchanging operations: two 4₂ screws, two 2₁ screws, two n-glides, two 4̄
- script verdict: ALTERMAGNETIC-ALLOWED. With explicit axial spins, {C₄z | ½,½,½} maps the structure to its time-reverse; the pure translation does not.
- The 16 operations found are identical to the tabulated general positions of No. 136.

Two negative controls also behave: the same Mn lattice with the anions removed returns DEGENERATE (translation); a two-sublattice pattern on the FCC tet sites returns DEGENERATE (inversion).

## 4. Search

### 4.1 Terms fixed before running

Card-mandated (original §3.3): `orient`, `rotat`, `stagger`, `sublattice`, `alternat`, `chiral`, `handed`, `screw`, `glide`, `4_2`, `P4_2`, `D_{4h}`, `D4h`, `decorat`, `occupan`; `void` within 3 lines of any of the preceding; `hopfion` within 3 lines of `sign`/`±`/`handed`; `winding` within 3 lines of `pattern`/`arrang`.

Runner additions, written down before any hit was seen (synonyms the mandated list would miss): `antiferro`, `altermagn`, `bipartite`, `checkerboard`, `body-cent` near `corner`, `Néel`, "two sublattices"/"A and B sub…", `enantio`, `helicit`, `opposite` near site/void/sphere/lattice, `antiparallel`, space-group vocabulary (`4_1`, `4_3`, `I4_1`, `mnm`, "space group", `\bar{4}`, `D_{2d}`, `D_{2h}`, `C_{4v}`, `Fm-3m`, `I4/mmm`), `tetragonal` near distort/break/split, `rutile`.

Matching was case-insensitive over every text-bearing file (LaTeX source as written, PDF text layers via `pdftotext -layout`). A de-hyphenation pass over the PDF text changed no count.

### 4.2 Results

"Blocks" are hit lines merged with ±3 lines of context. Every block was read; identical blocks in duplicate files (many files exist as `name.ext` and `name (1).ext`) were read once.

| Term | Hit lines | Blocks | Files |
|---|---:|---:|---:|
| orient | 50 | 34 | 15 |
| rotat | 190 | 145 | 34 |
| stagger | 8 | 3 | 1 |
| sublattice (incl. sub-lattice) | 60 | 51 | 18 |
| alternat | 35 | 33 | 18 |
| chiral | 331 | 220 | 28 |
| handed | 211 | 128 | 20 |
| screw | 4 | 3 | 2 |
| glide | 1 | 1 | 1 |
| **4_2** | **0** | 0 | 0 |
| **P4_2** | **0** | 0 | 0 |
| D_{4h} | 15 | 10 | 5 |
| D4h | 188 | 110 | 3 |
| decorat | 5 | 4 | 3 |
| occupan | 6 | 5 | 5 |
| void ~ any of the above | 233 | 141 | 30 |
| hopfion ~ sign/±/handed | 8 | 8 | 8 |
| winding ~ pattern/arrang | 1 | 1 | 1 |
| **antiferro** | **0** | 0 | 0 |
| **altermagn** | **0** | 0 | 0 |
| bipartite | 112 | 80 | 10 |
| **checkerboard** | **0** | 0 | 0 |
| body-cent ~ corner | 15 | 12 | 5 |
| **Néel** | **0** | 0 | 0 |
| two sublattices / A and B sub… | 3 | 3 | 2 |
| **enantio** | **0** | 0 | 0 |
| helicit | 54 | 49 | 28 |
| opposite ~ site/void/sphere/lattice | 39 | 33 | 15 |
| antiparallel | 3 | 3 | 2 |
| space-group vocabulary | 29 | 24 | 9 |
| tetragonal ~ distort/break/split | 17 | 13 | 5 |
| **rutile** | **0** | 0 | 0 |

Terms absent everywhere, which the card asks to be reported as findings: `4_2`, `P4_2`, `antiferro`, `altermagn`, `checkerboard`, `Néel`, `enantio`, `rutile`. The only `screw` hits are bone screws (a patent concept); the only `glide` hit is the docking program Glide; the `decorat` hits are "not decorative" and CSS `text-decoration`. The corpus never names a screw axis, a glide plane or a non-symmorphic space group. The only space group it names is I4/mmm (Letter 39 Addendum, for indium and for "the BCT vacuum"). The point groups it names are D₄h, C₄v, T_d, O_h, and in passing C_3v, C_3 and "D1h".

The `D_{4h}` row counts the LaTeX and subscript spellings (`D_{4h}`, `D_4h`, `D₄h`); the `D4h` row counts the plain spelling. Exact patterns are in Appendix A.

### 4.3 Terms added after seeing hits (logged, with reason)

Added because the hits showed the corpus's own vocabulary for sublattices ("A/B", "corner group", "inequivalent") or because a staggering could be phrased without any mandated word.

| Added term | Reason | Hit lines | Blocks | Files |
|---|---|---:|---:|---:|
| A/B, "A site(s)", "B site(s)", A→B | App K's labels | 14 | 11 | 4 |
| corner group / body-centre group / corner site / body-centre site | App D.1 and Monograph wording | 15 | 11 | 3 |
| inequivalent | App K "two inequivalent sublattices" | 6 | 6 | 5 |
| up-/down-pointing, "two kinds/types/sets/orientations of tet…", "tet voids of opposite/two…" | tet-void orientation | 0 | 0 | 0 |
| Wyckoff, motif, basis, "voids/sites per (unit) cell" | positional assignment | 3 | 3 | 1 |
| stacking, ABAB, ABCABC, double-layer | layer alternation | 60 | 50 | 16 |
| counter-rotating, (anti)clockwise | circulation sense | 18 | 17 | 4 |
| vortex lattice, antivortex, vortex–anti… | vortex arrangement | 20 | 19 | 7 |
| superlattice, period/cell doubling, dimeris…, zigzag | cell enlargement | 2 | 2 | 2 |
| (−1)^… sign patterns | staggered phases | 6 | 5 | 3 |
| mirror image, superimposable, enantiomorph | handedness | 3 | 3 | 3 |
| "opposite phase/sign/winding/chirality/handedness…" | opposite labels | 17 | 16 | 11 |
| parity-odd / parity-even void | void parity label | 1 | 1 | 1 |
| NaCl, rock-salt, fluorite, zinc-blende, CsCl, perovskite, spinel, pyrochlore, diamond | named decorated structures | 2 | 2 | 2 |
| "each/every site/void/sphere/cell carries/has/hosts…" | per-site assignment | 9 | 8 | 6 |
| `Hopf`/`OHC` within 3 lines of ±, handed, stagger, alternat, opposite, H = −1, sublattice, neighbouring/adjacent sphere | the mandated `hopfion` pattern misses "Hopf charge" and the `\OHC` macro | 89 | 53 | 34 |
| symmetry symbols in every spelling: `D₄…` (incl. the garbled `D₄�` of the Volume 2 text layer), `C₄…`, `C₂`, `C₃`, `S₄`, `Oᴴ`, `O_h`, `T_d`, `Tᵤ`, `\Td`, `4₂`, `4₁`, `2₁`, `D₂`, `C_3v`, `D1h`, `D2d` | the earlier patterns missed Unicode-subscript spellings; found by the independent check (§9) | 1,424 | 768 new | 40 |

The last row needs a note. 1,424 lines match; 386 of them were already inside a block read under another term. The remaining 1,038 lines form 768 further blocks, and all were read. They are group-theory bookkeeping: T_d orbit numbers and "T_d texture" for quark masses and mixing, the C₄v "democratic" lepton matrix, D₄h irreps for generations, O_h as the symmetry of the oct void. They contribute four passages to the source lists of NM-4 and NM-5 (cited there: Letter 62, Volume 1 Part 2 pp. 146 and 342, Volume 2 p. 333) and nothing of a new kind. The screw-axis symbols `4₂`, `4₁`, `2₁` do not occur in any spelling.

One malformed first attempt at the tet-orientation pattern matched any "T" followed by a sign or hyphen (790 lines of noise, e.g. "T-symmetry"); it was discarded unread and replaced by the pattern in the table, which has no hits.

## 5. Corpus accounting

The pinned tree has **290 files outside `audit/`**. None was excluded on grounds of quality, tier or authorship.

| Class | Count | By type |
|---|---:|---|
| Primary (Letters, Appendices, Volumes, monograph/papers, patent texts) | 159 | 138 `.tex`, 9 `.pdf`, 1 `.zip`, 1 `.txt`, 10 `.md` |
| Secondary (outreach, state saves, guides, indices, site code, licences) | 127 | 113 `.md`, 3 `.html`, 4 `.py`, 2 `.yml`, 1 `.gitignore`, 4 without extension |
| Images | 4 | 4 `.png` |

The primary/secondary split was made by filename and is only an accounting aid; all 286 text-bearing files were searched identically.

- **PDFs:** 1,480 pages in all. Volume 1 Parts 1–3 (425 + 425 + 25 pages), Volume 2 (582 pages, inside `BCT_Appendices_Volume2_2026_compressed.zip`, which was unpacked), the NPB paper (5), five SMOKE patent documents (18). Every page has a text layer; no page yielded fewer than 40 characters.
- **Could not be read or parsed as text:** none. All text files decode as UTF-8 without replacement characters.
- **Images:** the four PNGs (`hopf_logo.png`, `assets/hopf_logo.png`, `bct_banner.png`, `bct_banner (1).png`) and the ten image-bearing PDF pages (Volume 1 Part 1 p. 25; Volume 2 pp. 574–582) were looked at by eye. They are logos, a plot of void radii against c/a, and monochrome renderings of the void network. None marks, colours or orients sites by sublattice.
- **What "read" means here:** every file was text-searched in full. Every hit block was read in context, and the surrounding section was read wherever a block looked like a candidate. No file was read end to end. About 2,090 block-readings were made across all terms (with overlap between terms).
- **Hit blocks per term:** tables in §4.2 and §4.3.

## 6. The question and its three sub-questions

> On the BCT/FCC sphere lattice as the corpus specifies it, does any primary source (Letter, Appendix, or Volume section, dated on or before 2026-09-30) assign to the octahedral voids, tetrahedral voids, OHC hopfions, S¹ phase windings, or any other per-site or per-void degree of freedom a pattern that alternates between the two BCT sublattices under a 90° rotation about the tetragonal axis, such that the corner→body-centre operation is a screw or glide rather than a pure translation or inversion?

**Answer: NO.**

1. **Void orientation — NO.** The corpus gives the oct void a distinguished axis, but it is the c axis on every oct void alike (Monograph, "Corner group … Body-centre group"; Letter 127: "the octahedral void has a preferred orientation (the z-axis of the D₄h tetragonal lattice), while the tetrahedral void is orientation-symmetric"). That is near-miss NM-3: translation-symmetric. The corpus labels the two tet voids differently and says they are "related by the C₄v rotation" (App Q.5). That is NM-5: the difference is between the two tet sets, not between the two BCT sublattices; the two sets are exchanged by inversion; and the body-centring stays a pure translation. Volume 2 itself records (PDF p. 551): "The assumption that the physical vacuum retains the full D₄h symmetry (and is not further broken) has been used throughout. No spontaneous breaking of D₄h has been investigated."
2. **Hopfion / vortex handedness — the OHC: NO; one staggered handedness label elsewhere: YES, as a label only.** Every sphere carries the same Hopf charge, H = 1 (App JH, `tex/BCT_Appendix_JH_FINAL.tex` l. 223: the boundary condition requires Ψ_int "to carry exactly H = 1 Hopf winding"; Letter 36, `tex/BCT_Letter36_OHC_tex.tex` l. 102–126: "Each sphere … contains an interior condensate Ψ_int … characterised by Hopf invariant H = 1"), and the corpus's handedness claims are global (Chern–Simons level k = +1, App Y). The corpus is not uniform on this point: Letter 70 speaks of "equal numbers of H = +1 and H = −1 excitations at every scale" and Volume 1 Part 1 p. 65 of "equal numbers of vortex-antivortex pairs" in the ground state. Those are counts with no positions (§7.6), so they do not stagger anything, but they are not the same statement as H = 1 on every sphere. The one staggered statement is App L §4.3: "The BCT bipartite A/B sublattice naturally distributes the two Weyl spinor components across the two sublattice sites (right-handed on A, left-handed on B)." That is NM-2. It carries no position, axis or rotation; the two sublattices are exchanged by inversion; there is no screw. It does not meet the main question.
3. **S¹ winding pattern — NONE FOUND.** The integer windings of App X/App G are (n_r, n_g, n_b) on the three axes of a single tet void, with the constraint n_r + n_g + n_b ≡ 0 (mod 3). They are internal to a void. No passage arranges windings from site to site. The single hit for `winding` near `pattern`/`arrang` is Letter 125 (a "phase pattern" propagating from an event), which is not a lattice arrangement.

## 7. Near-miss derivations (ALTER-R §4)

Conventions. Tetragonal conventional cell, fractional coordinates; spheres at (0,0,0) ("corner", A) and (½,½,½) ("body centre", B); oct voids at (½,½,0), (0,0,½) (App D.1's V_oct = (½,½,0)); tet voids at (½,0,¼), (0,½,¾) and (0,½,¼), (½,0,¾) (App D.1's V_tet = (½,0,γ/4) and its images). "Generic c/a" uses the 16 operations of D₄h as candidates; "c/a = √2" uses the 48 operations of O_h written exactly in the same frame (check 1 shows the metric is cubic there). A point operation is accepted only if it maps the structure's true translation lattice into itself. Every operation set below was compared with the tabulated general positions of the named group (spglib 2.7.0 database of International Tables settings) and is identical to it; that comparison is a cross-check and is not one of the exact assertions.

Each near-miss answers the three questions of §4.2: are the two sublattices related by (a) a pure lattice translation, (b) inversion about some point, (c) a rotation or rotoinversion with fractional translation not reducible to (a) or (b)?

### NM-1 — "A sublattice = corners, B sublattice = body centres" (bipartite labels)

**Source.** App K §1.1 (Volume 1 Part 1, PDF p. 120): "A sublattice: corner sites at positions (n₁, n₂, n₃√2) … B sublattice: body-centre sites at (n₁+½, n₂+½, (n₃+½)√2)", eight nearest-neighbour vectors δ = (±½, ±½, ±½√2). The reconstructed source `tex/BCT_Appendix_K_GreenFunction.tex` l. 98–100 words it "Two sublattices: A (corners) at … B (body centres) at …". Reused in App L, App N, App R, App Z, App AZ7, Letter 27, Letter 31. The same partition appears as a sign: "E → −E under σ_z conjugation on the A/B sublattice" (App L §1, p. 129) and "Γ = diag(+1,−1)" (App N §N.3.1, p. 140). A scalar sign on A and B is the two-colour structure derived under NM-2 (P4/mmm, No. 123), with the two colours on translation-related sites.

**Structure.** Identical sites at A and B; the only thing distinguishing them is the name. Reading (ii) also keeps the eight declared A–B bonds as a decoration (bond midpoints at (¼,¼,¼), (¾,¼,¼), (¼,¾,¼), (¾,¾,¼) + I-centring) and leaves the in-plane A–A contacts unmarked.

**Tests.** (a) YES, translation (½,½,½). (b) YES, inversion about (¼,¼,¼). (c) 14 further exchanging operations exist, all reducible to (a).

**Surviving operations and space group.**

- (i) labels only, generic c/a: I lattice, D₄h, all 16 operations point-type → **I4/mmm (No. 139)**. 16 operations (tetragonal frame, modulo I-centring (0,0,0; 1/2,1/2,1/2)):

    -x,-y,-z                 -x,-y,z                  -x,y,-z                  -x,y,z
    -y,-x,-z                 -y,-x,z                  -y,x,-z                  -y,x,z
    x,-y,-z                  x,-y,z                   x,y,-z                   x,y,z
    y,-x,-z                  y,-x,z                   y,x,-z                   y,x,z

- (i) labels only, c/a = √2: **Fm-3m (No. 225)**, 48 operations, all point-type (listed in Appendix B).
- (ii) with the eight A–B bonds marked, c/a = √2: the marking singles out c and the group drops to **I4/mmm (No. 139)**, the same 16 operations as above. The body-centring translation survives.

Reasoning that fixes the group: body-centred translation lattice, holohedral point group, no operation that is a screw or glide for every lattice representative. Of the four I-centred D₄h groups (139–142) only 139 is symmorphic; of the four F-centred O_h groups (225–228) only 225 is.

**Consequence.** Degenerate: A and B are related by a pure translation.

**The partition is a choice of description.** Check 1 shows that at c/a = √2 the lattice is FCC, where every site has twelve equidistant neighbours: the eight A–B contacts and four in-plane A–A contacts. The A/B partition is therefore not a property of the lattice at √2. (`tex/BCT_Appendix_K_GreenFunction.tex` carries a banner saying the same thing and citing Gate KND. The file marks that banner "audit addition, not the author's text". It is mentioned for completeness and was not used as evidence.)

### NM-2 — "right-handed on A, left-handed on B"

**Source.** App L §4.3 "Staggered Phase Cancellation" (Volume 1 Part 1, PDF p. 132): "The BCT bipartite A/B sublattice naturally distributes the two Weyl spinor components across the two sublattice sites (right-handed on A, left-handed on B). … η_stag = Σ (−1)^(k₁+k₂+k₃) = 0. The phases cancel exactly. No staggered mass is generated." This is the only place in the pinned tree where a handedness is assigned differently to the two BCT sublattices.

**Structure.** A = (0,0,0) + ℤ³ carries R; B = (½,½,½) + ℤ³ carries L. Nothing else: no position inside the cell, no axis, no vector. Handedness is a pseudoscalar, so R ↔ L under every improper operation.

**Tests.**

- Bare site sets, label ignored: (a) YES, translation (½,½,½) — this is NM-1.
- Decorated structure, label respected: (a) **NO** — a translation cannot turn R into L. (b) **YES** — inversion about (¼,¼,¼) maps A onto B and R onto L. (c) 7 further exchanging operations: five glides and two 4̄; all coexist with the inversion, so none is "not reducible to (b)". There is **no screw axis of any kind**; every 4-fold operation is a pure rotation through a site.

**Surviving operations and space group.** Primitive tetragonal lattice (the body-centring is no longer a translation), point group D₄h, 16 operations, at generic c/a and at √2 alike. 16 operations (tetragonal frame, primitive lattice):

    -x+1/2,-y+1/2,-z+1/2     -x+1/2,y+1/2,z+1/2       -x,-y,z                  -x,y,-z
    -y+1/2,-x+1/2,z+1/2      -y+1/2,x+1/2,-z+1/2      -y,-x,-z                 -y,x,z
    x+1/2,-y+1/2,z+1/2       x+1/2,y+1/2,-z+1/2       x,-y,-z                  x,y,z
    y+1/2,-x+1/2,-z+1/2      y+1/2,x+1/2,z+1/2        y,-x,z                   y,x,-z

These are exactly the general positions of **P4/nnc (No. 126), origin choice 1**, with both sublattices together forming Wyckoff position 2a (site symmetry 422). Reasoning: P lattice with point group D₄h; the 4-fold axis and the 2-fold axis along a are pure rotations; the planes normal to c, to a and to [110] are all glides; an inversion centre exists at (¼,¼,¼), off the 4-fold axis. Among the sixteen P-lattice D₄h groups, a pure 4 with a glide normal to c leaves 125, 126, 129, 130; a glide normal to a removes 129; a glide normal to [110] removes 125; a pure 2 (not 2₁) along a removes 130.

**A second space group is possible on the information in the source.** If "right-handed" and "left-handed" are read as two plain colours with no pseudoscalar character, the structure is a two-colour ordering of FCC by alternate (001) layers: **P4/mmm (No. 123)**, symmorphic, 16 operations, none of which exchanges the two colours. 16 operations (tetragonal frame, primitive lattice):

    -x,-y,-z                 -x,-y,z                  -x,y,-z                  -x,y,z
    -y,-x,-z                 -y,-x,z                  -y,x,-z                  -y,x,z
    x,-y,-z                  x,-y,z                   x,y,-z                   x,y,z
    y,-x,-z                  y,-x,z                   y,x,-z                   y,x,z

The source does not say which reading it intends. Both are given.

**The formula in the same passage.** η_stag = Σ_{k∈{0,1}³} (−1)^(k₁+k₂+k₃) is a sum of eight signs over the corners of a cube, although the text calls it a sum "over the 2-site unit cell". Read on the two actual sites of the cell (k = 000 at the corner and k = 111 at the body centre, in half-cell units) it gives + on A and − on B, which is the two-colour reading above. Read instead as a checkerboard sign (−1)^(n₁+n₂+n₃) on the corner lattice alone, it is a rock-salt-type colouring: like signs form an F-centred tetragonal lattice on the doubled cell, the two colours are exchanged by the pure translation (a,0,0), and the coloured structure is F4/mmm, which is **I4/mmm (No. 139)** in its standard cell. Degenerate in that reading as well. The source gives no sign for body-centre sites in that reading.

**Consequence.** Degenerate on either reading. With handedness as a pseudoscalar the opposite-handed sublattices are related by inversion. With plain colours nothing relates them, and the positions are related by translation. In neither case is there a rotation or screw that exchanges them without a translation or inversion also doing so, and nothing in the source rotates by 90° about c.

**What the corner→body-centre operation is, for the record.** In the P4/nnc reading it is no longer a pure translation: it is the inversion about (¼,¼,¼), or equivalently one of the n-glides. That is the closest the corpus comes to demoting the body-centring. It fails the card's criterion on the word "inversion".

### NM-3 — the oct void's distinguished axis

**Sources.** App D.1 §3 (Volume 1 Part 1, PDF p. 22: "Corner group", "Body-center group") and the Monograph section "The BCT Lattice Geometry" (`tex/BCT_Monograph_PLB.tex` l. 255–266: "Corner group", "Body-centre group"): the six neighbours of V_oct = (½,½,0) split into four at a/√2 and two at c/2. `tex/BCT_OneMedium_JournalEdition_v2.txt` l. 264: "the corner-group and body-centre-group sublattices of the octahedral void". Letter 127 (`tex/BCT_Letter127_EWQCDScales.tex` l. 251–253): "the octahedral void has a preferred orientation (the z-axis of the D₄h tetragonal lattice), while the tetrahedral void is orientation-symmetric."

**Structure.** Each oct void carries a headless axis (director) along c. Both oct voids of the cell carry the same one.

**Tests.** (a) YES, translation (½,½,½) exchanges the void at (½,½,0) and the void at (0,0,½) together with their directors. (b) YES. (c) reducible to (a).

**Which neighbours are "corner" and which "body centre".** Around (½,½,0) the four equatorial neighbours are corners and the two axial ones are body centres. Around (0,0,½) the four equatorial neighbours are body centres and the two axial ones are corners. The two pictures are images of one another under the body-centring translation; the words "corner" and "body centre" swap because the origin moved, not because the environment changed.

**Surviving operations and space group.** At c/a = √2 the director removes the cubic operations and leaves **I4/mmm (No. 139)**, symmorphic. 16 operations (tetragonal frame, modulo I-centring (0,0,0; 1/2,1/2,1/2)):

    -x,-y,-z                 -x,-y,z                  -x,y,-z                  -x,y,z
    -y,-x,-z                 -y,-x,z                  -y,x,-z                  -y,x,z
    x,-y,-z                  x,-y,z                   x,y,-z                   x,y,z
    y,-x,-z                  y,-x,z                   y,x,-z                   y,x,z

**Consequence.** Degenerate: translation. This is a global tetragonal axis, which the card's guard 1 excludes in any case.

### NM-4 — oct voids and tet voids given different labels

**Sources.** App D.3 §4.2 (Volume 1 Part 1, PDF p. 35): "the BCT void network is bipartite: tetrahedral and octahedral voids alternate". Letter 30 (`tex/BCT_Letter30_DeltamN.tex` l. 85–86): "assigns u-type quarks to octahedral voids … and d-type quarks to tetrahedral voids". Letter 62 (`tex/BCT_Letter62.tex` l. 39–42): octahedral voids "host the OHC", tetrahedral voids "host the TVC". App Y §Y.4 (Volume 1 Part 1, PDF p. 198) and §Y.7 (pp. 199–200; the appendix is printed twice, again at pp. 202–206): the left-handed doublet in the oct void, "the right-handed component of the tet void (quark sector)". Volume 2 (PDF p. 436, "Physical Interpretation of the N*(1535) Ladder Step"): "the tetrahedral void … is the parity-odd void of the D₄h point group". Volume 2 (PDF p. 408): "the omega sees the oct and tet channels with opposite phase". Secondary: `BCT_WikiChallenge_Articles.md` l. 147: "octahedral voids (left-handed in D4) … tetrahedral voids (right-handed in D4 by complementarity)".

**The corpus disagrees with itself about which label goes where.** Letter 30 puts u on oct and d on tet. App BK (Volume 1 Part 1, PDF p. 336) has "the up-type matrix … aligned with the tet-void axis" and the down-type with the oct-void axis. Volume 1 Part 2 (PDF p. 342) has "the octahedral void contributes to the down quark but not the up quark". App Q.5 puts both on the two tet voids (NM-5). App Y seats SU(2) in the oct void; Volume 1 Part 2 (PDF p. 146) has "the W boson couples exclusively to the tetrahedral void". The derivation below does not depend on which assignment is meant: it uses only "one label on oct, another on tet".

**Structure.** Label X on every oct void, label Y on every tet void; both tet sets alike. Per primitive cell: one oct void, two tet voids.

**Tests.** (a) NO. (b) NO. (c) NO. No operation of any kind exchanges the oct set with a tet set: they are different Wyckoff sets with different multiplicities and different site symmetries.

**Surviving operations and space group.** Two readings, both given.

- Labels as scalars (occupancy, species, a sign): the voids were already distinct, so nothing changes. **Fm-3m (No. 225)** at √2, 48 operations; **I4/mmm (No. 139)** at generic c/a.
- Labels as genuine handedness (pseudoscalar L on oct, R on every tet): every improper operation is lost and only the proper ones remain. **F432 (No. 209)** at √2, symmorphic, 24 operations; **I422 (No. 97)** at generic c/a, 8 operations. 8 operations (tetragonal frame, modulo I-centring (0,0,0; 1/2,1/2,1/2)):

    -x,-y,z                  -x,y,-z                  -y,-x,-z                 -y,x,z
    x,-y,-z                  x,y,z                    y,-x,z                   y,x,-z

  The 24 operations of F432 and the 48 of Fm-3m are listed in Appendix B.

In every reading the body-centring translation survives as a pure translation.

**Consequence.** Not a compensated pair at all. The oct and tet sets are symmetry-inequivalent, so there are no "opposite sublattices" to be related. The corner and body-centre spheres remain related by a pure translation: degenerate.

**Aside.** The oct–tet adjacency graph is indeed bipartite (each tet void touches four oct voids and each oct void eight tet voids). The prototype the source names, NaCl, is the sphere + oct-void arrangement; the oct + tet void network is the fluorite arrangement. This does not affect the gate.

### NM-5 — two tet voids, "up-type and down-type", "related by the C₄v rotation"

**Source.** App Q.5 "The Void-Count Argument" (Volume 1 Part 1, PDF pp. 150–151): "1 octahedral void … 2 tetrahedral voids (sites of the quark vortices, up-type and down-type) … The doublet structure of the tet voids (2 per unit cell, related by the C₄v rotation) corresponds to the two lighter generations".

A second passage names the same pair by a different relation: Volume 2 (PDF p. 333), "there are two tetrahedral voids per BCT unit cell (above and below the ab-plane)". The mirror z → −z through a sphere does map T1 onto T2 (verified).

App Q.5 is the passage that comes nearest to the card's wording, because it names a 90° rotation about c as the relation between two differently labelled sets of sites.

**Structure.** T1 = (½,0,¼) + I-lattice, T2 = (0,½,¼) + I-lattice. C₄ about c through a sphere maps T1 onto T2 (verified).

**Tests.** (a) **NO** — (−½,½,0) is not a lattice vector. (b) **YES** — inversion about a sphere site exchanges T1 and T2. (c) the 4-fold rotations also exchange them, and every one of them is a pure rotation, not a screw; they coexist with the inversion.

**Surviving operations and space group.**

- T1 and T2 alike: **I4/mmm (No. 139)** at generic c/a with the tet voids on Wyckoff 4d; **Fm-3m (No. 225)** at √2 with the tet voids on 8c.
- T1 and T2 carrying distinct labels ("up-type", "down-type"): at generic c/a, I lattice, point group D₂d, symmorphic, mirrors normal to a kept and diagonal mirrors lost → **I-4m2 (No. 119)** (not I-42m, No. 121, which keeps the diagonal mirrors instead). 8 operations (tetragonal frame, modulo I-centring (0,0,0; 1/2,1/2,1/2)):

    -x,-y,z                  -x,y,z                   -y,-x,-z                 -y,x,-z
    x,-y,z                   x,y,z                    y,-x,-z                  y,x,-z

  At c/a = √2: F lattice, T_d, symmorphic → **F-43m (No. 216)**, 24 operations. 24 operations (cubic frame, modulo F-centring (0,0,0; 0,1/2,1/2; 1/2,0,1/2; 1/2,1/2,0)):

    -x,-y,z                  -x,-z,y                  -x,y,-z                  -x,z,-y
    -y,-x,z                  -y,-z,x                  -y,x,-z                  -y,z,-x
    -z,-x,y                  -z,-y,x                  -z,x,-y                  -z,y,-x
    x,-y,-z                  x,-z,-y                  x,y,z                    x,z,y
    y,-x,-z                  y,-z,-x                  y,x,z                    y,z,x
    z,-x,-y                  z,-y,-x                  z,x,y                    z,y,x

**Consequence.** Degenerate: the two tet sets are inversion partners. This is obstruction check 3 met again in the corpus's own words. And in every reading the body-centring (½,½,½) remains a pure translation that maps T1 to T1 and T2 to T2, so the corner→body-centre operation is untouched.

### Summary of §7

| | Pattern | (a) translation | (b) inversion | (c) irreducible rotation/screw/glide | Space group(s) | Consequence |
|---|---|---|---|---|---|---|
| NM-1 | A/B names on corner/body spheres | yes | yes | no | 139; 225 at √2 | degenerate |
| NM-2 | R on A, L on B | no (labels); yes (bare sites) | **yes** | no; no screw | **126** (or 123; 139 for the checkerboard reading of the formula) | degenerate |
| NM-3 | c-axis on every oct void | yes | yes | no | 139 | degenerate |
| NM-4 | oct vs tet labelled differently | no | no | no | 225 / 139 (or 209 / 97) | inequivalent sets; spheres degenerate by translation |
| NM-5 | two tet sets, "up"/"down", C₄-related | no | **yes** | no; 4-folds are pure | 139 / 225 (or 119 / 216) | degenerate |

### 7.6 Patterns examined and not taken to a derivation

These do not assign anything to the two sublattices, so ALTER-R §4 does not require a derivation. They are listed so that the omission is visible.

- **Four crystal orientations / domain walls** (Volume 2, App IX5, PDF pp. 238–239, and later appendices): a global orientation per Hubble patch. Guard 1.
- **H = +1 and H = −1 in one mode** (Letters 78, 81; App KA1): a pair within one resonance mode, no positions. Guard 3.
- **Equal numbers of vortices and antivortices in the ground state** (Volume 1 Part 1, PDF p. 65, §5.3 "Antimatter: Antivortex = Positron"; Letter 70 "equal numbers of H = +1 and H = −1 excitations at every scale"): a count, no positions. Guard 3.
- **Sphere rotation angles θ_i** (App D.3 §2; App E.1): an XY field with coupling −J cos(θ_i − θ_j), uniform in the ground state.
- **Generations as D₄h/C₄v irreps, "rotation by π/2 changes sign"** (App Q.3, App T, Volume 2 Phase 73–75): representation labels in k-space, not a real-space decoration.
- **"A vortex that tunnels between the two BCT sublattices A and B"** (App Z, Volume 1 Part 1, PDF p. 209): an event, not a static pattern; rests on NM-1.
- **"Three orthogonal void sublattices (octahedral-vector, strange-bridge, pseudo-Goldstone)"** (Letter 28): no positions. Counts of voids per cell elsewhere disagree with one another ("3 octahedral voids per BCT unit cell", Volume 2 p. 134; "three tetrahedral voids per unit cell", p. 85; "2 voids per unit cell (1 oct + 2 tet)", p. 505) and none gives positions.
- **"x-plane sub-lattice", "12-root sub-lattice D4⁺"** (App AR, App AM, App AH; Volume 1 Part 1, PDF pp. 260–288): sub-lattices of the 4D root system, internal. The SU(3) flag-manifold guard (guard 2) was not needed: no such passage was a hit.
- **"The D4 root lattice is chiral. It is not superimposable on its mirror image"** (`BCT_WikiChallenge_Articles.md`, secondary): a global handedness claim. Guard 1. (As geometry it is also incorrect: check 1 finds inversion among the 48 operations; App Y itself says "every sphere has an inversion centre".)
- **"Coupled A/B wells", Ψ_A·Ψ_B** (`BCT_AppAB2_Zenodo_Kit.md`, secondary): no positions.
- **Counter-rotating vortex pairs** (Letter 114): a macroscopic plasmoid, not the lattice.
- **"The up/down distinction is recovered by the sign of the orientation of the vortex core in the octahedral void"** (App G, Volume 1 Part 1, PDF p. 88): a sign carried by an individual vortex, with no site-to-site pattern. Guard 3.
- **Two-component condensate, Ψ₁ in the voids and Ψ₂ inside the spheres; Higgs as the anti-bonding combination (Ψ₁ − Ψ₂)/√2** (App I, PDF pp. 105–106; App AG, PDF p. 257): a relative sign between sphere interiors and void space, the same for every sphere. It does not distinguish corner from body-centre.
- **"PH symmetry Γ: k → k + (π, π, π√2)"** (App N, PDF p. 140) and the roadmap note on "the C₄ rotation (90° about z-axis)" mapping the k_x = π plane to the k_y = π plane (Volume 2, PDF p. 468): statements in k-space.
- **"One vortex-antivortex pair per two Planck cells"** (`tex/BCT_Appendix_AZ6.tex` l. 493–494): a density, no positions. Guard 3.

## 8. Provenance, one-sentence kill, verdict

### 8.1 Provenance (original card §3.5; ALTER-R §4.5)

Dates: "own date" is what the file says of itself; "first in repo" is the commit that added the file, within the ancestry of `0d9600a`.

| | Source file | Own date | First in repo | Derived or posited in the source | Assignment forced or free | Post-2026-09-30 text? |
|---|---|---|---|---|---|---|
| NM-1 | `BCT_Appendices_Volume1_2026_compressed_Part1.pdf` (App K) | PDF created 2026-08-11 | `0e27590`, 2026-09-12 | posited as the description of the lattice | which sublattice is called A is free (a naming) | no |
| NM-1 | `tex/BCT_Appendix_K_GreenFunction.tex` | "recovered as a draft PDF 15 Sep 2026" | `2b6e3d9`, 2026-09-15 | same | same | no |
| NM-2 | same Volume 1 Part 1 PDF (App L §4.3) | PDF created 2026-08-11 | `0e27590`, 2026-09-12 | posited in one sentence ("naturally distributes") | which sublattice is R is free (global swap only) | no |
| NM-3 | `tex/BCT_Monograph_PLB.tex`; Volume 1 Part 1 PDF (App D.1) | monograph carries corrections dated 16 Sep 2026 | `796ce60`, 2026-03-29 (last changed `9ee4070`, 2026-09-16) | derived (distances to neighbours) | forced by the tetragonal cell | no |
| NM-3 | `tex/BCT_Letter127_EWQCDScales.tex` and `_v2.tex` | 24 March 2026 | `796ce60`, 2026-03-29 | posited, to explain the sign of an NLO term | forced (the c axis) | no |
| NM-3 | `tex/BCT_OneMedium_JournalEdition_v2.txt` | 21 July 2026 | `b68bca9`, 2026-09-14 | asserted | — | no |
| NM-4 | Volume 1 Part 1 PDF (App D.3, App Y); `tex/BCT_Letter30_DeltamN.tex` (March 2026); Volume 2 zip | — ; March 2026; text dated February 2026 | `0e27590` 2026-09-12; `796ce60` 2026-03-29; `47a3dc0` 2026-09-12 | posited | oct/tet is forced; which is "left" is a global sign | no |
| NM-4 | `BCT_WikiChallenge_Articles.md` (secondary) | undated | `9ee4070`, 2026-09-16 | asserted | — | no |
| NM-5 | Volume 1 Part 1 PDF (App Q.5) | PDF created 2026-08-11 | `0e27590`, 2026-09-12 | posited as an "independent check" on the three-generation count | which tet set is "up-type" is free (global swap only) | no |

Every source is dated on or before 2026-09-30 and none was introduced after it. No pattern was found that was introduced to match a target or that carries a free orientation parameter, so SC-ALTER-3 has nothing to attach to.

### 8.2 One-sentence kill

> No primary source in the pinned tree places anything in the unit cell whose image under the body-centring vector is itself rotated by 90° about c: every statement that distinguishes sublattices is a bare name or sign on sites already related by a translation or an inversion (NM-1, NM-2, NM-5), a c-axis distinction shared by both sublattices (NM-3), or a distinction between two inequivalent void types (NM-4).

**It is true**, for the pinned tree. The corpus says as much about itself (Volume 2, PDF p. 551): "No spontaneous breaking of D₄h has been investigated."

### 8.3 Verdict

**SC-R-3 — completed. SC-ALTER-2 (KILL — absent).**

No sublattice-alternating orientation of the kind the card defines exists in the pinned corpus. Altermagnetism on the BCT lattice is a possible extension requiring new structural input; it is not a BCT result.

**Qualification.** SC-ALTER-2's second sentence reads: "Every void, hopfion and winding assignment in the corpus is sublattice-symmetric (translation-invariant under the body-centring vector)." Taken word for word that holds: the void, hopfion and winding assignments are all translation-invariant. But one assignment of another kind is not: App L §4.3 puts the right-handed Weyl component on A and the left-handed one on B (NM-2), and that labelling is not invariant under the body-centring translation. It is invariant under inversion instead, contains no orientation and no 90° rotation, and yields P4/nnc (No. 126) with no screw axis, so it cannot support SC-ALTER-1. It is recorded here so that the criterion is not read as "nothing staggered was found". If the operator reads SC-ALTER-2's second sentence as covering every per-site degree of freedom, the accurate statement is: "every such assignment is either translation-invariant or inversion-related".

SC-ALTER-1 does not apply (no rotation/screw/glide relation free of translation and inversion). SC-ALTER-3 does not apply (nothing imported, nothing with a free orientation parameter, nothing post-dated). SC-ALTER-4 does not apply: the two places where the source admits two readings (NM-2, NM-4) give the same consequence on both.

I have not compared this verdict with the earlier run.

### 8.4 Cost statement (original card §3.7, SC-ALTER-2 branch)

Stated as a symmetry requirement only; no decoration is proposed here.

- **What would have to be added:** one structural statement giving each sphere an environment that is not invariant under the 4-fold rotation about c, with the environment of a body-centre sphere being the environment of a corner sphere turned by 90° about c. In the rutile control that statement is the anion position, and it brings a free continuous parameter with it (the coordinate u). Nothing in the pinned corpus supplies such a statement.
- **What it would break:** the body-centring translation is demoted to a 4₂ screw, so the translation lattice goes from F (I in the tetragonal description) to primitive tetragonal, and the point group goes from O_h to D₄h at most. No translation and no inversion may exchange the two sublattices. The control (P4₂/mnm) is an example of the target class.
- **Interaction with the corpus's own use of O_h.** The corpus rests its isotropy claims on the cubic symmetry at √2: App HO5 (Volume 2, PDF p. 56, "BCT Lorentz Invariance Uniqueness Theorem": "c/a = √2 is the UNIQUE value for which the long-wavelength phonon spectrum is acoustically isotropic") and App E.0 §3.1 (Volume 1 Part 1, PDF p. 48: "under O_h symmetry, the leading correction to the phonon dispersion (which transforms as a rank-4 tensor) may vanish identically … This is an unproven conjecture"). A D₄h decoration removes the cubic symmetry those passages invoke: any second-rank response is isotropic under O_h and is not under D₄h, so anisotropy between c and a returns before the O(k⁴) question of Letter 18 Requirement 1 is even reached. With only D₄h symmetry, c/a = √2 is no longer a symmetry-distinguished value: the ratio becomes an ordinary structural parameter (in rutile-type crystals it is near 0.64–0.70). Whether the corpus's isotropy claims hold under O_h itself is outside this gate.
- **Limits of this statement.** Letter 18 is cited throughout the tree but is not in it, and Gate WHY√2 lives under `audit/`, which this gate may not read. The interaction is therefore stated from the original card's own description of those two items plus the corpus passages quoted above, not from the items themselves.

## 9. Run log: things that went wrong and what was done

1. **A wrong expected value in the control.** The first run asserted that P4₂/mnm has 8 screw/glide operations. It has 6 (two 4₂, two 2₁, two n); I had counted the two 4̄ operations, which exchange the sublattices but are point-type. The engine returned 6 and the assertion failed. The defining control test of ALTER-R §3.4 (translation fails, inversion fails, 4₂ screw succeeds) passed on that first run. I corrected the expected value, left a comment in the script, and the operation set is now also checked against the tabulated group. I treated SC-R-1 as not fired; the operator may rule otherwise.
2. **An engine defect, found by two failing near-miss assertions.** The first version accepted a point operation after testing it on one cell only. For a cubic operation written in the tetragonal frame (a rational, non-integer matrix) that is valid only if the operation preserves the structure's translation lattice. For structures whose lattice is primitive tetragonal it does not, and the first run reported 32 "operations" including 3-folds for NM-2 at √2, which cannot be a group. The fix requires every accepted operation to map the true translation lattice into itself. Effect: some counts under test (c) printed for checks 1 and 2 before the fix were inflated; no (a) or (b) answer and no pass/fail changed; the control was unaffected (it uses integer matrices only). Appendix B is the output after the fix.
3. **A bounded search replaced by an exact test.** The first version decided "screw or glide" by trying lattice representatives within ±2 cells. It now decides exactly, by an integer-span test. No result changed.
4. **Corrections made after an independent check.** Before delivery a separate checker, which had not seen the work and was confined to the local files under the same forbidden-action rules, re-derived the counts, re-ran the script, recomputed the three key crystallographic claims on its own, and searched for missed passages. It confirmed the verdict, the script results and the space groups. It also found, and I corrected: (i) a search gap — symmetry symbols written with Unicode subscripts (`D₄h`, `C₄v`, …) were not matched by the patterns in §4.1; a further pass over 768 blocks was made (last row of §4.3) and found nothing staggered; (ii) six wrong page or line references; (iii) an incomplete list of files that mention other gates (§2), and a banner that I had described as "the corpus itself" although the file marks it as an audit addition; (iv) passages belonging to the classes of NM-1, NM-4, NM-5 and §7.6 that I had read but not listed, and the corpus's inconsistency about which void carries u and d; (v) a sentence in §4.2 that omitted C_3v and "D1h" from the point groups the corpus names.
5. **An external reference could not be fetched.** The Bilbao Crystallographic Server was not reachable from this environment. Space-group operations were taken from the spglib database instead.

## 10. Coverage statement

**The verdict covers** the 290 files outside `audit/` in the tree at commit `0d9600a`: 138 LaTeX sources, 1,480 PDF pages of Volumes 1 and 2 and shorter papers, 123 Markdown files, and the remaining site and script files, all text-searched in full with the terms in §4 and every hit read in context.

**It does not cover:**

- anything under `audit/` at any commit (excluded by the card);
- any commit later than `0d9600a`;
- Letters and appendices that the tree cites but does not contain. Examples met during the search: Letter 18 (Uniqueness Theorem), Letters 171 and 195 (handedness), most Letters numbered below 19, and the Letters that exist in the tree only as Zenodo metadata entries;
- Zenodo records, the pi2.institute site, Substack posts and any other material outside the repository;
- text that uses none of the searched words or spellings. A staggered pattern described with vocabulary outside §4.1 and §4.3 would be missed, and the Unicode-subscript gap found during checking (§9, item 4) shows that a spelling can be missed too. No file was read end to end;
- information carried only by pictures. The fourteen images in the tree were inspected and show no sublattice marking, but a rendering is not a specification.

An absence verdict covers the pinned tree only. Under the original card's §6, SC-ALTER-2 reopens if a primary source dated on or before 2026-09-30 is later found to specify a sublattice-alternating orientation that this search missed.

## 11. 🦜

Two kinds of seat in the box: corner seats and middle seats. Runner look at every page for a rule that says "middle seat is corner seat turned a quarter turn". No such rule. Found one page that says "corner seat wears right mitten, middle seat wears left mitten" — but flip the box through its middle point and mittens swap, so that is only a mirror trick, not a quarter turn. Found one page that says "two little gaps, one for up, one for down, and they swap when you turn" — but they swap when you flip too. Turn-only, no-flip, no-slide: not in the box. Runner checked the checker on a real rock that does have it (the MnF₂ rock), and the checker said yes there. So: not here. 🦜

## 12. External references

- L. Šmejkal, J. Sinova, T. Jungwirth, *Phys. Rev. X* **12**, 031042 (2022) and **12**, 040501 (2022) — the sublattice criterion for altermagnetism and MnF₂/RuO₂ as rutile examples, as cited in the original card. The criterion was applied as the card states it; the papers were not re-fetched.
- *International Tables for Crystallography*, Vol. A — space groups Nos. 97, 119, 123, 126, 136, 139, 209, 216, 225. Consulted through the spglib symmetry database: A. Togo, K. Shinohara, I. Tanaka, *Sci. Technol. Adv. Mater. Methods* **4**, 2384822 (2024); spglib 2.7.0, Hall numbers 374, 396, 400, 404, 419, 424, 505, 512, 523.
- MnF₂ structure (rutile type, Mn on 2a, F on 4f, u ≈ 0.305): J. W. Stout and S. A. Reed, *J. Am. Chem. Soc.* **76**, 5279 (1954). Quoted from recall, not re-fetched. The value of u enters no verdict: check 4 holds for every 0 < u < ½.

---

## Appendix A — exact search patterns (Python `re`, case-insensitive unless noted)

Pre-registered terms (`simple`: one pattern per line of text; `prox`: first pattern on a line within 3 lines of the second):

```python
simple={
'T01 orient':r'orient','T02 rotat':r'rotat','T03 stagger':r'stagger','T04 sublattice':r'sub-?\s?lattice',
'T05 alternat':r'alternat','T06 chiral':r'chiral','T07 handed':r'handed','T08 screw':r'screw','T09 glide':r'glide',
'T10 4_2':r'4_\{?2\}?(?![0-9])|4₂','T11 P4_2':r'P\s?4_\{?2\}?|P4₂|P42/','T12 D_{4h}':r'D_\{4h\}|D_\{4\s*h\}|D_4h|D₄h|D_\{4\}h','T13 D4h':r'D4h',
'T14 decorat':r'decorat','T15 occupan':r'occupan',
'T19 antiferro':r'anti-?\s?ferro','T20 altermagn':r'altermagn','T21 bipartite':r'bipartite','T22 checkerboard':r'checker-?\s?board',
'T24 Neel':r'N[ée]el|N\'\{?e\}?el','T25 two sublattice':r'two\s+sub-?\s?lattices?|A\s+and\s+B\s+sub',
'T26 enantio':r'enantio','T27 helicit':r'helicit','T29 antiparallel':r'anti-?\s?parallel',
'T30 spacegroup':r'4_\{?[13]\}?(?![0-9])|I\s?4_\{?1\}?|mnm|space[- ]group|\bar\{?4\}?|D_\{?2d\}?|D_\{?2h\}?|C_\{?4v\}?|Fm\?-?\?(bar)?\{?3\}?m|I4/mmm',
'T32 rutile':r'rutile',
}
prox={
'T16 void~T01-15':(r'void', '|'.join(simple[k] for k in list(simple)[:15])),
'T17 hopfion~sign/±/handed':(r'hopfion', r'sign|±|\pm|\mp|handed'),
'T18 winding~pattern/arrang':(r'winding', r'pattern|arrang'),
'T23 body-cent~corner':(r'body[- ]?cent', r'corner'),
'T28 opposite~site/void/sphere/lattice':(r'opposite', r'sites?|void|sphere|lattice'),
'T31 tetragonal~distort/break/split':(r'tetragonal', r'distort|break|broke|split'),
}
```

Post-hoc terms of §4.3 (P01 and P04 are case-sensitive; the P04 pattern shown is the discarded first attempt, replaced by the one below it):

```python
post={
'P01 A/B site labels':r'A[/ ]B|A sites?|B sites?|A\s*(?:→|->|\to|\leftrightarrow|↔)\s*B',
'P02 corner/body group':r'corner[- ]group|body[- ]cent(?:re|er)[- ]group|corner sites?|body[- ]cent(?:re|er) sites?',
'P03 inequivalent':r'inequivalent',
'P04 T+/T- tet orientation':r'T[_^]?\{?[+\-−±]\}?|T₊|T₋|up[- ]pointing|down[- ]pointing|upward[- ]pointing|two (?:kinds|types|sets|orientations) of tet',
'P05 Wyckoff/basis/motif':r'wyckoff|motif|two-atom basis|atoms? per (?:unit )?cell|sites? per (?:unit )?cell|voids? per (?:unit |primitive )?cell',
'P06 stacking/layer':r'stacking|ABAB|ABCABC|layer(?:ed|s)? (?:alternat|stack)|double-?\s?layer',
'P07 counter-rotating/clockwise':r'counter-?\s?rotat|anticlockwise|counter-?clockwise|clockwise',
'P08 vortex/antivortex lattice':r'vortex lattice|anti-?vortex|vortex[- ]anti',
'P09 superlattice/doubling':r'superlattice|super-lattice|period[- ]doubl|cell[- ]doubl|doubled (?:unit )?cell|dimeri[sz]|zig-?zag',
'P10 sign pattern (-1)^':r'\(\s*[−-]1\s*\)\s*\^|\(-1\)\^\{|\(−1\)\^',
'P11 mirror image / enantiomorph':r'mirror[- ]image|superimposable|enantiomorph',
'P12 void sign/phase opposite':r'oct and tet channels with opposite|opposite (?:phase|sign|winding|circulation|chirality|handedness)',
'P13 Td void / parity-odd void':r'parity-odd void|parity-even void',
'P14 NaCl/fluorite/zincblende/rocksalt structure names':r'NaCl|rock-?salt|fluorite|zinc-?blende|sphalerite|CsCl|perovskite|spinel|pyrochlore|diamond (?:lattice|structure|cubic)',
'P15 each/every site|void carries':r'(?:each|every) (?:site|void|sphere|cell|lattice site) (?:carries|has|hosts|contains|is assigned)',
}
# P04 as used:
r'up[- ]pointing|down[- ]pointing|upward[- ]pointing|two (?:kinds|types|sets|orientations|classes) of tet|tet(?:rahedral)? voids? (?:of|with) (?:opposite|two)|T\^?\{?[+−-]\}? (?:and|/) T\^?\{?[+−-]\}? (?:void|tet|sublattice)'
# Hopf/OHC row: first pattern on a line within 3 lines of the second
r'hopf|OHC'   ~   r'±|\pm|\mp|handed|stagger|alternat|opposite|H\s*=\s*[-−]1|sublattice|neighbou?ring (sphere|cell|site)|adjacent (sphere|cell|site)'
# symmetry-symbol row:
r'D₄|D_?4\s?h|D4�|C₄|C_?4\s?v|C₂|C₃|S₄|Oᴴ|O_h|O_\{h\}|T_d|T_\{d\}|\Td|Tᵤ|4₂|4₁|2₁|D₂|C_\{?3v\}?|D_?1h|D2d|D_\{?2d\}?'
```

---

## Appendix B — full output of `alter_r_check.py`

```

==============================================================================
CHECK 1  BCT body-centring vector at c/a = sqrt2 is an FCC lattice vector
==============================================================================
  body-centring vector, Cartesian cubic frame, units of a: (1/2*sqrt2, 0, 1/2*sqrt2)
  in units of a_c = sqrt2*a: (1/2, 0, 1/2)
  PASS  body-centring vector = a_c*(1/2, 0, 1/2): an FCC face-centring vector
  PASS  c = a_c exactly (no sqrt2 residue)
  PASS  rational frame map sends (1/2,1/2,1/2)_t to (1/2,0,1/2)_c
  PASS  Gram matrix of BCT primitive vectors == Gram matrix of FCC primitive vectors
  [bare spheres, tetragonal cell, D4h candidates] ops per input-lattice cell: 16; point group D4h (4/mmm) (order 16); extra pure translations beyond input lattice: 0 []; ops that are screw/glide for every lattice representative: 0
  [bare spheres, tetragonal cell, O_h candidates (rational in this frame)] ops per input-lattice cell: 48; point group Oh (m-3m) (order 48); extra pure translations beyond input lattice: 0 []; ops that are screw/glide for every lattice representative: 0
  PASS  bare sphere lattice at c/a = sqrt2 has point group O_h (48 ops, symmorphic: Fm-3m, No. 225)
  [bare BCT spheres]
    sublattice-preserving ops: 16   sublattice-exchanging ops: 16
    (a) exchanged by pure lattice translation : YES (1/2,1/2,1/2)
    (b) exchanged by inversion about a point  : YES, centre at (1/4,1/4,1/4)
    (c) exchanged by rotation/rotoinversion   : 14 ops {'2 screw/glide': 3, 'm screw/glide': 5, '2 point-type': 2, '-4 point-type': 2, '4 screw/glide': 2}
    => DEGENERATE (translation)
  PASS  theorem instance: corner and body-centre spheres are exchanged by a pure translation

==============================================================================
CHECK 2  octahedral voids form an FCC translate of the sphere sites
==============================================================================
  oct candidate (1/2,1/2,1/2): nearest-sphere distance^2 = 1/4 a_c^2, coordination 6
  oct candidate (1/2,0,0): nearest-sphere distance^2 = 1/4 a_c^2, coordination 6
  oct candidate (0,1/2,0): nearest-sphere distance^2 = 1/4 a_c^2, coordination 6
  oct candidate (0,0,1/2): nearest-sphere distance^2 = 1/4 a_c^2, coordination 6
  PASS  each listed point is 6-coordinated at distance a_c/2 (an octahedral void)
  PASS  oct void set == sphere set + (1/2,1/2,1/2)_c  (an FCC translate, itself FCC)
  PASS  the oct set is closed under all FCC translations (one void per primitive cell)
  [oct voids alone] ops per input-lattice cell: 48; point group Oh (m-3m) (order 48); extra pure translations beyond input lattice: 0 []; ops that are screw/glide for every lattice representative: 0
  PASS  oct voids alone: Bravais, O_h, symmorphic (no sublattice structure at all)
  oct voids in tetragonal fractional coords (mod 1): [(Fraction(0, 1), Fraction(0, 1), Fraction(1, 2)), (Fraction(1, 2), Fraction(1, 2), Fraction(0, 1))]
  [oct voids, tetragonal cell: (0,0,1/2) vs (1/2,1/2,0)]
    sublattice-preserving ops: 16   sublattice-exchanging ops: 16
    (a) exchanged by pure lattice translation : YES (1/2,1/2,1/2)
    (b) exchanged by inversion about a point  : YES, centre at (1/4,1/4,1/4)
    (c) exchanged by rotation/rotoinversion   : 14 ops {'2 screw/glide': 3, 'm screw/glide': 5, '2 point-type': 2, '-4 point-type': 2, '4 screw/glide': 2}
    => DEGENERATE (translation)
  PASS  the two oct voids of the BCT cell are exchanged by a pure translation -> degenerate

==============================================================================
CHECK 3  tetrahedral voids (1/4,1/4,1/4), (3/4,3/4,3/4): inversion, not translation
==============================================================================
  tet candidate (1/4,1/4,1/4): nearest-sphere distance^2 = 3/16 a_c^2, coordination 4
  tet candidate (3/4,3/4,3/4): nearest-sphere distance^2 = 3/16 a_c^2, coordination 4
  PASS  both points are 4-coordinated at distance sqrt3/4 a_c (tetrahedral voids)
  PASS  T_B - T_A = (1/2,1/2,1/2)_c is NOT an FCC lattice vector
  [tet voids with spheres as host]
    sublattice-preserving ops: 24   sublattice-exchanging ops: 24
    (a) exchanged by pure lattice translation : NO
    (b) exchanged by inversion about a point  : YES, centre at (0,0,0)
    (c) exchanged by rotation/rotoinversion   : 23 ops {'2 point-type': 6, 'm point-type': 3, '-3 point-type': 8, '4 point-type': 6}
    => DEGENERATE (inversion)
  PASS  no pure translation exchanges the two tet sublattices
  PASS  inversion (about a sphere site) DOES exchange them -> degenerate by inversion
  PASS  verdict for undecorated tet voids is DEGENERATE (inversion)
  [spheres + both tet sets, all tets alike] ops per input-lattice cell: 48; point group Oh (m-3m) (order 48); extra pure translations beyond input lattice: 0 []; ops that are screw/glide for every lattice representative: 0
  PASS  spheres + undecorated tets keep O_h (fluorite-type arrangement, Fm-3m)

==============================================================================
CHECK 4  rutile: body-centring translation fails on the anion set, 4_2 screw succeeds
==============================================================================
  PASS  symbolic u: translation (1/2,1/2,1/2) does NOT map the anion set to itself
  PASS  symbolic u: screw {C4z | 1/2,1/2,1/2} DOES map the anion set to itself
  rational sweep: 550 distinct u = p/q, 0<u<1/2, q<=60
  PASS  sweep: translation fails for every u tested
  PASS  sweep: 4_2 screw succeeds for every u tested (anions and metals)
  PASS  boundary sanity: at the excluded endpoint u = 0 (where the four anions collapse onto two points) the translation DOES succeed; negative control 1 below is the real evidence that the test can return 'translation'
  PASS  {C4z|1/2,1/2,1/2} is non-symmorphic for every lattice representative
  PASS  (screw)^4 = translation by 2c, i.e. pitch c/2 per quarter turn: a 4_2 axis

==============================================================================
CONTROL  known altermagnet on a body-centred tetragonal magnetic lattice
==============================================================================
  Positive control: MnF2, rutile structure, P4_2/mnm (No. 136).
  Mn at 2a (0,0,0),(1/2,1/2,1/2) = a BCT magnetic lattice; F at 4f, u = 0.305 (61/200);
  collinear moments along c, antiparallel on the two Mn sites (Smejkal et al., PRX 12, 031042).
  [MnF2 non-magnetic crystal] ops per input-lattice cell: 16; point group D4h (4/mmm) (order 16); extra pure translations beyond input lattice: 0 []; ops that are screw/glide for every lattice representative: 6
    screw/glide operations by type: {'2': 2, 'm': 2, '4': 2}
  PASS  control crystal: 16 ops, point group D4h, primitive (body centring is NOT a translation), 6 screw/glide ops = {4: 2, 2: 2, m: 2}; plane normal to c is a mirror, normal to a is a glide, normal to [110] is a mirror -> P 4_2/m n m (No. 136)
  [MnF2: Mn(0,0,0) vs Mn(1/2,1/2,1/2)]
    sublattice-preserving ops: 8   sublattice-exchanging ops: 8
    (a) exchanged by pure lattice translation : NO
    (b) exchanged by inversion about a point  : NO
    (c) exchanged by rotation/rotoinversion   : 8 ops {'2 screw/glide': 2, 'm screw/glide': 2, '-4 point-type': 2, '4 screw/glide': 2}
    => ALTERMAGNETIC-ALLOWED (rotation/screw/glide only)
  PASS  control: translation FAILS to exchange the Mn sublattices
  PASS  control: inversion FAILS to exchange the Mn sublattices
  PASS  control: rotation-with-fractional-translation SUCCEEDS (4_2 screw among exchanging ops)
  PASS  control verdict: ALTERMAGNETIC-ALLOWED
  PASS  control with explicit axial spins: {C4z|1/2,1/2,1/2} maps structure to its time-reverse; pure translation does not; no inversion does

  Negative control 1: same Mn lattice, anions removed (bare BCT antiferromagnet).
  [bare BCT AFM]
    sublattice-preserving ops: 16   sublattice-exchanging ops: 16
    (a) exchanged by pure lattice translation : YES (1/2,1/2,1/2)
    (b) exchanged by inversion about a point  : YES, centre at (1/4,1/4,1/4)
    (c) exchanged by rotation/rotoinversion   : 14 ops {'2 screw/glide': 3, 'm screw/glide': 5, '2 point-type': 2, '-4 point-type': 2, '4 screw/glide': 2}
    => DEGENERATE (translation)
  PASS  negative control 1 returns DEGENERATE (translation)

  Negative control 2: magnetic sites on the two tet sublattices of FCC (inversion partners).
  [FCC tet-site AFM]
    sublattice-preserving ops: 24   sublattice-exchanging ops: 24
    (a) exchanged by pure lattice translation : NO
    (b) exchanged by inversion about a point  : YES, centre at (0,0,0)
    (c) exchanged by rotation/rotoinversion   : 23 ops {'2 point-type': 6, 'm point-type': 3, '-3 point-type': 8, '4 point-type': 6}
    => DEGENERATE (inversion)
  PASS  negative control 2 returns DEGENERATE (inversion)

  POSITIVE CONTROL: PASSED

==============================================================================
NM-1  App K sec.1.1 / Letter 27 / App AZ7: 'A sublattice = corners, B sublattice = body centres' (bipartite labels; 8 A-B bonds)
==============================================================================
  Decorated structure as written: identical sites; A at (n1,n2,n3) , B at (n1+1/2,n2+1/2,n3+1/2);
  only the 8 bonds delta = (+-1/2,+-1/2,+-1/2) are declared. Two readings, both derived.
  (i) labels only (no physical difference between A and B):
  [NM-1(i) generic c/a]
    sublattice-preserving ops: 16   sublattice-exchanging ops: 16
    (a) exchanged by pure lattice translation : YES (1/2,1/2,1/2)
    (b) exchanged by inversion about a point  : YES, centre at (1/4,1/4,1/4)
    (c) exchanged by rotation/rotoinversion   : 14 ops {'2 screw/glide': 3, 'm screw/glide': 5, '2 point-type': 2, '-4 point-type': 2, '4 screw/glide': 2}
    => DEGENERATE (translation)
  PASS  NM-1(i): A and B exchanged by a pure translation -> DEGENERATE
  [NM-1(i) generic c/a: bare BCT] ops per input-lattice cell: 16; point group D4h (4/mmm) (order 16); extra pure translations beyond input lattice: 0 []; ops that are screw/glide for every lattice representative: 0
    surviving operations (16; tetragonal frame, modulo I-centring (0,0,0; 1/2,1/2,1/2)):
      -x,-y,-z                   -x,-y,z                    -x,y,-z                    -x,y,z
      -y,-x,-z                   -y,-x,z                    -y,x,-z                    -y,x,z
      x,-y,-z                    x,-y,z                     x,y,-z                     x,y,z
      y,-x,-z                    y,-x,z                     y,x,-z                     y,x,z
    fingerprint: lattice I (tetragonal description); point group D4h (4/mmm); 16 ops; screw/glide ops 0; 4-fold about c point-type; 2 along a point-type; plane normal to c point-type; normal to a point-type; normal to [110] point-type; inversion present
    corner -> body-centre by the PURE translation (1/2,1/2,1/2) is a symmetry of this decorated structure: YES
  PASS  NM-1(i) generic c/a: I lattice, D4h, symmorphic -> I4/mmm (No. 139)
  [NM-1(i) c/a = sqrt2: bare BCT = FCC] ops per input-lattice cell: 48; point group Oh (m-3m) (order 48); extra pure translations beyond input lattice: 0 []; ops that are screw/glide for every lattice representative: 0
    surviving operations (48; cubic frame, modulo F-centring (0,0,0; 0,1/2,1/2; 1/2,0,1/2; 1/2,1/2,0)):
      -x,-y,-z                   -x,-y,z                    -x,-z,-y                   -x,-z,y
      -x,y,-z                    -x,y,z                     -x,z,-y                    -x,z,y
      -y,-x,-z                   -y,-x,z                    -y,-z,-x                   -y,-z,x
      -y,x,-z                    -y,x,z                     -y,z,-x                    -y,z,x
      -z,-x,-y                   -z,-x,y                    -z,-y,-x                   -z,-y,x
      -z,x,-y                    -z,x,y                     -z,y,-x                    -z,y,x
      x,-y,-z                    x,-y,z                     x,-z,-y                    x,-z,y
      x,y,-z                     x,y,z                      x,z,-y                     x,z,y
      y,-x,-z                    y,-x,z                     y,-z,-x                    y,-z,x
      y,x,-z                     y,x,z                      y,z,-x                     y,z,x
      z,-x,-y                    z,-x,y                     z,-y,-x                    z,-y,x
      z,x,-y                     z,x,y                      z,y,-x                     z,y,x
    fingerprint: lattice I (tetragonal description); point group Oh (m-3m); 48 ops; screw/glide ops 0; 4-fold about c point-type; 2 along a point-type; plane normal to c point-type; normal to a point-type; normal to [110] point-type; inversion present
    corner -> body-centre by the PURE translation (1/2,1/2,1/2) is a symmetry of this decorated structure: YES
  PASS  NM-1(i) c/a = sqrt2: O_h, symmorphic, 48 ops per primitive cell -> Fm-3m (No. 225)
  (ii) the 8 declared A-B bonds kept as a decoration (bond midpoints marked), in-plane A-A contacts unmarked:
  [NM-1(ii) c/a = sqrt2, O_h candidates] ops per input-lattice cell: 16; point group D4h (4/mmm) (order 16); extra pure translations beyond input lattice: 0 []; ops that are screw/glide for every lattice representative: 0
    surviving operations (16; tetragonal frame, modulo I-centring (0,0,0; 1/2,1/2,1/2)):
      -x,-y,-z                   -x,-y,z                    -x,y,-z                    -x,y,z
      -y,-x,-z                   -y,-x,z                    -y,x,-z                    -y,x,z
      x,-y,-z                    x,-y,z                     x,y,-z                     x,y,z
      y,-x,-z                    y,-x,z                     y,x,-z                     y,x,z
    fingerprint: lattice I (tetragonal description); point group D4h (4/mmm); 16 ops; screw/glide ops 0; 4-fold about c point-type; 2 along a point-type; plane normal to c point-type; normal to a point-type; normal to [110] point-type; inversion present
    corner -> body-centre by the PURE translation (1/2,1/2,1/2) is a symmetry of this decorated structure: YES
  PASS  NM-1(ii): marking only the 8 A-B bonds lowers Fm-3m to I4/mmm (No. 139) even at sqrt2, and the body-centring translation survives
  [NM-1(ii) A vs B with bonds as host]
    sublattice-preserving ops: 16   sublattice-exchanging ops: 16
    (a) exchanged by pure lattice translation : YES (1/2,1/2,1/2)
    (b) exchanged by inversion about a point  : YES, centre at (1/4,1/4,1/4)
    (c) exchanged by rotation/rotoinversion   : 14 ops {'2 screw/glide': 3, 'm screw/glide': 5, '2 point-type': 2, '-4 point-type': 2, '4 screw/glide': 2}
    => DEGENERATE (translation)
  PASS  NM-1(ii): A and B still exchanged by a pure translation -> DEGENERATE

==============================================================================
NM-2  App L sec.4.3: 'right-handed on A, left-handed on B' (staggered Weyl components)
==============================================================================
  Decorated structure as written: A = corners carry handedness R, B = body centres carry L. No positions,
  vectors or axes beyond that. Handedness is a pseudoscalar (+1 / -1): it changes sign under improper operations.
  Bare site sets (ignoring the label): related by the pure translation (1/2,1/2,1/2) -- see NM-1(i).
  [NM-2 generic c/a: R-sites vs L-sites, label transforming as a pseudoscalar]
    sublattice-preserving ops: 8   sublattice-exchanging ops: 8
    (a) exchanged by pure lattice translation : NO
    (b) exchanged by inversion about a point  : YES, centre at (1/4,1/4,1/4)
    (c) exchanged by rotation/rotoinversion   : 7 ops {'m screw/glide': 5, '-4 point-type': 2}
    => DEGENERATE (inversion)
  PASS  NM-2 generic c/a: no pure translation maps the R sublattice onto the L sublattice with labels respected
  PASS  NM-2 generic c/a: inversion (centre (1/4,1/4,1/4)) DOES -> DEGENERATE (inversion)
  [NM-2 generic c/a: handedness as pseudoscalar] ops per input-lattice cell: 16; point group D4h (4/mmm) (order 16); extra pure translations beyond input lattice: 0 []; ops that are screw/glide for every lattice representative: 5
    surviving operations (16; tetragonal frame, primitive lattice):
      -x+1/2,-y+1/2,-z+1/2       -x+1/2,y+1/2,z+1/2         -x,-y,z                    -x,y,-z
      -y+1/2,-x+1/2,z+1/2        -y+1/2,x+1/2,-z+1/2        -y,-x,-z                   -y,x,z
      x+1/2,-y+1/2,z+1/2         x+1/2,y+1/2,-z+1/2         x,-y,-z                    x,y,z
      y+1/2,-x+1/2,-z+1/2        y+1/2,x+1/2,z+1/2          y,-x,z                     y,x,-z
    fingerprint: lattice P (tetragonal description); point group D4h (4/mmm); 16 ops; screw/glide ops 5; 4-fold about c point-type; 2 along a point-type; plane normal to c glide/screw; normal to a glide/screw; normal to [110] glide/screw; inversion present
    corner -> body-centre by the PURE translation (1/2,1/2,1/2) is a symmetry of this decorated structure: NO
  PASS  NM-2 generic c/a: P lattice, D4h, 16 ops; 4 and 2(a) point-type; planes normal to c, a and [110] all glides; inversion present; body-centring demoted from translation -> P4/nnc (No. 126), sites on 2a (422)
  PASS  NM-2 generic c/a: there is NO 4_2 (or any) screw axis along c: every 4-fold operation is point-type
  [NM-2 c/a = sqrt2: R-sites vs L-sites, label transforming as a pseudoscalar]
    sublattice-preserving ops: 8   sublattice-exchanging ops: 8
    (a) exchanged by pure lattice translation : NO
    (b) exchanged by inversion about a point  : YES, centre at (1/4,1/4,1/4)
    (c) exchanged by rotation/rotoinversion   : 7 ops {'m screw/glide': 5, '-4 point-type': 2}
    => DEGENERATE (inversion)
  PASS  NM-2 c/a = sqrt2: no pure translation maps the R sublattice onto the L sublattice with labels respected
  PASS  NM-2 c/a = sqrt2: inversion (centre (1/4,1/4,1/4)) DOES -> DEGENERATE (inversion)
  [NM-2 c/a = sqrt2: handedness as pseudoscalar] ops per input-lattice cell: 16; point group D4h (4/mmm) (order 16); extra pure translations beyond input lattice: 0 []; ops that are screw/glide for every lattice representative: 5
    surviving operations (16; tetragonal frame, primitive lattice):
      -x+1/2,-y+1/2,-z+1/2       -x+1/2,y+1/2,z+1/2         -x,-y,z                    -x,y,-z
      -y+1/2,-x+1/2,z+1/2        -y+1/2,x+1/2,-z+1/2        -y,-x,-z                   -y,x,z
      x+1/2,-y+1/2,z+1/2         x+1/2,y+1/2,-z+1/2         x,-y,-z                    x,y,z
      y+1/2,-x+1/2,-z+1/2        y+1/2,x+1/2,z+1/2          y,-x,z                     y,x,-z
    fingerprint: lattice P (tetragonal description); point group D4h (4/mmm); 16 ops; screw/glide ops 5; 4-fold about c point-type; 2 along a point-type; plane normal to c glide/screw; normal to a glide/screw; normal to [110] glide/screw; inversion present
    corner -> body-centre by the PURE translation (1/2,1/2,1/2) is a symmetry of this decorated structure: NO
  PASS  NM-2 c/a = sqrt2: P lattice, D4h, 16 ops; 4 and 2(a) point-type; planes normal to c, a and [110] all glides; inversion present; body-centring demoted from translation -> P4/nnc (No. 126), sites on 2a (422)
  PASS  NM-2 c/a = sqrt2: there is NO 4_2 (or any) screw axis along c: every 4-fold operation is point-type
  Alternative reading (R and L as two plain colours, no pseudoscalar character; this is also the structure
  described by the sublattice sign operators sigma_z (App L sec.1) and Gamma = diag(+1,-1) (App N sec.N.3.1)):
  [NM-2 alt: two scalar labels] ops per input-lattice cell: 16; point group D4h (4/mmm) (order 16); extra pure translations beyond input lattice: 0 []; ops that are screw/glide for every lattice representative: 0
    surviving operations (16; tetragonal frame, primitive lattice):
      -x,-y,-z                   -x,-y,z                    -x,y,-z                    -x,y,z
      -y,-x,-z                   -y,-x,z                    -y,x,-z                    -y,x,z
      x,-y,-z                    x,-y,z                     x,y,-z                     x,y,z
      y,-x,-z                    y,-x,z                     y,x,-z                     y,x,z
    fingerprint: lattice P (tetragonal description); point group D4h (4/mmm); 16 ops; screw/glide ops 0; 4-fold about c point-type; 2 along a point-type; plane normal to c point-type; normal to a point-type; normal to [110] point-type; inversion present
    corner -> body-centre by the PURE translation (1/2,1/2,1/2) is a symmetry of this decorated structure: NO
  PASS  NM-2 alt: P lattice, D4h, symmorphic -> P4/mmm (No. 123) (CuAu-I / L1_0 type ordering); then no operation exchanges the two labels at all
  The formula written in the same passage, eta_stag = sum over k in {0,1}^3 of (-1)^(k1+k2+k3):
  PASS  NM-2: the eight signs sum to zero, as the source states
    read on the two actual sites of the cell (k = 000 at the corner, k = 111 at the body centre, in half-cell
    units) it gives sign +1 on A and -1 on B: the two-colour reading just derived.
    read instead as a checkerboard sign (-1)^(n1+n2+n3) on the corner lattice alone (the source gives no
    value for body centres in that reading): doubled cell 2a x 2a x 2c, like signs on an F-centred lattice.
  [NM-2 checkerboard reading: + sites vs - sites]
    sublattice-preserving ops: 16   sublattice-exchanging ops: 16
    (a) exchanged by pure lattice translation : YES (0,0,1/2)
    (b) exchanged by inversion about a point  : YES, centre at (0,0,1/4)
    (c) exchanged by rotation/rotoinversion   : 14 ops {'2 point-type': 5, 'm point-type': 3, 'm screw/glide': 2, '-4 point-type': 2, '4 point-type': 2}
    => DEGENERATE (translation)
  PASS  NM-2 checkerboard reading: + and - sites are exchanged by a pure translation -> DEGENERATE
  [NM-2 checkerboard reading, two colours] ops per input-lattice cell: 16; point group D4h (4/mmm) (order 16); extra pure translations beyond input lattice: 0 []; ops that are screw/glide for every lattice representative: 0
  PASS  NM-2 checkerboard reading: F-centred tetragonal cell, D4h, symmorphic -> F4/mmm, i.e. I4/mmm (No. 139) in its standard cell

==============================================================================
NM-3  App D.1 sec.3 / Monograph sec.2 / OneMedium: oct void 'corner group' vs 'body-centre group';  Letter 127: 'octahedral void has a preferred orientation (the z-axis)'
==============================================================================
  Decorated structure as written: each oct void carries a distinguished axis along c (its two axial
  neighbours vs its four equatorial neighbours). Modelled as a director (headless axis) (0,0,1) on every oct void.
  [NM-3 c/a = sqrt2: oct void (1/2,1/2,0) vs oct void (0,0,1/2), directors along c]
    sublattice-preserving ops: 16   sublattice-exchanging ops: 16
    (a) exchanged by pure lattice translation : YES (1/2,1/2,1/2)
    (b) exchanged by inversion about a point  : YES, centre at (1/4,1/4,1/4)
    (c) exchanged by rotation/rotoinversion   : 14 ops {'2 screw/glide': 3, 'm screw/glide': 5, '2 point-type': 2, '-4 point-type': 2, '4 screw/glide': 2}
    => DEGENERATE (translation)
  PASS  NM-3: the two oct voids of the cell, with their c-directors, are exchanged by a pure translation -> DEGENERATE
  [NM-3 c/a = sqrt2, O_h candidates] ops per input-lattice cell: 16; point group D4h (4/mmm) (order 16); extra pure translations beyond input lattice: 0 []; ops that are screw/glide for every lattice representative: 0
    surviving operations (16; tetragonal frame, modulo I-centring (0,0,0; 1/2,1/2,1/2)):
      -x,-y,-z                   -x,-y,z                    -x,y,-z                    -x,y,z
      -y,-x,-z                   -y,-x,z                    -y,x,-z                    -y,x,z
      x,-y,-z                    x,-y,z                     x,y,-z                     x,y,z
      y,-x,-z                    y,-x,z                     y,x,-z                     y,x,z
    fingerprint: lattice I (tetragonal description); point group D4h (4/mmm); 16 ops; screw/glide ops 0; 4-fold about c point-type; 2 along a point-type; plane normal to c point-type; normal to a point-type; normal to [110] point-type; inversion present
    corner -> body-centre by the PURE translation (1/2,1/2,1/2) is a symmetry of this decorated structure: YES
  PASS  NM-3: a c-director on every oct void lowers Fm-3m to I4/mmm (No. 139); symmorphic; body-centring translation survives
  Who is 'corner' and who is 'body centre' around each void:
    void (1/2,1/2,0): equatorial neighbours ['(0,0,0)']  axial ['(1/2,1/2,1/2)']
    void (0,0,1/2)  : equatorial neighbours ['(1/2,1/2,1/2)']  axial ['(0,0,0)']
  PASS  NM-3: around void (1/2,1/2,0) the equatorial four are corners and the axial two are body centres; around void (0,0,1/2) the roles are swapped -- i.e. the two pictures are images under the body-centring translation

==============================================================================
NM-4  oct voids vs tet voids given different labels: App D.3 sec.4.2 ('tet and oct voids alternate'), Letter 30 (u on oct, d on tet), App Y (left-handed oct doublet / right-handed tet component), Letter 62 (OHC in oct voids, TVC in tet voids), App BK and Vol.1 Part 2 p.342 (u/d vs tet/oct, reversed), Vol.2 ('tetrahedral void is the parity-odd void'), WikiChallenge (oct left-handed, tet right-handed)
==============================================================================
  Decorated structure as written: label X on every oct void, label Y on every tet void (both tet sets alike).
  per primitive cell: 1 oct void, 2 tet voids
  [NM-4 c/a = sqrt2: oct set vs one tet set (spheres + other tet set as host)]
    sublattice-preserving ops: 24   sublattice-exchanging ops: 0
    (a) exchanged by pure lattice translation : NO
    (b) exchanged by inversion about a point  : NO
    (c) exchanged by rotation/rotoinversion   : 0 ops
    => NO EXCHANGE SYMMETRY (sublattices inequivalent: ferri-type, not compensated by symmetry)
  PASS  NM-4: NO operation of any kind exchanges the oct sublattice with a tet sublattice (inequivalent sites)
  [NM-4 scalar labels, c/a = sqrt2] ops per input-lattice cell: 48; point group Oh (m-3m) (order 48); extra pure translations beyond input lattice: 0 []; ops that are screw/glide for every lattice representative: 0
    surviving operations (48; cubic frame, modulo F-centring (0,0,0; 0,1/2,1/2; 1/2,0,1/2; 1/2,1/2,0)):
      -x,-y,-z                   -x,-y,z                    -x,-z,-y                   -x,-z,y
      -x,y,-z                    -x,y,z                     -x,z,-y                    -x,z,y
      -y,-x,-z                   -y,-x,z                    -y,-z,-x                   -y,-z,x
      -y,x,-z                    -y,x,z                     -y,z,-x                    -y,z,x
      -z,-x,-y                   -z,-x,y                    -z,-y,-x                   -z,-y,x
      -z,x,-y                    -z,x,y                     -z,y,-x                    -z,y,x
      x,-y,-z                    x,-y,z                     x,-z,-y                    x,-z,y
      x,y,-z                     x,y,z                      x,z,-y                     x,z,y
      y,-x,-z                    y,-x,z                     y,-z,-x                    y,-z,x
      y,x,-z                     y,x,z                      y,z,-x                     y,z,x
      z,-x,-y                    z,-x,y                     z,-y,-x                    z,-y,x
      z,x,-y                     z,x,y                      z,y,-x                     z,y,x
    fingerprint: lattice I (tetragonal description); point group Oh (m-3m); 48 ops; screw/glide ops 0; 4-fold about c point-type; 2 along a point-type; plane normal to c point-type; normal to a point-type; normal to [110] point-type; inversion present
    corner -> body-centre by the PURE translation (1/2,1/2,1/2) is a symmetry of this decorated structure: YES
  PASS  NM-4 (scalar labels / occupancy): Fm-3m (No. 225) unchanged; body-centring translation survives
  [NM-4 scalar labels, generic c/a] ops per input-lattice cell: 16; point group D4h (4/mmm) (order 16); extra pure translations beyond input lattice: 0 []; ops that are screw/glide for every lattice representative: 0
    surviving operations (16; tetragonal frame, modulo I-centring (0,0,0; 1/2,1/2,1/2)):
      -x,-y,-z                   -x,-y,z                    -x,y,-z                    -x,y,z
      -y,-x,-z                   -y,-x,z                    -y,x,-z                    -y,x,z
      x,-y,-z                    x,-y,z                     x,y,-z                     x,y,z
      y,-x,-z                    y,-x,z                     y,x,-z                     y,x,z
    fingerprint: lattice I (tetragonal description); point group D4h (4/mmm); 16 ops; screw/glide ops 0; 4-fold about c point-type; 2 along a point-type; plane normal to c point-type; normal to a point-type; normal to [110] point-type; inversion present
    corner -> body-centre by the PURE translation (1/2,1/2,1/2) is a symmetry of this decorated structure: YES
  PASS  NM-4 (scalar labels), generic c/a: I4/mmm (No. 139)
  [NM-4 handedness as pseudoscalar (oct L, all tets R), c/a = sqrt2] ops per input-lattice cell: 24; point group O (432) (order 24); extra pure translations beyond input lattice: 0 []; ops that are screw/glide for every lattice representative: 0
    surviving operations (24; cubic frame, modulo F-centring (0,0,0; 0,1/2,1/2; 1/2,0,1/2; 1/2,1/2,0)):
      -x,-y,z                    -x,-z,-y                   -x,y,-z                    -x,z,y
      -y,-x,-z                   -y,-z,x                    -y,x,z                     -y,z,-x
      -z,-x,y                    -z,-y,-x                   -z,x,-y                    -z,y,x
      x,-y,-z                    x,-z,y                     x,y,z                      x,z,-y
      y,-x,z                     y,-z,-x                    y,x,-z                     y,z,x
      z,-x,-y                    z,-y,x                     z,x,y                      z,y,-x
    fingerprint: lattice I (tetragonal description); point group O (432); 24 ops; screw/glide ops 0; 4-fold about c point-type; 2 along a point-type; plane normal to c absent; normal to a absent; normal to [110] absent; inversion absent
    corner -> body-centre by the PURE translation (1/2,1/2,1/2) is a symmetry of this decorated structure: YES
  PASS  NM-4 (handedness as pseudoscalar): only the 24 proper operations survive, symmorphic -> F432 (No. 209); body-centring translation survives
  [NM-4 handedness as pseudoscalar, generic c/a] ops per input-lattice cell: 8; point group D4 (422) (order 8); extra pure translations beyond input lattice: 0 []; ops that are screw/glide for every lattice representative: 0
    surviving operations (8; tetragonal frame, modulo I-centring (0,0,0; 1/2,1/2,1/2)):
      -x,-y,z                    -x,y,-z                    -y,-x,-z                   -y,x,z
      x,-y,-z                    x,y,z                      y,-x,z                     y,x,-z
    fingerprint: lattice I (tetragonal description); point group D4 (422); 8 ops; screw/glide ops 0; 4-fold about c point-type; 2 along a point-type; plane normal to c absent; normal to a absent; normal to [110] absent; inversion absent
    corner -> body-centre by the PURE translation (1/2,1/2,1/2) is a symmetry of this decorated structure: YES
  PASS  NM-4 (handedness as pseudoscalar), generic c/a: I422 (No. 97)

==============================================================================
NM-5  App Q.5: '2 tetrahedral voids (up-type and down-type) ... 2 per unit cell, related by the C4v rotation'; Vol.2 p.333: 'two tetrahedral voids per BCT unit cell (above and below the ab-plane)'
==============================================================================
  Decorated structure as written: tet set T1 = (1/2,0,1/4)+BCT, tet set T2 = (0,1/2,1/4)+BCT (the C4 image).
  PASS  NM-5: C4 about c through a sphere maps T1 onto T2
  PASS  NM-5: the mirror z -> -z through a sphere ('above and below the ab-plane') also maps T1 onto T2
  [NM-5 generic c/a: T1 vs T2 (spheres as host)]
    sublattice-preserving ops: 8   sublattice-exchanging ops: 8
    (a) exchanged by pure lattice translation : NO
    (b) exchanged by inversion about a point  : YES, centre at (0,0,0)
    (c) exchanged by rotation/rotoinversion   : 7 ops {'2 point-type': 2, 'm point-type': 3, '4 point-type': 2}
    => DEGENERATE (inversion)
  PASS  NM-5 generic c/a: T1 and T2 are NOT related by a pure translation
  PASS  NM-5 generic c/a: they ARE related by inversion -> DEGENERATE (inversion)
  PASS  NM-5 generic c/a: they are also related by 4-fold rotations, all point-type (no screw)
  [NM-5 c/a = sqrt2: T1 vs T2 (spheres as host)]
    sublattice-preserving ops: 24   sublattice-exchanging ops: 24
    (a) exchanged by pure lattice translation : NO
    (b) exchanged by inversion about a point  : YES, centre at (0,0,0)
    (c) exchanged by rotation/rotoinversion   : 23 ops {'2 point-type': 6, '-3 point-type': 8, 'm point-type': 3, '4 point-type': 6}
    => DEGENERATE (inversion)
  PASS  NM-5 c/a = sqrt2: T1 and T2 are NOT related by a pure translation
  PASS  NM-5 c/a = sqrt2: they ARE related by inversion -> DEGENERATE (inversion)
  PASS  NM-5 c/a = sqrt2: they are also related by 4-fold rotations, all point-type (no screw)
  [NM-5 both tet sets alike, generic c/a] ops per input-lattice cell: 16; point group D4h (4/mmm) (order 16); extra pure translations beyond input lattice: 0 []; ops that are screw/glide for every lattice representative: 0
    surviving operations (16; tetragonal frame, modulo I-centring (0,0,0; 1/2,1/2,1/2)):
      -x,-y,-z                   -x,-y,z                    -x,y,-z                    -x,y,z
      -y,-x,-z                   -y,-x,z                    -y,x,-z                    -y,x,z
      x,-y,-z                    x,-y,z                     x,y,-z                     x,y,z
      y,-x,-z                    y,-x,z                     y,x,-z                     y,x,z
    fingerprint: lattice I (tetragonal description); point group D4h (4/mmm); 16 ops; screw/glide ops 0; 4-fold about c point-type; 2 along a point-type; plane normal to c point-type; normal to a point-type; normal to [110] point-type; inversion present
    corner -> body-centre by the PURE translation (1/2,1/2,1/2) is a symmetry of this decorated structure: YES
  PASS  NM-5 (T1, T2 alike), generic c/a: I4/mmm (No. 139), tets on 4d
  [NM-5 both tet sets alike, c/a = sqrt2] ops per input-lattice cell: 48; point group Oh (m-3m) (order 48); extra pure translations beyond input lattice: 0 []; ops that are screw/glide for every lattice representative: 0
    surviving operations (48; cubic frame, modulo F-centring (0,0,0; 0,1/2,1/2; 1/2,0,1/2; 1/2,1/2,0)):
      -x,-y,-z                   -x,-y,z                    -x,-z,-y                   -x,-z,y
      -x,y,-z                    -x,y,z                     -x,z,-y                    -x,z,y
      -y,-x,-z                   -y,-x,z                    -y,-z,-x                   -y,-z,x
      -y,x,-z                    -y,x,z                     -y,z,-x                    -y,z,x
      -z,-x,-y                   -z,-x,y                    -z,-y,-x                   -z,-y,x
      -z,x,-y                    -z,x,y                     -z,y,-x                    -z,y,x
      x,-y,-z                    x,-y,z                     x,-z,-y                    x,-z,y
      x,y,-z                     x,y,z                      x,z,-y                     x,z,y
      y,-x,-z                    y,-x,z                     y,-z,-x                    y,-z,x
      y,x,-z                     y,x,z                      y,z,-x                     y,z,x
      z,-x,-y                    z,-x,y                     z,-y,-x                    z,-y,x
      z,x,-y                     z,x,y                      z,y,-x                     z,y,x
    fingerprint: lattice I (tetragonal description); point group Oh (m-3m); 48 ops; screw/glide ops 0; 4-fold about c point-type; 2 along a point-type; plane normal to c point-type; normal to a point-type; normal to [110] point-type; inversion present
    corner -> body-centre by the PURE translation (1/2,1/2,1/2) is a symmetry of this decorated structure: YES
  PASS  NM-5 (T1, T2 alike), c/a = sqrt2: Fm-3m (No. 225), tets on 8c
  [NM-5 T1 = 'up-type', T2 = 'down-type' as distinct scalar labels, generic c/a] ops per input-lattice cell: 8; point group D2d (-42m) (order 8); extra pure translations beyond input lattice: 0 []; ops that are screw/glide for every lattice representative: 0
    surviving operations (8; tetragonal frame, modulo I-centring (0,0,0; 1/2,1/2,1/2)):
      -x,-y,z                    -x,y,z                     -y,-x,-z                   -y,x,-z
      x,-y,z                     x,y,z                      y,-x,-z                    y,x,-z
    fingerprint: lattice I (tetragonal description); point group D2d (-42m); 8 ops; screw/glide ops 0; 4-fold about c absent; 2 along a absent; plane normal to c absent; normal to a point-type; normal to [110] absent; inversion absent
    corner -> body-centre by the PURE translation (1/2,1/2,1/2) is a symmetry of this decorated structure: YES
  PASS  NM-5 (distinct labels), generic c/a: I lattice, D2d, symmorphic, mirrors normal to a kept, diagonal mirrors lost -> I-4m2 (No. 119); body-centring translation survives
  [NM-5 distinct scalar labels, c/a = sqrt2] ops per input-lattice cell: 24; point group Td (-43m) (order 24); extra pure translations beyond input lattice: 0 []; ops that are screw/glide for every lattice representative: 0
    surviving operations (24; cubic frame, modulo F-centring (0,0,0; 0,1/2,1/2; 1/2,0,1/2; 1/2,1/2,0)):
      -x,-y,z                    -x,-z,y                    -x,y,-z                    -x,z,-y
      -y,-x,z                    -y,-z,x                    -y,x,-z                    -y,z,-x
      -z,-x,y                    -z,-y,x                    -z,x,-y                    -z,y,-x
      x,-y,-z                    x,-z,-y                    x,y,z                      x,z,y
      y,-x,-z                    y,-z,-x                    y,x,z                      y,z,x
      z,-x,-y                    z,-y,-x                    z,x,y                      z,y,x
    fingerprint: lattice I (tetragonal description); point group Td (-43m); 24 ops; screw/glide ops 0; 4-fold about c absent; 2 along a absent; plane normal to c absent; normal to a point-type; normal to [110] absent; inversion absent
    corner -> body-centre by the PURE translation (1/2,1/2,1/2) is a symmetry of this decorated structure: YES
  PASS  NM-5 (distinct labels), c/a = sqrt2: F lattice, T_d, symmorphic -> F-43m (No. 216); body-centring translation survives

==============================================================================
NEAR-MISS SUMMARY: is the corner -> body-centre operation ever a screw or glide that is not reducible to a translation or an inversion?
==============================================================================
  NM-1  translation                       -> degenerate
  NM-2  inversion (translation for bare sites); glides present but inversion present too; no screw -> degenerate
  NM-3  translation                       -> degenerate
  NM-4  translation (oct/tet never exchanged by anything) -> not a compensated pair
  NM-5  translation for the spheres; T1<->T2 by inversion -> degenerate

==============================================================================
CROSSCHECK (non-gating)  operation sets vs tabulated space-group operations (spglib database)
==============================================================================
  MATCH     control MnF2 (rutile): 16 ops found vs 16 tabulated for P 4_2/m 2_1/n 2/m (No. 136, Hall 419)
  MATCH     NM-1(i)/NM-5 bare BCT, generic c/a: 16 ops found vs 16 tabulated for I 4/m 2/m 2/m (No. 139, Hall 424)
  MATCH     NM-1(i) bare BCT at c/a = sqrt2: 48 ops found vs 48 tabulated for F 4/m -3 2/m (No. 225, Hall 523)
  MATCH     NM-2 handedness staggered (pseudoscalar), generic c/a: 16 ops found vs 16 tabulated for P 4/n 2/n 2/c (No. 126, origin choice 1, Hall 404)
  MATCH     NM-2 handedness staggered (pseudoscalar), c/a = sqrt2: 16 ops found vs 16 tabulated for P 4/n 2/n 2/c (No. 126, origin choice 1, Hall 404)
  MATCH     NM-2 alt two scalar labels: 16 ops found vs 16 tabulated for P 4/m 2/m 2/m (No. 123, Hall 400)
  MATCH     NM-3 c-director on oct voids, c/a = sqrt2: 16 ops found vs 16 tabulated for I 4/m 2/m 2/m (No. 139, Hall 424)
  MATCH     NM-4 scalar labels, c/a = sqrt2: 48 ops found vs 48 tabulated for F 4/m -3 2/m (No. 225, Hall 523)
  MATCH     NM-4 pseudoscalar handedness, c/a = sqrt2: 24 ops found vs 24 tabulated for F 4 3 2 (No. 209, Hall 505)
  MATCH     NM-4 pseudoscalar handedness, generic c/a: 8 ops found vs 8 tabulated for I 4 2 2 (No. 97, Hall 374)
  MATCH     NM-5 distinct tet labels, generic c/a: 8 ops found vs 8 tabulated for I -4 m 2 (No. 119, Hall 396)
  MATCH     NM-5 distinct tet labels, c/a = sqrt2: 24 ops found vs 24 tabulated for F -4 3 m (No. 216, Hall 512)
  cross-check: 12 / 12 operation sets identical to the tabulated group
  spglib.get_spacegroup  control MnF2 (c/a = 0.68 as in the real crystal)           -> P4_2/mnm (136)
  spglib.get_spacegroup  bare BCT, c/a = 1.2 (generic)                              -> I4/mmm (139)
  spglib.get_spacegroup  bare BCT, c/a = sqrt2                                      -> Fm-3m (225)
  spglib.get_spacegroup  NM-2 alt two scalar labels, c/a = sqrt2                    -> P4/mmm (123)
  spglib.get_spacegroup  NM-4 scalar labels, c/a = sqrt2                            -> Fm-3m (225)
  spglib.get_spacegroup  NM-5 distinct tet labels, c/a = 1.2                        -> I-4m2 (119)
  spglib.get_spacegroup  NM-5 distinct tet labels, c/a = sqrt2                      -> F-43m (216)
  spglib.get_spacegroup  NM-3 c-axis marked on oct voids by two satellites, sqrt2   -> I4/mmm (139)

==============================================================================
SUMMARY
==============================================================================
  69 / 69 assertions passed
```
