# Gate ALTER — Result

**Programme:** The BCT Superfluid Lattice Model (ZeroFreeParameters, ORCID 0009-0007-9561-9859)
**Run:** 2026-10-01, fresh context, Cold Ledger. No project memory, ledger, prior gate results, `audit/gates/alter_check.py`, or the 2026-10-01 doc "Altermagnetism and the BCT Lattice" were opened.
**Auditor:** Claude (Opus 5.5), single session.
**Tier cap:** none (fresh thread).
**Corpus revision searched:** `0d9600a` (2026-09-30 11:44 UTC, the last commit on or before the cutoff). The three later commits (`7c9323e`, `dfd496a`, `ab693c8`) touch only the ALTER pre-registration files and `alter_check.py`, all excluded. `audit/` was excluded throughout.

**Verdict: SC-ALTER-2 (KILL — absent).** No primary source specifies a decoration under which the corner→body-centre operation is a rotation, screw or glide with no translation or inversion also relating the two sublattices. One sublattice-staggered assignment exists (Appendix L §4.3). It is recorded below and fails the test, because an inversion still relates A and B.

---

## 1. SHA-256 digests

| Item | SHA-256 |
|---|---|
| Card as fetched by `curl` from `raw.githubusercontent.com/.../dfd496a/audit/gates/gate_ALTER_prompt.md` | `3cf882a66d83c503a54a6aa5731c4da0ee7b50fccf019605423bd947bfe35882` |
| Pre-registered digest in `audit/gates/PREREG_20261001.sha256` (at `dfd496a` and at HEAD `ab693c8`) | `3cf882a66d83c503a54a6aa5731c4da0ee7b50fccf019605423bd947bfe35882` |
| Digest supplied in the run instruction | `3cf882a66d83c503a54a6aa5731c4da0ee7b50fccf019605423bd947bfe35882` |
| **Match** | **yes**. The card was opened only after this comparison. |
| `alter_gate_check.py` as delivered | `da625fcd3d3d9d4930e16b627c59f3a0eab1a7d6dcc4b906b61c18be04b59d22` |

`ab693c8` ("PREREG: dedupe") removes a duplicated line from the PREREG file. The digest it records is unchanged.

---

## 2. Obstruction checks (card §3.2): all four PASS

These use exact arithmetic only: `fractions.Fraction`, plus a small exact ℚ(√2) type for the BCT frame. sympy is not installed. The code is Part A of `alter_gate_check.py`, written without reading `alter_check.py`. The script prints 35 PASS lines and 0 FAIL lines across Parts A and C.

**A1. The body-centring vector at c/a = √2 is an FCC lattice vector.**
- Take the BCT frame with a = 1 and c = √2. Rotating 45° about z and scaling by 1/√2 maps a₁ → (½,½,0), a₂ → (½,−½,0), c → (0,0,1) in the cubic frame.
- This map is an exact similarity: the Gram matrices agree up to a factor of 2.
- The body-centring vector (½, ½, √2/2) maps to (½, 0, ½). That is an FCC primitive vector, since its doubled coordinates have an even sum.
- Independent check: the nearest-neighbour shell has exactly 12 equal members, |r|² = 1 in BCT units.
- Control: at c/a = 3/2, |b|² = 17/16 ≠ 1, so the lattice is not FCC.

```python
b = (Q2(1/2), Q2(1/2), R2*1/2)                 # corner -> body-centre, exact
cubic_from_bct(b) == (1/2, 0, 1/2)             # True, rational, no sqrt2 residue
is_int_combo_fcc_cubic((1/2, 0, 1/2))          # True
```

**A2. The octahedral voids form an FCC translate of the sphere sites.**
- The oct set is FCC + (½,0,0), which is the same set as FCC + (½,½,½).
- It is closed under all four FCC coset translations and disjoint from the sphere set.
- Every oct site has exactly 6 sphere neighbours at distance ½ (cube edge 1).

**A3. The tet voids at (¼,¼,¼) and (¾,¾,¾) are related by inversion, not by translation.**
- Their difference, (½,½,½), is not an FCC vector.
- No FCC translation maps T⁺ onto T⁻.
- Inversion through a sphere site preserves the sphere set and maps T⁺ onto T⁻.
- Every tet site has 4 sphere neighbours at |r|² = 3/16.

**A4. Rutile.** Metal atoms sit at (0,0,0) and (½,½,½). O atoms sit at ±(u,u,0), (½+u, ½−u, ½) and (½−u, ½+u, ½).
- Coordinates are treated as exact affine functions of u. Two components a₁+b₁u and a₂+b₂u agree mod 1 for all u exactly when b₁ = b₂ and a₁ − a₂ ∈ ℤ. When b₁ ≠ b₂ they agree only at isolated u, and the script lists every such u inside (0, ½).
- Body-centring translation: it maps metal A to metal B but does **not** map the O set to itself for any 0 < u < ½. There are no accidental coincidences in (0, ½); for example, (u,u,0) → (½+u, ½+u, ½) would need 2u ∈ ℤ.
- 4₂ screw {C₄z | ½,½,½}: it maps A → B, B → A, and the O set onto itself identically in u.
- Spot checks at u = 3/10, 1/7 and 2/5 agree.
- Inversion at the metal site fixes each metal sublattice and does not swap them.

```python
screw = lambda p: translate(C4z(p), (1/2, 1/2, 1/2))
maps_set(tb, Oset, Oset)      # False, and failing_u(...) == [set(), set(), set(), set()]
maps_set(screw, Oset, Oset)   # True for every u in (0, 1/2)
```

Proceeding: no SC-ALTER-4 stop.

---

## 3. Corpus search (card §3.3)

**Scope.** Every `.tex` and every PDF in the tree at `0d9600a`, outside `audit/`, is **primary**. That is 148 documents:
- 113 files under `tex/` plus the root `.tex` Letters and Volumes;
- Appendices Volume 1 Parts 1–3;
- Appendices Volume 2 (inside `BCT_Appendices_Volume2_2026_compressed.zip`, extracted);
- the NPB paper and the SMOKE PDFs.

Every primary document yielded more than 200 characters of text. The 124 `.md` and `.txt` files are reported separately as **secondary**. They are not Letters, Appendices or Volume sections as the card defines them.

**Method.** Case-insensitive regex over `pdftotext -layout` text and raw `.tex`. Proximity terms use a ±3-line window. Every hit's context was read: 1,341 blocks in all, split into four slices and each classified. Candidates were then re-read in full source by the auditor.

**PDF subscript flattening.** `pdftotext` renders 4₂ as `42`. The flattened variants `P42/m`, `42 … screw|axis`, `4₂` and `screw axis` were therefore also searched. They returned 0 hits everywhere.

| Term | Primary hits | Primary files (top) | Secondary hits |
|---|---:|---|---:|
| `orient` | 49 | Vol2 (15), Vol1-P1 (8), L81 (8), L78 (5), KA1 (3), L127 (2), +8 | 1 |
| `rotat` | 159 | Vol1-P1 (65), Vol1-P2 (38), Vol2 (26), Monograph_PLB (8), L114 (5), L68 (4), +12 | 31 |
| `stagger` | 8 | Vol1-P1 (8), all in App L §4 | **0** |
| `sublattice` | 54 | Vol1-P1 (23), Vol2 (10), L68 (5), AZ7 (4), L28 (3+3), +6 | 6 |
| `alternat` | 29 | Vol2 (8), Vol1-P1 (6), Vol1-P2 (3), L115 (2), L210, SMOKE_Description, +8 | 6 |
| `chiral` | 288 | Vol2 (118), Vol1-P2 (83), Vol1-P1 (62), L127 (6), L28 (3+3), +7 | 42 |
| `handed` | 179 | Vol1-P1 (83), Vol2 (60), Vol1-P2 (28), L126 (2), Monograph_PLB (2), Vol1-P3, +3 | 32 |
| `screw` | **0** | **ABSENT** | 4 (outreach prose: "screw", unrelated) |
| `glide` | 1 | L67 (drug-docking software "Glide") | **0** |
| `4_2` (incl. `4₂`, flattened) | **0** | **ABSENT** | **0** |
| `P4_2` (incl. `P4₂`, `P42/m`) | **0** | **ABSENT** | **0** |
| `D_{4h}` | 4 | L127, L128, L30, Monograph_PLB | **0** |
| `D4h` (incl. `D₄h`, `D_4h`) | 191 | Vol2 (185), Vol1-P1 (6) | 8 (Zenodo metadata titles) |
| `decorat` | 1 | Vol16 Philosophy ("decorative") | **0** |
| `occupan` | 6 | L204c, L108, L36 (×2), L82 | **0** |
| `void` ±3 of any above | 201 | Vol2 (73), Vol1-P1 (69), Vol1-P2 (24), L127 (5), L204c (4), L108 (4), +10 | 32 |
| `hopfion` ±3 of sign/±/handed | 4 | Vol3_QCD, KA1, L101, L78 | 4 |
| `winding` ±3 of pattern/arrang | 1 | L125 ("phase pattern", prose) | **0** |

**Absences are findings.** `screw`, `4_2` and `P4_2` are absent from the entire primary corpus. `glide` and `decorat` occur once each, and both are non-crystallographic uses. The corpus never names the operation that altermagnetism on this lattice would require.

### How the hits resolve

**`D4h` / `D_{4h}` (203 blocks).** Every hit falls into one of three groups; none is an A/B-dependent positional pattern (category (e) = 0).
- 26 blocks name the point group of the tetragonal lattice as a whole, or a global "tetragonal distortion":
  - Monograph_PLB:225;
  - Vol2 App JG6, Phase 67C;
  - Vol2 App IM5, IQ5, IV5;
  - Vol2 JZ6, Phase 80A: "O_h … broken to D4h by the BCT tetragonal distortion";
  - L30:86.
- 134 blocks are flavour or representation labels: generations labelled A1g, B1g, A2g, and C₄ phases assigned per irrep (Yukawa IQ5, CKM IV5, Majorana IY5, leptogenesis IM5). This is generation space, not real-space positions.
- The remainder are tables of contents, titles, or prose.

The "four-phase crystal" of App IX5 (Phase 74C) and App JH6 (Phase 76C) consists of four **global** crystal orientations, one per Hubble-volume domain. It assigns nothing to corner or body-centre sites.

**`chiral` / `handed` (541 blocks).**
- About 430 are particle-physics chirality.
- About 50 are global lattice, hopfion or void-type chirality. Examples are the OHC handedness attributed to "the D4 lattice c/a = √2 asymmetry" and T_d chirality.
- About 10 are internal space.
- About 50 are prose or index entries.
- **1 assigns chirality per sublattice: App L §4.3.** See §4.

**`orient`, `rotat`, `stagger`, `alternat`, `glide`, `decorat`, `occupan`, `screw` (295 blocks).** Category (e) = 0.
- All 8 `stagger` hits are App L §4 (same passage).
- The oct/tet void "alternation" (Vol1-P1:1736, Vol2:27749) alternates between void *types* in the NaCl-type void network. It does not alternate between sublattices.

**`sublattice`, `void`-proximity, `hopfion`, `winding` (302 blocks).** Category (e) = 0. "Sublattice" is used in five senses:
- the BCT A/B bipartition (App K, App L, App Z, AZ7, K_GreenFunction);
- D4 root sub-lattices;
- the oct and tet void classes;
- meson "void sublattices" (L28, non-spatial);
- 2-D hexagonal sub-lattices (L68, L120).

**Secondary tier.** The same four readers examined all secondary blocks. No positional sublattice-dependent pattern was found. Secondary sources could not count toward SC-ALTER-1 in any case.

### Sub-question answers

1. **Void orientation: NO.**
   - The only void orientation stated is Letter 127 (`tex/BCT_Letter127_EWQCDScales.tex`:250–252, repeated in v2:274 and L128:222): the octahedral void has a preferred orientation along the tetragonal z-axis, while the tetrahedral void is orientation-symmetric. This applies identically to every oct void, so it is sublattice-symmetric (tested as control C2 in §4).
   - Occupancy asymmetries (L30:85–86: u-type quarks to oct voids, d-type to tet voids; Vol1-P1:16023–16029) are assigned by **void type**, not by sublattice.
   - Citation for sublattice-dependent void orientation: **NONE FOUND.**
2. **Hopfion / vortex handedness: NO.**
   - OHC handedness is global: Zenodo L194–L202 guide:35 (L195), and L220.
   - Hopfion H = ±1 is a per-mode sign (spin up/down), not a per-site sign: KA1:18, L78:47, L81:80.
   - Monograph_PLB:1565 describes two chiralities "determined by the vortex winding direction" per excitation, with no positions.
   - App Z (Vol1-P1:10181, 10277) has a vortex tunnelling between A and B, with no chirality attached to either site.
   - Citation for staggered hopfion or vortex chirality: **NONE FOUND.**
3. **S¹ winding pattern: NO.**
   - App G (Vol1-P1:4300–4460): windings are assigned per particle (q_e = 1; quarks magnitude-uniform at ⅓).
   - App X (Vol1-P1:8912–9010): three winding axes inside one tet void become three colour charges, with n_r + n_g + n_b ≡ 0 (mod 3). This is colour internal space and is excluded by the §4 guard.
   - Neither appendix places windings on lattice sites.
   - Citation for a sublattice-alternating winding pattern: **NONE FOUND.**

---

## 4. Candidates: point set, symmetry test, classification (card §3.4)

This is Part C of the script. It works in the cubic frame with cube edge 1, where the BCT corners A are FCC points with z ∈ ℤ and the body-centres B are FCC points with z ∈ ℤ+½. It enumerates all 48 × 64 affine operations x ↦ Rx + t with R ∈ O_h (signed permutations) and t ∈ {0, ¼, ½, ¾}³. It keeps those that preserve the decorated structure and classifies each coset representative modulo the A-lattice. Only structures the corpus states are constructed, plus labelled controls.

| # | Source | Decorated point set (cubic frame) | A→B operations present | Classification |
|---|---|---|---|---|
| C0 | control: bare sphere lattice | FCC, A = z∈ℤ layers, B = z∈ℤ+½ layers | 48 cosets, **including a pure translation** (½,0,½) | degenerate (Fm-3m; the theorem of card §0) |
| **C1** | **App L §4.3** (Vol1-P1:6451–6452) | A sites at (0,0,0), (½,½,0) + A-lattice carry **R**; B sites at (½,0,½), (0,½,½) + A-lattice carry **L**. Handedness is a pseudoscalar, flipping under det R = −1. | 8 cosets: **inversion ×1** (centre (¼,0,¼), the A–B bond midpoint), glide ×5, 4̄ ×2. **No** translation. A→A subgroup is proper only (422). | **degenerate (inversion)**. Space group **P4/nnc (No. 126)**, origin choice 1: 422 at the A site, inversion at (¼,¼,¼) in tetragonal axes. |
| C1′ | same passage, reading R/L as the staggered "spin-like" label | the parent structure carrying it is C0 | pure translation | degenerate |
| C1″ | control: same labels as plain scalars | L1₀ (CuAu-type) layering | none. A and B are distinct species. | P4/mmm (No. 123). Not a sublattice relation at all. |
| C2 | Letter 127 (control of the "global" class) | a headless director ∥ z on every oct void | 16 cosets, **including a pure translation** | degenerate (uniform decoration is sublattice-symmetric) |

**Reading of C1.** The App L assignment does demote the body-centring translation: no pure translation maps A to B once R and L are placed. But the structure keeps an inversion centre at every A–B bond midpoint, and that inversion maps A(R) onto B(L). By the card's classification rule, *inversion → degenerate*. By the altermagnet criterion itself, the opposite-sublattice partners must be related by no translation **and** no inversion, and this pattern fails the second condition. The 5 glides and 2 rotoinversions present in the same coset do not rescue it; with inversion also present, the structure is PT-symmetric and not altermagnetic. Read either way (C1 or C1′), the pattern is degenerate.

It is also not a pattern of the kind the card seeks. It is an assignment of fermion (Weyl) components, not an orientation, shape or occupancy of voids, hopfions or windings. It involves no 90° rotation about c.

**Script output (Part C, abridged):**
```
[obs] NN of a corner site at c/a=sqrt2: A-A = 4, A-B = 8, total 12
C1: A->A {'translation':1, '2-fold screw':2, '2-fold rotation':3, '4-fold rotation':2}
    A->B {'glide':5, 'inversion':1, '-4 rotoinversion':2}
    inversion op: x -> -x + (1/2,0,1/2), centre at (1/4,0,1/4) (A-B bond midpoint)
[PASS] C1 inversion centre at (1/4,1/4,1/4) in tetragonal axes, 422 at origin -> P4/nnc (No.126, origin 1)
```

---

## 5. Provenance (card §3.5)

| Candidate | First appearance | Dated ≤ 2026-09-30? | Derived or posited | A/B assignment forced or free | Post-cutoff text? |
|---|---|---|---|---|---|
| C1, App L §4.3 "right-handed on A, left-handed on B" | Appendices Volume 1 (2026), Part 1, p. 131, "Appendix L — The Lattice of Resonance — Draft". The PDF was added to the repo 2026-09-12 (`0e27590`); the appendix itself carries no date. | yes (upper bound 2026-09-12) | **posited** ("naturally distributes"), no derivation | **free**, in two ways. (i) R↔L is a global ± and is allowed. (ii) At c/a = √2 the lattice is FCC, so which of the three cubic axes is "c", and hence which layers are A and which are B, is itself a free choice; nothing in App L fixes it. | none. The phrase occurs nowhere else in the corpus. |
| C2, Letter 127 oct-void z-orientation | `tex/BCT_Letter127_EWQCDScales.tex` (+ v2, L128) | yes | posited | not sublattice-dependent | none |

App L itself concludes that the mechanism "does not apply to BCT" (η_stag = 0). The corpus therefore neither uses the assignment nor builds on it.

---

## 6. One-sentence kill (card §3.6)

> *No primary source dated on or before 2026-09-30 assigns to any void, hopfion, winding or other per-site degree of freedom a pattern under which the corner→body-centre operation is a rotation, screw or glide with neither a translation nor an inversion also relating the two sublattices.*

**True.** The single sublattice-staggered assignment in the corpus (App L §4.3) retains an A→B inversion (P4/nnc), and every void, hopfion and winding assignment is sublattice-symmetric or lives in internal space.

---

## 7. Verdict

**SC-ALTER-2 (KILL — absent).** Altermagnetism is a possible *extension* of BCT that would require one new structural input. It is not a BCT result. The honest prior (SC-ALTER-2) is confirmed.

One qualification is reported straight. SC-ALTER-2's wording says every assignment is "translation-invariant under the body-centring vector". App L §4.3 is the one exception to that wording, because it breaks the translation. It keeps an inversion instead, so it fails SC-ALTER-1's requirement ("NOT a translation or inversion") and does not meet SC-ALTER-3's trigger either: it was not introduced to match a target, and it is not altermagnet-allowed. It is logged here so that §6 reopen condition 1 cannot be triggered by rediscovering it.

The gate moves no prediction and un-kills nothing (card scorecard status).

---

## 8. Cost statement (card §3.7, SC-ALTER-2 branch)

**The one structural input that would have to be added** is an anisotropic, non-magnetic decoration of the voids whose pattern around a body-centre sphere is the corner pattern rotated by 90° about c. The minimal example is the rutile analogue: an in-plane director (or an occupied-edge asymmetry) on the octahedral voids of the A layers along [110], and along [1̄10] on the B layers. That input must be stated with a reason internal to BCT, and it must also fix *which* cubic axis is c.

**Symmetry broken.** O_h → D₄h at the level of the decorated structure. The body-centring translation is demoted to the 4₂ screw {C₄z | ½,½,½}, giving P4₂/mnm-type symmetry for the decorated lattice. Test A4 shows this is exactly the mechanism in rutile.

**Interaction with Gate WHY√2 (√2 selected, not forced).** At c/a = √2 the sphere lattice is cubic, and all three axes are equivalent. A D₄h decoration must therefore either choose an axis, which is a new free discrete parameter and the SC-ALTER-3 failure class, or be accompanied by a mechanism that selects one. If √2 is itself only selected, an axis-selecting decoration adds a second selection on top of it rather than reducing to it.

**Interaction with Letter 18, Requirement 1** (Lorentz invariance as isotropic phonon propagation; Volume 2 §"Letter 18 — The BCT Uniqueness Theorem"). Under O_h, every rank-2 response tensor (sound-speed or stiffness at O(k²)) is isotropic, and anisotropy first appears at O(k⁴). Under D₄h, rank-2 tensors have two independent components (xx = yy ≠ zz). A decoration that couples to the phonon sector at quadratic order would therefore reintroduce **O(k²)** anisotropy, directly against Requirement 1. Avoiding this would take either a decoupling argument or tuning. This is Neumann's principle, a general symmetry statement; no spectrum was computed.

---

## 9. Out-of-scope observations (recorded, not scored)

1. **The A/B partition is not a nearest-neighbour bipartition at c/a = √2.** Each corner site has 12 equal nearest neighbours: 8 on B and 4 on A (in-plane, distance a). App K §1.1 and App L §4.3 describe "exactly 8 nearest-neighbour B sites" and a "bipartite" lattice. The corpus's own `tex/BCT_Appendix_K_GreenFunction.tex`:98 carries an audit note that the 4 in-plane A–A bonds are omitted. The particle-hole and η_stag arguments that rest on bipartiteness may need re-examination; this gate does not score them.
2. **App IX5 (Phase 74C) consistency.** It derives four degenerate crystal orientations from "the broken 90° rotational symmetry" of a D₄h crystal. C₄ is an element of D₄h, so the degeneracy as stated is not explained by D₄h. Recorded only.
3. Reader-reported internal inconsistencies about which void hosts SU(3) (App G vs App X vs Vol2:6450) are outside this gate.

---

## 10. 🦜 Baby-speak

Imagine a big box of marbles stacked perfectly. Half the marbles sit on the corners and half sit in the middles, but if you slide the whole pile over by one hop, corners and middles swap places and nothing looks different. That's why plain marbles can never do the special magnet trick called altermagnetism. To do the trick, the little gaps between marbles would need tiny arrows that point one way around the corners and turned-a-quarter-way around the middles. We looked through every page of the BCT books for arrows like that. We found none. We found one page that paints corner marbles "right-handed" and middle marbles "left-handed", but a mirror-flip through the point halfway between them still swaps them perfectly, so that doesn't count either. So: no hidden arrows, the trick isn't in BCT yet, and adding it would mean choosing a new ingredient on purpose.

---

**Files:** `audit/gates/ALTER/gate_ALTER_RESULT.md` (this file) and `audit/gates/ALTER/alter_gate_check.py`. To re-run from the repo root:

```
python3 audit/gates/ALTER/alter_gate_check.py --repo . --rev 0d9600a
```

Parts A and C take seconds. Part B needs `pdftotext` and git history.
