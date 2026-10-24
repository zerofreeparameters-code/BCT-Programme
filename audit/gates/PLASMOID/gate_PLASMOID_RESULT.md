# GATE PLASMOID — RESULT

**Quantised sizes, or a smooth spread?** Prediction #162 (Letter 114): plasmoid diameters cluster on
D_n = D_0 · (j₁,₁/j₀,₁)^(n−1), step ratio 1.5934, width σ < 10 %.

Run 24 October 2026, fresh thread. Repo `zerofreeparameters-code/BCT-Programme` at commit
`501ea793df505442375a3065a64a0c0e87189ee0`.

---

## 0 — Digest

The card was received as a file at the commit-pinned `raw.githubusercontent.com` URL, downloaded
with `curl` to disk, and hashed **before** it was read.

| Item | Value |
|---|---|
| File | `audit/gates/gate_PLASMOID_prompt.md` |
| Size | 8,897 bytes |
| SHA-256 (downloaded) | `5a13857e63faa0be392c628cd5c756f34ec794d8bde99aec4214fefdff06f7b4` |
| SHA-256 (pre-registered, `PREREG_20261024_PLASMOID.sha256`) | `5a13857e63faa0be392c628cd5c756f34ec794d8bde99aec4214fefdff06f7b4` |
| SHA-256 (repo copy at 501ea79) | identical |

**Match.** The as-run prompt is filed byte-for-byte as `gate_PLASMOID_prompt_asrun.md`.

---

## 1 — Search-space coverage (reported before any conclusion)

Every dataset searched for, with the outcome. "In-session" means reachable from this run: the
shell had no route to publisher, arXiv, Zenodo or PMC hosts, so papers were read through the
session's web-fetch tool, which cannot return binary files or figure images.

### 1a — The card's starting list, updated

| Tag | Dataset | Kind | Status found, 24 Oct 2026 | Used? |
|---|---|---|---|---|
| A | Keul 2021, *Hist. Geo Space Sci.* 12, 43–56 | Ball lightning, professional observers, 41 cases | **Found, public (CC BY 4.0).** Correction: Table 1 (and its XLSX) is a **binned contingency table** — four size bins summing to 28 — not per-case data. Per-case sizes exist only in the narrative case abstracts. 22 core cases state an explicit number with a length unit (+2 Section-6 notable cases). See CN-PLASMOID-04. | **Pilot A** (eyewitness → exploratory) |
| B | Keul & Stummer 2002, *Int. J. Meteorol.* 27(274), 385–393 | Ball lightning, 405 Central European reports (150 + 103 + 152 from three data banks) | **Not obtained.** No online copy found; no size statistics in any citing source reached. The card's summary "median 25–30 cm, mode 30 cm" could not be traced to the primary source (declared in §7). | No |
| C | Smirnov / Bychkov / Stakhanov data banks | Ball lightning, ~1,750 descriptions in the Stakhanov–Bychkov–Keul bank | **Not public.** Smirnov 1994 (*Phys.-Usp.* 37, 517) describes the banks but gives no diameter table. On request only. | No |
| D | Water-discharge ("Gatchina-type") plasmoids: IPP/HU Berlin, TU Eindhoven, Illinois, Texas State, St Petersburg | Laboratory, ~10–20 cm, ~0.3 s | **No published size distribution found.** Checked: IPP press release (2006: "10 to 20 cm", one shot per ~5 min); Juettner et al. ICPIG 2007 abstract (metadata only); Dubowsky 2015/2016 papers and prospectus (single value "approximately twenty cm"; shot-to-shot variation noted only qualitatively); Rose 2018 thesis (same; diameter not tabulated); Stephan et al. GEC 2012 abstract (no sizes); Fantz et al. 2013 *J. Appl. Phys.* 114, 043302 (paywalled, not checked). | No |
| E | Zhou et al. 2026, *Nat. Photon.* 20, 727–733, doi:10.1038/s41566-026-01899-y | Laboratory, laser-driven relativistic THz soliton, ~0.4 mm, ~100 ns | **Paper confirmed.** Public page: "millimetre-scale" in the abstract, 400 µm in the standfirst; no shot count or size distribution in visible text. Supplementary PDF and figshare source data (doi:10.6084/m9.figshare.31396380) exist but were **not reachable in-session**. | No |
| F | Sonoluminescing-bubble size distributions, pulsed fields (Melbourne: Lee et al. 2005 *JACS* 127, 16810; Brotchie, Grieser & Ashokkumar 2009 *PRL* 102, 084302) | Cavitation bubbles, µm | **Found, paywalled.** Distributions are inferred (pulse-enhancement method), published as figures. Figures could not be retrieved or digitised in-session. Bubbles, not plasmoids: secondary/pilot only whatever happens. | No |

### 1b — Extensions from this run's own search

| Tag | Dataset | Kind | Status | Used? |
|---|---|---|---|---|
| A2 | **Beatty collection**, New Mexico Tech ball-lightning report site (R. Sonnenfeld) | Ball lightning, eyewitness, 79 reports indexed | **Found, public.** Reports 1–58 readable; 59–79 present only as index entries in the PDF as served; report 49 confidential. 29 reports give a usable size (10 numeric, 19 regulation sports balls). | **Pilot A2** (eyewitness → exploratory) |
| G | Rayle 1966, NASA TN D-3188 | Ball lightning, eyewitness, 112 reports | **Found, public.** Diameters coded into ~9 questionnaire bins (bin labels illegible in the OCR as served); text reports a log-normal fit, median ≈ 14 in, spread ≈ factor 2.5, and an observer example "10 inches, give or take a factor of two". Bins far wider than P₀. | No (binned; unusable at P₀) |
| H | NMT site — outdoor, indoor (New York), indoor (Japan) report pages | Eyewitness | One report each; no numeric diameters. | No |
| I | Obreschkow et al., *Cavitation Bubble Data (Parabolic Flights, 2010)*, Zenodo doi:10.5281/zenodo.5733740 (CC BY 4.0) | 247 single laser/spark-generated cavitation bubbles, raw high-speed video | **Found; not obtainable in-session** (12.6 GB of zipped video; shell cannot reach Zenodo). Would not qualify: bubbles, variable gravity, and bubble size is set by the deposited energy (an apparatus setting). | No |
| J | Senegačnik et al. 2021, Mendeley Data doi:10.17632/w8mpz3v3w2.1 | Laser-induced cavitation bubbles over an edge | Found; bubble dynamics, energies varied 10–55 mJ; no fixed-condition size population. | No |
| K | Paiva et al. 2007, *PRL* 98, 048501 (silicon arc "luminous balls"); Dikhtyar & Jerby 2006 / Jerby 2008 (microwave fireballs) | Laboratory | Abstracts/papers reached report no size distribution over many events (Jerby: nanoparticle sizes only). | No |
| L | Small-scale magnetic flux-rope catalogues (e.g. Wind, Hu et al. 2018 *ApJS* 239, 12 on VizieR) | Space-plasma "plasmoids" | Identified; **outside the card's scope** (question names laboratory plasmoids, ball lightning and cavitation bubbles) and not fixed conditions. Not pursued. | No |
| M | Single-event papers: Sello 2011 (arXiv:1102.2829, one video event ~3–4 cm); Gunther (arXiv:2204.08288, one event ~30 cm); Keul 1999 *J. Meteorol.* 24, 178 (two cases) | Eyewitness / video | Single events; not distributions. | No |

**Coverage verdict: no qualifying dataset** (instrument-measured, ≥ 100 events, fixed conditions,
raw values) was obtainable. Every dataset actually scored is eyewitness.

---

## 2 — Verdict

**SC-PLASMOID-3 — HALT.** No qualifying dataset is obtainable. Pilot results below are exploratory
only. **#162 is neither supported nor refuted.**

Within the pilots:

- **Pilot A (Keul 2021, n = 22):** no clustering at P₀. R = 0.088, heaping-aware p = 0.85.
- **Pilot A2 (Beatty collection, n = 29): SC-PLASMOID-4 — artefact.** A naive uniform-phase Rayleigh
  test at P₀ gives p = 5.8 × 10⁻⁵ — an apparent "signal". The heaping-aware null explains it
  completely (p = 0.11): 13 of 29 reports are "basketball", "soccer ball" or "volleyball", all at
  21–24 cm. The R5 preferred-number step scores higher than #162's own ratio (0.59 vs 0.56).
  **The steelman against #162 succeeds here, and that is the headline pilot finding.**

**SC-PLASMOID-5 — open.** Stenhoff 1999 could not be read in-session (paywalled, no preview; Letter 114
gives no page number). The claim is neither confirmed nor corrected; it is **not inherited**
(CN-PLASMOID-11, data request R1).

SC-1 and SC-2 are not triggered (they need a qualifying dataset).

---

## 3 — Section 1: the arithmetic (`step0_arithmetic.py`, mpmath, 30 digits)

| Quantity | Value | Card expects |
|---|---|---|
| j₀,₁ | 2.404825557695773 | — |
| j₁,₁ | 3.831705970207512 | — |
| j₁,₁ / j₀,₁ | **1.593340505695112** | 1.59334 ✓ |
| P₀ = ln(j₁,₁/j₀,₁) | **0.4658327593074111** | 0.46583 ✓ |

| n | exact ratio^(n−1) | Letter 114 prints | status |
|---|---|---|---|
| 1 | 1 | 1 | ✓ |
| 2 | 1.593341 | 1.5934 | mis-rounded (4 dp is 1.5933) |
| 3 | 2.538734 | 2.5389 | equals 1.5934² (exact 2.5387) |
| 4 | **4.045068** | **4.0441** | **wrong** under either ratio (1.5934³ = 4.0455) |

Ball-lightning sequence for D₀ = 2 cm: 2.000, 3.187, 5.077, 8.090 cm → 2, 3.2, 5.1, 8.1 cm. Letter 114 ✓.

Correction recorded as CN-PLASMOID-02. It changes the 4th–5th significant figure only and has no
effect on the test, which uses P₀ exactly.

---

## 4 — The test as run

Fixed by the card (§2) and implemented in `plasmoid_stats.py`; coding rules and scoring frozen by
SHA-256 in `FREEZE.json` before any statistic was computed on real data.

- **Variable:** x = ln D (cm). **Primary statistic:** Rayleigh R at P₀, phase free. One primary test per dataset.
- **Heaping-aware null:** (1) log-normal fit to x (primary; KDE with bandwidth ≥ P₀ as sensitivity);
  (2) the dataset's own rounding scheme, estimated from every reported number: range vs single vs
  comparison-object reports; each number's coarsest step on a metric 1-2-5 grid (cm) or imperial
  grid (1, 2, 3, 6, 12 in…); range log-widths; comparison objects snapped to the nearest object the
  dataset actually uses; (3) 10,000 synthetic datasets of the same size. p = share of null R ≥ observed.
  **α = 0.01.**
- **Periodogram** over ratios 1.2–2.5 (step 0.0005), with competitors marked, the pointwise 99th
  percentile of the null, and a look-elsewhere p for the maximum (exploratory).

### 4a — Controls (synthetic; `step1_positive_control.py`)

The card requires that "this gate must be able to find a ladder". It can.

| Control | Set-up | Result |
|---|---|---|
| PC1 | Real ladder, D₀ = 12 cm, rungs 1–4, intrinsic width 8 %, 3 % measurement noise, 1 mm resolution, n = 150 | R = 0.582; null 99th pct 0.174; **p ≤ 10⁻⁴**. Periodogram peak at ratio 1.590 — but R(φ) = 0.565 and R(R5) = 0.581: unresolved, as the card says. |
| PC1n | Power of PC1 vs n (200 replicates) | n = 20: 0.80 · n = 30: **0.94** · n ≥ 50: **1.00** |
| PC2 | No ladder, instrument grade, n = 100 (400 replicates) | False-positive rate **0.75 %** at α = 0.01 (calibrated) |
| PC3 | PC1's ladder + 35 % eyewitness log-scatter + human rounding | **Detected 0/200.** |
| PC4 | No ladder + human rounding, n = 150 | False alarms: naive uniform-phase Rayleigh **27 %**; heaping-aware null **0.5 %** |
| PC5 | As PC1 but total width at Letter 114's own bound, σ = 0.10 (added after the independent check) | Power n = 30: 0.64 · n = 50: **0.92** · n = 100: **0.995** |

Analytic version (CN-PLASMOID-08): a perfect ladder with total log-scatter σ has expected
R = exp(−2π²σ²/P₀²). σ = 0.10 (Letter 114's own width bound) → R = 0.40; σ = 0.20 → 0.026;
σ = ln 1.5 → 3 × 10⁻⁷; σ = ln 2 (Rayle's "factor of two") → 10⁻¹⁹. Figure: `fig_positive_control.png`.

---

## 5 — Per-dataset results (`step2_score_pilots.py`; output `step2_output.txt`, `step2_results.json`)

### Pilot A — Keul 2021 (eyewitness: pilot / exploratory)

Coding (frozen): 22 core cases with an explicit number and unit; ranges → geometric mean; inches
converted exactly; outer envelope where a core and halo are both given; lower bounds, burn marks,
fragments, angular sizes and comparison objects not used. Provenance and verbatim fragments per case
in `data/keul2021_cases.csv`.

Sizes (cm): 11, 11.4, 13.3, 15, 15, 17.3, 20, 20, 22, 26.4, 30.5, 31.6, 34.6, 34.6, 44.7, 70.7, 100, 100, 100, 245, 350, 566.

Rounding audit: 34 reported numbers; 55 % of reports are ranges; 76 % of centimetre numbers are
multiples of 10 cm and a further 10 % multiples of 5; 48 % of centimetre numbers sit on the 1-2-5
sequence; 40 % of inch numbers are whole feet.

| Test | n | R(P₀) | null median | null 99th pct | **p** |
|---|---|---|---|---|---|
| **Primary** | 22 | 0.088 | 0.186 | 0.498 | **0.852** |
| core instead of outer (expl.) | 22 | 0.049 | 0.185 | 0.505 | 0.952 |
| drop angular-derived (expl.) | 20 | 0.051 | 0.205 | 0.542 | 0.954 |
| add 2 notable cases (expl.) | 24 | 0.091 | 0.179 | 0.477 | 0.829 |
| KDE density (expl.) | 22 | 0.088 | 0.187 | 0.502 | 0.857 |

Periodogram (`fig_A_keul2021.png`): span 8.5 periods → resolution ~12 % in log-period. Peak at
ratio 1.492 (R = 0.38), look-elsewhere p = 0.93. R at competitors: #162 0.088 · φ 0.140 · R5 0.076 ·
√e 0.141 · 1.5 0.373 · 2 0.006. φ and R5 cannot be excluded (and nothing is detected at any of them).

### Pilot A2 — Beatty collection, NMT site (eyewitness: pilot / exploratory)

Coding (frozen): size field first, narrative only if the field is empty or a bare shape word;
explicit numbers as for A; regulation sports balls at regulation diameters (ping-pong 4.0, golf 4.27,
cue 5.715, tennis 6.70, softball 9.70, volleyball 21.0, soccer 21.96, basketball 23.85 cm);
non-standard objects excluded. Provenance in `data/beatty_nmt_reports.csv`.

Sizes (cm): 4, 4.27, 5.71, 6.7, 8.94, 9.7, 9.7, 10.2, 12.2, 15, 15.2, 21, 22, 22, 22, 23.9 (×9), 34.6, 43.1, 50, 91.4, 91.4.

Rounding audit: 66 % of reports are comparison objects; of the explicit numbers, 63 % of centimetre
values are multiples of 10 cm and 67 % of inch values are whole feet.

| Test | n | R(P₀) | null median | null 99th pct | **p** | naive uniform-phase p |
|---|---|---|---|---|---|---|
| **Primary** | 29 | **0.560** | 0.415 | 0.692 | **0.109** | **5.8 × 10⁻⁵** |
| numeric only (expl.) | 10 | 0.361 | 0.262 | 0.699 | 0.276 | 0.28 |
| KDE density (expl.) | 29 | 0.560 | 0.411 | 0.678 | 0.110 | 5.8 × 10⁻⁵ |

Periodogram (`fig_A2_beatty.png`): span 6.7 periods → ~15 % resolution. Peak at ratio 1.557
(R = 0.65), look-elsewhere p = 0.28. R at competitors: #162 0.560 · **R5 0.592** · φ 0.450 · √e 0.328 ·
1.5 0.438 · 2 0.451.

**Reading:** the only pilot "signal" at P₀ is produced by comparison-object heaping and disappears
under the heaping-aware null. → **SC-PLASMOID-4, artefact.**

### Digitised histograms (F)

None — figures not retrievable in-session (data request R3). Pilot-only in any case.

---

## 6 — Width fits (§2.5)

Not triggered: no clustering was found in any dataset. Letter 114's σ < 10 % condition was not tested.
(Quantitative note, CN-PLASMOID-08 and PC5: a ladder at σ = 10 % gives R ≈ 0.40 at P₀; at instrument
grade the test detects it with power 0.92 at n = 50 and 0.995 at n = 100, but only 0.64 at n = 30.)

---

## 7 — Apparatus check (§2.6; `step3_apparatus_and_structure.py`)

No laboratory dataset was obtained, so the check could not be run on data. What it would need:

| Source | Apparatus lengths found | Reported plasmoid/bubble size |
|---|---|---|
| D — Illinois (Dubowsky, Rose) | cathode 6 mm OD (9 mm variant); insulator 6/8 mm; bowl 12 cm top, 4.5 cm lower; 20 L bucket | "approximately 20 cm" |
| D — IPP/HU Berlin (2006 release) | glass beaker, clay-tube electrode; 60 A for 0.15 s | 10–20 cm |
| E — Zhou et al. | tungsten tip, supersonic argon jet, fs laser | ~0.4 mm ("millimetre-scale") |
| F — cavitation | Minnaert resonance radius R_res = 3.29 m s⁻¹ / f: 20 kHz → 164 µm; 213 kHz → 15.4 µm; 355 kHz → 9.3 µm; 515 kHz → 6.4 µm; 647 kHz → 5.1 µm; 1056 kHz → 3.1 µm | µm-scale |

Two structural findings make the apparatus check decisive rather than routine:

- **j₁,₁/j₀,₁ is a generic apparatus ratio** (CN-PLASMOID-10). It is exactly the TM₁₁₀/TM₀₁₀ frequency
  ratio of a circular cylindrical cavity and the (1,1)/(0,1) mode ratio of a circular membrane or
  pressure-release cylinder. A wavelength-set size scales as 1/f, so a mode switch in any apparatus with
  circular cross-section produces a 1.5934 size ladder. (Rigid-wall acoustic modes use J′ zeros and give
  1.659, 1.376 — not 1.5934.)
- **In Letter 114's own setting, D₀ is an apparatus length by construction** ("set by the cavitation
  bubble size"). Only the ratio is testable; the apparatus check there must ask whether the ratio tracks
  the vessel/cavity modes.

---

## 8 — Steelman, both directions

### For #162 — the strongest case that a real ladder is present

1. **The eyewitness nulls carry no information.** PC3 shows a genuine 8.5 %-wide ladder becomes invisible
   (0/200) at eyewitness precision; analytically R falls to 3 × 10⁻⁷ at a factor-1.5 error. So pilot A's
   p = 0.85 says nothing against #162 — exactly as §0.6 anticipates.
2. **Mixed D₀ across sub-populations.** Ball lightning from different storms, ground conditions and
   (in BCT terms) different nucleation sizes would have different phases. Pooling smears any ladder even
   if each sub-population is perfectly quantised. No dataset available here is split by condition.
3. **The Letter's falsification experiment has never been run.** No controlled cavitation size dataset
   at fixed frequency exists in public; #162 is untested, not failed.
4. **The A2 periodogram does peak near the ladder** (1.557, within the 15 % resolution of 1.593).

**Does it succeed?** Only in establishing that absence of evidence here is uninformative. It does not
establish a ladder: point 4 is exactly what heaping produces (below).

### Against #162 — the strongest case that any apparent ladder is an artefact

1. **Comparison-object heaping (demonstrated).** A2's naive p = 5.8 × 10⁻⁵ is entirely produced by
   basketball/soccer/volleyball reports clustered at 21–24 cm; heaping-aware p = 0.11. PC4: naive tests
   false-alarm 27 % of the time on rounded smooth data.
2. **Preferred-number psychology is a built-in impostor** (CN-PLASMOID-09). Decimal rounding is periodic
   in ln D with period ln 10; its 5th harmonic is exactly the R5 step 10^(1/5) = 1.5849, 1.14 % from P₀.
   Telling the two apart by the card's own resolution rule needs a span of ~88 periods — about
   **18 decades of size**. No size dataset can exclude R5, so any human-reported sizes will tend to show
   Rayleigh power near P₀ with no ladder at all. (φ needs ~6 decades.)
3. **Apparatus-set sizes** (CN-PLASMOID-10): 1.5934 is the lowest mode ratio of a disc or cylinder.
4. **Selection effects.** Larger, brighter, longer-lived events are more often reported or filmed, and
   reporters choose familiar reference objects. These shape the size density and its heaping; for lab
   footage, "good" shots selected for publication could do the same.
5. **Letter 114's support is unverified.** The Stenhoff citation has no page and could not be checked;
   the printed D₄ is wrong.

**Does it succeed?** **Yes, for the one pilot dataset that looked positive** (A2): the apparent signal is
fully explained by heaping. Point 2 also means eyewitness "support" for #162 would be expected even if
#162 were false.

---

## 9 — Notices (revised clause by clause)

| ID | Tier | Notice |
|---|---|---|
| CN-PLASMOID-01 | PROVEN | j₀,₁ = 2.404825557695773, j₁,₁ = 3.831705970207512, ratio 1.593340505695112, P₀ = 0.4658327593074111; ladder 1, 1.593341, 2.538734, 4.045068; ball-lightning sequence for D₀ = 2 cm is 2, 3.2, 5.1, 8.1 cm as Letter 114 states. |
| CN-PLASMOID-02 | PROVEN (correction) | Letter 114's D₄ = 4.0441 D₀ is wrong; exact value **4.0451 D₀** (4.0455 with the Letter's rounded 1.5934). Also: the ratio prints as 1.5934 but rounds to 1.5933 at four decimals; D₃ = 2.5389 is 1.5934² (exact 2.5387). No effect on the test. |
| CN-PLASMOID-03 | PROVEN | Search-space audit (§1): no qualifying dataset was obtainable. → **SC-PLASMOID-3, halt.** |
| CN-PLASMOID-04 | PROVEN (correction to card §0.5 row A) | Keul 2021 Table 1 (and its XLSX) is a binned contingency table (size bins 1.5–20 cm: 19; 20–50 cm: 0; 50 cm–1 m: 1; > 1 m: 8; total 28), not per-case data. Per-case sizes exist only in the case abstracts; 22 core cases give an explicit number with a unit. The table's own bin counts could not be reconciled with the abstracts (several abstracts state 20–40 cm); not pursued. Source read through the web-fetch tool from the publisher's XML and PDF; per-case values extracted twice independently and agreed. |
| CN-PLASMOID-05 | PROVEN (pilot, exploratory) | Pilot A (Keul 2021, n = 22): R(P₀) = 0.088, heaping-aware p = 0.852; all four sensitivities p ≥ 0.82. No clustering. Uninformative about #162 (CN-08). |
| CN-PLASMOID-06 | PROVEN (pilot, exploratory) | Pilot A2 (Beatty, n = 29): R(P₀) = 0.560; naive uniform-phase p = 5.8 × 10⁻⁵; heaping-aware p = 0.109. The apparent signal is comparison-object heaping. → **SC-PLASMOID-4, artefact.** R5 outscores P₀ (0.592 vs 0.560). |
| CN-PLASMOID-07 | PROVEN (method) | The pipeline finds an injected ladder (8.5 % total width: power 0.94 at n = 30, 1.00 at n ≥ 50), is calibrated (0.75 % false positives at α = 0.01), and the heaping-aware null cuts false alarms on rounded data from 27 % (naive) to 0.5 %. |
| CN-PLASMOID-08 | PROVEN | Expected R for a perfect ladder with total log-scatter σ is exp(−2π²σ²/P₀²): 0.40 at σ = 0.10, 0.026 at 0.20, 3 × 10⁻⁷ at ln 1.5. Eyewitness data cannot test #162 at any sample size; this quantifies §0.6. |
| CN-PLASMOID-09 | PROVEN | R5 = 10^(1/5) is the 5th harmonic of decimal heaping (period ln 10/5), 1.14 % below P₀. Resolving it from P₀ by the card's 1/k rule needs ~88 periods (~18 decades of size); φ needs ~30 periods (~6 decades). R5 and φ can never be excluded by a size dataset; decimal rounding mimics #162 by construction. |
| CN-PLASMOID-10 | PROVEN | j₁,₁/j₀,₁ is exactly the TM₁₁₀/TM₀₁₀ frequency ratio of a circular cylindrical cavity and the (1,1)/(0,1) mode ratio of a circular membrane. Any apparatus with circular cross-section can produce a 1.5934 size ladder; §2.6 must test the vessel/cavity/electrode diameter specifically. A 1.5934 ladder in such an apparatus would not discriminate. |
| CN-PLASMOID-11 | ASSERTED (open) | **SC-PLASMOID-5 status:** Letter 114's "consistent with reported preferred ball lightning size clusters" (Stenhoff 1999) could not be checked — book paywalled, no preview, no page cited, and none of its 14 chapter titles concerns size. Neither confirmed nor corrected. **Not inherited.** No secondary source reached (Wikipedia, Sello 2011, a 2005 review) attributes any size clustering to Stenhoff. |
| CN-PLASMOID-12 | ASSERTED (untraced) | The card's §0.5 row B summary for Keul & Stummer 2002 ("median 25–30 cm, mode 30 cm") was not traced to the primary source. Declared in §7. |
| CN-PLASMOID-13 | PROVEN (prompt defect) | Card §0.3 says untraced claims must be "declared in §7", but the card has no §7. This deliverable adds §7 to honour the clause. |
| CN-PLASMOID-14 | PROVEN (prompt observation, by text comparison) | Scope tension. Letter 114's falsification clause is specifically a controlled **cavitation** experiment at fixed acoustic frequency. The card ranks cavitation bubbles as secondary (§0.5) and §0.6 generalises the clause to any instrument-measured sizes. So a qualifying dataset under the card would not be the Letter's own experiment, and SC-PLASMOID-2 applied to non-cavitation plasmoids would extend the clause beyond its text. This does not affect the present verdict (SC-3). |
| CN-PLASMOID-15 | CONJECTURE | What would settle it: ≥ 50–100 instrument-measured sizes at fixed conditions — water-discharge plasmoids at fixed voltage, capacitance, electrode and vessel, imaged with a scale; or Zhou et al.'s shot-by-shot sizes; or, for the Letter's own clause, directly imaged sonoluminescing-bubble or plasma sizes at fixed frequency. Plus an apparatus control varying vessel/cavity diameter (CN-10). The power figures (0.92 at n = 50, 0.995 at n = 100 for a 10 %-wide ladder; PC5) are proven only for the simulated ladder model; the recommendation is conjecture. |

---

## 10 — §7: untraced second-hand claims (declared per card §0.3)

1. Keul & Stummer 2002 — "median 25–30 cm, mode 30 cm" (from the card's own table). Primary
   (*Int. J. Meteorol.* 27(274), 385–393) not obtained. Composition 150 + 103 + 152 cases comes from a
   citing snippet, not the paper.
2. Stenhoff 1999 — "preferred ball lightning size clusters" (from Letter 114). Primary not obtained.
3. Charman 1972 (*New Scientist*) — "most commonly 10–20 cm", seen only via Wikipedia. Not used.
4. Birbrair — "average observed diameter 24 cm", seen only via Sello 2011. Not used.
5. Rayle 1966 — the McNally 1966 comparison (median ≈ 10 in) is second-hand within Rayle. Not used.

---

## 11 — Scripts and files (`audit/gates/PLASMOID/`)

| File | Role |
|---|---|
| `gate_PLASMOID_prompt_asrun.md` | as-run card, byte-identical to the pre-registered file |
| `step0_arithmetic.py`, `step0_output.txt` | §1 arithmetic |
| `plasmoid_stats.py` | test machinery (Rayleigh, periodogram, rounding-scheme estimation, heaping-aware null) |
| `step1_positive_control.py`, `step1_positive_control_output.txt`, `fig_positive_control.png` | controls PC1–PC5 |
| `data/keul2021_cases.csv` | pilot A: per-case coding with verbatim fragments |
| `data/beatty_nmt_reports.csv` | pilot A2: per-report coding with verbatim fragments |
| `FREEZE.json` | SHA-256 of library, scorer and both data files, frozen before scoring; the scorer refuses to run if any changed |
| `step2_score_pilots.py`, `step2_output.txt`, `step2_results.json`, `fig_A_keul2021.png`, `fig_A2_beatty.png` | primary tests, sensitivities, periodograms, null distributions |
| `step3_apparatus_and_structure.py`, `step3_output.txt` | §2.6 lengths, cylinder-mode ratio, decimal-heaping harmonics, resolution spans |

Erratum in a frozen file (left unedited so the freeze stays verifiable): the docstring of
`step2_score_pilots.py` says "Primary set = the 41 core cases … that state an explicit number"; it
means *those of* the 41 core cases that do — 22, as the CSV and this report use.

Delivered as a `git format-patch` of one commit on top of `501ea79`, adding only
`audit/gates/PLASMOID/`. `audit/NEXT.md` is not modified.

Reproduce: `python3 step0_arithmetic.py && python3 step1_positive_control.py && python3 step2_score_pilots.py && python3 step3_apparatus_and_structure.py`
(numpy, scipy, mpmath, matplotlib; seeds fixed).

---

## 12 — Contamination statement

- **Quarantine kept.** The 24 Oct 2026 drafting chat and concurrent gates were not consulted. No file
  under `audit/notes/` or `audit/gates/*/` was read. No past chats, project memory or project documents
  were searched or read. From the repo, only the card, its digest file and
  `tex/BCT_Letter114_PlasmoidPhysics.tex` (the #162 statement, the D_n table it depends on, the
  falsification clause, and the Stenhoff sentence and bibitem) were read. Disclosures: the read window
  on the Letter (lines 190–265) also displayed its SAFIRE section, and a keyword grep displayed a few
  table lines assigning Hopf charges; neither was used. Directory listings of the repo root and
  `audit/gates/` showed folder names only. The session's system context automatically displayed the
  titles and one-line descriptions of this Project's memory files; none was opened.
- **Order of work.** The test library and the controls were written and run on synthetic data first.
  The pilot coding rules were written after the per-case size statements had been seen during
  extraction, but **before any statistic was computed on them**; scorer, library and data files were then
  frozen by SHA-256 (`FREEZE.json`, 2026-10-24T11:53:37Z) and scored once; all scripts were then re-run
  unchanged as a reproducibility check (fixed seeds, byte-identical outputs), which is why output file
  times post-date the first draft of this report. Sensitivities are labelled exploratory.
- **Independent check.** A separate agent that had not seen the work being produced cross-checked every
  number here against the outputs and data files. It found no numerical errors and five slips (two
  roundings, an inequality, a cue-ball diameter written two ways, and a power claim at n = 30 that had
  been extrapolated from PC1's 8.5 % width). All were corrected; the power claim now rests on control
  PC5, added to `step1_positive_control.py` after PC1–PC4 so their outputs are unchanged.
- **Extraction route.** Publisher pages, PDFs and the NMT reports were read through the session's
  web-fetch tool, which returns a model-mediated text extraction rather than raw bytes. Per-case values
  were extracted twice with different prompts and agreed; residual transcription risk remains and is
  flagged.
- **No inheritance.** Letter 114's Stenhoff claim and the card's Keul & Stummer summary were not used
  as evidence.

---

## 13 — What settling this buys (card §0.6, verbatim)

> This gate decides whether measured sizes bunch at a ratio of 1.5934. It does **not** decide
> whether plasmoids are Hopf-charge excitations of a Planck-scale lattice. **A pass does not
> vindicate BCT** — size ladders can arise from apparatus resonances, electrode or bubble
> geometry, or human rounding, and the ratio cannot be told apart from nearby "nice" numbers
> (§2.4). **A fail on eyewitness data does not refute #162** — eyewitness size estimates are too
> coarse. By Letter 114's own falsification clause, only instrument-measured sizes from >100
> events at fixed conditions can refute it.

---

## 14 — What the gate did **not** establish

- Whether plasmoid sizes are quantised at 1.5934 — no qualifying data.
- Whether #162 fails — no qualifying data; eyewitness nulls are uninformative (CN-08).
- Whether Stenhoff 1999 reports size clusters (SC-5 open).
- Any σ < 10 % width test.
- Any apparatus check on real laboratory data.
- Anything about BCT, Hopf charge or a Planck-scale lattice.
- That φ or R5 are excluded — they cannot be, by any size dataset (CN-09).

---

## 15 — Data requests that would settle it

| # | Request | Settles |
|---|---|---|
| R1 | Stenhoff 1999, the pages where size or the survey is discussed (likely Ch. 1, pp. 1–21) | SC-PLASMOID-5 |
| R2 | Zhou et al. 2026 Supplementary Information and figshare source data (doi:10.6084/m9.figshare.31396380); if fewer than 100 shots, the raw shot-by-shot sizes from the SIOM group | possibly a qualifying dataset |
| R3 | Lee et al. 2005 *JACS* 127, 16810 and Brotchie et al. 2009 *PRL* 102, 084302 (PDFs, for digitising) | pilot only — cannot change SC-3 |
| R4 | ≥ 100 imaged water-discharge plasmoid sizes at fixed conditions, plus one run with a different vessel or electrode diameter (IPP/HU Berlin, Illinois, Texas State, TU/e, St Petersburg) | SC-1 or SC-2 |
| R5 | Fantz et al. 2013 *J. Appl. Phys.* 114, 043302 (to check for shot statistics) | possibly D |
| R6 | Keul & Stummer 2002, *Int. J. Meteorol.* 27, 385–393 | traces CN-12; pilot only |

---

## Sources

- Keul, A. G. (2021). [A brief history of ball lightning observations by scientists and trained professionals](https://hgss.copernicus.org/articles/12/43/2021/), *Hist. Geo Space Sci.* 12, 43–56 ([PDF](https://hgss.copernicus.org/articles/12/43/2021/hgss-12-43-2021.pdf), [XML](https://hgss.copernicus.org/articles/12/43/2021/hgss-12-43-2021.xml)).
- Sonnenfeld, R., NMT ball-lightning site: [index](https://kestrel.nmt.edu/~rsonnenf/BL/), [Beatty collection](https://kestrel.nmt.edu/~rsonnenf/BL/rpts/balllightningreports79.pdf), [outdoor](https://kestrel.nmt.edu/~rsonnenf/BL/rpts/outdoors.html), [indoor](https://kestrel.nmt.edu/~rsonnenf/BL/rpts/indoors.html), [Japan](https://kestrel.nmt.edu/~rsonnenf/BL/rpts/japan.pdf).
- Rayle, W. D. (1966). [Ball lightning characteristics, NASA TN D-3188](https://ntrs.nasa.gov/citations/19660006027).
- Smirnov, B. M. (1994). [Long-lived light phenomena in the atmosphere](https://ufn.ru/ufn94/ufn94_5/ufn945f.pdf), *Phys.-Usp.* 37, 517.
- Zhou, C. et al. (2026). [Ball-lightning-like relativistic terahertz solitons](https://www.nature.com/articles/s41566-026-01899-y), *Nat. Photon.* 20, 727–733; Bulanov, S. (2026). [Is ball lightning a relativistic soliton?](https://www.nature.com/articles/s41566-026-01914-2); preprint [Research Square rs-6473214](https://www.researchsquare.com/article/rs-6473214/v1).
- IPP (2006). [Ball-lightning in the laboratory](https://ipp.mpg.de/ippcms/eng/presse/archiv/05_06_pi); Juettner et al. (2007). [ICPIG abstract](https://research.tue.nl/en/publications/long-living-plasmoids-from-a-water-discharge-at-atmospheric-press/); Dubowsky, S. E. (2016). [Prospectus with two papers](https://bjm.scs.illinois.edu/miscpubs/Dubowsky2016.pdf); Rose, A. N. (2018). [BSc thesis](https://bjm.scs.illinois.edu/miscpubs/Rose2018.pdf); Stephan, K. et al. [GEC 2012 abstract](https://meetings-archive.aps.org/gec/2012/uf2/3); Fantz, U. et al. (2013). [JAP 114, 043302 record](https://opus.bibliothek.uni-augsburg.de/opus4/frontdoor/index/index/docId/60633).
- Stenhoff, M. (1999). *Ball Lightning: An Unsolved Problem in Atmospheric Physics*: [Springer TOC](https://link.springer.com/978-0-306-46150-7), [Ch. 1](https://link.springer.com/chapter/10.1007/0-306-47092-6_1), [Ch. 10](https://link.springer.com/chapter/10.1007/0-306-47092-6_10).
- Keul & Stummer (2002) reference as cited in [arXiv:2304.01784](https://arxiv.org/pdf/2304.01784); data-bank composition via [Keul 1981 record](https://www.researchgate.net/publication/227250889_Ball_lightning_reports); [Keul 2013 chapter](https://link.springer.com/chapter/10.1007/978-94-007-5000-5_3); [Keul 1999](https://kestrel.nmt.edu/~rsonnenf/BL/pubs/JMet1999TwoBLcasesKeul.pdf).
- Melbourne sonochemistry: [2005 publication list](https://sono.chemistry.unimelb.edu.au/?p=93); Kerboua et al. (2021) [Processes 9, 1546](https://www.mdpi.com/2227-9717/9/9/1546) (secondary description of Brotchie et al. 2009).
- Obreschkow, D. et al. [Cavitation Bubble Data (Parabolic Flights, 2010)](https://zenodo.org/records/5733740); Senegačnik, M. et al. [Mendeley dataset](https://data.mendeley.com/datasets/w8mpz3v3w2).
- Paiva, G. S. et al. (2007). [PRL 98, 048501 (ADS)](https://ui.adsabs.harvard.edu/abs/2007PhRvL..98d8501P); Jerby, E. (2008). [Fireballs](https://www.eng.tau.ac.il/~jerby/Fireballs_GCMEA_Jerby_8-2008.pdf); Dvornikov, M. S. et al. [arXiv:1711.10709](https://arxiv.org/pdf/1711.10709).
- Sello, S. (2011). [arXiv:1102.2829](https://ar5iv.arxiv.org/html/1102.2829); Gunther, N. J. [arXiv:2204.08288](https://arxiv.org/pdf/2204.08288); [Wikipedia, Ball lightning](https://en.wikipedia.org/wiki/Ball_lightning).
- Flux-rope catalogue (identified, not used): [VizieR J/ApJS/239/12](https://dc.g-vo.org/rr/q/lp/custom/CDS.VizieR/J/ApJS/239/12).

*Gate PLASMOID closed 24 October 2026: SC-PLASMOID-3 (halt), with SC-PLASMOID-4 for pilot A2 and
SC-PLASMOID-5 open.*
