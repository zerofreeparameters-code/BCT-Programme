# GATE MP — RESULT
## Is the Planck mass an input or an output?

Executed 13 September 2026. Cold Ledger. One gate, one thread.

**Model.** Operator brief states "Claude Opus 5". The executing session's own system context identifies it as Claude Fable 5.1 (Anthropic states Fable 5.1 and Mythos 5.1 share one underlying model). Both are recorded; the operator's label is not independently verifiable from inside the session.

---

## §1 — Digests

| item | digest / size |
|---|---|
| Pre-registered (operator brief) | `be3481fb27b3c22ec0dc9cd6ac31fec2d92131cab71f079343ecba62ca5b8f33`, 6464 bytes |
| `audit/gates/gate_MP_prompt.md` @ `aa709432` as fetched | `be3481fb27b3c22ec0dc9cd6ac31fec2d92131cab71f079343ecba62ca5b8f33`, 6464 bytes — **MATCH** |
| `audit/gates/gate_RANK_prompt.md` @ `aa709432` (the file the brief's literal `curl` line named) | `72865268c30c1a06d9dac94c46a0d958b27a46fcac27b1e8d3a94d05e8e698e4`, 8043 bytes — mismatch, not opened |
| Corpus tarball `codeload…/aa709432` | `3729ad1fea39d94a0555c698cef2ad7a3a6c8b7cbc4259dff162400af5546f07`, 45,461,432 bytes, 210 files |
| Vol 2 PDF (inside the zip) | `24b565f3bde5dab34724f3f8118f88af94f179bed872c8f578ab0e178421cc52`, 18,123,373 bytes, 582 pp |

The brief's `curl` line pointed at `gate_RANK_prompt.md` while its text said `gate_MP_prompt.md`. The RANK file was hashed, found not to match, and discarded unread. The MP file matched the pre-registration exactly and is the only gate executed.

## §2 — Search-space coverage (before any other number)

| gate's stated inventory | found at `aa709432` |
|---|---|
| 134 `.tex`, 26 at root | **134 `.tex`, 26 at root, 108 in `tex/`** — exact |
| Vol 1: three PDFs, 240,670 words, 137 appendices | Part1 425 pp / Part2 425 pp / Part3 25 pp; **249,941 words** (pymupdf); index headings: 64 + 112 + 9 |
| Vol 2: zip → 18 MB PDF, 582 pp, 151,710 words, 108 appendices | 582 pp, 18.1 MB, **159,217 words**; 182 `Appendix XX` headings (includes review/sub-parts) |
| `audit/APPENDIX_INDEX.md` — "use it" | **absent at this commit**. Substituted: the "Complete Index" on pp. 3–13 of each volume, extracted from the PDF text layer |
| "two mount PDFs are raw text; some are ZIPs of page images" | **not true of the repo files at this commit**: `file` types all three Vol 1 parts as genuine PDFs with text layers (1288 / 1525 / 96 fonts). The brief's note appears to describe an earlier mount, not the repo |

Every file was typed with `file` (listing in this thread; 210 files). Quarantined and not opened: `audit/notes/`, `audit/gates/LINK/`, `audit/gates/C1/` (the latter two do not exist as directories at this commit; `gate_LINK_prompt.md` and `gate_C1_prompt.md` sit in `audit/gates/` and were not opened). `conversation_search` and `recent_chats` were not called.

Search method: full-text regex over all four appendix volumes and all 134 `.tex` for (a) `m_P … exp(−…)` forms, (b) input/measured/assumed statements about m_P, G_N, the Planck mass, (c) lattice-spacing / Planck-length statements. Hits: 183 / 127 / 349. Script and raw output committed (`gate_MP_corpus_scan.py`, `.out`). Every appendix cited below was then read in full from the text layer.

## §3 — Verdict first

**SC-MP-1, with a qualification the stop condition does not name.** m_P is an input everywhere the corpus does physics with it. The titled derivation (Appendix HF4, Phase 60C, Vol 1 p. 837–838) is **neither a consistency check nor a fit: it is an algebraic identity**. It divides M_R by α₀², and M_R was defined three phases earlier (Appendix GG2, Phase 45A, Vol 1 p. 690) as m_P·α₀² with m_P supplied as a 3-significant-figure input. Followed back, HF4's chain does not terminate at any measurement — it returns to its own starting point. Its quoted −0.080% "error" is, to within 0.004%, the rounding of the input 1.22093→1.22 (−0.073%) plus the rounding of M_R 6.69527→6.6950 (−0.004%). Arithmetic in `gate_MP_precision.out`.

**Secondary finding, SC-MP-3 (corpus consistency).** Different documents declare different input sets, M_R takes two values that differ by a factor 10⁴, and G_BCT is quoted at four mutually incompatible values. Enumerated in §5 and the notices.

**Two further "derivations" of m_P exist and are fits, not circular:** JB6 (m_P = Λ_QCD·e^{S_QCD}) and Letter 128 (m_P = m_e·e^{S_e}). Each terminates at a stated value (220 MeV; CODATA m_e), so by the gate's own rule they are not circular. But in each case the exponent was *selected* by matching ln(m_P^CODATA/X) — HN5 tabulates the candidates it tried against "S_QCD(obs) = 45.463"; Letter 31 reports S_e against "ln(m_P/m_e)_obs = 51.527840" with a residual δ — so m_P^CODATA is consumed at the selection step and the "prediction" is the residual of that match, relabelled. That is the fit defect the gate says belongs elsewhere; it is named here and not scored.

**The scale finding (SC-MP-5 not reached).** The lattice spacing is set to the Planck length by assumption, and the corpus says so in three places (Appendix AL; Appendix E1; Vol 2 p. 483 "the dimensional relation between the void radii and the lattice constant a is assumed"). The scale is externally fixed and declared. Circularity in HF4 blocks the favourable stop condition.

## §4 — §0.6 reproduced verbatim

> Establishing whether m_P is an input or an output does **not** validate or refute any individual
> prediction, and it does not measure whether the predictions are surprising — that is a separate
> question for a separate gate. **What this gate buys is the dependency graph**: which quantities
> the corpus takes from measurement, which it claims to derive, and whether any derivation consumes
> its own output. A clean graph is a precondition for scoring anything. **A favourable verdict here
> is a ticket to a harder gate, not a result about physics.**

## §5 — Step 0: the dependency graph

Each node: stated status in primary source, with volume and line (line = PDF text-layer line number from the committed extraction; page numbers as printed in the volume).

| node | measured input? | claimed derived? | verdict | primary source |
|---|---|---|---|---|
| **m_P** | YES — "the Planck mass m_P is one of the three fundamental inputs (along with r_oct and r_tet)" (FP, V1 p. 635); "Input: m_P 1.2209×10²²" (Letter 126 tex l.445); "All inputs are geometric: r_oct, r_tet, and m_P" (Letter 127 v2 l.307); "reproduces G to the accuracy of the input Planck mass" (Volume1_Foundations.tex l.214); "m_P (the only input parameter beyond void geometry)" (V1P2 l.9845) | YES — HF4 "m_P = M_R/α₀²" (V1 p. 837); JB6 "m_P = Λ_QCD·exp(S_QCD)" (V2 p. 249); Letter 128 "m_P^BCT = m_e·exp(S_D4/(1−NLO))" (l.250); FP "since m_e is measured, m_P is effectively predicted too" (V1 p. 635) | **BOTH** | — |
| **α₀** | no | derived: α₀ = r_oct·r_tet/π (App D); but Vol 2 p. 497 lists "ASSUMPTION 2: The Josephson coupling formula α₀ = r_oct×r_tet/π … identified numerically … not proven from first principles" | derived (formula asserted) | V2 l.22258–22262 |
| **r_oct, r_tet** | no | derived from c/a = √2 void geometry; (√2−1)/2, (√6−2)/4 | derived | App D1; HN5 V2 p. 47 |
| **ξ** | no | ξ = a/√(8πα₀) = 2.32 ℓ_P — dimensionless in lattice units, inherits a = ℓ_P | derived, scale-dependent | V1P1 l.4471–4474, l.5442, l.12199 |
| **J** | no | J = 1/(4πα₀) by identification with the bare EM coupling ("Taking J = 1/g₀²") | identified, not derived | V1P1 l.3314–3316 |
| **Λ_QCD** | YES — "Λ_QCD = 220 MeV … fundamental input" (HF4 table, V1 p. 837); "(Phase D, BCT input scale)" (GT, V1 p. 758); input #3 in HF5's fit | YES — HN5 "Λ_QCD = m_P·exp(−S_QCD) = 219.7 MeV" (V2 p. 47); BB2 220.13; Letter 127 219.83; V2 l.4968 220.4 | **BOTH** | — |
| **v_EW** | measured 246.22 used as comparator; HF4 table prints "244,400" in the *observed* column (a transcription error) | derived: (a) λ(m_P)=0 criticality run down from m_P (BE/BH/BM/BR/CH) → 244.4; (b) v = m_P·e^{−π⁵/12/(1−x_EW)} → 245.80 (L128); (c) v = m_P·e^{−S_EW} with S_EW ≡ ln(m_P/v) (V1P1 l.12882 — definitional) | derived; **consumes m_P in every route** | — |
| **M_R** | no | two incompatible derivations: GG2 M_R = m_P·α₀² = 6.695×10¹⁴ GeV (V1 p. 690); CC M_R = m_P·e^{−S_R}, S_R = 2π²(1−r_oct/2π) → 6.256×10¹⁰ GeV (V1P2 l.10984) | derived, **two values, ratio 1.07×10⁴** | — |
| **S_D4 = π⁵/6** | no | "S_D4 = π⁵/6 exactly from D4 instanton saddle-point (App Z′)" (V2 l.21224); but Vol 2 p. 497 "ASSUMPTION 3: … No proof has been given that no other saddle point contributes" | derived conditional on a declared assumption | — |
| **m_e** | YES — CODATA used by Letter 128 to invert to m_P; CODATA used to define "ln(m_P/m_e)_obs" against which S_e is tuned (Letter 31 l.51, l.81) | YES — m_e = m_P·e^{−S_e}, several S_e forms (see §7) | **BOTH** | — |
| **ℏ, c** | units; set to 1 throughout; c identified with the BCT phonon speed (E1, V1P1 l.3189) | — | convention | — |
| **G** | YES — "G_N = ħc/m_P² (definition)" (FP); CODATA 2022 6.67430(15) quoted (AL) | claimed: AL (+0.151%), Letter 128 (−0.028%), JB6 (+0.40%) — all inversions of an m_P·e^{−S} relation; AL itself states "G CANNOT be derived numerically from BCT first principles alone" (V1 p. 274) | **BOTH**; the corpus contains its own negative finding | — |

**The graph.** Arrows point from what is consumed to what is produced.

```
                 c/a=√2 (axiom)
                     │
              r_oct, r_tet ──► α₀ ──► ξ, J        (pure ratios; no scale)
                     │            │
                     │            ├──────────────┐
   a ≡ ℓ_P (ASSUMED) │            │              │
        │            ▼            ▼              ▼
   m_P (INPUT) ──► M_R = m_P·α₀²  ──► HF4: "m_P = M_R/α₀²"   ◄── returns to m_P  [CIRCULAR]
        │
        ├──► m_e   = m_P·e^{−S_e}      S_e tuned to ln(m_P^CODATA/m_e)  ──► L128: "m_P = m_e·e^{S_e}" ──► "G_N"   [FIT, inverted]
        ├──► Λ_QCD = m_P·e^{−S_QCD}    S_QCD chosen against ln(m_P^CODATA/220) ──► JB6: "m_P = Λ·e^{S_QCD}" ──► "G_N"   [FIT, inverted]
        ├──► v_EW  via λ(m_P)=0 RG run, or m_P·e^{−S_EW}
        ├──► M_R   = m_P·e^{−S_R}      (second, incompatible M_R)
        ├──► E_inf = m_P·e^{−S_D4·r_tet}
        └──► ρ_CC^{1/4} = m_P·e^{−S_D4/2}
```

Nodes that are both input and output: **m_P, Λ_QCD, m_e, G**. §6 applies to each.

## §6 — Step 1: circularity test, node by node

### m_P — chain A (HF4). CIRCULAR.
1. GG2 (Phase 45A, V1 p. 690): "M_R(BCT) = m_P · α₀² = 1.22e+28 eV × (0.00740806)² = 6.695273338819552e+23 eV". m_P enters as **1.22×10¹⁹ GeV, three significant figures**.
2. GT2 (Phase 47D, V1 p. 756): "f_a = M_R = m_P·α₀² = 6.6953e+14 GeV" — restates (1); names it the "triple unification" scale.
3. HF4 (Phase 60C, V1 p. 837): "m_P(BCT) = M_R / α₀² … M_R(BCT) = 6.6950e+17 MeV (Phase 55, triple unification) … = 1.219950e+22 MeV … err −0.08025% ← sub-0.09%! [51st sub-1%]".
4. Terminus: **m_P itself**. No measured quantity other than the input m_P is consumed. With M_R carried at full precision the output is 1.220000×10²² exactly — the input.

Numerical consistency: HF4's output disagrees with the m_P it presupposes by −0.0769% (computed) vs −0.08025% (claimed); the 0.003% gap is HF4 using α₀² = 5.4879290e-5 against GG2's α₀ = 0.00740806 (α₀² = 5.4879353e-5) and a truncated M_R. Decomposition: input rounding −0.0729%, M_R rounding −0.0041%, α₀² mismatch +0.0001%. No physics enters the residual.

Note also: HF4 attributes M_R to "Phase 55"; no Phase-55 appendix in either volume defines M_R — Phase 55 (Vol 1 p. 18194 index) is neutrino spectrum/baryon asymmetry/dark energy. M_R's origin is Phase 45A. Attribution error, recorded.

### m_P — chain B (JB6). FIT, not circular.
1. HN5 (Phase 67B, V2 p. 46): "S_QCD(obs) = ln(mP/Λ_QCD) = 45.4628" — uses m_P^CODATA and Λ = 220. Tabulates five candidate expressions and their errors against 45.463; selects S_D4(1−r_tet+α₀/2) at −0.004%; labels it "Conjecture".
2. JB6 (Phase 75B, V2 p. 249): "m_P = Λ_QCD × exp(S_QCD) … = 220 × exp(45.4608) = 1.2185e+22 MeV … Error −0.200% … G_N error 0.40% … first derivation of Newton's constant from any underlying microscopic theory". Attributes S_QCD to "Phase 45 (the D4 Root Decomposition Theorem)" and calls it a Theorem.
3. Terminus: Λ_QCD = 220 MeV, a stated input (not a PDG value — PDG Λ^(3)_MS ≈ 332 MeV, Λ^(5) ≈ 210 MeV; provenance of 220 is outside this gate). m_P^CODATA was consumed at step 1 to choose the exponent; the −0.20% is the residual of that choice. Not circular in the gate's sense; a fit with its residual relabelled.
4. Arithmetic: HN5's own forward number "Λ_QCD = 219.7 MeV (−0.14%)" does not reproduce — 1.22093×10²²·e^{−45.4610} = 220.44 MeV (+0.20%). A later appendix (V2 l.4968, l.6389) prints 220.4 / +0.20% without noting the sign flip. Both survive in the corpus.

### m_P — chain C (Letter 128 / AL). FIT, not circular.
1. Letter 31 l.49–51: "S_e = (π⁵/6)/(1 − α₀(4π+1)/π²) = 51.527981 against the observed ln(m_P/m_e) = 51.527840". Residual δ = +0.000141. m_P^CODATA consumed to define the target.
2. Letter 128 l.249–258: "m_P^BCT = m_e exp(S_D4/(1−NLO)) … G_N^BCT/G_N^CODATA = (m_P^CODATA/m_P^BCT)² = 1 − 0.00028". Recomputed: 0.999718, −0.0282%. Reproduces.
3. AL (Phase 9, V1 p. 273–274) did the same with the earlier exponent π⁵/6/(1−4α₀/π) = 51.489 and obtained G_BCT "+0.151% above CODATA"; the printed value is "0.000000×10⁻¹¹" (broken rendering), elsewhere "6.684", "6.6844", and — in Vol 2 p. 497 — "6.764×10⁻¹¹". Recomputed from AL's own exponent: +8.09%, not +0.151% (51.489 vs 51.528 is a 3.97% shift in m_e, 8.1% in G). AL's headline number does not follow from AL's exponent.
4. Terminus: m_e (CODATA). Not circular; a fit whose residual is presented as a G_N prediction, with sign and magnitude changing every time the exponent is re-tuned.

### Λ_QCD. BOTH; the two roles are never reconciled.
Input 220 MeV feeds α_s(m_Z) (GT), HF5's global fit (as input #3), and defines S_QCD(obs). Derived Λ_QCD (HN5, JB6, BB2, L127) consumes m_P and the tuned exponent. HN5 §5 states the consequence — "BCT becomes a two-input theory (r_oct, r_tet)" — while HF5 (same volume, earlier phase) counts Λ_QCD as an input and FP counts m_P. The corpus has not settled its own input set. Terminates at measurement (m_P^CODATA); a fit.

### m_e. BOTH; terminates at measurement; a fit through a sequence of exponents.
Exponents in the corpus, in order written: π⁵/6 (+69%); π⁵/6/(1−4α₀/π) = 51.489 (+3.97%); (π⁵+π)/6 = 51.5269 (+0.023% with m_P = 1.2200×10²²; **+0.096% with CODATA m_P**); π⁵/6/(1−α₀(4π+1)/π²) = 51.527981 (−0.014%). Each is compared against ln(m_P^CODATA/m_e^CODATA) = 51.527840 and the next is chosen to reduce the residual. Not circular. A fit; scored elsewhere.

### G. BOTH; the corpus's own AL finding stands unrefuted.
AL: "the formula G = c⁴/(16πρ_BCT) … reduces to a tautology when ρ_BCT is expressed in terms of G. To derive G numerically, one needs the BCT lattice constant a in SI units INDEPENDENT of G." Nothing later in either volume supplies that. JB6's "first derivation of Newton's constant" and Letter 128's "Prediction #167a" are chains B and C above.

## §7 — Step 2: precision against input precision

CODATA 2022: m_P = 1.220890(14)×10¹⁹ GeV (relative uncertainty 1.1×10⁻⁵, inherited from G); m_e = 0.51099895069(16) MeV. Full output in `gate_MP_precision.out`.

| prediction | S | m_P used (s.f.) | claimed X, error | X at CODATA m_P, error | shift | flag |
|---|---|---|---|---|---|---|
| HF4 m_P = M_R/α₀² | — | 1.22×10²² (3) | 1.219950×10²², −0.080% | identity → returns input | — | **claimed error 0.08% < half-ulp of a 3-s.f. input (±0.41%)**; residual is the input's rounding |
| GG2 M_R = m_P α₀² | — | 1.22×10²² (3) | 6.6953×10¹⁴ GeV, "prediction" | 6.7004×10¹⁴ | +0.076% | printed to 16 digits ("669527333881955.250 GeV") from a 3-s.f. input |
| m_e = m_P e^{−(π⁵+π)/6} (FG/FP) | 51.526880 | 1.2200×10²² (4–5) | 0.511117, +0.023% | 0.51149, **+0.096%** | +0.073% | claimed precision depends on which rounded m_P was used; FP's "exact to 0.0004%" is a match in the *logarithm*, = 0.023% in m_e |
| m_e = m_P e^{−S_e} (L31/L19) | 51.527981 | CODATA | 0.510927, −0.014% | 0.510927, −0.0141% | 0 | reproduces; S_e tuned against this m_P (fit) |
| ln(m_P/m_e) = π⁵/6/(1−4α₀/π) (AL/AC) | 51.488936 | — | "0.075% residual" | m_e 0.53127, **+3.97%** | — | "0.075%" is the log residual; 4% in m_e, 8% in G |
| Λ_QCD = m_P e^{−S_QCD} (HN5) | 45.460835 | 1.22093×10²² (6) | 219.7, −0.14% | **220.44, +0.199%** | +0.34% | HN5's number does not reproduce from HN5's formula; V2 l.4968 later prints 220.4 |
| JB6 m_P = 220 e^{45.4608} | 45.4608 | (220 MeV, 2–3 s.f.) | 1.2185×10²², −0.200% | 1.21842×10²², −0.202% | 0 | reproduces; 220 MeV carries no stated uncertainty; exponent selected against m_P^CODATA |
| L128 v = m_P e^{−π⁵/12/(1−x_EW)} | 38.444185 | CODATA | 245.80 GeV, −0.171% | 245.80, −0.171% | 0 | reproduces |
| CC M_R = m_P e^{−S_R} | 19.088564 | — | 6.2561×10¹⁰ GeV | 6.2606×10¹⁰ | +0.07% | incompatible with GG2's M_R by ×1.07×10⁴; both survive |
| CT E_inf = m_P e^{−S_D4 r_tet} | 5.731363 | 1.2209×10²² | "39589248594.5 GeV", −3.5% and +23.3% both printed | **3.959×10¹⁶ GeV** | ×10⁶ | MeV→GeV conversion slip; two contradictory errors printed; does not reproduce |
| FQ ρ_CC^{1/4} = m_P e^{−S_D4/2} | 25.501640 | — | "2.2640×10⁻⁶ MeV", −2.8% | **1.03×10¹¹ MeV** | ×10¹⁷ | does not reproduce; the quoted "observed 2.33×10⁻⁶ MeV" is also not the observed 2.3 meV = 2.3×10⁻⁹ MeV |
| L128 G_N = (m_P/(m_e e^{S_e}))² | 51.527981 | CODATA | −0.028% | −0.0282% | 0 | reproduces; is the m_e-fit residual squared |
| AL G_BCT from exponent 51.489 | 51.488936 | CODATA | +0.151% (also 6.764 / 6.684 / 6.6844 ×10⁻¹¹) | **+8.09%** | — | AL's headline does not follow from AL's exponent |

m_P's own CODATA uncertainty (0.0011%) is below every claimed error in the table, so no prediction is flagged for *that* reason. Flags arise from (i) rounded m_P values (3–5 s.f.) used as inputs to predictions quoted at 0.02–0.08%, and (ii) arithmetic that does not reproduce.

## §8 — Step 3: the units question

**What sets a = 1 ℓ_P: assumption, declared.**
- E1 (V1P1 l.3187–3188): "ρ_s = J/a is the superfluid stiffness (J = lattice exchange coupling, a = l_P = lattice spacing)".
- App AL summary of App E.3/D (V1P1 l.3082–3083): "K_BCT was computed in Appendix D (though it required l_P as an external input)".
- Vol 2 §3.3 (l.21542–21544): "The identification of α₀ = r_oct × r_tet / π … derived from void geometry (App D) but the dimensional relation between the void radii and the lattice constant a is assumed."
- Vol 2 p. 504 (l.22502–22505): "ρ_BCT = m_P/(a³) where a = BCT lattice constant. Since the BCT lattice is at the Planck scale, a = ℓ_P".
- Letter 129 l.112: "a displacement of one lattice constant a = ℓ_P (one Planck length)".
- AL (V1 p. 274): the honest statement — the SI value of a requires "a non-gravitational measurement at the Planck scale — which is currently impossible."

One inconsistent usage: Vol 2 p. ~180 (l.8846) "lattice spacing a = ℏc/Λ" (i.e. ~0.9 fm) in an ultralight-phonon argument. Recorded as CN-MP-07(b).

Conclusion: the geometry fixes ratios only (r_oct, r_tet, α₀, ξ/a, S_D4 are all pure numbers). The single dimensionful scale is m_P (equivalently ℓ_P, equivalently G), supplied from measurement and identified with the lattice spacing by assumption. The corpus supplies the scale, declares it, and in AL states the impossibility of doing otherwise. Every X = m_P·e^{−S} is therefore a prediction of the *ratio* X/m_P, and every claimed "derivation of m_P" (HF4, JB6, L128) is either the identity or the inverse of one of those ratio predictions with X supplied instead.

## §9 — CN-MP notices

Tier: **PROVEN** = follows by arithmetic or verbatim quotation from the pinned corpus; **CONJECTURE** = my reading, could be overturned by a document I did not find; **ASSERTED** = the corpus's own statement, reported not verified.

**CN-MP-01 [PROVEN].** HF4's "m_P = M_R/α₀²" consumes GG2's "M_R = m_P·α₀²" and returns the input m_P. The chain is closed on itself; no measurement other than the input enters. (V1 p. 690; V1 p. 837.)

**CN-MP-02 [PROVEN].** HF4's −0.080% is rounding: −0.0729% (input 1.22 vs 1.22089) −0.0041% (M_R 6.6950 vs 6.69527) +0.0001% (α₀²) = −0.0769%; HF4 prints −0.08025%. The claim "51st sub-1% prediction" and "sub-0.09%" attach to no prediction. A 3-s.f. input carries ±0.41% half-ulp; the claimed error is 5× smaller than the input's own rounding uncertainty.

**CN-MP-03 [PROVEN].** M_R has two incompatible corpus values: 6.695×10¹⁴ GeV (GG2/GT2/HF4/L128, = m_P α₀²) and 6.256×10¹⁰ GeV (CC, = m_P e^{−S_R}, S_R = 2π²(1−r_oct/2π)). Ratio 1.07×10⁴. Downstream: m_ν₀, f_a, m_a, leptogenesis ε₁, and HF4 all consume the first; Letter 40's m_ν₃ = m_τ²/M_R consumes the second.

**CN-MP-04 [PROVEN].** Declared input sets differ: {r_oct, r_tet, m_P} (FP V1 p. 635; L126; L127 v2; Vol1_Foundations.tex); {r_oct, r_tet, Λ_QCD} (HF5 V1 p. 838; GT); {r_oct, r_tet} only (HN5 V2 p. 48; JB6 V2 p. 251 "No additional inputs beyond c/a = √2"). No document reconciles them.

**CN-MP-05 [PROVEN].** JB6 calls S_QCD = S_D4(1−r_tet+α₀/2) "THE BCT PLANCK MASS THEOREM" and attributes it to "Phase 45 (the D4 Root Decomposition Theorem)". Its source is HN5, Phase 67B, which labels it "Conjecture", obtained by trying five expressions against ln(m_P^CODATA/220), and lists the analytic derivation as not done ("target of Phase 68B"). JB6 also prints "π⁵/6 = 97.409" (it is 51.003) in its §3.1 line "97.409 × 0.891334 = 45.461".

**CN-MP-06 [PROVEN].** G_BCT is quoted at −0.028% (L128), +0.151% (AL; printed value "0.000000×10⁻¹¹"), 6.764×10⁻¹¹ (Vol 2 p. 497, = +1.35%), 6.684 and 6.6844×10⁻¹¹ (Vol 2 pp. 512–513, = +0.15%), and +0.40% (JB6). Each is the residual of a different tuned exponent. AL's +0.151% does not follow from AL's exponent (recomputed +8.09%).

**CN-MP-07 [PROVEN].** (a) The lattice scale is fixed by assumption a = ℓ_P, declared in E1, AL, Vol 2 §3.3, Vol 2 p. 504, Letter 129. (b) Vol 2 l.8846 instead uses a = ℏc/Λ_QCD in one argument.

**CN-MP-08 [PROVEN].** Two m_P·e^{−S} predictions do not reproduce from their own printed formulas: CT's E_inf (off ×10⁶; two contradictory errors printed) and FQ's ρ_CC^{1/4} (off ×10¹⁷; "observed" value also wrong by ×10³). HN5's Λ_QCD = 219.7 (should be 220.44 from its own formula and m_P).

**CN-MP-09 [PROVEN, corpus's own statement].** Appendix AL: "G CANNOT be derived numerically from BCT first principles alone… The structural formula G = c⁴/(16πρ_BCT) is dimensionally self-referential." HF4, JB6 and Letter 128 later claim derivations of m_P/G_N without citing or answering AL.

**CN-MP-10 [PROVEN].** FP's "exact to 0.0004%" for ln(m_P/m_e) = (π⁵+π)/6 is a match in the logarithm; in m_e it is +0.023% with FP's rounded m_P = 1.2200×10²² and +0.096% with CODATA m_P. FP's table also prints v_EW "observed" as 244,400 MeV (the BCT value; observed is 246,220).

**CN-MP-11 [CONJECTURE].** No document in either volume or any `.tex` derives a dimensionful scale from the geometry without consuming m_P, Λ_QCD = 220 MeV, or m_e. Search covered the full corpus (§2); a derivation phrased without any of the regex-matched tokens could have been missed.

**CN-MP-12 [ASSERTED, not verified here].** The corpus's own "honest audit" (Vol 2 pp. 497 and 512–513) lists as undischarged assumptions: the GP condensate structure; the formula α₀ = r_oct r_tet/π; D4-instanton saddle dominance; and the 0.075% residual. These bear on every node in §5 and are outside this gate.

## §10 — Contamination statement

- **Auto-loaded context.** The session's memory listing displayed one-line descriptions for three Cold Ledger project files (`audit-findings.md`: "closed sectors by proof, what survives, active correction ledger, open problems"; `overview.md`; `ways-of-working.md`). **None was opened.** No m_P- or m_e-specific content appeared in those descriptions. The project-files list also named `claude_Gate_C1_Result___Interior_Healing_Length.md` and `claude_Gate_Session_Prompts.md`; neither was opened. Fourteen project PDFs were attached with empty content blocks; none was read.
- **Prior findings.** No prior finding about m_P, G, or the electron mass reached me before the dependency graph was built. `audit/NEXT.md` was read *after* §5–§8 were complete, solely to update it; it mentions m_e only as a queued PRED item and π⁵/6 only as "Gate STAT … 3.3 bits". Neither affected the derivation above, which preceded the read.
- **Operator brief.** Contained no physics findings. It contained the pre-registered digest, the commit, and mount-format notes that turned out not to describe the repo files at this commit (§2).
- **Not consulted.** `conversation_search`, `recent_chats`, `audit/notes/`, any 9–12 Sep thread, BCT-X / Sandbox TOP, any concurrent gate.
- **Model.** See header.

## §11 — What the gate did not establish

- Whether any X/m_P ratio prediction is *surprising* — the exponents' fit-vs-derivation status is named, not scored. Gate PRED.
- Whether α₀ = r_oct·r_tet/π, S_D4 = π⁵/6, or c/a = √2 are derived; the corpus itself lists two of the three as assumptions (CN-MP-12).
- Whether Λ_QCD = 220 MeV has a measured provenance. It is not a PDG value; its origin ("Phase D") was not traced.
- Whether the λ(m_P) = 0 boundary condition — the route by which v_EW consumes m_P — is derived or assumed (Vol 2 l.24552–24553 calls it "an assumption, not a proof").
- Whether any *post*-Phase-94 `.tex` (Letters 204–254 at the root) changes the m_P picture. They were regex-searched and none defines or derives m_P; they were not read in full.
- Anything about the physics. §0.6 governs.

## §12 — Prompt defects, recorded not fitted

- SC-MP-1 offers "consistency check or a fit". HF4 is neither; it is an identity. Reported under SC-MP-1 with that qualification.
- §0.5 cites `audit/APPENDIX_INDEX.md`, absent at the pinned commit.
- §0.5's file-format warnings describe a mount, not the repo tarball, at this commit.
- The operator's `curl` line named the wrong file; the text named the right one. Resolved by hashing both and running only the match.

## §13 — Files committed to `audit/gates/MP/`

`gate_MP_RESULT.md` (this file) · `gate_MP_prompt_asrun.md` · `gate_MP_precision.py` / `.out` · `gate_MP_corpus_scan.py` / `.out`. `audit/NEXT.md` updated (MP moved to Closed; SC-MP-3 residue queued as a corpus-consistency item under PRED).
