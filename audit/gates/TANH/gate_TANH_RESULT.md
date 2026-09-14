# GATE TANH — RESULT

**Which Josephson coupling does the corpus have?**

- **Model:** Claude Opus 4.8 (selected model this session). *Note: the execution thread's first
  line was answered "Fable 5.1" in error and corrected to Opus 4.8 before any corpus was read; the
  MODEL field of record is **Opus 4.8**.*
- **Gate prompt digest (SHA-256, from the file the session received):**
  `6ec126a68ac6efba6a76bff16605e2edac0eae802a3062113c6f865c50c22297` (7476 bytes) —
  **matches pre-registration.**
- **Pinned corpus:** tarball of `zerofreeparameters-code/BCT-Programme@cde0350`,
  SHA-256 `9a382e05878a562bda5f1802082afa726b2bdc440bf38c04c2e8061fd578cc4f` (45,685,391 bytes).
- Date executed: 14 September 2026.

---

## SEARCH-SPACE COVERAGE (reported before any other number, per §0.5)

- **`.tex` files:** 134 total — **26 at tree root**, 108 under `tex/`. A `tex/*.tex` glob would
  cover only the 108 and miss the 26 root files. Full corpus was searched with
  `find . -name '*.tex'` (all 134).
- **Appendix PDFs, typed with `file` (trusted over §0.5's mount description, per the execution
  thread):**
  - `BCT_Appendices_Volume1_2026_compressed_Part1.pdf` — genuine PDF, 425 pp.
  - `..._Part2.pdf` — genuine PDF, 425 pp.
  - `..._Part3.pdf` — genuine PDF, 25 pp.
  - `BCT_Appendices_Volume2_2026_compressed.zip` — real ZIP → one 582-pp. genuine PDF.
  All read with `pymupdf`. Vol1/Vol2 text layers extract cleanly; Josephson content located by
  full scan of all 875 + 582 pages, not by page guess.
- **Other PDFs** (`BCT_NPB_Paper_v1`, five `BCT_SMOKE_*`): genuine PDFs, scanned.
- **Appendix J proper** identified at **Part1 page-index 112** (title "APPENDIX J — THE SPHERE
  INTERIOR ACTION S[Ψ₂]"). The four `tex/BCT_Appendix_JH*.tex` files are the *Hopf* appendix
  ("JH"), a different document that *cites* Appendix J; they were not mistaken for it.

---

## VERDICT — SC-TANH-3 (with a local SC-TANH-1 reading), numeric-prediction tally **ZERO**

**Both numbers are correct, for two different physical objects, and the corpus conflates them
under one name ("the Josephson coupling"):**

- The number App J §3.1 **prints from its own factors**, `g = 0.00036975`, is the correct value of
  the object §3.1 sets out to compute: the **interior↔oct-void, overlap-weighted Josephson
  coupling** `g = H_int/(J/R)`. This is the BCT Josephson coupling *as §3.1 defines it*.
- The number App J §3.1 **boxes**, `g ≈ α₀ = 0.00740806`, is the correct value of a **different**
  object — the **surface-potential / boundary coupling** `σ_s/J = α₀ = r_oct·r_tet/π`, established
  in §1.3 and derived independently in Appendix D as the fine-structure candidate.
- The two differ by the factor `4πR·tanh²(r_oct/ξ) = 0.049912`, i.e. **α₀/g = 20.0353**.

**Within §3.1's own local frame** — where "g" is explicitly the overlap coupling `H_int/(J/R)` —
the boxed line is simply an **error** (SC-TANH-1): the "to leading order" justification requires
the discarded factor to be ≈1, and it is ≈1/20. The reading that rescues it to SC-TANH-3 is that
the boxed value `α₀` is not fabricated: it is the correct value of the boundary coupling `σ_s/J`,
which is the object the *rest of the corpus* actually uses. The single act of conflation is the
§3.1 box relabelling the overlap coupling as `α₀`.

**Downstream numeric predictions affected: ZERO.** The printed value `0.00036975` occurs **nowhere
in the 134 `.tex` files**; it appears only inside App J itself. Every downstream numeric use of
"the Josephson coupling" uses `α₀ = r_oct·r_tet/π = 0.0074081` — i.e. the boundary/surface coupling
`σ_s/J` (= the fine-structure constant), which is correctly derived independently. Correcting the
§3.1 box changes **no** published prediction, because the boundary coupling keeps its value `α₀`
and nothing published is a coefficient-of-`g` formula. **Structural claims are affected** (the
"Josephson coupling equals the EM coupling exactly / same geometric origin" family). See §5.

SC-TANH-4 (ill-formed) and SC-TANH-5 (non-reproduction) are **ruled out**: every printed factor
reproduces at 40 dps, and the expression is determinate under the corpus's uniform lengths-in-`l_P`
convention.

---

## STEP 0 — REPRODUCTION OF APP J §3.1, EVERY PRINTED FACTOR

**Full expression, quoted from §3.1 (Part1 p.115):**

> H_int = σ_s × ∫_{r=R} |Ψ|² dS = σ_s × 4πR² × |Ψ(R)|²
> g = H_int / (J/R) = σ_s × 4πR² / (J × R) × |Ψ(R)|²/Ψ₀²
> Substituting σ_s = α₀ J and |Ψ(R)|/Ψ₀ = tanh(r_oct/ξ):
> g = α₀ × 4πR²/R × tanh²(r_oct/ξ)
>   = α₀ × 4πR × tanh²(0.0894)
>   = 0.00740806 × 6.2832 × 0.007944
>   = 0.00036975

**Inputs derived independently (not read from §3.1's own printouts):**
- `r_oct = (√2−1)/2` and `r_tet = (√6−2)/4` (App C p.24, App D.2 p.27); `R = a/2` (App D.2 p.27).
- `α₀ = r_tet·r_oct/(4πR²)` (App D). With `R = 1/2`, `4πR² = π`, so `α₀ = r_oct·r_tet/π`.
- **ξ derived as the BCT healing length** `ξ = a/√(8πα₀)` (stated at App-I/J region, Part1 p.81:
  "the healing length ξ = a/√(8πα₀)"). This is the ξ that makes §3.1's printed `tanh²(0.0894)`
  come out right; the two other ξ conventions the corpus uses (see Step-2) do not.

**40-dps reproduction (`scripts/repro_step0.py`):**

| quantity | independent value (40 dps head) | App J printed | match |
|---|---|---|---|
| r_oct | 0.2071067811865475244 | 0.207107 | ✔ |
| r_tet | 0.11237243569579452455 | 0.112372 | ✔ |
| R | 0.5 | 0.500000 | ✔ |
| α₀ = r_tet·r_oct/(4πR²) | 0.0074080557275479081 | 0.00740806 | ✔ |
| ξ = a/√(8πα₀) | 2.317543794911665 | (ξ/r_oct=11.1901 p.96; 2/ξ=0.8630 p.114) | ✔ |
| 4πR | 6.28318530718 | 6.2832 | ✔ |
| r_oct/ξ | 0.0893647756 | 0.0894 | ✔ |
| tanh²(r_oct/ξ) | 0.00794373660 | 0.007944 | ✔ |
| **g (computed)** | **0.000369750648** | **0.00036975** | ✔ |
| **g (boxed) = α₀** | **0.00740805573** | **0.00740806** | ✔ |

**The sentence and boxed statement that follow (Part1 p.115), verbatim:**

> g ≈ α₀  (to leading order)
>
> ✔  The dimensionless Josephson coupling between the sphere interior and the oct void electron
> vortex is g = α₀ to leading order. This follows from the same geometric ratio
> r_tet × r_oct / (4πR²) that defines the fine structure constant (Appendix D). The coupling and
> the electromagnetic coupling have the same geometric origin.

**Ratio between the computed and boxed values:** `α₀ / g = 20.0353` (equivalently, the discarded
factor `4πR·tanh²(r_oct/ξ) = 0.049912 = 1/20.0353`).

---

## STEP 1 — STEELMAN OF THE BOXED VALUE

The boxed `g ≈ α₀` is true iff the discarded factor `4πR·tanh²(r_oct/ξ) → 1`. Testing every route
(`scripts/repro_step1_steelman.py`):

| ξ convention (all used in the corpus) | source | r_oct/ξ | 4πR·tanh² | g | g/α₀ |
|---|---|---|---|---|---|
| ξ = a/√(8πα₀) (healing) — **as printed** | p.81 | 0.08936 | 0.04991 | 0.00036975 | 1/20.0 |
| ξ = R (vortex core) | pp.77–81 | 0.41421 | **0.96572** | 0.0071541 | **0.966** |
| ξ = r_oct (tight-binding) | p.82 | 1.0 | 3.64441 | 0.026998 | 3.64 |

**What would have made the boxed value right:** the factor equals 1 at `ξ ≈ 0.4903`, essentially
`ξ = R`. Under the corpus's own **vortex-core convention `ξ = R = 0.5`** (used on pp.77–81:
"core size is ξ = R_sphere = R"), the discarded factor is **0.966**, so `g = 0.966 α₀` — the boxed
"g ≈ α₀ to leading order" would hold, off by only **3.4 %**. This is why the box is *plausible*:
it is exactly the result under one of the three ξ values the corpus uses interchangeably.

**Why the boxed value nonetheless loses on the physics.** The factor `tanh(r_oct/ξ)` is, in §3.1's
own words, "the condensate amplitude at the oct void / sphere interface." A Gross–Pitaevskii
condensate recovers to its bulk value over the **healing length**; the tanh profile `ψ₀ tanh(x/ξ)`
*defines* ξ as that healing length. Using the sphere radius `R` in place of the healing length in a
condensate-amplitude factor is a category substitution, not a regime choice. The corpus places the
model at `ξ = a/√(8πα₀) = 2.32` (pp.81, 96, 114), not at `ξ = 0.49`. So the physically correct
overlap coupling is `g = 0.00036975`, and the boxed `α₀` is reachable only by swapping the healing
length for the sphere radius inside the tanh.

**Is the boxed number a different, legitimate object?** Yes — it is `σ_s/J = α₀` (§1.3), the
surface-potential/boundary coupling that sets the derivative-jump boundary condition
`κ cot(κR) = −1/ξ + α₀`. That object is correctly `α₀`. The error is not that `α₀` is wrong; it is
that §3.1 attaches `α₀` to `g` (the overlap coupling), a different quantity. Hence SC-TANH-3.

**Is the discarded factor a transcription slip that appears correctly elsewhere?** No. The overlap
suppression `tanh²(r_oct/ξ)` and the `4πR` surface/energy-denominator factor are computed only
here; they are not dropped by transcription but by the explicit (false) "to leading order" claim.

---

## STEP 2 — DIMENSIONS AND CONVENTION

- **Dimensional consistency as written:** `g = α₀ × 4πR × tanh²`. `α₀` and `tanh²` are
  dimensionless; `4πR` carries a **length**. The expression is dimensionless **only** under the
  corpus-wide convention `a = l_P = 1`, which reads `R = 0.5` as a pure number so that
  `4πR = 2π = 6.2832`. Under that convention the expression is well-formed and the value is
  determinate — so **not SC-TANH-4**. The latent point: a hidden length dimension is absorbed by
  the `l_P = 1` convention; had `R` carried explicit units, `g` would be dimensionful.
- **Silent unit convention:** lengths in units of the edge length `a`, with `a` set to `l_P`. This
  is used throughout (`r_oct = 0.207 l_P`, `R = a/2`, etc.), so it is **structural, not local**.
- **The convention question that actually bites is ξ, not units.** ξ is used at three
  incompatible values in the same neighbourhood of the corpus — `a/√(8πα₀) ≈ 2.32` (healing,
  p.81), `R = 0.5` (vortex core, pp.77–81), `r_oct = 0.207` (tight-binding, p.82). App J §3.1's
  printed arithmetic uses the healing value; its boxed conclusion is only valid at the vortex-core
  value. This ξ ambiguity is **structural** across the App-I/J and Ξ_BCT material (pp.77–83, 96,
  114), not local to §3.1.

---

## STEP 3 — DOWNSTREAM TRACE

Search built by: `grep -rniE "josephson|0\.0003697|α0=0\.0074|g *= *α|appendix[ ~]j"` over all 134
`.tex`; `pymupdf` full-text scan of Vol1 Parts 1–3 (875 pp.) and Vol2 (582 pp.) for `josephson`,
`0.00036975`, and `Appendix J`. **The computed value `0.00036975` was found in no `.tex` file and
in no PDF outside App J itself.** Each numeric user of a Josephson coupling, or citer of App J for
one, recomputed (`scripts/repro_step34_downstream.py`), not scaled:

| location | what it uses the value for | number it uses | correct object? | value under Step-1 verdict |
|---|---|---|---|---|
| App J §3.2 (Part1 p.115) | 2nd-order shift δE = −g²/(κ₀−ξ_geom) | g = α₀ | uses overlap-`g` name but plugs α₀ | δE −1.643e-5 → **−4.093e-8**; still 10¹⁴–10¹⁵× > m_e ⇒ **mechanism still rejected** |
| App J §4.1 (Part1 p.116) | Kondo m = m_P·exp(−1/[ρg]) | g = α₀ | overlap-`g` name, plugs α₀ | exp(−8.4e5) → exp(−1.7e7); **still rejected** |
| App J §4.2 / abstract | m_e/m_P ≈ α₀^(21/2) | **α₀**, not g | fine-structure α₀ (correct) | unchanged |
| `tex/BCT_Letter36_OHC_tex.tex` | α_z boundary coupling forces Hopf N=1; cites App J for κ₀=3.39 | α_z = α₀ = 0.00740806 | σ_s/J = α₀ (correct object) | **unchanged** (boundary coupling, not overlap-g) |
| `tex/BCT_Appendix_JH*.tex` | α_z across Josephson layer (boundary condition) | α₀ = 0.0074081 | σ_s/J = α₀ | **unchanged** |
| `tex/BCT_Appendix_KA1.tex` | "Josephson boundary condition at coupling α₀ = r_oct·r_tet/π" | α₀ = 0.0074081 | σ_s/J = α₀ | **unchanged** |
| `tex/BCT_Letter76_DarkEnergy.tex`, `tex/BCT_Letter77_ArrowOfTime.tex` | "Josephson correction 2α₀" to w and to T-asymmetry | 2α₀ | α₀ correction term (correct) | **unchanged** |
| `tex/BCT_Letter71_Baryogenesis.tex` | 3 Josephson phase slips, amplitude ~απ | α | α (correct) | **unchanged** |
| Vol2 pp.447, 453, 457, 463–464 | assert "Josephson coupling g = α₀ (exactly)", "= Higgs coupling analogue" | α₀ | **structural claim** (see §5) | claim false for overlap-g |
| Vol2 §3.3 p.482 | "Josephson coupling = α₀ — exact or approximate?"; higher-loop α₀ corrections | α₀ | structural | inherited the boxed claim; never saw the ×20 |
| Vol2 pp.493, 501, 509, 513 | Josephson coupling runs → 0 at m_P ⇒ Higgs criticality λ(m_P)≈0 | α₀ (running) | structural / RG | qualitative (runs to 0), start-value-independent |

**Note on δE/Kondo:** these are the *only* in-corpus numeric uses of the §3.1 overlap-`g`, and both
plug in `α₀` (the boxed value) rather than the printed `0.00036975`. Correcting them shrinks the
estimates by ~4×10² and more, but both mechanisms are *rejected in the same appendix* regardless,
so no conclusion moves.

---

## STEP 4 — THE TWO TALLIES (kept separate)

### Published numeric predictions affected: **ZERO**
No published numeric prediction uses the interior↔void overlap coupling `g = 0.00036975`. The value
appears in no `.tex` and in no PDF outside App J. Every numeric "Josephson coupling" downstream is
`α₀ = r_oct·r_tet/π = 0.0074081`, i.e. the boundary/surface coupling `σ_s/J` (= the fine-structure
constant), correctly and independently derived. The predictions in the corpus
(`m_P = M_R/α₀²`, `m_e = m_P exp[−S_D4/(1−α₀(4π+1)/π²)]`, `m_K = m_π/(√2 α₀^{1/3})`,
`m_e/m_P ≈ α₀^{21/2}`, dark-energy `w` deviation `∝ 2α₀`, …) are functions of **α₀**, not of `g`.
Correcting the §3.1 box moves none of them.

### Structural claims affected (named by document/section)
1. **App J, abstract** (Part1 p.112): "The dimensionless Josephson coupling between the sphere
   interior and the surrounding oct void is derived and found to equal exactly α₀." — FALSE for the
   overlap coupling (it is α₀/20). Survives only if reread as a statement about `σ_s/J`.
2. **App J §3.1 box** (Part1 p.115): "g = α₀ to leading order … the coupling and the
   electromagnetic coupling have the same geometric origin." — the "leading order" and "same
   geometric origin (as a coupling equality)" clauses fail for the overlap coupling.
3. **Vol2 p.447 / p.457 / p.463 / p.464:** "Josephson coupling g = α₀ (exactly)", "geometric
   coupling equals EM coupling", "BCT analogue of the Higgs coupling". — the coupling *equality* is
   false for the overlap coupling; these inherited the §3.1 box.
4. **Vol2 §3.3 p.482:** "The Josephson Coupling = α₀ — Exact or Approximate?" treats `g = α₀` as
   established from App J and debates only higher-loop α₀ corrections; it never registers the
   factor-of-20 between the printed and boxed values.
5. **Vol2 pp.493/501/509/513:** "Higgs criticality λ(m_P)≈0 derived from the Josephson coupling
   vanishing at m_P." This is a *running-to-zero* (RG) claim, independent of the coupling's
   Planck-scale starting value, so it is not numerically wrong; but it inherits the identification
   of "the Josephson coupling" with `α₀`, which for the overlap coupling is the conflation above.

Per §0.6 and a sibling gate's finding, the inter-component coupling that `g = α₀` is meant to be
the coefficient *of* is never written into any prediction, so even the structural reach is limited:
these are identity/name claims, not load-bearing coefficients.

---

## CN-TANH NOTICES (tiered; revised clause by clause)

- **CN-TANH-01 [PROVEN].** App J §3.1 prints `g = α₀·4πR·tanh²(r_oct/ξ) = 0.00036975` and boxes
  `g ≈ α₀ = 0.00740806`; the two differ by the factor `4πR·tanh²(r_oct/ξ) = 0.049912`, ratio
  **20.0353**. Every printed factor reproduces at 40 dps from independently derived
  `r_oct, r_tet, R, α₀, ξ`. *(scripts/repro_step0.py)*
- **CN-TANH-02 [PROVEN].** The "g ≈ α₀ to leading order" claim requires the discarded factor to be
  ≈1; at the healing length `ξ = a/√(8πα₀)` that §3.1's own arithmetic uses, it is 0.0499 (≈1/20).
  The claim is false at the ξ actually used. *(repro_step0.py, repro_step1_steelman.py)*
- **CN-TANH-03 [PROVEN].** The boxed `α₀` is the correct value of a *different* object, the
  surface/boundary coupling `σ_s/J = α₀` (§1.3, App D). The overlap coupling and the boundary
  coupling are conflated under the single name "the Josephson coupling". *(primary source §1.3, §3.1)*
- **CN-TANH-04 [PROVEN].** The boxed claim holds (to 3.4 %) under the corpus's alternative
  `ξ = R` vortex-core convention (pp.77–81); the factor is 0.966 there. The corpus uses ξ at three
  incompatible values (2.32 / 0.5 / 0.207) in the same region. *(repro_step1_steelman.py; pp.77–83)*
- **CN-TANH-05 [PROVEN].** The printed value `0.00036975` occurs in no `.tex` (of 134) and in no
  PDF outside App J. No published numeric prediction uses the overlap coupling `g`. Numeric-tally
  = 0. *(grep over 134 tex; pymupdf scan of 1457 PDF pages)*
- **CN-TANH-06 [PROVEN].** The only in-corpus numeric uses of the §3.1 `g` (App J §3.2 δE, §4.1
  Kondo) both plug in `α₀`, and both belong to mechanisms explicitly rejected in App J; under the
  correct `g = α₀/20` they shrink (δE → −4.09e-8; Kondo exponent → −1.7e7) but stay rejected.
  *(repro_step34_downstream.py)*
- **CN-TANH-07 [CONJECTURE].** The physically correct ξ inside a condensate-amplitude
  `tanh(r_oct/ξ)` is the healing length, making `g = 0.00036975` the true overlap coupling and the
  box an error. This rests on the standard GP reading of the tanh profile, which the corpus states
  but does not re-derive at §3.1. *(inference from GP profile + p.81 healing-length definition)*
- **CN-TANH-08 [ASSERTED].** Vol2 pp.447/457/463/464/482 assert `g = α₀` ("exactly", "= EM
  coupling", "Higgs analogue") citing App J; these inherit the §3.1 box and carry no independent
  derivation of the coupling equality. *(Vol2 primary text; not independently checked beyond
  confirming they cite App J and use α₀)*

---

## §0.6 — WHAT SETTLING THIS BUYS (reproduced verbatim)

> Fixing a coupling constant does **not** supply the BCT mass mechanism, the Higgs mass, or any
> prediction. A separate gate found the inter-component coupling this constant is used *as* is
> never written down anywhere, so a corrected value may have nothing correct to be the coefficient
> of. **What this gate buys is a known number in place of an ambiguous one, and an honest count of
> what moves when it changes.** If nothing published moves, that is the result and it should be
> stated as plainly as any other.

Consistent with this: nothing published moves. The gate buys a known number
(`g_overlap = 0.00036975 = α₀/20.035`, distinct from the boundary coupling `σ_s/J = α₀`) in place
of the ambiguous "g = α₀", and the honest count is: **0 numeric predictions, a family of
identity/name structural claims.**

---

## CONTAMINATION STATEMENT

- **Digest:** held (gate-prompt SHA matched pre-registration; corpus tarball SHA recorded above).
- **No `conversation_search`, no `recent_chats`** were used (per QUARANTINE).
- **audit/notes/ and every audit/gates/\*/ deliverable were not read.** In particular, a
  pre-existing `audit/gates/TANH/README_MISSING.md` (436 B) was found in the corpus tarball; it was
  typed with `file` but **its contents were not read**, and this patch does not modify it.
- **Inheritance (§0.3):** the §3.1 arithmetic was derived from App J's own printed factors and the
  primary definitions of `r_oct, r_tet, R, α₀, ξ`. No prior finding on App J §3.1 was read as an
  input.
- **Memory system:** this session runs with a memory filesystem whose *one-line listing* (file
  paths + descriptions) is injected into context. That listing names sibling-gate files
  (MAD, RANK/MP/PRED, LINK) and an audit-findings file. **None of their contents was read**, and no
  description in the listing concerns App J §3.1 or the Josephson-coupling factor-of-20. My
  derivation preceded and did not draw on any of them.
- `audit/NEXT.md` was **not** modified (per instruction; concurrent patches conflict there).

---

## WHAT THIS GATE DID **NOT** ESTABLISH

- It did **not** supply a mass mechanism, the electron or Higgs mass, or any prediction. The
  `m_e/m_P ≈ α₀^{21/2}` numerology and the "21-vertex fermionic loop" remain unproven and untouched
  by this gate.
- It did **not** verify that `σ_s/J = α₀` is itself physically correct — only that it is the object
  the corpus uses downstream and that it is derived independently in App D; App D's own 1.52 %
  miss against CODATA α is a separate matter and out of scope here.
- It did **not** audit the RG claim that the Josephson coupling runs to zero at `m_P` (Vol2
  App AG); only noted that it is start-value-independent and so numerically untouched.
- It did **not** re-derive the GP tanh interface profile; CN-TANH-07 (that the healing-length ξ is
  the physically correct one) is tiered CONJECTURE for that reason.
- It did **not** read the pre-existing `README_MISSING.md`, so whatever that file records about
  TANH is not reflected here.
