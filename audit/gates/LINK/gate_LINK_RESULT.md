# GATE LINK — RESULT

**Run:** 14 September 2026. **Prompt:** `audit/gates/gate_LINK_prompt.md`, pinned at commit
`ec0592f9319ab5a61851018539ab2b6ff2eb72b3`.
**Digest (curl to disk, hashed before reading):**
`d9dba4c836339b6a27ce58f6bca2bf1fa28e0fc89c3a0eaa25aca4d7f4b4a894` (7493 bytes).
Independently re-hashed inside the checkout at the same commit: identical.
Repo write is blocked in this container (no credentials); the deliverable is returned as a
`git format-patch` bundle, per standing practice.

---

## 0 — SEARCH-SPACE COVERAGE (reported before any other number)

**Repo.** `git clone` at the pinned commit succeeded (tarball via codeload was not needed).
Commit SHA-1 `ec0592f9319ab5a61851018539ab2b6ff2eb72b3`. **134 `.tex` files, 26 at the tree root
outside `tex/`** — both counts match the prompt exactly. Coverage: full-text term census over all
134 (`plaquette`, `Wilson`, link/site language, `Gauss`, `Coulomb phase`, `helicity`, `phonon`,
`polarisation`, `healing length`, `Polyakov`, `Kalb–Ramond`, particle–vortex duality); full reads
of the hits. Notable null results in the `.tex` corpus: **0 occurrences of `plaquette`, 0 of
`Gauss law`, 0 of `Coulomb phase`, 0 of `two polarisations`, 0 of `cos(θ_i − θ_j)`** — the U(1)
sector's dynamics is not written in the `.tex` tree at all; it lives in the mount.

**Mount.** 95 files, **every one typed with `file`**:
- **33 ZIP archives** of page images with `.txt` layers — **387 pages**, text layer present for
  every page (txt:image is 1:1 in all 33). Full term census over all 387; full reads of
  `BCT_AppendixJH4_YangMills_tex` pp. 1/3/4 and `BCT_OneMedium_JournalEdition_v2` pp. 1–5, 8–9,
  12–13.
- **14 true PDFs** — matches the prompt's count exactly. All 14 converted with `pdftotext`
  (6,996 lines) and censused; `BCT_Letter88_ThreeDimensions` read in full.
- **2 raw UTF-8 files that `file` reports as `data`**, openable by neither PDF nor ZIP tools:
  `4_BCT_Appendices_Volume1_2026_compressed_Part1.pdf` (849,709 B, 14,468 lines) and
  `…_Part2_compressed.pdf` (713,071 B, 13,716 lines). **App D.3 and App E.1 are both in Part1**
  (lines 1211–1516 and 1903–2179 respectively). Both read **in full, at primary source**; both
  files censused end to end.
- Remainder: 5 Python scripts, 5 gate/result `.md` files, 4 HTML, 2 `.tex`, 1 `.docx`-labelled
  text file, images.

Page-level coverage: 28,184 lines of raw text + 387 page layers + 14 PDFs + 134 `.tex`
term-covered; ~600 lines of App D.3/E.1/E.0 and ~9 pages of the One Medium synthesis read
line by line. The two appendices the gate names were located and read at primary source, not
via summary.

---

## 1 — VERDICT

**SC-LINK-2.** The corpus's dynamical phase variable is **site-valued**, and the compact-U(1)
link reformulation **is available** — nothing in the corpus forbids it. The itemised price is in
§4 and it is not small: it costs the identification the programme's public face rests on.

Two qualifications, both reported rather than smoothed:

- **SC-LINK-4 fires at corpus level, not at Hamiltonian level.** The *written dynamics* commits
  to sites without ambiguity. But the corpus as a whole carries **three** incompatible field
  contents for the photon: the site phase θ_i (App D.3, E.1), a **three-component octahedral-void
  displacement field ξ_i** (One Medium App C.1), and genuine **SU(3) link variables** in the QCD
  sector (App JH4). The site-vs-link question is settled for the U(1) phase field; the
  *field-content* question is not settled across the corpus.
- **SC-LINK-5 does not fire.** No general obstruction to 2 polarisations exists in the corpus
  (§5). What exists is a gap, not a theorem.

**Gate G′'s premise is confirmed by re-derivation, not inherited:** the Hamiltonian as written
carries **exactly one** propagating branch. Derivation in §2, script
`link_step0_site_dof.py`.

---

## 2 — STEP 0: WHAT IS THE CORPUS'S VARIABLE, ACTUALLY?

### 2.1 The index audit

Every dynamical phase variable the corpus defines, with its index structure and canonical status:

| symbol | where | index runs over | canonical? |
|---|---|---|---|
| θ_i | App D.3 §2.2; repeated Vol.1 Pt1 L3050 | **sites** ("the rotation angle of sphere i") | **yes** — has a kinetic term via the stated dispersion ω_k² = (4J/m)Σ_μ sin²(k_μa/2), hence a conjugate momentum |
| A_ij | App D.3 §2.4 | **links** ⟨i,j⟩ | **no** — algebraically fixed: A_ij = Φ_v(r_j) − Φ_v(r_i), the Peierls phase of the vortex field. No kinetic term, no conjugate momentum, no plaquette term anywhere |
| A_μ = (1/e)∂_μθ | App E.1 §2.1 | continuum, slaved to θ | **no** — a definition, not a field; carries no independent dof |
| Φ_v | App D.3 §2.4 | continuum background | no — external source |
| ξ_i (3 components) | One Medium App C.1 | void displacement, vector | **no Hamiltonian is written for it anywhere** |
| U_ℓ ∈ SU(3) | App JH4 §JH4.2.1 | **links** of Λ_D4, with a Wilson plaquette action | **yes — but this is the SU(3) sector, not the photon** |

The corpus's own words, App E.0 §2.1 (Vol.1 Pt1 L1742), conceding the problem in advance:
the massless scalar Lagrangian is called <q>a good starting point, but photons are vector fields,
not scalars</q>, with the vector structure to <q>emerge from the topology</q>. That emergence is
the thing Gate G′ found does not happen, and the thing this gate priced.

### 2.2 The propagating-mode recount, from the Hamiltonian as written

H_lattice = −J Σ_⟨i,j⟩ cos(θ_i − θ_j), one compact phase per site, one site per primitive cell
of the BCT lattice at c/a = √2 (12 equal nearest neighbours). The dynamical matrix is therefore
**1 × 1**: one branch, ω²(k) = (2J/m) Σ_δ (1 − cos k·δ). Numerically (script, exact in the
second-moment tensor): the 12 nn vectors give M_ij = Σ_δ δ_i δ_j = 8·𝟙 exactly, so ω² → 4(J/m)|k|²
isotropically to leading order in every direction tested.

**Count: 1 propagating degree of freedom. The photon needs 2. G′'s premise holds.**

### 2.3 Does the corpus commit to a reading?

**Yes, and to sites.** The prompt's own diagnostic — a Hamiltonian summed over ⟨i,j⟩ of
cos(θ_i − θ_j) is site-valued, a Hamiltonian over plaquettes of link phases is link-valued — is
decided by the text: the corpus writes the former, twice (App D.3 §2.2; Vol.1 Pt1 L3050, the
Monte-Carlo route). Across 134 `.tex` files and 28,184 lines of appendix text, the **only**
plaquette term in the entire corpus is App JH4's SU(3) Wilson action. There is no U(1) plaquette
term, no U(1) link kinetic term, and no Gauss law.

**But App E.1 reasons throughout as if the link theory were in hand.** It invokes, by name, the
Wilson plaquette action reducing to the Maxwell action, the compact-U(1) Higgs/Coulomb phase
diagram, monopole condensation, and 1/e² = J. Every one of those is a theorem *about link
variables*. The site theory has no monopoles in that sense, no plaquette angle, and no Coulomb
phase to sit in. This is the gate's central finding: **the corpus writes a site theory and
borrows a link theory's phase diagram.**

---

## 3 — STEP 1: THE LINK THEORY, CONSTRUCTED

### 3.1 The Hamiltonian

On the BCT lattice at c/a = √2 (= FCC; 12 nn, **6 link directions per site**), put a compact
phase on each directed link, A_ℓ ∈ (−π, π], with conjugate integer electric field E_ℓ:

  H = (e²/2) Σ_ℓ E_ℓ² − (1/e²) Σ_△ cos(curl_△ A)

where △ runs over the minimal closed loops of the nn graph. On FCC those are **triangles**, not
squares: 24 through each site (computed, not assumed). curl_△ A = A_{0→a} + A_{a→b} − A_{0→b}.

### 3.2 The Gauss law

  G_i ≡ Σ_{ℓ ∋ i} E_ℓ − q_i = 0 at every site,

one first-class constraint per site, generating A_ℓ → A_ℓ + (λ_j − λ_i). It constrains the
longitudinal electric field and ties it to the charge at that site.

### 3.3 The degree-of-freedom count, derived

Canonically: 6 link pairs (A_ℓ, E_ℓ) per site = 12 phase-space dimensions; one first-class
constraint removes 2 (constraint surface + gauge orbit) → 10 phase-space = **5 configuration
dof per site**.

Diagonalising the linearised magnetic form M(k) (script `link_step1_dof_count.py`) resolves
those 5:

| branch | eigenvalue | count |
|---|---|---|
| exact gauge null mode | 0 for all k (‖M·g_gauge‖/‖g‖ ≈ 10⁻¹⁶) | 1 |
| **transverse, soft** | **→ 1.5 k² exactly, doubly degenerate** | **2** |
| gapped lattice modes | → 24 (cutoff-scale) | 3 |

The soft pair is degenerate and isotropic to leading order across [100], [110], [111] and [210]
(1.499993–1.499997 at |k| = 10⁻²). The three gapped modes sit at the cutoff and decouple below it.

**Continuum limit: two transverse massless polarisations with ω = c|k| — Maxwell.** Derived, not
asserted. Higher orders in (ka) were not tested and Lorentz invariance beyond leading order is
**not** established by this calculation.

### 3.4 THE PRICE TAG, ITEMISED

**New variables.** 6 compact link phases + 6 conjugate electric fields per site, replacing the
single site phase as the carrier of electromagnetism.

**New constraints.** A Gauss law at every site. The corpus has none.

**New terms.** A plaquette (triangle) magnetic term and an electric term. Neither exists in the
U(1) sector.

**Removed or reinterpreted — this is the expensive column.**

1. **"The photon is a phonon of the superfluid."** One Medium §5.1 states it flatly: a photon is
   <q>a propagating quantum of the octahedral-void phase mode</q>, and the chapter's thesis is that
   light is the sound of the vacuum. Link variables are **gauge connections, not condensate
   phases**. The photon becomes an excitation of a field the medium does not itself possess as a
   phase. **The identification does not survive its own repair.** §0.7 warned of exactly this; it
   is what the construction shows.
2. **c_s = c.** One Medium §5.2 and App B fix the photon speed from the condensate equation of
   state (g = mc²/n₀ ⇒ c_s = c identically). In a link theory the photon speed is set by the
   **ratio of the electric and magnetic couplings**, which the equation of state does not
   constrain. The parameter-free derivation of the speed of light is lost with the phonon
   identification, not separately recoverable.
3. **α₀ from void transmission.** App D.3 §3 derives g² = t_tet·t_oct as the transmission
   amplitude of **a wave crossing two voids per unit cell**. In a link theory the coupling is the
   plaquette coefficient β = 1/e². These are different objects; equating them is a **new
   postulate**, not the existing derivation carried over.
4. **Charge = vortex winding.** Survives only in modified form: see §4.
5. **θ_i itself.** It does not vanish — it becomes a neutral scalar or a matter/Higgs field
   alongside the gauge sector, and something must then be said about the extra scalar the theory
   now propagates. The corpus currently has θ doing the photon's job and no one doing θ's.

**What the reformulation does NOT cost:** the Coulomb-phase claim. That one survives, and
survives more strongly than the corpus states (§4.4).

---

## 4 — STEP 2: SURVIVAL TABLE

| test | corpus position (primary source) | under a link reformulation |
|---|---|---|
| **Phonon identification** | One Medium §5.1: photon = octahedral-void phase-mode quantum; App D.3 §2.2 calls the XY spin waves <q>the BCT photons</q> | **LOST.** A_ℓ is a connection. The medium's sound remains, but it is no longer light |
| **Vortex/charge identification** | App E.1 §2.2–2.3: 2π winding of θ ⇒ quantised flux h/e; the moving vortex <q>IS an electrically charged particle</q> | **CHANGES SIDE.** In a link theory charge is a Gauss-law source, and a vortex of a *phase* field is naturally a magnetic-flux/string object, not an electric charge, unless the phase is minimally coupled to A_ℓ — which must be added. The identification survives only by being re-derived from a different construction |
| **α₀ / transfer matrix** | App D.3 §3.1–3.3 | **PRESUPPOSES A PROPAGATING-WAVE READING.** Does not survive as a derivation; would have to be re-posed as a statement about β. Note it is *consistent*: setting β = J = 1/(4πα₀) returns e² = 4πα₀ at tree level — but that makes α₀ an **input to the lattice action** rather than an output of void geometry |
| **Confinement / Coulomb phase** | App E.1 §3.2–3.3: BCT vacuum in the Coulomb phase, monopoles suppressed by exp(−4π²J) ≈ 10⁻¹⁵ | **SURVIVES, AND IS STRENGTHENED.** See §4.4 |
| **Healing length** | ξ = a/√(8πα₀), a = ℓ_P | **CAUTION, NOT A BLOCK.** See §4.5 |

### 4.4 Confinement: where BCT sits

Compact U(1) lattice gauge theory in 4D has a confining strong-coupling phase and a Coulomb
weak-coupling phase with a massless photon. For the pure Wilson action (γ = 0) the transition sits
at **β_c ≈ 1.011** (Cox, Franzki, Jersák, Lang, Neuhaus, Stephenson, *Gauge-ball spectrum of the
four-dimensional pure U(1) gauge theory*, hep-lat/9701005, §2.1 — read in full; their own
measurement at γ = −0.2 gives β_c = 1.1607(3), and the maximal renormalised coupling in the
Coulomb phase is α_R,c = 0.19(1)).

BCT's own numbers put it at **β = J = 1/(4πα₀) = 10.742018**, i.e. **10.6 × β_c**, deep in the
Coulomb phase. The corpus's language about a Coulomb phase matches its own coupling. This is a
favourable finding and is reported as such.

The corpus's monopole arithmetic, however, is wrong. With J = 10.742018:

  S_mono = 4π²J = **424.0779**, so P ~ exp(−S) ≈ **6.7 × 10⁻¹⁸⁵**,

not the stated S ≈ 34 and P ≈ 2 × 10⁻¹⁵. The stated 34 equals **πJ = 33.75** — the quoted value
is short by a factor of 4π, traceable to the garbled intermediate line in App E.1 §3.3
("4π²/(α4πα₀)"). **The direction is unchanged and the conclusion is strengthened by 170 orders
of magnitude.** CN-LINK-03.

### 4.5 The healing length

From source: ξ = a/√(8πα₀) with a = ℓ_P, giving

  **ξ/a = 2.3175438**, ξ/R = 4.6351 (R = a/2), ξ/r_oct = 11.1901.

ξ > a means the condensate cannot vary on the scale of its own lattice spacing. A compact-link
description written **at** a = ℓ_P therefore discretises below the medium's own correlation length:
the compactness, the monopole action and β are all scale-dependent quantities being evaluated at a
scale the medium does not resolve. The physically appropriate lattice for a gauge-theory reading
is a coarse-grained one at a′ ≳ ξ, at which β and S_mono must be recomputed. This is a caution on
the *quantitative* Coulomb-phase claim (§4.4 uses a value of β defined at a = ℓ_P), not an
obstruction to the reformulation. The corpus itself (Vol.1 Pt1, App I §1.3) draws the opposite
conclusion from the same ratio — that the condensate permeates the spheres — without noticing that
the same inequality bears on whether the lattice-scale gauge theory is well posed.

---

## 5 — STEP 3: THE OBSTRUCTION CHECK

**No sound general obstruction to 2 polarisations exists in the corpus.** Searched: all 134 `.tex`,
all 387 page layers, all 14 PDFs, both raw text files, for stated rank arguments, helicity
arguments, symmetry obstructions and representation-theoretic results. What was found:

1. **App E.0 §2.1** concedes the scalar/vector mismatch and defers it to topology. A statement of
   the problem, not an obstruction.
2. **App D.3 §4.4** asserts that O_h's T1u representation is triply degenerate and that two of the
   three are transverse for propagation along c. T1u is a **vector** representation of the void's
   point group; the written dynamical field is **one scalar per site**, which transforms as A1g.
   The assertion names modes the Hamiltonian does not contain. **This is the gap, stated in the
   language of a derivation.**
3. **Helicity** appears 21 times in the `.tex` corpus, all of it Hopf-charge/twistor bookkeeping
   (Hopf charge N = twice the twistor helicity, App JH). Nothing there forbids 2 photon
   polarisations.
4. **Letter 88** proves 3+1 dimensions from D4 triality. It constrains the dimension count, not
   the polarisation count.

**So SC-LINK-5 does not fire, and the reformulation is not moot.**

One structural point from the external literature, which is the nearest thing to an obstruction
and cuts against a *cheaper* route: in 4D a massless scalar is dual to a Kalb–Ramond 2-form, and
the 2-form propagates **a single dynamical degree of freedom** — it is the scalar, re-described
(Kalb–Ramond/2-form cosmological duality literature, arXiv:2212.12427, §§5–6, read at excerpt
level; superfluid-vortex/Nambu–Goldstone dualisation, arXiv:1912.03124 reference list and
PTEP 2021 12C104 abstract, read at excerpt level). **Particle–vortex duality therefore cannot
manufacture the second polarisation.** A phase field dualised is still one dof; getting 2 requires
genuinely new variables, which is exactly the price in §3.4. This is the strongest technical
result of the gate and it is a negative one about the cheap route, not about the expensive one.

---

## 6 — CN NOTICES

| id | tier | notice |
|---|---|---|
| CN-LINK-01 | **PROVEN** | The U(1)/photon sector's only canonical dynamical variable is site-valued (θ_i, App D.3 §2.2). No U(1) plaquette term, link kinetic term or Gauss law exists anywhere in the corpus |
| CN-LINK-02 | **PROVEN** | App E.1 imports compact-U(1)-lattice-gauge-theory results (Wilson→Maxwell, Higgs/Coulomb phase diagram, monopole suppression, 1/e² = J) into a theory whose dynamical variable is a site phase. Those are theorems about link variables |
| CN-LINK-03 | **PROVEN** | App E.1 §3.3: S_mono = 4π²J = 424.078 with the corpus's own J = 10.742, not the stated ≈34; the stated value equals πJ, short by 4π. P ≈ 6.7×10⁻¹⁸⁵, not 2×10⁻¹⁵. Direction unchanged; conclusion strengthened |
| CN-LINK-04 | **PROVEN** | A_ij (App D.3 §2.4) is link-indexed but algebraically slaved to the vortex phase; it carries no degree of freedom. Calling H_coupling <q>the standard minimal coupling of a U(1) gauge field</q> overstates its status |
| CN-LINK-05 | **PROVEN** | The factor 2 in α = α₀(1−2α₀) is attributed to **two different physical objects** across the corpus: two transverse *photon polarisations* (App D.3 §4.4) and two *vortex helicities* (Monograph PLB §; One Medium §4.4). At most one can be the derivation |
| CN-LINK-06 | **PROVEN** | One Medium App C.1 obtains 2 polarisations from a **3-component void displacement field ξ_i** by gauge-removing one component — a third field content, with no Hamiltonian written for it anywhere, and in tension with One Medium §5.3's own argument that an elastic-solid vacuum is excluded by isotropy |
| CN-LINK-07 | **PROVEN** | App JH4 §JH4.2.1 puts SU(3) on the **links** of Λ_D4 with a Wilson plaquette action. The corpus can write a link theory; it has not done so for U(1) |
| CN-LINK-08 | **PROVEN** | App D.3 §3 derives the coupling from wave transmission through voids. In a link theory the coupling is the plaquette coefficient. Carrying α₀ across is a postulate, not the existing derivation |
| CN-LINK-09 | **PROVEN** | ξ/a = 2.3175 > 1: the compact-link description at a = ℓ_P is written below the condensate's own healing length. β and S_mono are scale-dependent and would need recomputation on a lattice at a′ ≳ ξ |
| CN-LINK-10 | CONJECTURE | Under a link reformulation the c_s = c derivation (One Medium §5.2) no longer fixes the photon's speed, because the photon is no longer a mode of the fluid whose equation of state was used |
| CN-LINK-11 | CONJECTURE | With β ≡ J = 1/(4πα₀), BCT sits at 10.6 × β_c and the Coulomb-phase claim holds; but α₀ then enters as an input to the lattice action, and its geometric derivation must be re-established independently |

---

## 7 — §0.7 REPRODUCED VERBATIM

> A link reformulation that yields 2 transverse polarisations would give BCT the photon's degree-of-
> freedom count. It would **not** give the photon's coupling to matter, the fine structure constant,
> Lorentz invariance of the resulting theory, or any prediction. **And it may cost an identification
> the programme is built on**: link variables are gauge connections, not condensate phases, so
> "the photon is a phonon of the superfluid" may not survive its own repair. **Gate LINK cannot
> deliver electromagnetism. At most it delivers a degree-of-freedom count and an honest price
> tag.** A favourable verdict is a ticket to a harder gate.

---

## 8 — WHAT THIS GATE DID NOT ESTABLISH

- **It did not derive electromagnetism.** As §0.7 says.
- It did not establish Lorentz invariance of the link theory beyond leading order in (ka). The
  transverse branch was checked for degeneracy and isotropy at leading order only.
- It did not establish that the link theory's photon couples to BCT matter. Minimal coupling of
  vortices to A_ℓ was not constructed.
- It did not recompute β or S_mono on a coarse-grained lattice at a′ ≳ ξ, which CN-LINK-09 says
  is the physically appropriate scale.
- It did not test whether the ξ_i displacement reading (CN-LINK-06) is viable; that is a separate
  gate and probably the next one.
- It did not price the loss of c_s = c quantitatively — only structurally.
- It scored no prediction, moved no observable, and changes no published number.

---

## 9 — CONTAMINATION STATEMENT

**Declared.** The Cold Ledger auto-loads and cannot be partially read. In this session I read
`ways-of-working.md` (protocol, toolchain, document standards) before starting. The memory listing
was present in context throughout and carries one-line summaries naming closed gates MAD, RANK, MP
and PRED; I did **not** open `audit-findings.md`, `gate-mad.md` or `gates-rank-mp-pred.md`.

I read `audit/NEXT.md` from the checkout — required by §6 of the prompt, which instructs me to
update it — **after** the analysis above was complete. It contains one-line verdicts for PSI2,
TANH, INT, C1, RANK, MP, PRED and MAD. Gate G′'s DOF count was re-derived from App D.3 and App E.1
at primary source before any of that was read, and the derivation stands on the appendices alone.

I did not consult the 9–11 September threads, BCT-X / Sandbox TOP, or any concurrent gate.

**External literature, with honesty about depth of reading:**
- Cox, Franzki, Jersák, Lang, Neuhaus, Stephenson, hep-lat/9701005 — **read in full.** Source for
  β_c ≈ 1.011 (Wilson action), β_c = 1.1607(3) at γ = −0.2, α_R,c = 0.19(1), and the
  confinement/Coulomb phase structure.
- arXiv:2212.12427 (2-form cosmological dualities); arXiv:1912.03124 (vortex dualisation
  bibliography); PTEP 2021 12C104 (Kalb–Ramond/Gross–Pitaevskii duality) — **read at excerpt
  level only**, via search results, not fetched in full. They are cited for one structural point:
  the 4D 2-form dual of a massless scalar propagates one degree of freedom. That point is standard
  and independently checkable, but this session did not verify it from the full texts.

---

## 10 — ARTEFACTS

- `link_step0_site_dof.py` — site-theory branch count and isotropy check.
- `link_step1_dof_count.py` — constructed link theory: 24 triangles/site, 6×6 curl-energy matrix,
  gauge null mode, 2 soft transverse modes (→1.5k², isotropic), 3 gapped modes.
- `link_step3_numbers.py` — mpmath at 60 dps working / 40 dps reported: α₀, α, ξ/a, ξ/r_oct, J,
  S_mono, and the reconstruction of the corpus's erroneous "34".
- `gate_LINK_prompt_asrun.md` — the prompt as run, digest as above.
