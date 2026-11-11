# GATE SONO — RESULT

**Letter 110's two ratio claims (#154 sonoluminescence spectral ratio, #155 biophoton band ratio), reproduced and
fitted on their own terms.**
Run 12 November 2026 (started 07:40 AEDT) · fresh thread inside the BCT Project · Claude (Fable 5.1) · one gate, this
thread · nothing from memory or past chats · same-session result, **capped at CONJECTURE** (card §8, §11).

---

## 0. Digest and provenance

| item | value |
|---|---|
| card received | `raw.githubusercontent.com/zerofreeparameters-code/BCT-Programme/093506c4ed74fa39067221d113c65afd06e86642/audit/gates/gate_SONO_prompt.md`, `curl` to disk, hashed **before** reading |
| **card SHA-256** | `c1980aa78d362e423e7fd38eba76adf03d163e3b42c59b82bfc103551f917004` (17 782 B) — matches the expected digest in the run instruction and `audit/gates/PREREG_20261111_SONO.sha256` in the clone |
| `sono_deskcheck.py` SHA-256 | `d3a866724c38a52d7ceb6e30a03718e287f9b410138b237b8627884e3c464284` (2 415 B) — matches card §7; the run instruction's copy of this digest was truncated at 40 hex characters, which are a prefix match |
| pre-registration commit | `093506c4ed74fa39067221d113c65afd06e86642`, 2026-11-11 17:15:05 +1100, "Pre-register Gate SONO …" — shallow-fetched by SHA; every file below read from that tree |
| `letters/BCT_Letter110_Sonoluminescence.pdf` | `336912ed81eb2502a5766da4cb9f1688b425c5d29997ae3049dfe29e2c8f657a`, 70 509 B, 2 pp. — **matches card §4.1**; `pdftotext -layout` gives 81 lines, line numbers below as in the card |
| `audit/gates/gate_PRED2_prompt.md` | `69b7b7ea…77c9` — matches |
| `audit/gates/PRED2/gate_PRED2_RESULT.md` | `e64ddf90…6b62` — matches |
| `BCT_Volumes_Zenodo_Guide.md` (orientation) | `2ac282ed…4add` — matches |
| `BCT_Letter207_AncientGeometers.tex` (orientation) | `b6fd2b6d…ba82` — matches |
| `audit/gates/RATIO/` | present as committed (5 files); `gate_RATIO_deliverable.md` read for SC-RATIO-2 / CN-RATIO-02 only |
| arithmetic | mpmath 1.4.1, `mp.dps = 30`, 10 digits reported (card §4.5); scripts under `audit/gates/SONO/` |
| as-run prompt | `gate_SONO_prompt_asrun.md`, byte-identical to the fetched card (same digest) |

Every §4.1 hash was verified **before** any source was read. All hashes matched; nothing was re-fetched.

---

## VERDICT

**SC-SONO-1 — reproduces arithmetically, but both comparisons are against chosen numbers.** (CONJECTURE tier by the
same-session cap; the arithmetic underneath is PROVEN.)

- **Both BCT values reproduce** from the letter's own formula and inputs: r_tet/r_oct = 0.5425821166 (letter 0.5426);
  j_{1,2}/j_{1,1} = 1.830930328 (letter 1.830). Both printed errors reproduce under the convention
  Error = obs/BCT − 1 **computed from the letter's rounded printed values** (0.541/0.5426 − 1 = −0.29 % → "−0.3 %";
  1.842/1.830 − 1 = +0.66 % → "+0.65 %"). At full precision the #155 error is +0.61 %, not +0.65 %.
- **No comparison value traces to a named source with conditions matching the letter (card §4.3, §5).**
  - **#154.** The "UV cutoff around 200 nm" is traced — to the transmission cutoff of water (Barber et al. 1997, Fig. 2
    caption; Brenner, Hilgenfeldt & Lohse 2002, §V.D), i.e. a host limit, not an emission feature. The "broad peak near
    350 nm" is **not** in any pinned reference: Hiller, Putterman & Barber (1992) state that if a spectral peak exists it
    lies above 6 eV (λ < 207 nm); the 2002 review states that the apparent peak in some spectra is the water
    absorption itself. The one genuine turnover in the pinned references is xenon's "broad spectral peak" (Barber et al.
    1997, §8; wavelength not printed; the review's ab-initio calculation puts it near 336 nm). The letter names no gas,
    writes 350 nm in its text and 370 nm in its arithmetic, and 336 nm would give δ = −8.8 %.
  - **#155.** "700 nm" is traceable to a published band — the singlet-oxygen dimol emission at 703 nm (Pospíšil, Prasad &
    Rác 2014) — but as a chemiluminescence line of oxidative metabolism, not a "mitochondrial Bessel mode". "380 nm" is
    not a published band: the near-UV component of ultra-weak photon emission is the triplet-carbonyl band spanning
    350–550 nm, with no 380 nm peak reported in the reviews retrieved. No two-band 380/700 nm structure is published.
  - **Cristae ratio.** The letter gives no observed value at all, and the literature defines no "cristae spacing ratio";
    nothing can be compared.
- **Q4 fit scoring (PRED2 grammar and charges, unchanged):** raw 10.4 bits (#154) and 9.7 bits (#155) at complexity 3;
  after PRED2's look-elsewhere and this card's comparison-value charges, **net −6.0 and −9.5 bits — "unsurprising"**;
  without the comparison-value charge they are still −2.3 and −4.3 bits. The blind C ≤ 3 control lands ~10× closer to
  each "observed" ratio than the letter's expression does (cos 1 = 0.5403 for 200/370; r_oct/r_tet = 1.8430 for
  700/380).
- Q3(d): Letter 207's flash-radius statement is absent from Letter 110; its literal value (6.3 mm at 26.5 kHz) misses
  the measured SBSL radii by 10²–10⁴. Q5: nothing in the letter fixes an absolute length, time or mass.

Why not SC-SONO-5 (inconclusive): the pinned references do not merely fail to contain the comparison values; they
positively locate the SBSL "peak" at λ < 207 nm for the standard air/argon bubble, attribute apparent visible-range
peaks to water absorption, and place the near-UV biophoton band at 350–550 nm. "Untraceable" here is a finding, not an
absence of evidence — subject to the as-of-run limitation in card §10.

---

## Plain-language summary

Letter 110 says two light-emission ratios match two BCT constants to better than 1 %. The constants are computed
correctly and the percentage errors are what the letter says they are (once one notices the letter rounds first and
divides second). But the "observed" numbers the constants are compared with were not taken from any measurement the
letter names, and this run could not find them in the standard literature. For sonoluminescence, the 200 nm "cutoff" is
where water stops transmitting light, and the published spectra of the usual bubbles keep rising right up to that
cutoff — there is no peak at 350 nm to take a ratio with; the one gas that does show a broad near-UV maximum (xenon)
shows it nearer 336 nm, which would make the match 9 % off instead of 0.4 %. For biophotons, there is a known emission
band at 703 nm, but there is no known band at 380 nm; the near-UV light is a broad band from 350 to 550 nm, and the
letter's "two bands" are not a published feature. So each ratio is a constant compared with a number the letter chose.
Scored under the programme's own PRED2 grammar, both predictions come out well below the "suggestive" line even before
that choice is charged for; and a blind search of the same grammar finds closer matches than the letter's for both
numbers. Nothing in the letter fixes a size, a time or a mass, so it cannot serve as a scale bar either.

---

## Q1 — Statement and input ledgers (card §4.2)

Source for every row: the pinned Letter 110, `pdftotext -layout`, 81 lines. "none given" means the letter cites nothing;
the letter has no reference list (L1–81). The right-hand columns record what the run found (Q3) for each value.

### Prediction #154 — SBSL spectral ratio

| Symbol | Value | Dimension | Source (letter line) | Terminal inputs | Comparison value | Comparison source and conditions | Notes |
|---|---|---|---|---|---|---|---|
| λ_UV/λ_peak (BCT) | r_tet/r_oct = 0.5426 | — | L51, L58 | r_tet = (√6−2)/4 = 0.1123724357, r_oct = (√2−1)/2 = 0.2071067812 (FCC void inradii, fixed by packing: Gate RATIO CN-RATIO-02) | 0.541 (= 200/370, L53) | **none given** | recomputed 0.5425821166 |
| λ_UV | 200 nm | length | L52 | — | — | none given in letter. **Traced:** water transmission cutoff at 6 eV ≈ 200 nm (Barber et al. 1997, Fig. 2 caption, He bubble, water 0 °C, 150 mm partial pressure; instrument onset 185–190 nm, §8); "ultraviolet cutoff … about 200 nm" from absorption in water or other liquids (BHL 2002, §V.D) | **host/instrument limit, not an emission feature** |
| λ_peak | "near 350 nm" (text) / 370 nm (arithmetic) | length | L52–53 | — | — | none given. **Traced:** no maximum at 350–370 nm in any pinned reference (Q3(a)); air bubble/water: any peak above 6 eV (Hiller 1992); apparent peaks = water absorption (BHL 2002, §I.C); xenon only: "broad spectral peak", wavelength not printed (Barber 1997, §8), calculated ≈ 336 nm (BHL 2002, §V.E.2) | **untraceable at the stated wavelength; letter's own two values differ by 5.7 %** |
| "bubble collapse velocity (fraction of c)", "ambient acoustic frequency" | unspecified | — | L48–49 | named in words; no formula written | — | — | do not enter the ratio; no absolute wavelength is ever computed (Q5) |
| Error | "−0.3 %" (text L53) / "0.3 %" (table L58) | — | L53, L58 | obs/BCT − 1 from the rounded printed values: 0.541/0.5426 − 1 = −0.295 % | — | — | full precision: obs/BCT − 1 = −0.376 %; card's δ_154 = BCT/obs − 1 = **+0.378 %**; with the text's 350 nm, δ_154 = −5.05 % |

### Prediction #155 — biophoton band ratio

| Symbol | Value | Dimension | Source (letter line) | Terminal inputs | Comparison value | Comparison source and conditions | Notes |
|---|---|---|---|---|---|---|---|
| λ_1/λ_2 (BCT) | "j(2,1)/j(1,1) = 7.016/3.832 = 1.830" | — | L63, L71 | j_{1,1} = 3.83170597 (first zero of J_1, correctly labelled); "j(2,1) = 7.016" is **j_{1,2} = 7.01558667, the second zero of J_1** (j_{2,1} = 5.1356223) | 1.842 (= 700/380, L64) | **none given** | recomputed j_{1,2}/j_{1,1} = 1.830930328; 7.016/3.832 = 1.8309 (prints "1.830", a truncation) |
| λ_1 | 700 nm | length | L64 | — | — | none given. **Traced:** singlet-oxygen dimol emission band at 703 nm (and 634 nm), chemiluminescence of oxidative metabolism in cells and tissues, filter-resolved (Pospíšil, Prasad & Rác 2014; Van Wijk et al. 2020) | nearest published band 703 nm (0.4 % from 700); a chemical emitter, present in many systems, not specific to mitochondria |
| λ_2 | 380 nm | length | L64 | — | — | none given. **Traced:** no 380 nm band; near-UV component is the triplet-carbonyl band 350–550 nm (Pospíšil et al. 2014); yeast UV band 210–330 nm (Quickenden & Tilbury via Van Wijk et al. 2020); skin 470–570 nm (Van Wijk et al. 2020) | **untraceable** |
| "two spectral bands" | — | — | L61, L64 | — | — | none given. **Traced:** reviews list ≥ 6 bands/regions (350–550, 550–750, 750–1000, 634, 703, 1270 nm); no two-band 380/700 structure | the pairing is the letter's choice |
| cristae spacing ratio | "matches r_tet/r_oct = 0.5426" | — | L40 | — | **no observed value given** | none given. **Traced:** no "cristae spacing ratio" is defined in the literature; representative measured spacings: inner boundary membrane follows the outer at ~20 nm (Kühlbrandt 2015, Fig. 3); OMM–IMM centre-to-centre 12.7–13.5 nm in MEF cells (JCB 2023 surface-morphometrics paper, §9); crista junctions classified at 19–40 nm from the OMM (same) | not a prediction: no number to compare; forming a pair would be construction (card §4.6) |
| Error | "+0.65 %" (text L65) / "0.65 %" (table L71) | — | L65, L71 | obs/BCT − 1 from the rounded printed values: 1.842/1.830 − 1 = +0.656 % | — | — | full precision: obs/BCT − 1 = **+0.610 %**; card's δ_155 = BCT/obs − 1 = −0.607 % |

---

## Q2 — Reproduction (script `sono_q2_reproduce.py`, output `sono_q2_output.txt`)

| printed (line) | recomputed, 30 dps | reproduces? |
|---|---|---|
| r_tet/r_oct = 0.5426 (L40, L51, L58) | 0.5425821166 | **yes** |
| j(1,1) = 3.832 (L33) | j_{1,1} = 3.83170597 | yes, label correct |
| j(2,1) = 7.016 (L33–34) | j_{1,2} = 7.01558667; the true j_{2,1} = 5.135622302 | **value yes, label no** — second zero of J_1 under the name of the first zero of J_2 |
| j(2,1)/j(1,1) = 1.830 (L34, L63, L71) | j_{1,2}/j_{1,1} = 1.830930328; 7.016/3.832 = 1.830897704 | yes to 3 s.f.; "1.830" is a truncation of 1.8309 (rounds to 1.831) |
| (j(2,1)/j(1,1))² = 3.348 (L34) | 3.352305867; 1.830² = 3.3489 | **only from the truncated 1.830** |
| abstract: j(2,1)/j(1,1) = 3.054 (L15) | — | **no**: matches neither the ratio (1.8309), its square (3.3523), the label-literal j_{2,1}/j_{1,1} (1.3403) nor its square (1.7964); the nearest low-order Bessel-zero ratio is j_{2,3}/j_{1,1} = 3.0326 (0.7 % away) — record only |
| observed 0.541 (L53, L58) | 200/370 = 0.5405405405 | yes; **but the text's "near 350 nm" gives 200/350 = 0.5714** |
| Error −0.3 % / 0.3 % (L53 / L58) | obs/BCT − 1: −0.376 % (full), −0.295 % (rounded inputs); BCT/obs − 1 = +0.378 % | yes, as obs/BCT − 1; the table drops the sign |
| observed 1.842 (L64, L71) | 700/380 = 1.842105263 | yes |
| Error +0.65 % / 0.65 % (L65 / L71) | obs/BCT − 1: +0.610 % (full), **+0.656 % (rounded inputs 1.842/1.830)**; BCT/obs − 1 = −0.607 % | **yes only from the rounded values**; full precision gives +0.61 % |

**Sign convention the letter used:** Error = obs/BCT − 1, evaluated on the rounded printed values (both predictions
consistent). The card's §6 defines δ = BCT/obs − 1, opposite in sign; the magnitudes handed to Q4 are the
full-precision |δ|: ε_154 = 0.003777, ε_155 = 0.006066 (card: 0.38 %, 0.61 %).

Internal inconsistencies → CN-SONO-01…05 (§7).

---

## Q3 — Comparison-value audit, with sources

All four §4.4 references were located and read this session (how, and how much, in §9 Sources). The run added three
peer-reviewed sources by DOI for Q3(b)–(c), listed there.

### Q3(a) SBSL

**Is there a spectral maximum near 350–370 nm in the pinned references?** No.

- *Hiller, Putterman & Barber, PRL 69, 1182 (1992)* — air bubble in water. The abstract (publisher page) states the
  spectrum is broadband and that "if a spectral peak exists, it lies at photon energies above 6 eV", i.e. λ < 207 nm. The same group's
  contemporaneous abstract records the spectral density increasing with photon energy from above 700 nm to below
  190 nm, matching the tail of a 25 000 K blackbody.
- *Barber, Hiller, Löfstedt, Putterman & Weninger, Phys. Rep. 281, 65 (1997)* — abstract: a broadband spectrum that
  increases into the ultraviolet, with the complete spectrum unmappable above 6 eV because of water's cutoff. §10:
  the SL spectrum is generally rising at 6 eV (200 nm). Fig. 2 (⁴He, water 0 °C, 150 mm): the 6 eV (200 nm) cutoff is
  the transmission cutoff of water. §8, noble gases at room temperature and 0 °C (Figs. 54–57): helium has greater
  spectral density in the UV than xenon; the "broad spectral peak exhibited by xenon" is mentioned **without a wavelength**, and
  xenon's emission decreases as 200 nm is approached. Heavy-water H₂/D₂ spectra fit a 6000 K blackbody (Fig. 73).
  No spectrum in the paper is described with a maximum at a stated wavelength.
- *Brenner, Hilgenfeldt & Lohse, RMP 74, 425 (2002)* — §I.C (Fig. 5, Hiller 1992 data, water 22 °C, best blackbody fit
  ≈ 40 000 K): the spectrum rises toward the UV and the "apparent peak in some spectra is due to the strong absorption" of wavelengths
  below ~200 nm by the water in the flask. §V.D: UV cutoff ≈ 200 nm from absorption in water or other liquids; red end
  ≈ 800 nm where noise dominates; Fig. 40 (Barber 1997 data, Hammer & Frommhold 2001 fits): noble-gas spectra fit
  blackbody curves at 8 000–30 000 K, best-fit temperature falling with molecular weight. §V.E.2: the calculated xenon
  spectrum has a maximum near 336 nm, described as close to what is measured (Barber et al. 1997). §VI.B: the UV
  shape for light noble gases is still unknown because water absorbs there.

**Is the 200 nm cutoff an emission feature or the absorption edge of water?** The absorption edge of water (all three
references; Barber 1997 §8 adds the instrument onset at 185–190 nm). **What λ_UV/λ_peak then measures:** for the
standard air/argon/helium bubble, the "peak" is the water edge seen from the other side, so the ratio is
(water edge)/(water edge) ≈ 1 or is undefined; for xenon it is (water edge)/(gas- and temperature-dependent thermal
maximum), a number that depends on the gas, the drive and the water temperature and that the pinned references put
near 336 nm (calculated), not 350–370 nm. With 336 nm: 200/336 = 0.5952, δ_154 = −8.8 %. With the letter's own text value
350 nm: δ_154 = −5.05 %. Only the arithmetic's 370 nm gives +0.38 %. (A sentence, per §4.6: the fitted 8 000 K of Fig. 40
would place a Planck B_λ maximum at 362 nm; the review's own calculation says 336 nm; "the peak" of a broad continuum
is defined to no better than ±5 %, ten times the letter's tolerance.)

**§8 test (does a traced feature near 350–370 nm lift the comparison-value charge?):** No. The only traced turnover is
xenon's, at a wavelength the pinned references either do not print (Barber 1997) or place at ≈ 336 nm (BHL 2002), for a
gas the letter does not name. The charge stands; it would be lifted by a measured xenon maximum documented at
350–370 nm, which none of the pinned references prints.

### Q3(b) Biophotons

**Is there a published two-band structure at ~380 and ~700 nm?** No.

- *Cifra & Pospíšil, J. Photochem. Photobiol. B 139, 2 (2014)* (abstract, via the Czech National Medical Library record
  and Elsevier listing): ultra-weak photon emission is chemiluminescence from electronically excited species formed in
  oxidative metabolism and oxidative stress; spectral range near-UVA to near-IR, ~350–1300 nm; detection by low-noise
  photomultipliers and CCD imaging. No bands are enumerated in the abstract.
- *Pospíšil, Prasad & Rác, J. Photochem. Photobiol. B 139, 11 (2014), doi:10.1016/j.jphotobiol.2014.02.008* (added,
  companion review, abstract via ScienceDirect): emission regions are "triplet excited carbonyl in the near UVA and blue–green areas (350–550 nm)";
  singlet and triplet excited pigments at 550–750 nm and 750–1000 nm; singlet oxygen at 634 and 703 nm and 1270 nm.
- *Van Wijk, Van Wijk, Pang, Yang, Yan & Han, Front. Physiol. 11, 717 (2020), doi:10.3389/fphys.2020.00717* (added,
  open-access review on mitochondrial UPE): overall range 300–900 nm; mitochondria produce the majority of cellular
  UPE but no mitochondria-only spectrum is given; yeast UV band 210–330 nm and visible band 450–620 nm (Quickenden &
  Tilbury 1983, seven ~70 nm windows over 210–630 nm); dye-stressed yeast dominant band near 600 nm; human skin major
  emission 470–570 nm; singlet-oxygen dimol bands at 634 and 703 nm; excited carbonyls 350–500 nm; radical
  recombination 230–300 nm. Filter sets cited: Inaba 1988, 27 filters over 275–670 nm (30–50 nm windows below 450 nm,
  20–25 nm above); Ezzahir/Slawinski 1992, 11 windows of 20–25 nm over 470–700 nm plus three over 670–830 nm.
  The review does not mention 380 nm.

**Conditions:** every band above is a chemiluminescence assignment (triplet carbonyls from lipid peroxidation; singlet
oxygen; pigments), measured through cut-on or interference filters on whole cells, tissues or organisms; none is a
"mitochondrial Bessel mode", and no source reports mitochondria emitting two bands. The 700 nm value is near a real
band (703 nm); the 380 nm value is not a reported band.

### Q3(c) Cristae

The letter prints no observed cristae ratio (L40), so there is nothing to reproduce or score. The literature measures
individual spacings, not a ratio: inner boundary membrane ~20 nm from the outer membrane (Kühlbrandt, BMC Biol. 13, 89
(2015), Fig. 3, doi:10.1186/s12915-015-0201-x); OMM–IMM centre-to-centre 13.5 → 12.7 nm (≈ 6.5 → 5.7 nm after a ~7 nm
membrane correction), intracrista spacing changing by 1.8–5.3 nm under thapsigargin, crista junctions 19–40 nm from
the OMM, mouse embryonic fibroblasts, cryo-ET ("Quantifying organellar ultrastructure in cryo-electron tomography using a
surface morphometrics pipeline", J. Cell Biol. 222(4), e202204093 (2023)). Any pair of these could be formed into a ratio; the letter forms none. Recorded as an assertion without a
comparison value (CN-SONO-06).

### Q3(d) Letter 207's flash-radius statement

`BCT_Letter207_AncientGeometers.tex` L50–52: the flash occurs when the collapsing radius crosses "r = r_tet × λ_acoustic",
introduced with "Already solved in L110." **Confirmed absent from Letter 110:** the 81-line extraction contains no
flash-radius formula and no λ_acoustic; "acoustic" occurs only in "ambient acoustic frequency" (L49), as a named but
unused input. Literal evaluation (water, c = 1482 m s⁻¹, card §4.4; frequencies from the pinned references):

| f | λ_acoustic | r_tet × λ | vs R_max ≈ 50 µm | vs R_min ≈ 0.5 µm |
|---|---|---|---|---|
| 20 kHz | 74.1 mm | 8.33 mm | 167× | 1.7×10⁴ |
| 26.5 kHz | 55.9 mm | 6.28 mm | 126× | 1.3×10⁴ |
| 40 kHz | 37.1 mm | 4.16 mm | 83× | 8.3×10³ |

Measured SBSL radii (BHL 2002 §I.A; Barber 1997 §1, §3): R_0 ≈ 4–5 µm, R_max ≈ 40–50 µm, R_min ≈ 0.5 µm. The statement
misses by 10²–10⁴ under the literal reading. Recorded as unsupported (CN-SONO-07); not scored.

---

## Q4 — Fit scoring under PRED2's grammar and charges

### Preamble: the rule, written before any score below was computed

- **Grammar.** PRED2's, reproduced line for line from `pred2_step2_grammar.py` / `pred2_step3_score.py` (20 atoms,
  17 unary + 4 binary operations, node-count complexity, density per unit ln x in the narrowest log-window with ≥ 60
  hits at complexity exactly C_expr, P = ρ·2ε, raw bits = −log₂ P). Check: this run's re-implementation generates the
  same pools as PRED2's own module (325 / 6 782 / 158 430 values at C = 2/3/4) and the identical #154 density
  (window 0.1, 135/6726 hits, 10.37 bits) when PRED2's module is run directly.
- **Atoms.** #154 (r_tet/r_oct) is scored under PRED2's 20 atoms. #155 (j_{1,2}/j_{1,1}) is **not expressible** under
  them; PRED2's rule "add any atom the census shows the corpus using" obliges adding the Bessel zeros the letter names
  (j_{1,1}, j_{1,2}, j_{2,1}; 23 atoms). #154 is also shown under the 23-atom grammar for comparability.
- **Targets and tolerances (card §6).** T_154 = 200/370, ε_154 = |δ_154| = 0.003777; T_155 = 700/380, ε_155 = 0.006066.
  C_expr = 3 for both (atom ÷ atom).
- **Charges (PRED2 lines; floors, not estimates):**
  1. look-elsewhere over targets, log₂ 92 = **6.52 bits**, PRED2's census floor charged to every prediction (the letter's
     own numbering, #154/#155, places both inside the programme-wide census);
  2. look-elsewhere over corpus constants, **log₂ 12 = 3.58 bits**: the card's enumerated palette
     {r_tet/r_oct, r_oct/r_tet, j_{1,2}/j_{1,1}, j_{2,1}/j_{1,1}}, their inverses and squares = 12 distinct values
     (the letter demonstrably draws from both families: 0.5426 ≈ r_tet/r_oct ≈ j_{1,1}/j_{1,2} = 0.5462, and
     1.8309 ≈ j_{1,2}/j_{1,1} ≈ r_oct/r_tet = 1.8430);
  3. look-elsewhere over comparison-value pairs, log₂ C(n, 2), n = distinct wavelength features named in the traced
     sources: **#154 n = 4** {≈200 water edge / 185–190 onset (merged), 310 OH line, 336/337 (merged), ≈800 red end}
     → 6 pairs, **2.58 bits** (15 pairs, 3.91 bits, if the merged features are counted separately); **#155 n = 6**
     {carbonyl band 350–550, singlet-pigment 550–750, triplet-pigment 750–1000, 634, 703, 1270} → 15 pairs,
     **3.91 bits** (21 pairs, 4.39 bits, if band edges count as features);
  4. comparison-value ("drift") charge — the card's phrase "PRED2's comparison-value drift rule" names a Gate PRED
     *finding* (PRED §3, "same quantity, different observed value across phases"), for which neither PRED gate fixes a
     formula (CN-SONO-08). The run operationalises it in PRED2's correction-factor form (candidates available inside
     the window a choice had to close): **charge = log₂( ln(R_hi/R_lo) / 2ε )**, where [R_lo, R_hi] is the range of
     the "observed" ratio spanned by the documented drift of the chosen value — the letter's own alternatives and the
     traced sources' values for the same feature — and 2ε is the tolerance window in log-space; 0 if the quotient is
     < 1. **#154:** λ_peak documented over 336 nm (BHL 2002 calc.) to 370 nm (letter arithmetic), λ_UV held at 200 →
     ln(370/336)/(2·0.003777) = 12.8 windows → **3.67 bits**. **#155:** 700 ↔ 703 (0.4 %, within ε, no charge); 380 ↔
     the carbonyl band 350–550 nm with no reported peak → ln(550/350)/(2·0.006066) = 37.3 windows → **5.22 bits**;
  5. correction-factor / date-order charges: **0** (no post-hoc factor in either expression).
- **Also reported, as PRED practice:** under Gate PRED's own rule a comparison against a chosen value is *excluded
  from scoring*; the charge sheet is given so the reader can see the bits either way.
- **Control.** PRED2's blind inverse-symbolic control, exhaustive here at C ≤ 3: the best grammar expression for each
  target, reported as a sentence (card §4.6), not a rescoring.
- Thresholds: ≥ 10 surprising · 3–10 suggestive · < 3 unsurprising (fixed in the card).

### Charge sheets (script `sono_q4_score.py`, output `sono_q4_output.txt`)

| prediction | grammar | C | ε | p_raw | raw | LE targets | LE constants | LE pairs | comparison-value | corr. | **net** | bin |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| #154 r_tet/r_oct vs 200/370 | PRED2 20 atoms | 3 | 3.78e−3 | 7.58e−4 | 10.37 | 6.52 | 3.58 | 2.58 | 3.67 | 0 | **−6.00** | unsurprising |
| #154 r_tet/r_oct vs 200/370 | +3 Bessel zeros (23) | 3 | 3.78e−3 | 6.13e−4 | 10.67 | 6.52 | 3.58 | 2.58 | 3.67 | 0 | **−5.70** | unsurprising |
| #155 j_{1,2}/j_{1,1} vs 700/380 | +3 Bessel zeros (23) | 3 | 6.07e−3 | 1.17e−3 | 9.73 | 6.52 | 3.58 | 3.91 | 5.22 | 0 | **−9.50** | unsurprising |

Robustness, so the reader need not take the operationalised charge on trust:

| what is dropped | #154 net | #155 net |
|---|---:|---:|
| nothing (full sheet) | −6.00 | −9.50 |
| the comparison-value charge (line 4) | −2.33 | −4.28 |
| lines 2–4 (only PRED2's 6.52-bit census floor kept) | +3.84 | +3.21 |
| every charge (raw bits only) | 10.37 | 9.73 |

Even the most generous row — raw bits minus the one charge PRED2 applied to every prediction in the programme — leaves
both predictions at the bottom of the "suggestive" band, and that row ignores that the "observed" number was chosen.
Under PRED-practice (chosen comparison value → excluded from scoring) neither is scored at all.

**Control (blind, exhaustive C ≤ 3, same grammar):** for T_154 = 0.54054 the best expression is cos(cos x_lep) =
0.540340 (|ε| = 3.7e−4), with cos 1 = 0.540302 (4.4e−4) next — both ~10× closer than r_tet/r_oct (3.8e−3); five
distinct C ≤ 3 values lie inside the letter's tolerance window. For T_155 = 1.84211 the best is r_oct/r_tet = 1.843039
(|ε| = 5.1e−4), 12× closer than j_{1,2}/j_{1,1} (6.1e−3), with √3 + r_tet = 1.84442 next; seven distinct C ≤ 3 values
lie inside the window. The corpus's other "1.84" beats the letter's own choice for #155 — recorded as a look-elsewhere
illustration, as the card anticipated, not as a finding about physics.

Sensitivity to the scored complexity (same ε): #154 raw bits 10.11 / 10.37 / 7.82 at C = 2/3/4; #155 9.09 / 9.73 / 10.07.
No choice of C moves either prediction's net above 3 bits under the full sheet.

---

## Q5 — Scale (one sentence)

Nothing in Letter 110 fixes an absolute length, time or mass: both predictions are ratios of wavelengths, the
"collapse velocity (fraction of c)" and "ambient acoustic frequency" of L48–49 are named but never used in a formula,
and the only length-like statement in the corpus about this letter (Letter 207's r = r_tet × λ_acoustic) is not in it.

---

## 6. The §9 disclosure, scored item by item

| forecast (card §9) | outcome |
|---|---|
| SC-SONO-1 ~65 %, SC-SONO-2 ~30 % | **SC-SONO-1** |
| standard SBSL spectrum rises monotonically into the UV and is cut off by water near 200 nm, no maximum near 350–370 nm | confirmed from all three pinned references; refined: xenon alone shows a broad near-UV maximum, placed near 336 nm by the review's calculation, wavelength not printed by Barber et al. 1997 |
| no published 380/700 nm two-band structure; broadband UPE with system-dependent peaks | confirmed; refined: 700 nm is near a real band (703 nm, singlet-oxygen dimol), 380 nm is not |
| if both traced, SC-SONO-2 with net bits < 3 | moot; net bits are negative under the full sheet and ≤ 3.8 under any partial sheet |
| Q2: both BCT values reproduce; both errors reproduce under obs/BCT − 1 | confirmed; refined: the errors reproduce from the **rounded** printed values (full precision gives +0.61 %, not +0.65 %, for #155) |
| Q2: three CNs (350 vs 370; 3.054; the j(2,1) label) | all three recorded, plus five more (CN-SONO-04…08) |
| Q3(d): absent from Letter 110 (certain); literal value misses by 10²–10⁴ | confirmed: absent; 83–167× R_max, 0.8–1.7×10⁴ × R_min |
| Q5: no absolute scale (~99 %) | confirmed |
| interest: card framed after the BULK-thread argument that sonoluminescence is not a scale bar | the verdict code was set by Q2/Q3 (comparison clause) and does not use Q5 or Q3(d), as the card requires |

---

## 7. Correction notices

**PROVEN** (terminal-verified arithmetic, this session, 30 dps):

- **CN-SONO-01.** Letter 110 L33–34 labels the second zero of J_1 (j_{1,2} = 7.0156) as "j(2,1)". The first zero of J_2
  is 5.1356. The value used is a real Bessel zero under a nonstandard label; every downstream number uses j_{1,2}.
- **CN-SONO-02.** The abstract's "j(2,1)/j(1,1) = 3.054" (L15–16) equals neither the ratio used (1.8309), its square
  (3.3523), the label-literal ratio (1.3403), nor its square (1.7964), nor any low-order Bessel-zero ratio to better than
  0.7 %. The letter's headline constant is not one it computes anywhere.
- **CN-SONO-03.** L52 says "broad peak near 350 nm"; L53 computes 200/370. With the text's own value the error is −5.05 %
  (δ_154), not −0.3 %. The letter's two statements of its comparison value differ by 5.7 %, fifteen times its printed
  tolerance.
- **CN-SONO-04.** The printed errors are obs/BCT − 1 on the rounded printed values. For #155 full precision gives
  +0.610 %, printed as "+0.65 %" (from 1.842/1.830). The tables (L58, L71) drop the signs the text carries.
- **CN-SONO-05.** "1.830" (L34, L63, L71) is a truncation of 7.016/3.832 = 1.8309 (rounds to 1.831); "3.348" (L34) is
  1.830², not (j_{1,2}/j_{1,1})² = 3.352.

**ASSERTED** (recorded from sources read this session; the sources, not this run, establish them):

- **CN-SONO-06.** L40's "cristae spacing ratio matches r_tet/r_oct" states no observed value and names no measurement; no
  "cristae spacing ratio" is defined in the structural literature retrieved. It is an assertion, not a prediction.
- **CN-SONO-07.** Letter 207 L50–52 attributes to Letter 110 a flash-radius formula r = r_tet × λ_acoustic that Letter 110
  does not contain; evaluated literally it exceeds measured SBSL radii by 10²–10⁴.
- **CN-SONO-08 (card defect, recorded not force-fitted).** Card §2 Q4 and §3 cite "PRED2's comparison-value drift
  rule". The phrase occurs in Gate PRED's deliverable (§3), not PRED2's, and there as a finding without a scoring
  formula. This run fixed an operationalisation before scoring (Q4 preamble) and reports net bits with and without it.
- **CN-SONO-09.** The "UV cutoff around 200 nm" of #154 is the transmission cutoff of water (host limit); for the
  standard air/argon/helium bubble the pinned references report no emission maximum above it. λ_UV/λ_peak as written
  compares the host's absorption edge with a feature the references attribute to that same edge.
- **CN-SONO-10.** "Primary bands near 380 nm and 700 nm" (#155): 700 nm lies 0.4 % from the published singlet-oxygen
  dimol band at 703 nm; 380 nm corresponds to no published band (the near-UV emission is the 350–550 nm triplet-carbonyl
  band). No two-band structure is published for mitochondrial or cellular emission in the sources retrieved.

**CONJECTURE** (model-dependent on PRED2's grammar and the charge schedule; same-session cap):

- **CN-SONO-11.** Under PRED2's grammar and charges, #154 nets −6.0 bits and #155 −9.5 bits; without any comparison-value
  charge, −2.3 and −4.3; with only PRED2's census floor, +3.8 and +3.2. No reading reaches "surprising".
- **CN-SONO-12.** A blind C ≤ 3 search of the same grammar lands ~10× closer than the letter's expression to each
  "observed" ratio (cos 1 for 200/370; r_oct/r_tet for 700/380).
- **CN-SONO-13.** `BCT_Volumes_Zenodo_Guide.md` L40 should stop describing #154 and #155 as errors of −0.3 % and +0.65 %
  against observation: the "observed" numbers are the letter's own, and the traced features give −5 % to −9 % (#154)
  or no feature at all (#155, 380 nm).

---

## 8. What this gate did **not** establish

- It did not test the OHC/Bessel framework, Gate J or Gate BUBBLE_BELLS, nor assess "OHC relaxation" as a mechanism
  (card §3, §8). It did not adjudicate the physics of sonoluminescence or of biophotons.
- It did not show that no SBSL spectrum anywhere has a maximum at 350–370 nm; it showed that none of the pinned
  references reports one, that the one reported turnover (xenon) is elsewhere, and that the letter names no gas,
  liquid, temperature or drive. "Untraceable" is as-of-run (card §10).
- It did not search for a better wavelength pair or a better corpus constant (card §4.6); the control results are
  PRED2's standard check and are reported as sentences.
- It did not score the cristae statement or Letter 207's flash radius; neither has a comparison value.
- The drift-charge formula is this run's operationalisation of a rule the card names but no prior gate defines; the
  robustness table shows the verdict does not depend on it.
- Nothing here is a scale test; that was closed by Gate BULK and is re-examined by Gate PQCD.

---

## 9. Sources — what was read, and how

**Pinned (card §4.4), all located:**
- Brenner, Hilgenfeldt & Lohse, *Rev. Mod. Phys.* 74, 425 (2002), doi:10.1103/RevModPhys.74.425 — full text read in
  four passes from a university-hosted copy (fluid.dtu.dk; the Twente repository copy was refused by the session's
  egress proxy). §§I.A, I.C, III, IV, V.B–V.G, VI.B and the reference list.
- Barber, Hiller, Löfstedt, Putterman & Weninger, *Phys. Rep.* 281, 65 (1997), doi:10.1016/S0370-1573(96)00050-6 — full
  text read in two passes from a course-hosted copy (sfu.ca). Abstract, §§1, 3–5, 7, 8, 10; Figs. 1, 2, 51–59, 62, 73–75.
- Hiller, Putterman & Barber, *Phys. Rev. Lett.* 69, 1182 (1992), doi:10.1103/PhysRevLett.69.1182 — abstract only
  (publisher page via link.aps.org; full text paywalled), plus the group's ASA 1992 meeting abstract (auditory.org).
- Cifra & Pospíšil, *J. Photochem. Photobiol. B* 139, 2 (2014), doi:10.1016/j.jphotobiol.2014.02.009 — abstract only
  (Czech National Medical Library record, PMID 24726298; full text paywalled).

**Added by DOI for Q3(b)–(c) (card §4.4 permits):**
- Pospíšil, Prasad & Rác, *J. Photochem. Photobiol. B* 139, 11 (2014), doi:10.1016/j.jphotobiol.2014.02.008 — abstract
  (ScienceDirect).
- Van Wijk, Van Wijk, Pang, Yang, Yan & Han, *Front. Physiol.* 11, 717 (2020), doi:10.3389/fphys.2020.00717 — full text,
  first 100 000 characters (PMC7360823).
- Kühlbrandt, *BMC Biol.* 13, 89 (2015), doi:10.1186/s12915-015-0201-x — Fig. 3 caption (via search-result text; the
  PMC figure page returned a CAPTCHA).
- "Quantifying organellar ultrastructure in cryo-electron tomography using a surface morphometrics pipeline",
  *J. Cell Biol.* 222(4), e202204093 (2023) — full text, first 100 000 characters (rupress.org); neither the author list
  nor the DOI was shown on the page read, so the paper is cited by title and article ID.

**Corpus (pinned commit):** Letter 110 (pdftotext); `gate_PRED2_prompt.md`; `gate_PRED2_RESULT.md`;
`pred2_step2_grammar.py`, `pred2_step3_score.py`, `scores_raw.txt`; `gate_PRED_RESULT.md` §3 and `gate_PRED_prompt.md`
§1 (to locate the "comparison-value drift" phrase; nothing else from those files was used); `gate_RATIO_deliverable.md`
(SC-RATIO-2, CN-RATIO-02); `BCT_Volumes_Zenodo_Guide.md` L38–42; `BCT_Letter207_AncientGeometers.tex` L44–56.

**Water sound speed** 1482 m s⁻¹ at 20 °C, card §4.4.

---

## 10. Contamination statement

- No memory was available or used (the session reports memory disabled); no past chat was searched or referenced.
- The Project's document list (file names and one-line labels only) was visible in the session context, including
  names such as `gate_BULK_RESULT.md`, `gate_SONO_prompt.md`, `sono_deskcheck.py`, `gate_CRIT*`, `gate_SPECTRUM*`,
  `gate_PQCD_prompt.md`. **None was opened.** Everything read came from the clone at `093506c4` or from the web sources
  in §9.
- Nothing numerical was inherited: every corpus value was recomputed from the printed expression; every literature
  value is cited to the page where it was read.
- The card's §7 desk-check numbers were reproduced, not copied: `sono_deskcheck.py` was run and its output is committed
  (`deskcheck_output.txt`).

---

## 11. Ledger entry (for `audit/NEXT.md`, not applied by this run)

> **Gate SONO — run and closed 12 Nov 2026, SC-SONO-1 (CONJECTURE, same-session cap).** Letter 110's #154 and #155
> reproduce arithmetically (printed errors are obs/BCT − 1 on rounded values); neither comparison value traces to a
> measurement: the 200 nm "cutoff" is water's absorption edge, no pinned SBSL spectrum peaks at 350–370 nm (xenon's broad
> maximum is near 336 nm), and 380 nm is not a published biophoton band (703 nm is). Under PRED2's grammar and charges
> both net negative bits; a blind C ≤ 3 search beats both expressions ~10×. CN-SONO-01…13. Not a scale test.

---

*Scripts: `sono_q2_reproduce.py`, `sono_q4_score.py` (plus the card-thread `sono_deskcheck.py`, unchanged).
Outputs: `deskcheck_output.txt`, `sono_q2_output.txt`, `sono_q4_output.txt`, `pred2_grammar_crosscheck.txt`.
As-run prompt: `gate_SONO_prompt_asrun.md`, byte-identical to the pre-registered card (digest in §0).
Gate SONO closed by Claude (Fable 5.1), 12 November 2026.*
