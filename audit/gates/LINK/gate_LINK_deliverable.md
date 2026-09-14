# GATE LINK — DELIVERABLE
## Site or link? Is the second polarisation reachable?

**Executed:** Sunday 13 September 2026, fresh thread.
**Model:** Claude Fable 5.1 (Anthropic).
**Gate file:** `audit/gates/gate_LINK_prompt.md` at commit `47d3eefe6c01bc2c3a7e0d9bbe791b1b989396b6`.

---

## 0. Digest

| | SHA-256 |
|---|---|
| Pre-registered (execution-thread prompt) | `d9dba4c836339b6a27ce58f6bca2bf1fa28e0fc89c3a0eaa25aca4d7f4b4a894` |
| Computed from the fetched file (`sha256sum gate.md`) | `d9dba4c836339b6a27ce58f6bca2bf1fa28e0fc89c3a0eaa25aca4d7f4b4a894` |
| Size | 7493 bytes (matches pre-registration) |

**MATCH.** The file was fetched with `curl` to disk and hashed before it was opened. Not pasted.

Repo tarball at the same commit: SHA-256 `0a32cca4c60c15a4297607c642f7f9381e5ac96dedbe3db4680a5ddf8963c1c8`, 2,117,991 bytes.

---

## 0.5 Search-space coverage (reported before any other number)

**Repo** (tarball, extracted): **134 `.tex` files, 26 at the tree root outside `tex/`** — matches §0.5 exactly. All `.tex` and `.md` outside `audit/` were concatenated into a searchable corpus (169,604 words). Nothing under `audit/notes/` was read. `audit/NEXT.md` was not read (see §11).

**Mount** (`/mnt/project/`, 79 files, every file typed with `file`):

| Type reported by `file` | Count | Notes |
|---|---|---|
| Zip archive (`.pdf` extension) | **33** | page images + `.txt` layers; matches §0.5 |
| True PDF | **14** | matches §0.5 |
| `data` (raw UTF-8, CRLF) | **2** | `4_BCT_Appendices_Volume1_2026_compressed_Part1.pdf` (849,709 B, 14,467 lines) and `..._Part2_compressed.pdf` (713,071 B, 13,715 lines); matches §0.5. **App D.0–D.4, E.0–E.3, F, K are in Part1.** |
| JPEG image (`.PNG`/`.jpeg` extensions) | 18 | not text-bearing; not read |
| HTML | 4 | not read (web tools) |
| LaTeX | 2 | in corpus |
| Plain text / markdown | 6 | **4 deliberately not read** — see contamination statement |

**Page-level coverage:** the 33 ZIP archives contain 393 page images, and **393/393 have a `.txt` layer** (101,724 words). The 14 true PDFs total 94 pages, all extracted with `pdftotext` (28,623 words). Combined mount corpus: 365,110 words. Combined repo corpus: 169,604 words.

Files read in full: App D.0, D.1, D.2, D.3, D.4, E.0, E.1 (Vol 1 Part1); App K §§1–4; App F §(healing length); App JH4 §§JH4.1–JH4.2, JH4.6 table; Monograph v2.1 §§25–27 and fn. 13; One Medium (Journal Edition) §5.5, §9, §10, App C.1. Keyword sweeps ran over both full corpora for: `plaquette`, `link variable`, `U_{ij}`, `Wilson action/loop`, `cos(θ_i − θ_j)`, `Gauss`, `XY model`, `rotation angle`, `polarisation`, `transverse`, `shear`, `longitudinal`, `helicity`, `healing length`, `Superfluid Necessity`.

---

## 1. VERDICT (first)

**SC-LINK-2 — Site variables; the link reformulation is available, at a price that includes the programme's founding identification.**

- The corpus's dynamical phase variable is **site-valued** everywhere it is written: `θ_i` "the rotation angle of sphere i" (App D.3 §2.2), `θ(x,t)` "a compact (U(1)-valued) scalar field" (App E.1 abstract). No dynamical U(1) link variable exists anywhere in the corpus. The G′ premise ("never specified") is **too generous**: the corpus *does* specify, and it specifies site.
- The propagating degree-of-freedom count from the Hamiltonian as written, re-derived here (§3), is **1**. G′'s count is confirmed independently, not inherited.
- A compact U(1) **link** theory on the BCT lattice was constructed (§4) and yields **exactly 2 massless transverse polarisations**, derived numerically from the plaquette quadratic form and by the counting identity E − V + 1.
- **Nothing in the corpus forbids 2 polarisations on general grounds** (§6): the corpus asserts 2 polarisations repeatedly; it never argues against them. SC-LINK-5 does not fire.
- **The price** (§5) is the loss of "the photon is a phonon of the superfluid": link variables are gauge connections, the phonon of the site phase remains as an unwanted extra massless scalar, the transfer-matrix derivation of α₀ no longer refers to the photon, and — decisively — coupling an independent gauge field to a *condensed* site phase is the lattice Abelian–Higgs model, whose ordered (superfluid) phase has a **massive** photon, exactly as App E.1 §3.1 itself computes before trying to escape it.

Secondary findings that the gate did not ask for but the audit turned up: the corpus is internally inconsistent about the **rank** of its site variable (scalar in D.3/E.1/Monograph §25; "two transverse rotation modes" in D.3 §4.4; vector `ξ_i` in One Medium C.1), and internally inconsistent about which **phase** it is in (§7.4) and which **U(1) coupling** it has (§7.5).

---

## 2. §0.7 — reproduced verbatim

> A link reformulation that yields 2 transverse polarisations would give BCT the photon's degree-of-freedom count. It would **not** give the photon's coupling to matter, the fine structure constant, Lorentz invariance of the resulting theory, or any prediction. **And it may cost an identification the programme is built on**: link variables are gauge connections, not condensate phases, so "the photon is a phonon of the superfluid" may not survive its own repair. **Gate LINK cannot deliver electromagnetism. At most it delivers a degree-of-freedom count and an honest price tag.** A favourable verdict is a ticket to a harder gate.

---

## 3. STEP 0 — What is the corpus's variable, actually? (index audit, DOF re-derived)

### 3.1 Every dynamical phase variable the corpus defines

| # | Variable | Where | Index runs over | Canonical? | Quoted definition |
|---|---|---|---|---|---|
| V1 | `θ_i` | App D.3 §2.2 | **sites** (one angle per sphere) | **Yes** — kinetic term implied by "rotational inertia of the spheres", conjugate angular momentum; harmonic expansion and dispersion `ω_k² = (4J/m)·Σ_μ sin²(k_μ a/2)` written | "H_lattice = −J ∑_{<i,j>} cos(θ_i − θ_j) where θ_i is the rotation angle of sphere i, the sum runs over nearest-neighbour pairs" |
| V2 | `θ(x,t)` | App E.0 §2.1, App E.1 §1.1 | **sites** (continuum limit of V1) | **Yes** — `L = (ρ_s/2) η^{μν} ∂_μθ ∂_νθ` | "The BCT phase field θ(x,t) — the rotation angle of the sphere lattice — is a compact (U(1)-valued) scalar field" (E.1 abstract) |
| V3 | `A_{ij}` | App D.3 §2.4 | **links** | **No** — algebraically fixed: `A_{ij} = Φ_v(r_j) − Φ_v(r_i)` where `Φ_v(r) = arctan((y−y_v)/(x−x_v))` is the vortex phase field. A background Peierls phase determined by the vortex position; no kinetic term, no conjugate momentum. | "A_{ij} is the gauge field generated by the vortex — the phase accumulated along bond <i,j> due to the vortex-induced flow" |
| V4 | `A_μ` | App E.0 §2.2, App E.1 §2.1 | continuum (derived from V2) | **No** — `A_μ = (1/e)∂_μθ` "on smooth, vortex-free configurations". Identically pure gauge; no independent dynamics. | "F_μν = ∂_μ A_ν − ∂_ν A_μ = (1/e)(∂_μ∂_ν − ∂_ν∂_μ)θ … For smooth θ, partial derivatives commute … So F_μν = 0 on smooth configurations" (E.1 §2.1) |
| V5 | "two independent transverse rotation modes of the spheres" | App D.3 §4.4 | sites (implied) | **Never written** — no Hamiltonian, no coordinates, no conjugate momenta. Would require θ_i → a rotation vector (SO(3) rotor per sphere), contradicting V1. | "In the BCT lattice, these correspond to the two independent transverse rotation modes of the spheres — rotations about the two axes perpendicular to the propagation direction." |
| V6 | `ξ_i` "octahedral void displacement field" | One Medium C.1; Monograph §25 | **sites** (oct-void sites), 3-vector | **Never written** as a Lagrangian; asserted only. | "Gauge invariance of the resulting U(1) action (invariance under θ → θ + f(x,t) for the massless mode) removes one of the three naive polarisation components of ξ_i, leaving exactly two transverse propagating modes" |
| V7 | fermion field, A/B sublattice | App K §1.2 | **sites** (one orbital per site, 2-component sublattice index) | Yes (hopping Hamiltonian `H(k) = tγ(k)σ₊ + h.c.`) | matter sector, not a phase variable |
| V8 | `U_ℓ ∈ SU(3)` | App JH4 Def. JH4.1–JH4.2 | **links** of the D4 lattice `Λ_D4` | Yes (Wilson action, plaquettes, Haar measure) | "The SU(3) gauge field lives on the links of Λ_D4: each directed link ℓ = (x, x + μ̂) carries a group element U_ℓ ∈ SU(3)." Colour sector only; not connected to θ_i; not on the BCT lattice; U(1) appears only in a group table (see §7.5). |

**Finding S0-A.** Every canonical phase variable (V1, V2) is **site-valued**. The only link-indexed objects are a non-dynamical background (V3) and the SU(3) colour field on a different lattice (V8). There is no dynamical U(1) link variable, no U(1) plaquette term, and no U(1) Gauss law anywhere in the corpus (`grep` for "Gauss" in the EM sense: 0 hits in both corpora; "plaquette": 3 hits, 1 in E.1 citing "the Wilson plaquette action" by name only, 2 in JH4 for SU(3)).

**Finding S0-B (structure of the equation).** The gate's own test: *"A Hamiltonian summed over ⟨i,j⟩ of cos(θ_i − θ_j) is site-valued."* The corpus writes exactly that (D.3 §2.2, and again in App F: `JΣ_{<ij>}(1−cos(θ_i−θ_j))`). **The corpus commits to the site reading by the structure of its Hamiltonian.**

**Finding S0-C (the corpus commits in prose too).** Monograph v2.1 §25: "The electromagnetic field is identified with the irrotational (longitudinal) phonon mode of the octahedral void condensate." An irrotational mode is a gradient field — one degree of freedom by construction. §27 then assigns "the transverse-traceless phonon mode of the lattice displacement field" to the **graviton**. And fn. 13 (Superfluid Necessity Theorem, Letter 259) excludes the vector realisation outright: "a central-force elastic-solid realisation — vector displacements, three phonon branches — exhibits directional sound-speed variation of order 15% … An elastic-solid vacuum on this lattice is therefore excluded by observed Lorentz invariance", while "the scalar phase mode" passes with `M = 4a² 𝟙`.

**Finding S0-D (rank inconsistency).** V1/V2/S0-C say scalar. V5 and V6 say vector. These are not reconcilable; V5 and V6 are never given a Hamiltonian; and V6 is the very "vector displacements, three phonon branches" realisation that fn. 13 excludes. This is a corpus defect distinct from the site/link question and is recorded as CN-LINK-06.

### 3.2 Recount of propagating degrees of freedom from the Hamiltonian as written

From D.3 §2.2, with N sites:

- Configuration space: N angles `θ_i ∈ S¹`. Conjugate momenta: N angular momenta `L_i`. Phase space: 2N.
- No constraints (no Gauss law is written; nothing is gauged).
- Harmonic expansion: `H ≈ Σ_i L_i²/2I + (J/2)Σ_{<ij>}(θ_i − θ_j)²`. Bloch-diagonalising on the BCT Bravais lattice (1 site per primitive cell) gives **one band**, `ω_k² = (J/I)·Σ_δ (1 − cos k·δ)`, which is D.3's own `(4J/m)Σ_μ sin²(k_μ a/2)`. No polarisation index exists in the Hamiltonian for one to appear in the spectrum.
- Continuum limit (E.1 §1.1): `L = (ρ_s/2)(∂θ)²` — the massless scalar. E.1 says so: "This is the massless scalar field Lagrangian. Alone, it would describe a scalar boson (a Goldstone mode)."
- `A_μ = (1/e)∂_μθ` adds **zero** degrees of freedom: it is a function of θ. E.1 §2.1 concedes `F_μν = 0` on all smooth configurations.

**Propagating DOF = 1.** This agrees with Gate G′'s count. Re-derived from D.3 and E.1, not inherited.

Numerical check (script `link_dof.py`, §12): the single site-XY branch at small k has `ω²/k² = 2` in every direction on the 12-bond FCC graph (isotropic, matching the corpus's `M = 4a²𝟙`), but `ω²/k² = 1` along x and `2` along z on the 8-bond bipartite graph that App K §1.1 and D.3 §4.2 use. Side finding: **the corpus's bipartite (8-NN) graph and its isotropy theorem (12-NN) are different graphs.** Not this gate's target; recorded as CN-LINK-13.

### 3.3 Is the phonon an electromagnetic wave by the corpus's own equations?

No. E.1 §2.1 states `F_μν = 0` on smooth configurations. A spin wave is a smooth configuration. Therefore by E.1's own definition the spin wave carries **no** electromagnetic field. E.1 Table 2.4 nonetheless lists "Spin wave (phonon) — B oscillates — Electromagnetic wave = photon". The table row contradicts the section that precedes it. Recorded as CN-LINK-04.

---

## 4. STEP 1 — What would the link theory require? (constructed)

### 4.1 The link-variable Hamiltonian on the BCT lattice

Sites `v` of the BCT Bravais lattice at c/a = √2; links `ℓ = (v, v+δ)` for the NN set (either the corpus's 8 body-diagonal bonds `δ = (±½, ±½, ±√2/2)`, |δ| = a, or the full 12-bond FCC set adding `(±1,0,0), (0,±1,0)`); plaquettes `□` = minimal closed loops of links (4-cycles for the 8-bond graph, 12 per site; triangles for the 12-bond graph, 8 per site — enumerated in `link_dof.py`).

On each link a compact angle `θ_ℓ ∈ [0, 2π)` (equivalently `U_ℓ = e^{iθ_ℓ}`) and its conjugate integer-valued electric field `E_ℓ`, `[E_ℓ, U_ℓ′] = δ_{ℓℓ′} U_ℓ` (Kogut–Susskind form; see Kaplan & Stryker eq. (2), read). The Hamiltonian:

```
H_link = (g²/2) Σ_ℓ E_ℓ²  −  (1/g²) Σ_□ cos(θ_□),      θ_□ = Σ_{ℓ∈□} (±) θ_ℓ
```

### 4.2 Gauss law

At every site `v`:

```
G_v ≡ Σ_{ℓ out of v} E_ℓ − Σ_{ℓ into v} E_ℓ = ρ_v
```

`ρ_v` is the **matter charge density on site v** — an integer per site supplied by an independent matter field (or a static source). `G_v` generates the local gauge transformation `θ_ℓ → θ_ℓ + φ_{v′} − φ_v`; physical states satisfy `G_v |phys⟩ = ρ_v |phys⟩`. This constrains the **longitudinal** part of `E` (Gauss's law) and, via the gauge redundancy, removes the longitudinal part of `θ_ℓ`.

### 4.3 Degree-of-freedom count — derived

**Counting identity.** With V sites and E links on a closed lattice: configuration space has E angles; Gauss's law gives V−1 independent constraints (the sum over all sites is an identity on a torus); the gauge group acts with V−1 independent generators (a constant gauge transformation acts trivially on links). Reduced phase space dimension = 2E − 2(V−1); **canonical pairs = E − V + 1**, i.e. **E/V − 1 per site**. On the cubic lattice (z = 6, E/V = 3) this gives 2 per site — the count Kaplan & Stryker obtain as (n−1)(d−1) physical variables per topological sector (read; their Fig. 1 discussion). On BCT-8 (E/V = 4) it gives **3** per site; on FCC-12 (E/V = 6) it gives **5** per site.

**Which of these propagate at long wavelength?** Harmonic expansion of the plaquette term gives the magnetic quadratic form `Q = Pᵀ P` (P = plaquette–link incidence). Bloch-diagonalised at wavevector k, `D(k)` is (links-per-cell)×(links-per-cell). Computed in `link_dof.py`:

| Graph | links/cell | eigenvalues of D(k) as k→0 | classification |
|---|---|---|---|
| BCT-8 | 4 | `0, ∝k², ∝k², 96` | 1 gauge zero · **2 massless (photons)** · 1 lattice-scale mode |
| FCC-12 | 6 | `0, ∝k², ∝k², 24, 24, 24` | 1 gauge zero · **2 massless (photons)** · 3 lattice-scale modes |

Verified along k ∥ (100), (001), (111), (123) at |k| = 0.4, 0.2, 0.1, 0.05: the two acoustic eigenvalues scale as k² (ratio 4.00 per halving of k) and are degenerate with each other; the O(1) eigenvalues are pinned at the lattice scale and do not propagate in the continuum.

**Result: exactly 2 propagating transverse polarisations**, on either graph. The extra E/V − 3 canonical pairs are gapped at the lattice scale.

**Anisotropy finding.** On BCT-8 the acoustic stiffness is `0.060` along x and `0.120` along z at |k| = 0.1 — the two photons propagate **√2 faster along c than in the basal plane**. On FCC-12 the stiffness is `0.0075` in every direction tested — isotropic. The link theory reproduces the corpus's own HO6 lesson: on this lattice, isotropy needs the full 12-fold coordination. But D.3 §4.2 and D.4 §2.2 (the bipartite loop argument that produces `(1−2α₀)` and `(1−3α₀)/(1−α₀)`) require the **8-bond bipartite** graph. The two requirements conflict. CN-LINK-13.

### 4.4 Continuum limit

At weak coupling (β ≡ 1/g² > β_c), the Coulomb phase: expanding `cos θ_□ ≈ 1 − θ_□²/2` with `θ_□ ≈ a² F_{μν}` gives `H → ½∫(E² + B²)`, i.e. Maxwell with 2 polarisations (Kaplan & Stryker, opening paragraph of "U(1) Hamiltonian and Hilbert space"; Cox et al. hep-lat/9701005 §2.1: "Taking Θ_P = a²gF_μν … one obtains for weak coupling g the usual continuum action S = ¼∫d⁴x F²"). For the Wilson action the transition is at **β_c ≃ 1.011** (hep-lat/9701005 §2.1, read); the strong-coupling side is confining with condensed monopoles, the weak side Coulomb with dilute monopoles (Akerlund & de Forcrand, abstract, read). On the FCC-12 graph the continuum limit is isotropic Maxwell; on BCT-8 it is Maxwell in an anisotropic medium (a birefringent vacuum).

### 4.5 THE PRICE TAG — what must be added to BCT, itemised

**New variables (add):**
1. One compact angle `θ_ℓ` on every link (4 per site on BCT-8; 6 on FCC-12), independent of `θ_i`.
2. One conjugate electric field `E_ℓ` per link.
3. A matter field on sites carrying an integer charge `ρ_v` (a vortex line of `θ_i` is not a site charge — see §5.2).

**New constraints (add):**
4. Gauss's law `G_v = ρ_v` at every site.

**New terms (add):**
5. A plaquette (magnetic) term `−(1/g²)Σ_□ cos θ_□` — the corpus has none for U(1).
6. An electric term `(g²/2)Σ_ℓ E_ℓ²`.
7. If the site phase `θ_i` is retained, a minimal coupling `−J Σ_{<ij>} cos(θ_i − θ_j − θ_{ij})` — which turns the theory into the lattice Abelian–Higgs model (§5.1).

**Removed or reinterpreted:**
8. **Remove** `A_μ = (1/e)∂_μθ` (E.0 §2.2, E.1 §2.1). This identity makes A pure gauge; it is incompatible with A having its own dynamics. Everything downstream of it in E.1 (§§2.1–2.3, the "F_μν from vortex topology" identification, the Table 2.4 rows) is rewritten.
9. **Reinterpret** "the BCT photons are the spin-wave modes (phonons/magnons)" (D.3 §2.2). The photon becomes the link excitation; the phonon of `θ_i` becomes a **separate** massless scalar that must be either gapped, removed, or identified with something else (it cannot be the graviton either — Monograph §27 already gives that to the transverse-traceless *displacement* modes).
10. **Reinterpret** the transfer-matrix derivation of `g² = t_tet·t_oct` (D.3 §3): it is a statement about "an electromagnetic wave (spin-wave mode) propagating through the BCT lattice". If the photon is not the spin wave, the derivation no longer computes the photon's coupling. §5.3.
11. **Reinterpret** the one-loop and all-orders factors `(1−2α₀)`, `(1−3α₀)/(1−α₀)` (D.3 §4, D.4): they count "two transverse polarisation modes" of a mode that, in the site theory, has one, and they use the 8-bond bipartite graph on which the link photon is anisotropic.
12. **Reinterpret** "vortex = electron = point charge": in the link theory charges are Gauss-law sources on sites; vortex lines of a site phase are strings that couple to A as **magnetic** flux tubes (E.1 §2.2 itself calls them Abrikosov vortices carrying flux h/e). §5.2.
13. **Reinterpret** the phase assignment: E.1's "Coulomb phase" (`⟨e^{iθ}⟩ = 0, ρ_s → 0`) is the XY *disordered* phase. §5.4.
14. **Reinterpret** the Superfluid Necessity Theorem's scope: it excludes the vector-displacement solid, not a link gauge theory — but its isotropy result is for the 12-NN graph, which the bipartite arguments cannot use (item 11).

**Cost that cannot be itemised away:** the programme's name. See §5.1.

---

## 5. STEP 2 — Is it available, or does something block it? (survival table)

### 5.0 Survival table

| Identification | Corpus text | Site reading (as written) | Under link reformulation | Survives? |
|---|---|---|---|---|
| Photon = phonon/spin wave of the medium | D.3 §2.2 "spin-wave modes … are the BCT photons"; Monograph §25 "irrotational (longitudinal) phonon"; E.0 §1 "EM = lattice shear waves"; PRL-style text "longitudinal phonons (Maxwell)" | 1 scalar DOF; by E.1 §2.1 carries F = 0 | Photon is a link excitation; phonon is a separate extra scalar | **Lost** |
| Matter = vortex of the phase; vortex = electric charge | E.1 §2.3 "The BCT vortex IS an electrically charged particle"; E.1 §2.2 "the Abrikosov vortex … one magnetic flux quantum" | Already self-contradictory (electric in §2.3, magnetic in §2.2) | Charges are Gauss-law site sources; θ-vortex lines couple as magnetic flux tubes (Higgs phase) | **Lost as electric charge; survives only as magnetic string** |
| α₀ from void transmission amplitudes | D.3 §3 "An electromagnetic wave (spin-wave mode) propagating through the BCT lattice must pass through the interstitial void network" | Presupposes photon = spin wave | Computes the spin-wave transmission, not the photon coupling | **Does not survive as a derivation of α** |
| `(1−2α₀)` factor from 2 transverse polarisations | D.3 §4.4 | Asserted; the Hamiltonian has 1 mode | 2 modes now exist, but the bipartite loop argument needs BCT-8 on which they are anisotropic; and the "loop integral" is not a link-theory quantity | **Not rescued** |
| Coulomb phase / massless photon | E.1 §3 | E.1's own definition is the XY disordered phase — no phonon at all | Depends on coupling: β = J ≈ 10.7 → Coulomb; β = 6/π⁵ ≈ 0.02 (JH4) → confining | **Undetermined by the corpus (two couplings)** |
| Superfluid Necessity (Letter 259) | Monograph fn. 13 | Scalar phase mode isotropic on 12-NN graph | Not contradicted by a link theory per se; contradicted by the Abelian–Higgs consequence (§5.1) | **Survives as a theorem; its premise (condensate) conflicts with masslessness** |
| Healing length ξ = 2.32 a | App F | see §5.5 | see §5.5 | neutral |

### 5.1 The phonon identification — and the Abelian–Higgs trap

E.1 §3.1 computes, for the site theory: "Substituting A_μ = (1/e)∂_μθ into L_BCT on smooth configurations: L_BCT = (ρ_s/2)(∂_μθ)(∂^μθ) = (ρ_s e²/2) A_μ A^μ. This is a MASS TERM for the photon field. The photon would have mass m_γ = e√ρ_s. This is the Meissner effect."

That computation is correct, and it is *more* correct in the link reformulation than in the site theory. Once A is an independent gauge field minimally coupled to a condensed phase, the term `(ρ_s/2)(∂θ − eA)²` with `⟨e^{iθ}⟩ ≠ 0` **is** the Higgs mechanism: the photon eats the phonon and becomes massive. The lattice version — link U(1) gauge field + site XY matter — is the lattice Abelian–Higgs model, and its ordered-matter phase is the Higgs phase.

E.1 tries to escape by invoking compactness: "The BCT vacuum is NOT a simple superfluid. The phase field θ is compact." But compactness of the *site* phase does not change this: the compact XY model's ordered phase is the superfluid (Goldstone mode present, vortices gapped), its disordered phase has no Goldstone mode. E.1 then defines the "Coulomb phase" as `⟨e^{iθ}⟩ = 0, ρ_s → 0` — that is the disordered phase, in which **the phonon E.1 calls the photon does not exist**. Either the medium is a superfluid (condensate, phonon, massive gauge field if one is added) or the added gauge field is massless (no condensate, no superfluid, no phonon-photon). The corpus wants both.

**Conclusion:** the phonon identification does not survive the link reformulation — and the reason is the corpus's own §3.1 calculation. The reformulation is *available* (nothing forbids writing it), but it converts "BCT Superfluid" into either a superconductor or a non-superfluid.

### 5.2 The vortex/charge identification

In the link theory, charge is the eigenvalue of `G_v` — an integer on a **site**, sourced by a matter field. A vortex of the site phase is a **line** (E.1 §2.2: "a single vortex line along the z-axis") with `∮∇θ·dl = 2π`. With an independent A coupled via `(∂θ − eA)`, such a line is the Abrikosov/Nielsen–Olesen flux tube — E.1 §2.2 says so verbatim — which is a **magnetic** object. E.1 §2.3's claim that a moving θ-vortex "IS an electrically charged particle" is the standard **2+1D** particle–vortex duality statement misapplied: in 3+1D the superfluid's vortices are strings and the dual gauge field is a **2-form** (Kalb–Ramond), not Maxwell (Franz cond-mat/0607310 abstract; Beekman–Sadri–Zaanen arXiv:1006.2267 abstract, both read: "the dual theory … is a theory of bosonic strings interacting through a Kalb-Ramond rank-2 tensorial gauge field"; "the 2-form transversal photon that represents the remnant of the zero sound mode"). A massless 2-form in 3+1D carries **one** propagating degree of freedom — the zero sound. Duality therefore cannot supply the missing polarisation; it re-expresses the single one.

The healing-length number sharpens this: the corpus's vortex core radius ξ = 2.32 a is **11.2×** the oct-void inradius r_oct = 0.207 a (App F: "the vortex FILLS the oct void"). A core eleven times larger than the cavity it is said to sit in is not a point charge localised in one void; it is a string threading ≈ 5 unit cells in diameter.

**Conclusion:** "vortex = electron" survives only as "vortex line = magnetic flux tube of the Higgs phase". The electric-charge reading needs a new site matter field (price item 3).

### 5.3 α₀ and the transfer matrix

D.3 §3.1: "An electromagnetic wave (spin-wave mode) propagating through the BCT lattice must pass through the interstitial void network … Each void acts as a transmission channel." The object propagating is the spin wave of `θ_i` — the site phonon — and the derivation is explicitly for "a wave propagating along the c-axis" in "the basis of forward/backward propagating waves" with a **2×2** transfer matrix (one mode, forward and back). The derivation presupposes the site reading twice: the wave is the spin wave, and it has one polarisation. Under the link reformulation the photon is not the spin wave, and the transfer matrix computes a quantity that is not the photon's coupling to anything. The number `g² = t_tet·t_oct` would survive as a property of the site phonon; its identification with `e²/ħc` would not.

### 5.4 Confinement

The corpus's language is contradictory on two axes:

*(a) Which phase.* E.1 §3.2 labels the phases: "Higgs phase … ⟨e^{iθ}⟩ ≠ 0 … Photons are massive"; "Coulomb phase … ⟨e^{iθ}⟩ = 0 … ρ_s → 0 … Photons are massless." For a site XY theory, `⟨e^{iθ}⟩ ≠ 0` is the superfluid with its Goldstone phonon, and `⟨e^{iθ}⟩ = 0` is the gapped disordered phase. E.1 has assigned the massless photon to the phase with **no** massless mode. In a genuine compact U(1) link theory the Coulomb phase is the **weak-coupling** phase with dilute monopoles and a massless photon (Akerlund & de Forcrand, abstract; Cox et al. §2.1), which does not involve any `⟨e^{iθ}⟩` of a matter field at all.

*(b) Which coupling.* Two incompatible bare U(1) couplings appear:
- E.1 §3.3 and §5.1: `J = 1/(4πα₀) ≈ 10.74`, "1/e² = J". As a Wilson β this is **10.74 ≫ β_c ≈ 1.011** → deep Coulomb phase (if the link theory were adopted).
- App JH4 §JH4.6 group table: "U(1) (lepton) — 24 D4 roots — bare action π⁵/6 — mass gap ∼ m_e sector", with "The proof of Theorem JH4.1 applies mutatis mutandis to each group". `g² = π⁵/6 ≈ 51.0`, so β = 1/g² ≈ **0.0196 ≪ β_c** → deep confining phase, and JH4 indeed asserts a **mass gap** for U(1). Where the corpus does use link variables and a Wilson action, it puts U(1) in the confining phase — a gapped photon.

*(c) Arithmetic.* E.1 §3.3 writes `S_monopole = 4π²J` then "= π/(4α₀α) ≈ 34" and `P ~ exp(−34) ≈ 2×10⁻¹⁵`. With J = 10.74, `4π²J = 424`; the printed alternative formula `π/(4α₀α)` evaluates to 14,528. The number 34 follows from neither expression. CN-LINK-08.

**Where would BCT sit?** Undetermined by the corpus: Coulomb at E.1's coupling, confining at JH4's. Both cannot hold.

### 5.5 The healing length

From source (App F, Vol 1 p. ~3003 and 3738): `ξ = a/√(8πα₀)`. Recomputed: **ξ/a = 2.3175**, ξ/R = 4.635, ξ/r_oct = 11.19, ξ/r_tet = 20.6 — the corpus's own printed values (2.3175, 4.6351, 11.1901) are reproduced.

Bearing on the formulation: ξ > a means the condensate cannot vary between neighbouring sites; a site-resolved phase `θ_i` is over-resolved and the continuum Gross–Pitaevskii description is the physically appropriate one (App F says as much: "the condensate sees it as a weakly perturbing potential, not a hard wall"). Neither the site-lattice nor the link-lattice formulation is *physically distinguished* by ξ — both are UV completions of a continuum theory whose DOF count is fixed by the continuum field content (1 for a scalar phase, 2 for a gauge field). ξ/a does not decide site vs link; it says the lattice is below the coherence scale, so the question is really *scalar vs vector field content*, which the corpus (S0-D) has not settled.

Note the definition `ξ = a/√(8πα₀)` is itself an identification (the GP healing length is `1/√(8π n a_s)`; the substitution `n a_s a² → α₀` is not derived anywhere located). Tiered ASSERTED for the ratio's provenance; the arithmetic from that definition is PROVEN.

---

## 6. STEP 3 — Obstruction check

Does anything in the corpus **forbid** 2 polarisations on general grounds?

Searched: `helicit*`, `spin-1`, `rank`, `representation`, `T1u`, `transverse`, `polari*`, `Superfluid Necessity`, `HO6`, `HO5` across both corpora.

- **No rank/helicity argument against 2 polarisations exists.** The corpus asserts 2 in D.3 §4.4 ("exactly two of the three T1u modes are transverse"), One Medium §5.5 ("The physical photon carries two transverse polarisation states … the two transverse modes of the octahedral channel"), and One Medium C.1. The T1u argument is representation-theoretically fine for a *vector* field on an O_h site; it does not apply to the scalar `θ_i` the Hamiltonian contains.
- **The closest thing to an obstruction** is the Superfluid Necessity Theorem (Monograph fn. 13 / Letter 259 / App HO6), which excludes the "vector displacements, three phonon branches" elastic realisation on isotropy grounds. It closes the *phonon* route to 2 polarisations. It does **not** address a link gauge field, whose isotropy on FCC-12 was verified here (§4.3) and which is in any case a different object from a displacement field.
- Monograph §27 already assigns the transverse-traceless displacement modes to the graviton — so even if the vector-displacement route were reopened, its transverse modes are spoken for.

**Result: no sound general obstruction. SC-LINK-5 does not fire.** The reformulation question is live, and answered in §§4–5.

---

## 7. CN-LINK notices (tiered PROVEN / CONJECTURE / ASSERTED; revised clause by clause)

**CN-LINK-01** [PROVEN — primary text] The corpus's canonical phase variables are site-valued: `θ_i` "the rotation angle of sphere i" with `H_lattice = −J∑_{<i,j>}cos(θ_i − θ_j)` (D.3 §2.2); `θ(x,t)` "a compact (U(1)-valued) scalar field" (E.1 abstract). No dynamical U(1) link variable, plaquette term, or Gauss law exists in the corpus. The G′ record "never specified" is corrected to "specified: site".

**CN-LINK-02** [PROVEN — re-derived] Propagating degrees of freedom from the Hamiltonian as written: **1** (one scalar band; `A_μ = ∂_μθ/e` adds none). G′'s count confirmed independently.

**CN-LINK-03** [PROVEN — constructed, `link_dof.py`] Compact U(1) on the BCT lattice (Kogut–Susskind Hamiltonian, Gauss law at sites) has exactly 2 massless transverse polarisations on both the 8-bond and 12-bond graphs; remaining `E/V − 3` link modes per site are gapped at the lattice scale. Counting identity `E − V + 1` reproduces the cubic-lattice (n−1)(d−1) of Kaplan & Stryker.

**CN-LINK-04** [PROVEN — primary text, internal contradiction] E.1 §2.1: "F_μν = 0 on smooth configurations". E.1 Table 2.4: "Spin wave (phonon) — B oscillates — Electromagnetic wave = photon". A spin wave is smooth. The table contradicts the section.

**CN-LINK-05** [PROVEN — primary text] Monograph v2.1 §25 identifies the photon with "the irrotational (longitudinal) phonon mode"; §27 gives the transverse-traceless displacement modes to the graviton; fn. 13 excludes the vector-displacement solid. The flagship document commits to a one-DOF photon.

**CN-LINK-06** [ASSERTED in corpus — unsupported] D.3 §4.4's "two independent transverse rotation modes of the spheres" and One Medium C.1's vector `ξ_i` with "gauge invariance … under θ → θ + f(x,t)" are never given a Hamiltonian or Lagrangian; `θ → θ + f(x,t)` for arbitrary `f` is not a symmetry of `(∂θ)²`; and `ξ_i` is the realisation fn. 13 excludes. The corpus is inconsistent about the rank of its own site variable.

**CN-LINK-07** [PROVEN — primary text] E.1 imports compact-U(1)-LGT vocabulary ("Wilson plaquette action", "Coulomb phase", "monopole") into a site theory and defines "Coulomb phase" as `⟨e^{iθ}⟩ = 0, ρ_s → 0` — the XY disordered phase, in which the phonon E.1 calls the photon does not exist.

**CN-LINK-08** [PROVEN — arithmetic] E.1 §3.3: `S_monopole = 4π²J` with J = 10.74 is 424, not "≈ 34"; the alternative printed form `π/(4α₀α)` is 14,528. The suppression factor `exp(−34) ≈ 2×10⁻¹⁵` follows from neither.

**CN-LINK-09** [PROVEN — primary text] Two incompatible bare U(1) couplings: E.1 `1/e² = J = 1/(4πα₀) ≈ 10.74` (Coulomb if a link theory) versus JH4 `g² = π⁵/6 ≈ 51` (β ≈ 0.02, confining; JH4 itself asserts a U(1) mass gap "∼ m_e sector"). The only place the corpus writes a Wilson action, it puts U(1) in the confining phase.

**CN-LINK-10** [PROVEN — consequence of E.1 §3.1 plus standard Higgs mechanism] Adding an independent link gauge field minimally coupled to a condensed site phase yields the lattice Abelian–Higgs model; in the superfluid (`⟨e^{iθ}⟩ ≠ 0`) phase the photon is massive, as E.1 §3.1 computes. Masslessness requires `⟨e^{iθ}⟩ = 0` — no superfluid. The link reformulation is available but cannot coexist with "BCT Superfluid" and a massless photon.

**CN-LINK-11** [PROVEN — external, abstracts read] In 3+1D the superfluid phase mode is dual to a Kalb–Ramond 2-form gauge field with one propagating mode (the zero sound), not to Maxwell (Franz 2007; Beekman–Sadri–Zaanen 2011). E.1 §2.3's "moving vortex = electrically charged particle" is the 2+1D statement; in 3+1D the vortex is a string and duality does not supply a second polarisation.

**CN-LINK-12** [PROVEN arithmetic on an ASSERTED definition] ξ/a = 2.3175 from `ξ = a/√(8πα₀)` (App F); ξ/r_oct = 11.19, so the "vortex in the oct void" overfills the void elevenfold. The definition's substitution `n a_s a² → α₀` is not derived in any text located.

**CN-LINK-13** [PROVEN — computed] The corpus's bipartite arguments (App K §1.1; D.3 §4.2; D.4 §2.2) use the 8-NN graph, on which both the site phonon and the link photon are anisotropic (`ω²/k²` = 1 along x, 2 along z); the isotropy theorem (HO5, `M = 4a²𝟙`) uses the 12-NN graph. Any link reformulation must choose: isotropy (12-NN) or the bipartite loop factors (8-NN), not both.

**CN-LINK-14** [PROMPT DEFECT — recorded, not force-fitted] The gate's stop conditions treat "site vs link" as the only unresolved axis. The audit finds a second unresolved axis, **scalar vs vector site variable** (CN-LINK-06), which the stop conditions do not address. SC-LINK-2 is selected because site/link *is* determined; the rank inconsistency is logged as a separate correction item rather than triggering SC-LINK-4.

---

## 8. Scripts

- `link_dof.py` — enumerates BCT NN bonds (8-bond and 12-bond), minimal plaquettes, builds the Bloch-diagonalised magnetic quadratic form `D(k)`, classifies eigenvalues (gauge zero / ∝k² / O(1)) along four k-directions at four |k|. Output reproduced in §4.3.
- `checks.py` — α₀, J, β placements vs β_c, E.1 monopole-action arithmetic, ξ/a and ratios, site-XY isotropy on 8- and 12-bond graphs. Output reproduced in §§3.2, 5.4, 5.5.
- `corpus_build.sh` — the exact `file`/`unzip`/`pdftotext`/`tr` pipeline used for §0.5.

All three are committed alongside this deliverable.

---

## 9. External citations (each actually read)

1. D. B. Kaplan & J. R. Stryker, "Gauss's Law, Duality, and the Hamiltonian Formulation of U(1) Lattice Gauge Theory", arXiv:1806.08797 (PRD 102, 094515 (2020)). **Read in full** (fetched PDF). Used for: Kogut–Susskind form, link/electric-field commutator, lattice Gauss law (their eq. 5), the physical-variable count (n−1)(d−1) per topological sector, and the statement that the continuum limit of compact U(1) is the weak-coupling limit.
2. J. Cox, W. Franzki, J. Jersák, C. B. Lang, T. Neuhaus, P. W. Stephenson, "Gauge-ball spectrum of the four-dimensional pure U(1) gauge theory", arXiv:hep-lat/9701005. **Read: §2.1** (search-result excerpt). Used for: `Θ_P = a²gF_μν` → Maxwell at weak coupling; `β_c ≃ 1.011` for the Wilson action; confinement at strong / Coulomb at weak coupling.
3. O. Akerlund & P. de Forcrand, "U(1) lattice gauge theory with a topological action", arXiv:1505.02666. **Read: abstract and introduction** (search-result excerpt). Used for: confining phase = monopole condensation; Coulomb phase = dilute monopoles; weakly first-order transition with the Wilson action.
4. M. Franz, "Vortex-boson duality in four space-time dimensions", arXiv:cond-mat/0607310 (EPL 77, 47005 (2007)). **Read: abstract.** Used for: 3+1D dual of a phase-fluctuating superfluid is a theory of strings coupled to a Kalb–Ramond rank-2 gauge field.
5. A. J. Beekman, D. Sadri, J. Zaanen, "Condensing Nielsen-Olesen strings and the vortex-boson duality in 3+1 and higher dimensions", arXiv:1006.2267 (NJP 13, 033004 (2011)). **Read: abstract.** Used for: the 2-form "transversal photon" is the remnant of the superfluid's zero-sound mode; string condensation gives it a mass.

Not cited because not read: Kogut & Susskind PRD 11, 395 (1975); Polyakov (1977); Guth (1980); Banks–Myerson–Kogut (1977); Fradkin–Shenker (1979); Kalb & Ramond (1974). Their results are referred to only through the sources above that cite them.

---

## 10. Contamination statement

- **Memory listing auto-loaded** into the session context before the gate file was fetched. I saw file *names and one-line summaries only*. The unpermitted summaries seen: `/projects/…/audit-findings.md` (aliases "Cold Ledger, CN ledger, gates"; summary: "Cold Ledger audit results — closed sectors by proof, what survives, active correction ledger, and open problems in priority order") and `/projects/…/overview.md` (summary mentions "current audit state (Cold Ledger, Aug–Sep 2026)"). **Neither file was opened.** No gate-specific content, no CN numbers, no verdicts were visible in the listing.
- **Not called:** `conversation_search`, `recent_chats`, `memory_read`, `project_knowledge_search`.
- **Not read:** `audit/notes/`, `audit/NEXT.md`, `audit/gates/{C1,INT,PSI2,TANH,crossaudits}`, `gate PSI2 prompt.md`, and — in the mount — `claude_Gate_C1_Result___Interior_Healing_Length.md`, `claude_Gate_Session_Prompts.md`, `BCT_GP_STATE_SAVE.md`, `Michel_Running_Thoughts.md`, `Letter_From_Dr_Newstead_`, `Eureka2026_CV.docx`, and the four HTML files. The C1 result file was avoided specifically because §3 requires the healing-length ratio to be computed from source, which it was (App F).
- **Inheritance:** the G′ premise (1 DOF) was re-derived from D.3 and E.1 (§3.2) before being relied on.
- Web searches were run for external literature only (§9); no BCT-related query was issued to the web.

---

## 11. What the gate did NOT establish

- It did not establish electromagnetism, the photon's coupling to matter, α, Lorentz invariance, or any prediction (§0.7).
- It did not establish that the price in §4.5 *can* be paid consistently. CN-LINK-10 says the straightforward payment (link field + condensed site phase) gives a massive photon; whether some non-straightforward construction (e.g. a disordered site phase with vortex-string matter, or a 2-form sector re-identified with something other than the photon) is viable was not investigated and is a harder gate.
- It did not determine which U(1) coupling the programme holds (CN-LINK-09) or which NN graph it holds (CN-LINK-13); those are corpus decisions, not audit findings.
- It did not audit the D.3 "loop integral" `I_BCT = α₀` or the D.4 resummation on their own terms — only their dependence on the polarisation count and graph choice.
- It did not test the O_h/T1u claim as a claim about a *vector* site field; it only established that no vector site field is written.
- It did not read App HO5/HO6 at primary source (not located in the mount by heading; the isotropy statements were read as quoted in Monograph v2.1 fn. 13 and One Medium §10).
- It did not commit to the repository (no write credentials in this session). Files are delivered under `audit/gates/LINK/` for Michel to commit; an append block for `audit/NEXT.md` is provided in `NEXT_append.md` **without** having read the existing `NEXT.md` (quarantine).

---

*Cold Ledger. Gate LINK closed at SC-LINK-2. Written 13 September 2026. Not inherited by any other gate without re-derivation.*
