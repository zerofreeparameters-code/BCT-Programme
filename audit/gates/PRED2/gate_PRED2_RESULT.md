# GATE PRED2 — RESULT

**How surprising are the numbers?**
Run 14 September 2026 · fresh thread · Whopper Protocol (one gate, this thread)

---

## 0. Digest and provenance

| item | value |
|---|---|
| prompt received | `raw.githubusercontent.com/.../BCT-Programme/ec0592f9319ab5a61851018539ab2b6ff2eb72b3/audit/gates/gate_PRED2_prompt.md` |
| fetched | `curl` to disk, hashed **before** reading |
| **SHA-256** | `69b7b7ea242146581cc05cd4e6b08257e2d29794d29b43f8d02e117bd20477c9` |
| bytes | 11 139 |
| independent check | same digest computed on `audit/gates/gate_PRED2_prompt.md` inside a fresh clone at commit `ec0592f9319ab5a61851018539ab2b6ff2eb72b3` |
| repo commit (no tarball — codeload blocked) | `ec0592f9319ab5a61851018539ab2b6ff2eb72b3` |

---

## VERDICT (first, as required)

**SC-PRED-1 — met, but by a formula the programme itself disclaims.**

Exactly one scorable prediction nets ≥ 10 bits after every charge:

> **m_p/m_e = 6π⁵ — +15.6 net bits.**

The corpus states in App. F/G that this expression is **"not a derivable result of the BCT
Chern–Simons calculation… a numerological approximation"** and does not claim it as derived.
It is also reproduced *exactly* by this gate's blind inverse-symbolic control at the same
complexity — the control found `S_D4 / 6^-2` ( = 36 × π⁵/6 = 6π⁵ ) without being told the answer.

**Every prediction the programme does claim to derive nets below 10 bits, and most net below
zero.** α, the electron mass, the Cabibbo angle, the Wolfenstein A, the quark masses, m_ρ and the
Koide phase all score **negative** net bits — the grammar produces them for free, several times
over, once the look-elsewhere count and the post-hoc correction factors are charged.

Three predictions land in the 3–10 bit "suggestive" band, and they share one property: **none of
them carries a post-hoc correction factor.** They are `sin²θ₁₃ = 3α₀` (4.6 bits),
`sin²θ₁₂ = ⅓ − r_tet·r_oct` (4.0 bits), `sin²θ_W(tree) = r_tet²/(r_oct²+r_tet²)` (3.4 bits),
plus `β = arccos(2r_oct)` (6.7 bits).

**Benchmark:** Wyler's 1969/71 α formula scores **≈25 ± 1 bits** under the same grammar — four times
the best BCT score and ten bits above the pre-registered "surprising" line. Wyler's formula has no
accepted derivation and is universally regarded as a coincidence. This is the single most
important number in the report: **BCT's expressions are less surprising than a famous
coincidence, and even that famous coincidence is not physics.**

**Also, and independently of the scoring:** recomputation contradicts the printed values in six
places, including the programme's flagship worked example. See §2. This is close to SC-PRED-5
territory and is reported first among the findings, per §5.

---

## 0.7 — WHAT PASSING THIS BUYS (reproduced verbatim, as required)

> A prediction that scores high after the look-elsewhere charge is evidence that the corpus's
> expression is not a coincidence of its own grammar. It is **not** evidence that the derivation
> printed beside it is correct, that the mechanism is physical, or that the framework is
> unified — a true formula with a false derivation is still a true formula, and this gate cannot
> tell them apart. A prediction that scores low is not thereby false; it is thereby **unsurprising**,
> and the programme should stop citing it as evidence. **Gate PRED cannot deliver physics. At
> most it delivers a ranked list of which numbers are worth defending and which are noise the
> grammar produces for free.** A favourable verdict is a ticket to a harder gate on the one or two
> expressions that survive.

---

## 1. SEARCH-SPACE AUDIT AND PREDICTION CENSUS (before any other number)

### 1.1 Coverage

**Repo** (clone at `ec0592f9`, tarball route blocked at network level, commit SHA-1 recorded in
place of a tarball digest): **134 `.tex` files, 26 of them at the tree root outside `tex/`** —
matches the prompt's stated figures exactly.

**Mount** — every file typed with `file(1)`:

| type | count | handling |
|---|---|---|
| ZIP archives of page images with `.txt` layers | **33** | all extracted; **387 pages**, all `.txt` layers read |
| true PDFs | **14** | 13 text-extracted with `pdftotext -layout`; 1 (`BCT_PeriodicTable_Round_v12_1`) is a 1-page ZIP, counted above |
| raw UTF-8 text files reported by `file` as `data` | **2** | `4_BCT_Appendices_Volume1_..._Part1` (14 467 lines) and `Part2` (13 715 lines) — read directly |
| HTML / Python / images / .tex / .docx | 46 | typed, not corpus-of-record for predictions |

Named targets confirmed present and read: `BCT_CompleteRegistry.pdf`, `BCT_LetterList_v4.pdf`,
One Medium §§10–11 (and App. A, C.2), Monograph v2.1 Table 2 and Table B.9, App. D.2–D.4 and the
AD–AG / AL material inside the Appendices Volume 1 text files.

**Coverage gap, stated plainly:** the mount carries **Appendices Volume 1 only**. Table B.9 cites
appendix IDs up to `LZ6` (the corpus claims 459 appendices); roughly 38 table rows cite an
appendix that is not in the search space, so **no printed closed-form expression exists in the
search space for those rows** and they are not scored. That is a coverage limit of this run, not
a finding about those predictions.

### 1.2 The census

| count | meaning |
|---|---|
| **92** | predictions the corpus claims in Monograph Table B.9 ("92 sub-1%") |
| **280+** | predictions the corpus claims programme-wide (One Medium, p.1) |
| **67** | rows machine-recoverable from Table B.9 as printed (PDF line-breaking mangles δ_CKM and J) |
| **9** | of those are `exact` / `derived` — **unscorable here**, set aside without judgement |
| **1** | is an input (m_π = 139.6 MeV, labelled `input` in the corpus's own table) |
| **57** | numerical rows with a stated error, in principle scorable |
| **~38** | of those cite an appendix outside the search space — no expression available |
| **19** | scored in §3: every prediction for which a **printed closed-form expression** was located and recomputed |

**Unscorable-here (not measured, or not a number):** `θ̄ = 0`, `N_gen = 3`, `Λ_bare = 0`,
`δ_CP = −π/2` (pre-DUNE), `Q_quark = 1/3`, gauge group, Maxwell / Dirac / Einstein equations,
"no QCD axion", `d_n ≈ 10⁻³² e·cm`, `τ_p ~ 10³⁵·⁹ yr`, `r = 0.0046`, 62.9 GeV scalar. The last
six are **out-of-sample** and are listed separately in §5, not scored.

---

## 2. RECOMPUTATION (§1c) — SIX CONTRADICTIONS OF THE PRINTED VALUES

Every value below recomputed at 60 dps (mpmath) from the expression **as printed**, against
CODATA 2022 (`pml.nist.gov/cuu/Constants/Table/allascii.txt`, fetched this session) and PDG 2024 /
current global CKM fits (fetched this session).

**(i) The flagship worked example is arithmetically wrong.**
One Medium Appendix A, Eqs. (14)–(15), works the strange quark through "start to finish, so the
shape of the derivation is visible rather than asserted":

    S_Td · n_s/24 = 15.015 × 12/24 = 7.5075          ✓ reproduces
    m_s = 172 000 × e^−7.5075 MeV = 93.0 MeV          ✗ the arithmetic gives 94.42 MeV

Recomputed: **94.4197 MeV**, not 93.0 MeV. Against PDG m_s = 93.5 MeV the true error is
**+0.98 %**, not the printed **−0.43 %**. The printed number is off by 1.5 %, and the printed
error has the wrong sign. This is the one derivation the corpus chose to display in full.

**(ii) The Koide NLO formula does not give the Koide NLO value.**
Phase 35A prints `δ(NLO) = δ(LO) + r_oct²/(r_tet·π²)` and states the correction equals
`0.04050025`. Recomputed, `r_oct²/(r_tet·π²) = 0.03867489`. The printed **value** is produced by
Phase 36A's `r_oct²/(3·r_tet·π) = 0.04050025`. The two forms are printed as the same quantity in
two appendices; only one matches. Using the printed 35A formula, m_μ comes out at 95.56 MeV
(−9.6 %), not the printed 105.5719 MeV (−0.082 %).

**(iii) The ρ-meson theorem silently switches pion.**
`m_ρ = m_π/(2√α₀)·(1−3α₀/2)` is printed with `m_π = 139.6 MeV` listed as the corpus's own input
(Table B.9). With m_π± = 139.57039 the expression gives **801.79 MeV** (+3.4 %). The printed value
775.5 MeV is recovered only with **m_π0 = 134.9768** (→ 775.397). The expression as printed with
the input as tabled does not reproduce the result as printed.

**(iv) The proton-radius theorem is off by a factor of 3.27.**
`r_p = ℏc/(m_ρc²)·(1+α₀)` with the corpus's own m_ρ = 775.5 MeV gives **0.2563 fm**. The printed
value is 0.8386 fm — a factor 3.2715 adrift. Unscorable as printed.

**(v) `1/α = 2π/x_lep` is off by a factor of 4.86.**
Printed in the Appendices Vol. 1 summary tables (five separate occurrences) as `1/α = 2π/x_lep
(App E) = 137.046, +0.007 %`. Recomputed: `2π/x_lep = 666.140`. No reading of the printed
expression gives 137.046. This is a *second, incompatible* printed final form for α.

**(vi) The Planck mass is circular.**
Monograph §19.1: `m_P = M_R/α₀² = 6.695×10¹⁴/(0.0074081)² = 1.220×10¹⁹ GeV (−0.08 %)`.
Appendix GG2 (Phase 45A), and Part 3 p.113/134/367/423/474: `M_R(BCT) = m_P·α₀² = 1.22×10²⁸ eV ×
(0.00740806)² = 6.695×10¹⁴ GeV`. **M_R is defined as m_P·α₀² and m_P is then "derived" as
M_R/α₀².** The −0.08 % is the round-trip rounding error of the observed Planck mass, nothing
else: feeding the measured m_P = 1.220890×10¹⁹ GeV in gives M_R = 6.7002×10¹⁴, and feeding the
rounded 6.695×10¹⁴ back out gives 1.21995×10¹⁹. G = ℏc/m_P² inherits the circularity, so the
Gravity sector of Table B.9 (two rows) contains **zero independent content**. Not scored.

**Targets with more than one printed final form** (listed twice per §1, as required):
α (three: `α₀(1−2α₀)`, `α₀(1−3α₀)/(1−α₀)`, `2π/x_lep`); m_e (four: `e^−π⁵/⁶`,
`e^−S/(1−x_lep)`, `e^−(π⁵+π)/6`, `e^−S/(1−α₀(4π+1)/π²)` — plus a fifth value, 0.5123 MeV, in
Table B.9 via Koide); m_b (three); the Koide NLO phase (two); the CKM phase (two: `arccos(1/3) =
70.53°` and `arccos(2r_oct) = 65.53°`).

**Stated errors that do not survive a current measured value:** η̄ = 3r_tet is printed at
−0.603 % against η̄ = 0.3392. Current global fits give η̄ = 0.3523–0.3548; the recomputed error is
**−4.3 %**. δ_CKM = arccos(1/3) = 70.53° is printed against "69.4°"; against the current
γ = 65.75 ± 1.07° it is **+7.3 %, roughly 4.5σ away** — this prediction is, on present data,
already falsified in the form Table B.9 and One Medium §11 print it.

Full recomputation table: `pred2_step1_census.py` output, reproduced in `census_table.txt`.

---

## 3. THE GRAMMAR (§2) — written, run and committed **before** any score

Source: `pred2_step2_grammar.py`. It was executed and its N(C) table printed *before*
`pred2_step3_score.py` was written. The scorer imports the grammar module; it cannot change it.

**Atoms (20)** — every one taken from the census, none added that the corpus does not use:
`{1, 2, 3, 4, 6, 8, 12, 24, 48, π, √2, √3, √6, e, α₀, r_tet, r_oct, R = ½, S_D4 = π⁵/6,
x_lep = 4α₀/π}`. `N_gen = 3` is not listed separately (identical to the atom 3).
α₀, S_D4 and x_lep are treated as **atoms** because the corpus uses them as building blocks. This
is the corpus-favourable choice: forcing them to be spelled out would raise every C_expr, enlarge
the accessible space, and **lower** every score.

**Operations (22)** — `√, x^n for |n| ≤ 5, exp, ln, 1/(1−x)` per the prompt, plus `cos, tan,
arccos, arctan` which the census shows in use (Koide phase, Wolfenstein β, ρ̄).
Binary: `+, −, ×, ÷`.

**Complexity measure:** node count of the expression tree. Atom = 1; each unary op adds 1; each
binary op adds 1.

**Enumeration** — exhaustive with value-dedup to C = 5; uniform sampling weighted by the exact
structural counts N(C) beyond:

| C | N(C) = expressions of complexity exactly C | distinct real values (12 s.f.) |
|---:|---:|---:|
| 1 | 20 | 20 |
| 2 | 340 | 279 |
| 3 | 7 380 | 3 782 |
| 4 | 179 860 | 68 000 |
| 5 | 4 700 820 | 1 229 750 |
| 6 | 128 765 140 | sampled |
| 7 | 3 648 215 380 | sampled |
| 8 | 106 027 248 660 | sampled |
| 9 | 3 143 353 760 020 | sampled |
| 10 | 94 690 729 286 740 | sampled |
| 11 | 2 890 132 171 200 980 | sampled |
| 12 | 89 184 292 693 728 660 | sampled |
| 13 | 2 777 775 676 086 729 620 | sampled |

(computed to C = 20; the corpus's deepest scored expression is C = 19.)

**Density.** For each target T and complexity C, the local density of grammar values per unit
`ln x` near T is measured from the enumeration (C ≤ 5) or from a 700 000-expression uniform sample
(C ≥ 6), using the narrowest log-window that contains ≥ 60 hits. Then
`P(|x−T|/T ≤ ε) = ρ(T)·2ε`. Sampling error on ρ with ≥ 60 hits is ≤ 13 % (1σ), i.e. **≤ 0.2 bits**
— negligible against the charges below. Windows and hit counts are printed per target in
`scores_raw.txt`.

**Pre-registered thresholds (from the prompt, fixed before §4 and not moved):**
**≥ 10 bits = surprising · 3–10 bits = suggestive · < 3 bits = unsurprising.**

---

## 4. THE SCORES (§3)

**Look-elsewhere over targets:** −log₂(92) = **6.52 bits**, charged to every prediction. (The
corpus's own claim of 280+ predictions would make this 8.13; 92 is used as the conservative floor.)

**Per-target reported-search charge:** App. D.2 §3 reports four dynamical approaches plus an
"exhaustive systematic search over all two-quantity products of BCT geometric invariants"
`{R, r_tet, r_oct, r_s, φ, η, τ}` — 21 products + 42 ratios + 4 approaches ≈ 67 candidates →
**6.07 bits** charged to α. Where the corpus prints k incompatible final forms for a target, k is
charged as a documented floor on candidates tried. Where no search is documented, 0 is charged —
**these are floors, not estimates.**

**Correction-factor / date-order charge:** each post-hoc factor is charged
`log₂(number of distinct grammar values, at the factor's own complexity, lying inside the
residual window the factor had to close)` — because any of those was available to be tried, and
the record shows the factor was introduced *after* the residual was recorded. App. D.2 §5.3 is
explicit about the ordering: it records the required correction f = 0.98506, offers a numerical
observation, says **"This conjecture has no derivation… Presenting it as a derivation would be
dishonest. It is recorded here as a target for Appendix D.3"** — and D.3 then supplies the factor.
Every correction factor in the census is post-hoc by this test; none was printed before the
discrepancy it closes.

### Charge sheets

| prediction | C | ε | raw bits | LE | search | corr. | **net** | bin |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| **m_p/m_e = 6π⁵** | 4 | 1.9e−5 | 22.09 | 6.52 | 0 | 0 | **+15.56** | **SURPRISING** |
| β = arccos(2r_oct) | 4 | 3.4e−3 | 13.22 | 6.52 | 0 | 0 | **+6.70** | suggestive |
| sin²θ₁₃ = 3α₀ | 3 | 8.8e−3 | 11.13 | 6.52 | 0 | 0 | **+4.61** | suggestive |
| sin²θ₁₂ = ⅓ − r_tet r_oct | 6 | 1.0e−2 | 10.54 | 6.52 | 0 | 0 | **+4.02** | suggestive |
| sin²θ_W (tree) | 8 | 1.6e−2 | 9.91 | 6.52 | 0 | 0 | **+3.38** | suggestive |
| m_s/m_t (T_d orbit n=12) | 12 | 9.8e−2 | 9.49 | 6.52 | 0 | 0 | **+2.96** | unsurprising |
| δ_CKM = arccos(⅓) | 3 | 7.3e−2 | 7.83 | 6.52 | 0 | 0 | **+1.31** | unsurprising |
| η̄ = 3 r_tet | 3 | 5.0e−2 | 7.30 | 6.52 | 0 | 0 | **+0.77** | unsurprising |
| **α = α₀(1−2α₀)** | 7 | 1.3e−4 | 18.23 | 6.52 | 6.07 | 7.41 | **−1.77** | unsurprising |
| m_e/m_P = e^−(π⁵+π)/6 | 8 | 9.6e−4 | 19.96 | 6.52 | 2.00 | 14.13 | **−2.70** | unsurprising |
| Koide phase δ (LO+NLO) | 19 | 2.0e−5 | 18.88 | 6.52 | 1.00 | 15.01 | **−3.66** | unsurprising |
| α = α₀(1−3α₀)/(1−α₀) | 11 | 1.7e−5 | 20.93 | 6.52 | 6.07 | 13.92 | **−5.57** | unsurprising |
| m_ρ/m_π0 | 12 | 3.4e−4 | 15.26 | 6.52 | 0 | 15.00 | **−6.26** | unsurprising |
| λ = 2r_tet(1+3α₀/8) | 11 | 1.6e−3 | 13.50 | 6.52 | 0 | 14.06 | **−7.09** | unsurprising |
| m_u/m_t (n = 18+δn_u) | 18 | 8.3e−3 | 13.52 | 6.52 | 0 | 15.89 | **−8.89** | unsurprising |
| A = (1+r_oct)⁻¹(1−α₀/2) | 10 | 6.5e−3 | 10.24 | 6.52 | 0 | 13.88 | **−10.17** | unsurprising |
| m_d/m_t (n = 17−δn_d) | 17 | 1.9e−2 | 12.33 | 6.52 | 0 | 16.32 | **−10.52** | unsurprising |
| m_b/m_t = πα₀(1+5α₀) | 9 | 7.6e−3 | 12.21 | 6.52 | 1.58 | 14.86 | **−10.76** | unsurprising |
| m_e/m_P = e^−S/(1−α₀(4π+1)/π²) | 15 | 1.4e−4 | 22.48 | 6.52 | 2.00 | 31.08 | **−17.12** | unsurprising |

Correction-factor candidate counts (the `corr.` column) are printed in full in
`charges_detail.txt`. Two examples: α's factor `(1−2α₀)` had to land within ±1.52 % of 0.98506 —
**170 distinct grammar values of complexity ≤ 3 sit in that window**. The One Medium C.2
electron-mass dressing `α₀(4π+1)/π²` had to land within ±3.97 % of 1.0000027 —
**126 661 distinct grammar values of complexity ≤ 10 sit in that window.**

The shape of the table is the result: **the tighter a BCT prediction's ε, the more post-hoc
correction it carries, and the more negative its net bits.** The four best-scoring predictions are
the four with no correction factor at all, and all four are 1–5 % matches, not sub-0.1 % ones.

### Benchmark — Wyler

`α = (9/8π⁴)(π⁵/2⁴·5!)^¼ = 1/137.036082`, ε = 6.1×10⁻⁷, C = 20 in this grammar
(9 = 3², 5! = 24·(4+1)). **Raw ≈25 ± 1 bits; the same net** (Wyler targeted one number, so no
look-elsewhere charge is honest; charging BCT's 92-target LE anyway still leaves ≈18).
Two runs at different sample sizes bracket it: 25.64 bits at 900 000 samples, 24.48 bits at
350 000 samples (the committed `wyler.txt`). At C = 20 the log-window needed for ≥60 hits is wide
and the sampling error on ρ is ≈1 bit — larger than for any target in §4, and stated here rather
than hidden behind a two-decimal figure. Wyler beats every BCT expression by ten bits or more,
and Wyler's formula is a coincidence.

### Inverse-symbolic control (§3, last bullet)

1 500 000 random grammar expressions per target at complexity ≤ C_corpus, blind to the corpus
answer (`pred2_step5_control.py`):

| target | corpus ε | best control ε | control expression | control beats corpus? |
|---|---:|---:|---|---|
| α | 1.29e−4 | **3.70e−5** | `12·α₀/e^{5/2}` | **yes, 3.5× closer** |
| sin²θ_W | 1.64e−2 | **3.89e−5** | `√2⁻³/arctan(24−x_lep)` | **yes, 420× closer** |
| sin²θ₁₂ | 9.97e−3 | **1.70e−5** | `r_oct^{3/4}` | **yes, 590× closer** |
| λ_Wolfenstein | 1.60e−3 | **1.58e−5** | `√2 − √(√2)` | **yes, 100× closer** |
| m_ρ/m_π0 | 3.40e−4 | **4.17e−5** | `(3+r_oct)^{3/2}` | **yes, 8× closer** |
| β (deg) | 3.40e−3 | **7.69e−5** | `e²/r_tet` | **yes, 44× closer** |
| η̄ | 4.97e−2 | **6.67e−4** | `e^{−5r_oct}` | **yes, 75× closer** |
| sin²θ₁₃ | 8.81e−3 | 8.81e−3 | `3α₀` | ties (control **rediscovers** the corpus expression) |
| m_p/m_e | 1.88e−5 | 1.88e−5 | `S_D4/6⁻²` = 6π⁵ | ties (control **rediscovers** 6π⁵) |
| m_e/m_P | 9.61e−4 | 2.96e−3 | `exp(tan(exp(cos r_oct)) − S_D4)` | no |

**Eight of ten targets are matched more closely by a blind random draw from the corpus's own
grammar than by the corpus's published expression**, at equal or lower complexity. On the two it
does not beat, it independently finds the corpus's own formula. This is the ways-of-working
lesson — "113 simple expressions land within 1 % of 137.036" — reproduced quantitatively and
extended: at the corpus's own complexity, the grammar does better than the corpus almost
everywhere.

---

## 5. THE OBSTRUCTION CHECK (§4) — out-of-sample predictions

**Pre-registration search across the full search space (387 ZIP pages + 13 PDFs + 2 text
volumes): no numerical prediction is pre-registered anywhere before the relevant measurement.**
The only occurrences of "pre-registered" in the corpus are a psychology-trial aside in
*Accidentally Solved* and a grant-application note in the CSSC Design Bible. **Every prediction
scored in §4 is a retrodiction.**

Genuine out-of-sample predictions — **not scored by §4 at all**, listed with falsification dates:

| prediction | printed value | test | date |
|---|---|---|---|
| neutron EDM | d_n ≈ 10⁻³² e·cm; falsified if \|d_n\| > 3×10⁻³¹ | n2EDM (PSI) | ~2028 |
| no QCD axion (anti-prediction) | discovery falsifies | ADMX / IAXO | ongoing |
| tensor-to-scalar ratio | r = 8/S_D4² = 0.0046 | LiteBIRD, CMB-S4 | 2028–2033 |
| dark-matter scalar | 62.9 GeV, D4 Z₂-stable | LZ / XENONnT | 2025–2030 |
| leptonic CP phase | δ_CP = −π/2 exact | Hyper-K, DUNE | 2027+ |
| proton lifetime | τ_p ~ 10³⁵·⁹ yr | Hyper-K | 2027–2045 |
| c_GW = c exactly | any confirmed deviation falsifies | LVK O5+ | ongoing |

**These seven are the programme's only real evidential currency.** Note also that the CKM phase
in the form `δ_CKM = arccos(1/3) = 70.53°`, which One Medium §11 offers as a live test at degree
precision, is **already ~4.5σ from the current γ = 65.75 ± 1.07°** — it should move to the
falsified column or be withdrawn in favour of the `arccos(2r_oct)` form, which cannot be counted
twice.

---

## 6. CN-PRED NOTICES

**PROVEN** (terminal-verified arithmetic, this session, 60 dps):

- **CN-PRED-01.** One Medium App. A Eq. (15) is arithmetically wrong: `172 000 × e^−7.5075 =
  94.42 MeV`, not 93.0 MeV. The printed error (−0.43 %) has the wrong sign and the wrong
  magnitude; the true error vs PDG is +0.98 %.
- **CN-PRED-02.** The Planck-mass prediction is circular: `M_R ≡ m_P·α₀²` (App. GG2) and
  `m_P ≡ M_R/α₀²` (Monograph §19.1). The Gravity sector of Table B.9 (m_P, G_N) has no
  independent content. *Note: a file summary I could not avoid seeing (see §8) used the phrase
  "Planck-mass-circularity", so I cannot claim this finding is uncontaminated by priming — but it
  is derived here from primary text only, and the arithmetic is shown.*
- **CN-PRED-03.** `1/α = 2π/x_lep` recomputes to 666.14, not the printed 137.046. Five printed
  occurrences.
- **CN-PRED-04.** `r_p = ℏc/(m_ρc²)(1+α₀)` recomputes to 0.2563 fm, not the printed 0.8386 fm
  (factor 3.2715).
- **CN-PRED-05.** Phase 35A's printed NLO Koide correction `r_oct²/(r_tet π²)` = 0.038675 does not
  equal its own printed value 0.04050025; Phase 36A's `r_oct²/(3r_tet π)` does.
- **CN-PRED-06.** `m_ρ = m_π/(2√α₀)(1−3α₀/2)` reproduces 775.5 MeV only with m_π0 = 134.977, while
  the corpus tables m_π = 139.6 MeV as its input.
- **CN-PRED-07.** Wyler's α formula scores ≈25 ± 1 bits under the BCT grammar; no BCT expression
  exceeds 15.6, and no *derived* BCT expression exceeds 6.7.
- **CN-PRED-08.** A blind inverse-symbolic control inside the corpus's own grammar beats the
  published expression on 8 of 10 targets at equal or lower complexity.

**CONJECTURE** (model-dependent on the grammar and the charge schedule):

- **CN-PRED-09.** No prediction the programme claims to derive nets ≥ 10 bits. The maximum over
  derived predictions is 6.70 (β = arccos 2r_oct).
- **CN-PRED-10.** Net bits correlate *negatively* with printed precision across the census: the
  sub-0.1 % results are the ones carrying the most post-hoc correction.
- **CN-PRED-11.** The four best-scoring predictions are exactly the four with no correction
  factor, and all are 1–5 % matches.

**ASSERTED** (recorded, not established here):

- **CN-PRED-12.** η̄ = 3r_tet at −0.603 % rests on an outdated η̄ = 0.3392; against current global
  fits the error is −4.3 %.
- **CN-PRED-13.** `δ_CKM = arccos(1/3) = 70.53°` is ~4.5σ from the current γ and should be
  retired or reclassified.

---

## 7. WHAT SHOULD STOP BEING CITED (per SC-PRED-2's instruction, applied to the sub-3-bit set)

One Medium §10 "One table" and §13 Conclusion — the sentences claiming "α to 0.013 %, G to
0.151 %, and ninety further observables at sub-percent precision from two void radii and one
scale" — should not be cited as evidence. Specifically:

- **α = α₀(1−2α₀)** (−1.8 bits) and **α = α₀(1−3α₀)/(1−α₀)** (−5.6 bits): the grammar produces
  matches this good for free, and the blind control does better.
- **G and m_P** (Monograph §19.1–19.2, One Medium §10 Gravity row): circular, zero content.
- **The Wolfenstein set** λ (−7.1), A (−10.2), ρ̄, and the quark masses m_d (−10.5), m_u (−8.9),
  m_b (−10.8): each is a fitted correction to a grammar near-miss.
- **m_ρ and r_p** (Letters 11/12, Monograph §16): the ρ mass is −6.3 bits and switches pion; the
  proton radius does not recompute at all.
- **The electron mass** at −0.014 % (One Medium App. C.2, the headline of the July 2026 edition):
  **−17.1 bits — the single least surprising claim in the census**, because the dressing factor
  had 126 661 grammar candidates available in the window it closed.

What may still be cited, with the bit-count attached and no claim of derivation:
`sin²θ₁₃ = 3α₀`, `sin²θ₁₂ = ⅓ − r_tet r_oct`, `sin²θ_W(tree)`, `β = arccos(2r_oct)`, and
— with the corpus's own disclaimer intact — `m_p/m_e = 6π⁵`.

**Recommended next gate:** a derivation audit of `m_p/m_e = 6π⁵` is *not* recommended, because
the corpus already classifies it as underived and the control shows it is the grammar's own
optimum at C = 4. The defensible ticket is a derivation audit of the **three uncorrected mixing
predictions** (`3α₀`, `⅓ − r_tet r_oct`, tree-level `sin²θ_W`), which score positively for the
right reason: nothing was added to them after the fact.

---

## 8. CONTAMINATION STATEMENT

- I did **not** read the 9–13 Sep 2026 threads, BCT-X / Sandbox TOP, `audit/notes/`, or any
  concurrent gate. The files `gate_RANK_RESULT`, `gate_MP_RESULT`, `gate_PRED_RESULT`,
  `gate_PRED_prompt_asrun`, `claude_Gate_C1_Result`, `claude_Gate_Session_Prompts`, `NEXT.md` and
  `NEXT_patch.md` are present in the mount and in the repo; **none was opened.** I did not open
  `notes/note_identities.md` either — the §0.2 permission to read its scoring definitions was not
  exercised, so the bits here are on this gate's own definition and are **not** guaranteed
  commensurable with Gate STAT's 3.3 bits. That is a deliberate choice: reading it after §3 was
  written would have added a commensurability footnote at the cost of a quarantine risk, and the
  verdict does not turn on it.
- **The Cold Ledger auto-loads and cannot be partially read. I declare it.** What I saw was a file
  listing with one-line descriptions. The unpermitted summaries visible to me were:
  `audit-findings.md` — "Cold Ledger audit results — closed sectors by proof, what survives,
  active correction ledger, and open problems in priority order"; `gate-mad.md` — "run and closed
  14 Sep 2026, verdict SC-MAD-1"; `gates-rank-mp-pred.md` — "Gates RANK, MP and PRED — run and
  closed 13 Sep 2026; the field-content, **Planck-mass-circularity** and prediction-scoring
  verdicts". **The bodies of those three files were not opened.** The phrase
  "Planck-mass-circularity" is a prior verdict I should not have seen; CN-PRED-02 is flagged
  accordingly. I also read `ways-of-working.md` in full, for the toolchain and delivery protocol
  (PDF standards, git constraints, mpmath conventions) — it contains no gate verdicts, but it
  contains the general lesson "113 simple expressions land within 1 % of 137.036", which is
  thematically adjacent to this gate's method. Declared.
- **Nothing numerical was inherited.** Every predicted value was recomputed from the printed
  expression; every measured value was fetched this session (CODATA 2022 complete listing; PDG
  2024 / UTfit / global CKM fits; NuFIT for the PMNS angles) and is cited in the scripts.

---

## 9. EXTERNAL LITERATURE, EACH ACTUALLY READ

- **CODATA 2022 complete listing**, `pml.nist.gov/cuu/Constants/Table/allascii.txt`, fetched
  14 Sep 2026 — α⁻¹ = 137.035999177(21), m_e = 0.51099895069(16) MeV, m_P = 1.220890(14)×10¹⁹ GeV,
  m_p/m_e = 1836.152673426(32), G = 6.67430(15)×10⁻¹¹, r_p = 0.84075(64) fm, on-shell weak mixing
  angle 0.22305(23).
- **Wyler's α formula and its status**: taken as the benchmark near-miss per §0.6; the value
  1/137.036082 is recomputed here from the published closed form, not quoted.
- **Global CKM fits** (UTfit 2022 quoted in arXiv:2401.08006; the fit quoted in arXiv:2504.05209):
  λ ≈ 0.2250, A ≈ 0.820–0.828, ρ̄ ≈ 0.1598–0.161, η̄ ≈ 0.347–0.355, γ = 65.75 ± 1.07°. Used only
  for the measured column.
- **Look-elsewhere effect / trials factor** and **minimum-description-length** arguments are used
  in their standard form; no source is cited that was not read, and no citation is used to support
  a claim it does not make.

---

## 10. WHAT THIS GATE DID **NOT** ESTABLISH

- It did not show any BCT prediction is **false**. Low bits mean unsurprising, not wrong.
- It did not show `m_p/m_e = 6π⁵` is **true physics**. It is one formula that survives one
  grammar's charge sheet, and the corpus itself calls it numerological.
- It did not audit a single **derivation**. A true formula with a false derivation scores
  identically here.
- It did not score ~38 of the 92 claimed predictions, because their appendices are outside the
  search space. A later run with Appendices Vols. 2+ mounted could change the census, though the
  charge schedule (6.52 bits of look-elsewhere alone) would apply unchanged.
- It did not establish that the grammar is the **right** grammar. A different atom set moves every
  raw-bits number. What is robust across any reasonable choice is the *ordering* and the
  *correction-factor arithmetic*: 126 661 candidates in the electron-mass window is not a
  grammar-specific artefact.
- **SC-PRED-4 was checked and did not fire**, but narrowly: the corpus's correction factors are
  bounded in practice (C ≤ 10 for every one located), so C_max exists. Had the C.2 electron-mass
  dressing been one level deeper, the grammar would have been effectively unbounded for that
  target.
- **Prompt defect, recorded rather than force-fitted:** SC-PRED-1 does not anticipate the case
  that fired — the single ≥10-bit prediction is one the corpus explicitly disclaims and that a
  blind control reproduces. "At least one scorable prediction nets ≥ 10 bits → favourable
  outcome" reads, on this run, as a favourable verdict for a result nobody claims. Future PRED-
  class prompts should distinguish *claimed-as-derived* from *published-with-disclaimer* in the
  census, and should require the control's result to be reported in the same breath as the score.

---

*Scripts: `pred2_step1_census.py`, `pred2_step2_grammar.py`, `pred2_step3_score.py`,
`pred2_step4_charges.py`, `pred2_step5_control.py`, `pred2_step6_wyler.py`.
Outputs: `census_table.txt`, `grammar_counts.txt`, `scores_raw.txt`, `charges_detail.txt`,
`control.txt`, `wyler.txt`. As-run prompt: `gate_PRED2_prompt_asrun.md` (byte-identical to the
pre-registered file; digest above).*
