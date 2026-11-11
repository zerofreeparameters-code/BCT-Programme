# Gate SONO — pre-registration card

**Programme:** BCT Cold Ledger
**Card written:** 11 November 2026, Claude (Fable 5.1), at Michel's request ("both pls"), in the Gate BULK thread after
BULK closed; the draft of 12:11 AEDT was completed once Michel attached Letter 110 (12:25 AEDT).
**Status:** PRE-REGISTERED, NOT RUN. No comparison value has been traced, nothing has been scored.
**Type:** a reproduction-and-fit audit of two ratio claims. Not a scale test (§1, last paragraph).
**Depends on:** Gate PRED2 (grammar, charge schedule, thresholds; `audit/NEXT.md` lists per-prediction fit scoring as
the method of record), Gate PLASMOID (sonoluminescing-bubble data treated as secondary evidence only;
CN-PLASMOID-14/15), Gate BULK (closed; this is the "Letter 110's ratio claim tested on its own terms" named in the
BULK thread), Gate RATIO (r_oct/r_tet = 1.8430 is a fixed FCC constant, SC-RATIO-2).

---

## 1. Background (stated, not a result of this card)

**The source.** BCT Letter 110, "The Vacuum Speaks: Sonoluminescence and Biophoton Emission as OHC Bessel Relaxation",
23 March 2026, DOI 10.5281/zenodo.19177501, two pages, added to the repository by the pre-registration commit as
`letters/BCT_Letter110_Sonoluminescence.pdf` (§4.1). Extracted with `pdftotext -layout` it is 81 lines; line numbers
below refer to that extraction.

**What it claims, verbatim.**

- Abstract (L15–16): "BCT predicts both spectra from the OHC Bessel resonance ratio j(2,1)/j(1,1) = 3.054 with zero
  free parameters."
- §2 (L33–34): "The fundamental mode is j(1,1) = 3.832 (first zero of J_1), with the second mode j(2,1) = 7.016.
  Their ratio is j(2,1)/j(1,1) = 1.830, and the energy ratio is (j(2,1)/j(1,1))^2 = 3.348."
- §2 (L40): "Mitochondrial cristae spacing ratio matches r_tet/r_oct = 0.5426."
- **Prediction #154** (L47–53, table L57–58): "The SBSL spectral peak wavelength is determined by the OHC j(1,1) Bessel
  mode energy scaled by the bubble collapse velocity (fraction of c) and the ambient acoustic frequency. BCT predicts
  the spectral peak ratio between the UV cutoff and visible peak: lambda(UV)/lambda(peak) = r_tet/r_oct = 0.5426.
  Observed SBSL spectra show a UV cutoff around 200 nm and a broad peak near 350 nm, giving ratio 200/370 = 0.541.
  BCT prediction: 0.5426. Error: −0.3%."
- **Prediction #155** (L60–65, table L70–71): "lambda(1)/lambda(2) = j(2,1)/j(1,1) = 7.016/3.832 = 1.830. Observed
  biophoton emission shows primary bands near 380 nm and 700 nm. Ratio: 700/380 = 1.842. BCT prediction: 1.830.
  Error: +0.65%."
- No source is cited for "UV cutoff around 200 nm", "broad peak near 350 nm", "primary bands near 380 nm and 700 nm",
  or the cristae spacing ratio. The letter has no reference list.

**What the repository says about it** (orientation only, not sources for Q1–Q4): `BCT_Volumes_Zenodo_Guide.md` L40
("Predictions #154 (spectral ratio 0.5426, error −0.3%) and #155 (biophoton band ratio 1.830, error +0.65%)");
`BCT_Letter207_AncientGeometers.tex` L50–52 ("The flash occurs when the collapsing bubble radius crosses the OHC
Bessel node at r = r_tet × λ_acoustic") — a statement that **does not occur in Letter 110** (§7).

**Mainstream context the run may use** (references pinned by DOI in §4.4, to be fetched and recorded): single-bubble
sonoluminescence in water at ~20–40 kHz has ambient bubble radius of a few µm, maximum of tens of µm and minimum of
order 0.5 µm; the emitted spectrum is continuous, consistent with thermal radiation from a transient plasma at
~10⁴ K, and in water is cut off below ~200 nm by the water's own absorption (Brenner, Hilgenfeldt & Lohse, Rev. Mod.
Phys. 74, 425 (2002); Barber, Hiller, Löfstedt & Putterman, Phys. Rep. 281, 65 (1997); Hiller, Putterman & Barber,
Phys. Rev. Lett. 69, 1182 (1992)). Whether any published SBSL spectrum shows "a broad peak near 350 nm" is Q3, not a
premise. Ultraweak photon emission from cells is broadband (roughly 350–1300 nm in reviews such as Cifra & Pospíšil,
J. Photochem. Photobiol. B 139, 2 (2014)); whether "primary bands near 380 nm and 700 nm" is a published feature is
Q3. This gate does not adjudicate the mechanism of either phenomenon.

**Why this is not a scale test.** Both predictions are ratios of wavelengths; the letter gives no formula for any
wavelength itself (L48–49 describes one in words, with "collapse velocity" and "acoustic frequency" as inputs, and
never writes it). Nothing here can fix a length in metres; that question was closed by Gate BULK and is re-examined
for its one remaining candidate by Gate PQCD.

## 2. Question

1. **Statement and ledger (Q1).** From the pinned letter: the formula, inputs and comparison value of #154 and #155,
   in the §4.2 ledger. For each comparison value — 200 nm, "350 nm"/370 nm, 380 nm, 700 nm, and the cristae ratio —
   record what the letter gives as its source (nothing) and what the run can find in the §4.4 references or in
   peer-reviewed literature retrieved by DOI: the quantity, its conditions (liquid, gas, drive frequency, temperature;
   cell type and measurement band), and whether it is a measured emission feature or an instrument/host limit.
2. **Reproduction (Q2).** Recompute r_tet/r_oct, j_{1,2}/j_{1,1} and the letter's "observed" ratios at full precision;
   report each printed value, each printed error, and the sign convention the letter used. Record the letter's own
   inconsistencies (§7) as CNs.
3. **Comparison-value audit (Q3).** (a) SBSL: in the pinned references, is there a spectral maximum near 350–370 nm
   for any gas/liquid condition, or does the spectrum rise monotonically to the water cutoff? Is the 200 nm cutoff an
   emission feature or the absorption edge of water? If the latter, state what "λ_UV/λ_peak" measures. (b) Biophotons:
   is there a published two-band structure at ~380 and ~700 nm for mitochondrial or cellular emission, and under what
   filter set? (c) Cristae: any measured spacing ratio in the literature that the letter's 0.5426 could be compared to.
   (d) Letter 207's flash-radius statement: confirm it is absent from Letter 110; evaluate it once under the literal
   reading (drive wavelength in water) against the measured SBSL radii, for the record only.
4. **Fit scoring (Q4).** Score #154 and #155 under PRED2's pinned grammar and charges: raw bits for the printed
   tolerance (0.38 % for #154 at 200/370; 0.61 % for #155); look-elsewhere over the comparison values available (for a
   continuous spectrum with one cutoff and one claimed peak, and for a broadband emission with several reported bands,
   the run enumerates the wavelength pairs a reader could have formed) and over the corpus constants near each target
   (r_tet/r_oct, r_oct/r_tet, j_{1,2}/j_{1,1}, j_{2,1}/j_{1,1}, their squares and inverses — note r_oct/r_tet = 1.8430
   sits 0.05 % from the letter's "observed" 1.842); comparison-value charge where the "observed" number is a round
   figure chosen in the letter (PRED2's comparison-value drift rule); net bits and bin.
5. **Scale (Q5, one sentence).** Confirm that no quantity in the letter fixes an absolute length, time or mass
   without an external scale.

## 3. Choices made by the analyst, and what they cost

- The claim is the pinned letter's text; the repository's summaries and Letter 207 are orientation and are not
  scored. Cost: Letter 207's flash statement is recorded as unsupported (CN), not tested as a BCT claim.
- A comparison value counts as measured only with a named source and stated conditions (§4.3); the letter supplies
  none, so every comparison value starts as a choice and is charged as one unless the run finds a source that matches
  the letter's number and conditions. Cost: a real feature with an unnamed source is charged as if chosen; the run
  records the source if found and lifts the charge.
- Grammar and charges are PRED2's, unchanged.
- The UV cutoff is treated as what the references say it is (expected: water absorption). Cost: if a reference shows
  an emission cutoff independent of the host, the run says so and the ratio is scored as a genuine feature pair.
- Out of scope: biology of biophotons; mechanism of sonoluminescence; the OHC/Bessel framework itself (Gates J,
  BUBBLE_BELLS); any claim in Letters 204/207 beyond the quoted paraphrase.

## 4. Fixed rules

**4.1 Sources, pinned.** Repository zerofreeparameters-code/BCT-Programme. The letter is added by the pre-registration
commit (its hash is fixed here and is verified against the committed file); every other file is pinned at
`28e6d3015c1b33a2b91233b2cc419bd08c76e4d6`. SHA-256 (verify before reading):

| File | SHA-256 |
|---|---|
| `letters/BCT_Letter110_Sonoluminescence.pdf` (70,509 B, 2 pp.; at the pre-registration commit) | 336912ed81eb2502a5766da4cb9f1688b425c5d29997ae3049dfe29e2c8f657a |
| `audit/gates/gate_PRED2_prompt.md` (grammar and charge schedule) | 69b7b7ea242146581cc05cd4e6b08257e2d29794d29b43f8d02e117bd20477c9 |
| `audit/gates/PRED2/gate_PRED2_RESULT.md` | e64ddf90cb8ad1c2b907c8ee16069b40258f2724fbfcbf73926a4114626c6b62 |
| `BCT_Volumes_Zenodo_Guide.md` (orientation only) | 2ac282ed3e93b0b0a3e61ed1d0912e9f273860f04ce3a071690e782a18234add |
| `BCT_Letter207_AncientGeometers.tex` (orientation only) | b6fd2b6d01d8af6ee104fd60d79218f6ff48aa41c4688b0c0ac43e3f6aa1ba82 |
| `audit/gates/RATIO/` (directory, as committed; for r_oct/r_tet) | — |

**4.2 Input ledger.** One table per prediction, columns: Symbol | Value | Dimension | Source (letter line) | Terminal
inputs | Comparison value | Comparison source and conditions (or "none given") | Notes.

**4.3 What counts as a measured comparison value.** A number with a named peer-reviewed source outside the corpus and
stated conditions. A round figure given only as "observed" in the letter is a choice and is charged as one in Q4.

**4.4 References (DOIs; the run fetches and records what they give).** Brenner, Hilgenfeldt & Lohse, Rev. Mod. Phys.
74, 425 (2002), doi:10.1103/RevModPhys.74.425; Barber, Hiller, Löfstedt & Putterman, Phys. Rep. 281, 65 (1997),
doi:10.1016/S0370-1573(96)00050-6; Hiller, Putterman & Barber, Phys. Rev. Lett. 69, 1182 (1992),
doi:10.1103/PhysRevLett.69.1182; Cifra & Pospíšil, J. Photochem. Photobiol. B 139, 2 (2014),
doi:10.1016/j.jphotobiol.2014.02.009. The run may add peer-reviewed sources retrieved by DOI for Q3(b)–(c), listing
each. Water sound speed 1482 m s⁻¹ at 20 °C for Q3(d).

**4.5 Arithmetic.** mpmath, 30 digits working, 10 reported. Scripts under `audit/gates/SONO/`.

**4.6 No construction.** No new formula, comparison value, band assignment or definition of λ_acoustic. If the run
sees a published feature pair that the letter's ratio would match better, that is a sentence, not a rescoring.

## 5. Verdict codes

- **SC-SONO-0 (unposable).** The letter's two predictions cannot be located in the pinned file. Not expected.
- **SC-SONO-1 (does not reproduce, or comparison untraceable).** A printed BCT value or error does not follow from the
  letter's own formula and inputs, **or** a comparison value cannot be traced to a named source with conditions
  matching the letter's description (in particular: no published SBSL spectrum with a maximum near 350–370 nm; no
  published 380/700 nm two-band biophoton structure). The ratio is then a comparison against a chosen number.
- **SC-SONO-2 (reproduces; fit).** Both reproduce; comparison values traceable; Q4 nets < 3 bits for both.
- **SC-SONO-3 (reproduces; suggestive).** As 2 with 3–10 net bits for at least one.
- **SC-SONO-4 (reproduces; surprising).** As 2 with ≥ 10 net bits for at least one. CONJECTURE; opens a mechanism
  card.
- **SC-SONO-5 (inconclusive).** Present but untraceable within the pinned sources and the §4.4 references.

Q1–Q4 are reported whatever the code. The Q3(d) line (Letter 207) and Q5 do not set the code.

## 6. The scoring rule (fixed here, before the run)

    δ_154 ≡ (r_tet/r_oct) / (λ_UV/λ_peak)_obs − 1,   δ_155 ≡ (j_{1,2}/j_{1,1}) / (λ_1/λ_2)_obs − 1,

with the "obs" ratio taken from the letter's printed numbers for Q2 and from the traced sources for Q3/Q4. PRED2's
thresholds: ≥ 10 bits surprising, 3–10 suggestive, < 3 free.

## 7. Validation already done (why the card is not blind to the arithmetic)

In the card-writing thread, 11 November 2026, `sono_deskcheck.py` (SHA-256
d3a866724c38a52d7ceb6e30a03718e287f9b410138b237b8627884e3c464284, 2415 B; committed alongside this card under
`audit/gates/SONO/`), mpmath at 30 digits:

- r_tet/r_oct = 0.5425821166; r_oct/r_tet = 1.843038997.
- The letter's "j(2,1) = 7.016" is j_{1,2} = 7.01558667, the **second zero of J_1**; the first zero of J_2 is
  j_{2,1} = 5.1356223. The value used is a real Bessel zero under a nonstandard label; j_{1,2}/j_{1,1} = 1.830930328
  (letter 1.830), squared 3.3523 (letter prints 3.348, the square of the rounded 1.830). The abstract's
  "j(2,1)/j(1,1) = 3.054" matches neither the ratio nor its square (CN to be recorded).
- #154: the text says "broad peak near 350 nm" and then computes 200/370; 200/370 = 0.540541 and the BCT value is
  +0.378 % above it (the letter prints −0.3 %, i.e. obs/BCT − 1 = −0.376 %); with 350 nm the discrepancy is −5.05 %.
- #155: 700/380 = 1.842105; BCT/obs − 1 = −0.607 % (letter prints +0.65 %: sign convention is obs/BCT). The corpus's
  other "1.83", r_oct/r_tet = 1.8430, lies 0.05 % from 1.842 — recorded as a look-elsewhere illustration, not a
  finding.
- Letter 207's "r = r_tet × λ_acoustic" is absent from Letter 110. Literal orientation value: water at 26.5 kHz,
  λ = 55.9 mm, r_tet × λ = 6.28 mm, against SBSL radii of 0.5–50 µm.
- Nothing about the comparison values was traced; no reference was opened; nothing was scored.

## 8. No-fit clause

- No comparison value, tolerance, grammar or charge rate may be changed after the run starts.
- If a traced spectrum has a feature near 350–370 nm or bands near 380/700 nm, that lifts the comparison-value
  charge for that prediction; it does not change the look-elsewhere count.
- The run scores the two ratios the letter printed. It does not search for a better pair of wavelengths or a better
  corpus constant (§4.6).
- The OHC/Bessel framework, Gate J and Gate BUBBLE_BELLS are not reopened; "OHC relaxation" as a mechanism is not
  assessed.
- Same-session results are capped at CONJECTURE.

## 9. Analyst's disclosure

- **Forecast: SC-SONO-1, about 65 %; SC-SONO-2, about 30 %.** The letter cites no source for any comparison value;
  the standard SBSL spectrum in water (argon) rises monotonically into the UV and is cut off by water absorption near
  200 nm, with no reported maximum near 350–370 nm — if the run confirms that from the pinned references, #154 compares
  a host-absorption edge to a feature that is not there, which is SC-SONO-1 by the comparison clause. For #155 the
  analyst does not know of a published 380/700 nm two-band structure; broadband UPE reviews give a wide range with
  system-dependent peaks. If the run finds sources for both, the forecast is SC-SONO-2 with net bits < 3: each ratio
  is a one-constant match at 0.4–0.6 % against a comparison value chosen from several available, with PRED2's
  look-elsewhere and comparison-value charges.
- **Q2 forecast:** both BCT values reproduce; both printed errors reproduce under obs/BCT − 1; three CNs (350 vs 370;
  3.054; the j(2,1) label).
- **Q3(d) forecast:** absent from Letter 110 (certain); literal value misses the measured radii by 10²–10⁴.
- **Q5 forecast:** no absolute scale (~99 %).
- **Interest.** The analyst wrote this card in the BULK thread after arguing, in that thread, that sonoluminescence
  cannot serve as a scale bar; the card is framed accordingly, and §1's last paragraph is that argument restated. The
  verdict codes do not depend on it.

## 10. Known limitations (stated in advance)

- The letter's comparison values may come from a source the run cannot retrieve; "untraceable" is as-of-run.
- SBSL spectra depend on gas, liquid, temperature and drive; "the" spectrum is a family. The run reports what the
  pinned references show for water with noble gases and does not generalise beyond them.
- Biophoton spectra are instrument- and system-dependent; a two-band structure in one preparation does not establish
  a general feature. The run records conditions with any source it finds.
- PRED2's grammar and charges are inherited with their limitations.

## 11. Run protocol

- Fresh thread inside the BCT Project. Before opening it, switch off "Search and reference past chats" and "Generate
  memory from chats" in Settings; switch them back on after the run. One gate per thread.
- Fetch this card by commit-pinned raw URL with curl to disk; `shasum -a 256` (or `sha256sum`) it there and compare with
  `audit/gates/PREREG_20261111_SONO.sha256` **before reading it**. Record the digest and the commit.
- `git clone --depth 1` the repository at the pre-registration commit; verify the letter's hash and every other §4.1
  hash (the others at 28e6d30 are unchanged by the pre-registration commit) before reading any source. Extract the
  letter with `pdftotext -layout`.
- Build the Q1 ledger first, Q2 second, Q3 third, Q4 fourth, Q5 last.
- Deliverable: `audit/gates/SONO/gate_SONO_RESULT.md` with the ledgers, the reproduction table, the Q3 audit with
  sources, the Q4 charge sheets, the verdict code, the §9 disclosure scored item by item, correction notices
  CN-SONO-nn, and a plain-language summary; the scripts; and a copy of the as-run prompt. The session cannot push, so
  the deliverable comes back as a `git format-patch` bundle for Michel to apply.
- Same-session results are capped at CONJECTURE.
