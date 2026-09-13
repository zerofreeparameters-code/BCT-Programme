# GATE C1 — RESULT

**Does the interior carry its own healing length?**

Run 12 September 2026. Cold Ledger gate, fresh thread.
Prompt pre-registered at commit `47d3eefe6c01bc2c3a7e0d9bbe791b1b989396b6`,
path `audit/gates/gate_C1_prompt.md`.

---

## 0. PRE-REGISTRATION

| | |
|---|---|
| Fetched from | `https://raw.githubusercontent.com/zerofreeparameters-code/BCT-Programme/47d3eefe6c01bc2c3a7e0d9bbe791b1b989396b6/audit/gates/gate_C1_prompt.md` |
| SHA-256 of file as received | `c9f27b54ce8633d620f927879cf7b627b5c2af7c0f010e21ea2b73a7cad421b2` |
| SHA-256 supplied by operator | `c9f27b54ce8633d620f927879cf7b627b5c2af7c0f010e21ea2b73a7cad421b2` |
| Size | 7731 bytes (operator: 7731) |
| git blob SHA-1 | `af31a3f500a522d786983b627738760093af3523` |
| **Verdict** | **MATCH** |

Third, independent confirmation: the repository's own copy of the file at the
pinned commit, obtained by `git clone` + `git checkout 47d3eefe` rather than by
raw fetch, hashes to the same `c9f27b54…`. Two transport paths, one digest.

**Procedural note, for the ledger.** The prompt as delivered to this session
carried the URL and the commit SHA-1 but **not** the SHA-256 line. This session
computed the digest, reported it, and **refused to self-authorise** the
comparison — the commit SHA-1 in the URL is a different hash of a different
object and cannot be compared to a SHA-256. The operator then supplied
`c9f27b54… / 7731 bytes` and confirmed the pre-registration had contained it;
the digest line was lost in transit, not absent from the pre-registration.
The file was not opened until after the match was confirmed.

---

## 1. SEARCH-SPACE COVERAGE — reported before any other number

### 1.1 Repo

Pulled by `git clone` + checkout of the pinned commit. **The tarball route was
blocked**: `codeload.github.com` and `api.github.com` both returned
`403 GitHub access to this repository is not enabled for this session`, so no
tarball SHA-256 can be recorded for this run. The commit SHA-1 is the integrity
anchor instead, and it is exact.

| | count | note |
|---|---|---|
| `.tex` in repo | **134** | matches §0.5 |
| `.tex` at tree root, outside `tex/` | **26** | matches §0.5 |
| `tex/*.tex` | **108** | a `tex/*.tex` glob would have missed 26 files (19.4%) |
| `.tex` searched by this gate | **134 / 134 (100%)** | full-text grep, all of them |
| `.tex` read in full or in substantial part | **11** | AZ6, AZ7, F(via extract), JH_FINAL, KA1, KA4, L19, L27, L36_OHC, L60, L64, ChemistrySeries_VolK |
| repo `.pdf` | 6 | typed with `file`: 6/6 true PDFs, 23 pages |
| repo `.md` | 28 | `audit/notes/` (3) **not read** — see §8 |

Counts from full-corpus greps (all 134 `.tex`):

| term | files |
|---|---|
| `OHC` | **86** |
| `interior` | 38 |
| `Gross-Pitaevskii` | 13 |
| `\xi` | 9 |
| `healing` | **5** |
| `OHC` **and** `Bessel` (site-local interior structure required) | **45** |

### 1.2 Mount

**The mount presented differently in this session than §0.5 describes, and this
is a material deviation that must be recorded.** §0.5 describes a filesystem of
49 files: 33 ZIP archives of page images with `.txt` layers, 14 true PDFs, 2 raw
UTF-8 files that `file` reports as `data`. In this session the mount was reached
through the claude.ai Project API, which returns two kinds of object:

- **`blob`** — the original bytes. 14 of these. Downloaded, typed with `file`,
  page-counted with `pdfinfo`, text-extracted with `pdftotext -layout`.
  **All 14 are true PDFs. 92 pages. All 14 carry a real text layer** (11.2 kB –
  45.7 kB extracted each; none image-only, so no OCR was needed).
  This is §0.5's "14 are true PDFs", confirmed by typing, not assumed.
- **`document`** — a server-side text extract, no bytes. 35 of these
  (33 in `files` + 2 appendix volumes in `docs`). These are §0.5's 33 ZIP
  page-image archives plus the 2 raw-text files.

The two raw-UTF-8 files were located and confirmed exactly as §0.5 warns:
`4_BCT_Appendices_Volume1_2026_compressed_Part1.pdf` (849 709 bytes) and
`_Part2_compressed.pdf` (713 071 bytes) both land on disk as files that `file`
reports as **`data`**, decode cleanly as UTF-8 (0 null bytes, 825 273 chars in
Part 1), and open with neither `pdftotext`, `pymupdf` nor `unzip`. **App J and
App K live in Part 1**, as §0.5 states. They are the single most load-bearing
source for this gate.

| mount file | type as found | coverage |
|---|---|---|
| AppVol1 Part 1 (Apps D0–~CV, Phases 1–19) | raw UTF-8, `file`→`data` | **full text searched**; Apps F, H, I, J, K, AG, AI read |
| AppVol1 Part 2 (Apps CW–ER, Phases 20–31) | raw UTF-8, `file`→`data` | **full text searched**. `healing` = 0, `interior` = 0, `Gross-Pitaevskii` = 0 |
| AppVol1 Part 3 (Apps HH2–HJ2, Phases 50–66) | document extract | full text searched; App HI5 read |
| BCT Monograph v21 | document extract | read in full |
| BCT OneMedium JournalEdition v2 | document extract | read in full |
| BCT_AppendixJH4_YangMills | document extract | read in full |
| 14 blob PDFs (92 pp) | true PDF, text layer | **full text searched**. `healing` = **0 across all 92 pages** |
| remaining 28 `document` files | not retrieved | **coverage gap — declared, see below** |

**Declared coverage gap.** 28 of the 49 mount files were not retrieved: the 12
individual Letter PDFs (1–12), `BCT_Letters_Vol2b 5 1`, `BCT_Special_Issue_
Geometry_of_the_Void`, `BCT_PeriodicTable_Round_v12 1`, `BCT_Letter195_
UniverseAsymmetry`, the 8 leptogenesis appendices (KE6, JX6, KN6, KJ6, KC6,
LA6, LB6, KX6), the 3 `AccidentallySolved` files, `NPBS2601701 3`, and
`CP_Book_Proposal_form`. Two mitigations, stated so the gap can be weighed
rather than trusted: (i) `tex/BCT_Letters_Vol2b.tex` is in the repo and was
searched — 0 hits for `healing`, `interior`, `OHC`; (ii) the 8 leptogenesis
appendices sit in Phases 79–85, entirely downstream of the Planck-scale
condensate sector. **Neither mitigation covers the 12 Letter PDFs.** If a
statement of ξ₂ exists there, this gate did not see it.

**Net: 21 of 49 mount files retrieved and searched (43%); 92 PDF pages
typed and page-counted; ~1.56 MB of raw appendix text searched in full;
134 of 134 `.tex` searched (100%).**

---

## 2. VERDICT

> ### **SC-C1-3 — ξ₂ is not determined by the corpus.**
>
> The gate **halts and reports**, as SC-C1-3 directs. §3 is delivered both ways.
>
> **SC-C1-4 does not close the gate at Step 0.** Not every interior is a
> restriction: App I, App JH and Letter 36 each commit to the interior as a
> field with structure of its own. But the *one* appendix that actually
> formulates an interior action — App J — makes it a restriction of the
> exterior field, and therefore assigns it no second healing length by
> construction. The corpus holds both positions simultaneously.
>
> **SC-C1-5 is triggered in part, but does not block the gate.** The symbol ξ
> denotes **at least five numerically distinct objects** across the corpus,
> spanning 17 orders of magnitude (§5.3). Nevertheless the lattice healing
> length is recoverable: one value, ξ = 2.31754 ℓ_P, is reached independently
> by two routes and is the value every downstream user propagates. ξ is
> *reproducible*. It is not *derived* — see CN-C1-04.

**The one-line answer to the question as asked.** The corpus has one healing
length in practice, ξ ≈ 2.32 ℓ_P, and the interior is claimed to share it
(App J) — but that sharing is an assumption about the interior's coupling,
mass and density, none of which the corpus supplies, and it is contradicted by
the corpus's own claim that the interior propagates at a different speed from
the exterior. The corpus does not determine ξ₂ because it does not determine
the interior's equation of state.

**What settling it would take, and at what price:** see §7.

---

## 3. WHAT SETTLING THIS BUYS — §0.6, reproduced verbatim

> Determining ξ₂ does **not** validate or refute any BCT prediction, supply a
> mechanism, or close a sector. What it decides is **which regime the model is
> in**, and therefore which claims are even available to be argued. A single
> healing length longer than the lattice spacing forbids site-local structure;
> an independent short interior healing length permits it. **Either verdict is
> a precondition for other work, not a result about physics.** A favourable
> verdict is a ticket to a harder question, not an answer to one.

---

## 4. STEP 0 — IS THERE A SECOND FIELD TO CARRY A SECOND ξ?

Gate INT's SC-INT-4 (three distinct interior commitments, re-scoped to
enumeration) is inherited as a fact and nothing else. Enumerated afresh from
primary source, this gate finds **five**, not three. They are not versions of
one position; three of them are mutually exclusive as physics.

### I-1 — Interior as inert hard boundary (Apps D–H)

| | |
|---|---|
| **Location** | AppVol1 Part 1, Apps D0–H |
| **Quoted** | "the BCT model treated the vacuum as a single-component superfluid condensate: one order parameter Ψ = \|Ψ\| exp(iθ) filling all of space, with the plasma spheres acting as hard boundaries that create the void geometry. **The spheres were obstacles, not participants.**" (App I §1.1, characterising D–H) |
| **Separate field?** | No. No interior field exists. |
| **Own J₂, μ₂?** | N/A |
| **ξ₂?** | **Absent** — the question does not arise. |

### I-2 — Interior as a second order parameter (App I)

| | |
|---|---|
| **Location** | AppVol1 Part 1, **Appendix I, "The Dual-Phase Medium"**, §2.1, §2.3, §6.1 |
| **Quoted** | "The revised BCT model contains **two coupled order parameters**: Ψ₁(r) = ρ₁(r) exp(iθ₁) [exterior phase — void condensate]; Ψ₂(r) = ς₂(r) exp(iφ₂) [interior phase — sphere condensate] … The full BCT action is S_BCT = S[Ψ₁] + S[Ψ₂] + S_int[Ψ₁, Ψ₂] … **S[Ψ₂] is the interior condensate action — not yet formulated.**" |
| **Separate field?** | **Yes, explicitly.** Two order parameters, two phases, an inter-component coupling term. |
| **Own J₂, μ₂?** | **Yes — J₂ is named as an independent quantity.** "m_gap² = λ × ρ₁ × ρ₂ / (J₁J₂)^(1/2) where J₁, J₂ are the respective stiffnesses." §6.1 tables J₂ as a quantity still "to compute", "From sphere interior GP action (RG of sphere plasma)". |
| **ξ₂?** | **Absent, and admitted absent.** "ρ₂ (sphere interior condensate density): determined by the sphere interior action S[Ψ₂] — **not yet computed**"; "λ (inter-component coupling): set by the physics at the sphere surface — **not yet formulated**." With neither g₂ nor n₂ nor m₂, ξ₂ = ħ/√(2m₂g₂n₂) is undefined. |

### I-3 — Interior as the same field restricted to r < R (App J)

| | |
|---|---|
| **Location** | AppVol1 Part 1, **Appendix J, "The Sphere Interior Action S[Ψ₂]"**, abstract, §1.2, §5.1 |
| **Quoted (abstract)** | "the **same** Gross-Pitaevskii condensate fills both the interstitial void space (exterior) and the sphere interiors" |
| **Quoted (§1.2)** | "**The interior action S[Ψ₂] is the same GP action as the exterior condensate (same J, same ξ, same nonlinear coupling), restricted to r < R.** The ONLY difference from the exterior is the boundary condition at r = R: a derivative jump of magnitude σ_s/J × Ψ(R), imposed by the double-layer shell. **There is no new field, no new coupling, and no new free parameter.**" |
| **Separate field?** | **No — explicitly a restriction of one field to a subregion.** |
| **Own J₂, μ₂?** | **No.** Same J, same g, same μ, by assertion. |
| **ξ₂?** | **Stated, and stated equal to ξ** — by the gate's §1 rule, a restriction carries no second healing length by construction. This is I-3's whole content on the question. |

App J **retracts App I's second field without saying so.** App I's open problem
was "compute S[Ψ₂]"; App J's answer is "S[Ψ₂] is S[Ψ₁] on a smaller ball". The
two appendices are consecutive, the second cites the first, and the second uses
the first's symbol Ψ₂ while denying it is a second field.

### I-4 — Interior as a ℂ² spinor field with its own topology and phase velocity (App JH / Letter 36 / KA1 / KA4)

| | |
|---|---|
| **Location** | `tex/BCT_Appendix_JH_FINAL.tex` §4.1, §4.2, Result 6; `tex/BCT_Letter36_OHC_tex.tex`; `tex/BCT_Appendix_KA1.tex` §2; `tex/BCT_Appendix_KA4.tex` §2 |
| **Quoted (JH §4.1)** | "Let Ψ_int : ℝ³ ⊃ B³(R_s) → **ℂ²** be the **two-component interior condensate field**, with \|Ψ_int\|² = \|ψ₊\|² + \|ψ₋\|² = ρ₀ (constant bulk density)." |
| **Quoted (JH abstract)** | "the ground-state interior phase velocity is v_ph = κ₀/R_s ≈ **6.78 c**, superluminal but causally screened behind the α₀ Josephson shell" |
| **Quoted (KA1 §2)** | "The OHC interior condensate Ψ_int satisfies the Gross-Pitaevskii equation within each Planck sphere of radius R = ℓ_P/2 … Linearised modes are spherical Bessel resonances indexed by (n, ℓ, m)" |
| **Separate field?** | **Yes — and a different *kind* of field from either I-2 or I-3.** App J's interior is a single complex scalar with an l = 0 radial mode j₀(κr); JH's is a two-component spinor field whose unit-normalised form maps S³ → S², classified by π₃(S²) = ℤ. A ℂ¹ field has no Hopf invariant. |
| **Own J₂, μ₂?** | **Not stated.** JH's free energy (Eq. free-energy) writes ħ²/2m and g without saying whether they are the exterior's. |
| **ξ₂?** | **Absent as a symbol, but implied ≠ ξ.** A distinct interior phase velocity requires, by the corpus's own equation of state c_s² = g n₀/m (One Medium, App B, Step 3), a distinct g/m, hence a distinct ξ. See §5.4. |

### I-5 — "OHC" as the whole vacuum, with a hadronic-scale healing length (Letters 60, 64; App AF1; Letter 104)

| | |
|---|---|
| **Location** | `tex/BCT_Letter64.tex` §; `tex/BCT_Letter60.tex`; `tex/BCT_Appendix_AF1.tex`; `tex/BCT_Letter104_ThreeBody.tex` |
| **Quoted (L64)** | "ξ = ħ/(m_defect c_s) is **the OHC healing length**, and m_defect = H × E_D4/c² where E_D4 = Λ_QCD × π⁵/6 = 11.22 GeV" |
| **Quoted (AF1)** | "ξ_OHC is **the OHC coherence length**: ξ_OHC = (ħ/m_P c)√(S_D4/2π) = ℓ_P√(50.75/2π) = **2.84 ℓ_P**" |
| **Separate field?** | Ambiguous, and the ambiguity is the finding. **OHC is defined in App JH and Letter 36 as an interior object** — "the ground-state field configuration of the BCT **interior** condensate Ψ_int". Letters 60/64 then use "the OHC vacuum", "the OHC phonon dispersion", "the OHC healing length" for the medium as a whole. |
| **ξ₂?** | **Two further stated values, mutually inconsistent and inconsistent with ξ:** 2.84 ℓ_P (AF1, L104) and ħc/(11.22 GeV) = 1.76 × 10⁻² fm (L64, Prediction #121). |

### Step 0 conclusion

| | |
|---|---|
| Interiors enumerated | **5** |
| Committing to a separate interior field | **3** (I-2, I-4, I-5) |
| Committing to a restriction | **1** (I-3) |
| Committing to no interior at all | **1** (I-1) |
| Naming an independent stiffness J₂ | **1** (I-2) |
| Stating a value for ξ₂ | **2** (I-5 twice, at two different values) |
| Deriving ξ₂ from an interior action | **0** |

**§2 therefore runs.** Not all interiors are restrictions, so the gate does not
close at Step 0.

---

## 5. STEP 1 — WHAT FIXES ξ₂, IF ANYTHING?

### 5.1 ξ derived from primary source

The corpus's GP action, quoted from AppVol1 Part 1 §AI.2 and repeated in
One Medium App B Eq. (16):

    S_GP = ∫ d⁴x [ (iħ/2)(Ψ*∂_tΨ − Ψ∂_tΨ*) − (ħ²/2m)|∇Ψ|² − V(|Ψ|²) ],
    V(|Ψ|²) = (g/2)(|Ψ|² − n₀)²

The healing length is defined in **App AZ6, line 168**:

    ξ = ħ/√(2 m g n₀)          i.e.  ξ² = (ħ²/2m) / μ,   μ = g n₀

**The value the corpus uses is not obtained from that equation.** It is
asserted, in one line, in **Appendix F** (AppVol1 Part 1, l. 3003–3007):

    ξ = a/√(8πα₀) = ℓ_P/√(8π × 7.408×10⁻³) = ℓ_P/0.432 ≈ 2.3 ℓ_P

Reproduced to 12 digits by `gate_C1_step1_xi.py`:

| quantity | value | corpus print |
|---|---|---|
| r_oct = (√2−1)/2 | 0.207106781187 | 0.20711 |
| r_tet = (√6−2)/4 | 0.112372435696 | 0.11237 |
| α₀ = r_oct r_tet/π | 0.00740805572755 | 0.0074081 |
| **ξ = a/√(8πα₀)** | **2.31754379491 ℓ_P** | 2.3175 (App I §1.3) |
| ξ/a | 2.3175438 | — |
| ξ/R, R = a/2 | 4.6350876 | 4.6351 (App I §1.3) |
| ξ/r_oct | **11.190091** | **11.19 (Letter 19)** |

**Independent confirmation of the value.** Letter 19 §Predictions states, as a
falsifiable BCT prediction, "ξ/r_oct = 1/[r_oct√(8πα₀)] = 11.19". Computing
ξ from that relation alone gives 2.3175249 ℓ_P — the same number, by a route
that never passes through App F's assertion. **The value is reproducible.**

**The lattice spacing is the Planck length**, confirmed three times
independently: App K §1.1 ("the nearest-neighbour distance in BCT at c/a = √2
is exactly a = 1 (in Planck units, since a = 2R = 1 ℓ_P)"); App JH4 Def. JH4.1
("the lattice spacing is a = ℓ_P"); App I §1.2 volume table (R = 0.5 ℓ_P).
So **ξ = 2.3175 a and ξ = 4.635 R**, and the phrase "2.32 ℓ_P" and the phrase
"2.32 lattice spacings" denote the same thing.

### 5.2 ξ is reproducible but not derived

Put App F's own stiffness and App AZ7's own chemical potential into App AZ6's
own definition and the number does not come out. From
`gate_C1_step3_xi_conflicts.py`:

| corpus statement | location | value |
|---|---|---|
| ħ²/2m = J = 1/g₀², g₀² = 4πα₀ | App F, l. 2038–2040 | J = 10.742018 |
| μ = U = t_kin = t | App AZ7 Lemma 2 + Thm (t/U = t_kin/t_kin = 1) | — |
| t = α₀ | App AZ7 Lemma 1; App K §1.2 | 0.0074081 |
| **⇒ ξ = √(J/μ)** | by App AZ6's definition | **38.079 ℓ_P** |
| ratio to the value in use | | **16.43 ×** |

For ξ = 2.3175 ℓ_P to follow from App AZ6's definition with App F's J, one
needs **μ = 2.000 m_P c² exactly** — a value the corpus never states, and 270×
App AZ7's μ = α₀. Read the other way, with the tight-binding gradient
coefficient ħ²/2m = t a² = α₀ a² and App AZ7's μ = t_kin = α₀, App AZ6's
definition gives **ξ = a exactly, 1 ℓ_P** — inside the very appendix (AZ7)
whose input list reads "Healing length ξ = 2.32 ℓ_P".

**ξ = a/√(8πα₀) is an assertion with a self-consistent downstream, not a
derivation.** It is equivalent to ξ = a√(J/2), i.e. to choosing μ = 2; nothing
in the corpus chooses it.

**Citation defect, checked directly.** App AZ6 l. 169 and App AZ7 l. 113 both
cite "**App E.3**" for ξ = 2.32 ℓ_P. App E.3 (AppVol1 Part 1, ll. 2488–2789,
"The Einstein Equations from BCT Pressure Dynamics") contains **zero**
occurrences of `ξ` or `healing`. The correct source is App F, which App AG
(l. 8998) cites correctly.

### 5.3 The symbol ξ, across the corpus

| object called "ξ" / "the healing length" | where | value |
|---|---|---|
| a/√(8πα₀) — the lattice healing length | App F, I, J, AG, AI, AZ6, AZ7, L19, One Medium | **2.31754 ℓ_P** |
| ξ = R_sphere, "the tube radius is the healing length ξ ≪ R" | **App F, same appendix, l. 2846, 2900, 2921** | 0.5 ℓ_P |
| ξ = r_oct, "tight-binding limit" | **App F, l. 3031** | 0.20711 ℓ_P |
| ξ_OHC = ℓ_P√(S_D4/2π), "the OHC coherence length" | App AF1, Letter 104 | **2.84911 ℓ_P** |
| ξ = ħc/Λ_QCD, "the QCD healing length" | App HI5 (retired T_c formula) | **0.8969 fm** |
| ξ = ħ/(m_def c_s), "the OHC healing length", Prediction #121 | Letter 64 | **0.01759 fm** |

Spread between the Planck-scale and the hadronic-scale ξ: **4.7 × 10¹⁷**.

Two of these sit in the *same appendix*: App F asserts "the tube radius is the
healing length ξ ≪ R" three lines before computing ξ = 2.3 ℓ_P = 4.6 R, and
uses ξ = r_oct thirty lines later.

One of them is a category error that can be traced exactly. App AF1's
ξ_OHC = √(S_D4/2π) = **2.84911** is numerically identical, to nine figures, to
the quantity printed at AppVol1 Part 1 l. 8024–8025 as
"J = (S_D4/(2π))^(1/2) = **2.84910938**" — a **dimensionless zero-mode
Jacobian in the instanton moduli measure**, from a different calculation in a
different sector. A dimensionless Jacobian has been read as a length in Planck
units and propagated into two documents as "the OHC coherence length".

### 5.4 What ξ₂ would be on the corpus's own stated inputs

The corpus does fix its exterior equation of state. One Medium App B, Step 3
(and this is the load-bearing step of the entire gravity claim):

    c_s² = ∂P/∂ρ|_ρ₀ = g n₀ / m,   and the Josephson condition requires
    g = m c² / n₀,   hence   c_s = c   identically.

Combining with App AZ6's ξ = ħ/√(2mgn₀):

    ξ = ħ/√(2m · mc²) = ħ/(√2 m c)

So **the healing length is fixed by the condensate's quantum mass m alone**,
and reciprocally: a medium with ξ' ≠ ξ is a medium with m' ≠ m, hence
g' ≠ g, hence — by the same chain — **c_s' ≠ c**. Healing length and
propagation speed are not independent in this corpus. They are the same
statement.

Now apply that to the interior. The interior needs g₂, n₂, m₂.

| input needed for ξ₂ | what the corpus supplies |
|---|---|
| interior stiffness J₂ | App I §6.1: "**From sphere interior GP action (RG of sphere plasma)**" — listed as a quantity to be computed. Never computed. |
| interior density n₂ / ρ₂ | App I §2.3: "determined by the sphere interior action S[Ψ₂] — **not yet computed**" |
| interior coupling g₂ / λ | App I §2.3: "set by the physics at the sphere surface — **not yet formulated**" |
| interior mass m₂ | Nowhere. |
| interior sound speed c_s,₂ | **Contradicted twice over** — see below |

**This is the whole of Step 1's answer. Two of the three inputs ξ₂ requires are
named by the corpus as open problems, in the same appendix that introduces the
second field. The third is never named at all.**

App J's reply to this is not a computation of the missing inputs. It is the
assertion that they equal the exterior's: "same J, same ξ, same nonlinear
coupling". That assertion is exactly the thing in question, and the corpus
supplies a reason to doubt it in its own description of what a sphere is — a
**"double-layered plasma sphere"** with surface charge ±σ, a potential step ΔV,
and (App I §3.1) "a CONFINED interior (r < R₀) with its own potential
landscape". A confined plasma with its own potential landscape is not, prima
facie, the same medium at the same density with the same coupling as the
condensate outside it.

### 5.5 Testing the argument that ξ₂ = ξ

**The argument, at its strongest.** The interior and exterior are one
Gross-Pitaevskii field. The double layer is a surface term, a delta-function
shell at r = R with no volume potential inside (App J §1.2: "Inside the sphere
(r < R), the GP equation is −ξ²∇²Ψ + g|Ψ|²Ψ/J = Ψ with NO volume potential").
A boundary condition changes the mode spectrum; it does not change the
parameters of the bulk equation. Since g, m and n₀ are properties of the field
and not of the region, ξ₂ = ξ trivially. On this reading the question dissolves,
and it dissolves cleanly: App J needs no new parameter, and that parsimony is
a genuine virtue.

**Steelman of the opposite.** Take the corpus's own words seriously and the
interior is *not* the same medium:

1. **The corpus says the interior propagates at a different speed.** App JH
   Result 6, Letter 36 Result 5, `BCT_VortexTopology_PRL` p. 2 and
   `BCT_GeometryOfEverything_v4` all state an interior phase velocity of
   **6.78 c**; GeometryOfEverything adds "**the interior metric differs from
   the exterior**". By the chain in §5.4, a different propagation speed *is* a
   different g/m *is* a different ξ₂. App J's "same ξ" and App JH's "6.78 c"
   cannot both be true.
2. **The corpus says the interior is a different kind of field.** App JH §4.1
   makes Ψ_int a ℂ² two-component field; App J made it a ℂ¹ scalar. A
   two-component condensate has two healing lengths generically, not one.
3. **The corpus says the interior is a plasma, not the condensate.** "Planck-scale
   plasma sphere", "double-layered", with "its own potential landscape". A
   charged confined plasma at density n₂ ≠ n₀ has ξ₂ = ξ√(n₀/n₂) at minimum.
4. **The corpus assigns the interior its own coherence length, twice, at two
   values** — 2.84 ℓ_P (App AF1, L104) and 1.76 × 10⁻² fm (L64) — neither
   equal to ξ and neither equal to the other.

**Is ξ₂ ≪ a derivable or excluded?** Neither. For ξ₂ ≪ a = 2R one needs
n₂/n₀ ≳ 22 (from ξ₂ = ξ√(n₀/n₂) and ξ₂ < R). The corpus states no interior
density at all, so the condition is neither met nor excluded. It is *not
absurd*: the sphere interiors hold **74.0% of the unit-cell volume** (App I
§1.2 table) against 4.4% for the octahedral void, so a denser interior is
geometrically unremarkable. But a density is not stated, and the gate will not
supply one.

**The claimed interior/exterior mismatch does not survive checking.** The
single quantitative statement in the corpus that the interior differs from the
exterior is App JH Eq. (phase-velocity):

    v_ph = κ₀ / R_s = 3.39 / 0.5 c ≈ 6.78 c

**This is dimensionally invalid.** In App J's own convention κ₀ is a wavenumber
— App J §2.2 gives the mode energies as E_n = ħc κ_n and tabulates
"κ₀ = 3.3905 → 3.39 m_P c²" — so κ₀/R_s has units of 1/length², not velocity.
In App JH's and Letter 36's own competing convention κ₀ is the dimensionless
Bessel argument (JH: "j₀(κ₀ r/R_s)"; L36 Eq. spectrum: ε₀ = ħ²κ₀²/2mR_s²), and
then κ₀/R_s has units of 1/length, still not a velocity. A phase velocity is
ω/k; with App J's own ω = cκ, **v_ph = c exactly**.

So the position is this. **Remove the 6.78 c and nothing in the corpus
determines ξ₂ ≠ ξ. Keep it and it contradicts App J's "same ξ". Either way,
ξ₂ is not determined.** That is SC-C1-3.

---

## 6. STEP 2 — THE REGIME, AND WHAT EACH BRANCH PERMITS

### 6.1 The regime, by computation

| ratio | value |
|---|---|
| ξ / a | **2.3175** |
| ξ / R | **4.6351** |
| ξ / r_oct | 11.190 |

**Neither limit holds. This is a prompt defect and is recorded as one rather
than force-fitted.** §3 of the prompt offers two limits, ξ ≫ a and ξ ≪ a, and
asks which one each branch sits in. The answer computed from the corpus's own
numbers is **neither**: ξ/a = 2.32 is an O(1) number. The BCT lattice is in the
crossover, roughly two lattice spacings of coherence — a regime in which
site-local structure is *suppressed*, not *forbidden*, and in which the
suppression is a finite energy penalty that can be quoted.

The right quantity is the gradient-energy cost of forcing the condensate to
vary on scale L, which is (ξ/L)² in units of the condensation energy:

| structure on scale | L (ℓ_P) | penalty (ξ/L)² |
|---|---|---|
| one lattice spacing a | 1.0 | **5.37** |
| one sphere radius R | 0.5 | **21.5** |
| octahedral void radius r_oct | 0.2071 | 125.2 |
| App J's interior ground mode, 1/κ₀ | 0.2950 | **61.7** |

**This is the substantive regime finding.** The gate's framing — "a single
healing length longer than the lattice spacing forbids site-local structure" —
is right in direction and wrong in strength for ξ/a = 2.32. Site-local
structure costs 5× to 60× the condensation energy per site. That is a
suppression the corpus must pay for and nowhere prices; it is not a
prohibition.

### 6.2 The consequence map — both columns filled

Branch A: **ξ₂ = ξ = 2.3175 ℓ_P** (App J's position; the interior is a
restriction).
Branch B: **ξ₂ ≪ ξ, short enough to resolve the sphere** (App I / JH / KA's
requirement; requires an interior density ≳ 22 n₀ or an equivalent parameter).

| claim, by document and section | **Branch A — ξ₂ = ξ** | **Branch B — ξ₂ ≪ a** |
|---|---|---|
| **Interior condensate modes, κ₀ = 3.3905, κ₁ = 9.5139, κ₂ = 15.762** (App J §2.2) | **Not condensate modes.** kξ = 7.86, 22.0, 36.5 — all far above the Bogoliubov crossover (§6.3). The eigenvalue equation κ cot(κR) = −1/ξ + α₀ is still *solvable* and reproduces exactly, but its solutions describe single-particle states in a delta-shell well, not collective excitations of a condensate. The κ values survive as arithmetic; the word "condensate" does not. | **Modes are legitimate.** With ξ₂ ≲ 0.1 ℓ_P, κ₀ξ₂ ≲ 0.34 and the ground mode is a genuine collective mode of an interior condensate. The whole Bessel ladder becomes physical. |
| **Josephson network of 12 junctions per sphere, bandwidth W = 12 E_J, plasma frequency ω_J = √(8E_J E_C)/ħ** (App I §3.3) | **Not a network.** A Josephson junction requires two condensates with independently definable phases. At ξ₂ = ξ = 4.64 R the phase cannot vary across a sphere, so interior and exterior share one phase: there is no phase difference to carry a current and no E_J. The junction picture is a redescription of one order parameter. E_C and ω_J are undefined. | **Network is well posed.** Interior phases are independently definable, E_J = σ_s × overlap is meaningful, the band structure and ω_J follow. |
| **Site-local topological charge H = 1 per sphere; \|H\| ≤ n per mode** (App JH §4.2, Result 1; KA4 Thm 1; L81) | **Not available.** A Hopf invariant requires a map S³ → S² defined *within* one sphere, which requires the order-parameter direction to vary on scale ≤ R. At ξ/R = 4.64 it cannot. Hopf charge would be a property of the whole lattice, not of a site — and then "H = 1 per sphere" is meaningless and the per-site counting collapses. Note that INV-0020 already flags KA4 Thm 1 as vacuous on independent grounds (α₀ cancels identically); this is a second, separate failure. | **Available.** Site-local Hopf charge is exactly the structure a short ξ₂ permits. This is the branch the entire OHC programme needs. |
| **Interior phase velocity v_ph = 6.78 c** (App JH Result 6; L36 Result 5; VortexTopology_PRL; GeometryOfEverything_v4) | **False, and false on its own terms.** ξ₂ = ξ ⇒ same g, m ⇒ c_s,int = c_s,ext = c. Independently the formula v_ph = κ₀/R_s is dimensionally invalid under both of the corpus's own readings of κ₀ (§5.5). | **Not established either.** Branch B permits c_s,int ≠ c, but the *value* 6.78 c does not follow: it is a wavenumber divided by a length. Branch B makes an interior velocity *possible*; it does not make this number right. **This claim fails in both columns** — the only claim in the map that does. |
| **Chemistry series: shell capacity 2n², Pauli exclusion, noble-gas inertness, bond angles, the periodic table** (L78, L80, L81, L83, L84, L85, KA1 §2–3, KA4 §2–3, `BCT_ChemistrySeries_VolK.tex`) | **Not available.** Every one of these rests on "the n-th OHC Bessel resonance mode" *inside one Planck sphere* of radius 0.5 ℓ_P, with n = 1, 2, 3, 4 resolving structure at 1/κ_n ≈ 0.29, 0.11, 0.063 ℓ_P. Under Branch A the condensate cannot support structure at any of those scales. **45 of the 134 `.tex` files invoke OHC Bessel modes.** | **Available in principle.** Branch B is what these claims need. It does not make them correct — the mode-to-shell mapping, the 2n² counting and the \|H\| ≤ n theorem each need separate verification — but it makes them arguable. |
| **Electron-mass mechanism via interior/exterior mismatch** (App JH Result 6; App J §4.3) | **Not available.** The Kondo-like mechanism is driven by the phase-velocity mismatch, which is zero in this branch. App J's §4.1 already rules out the Kondo route on density-of-states grounds by a factor of 10³⁵⁷⁰⁰⁰. | **Mechanism is open, not supported.** A real mismatch would supply the ingredient; App J's own arithmetic (δm ~ α₀²/κ₀ ~ 1.6×10⁻⁵ m_P, "10¹⁸ times larger than m_e") shows the perturbative version does not reach m_e in either branch. |
| **α = α₀(1−2α₀), the 92 sub-1% predictions, Λ_QCD, m_P = M_R/α₀², the Td orbit masses, CKM/PMNS** | **Unaffected — and this is a checked claim, not a courtesy.** The Monograph's Appendix A notation guide and Appendix B master table were read in full: **ξ appears in neither**, and no entry in the 92-prediction table has a source appendix in the D–L interior sequence. The predictions run on r_oct, r_tet, Λ_QCD and S_D4. | **Unaffected, same evidence.** |
| **Prediction #121 (rate of classicality emergence ~ e^{−R/ξ})** (L64) | **Affected.** Its ξ is the hadronic-scale ħ/(m_def c_s), not the lattice ξ; the prediction inherits whichever ξ is meant and the corpus does not say. | **Affected identically.** Branch choice does not rescue it; the ambiguity is in the symbol, not the regime. |
| **Letter 19's "vortex healing ratio ξ/r_oct = 11.19", offered as a falsifiable structural invariant** | **Survives as arithmetic.** The ratio is exactly 1/[r_oct√(8πα₀)] and reproduces to 6 figures. What it does *not* survive is §5.2: ξ itself is asserted rather than derived, so the "prediction" is a restatement of that assertion. | **Fails.** If ξ₂ ≠ ξ, the electron vortex — which App F places filling the oct void, ξ > r_oct — sits at an interface between two healing lengths, and a single ratio does not characterise it. |
| **Gauss–Bonnet coefficient α_GB = c⁴ξ²/(16πG)** (App AZ6 l. 515) | Unaffected in form; inherits ξ's 16× uncertainty from §5.2 in value. | Same. |

**Branch A is the branch App J puts the corpus in, and it is the branch that
costs the most.** It preserves every published prediction and removes the
entire interior programme: the OHC, the Hopf charge, the Josephson network, the
twistor correspondence, and all of chemistry. Branch B preserves the interior
programme and requires an interior density or coupling that the corpus does not
state and has never computed.

---

## 7. STEP 3 — THE MODE CHARACTER CHECK

Independent of ξ₂. Where do the corpus's stated interior modes sit relative to
the Bogoliubov crossover kξ ~ 1?

The dispersion is the corpus's own, quoted at `tex/BCT_Letter64.tex`:

    ω(k) = c_s k √(1 + (kξ)²)
    "In the phonon sector (kξ ≪ 1), ω ∝ k (linear, Markovian-compatible).
     In the particle sector (kξ ≫ 1), ω ∝ k² (quadratic, dispersive)."

The corpus states the crossover criterion itself. Applying it to the corpus's
own interior modes (`gate_C1_step2_modes.py`; the eigenvalue equation
κ cot(κR) = −1/ξ + α₀ = −0.42408 is App J §2.1 verbatim, and its roots
reproduce App J §2.2 exactly):

| mode | App J κ_n | recomputed | κ_n R | **kξ**, k = κ | **kξ**, k = κ/R | character |
|---|---|---|---|---|---|---|
| n=1, A₁ s-wave | 3.3905 | **3.3904626** | 1.6952 | **7.86** | 15.72 | **single-particle** |
| n=2, A₁ | 9.5139 | **9.5138695** | 4.7569 | **22.05** | 44.10 | **single-particle** |
| n=3, A₁ | 15.762 | **15.761762** | 7.8809 | **36.53** | 73.06 | **single-particle** |
| crossover kξ = 1 | — | k = 0.43149 /ℓ_P | — | 1 | 1 | — |
| exterior gapped mode, 2/ξ | 0.8630 m_P c² | **0.86298** | — | — | — | — |

**Every stated interior mode is a single-particle excitation, by the corpus's
own criterion, by a factor of 8 to 37.** Under the reading that makes κ₀ the
dimensionless Bessel argument (App JH, Letter 36), it is worse by a further
factor of 2. There is no reading of the corpus's own numbers on which any
interior mode is collective.

**Does the corpus's description match?** No. It describes them as condensate
modes throughout:

- App J abstract: "The **interior mode spectrum** is computed; the ground state
  mode lies at κ₀ = 3.39"; §2.1 "The **interior condensate modes** are
  solutions of the linearised GP equation inside the sphere."
- App JH §4.1: "the **two-component interior condensate field**"; Result 1:
  "The interior condensate Ψ_int ground state is the OHC".
- KA1 §2: "The OHC **interior condensate** Ψ_int satisfies the
  Gross-Pitaevskii equation … Linearised modes are **spherical Bessel
  resonances**."
- L78: "electron shells are **quantised OHC Bessel resonance modes** with
  capacity 2n²".

App J does notice half of the problem — "The ground state interior mode
(κ₀ = 3.3905) lies above this gap, so it is **in the continuum of the exterior
spectrum — it is a resonance, not an isolated bound state**" — but draws no
consequence from it, and every downstream document (JH, L36, KA1, KA4, L78,
L81, L84, L85) treats the modes as bound, discrete, and collective.

**This finding is independent of the entire ξ₂ question and survives both
branches of §6.** It is, in this session's judgement, the most robust result
the gate produced: it needs only ξ, κ_n and the corpus's own crossover
criterion, all three of which reproduce exactly.

---

## 8. NOTICES — CN-C1

Tiered PROVEN / CONJECTURE / ASSERTED. PROVEN = follows from quoted corpus text
plus arithmetic reproduced in the committed scripts. Revised clause by clause.

| id | tier | notice |
|---|---|---|
| **CN-C1-01** | **PROVEN** | **ξ₂ is not determined by the corpus.** Of the three inputs it requires (g₂, n₂, m₂), two are named by App I §2.3/§6.1 as uncomputed and the third is never named. App J supplies ξ₂ = ξ by assertion of identity, not by computation. **SC-C1-3.** |
| **CN-C1-02** | **PROVEN** | The symbol ξ denotes **at least five numerically distinct objects** in the corpus: 2.31754 ℓ_P, 0.5 ℓ_P, 0.20711 ℓ_P, 2.84911 ℓ_P, 0.8969 fm, 0.01759 fm — a spread of 4.7 × 10¹⁷. Three of them appear under the words "the healing length". Partial trigger of SC-C1-5. |
| **CN-C1-03** | **PROVEN** | **Appendix F uses ξ with three different values in one appendix**: "the tube radius is the healing length ξ ≪ R" (l. 2846/2900), then ξ = a/√(8πα₀) = 4.6 R (l. 3003–3007), then "ξ = r_oct (tight-binding limit)" (l. 3031). The first is contradicted by the second twenty lines later. |
| **CN-C1-04** | **PROVEN** | **ξ = a/√(8πα₀) is asserted, not derived.** Substituting App F's own J = 1/(4πα₀) and App AZ7's own μ = t_kin = t = α₀ into App AZ6's own ξ = ħ/√(2mgn₀) gives **ξ = 38.08 ℓ_P**, 16.4× the value in use. The value in use requires μ = 2.000 m_P c² exactly, which the corpus nowhere states. |
| **CN-C1-05** | **PROVEN** | **App AZ7 contradicts itself.** Its input list (l. 113) reads "Healing length ξ = 2.32 ℓ_P"; its Lemma 1 (t = α₀), Lemma 2 (μ = U = t_kin ≡ ħ²/2mξ²) and Theorem (t/U = t_kin/t_kin = 1, called "an *exact* consequence of the GP self-consistency") together give ξ = a = 1 ℓ_P. |
| **CN-C1-06** | **PROVEN** | **App AZ6 (l. 169) and App AZ7 (l. 113) cite "App E.3" for ξ = 2.32 ℓ_P. App E.3 contains no occurrence of ξ or "healing".** The correct source is App F; App AG (l. 8998) cites it correctly. Two documents carry a mis-citation to a third that does not contain the claim. |
| **CN-C1-07** | **PROVEN** | **App I and App J make incompatible commitments and the second does not announce the retraction.** App I §2.1: "two coupled order parameters", with J₂ tabled as an independent stiffness. App J §1.2: "the same GP action … restricted to r < R … no new field, no new coupling, no new free parameter." |
| **CN-C1-08** | **PROVEN** | **App JH Result 6's interior phase velocity v_ph = κ₀/R_s = 6.78 c is dimensionally invalid** under both of the corpus's own readings of κ₀ (wavenumber, App J §2.2 E_n = ħcκ_n; dimensionless Bessel argument, App JH §4.1 and L36 Eq. spectrum). With App J's ω = cκ, v_ph = c exactly. Propagated to `BCT_VortexTopology_PRL` p. 2 and `BCT_GeometryOfEverything_v4` p. 115 as an established result. |
| **CN-C1-09** | **PROVEN** | **κ₀ carries two incompatible readings a factor of 2 apart.** App J §2.2 makes it a wavenumber (E_n = ħcκ_n, κ₀R = 1.695); App JH §4.1 ("j₀(κ₀ r/R_s)") and Letter 36 Eq. spectrum (ε₀ = ħ²κ₀²/2mR_s²) make it the dimensionless argument, i.e. k = κ₀/R_s = 6.78/ℓ_P. |
| **CN-C1-10** | **PROVEN** | **Every stated interior mode is a single-particle excitation by the corpus's own crossover criterion.** kξ = 7.86, 22.05, 36.53 against the crossover at kξ = 1 (Letter 64's own dispersion). The corpus describes them as "interior condensate modes" and "Bessel resonances" throughout. **Independent of ξ₂; survives both branches.** |
| **CN-C1-11** | **PROVEN** | **App AF1 and Letter 104's "OHC coherence length" ξ_OHC = ℓ_P√(S_D4/2π) = 2.84911 ℓ_P is numerically identical to nine figures to the dimensionless zero-mode Jacobian "J = (S_D4/2π)^(1/2) = 2.84910938" at AppVol1 Part 1 l. 8024.** A dimensionless instanton-measure Jacobian has been read as a length. |
| **CN-C1-12** | **PROVEN** | **App J §3.1 computes g = α₀ × 4πR × tanh²(r_oct/ξ) = 3.6975 × 10⁻⁴, then states "g ≈ α₀ to leading order".** The ratio is 0.0499 — a factor of 20. (This session reached this independently before reading `audit/NEXT.md`; NEXT.md records Gate TANH's SC-TANH-3 as the same finding. See §9.) |
| **CN-C1-13** | **PROVEN** | **App I §3.2 contains an unrendered JavaScript template literal in place of a numerical result:** "\|overlap\|^2 ~ tanh²(r_oct / ξ) = ${Math.pow(Math.tanh(r_oct/xi_BCT),2).toFixed(4)}". The intended value is 0.0079437. A build artefact is sitting in the published appendix text. |
| **CN-C1-14** | **PROVEN** | **The model is in neither limit of §3.** ξ/a = 2.3175. Site-local structure is penalised by (ξ/L)² = 5.4 (scale a), 21.5 (scale R), 61.7 (App J's own ground mode) — suppressed, not forbidden. Recorded as a **prompt defect**: §3's two-limit dichotomy does not contain the corpus's answer. |
| **CN-C1-15** | **PROVEN** | **45 of 134 `.tex` invoke OHC Bessel modes**, i.e. site-local interior structure; **86 of 134 mention OHC at all.** The branch chosen in §6.2 decides the status of that fraction of the corpus. |
| **CN-C1-16** | **PROVEN** | **ξ appears in none of the 92 published sub-1% predictions.** Monograph Appendix A (notation guide) and Appendix B (master table) were read in full; ξ is absent from both, and no table entry sources to the D–L interior appendix sequence. The published prediction set does not move on this gate's verdict. |
| **CN-C1-17** | **CONJECTURE** | **The interior, on the corpus's own description, is not the exterior medium.** "Double-layered plasma sphere", surface charge ±σ, potential step ΔV, "a CONFINED interior (r < R₀) with its own potential landscape" (App I §3.1). If the interior is a confined charged plasma at n₂ ≠ n₀, then ξ₂ = ξ√(n₀/n₂) ≠ ξ. **No interior density is stated**, so this is a conjecture and not a finding. |
| **CN-C1-18** | **CONJECTURE** | **ξ₂ ≪ a is not excluded and is not absurd.** It requires n₂ ≳ 22 n₀. The sphere interiors hold 74.0% of unit-cell volume against the oct void's 4.4% (App I §1.2), so a denser interior is geometrically unremarkable. The gate declines to supply the number. |
| **CN-C1-19** | **ASSERTED** | **"The interior metric differs from the exterior"** (`BCT_GeometryOfEverything_v4` p. 115), offered as the reason 6.78 c is consistent with special relativity. No interior metric is constructed anywhere in the material this gate searched. |
| **CN-C1-20** | **ASSERTED** | **"Causally screened behind the α₀ Josephson shell"** (App JH abstract, Result 6; L36 Result 5). No screening calculation accompanies it in any document searched. |
| **CN-C1-21** | **ASSERTED** | **Letter 19's "vortex healing ratio ξ/r_oct = 11.19" is offered as a falsifiable structural prediction.** The arithmetic is exact, but by CN-C1-04 the ξ it ratios is itself an assertion; the "prediction" restates App F's choice of μ. Tier ASSERTED, not PROVEN, on that ground alone. |
| **CN-C1-22** | **ASSERTED** | **"OHC" names an interior object in its definitions** (App JH, Letter 36, KA1, KA4: "the ground-state field configuration of the BCT **interior** condensate Ψ_int") **and the whole vacuum in its uses** (L60, L64, One Medium: "the OHC vacuum", "the OHC phonon dispersion", "the OHC healing length"). Prediction #121 and App AF1's δH formula each inherit whichever reading the reader supplies. |

### Revision of the "unaffected" list, clause by clause

Per the standing rule, an "unaffected" list is a set of claims needing the same
evidence as any other. The evidence for CN-C1-16 is: Monograph Appendix A §A.1
and §A.2 list every canonical symbol of the programme and ξ is not among them;
Appendix B Table B.9 lists 92 rows with a source appendix per row, and the
source appendices are D2, D4, CJ, CD, AF, EH, HJ3, GR, GW, GX, GB2, GV2, GC2,
BF, FG, BP, CQ, HA2, GC, EE, BY, EJ, HR5, GM2, CM, CR, DV, KS6, KT6, LP6, LV6,
LZ6, LC7, KO6, LO6, LF7, LK7, LG7, LL7, LM7, KZ6, KU6, AL, DU, CO, HI4, HL4,
Q, CE, R, S, X, Y, E1, E2, E3 — **none in the D–L interior sequence (F, G, H,
I, J, K, L) except E3, which contains no ξ (CN-C1-06).** That is the whole of
the evidence, and it is checkable.

---

## 9. CONTAMINATION STATEMENT

**§0.3 — the forbidden note. `audit/notes/note_healing_length.md` was NOT
read.** Its existence and filename became visible in the output of
`git ls-files audit/`, run to inventory the repo before any physics work; the
filename alone is unavoidable from any directory listing. Its contents were not
opened, quoted, or inferred from. No file under `audit/notes/` was read.
`audit/gates/C1/` did not exist before this session created it.

**§0.2 — the Cold Ledger.** The Cold Ledger did not auto-load in this session.
`audit/README.md` and `audit/NEXT.md` **were** read, and this must be declared,
because §6 requires updating NEXT.md and NEXT.md is a gate-summary file. The
unpermitted gate summaries seen there, in full:

- **TANH — "SC-TANH-3: alpha_0 and g are distinct objects, App J §3.1
  conflates them. 0 published predictions moved."**
- **INT — "SC-INT-4: three distinct interior commitments, re-scoped to
  enumeration."** (Already supplied by the C1 prompt itself, §1.)
- **PSI2 — "closed on SC-PSI2-2/4/5; Psi_2 supplies no second A1g Goldstone."**
- **LAM, LAMBDA — "run elsewhere; cross-audited from the PSI2 thread."**
- The queued-gate descriptions for MAD, LINK, PRED, and the parked Gate PV.

No gate deliverable was opened: `gates/PSI2/*`, `gates/crossaudits/*`,
`gates/gate_INT_prompt.md`, `gates/gate_MAD_prompt.md`,
`gates/gate_LINK_prompt.md`, `gates/gate_TANH_prompt.md` were all left unread.
`audit/inventory/inv_claims.csv` was read (inventory, not a gate summary);
INV-0020's finding on KA4 Thm 1 is cited in §6.2 and attributed.

**Ordering, for the TANH overlap.** CN-C1-12 (App J §3.1's g = 3.6975×10⁻⁴ vs
"g ≈ α₀") was computed and printed by `gate_C1_step1_xi.py` **before**
`audit/NEXT.md` was read, and the tool transcript for this session carries that
order. The derivation did not come from TANH's headline. That said, the reader
should weigh it as corroboration of a known finding, not as an independent one.

**No prior finding on the central question reached this session.** The
derivation in §5 was built from App F, App I, App J, App K, App AZ6, App AZ7,
Letter 19 and One Medium App B, in that order, with no intermediary. The
session did not consult `conversation_search` or `recent_chats`; neither tool
was available, and neither was attempted.

**One further deviation to record.** The repo could not be pulled by tarball:
`codeload.github.com` and `api.github.com` both returned 403 for this
repository. `git clone` over HTTPS succeeded. **No tarball SHA-256 is recorded
for this run**, breaking the pattern set by `audit/README.md`. The commit SHA-1
`47d3eefe…` is the anchor instead, and the gate prompt's own SHA-256 inside the
checkout matches the pre-registration, which is a stronger check on the one
file that matters.

---

## 10. SCRIPTS

Committed alongside this deliverable. Deterministic, `mpmath` at 25–30 dps, no
seeds, no imported constants — every number is built from r_oct, r_tet and
quoted corpus statements.

| script | what it establishes |
|---|---|
| `gate_C1_step1_xi.py` | ξ = a/√(8πα₀) = 2.31754379491 ℓ_P; ξ/a, ξ/R, ξ/r_oct; the implied μ = 2; reproduces App I's 4.6351, Letter 19's 11.19, App I/J's tanh values 0.0894 / 0.0079 / 0.54360, and App J's g = 0.00036975 with its 0.0499 ratio to α₀ |
| `gate_C1_step2_modes.py` | solves App J §2.1's eigenvalue equation κ cot(κR) = −0.424083 and recovers κ = 3.3904626, 9.5138695, 15.761762 against App J's printed 3.3905, 9.5139, 15.762; computes kξ under both readings of κ₀; reproduces 2/ξ = 0.86298 |
| `gate_C1_step3_xi_conflicts.py` | the ξ = 38.08 ℓ_P result from the corpus's own J and μ; the ξ = a result from the tight-binding reading; the five-valued ξ table and its 4.7 × 10¹⁷ spread; the AF1 / zero-mode-Jacobian identity; the (ξ/L)² penalty table |

`gate_C1_prompt_asrun.md` is the byte-identical prompt, SHA-256 `c9f27b54…`.

---

## 11. WHAT THIS GATE DID **NOT** ESTABLISH

Stated plainly, because a gate that does not say where it stopped is not a gate.

1. **It did not determine ξ₂.** That is the verdict, not a failure — but it
   means the regime question the prompt set out to settle is *still open*, and
   §6's two columns are both live.
2. **It did not establish that ξ₂ = ξ is wrong.** App J's parsimony argument
   (§5.5) is a real argument. The gate establishes that the corpus does not
   *support* it, not that it is false.
3. **It did not establish that ξ₂ ≪ a is available.** No interior density is
   stated anywhere the gate searched. CN-C1-18 is a conjecture with a number
   attached, not a finding.
4. **It did not derive ξ.** It established that the corpus does not derive it
   either (CN-C1-04), and that the value is reproducible by two routes from one
   assertion. Whether μ = 2 m_P c² is the right choice is untouched.
5. **It did not check the 12 individual Letter PDFs (1–12) in the mount**, nor
   15 other mount documents. 28 of 49 mount files were not retrieved (§1.2).
   A statement of ξ₂ in those files would change §4 and possibly §2.
6. **It did not verify the chemistry claims themselves.** §6.2 says only that
   Branch A removes their precondition and Branch B restores it. The 2n²
   counting, the mode-to-shell mapping and the \|H\| ≤ n theorem each need their
   own audit; INV-0020 has already found the last of them vacuous on separate
   grounds.
7. **It did not price the reformulation.** If Branch B is taken, someone must
   write S[Ψ₂] with an interior density and coupling, and every number in the
   45 OHC-Bessel files inherits them. The gate did not itemise that cost.
8. **It did not resolve whether 6.78 c has a correct version.** It established
   the stated formula is dimensionally invalid (CN-C1-08). Whether some interior
   velocity ≠ c is derivable from a properly formulated S[Ψ₂] is open, and is
   exactly the question Branch B turns on.
9. **It touched no sector outside the interior question.** σ = Λ² (Monograph
   §6.2, App HI5) versus σ = 2πΛ² (App JH4 Step 4) was noticed in passing and
   is **not** a C1 finding; it is recorded here only so it is not lost.

---

## 12. WHAT WOULD SETTLE IT, AND AT WHAT PRICE

Per SC-C1-3's requirement to state the input that would settle the question.

**One number settles it: the interior condensate density n₂, in units of n₀.**
Everything else follows. With n₂ and the corpus's existing g = mc²/n₀ and
ξ = ħ/(√2 mc):

    ξ₂ / ξ = √(n₀ / n₂),   and the regime turns at n₂ / n₀ ≈ 22.

**The price, stated honestly:**

- If n₂ is *derived* — from the double-layer charge σ, the shell thickness d
  and the potential step ΔV, all of which App I §3.1 already names — the cost is
  **zero new free parameters**. This is the cheap path and it is the one App I
  §6.1 already laid out and never walked.
- If n₂ must be *posited*, the cost is **one new free parameter**, and the
  programme is no longer zero-free-parameter. That is not a small price for
  this corpus; it is the price of the name.
- Either way, a second consequence follows immediately and is not optional: by
  §5.4, fixing n₂ fixes c_s,₂. If c_s,₂ ≠ c, **the acoustic-metric derivation of
  the Einstein equations (App E.3, Letter 26, One Medium §8) holds only in the
  exterior**, and the interior — 74% of the volume — is outside it. Whoever
  computes n₂ inherits that question on the same day.

**The gate's recommendation, offered as a judgement and labelled as one:** do
not run Branch B's reformulation before CN-C1-10 is answered. The mode-character
result needs no interior density, survives both branches, and says the interior
"condensate modes" are single-particle states at kξ = 8–37. If that stands, the
Bessel-resonance reading of the interior needs repair regardless of what n₂ turns
out to be, and 45 files wait on it.

---

*Gate C1 run 12 September 2026. Deliverable, scripts and as-run prompt committed
to `audit/gates/C1/` at close, per the standing rule.*
