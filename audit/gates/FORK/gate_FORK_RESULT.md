# GATE FORK — RESULT
## Working backwards through the forks of the BCT derivation, with a scored null model. Cold Ledger gate, run 11 October 2026.

**Model that ran this gate: Claude Opus 5.5** (`claude-opus-5-5`, Anthropic). One gate, this thread only.

---
## §1 — Digest and provenance (recorded before any other number)

| item | value |
|---|---|
| repository | `zerofreeparameters-code/BCT-Programme` |
| **commit SHA-1 of the checkout** | **`bc5c87dc2f5b978d014d0da876bd718c3f20aada`** (`git rev-parse HEAD`, re-checked by the run script) |
| prompt fetched | `curl` to disk from `raw.githubusercontent.com/…/bc5c87dc…/audit/gates/gate_FORK_prompt.md` (12,559 bytes) |
| check | `sha256sum -c audit/gates/PREREG_20261011.sha256` in the checkout → `gate_FORK_prompt.md: OK` |
| **prompt SHA-256** | **`c21bc5d6a6c13b25016c6835966adf86d8bdb330b4cc5fb9c082a4947fc59e09`** — matches the pre-registration; hashed before reading; the in-tree copy has the same digest |
| verdict on digest | **MATCH. Gate run.** |
| J1–J5 source | `audit/gates/PRED/scripts/pred_step2_nullmodel.py`, SHA-256 `e8ddc17136a521ed5f8e015cc1587fbeccd16521bedab3a004bc06b341aabc82` |
| J1–J5 copied byte-for-byte | judgement text = lines 5–16 (SHA-256 `9536c709…cdadd9f`); implementation = lines 18–77 (SHA-256 `aff0ef8a…4495c9c`): atoms, unary, clean, binary, L1…L3r, target dict, Nmenu, hit_stats. The script re-reads the PRED file at run time and halts unless both slices are byte-identical. They are. |
| environment | Python 3.13.16, numpy 2.5.3, mpmath 1.4.1, scipy 1.18.1; 2 CPUs; run time 1,107 s; peak memory 1.26 GB |
| precision | geometry in mpmath at 60 dps, 40 significant digits reported; enumeration in float64 exactly as PRED |
| determinism | three independent full runs; `fork_scores.csv`, `fork_alpha_sweep.csv` and the verdict tables are byte-identical across all three (the map changed between runs 2 and 3 only by a formatting fix to its own text) |

**Reproduction of PRED inside this run.** The verbatim block, executed as copied, prints PRED's own numbers (1-atom 102, 2-atom 90,755, 3-atom 20,158,524 distinct values; 48 targets). The per-branch replay of PRED's enumeration lines, run on PRED's ★ atoms, returns arrays bit-identical to the verbatim module-level ones, and PRED's ★ statistics come back unchanged: P = 0.1078 / 0.5034 / 0.0115 / 0.2296 with 48/48 covered (3-atom; 1 %/1 % with layer/0.1 %/0.1 % with layer), as in `PRED/output/step2_out.txt`.

---
## §2 — Verdict

> **SC-FORK-2 (selection is base rate).**
> The clean numbers of the forward chain are what any branch produces; the forks did not discriminate.
> **Closes:** the claim that the α₀ layer's agreement is evidence for the lattice/unit/form choices.
> **Does not touch** the void geometry as geometry (R8 scope note stands).

How the rule was met:

| condition (§5) | value | met? |
|---|---|---|
| SC-FORK-2: ★ within the central 80 % on C **or** C₀.₁ | PR(C) = 50.52, PR(C₀.₁) = 50.52 (one-step set, 96 alphabets) | **yes** |
| SC-FORK-2: **or** L_α at ★'s own error ≥ 10 | L_α = 1 | no (not needed) |
| SC-FORK-1: PR ≥ 95 on both, ≥ 2 exclusive hits, L_α ≤ 3 | PR 50.52; exclusive hits of ★ = 0; L_α = 1 | no (and excluded by 2) |
| SC-FORK-3: an untaken branch beats ★ on both C and C₀.₁ with ≥ 2 exclusive hits | no branch exceeds ★ on either score | no |
| SC-FORK-0: a sensitivity run (a)–(d) changes the verdict or moves ★ across a band edge; or F2/F4 numerics fail | (a)–(d) all give SC-FORK-2 with ★ in the central band; F2 and F4 close to 40 digits | no |

**What the 50.52 is, in plain words.** Every scored alphabet — all 96 in the one-step set, all 24 in the F1 × F3 set, all 110 in their union, and all 101 continuum points — covers **48/48 targets at 1 % and 48/48 at 0.1 %**. ★ is tied with every branch. The percentile under ties is the average rank of the tied block, 100·(96+1)/(2·96) = 50.52. The coverage statistics C and C₀.₁ carry no information that distinguishes any branch from any other.

**Dependence on the tie convention, stated in full.** The prompt does not say how to rank ties, and here every score ties, so this is the load-bearing reading. K3 fixed it before any branch was scored: scipy's default percentile rank (`kind='rank'`, average rank of ties). Under `mean` the percentile is 50.00 (same verdict). Under `weak` (★ placed at the top of its tie block) it is 100, and under `strict` (bottom) it is 0; in both of those cases **no verdict condition is met at all** — SC-FORK-1 still fails (zero exclusive hits) and SC-FORK-3 still fails (nothing beats ★). **No tie convention produces SC-FORK-1 or SC-FORK-3.**

---
## §3 — Headline count L_α (F6 × F7, single target 1/α)

★: 1/α = 1/[α₀(1−2α₀)] = **137.0182632593250628542024417630252884732**; H_α(★) = |1/α − 137.035999|/137.035999 = **1.294239528617377817456436171542889747489 × 10⁻⁴** (0.01294 %).

| threshold | forms within (of 3,528) |
|---|---|
| H_α(★) — the taken path's own error (K11) | **1** (★ itself) |
| 0.013 % (literal) | 1 |
| 0.1 % | 3 |
| 1 % | 33 |

The three within 0.1 %: product/π with N = −2, s = +1 (★; 0.0129 %); product/π with N = +2, s = −1 (136.98819; 0.0349 %); r_tet²/√3 with no correction (137.16428; 0.0936 %). The 33 within 1 % come from four base forms only: product/π, r_tet²/√3, |r_oct − r_tet|/4π, r_oct²/2π. All 33 are listed in `fork_map.md`.

**Row-count defect.** The rule in F6 lists 8 functions g, not 9, so there are 72 coupling forms and 72 × 49 = **3,528** F6 × F7 forms, not 3,969. `fork_alpha_sweep.csv` has 3,528 rows. No ninth function was invented (§1 of the prompt forbids additions). See §9, D2.

---
## §4 — Rank of ★

| run | n | C★ | PR(C) | C₀.₁★ | PR(C₀.₁) | C distribution | C₀.₁ distribution | excl. hits of ★ | verdicts met |
|---|---|---|---|---|---|---|---|---|---|
| **primary** (3-atom, J3 layer on, 48 targets, 1 % / 0.1 %) | 96 | 48/48 | 50.52 | 48/48 | 50.52 | 48 ×96 | 48 ×96 | 0 | 2 |
| (a) 2-atom bound | 96 | 48/48 | 50.52 | 48/48 | 51.04 | 48 ×96 | 47 ×1, 48 ×95 | 0 | 2 |
| (b) J3 layer off | 96 | 48/48 | 50.52 | 48/48 | 50.52 | 48 ×96 | 48 ×96 | 0 | 2 |
| (c) 11 headline targets | 96 | 11/11 | 50.52 | 11/11 | 50.52 | 11 ×96 | 11 ×96 | 0 | 2 |
| (d) tolerance 0.5 % (replaces 1 %) | 96 | 48/48 | 50.52 | 48/48 | 50.52 | 48 ×96 | 48 ×96 | 0 | 2 |

In (a) the single 47 is F2 at c/a = √(2/3) (alphabet A006, whose octahedral-continuation void has zero radius); it misses m_μ/m_e, the same target PRED's own 2-atom run missed without the layer.

**F1 × F3 set** (24 distinct alphabets, every one at 48/48 on both scores): ★ at 52.08 (rank), 0 (strict), 100 (weak), 50 (mean), on both C and C₀.₁.

**Scored-set sizes.** One-step: 150 fork-branch rows (★ once) → **96 distinct alphabets** (K2; every F7 row and HCP share ★'s alphabet; D4, FCC-oct-only and BCT c/a = 2 share one alphabet; BCC appears in F1 and F2; u = c equals u = a_cubic for FCC). F1 × F3: 42 cells → 39 defined (HCP has no cubic cell; SC and diamond have no second void) → **24 distinct alphabets**. Union: **110**. F2 continuum: 101 points (plotted, outside the reference set, K4). In all, 213 distinct atom sets were enumerated; counting F9's four anchor variants of ★'s atom set separately (K2), there are 217 scored alphabets (ids A001–A118 for the one-step, F1 × F3 and K13 rows; the rest are continuum points).

**Independent check.** A separate agent that had not seen the work recomputed ★'s constants, rebuilt the 3,528-form sweep from scratch, recounted the CSVs and redid the percentile arithmetic and verdict logic. Every number in §§2–8 reproduced; its one note (the 213/217 wording above) is incorporated.

---
## §5 — Per-target look-elsewhere count L(t)

Primary configuration, 0.1 %: **L(t) = 110 of 110 for every one of the 48 targets.** By the prompt's own reading ("a target reached by most branches is reachable by the alphabet's richness, not by the geometry"), every target is. The full table is degenerate; it is in `fork_scores.csv` (column `missed_targets_0.1pct` is empty on every scored row).

---
## §6 — Exclusive hits ("clues")

- **Exclusive hits of ★:** none. The smallest L(t)/110 is 1.000; the threshold is 0.05.
- **Exclusive hits of untaken branches:** none, in the primary run and in every sensitivity run, because ★ itself reaches every target in every run. **No CANDIDATE is logged. Nothing is opened.**

---
## §7 — Sensitivity (§6 of the prompt)

(a)–(d) are in the §4 table. ★'s percentile is 50.52 (51.04 on C₀.₁ in (a)) in every run; it never leaves the central band [10, 90] and never reaches 95; the verdict set is {2} in every run. **The primary verdict does not flip.** SC-FORK-0 is not triggered.

**Convention sensitivity (reported; outside the verdict rule):**

| convention | n | PR(C) | PR(C₀.₁) | verdicts met |
|---|---|---|---|---|
| percentile `strict` | 96 | 0.00 | 0.00 | none |
| percentile `weak` | 96 | 100.00 | 100.00 | none |
| percentile `mean` | 96 | 50.00 | 50.00 | 2 |
| no de-duplication (each fork-branch row counted, K2 off) | 150 | 50.33 | 50.33 | 2 |
| F2 continuum inside the reference set (K4 off) | 195 | 50.26 | 50.26 | 2 |
| F2 voids = Voronoi-vertex classes (K13) | 98 | 50.51 | 50.51 | 2 |

---
## §8 — Notices

**CN-FORK-01 [verdict, pre-registered].** SC-FORK-2. Under the PRED null (J1–J5 copied byte-for-byte), standing at each fork of F1–F9, the taken branch reaches exactly as many of the 48 fixed targets as every untaken branch: all of them, at 1 % and at 0.1 %. Clause: the α₀ layer's agreement is withdrawn as evidence for the lattice, unit, radius-definition, void-subset, coupling-form, dimension and anchor choices.

**CN-FORK-02 [CONJECTURE — post-hoc, not pre-registered].** The coverage score is blind to geometry, not merely flat across these branches. With r_oct, r_tet and α₀ all **removed** from the alphabet, the remaining 14 atoms ({1,2,3,4,5,6,8,9,12}, π, √2, √3, √6, S_D4) still reach 48/48 targets at 0.1 % with 3 atoms and no correction layer (47/48 at 2 atoms, missing m_μ/m_e). Code in Appendix A. The pre-registered C and C₀.₁ therefore could not have discriminated any geometric branch, whatever the geometry; the forks were tested with an instrument that saturates before the geometry enters.

**CN-FORK-03 [CONJECTURE].** L_α = 1 is not evidence on its own. ★ has the smallest error of all 3,528 forms, so the count at ★'s own error is 1 by construction. The local density of forms near 137.036 (33 within ±1 %, 3 within ±0.1 %) predicts about 0.43 (resp. 0.39) forms inside ±H_α(★): roughly a one-in-three chance that the best of this menu lands as close as ★ does. This does not price in the documented post-hoc choice of the correction (PRED §7).

**CN-FORK-04 [CONJECTURE, descriptive].** P_hit, the one score that varies between branches, puts ★ at the 25th percentile at 1 % (0.5034 against a one-step median of 0.747) and the 48th at 0.1 %. Across F6 it rises with α₀ (Spearman 0.74), because the J3 layer's reach grows with the branch's α₀. P_hit measures how rich an alphabet is, not how good its geometry is.

**CN-FORK-05 [CONJECTURE, map].** Identities found while mapping, each computed to 40 digits: D4's three hole classes all have ρ/D = (√2−1)/2, so the D4 alphabet equals FCC-octahedral-only and BCT at c/a = 2; HCP's voids equal FCC's (stacking-blind); diamond's large void has ρ = R exactly (r = 1/2 in u = D); the BCC "octahedral" site is a two-neighbour saddle, not a Voronoi vertex; at c/a = √(2/3) the octahedral continuation has zero radius; at c/a = √(6/5) the octahedral-continuation radius equals FCC's r_tet = (√6−2)/4 exactly. None is evaluated as physics here.

---
## §9 — Prompt defects and ambiguities (recorded; none changed a fork, branch, target, tolerance or rule)

- **D1 — target count.** §3 says "47 dimensionless targets". The PRED J4 list, copied byte-for-byte as §7 requires, has **48** (PRED's own run prints "targets fixed: 48"). 48 were used. Since every alphabet covers every target, removing any one leaves every rank unchanged.
- **D2 — F6 arithmetic.** The g list has 8 members (product, two ratios, sum, |difference|, geometric mean, r_a², r_b²), so "9 × 9 = 81" is 8 × 9 = **72**, and F6 × F7 is **3,528**, not 3,969.
- **D3 — §7 cross-check at c/a = 1.** In F2's own parameterisation c/a = 1 is BCC, where (√2−1)/2 and (√6−2)/4 are not the void radii. All three readings were run and pass to 40 digits: BCT c/a = √2 → (√2−1)/2, (√6−2)/4; FCC's cubic cell (FCT c/a = 1) → the same; BCT c/a = 1 → BCC's (2−√3)/(2√3), (√5−√3)/(2√3).
- **D4 — "D4 with its two hole types".** D4 has three hole classes (the three non-zero glue cosets); all have circumradius 1 and coordination 8, equal under triality. Computed and recorded; the alphabet uses two equal radii.
- **D5 — BCC "distorted octahedral" void.** Not a Voronoi vertex (it is the midpoint of the two axial second neighbours). F1's two-void BCC was kept; the pure Voronoi reading of F2 (one void at c/a = 1) is reported as K13.
- **D6 — F2 named list.** The crossing enumeration (K5) adds c/a = √(3/4), √(6/5), √(14/9), √(10/3) to the five named points.
- **D7 — F7 in the general score.** α is not a PRED atom, so no F7 branch can change the scored alphabet; all 48 untaken F7 branches are ★'s alphabet. Their only effect is in the F6 × F7 sweep. The design's "about 200" counted them.
- **D8 — F1 × F3 "7 × 7".** RCP is "not scored separately" by F1; HCP has no cubic cell; SC and diamond have no second void. 39 defined cells.
- **D9 — unstated rules, fixed by judgement calls before scoring:** J3 layer in the primary (K1); "scored alphabet" (K2); percentile under ties (K3, load-bearing, §2); continuum role (K4); crossing bound (K5); F2 void identity (K6, K13); F4 polyhedra (K7); per-lattice units (K8); meaning of "tolerance 0.5 %" (K9); the "80/95 boundaries" (K10); L_α threshold (K11); "exclusive hits of its own" (K12).
- **D10 — run conditions.** The prompt asks for a fresh thread with past-chat search and memory generation off. Memory is not enabled on this account; no past-chat tool was available or used.

---
## §10 — Judgement calls (verbatim in `gate_FORK_run.py`, fixed before any branch alphabet was scored)

K1 primary = 3-atom, J3 layer on with the branch's own α₀, all 48 targets, 1 % and 0.1 %. K2 "scored alphabet" = distinct (atom set, targets) at 35 digits. K3 percentile = scipy `kind='rank'`, ★ in the array; central 80 % = 10 ≤ PR ≤ 90. K4 continuum scored, not in the reference set. K5 crossings: c/a ∈ [√(2/3), 2], vector classes of length ≤ 2a, exact rationals. K6 F2 voids = Wyckoff 2b (½,½,0) and 4d (0,½,¼), radii by exhaustive nearest-point search at 60 dps. K7 F4 polyhedra from the atom centres at the void's circumradius. K8 units per lattice as listed in the script. K9 (d) replaces 1 % by 0.5 %. K10 SC-FORK-0 if any of (a)–(d) changes the verdict set or ★'s band membership. K11 L_α threshold = H_α(★), inclusive; literal 0.013 % alongside. K12 SC-FORK-3 uses the §4 untaken-branch definition. K13 Voronoi-vertex reading of F2, reported only.

---
## §11 — Verification

| check | result |
|---|---|
| BCT c/a = √2: r_oct (2b), r_tet (4d) vs (√2−1)/2, (√6−2)/4 | 0.2071067811865475244008443621048490392848, 0.1123724356957945245493210186764728479915 — equal to 40 digits |
| FCC cubic cell (FCT c/a = 1): same two | equal to 40 digits |
| BCT c/a = 1 (BCC) vs (2−√3)/(2√3), (√5−√3)/(2√3) | 0.07735026918962576450914878050195745564760, 0.1454972243679028141965442332970666018055 — equal to 40 digits |
| F2 closure at all nine c/a points (numerics vs piecewise closed form; 60 vs 80 dps) | all agree to 40 digits |
| F4 hole polyhedra (6 vertices/8 faces; 4/4) vs 1/√2, 1/√6, √6/4, √6/12 | equal to 40 digits |
| Voronoi-vertex classes at the nine points (K13) | every class re-solved at 60 dps and confirmed as a Voronoi vertex and local maximum |
| per-branch replay ≡ PRED enumeration | bit-identical L2r, L3r |
| ★ with mpmath-derived atoms vs PRED's float atoms (they differ in the last ulp) | identical P_hit to 4 dp and identical coverage in all four PRED configurations |
| target re-evaluation for F9 (PRED's dict literal re-run with Λ bound) | reproduces PRED's 48-vector exactly at Λ = 220 MeV |
| percentiles | every value cross-checked against `scipy.stats.percentileofscore` |
| determinism | three full runs, identical scores, sweep and verdict tables |

---
## §12 — Contamination statement

- Read in this thread: the FORK prompt (after hashing); `audit/gates/PRED/scripts/pred_step2_nullmodel.py`; `PRED/output/step2_out.txt`; `PRED/gate_PRED_RESULT.md` in full (it states PRED's verdict and its ~6-bit reading of 1/α; this gate's scoring and verdict rule were fixed by the prompt and do not use those numbers).
- Read for the F10 citations only, by targeted search for verdict lines: `RANK/gate_RANK_RESULT.md`, `JHF/gate_JHF_deliverable.md`, `PT/gate_PT_prompt.md` (no PT result exists at this commit), `PROMOTE/gate_PROMOTE_result.md`.
- Directory listings of `audit/gates/`. Nothing else in the corpus was opened. No web search. Memory not enabled; no past-chat tools.

---
## §13 — What this gate does not establish

- It does not evaluate the physics of any branch, and it does not test the void geometry as geometry.
- SC-FORK-2 here means the forks are **indistinguishable by this score**. It does not mean the score was informative (CN-FORK-02). A statistic that does not saturate — per-target multiplicity, best error per target, or P_hit — was not pre-registered; any such follow-up needs its own prompt and digest.
- It does not say any BCT number is wrong; every ★ value is reproduced.
- It does not price the 1/α result beyond the registered count; CN-FORK-03 is a conjecture-level reading.

---
## §14 — Files (`audit/gates/FORK/`)

| file | SHA-256 |
|---|---|
| `gate_FORK_run.py` | `58cdb7a2ce450743b7de8c94d807d8c11f46926ba0ab329e301aa38e1ed2ee94` |
| `fork_map.md` | `a01e10b2a905075a5c7f8564a8f2ef98f259e08cde81fa72beb4b600a6485f6f` |
| `fork_scores.csv` (303 rows: 298 scored, 3 n/a, 2 map-only) | `6bbff5992b29ee2370d0c24ad883e0b778735638a309a27148106ce3f89e826f` |
| `fork_alpha_sweep.csv` (3,528 rows) | `54b9b3f3ccf357e044cce2e8379af1f8b1afe46e79e8d57f741c2d54dc844d17` |
| `gate_FORK_RESULT.md` | this file |

Reproduce: `python3 -I gate_FORK_run.py --repo <checkout at bc5c87dc> --prompt <curl'd prompt> --out <dir>` (about 19 minutes, 1.3 GB).

---
## Appendix A — post-hoc diagnostic behind CN-FORK-02 (not pre-registered)

```python
# python3 -I posthoc_nogeom.py gate_FORK_run.py
import importlib.util, sys
spec = importlib.util.spec_from_file_location('fork', sys.argv[1]); m = importlib.util.module_from_spec(spec)
sys.argv = ['x']; spec.loader.exec_module(m)
atoms_g = {k: v for k, v in m.ATOMS_PRED.items() if k not in ('roct', 'rtet', 'a0')}
L1, L2, L2r, L3r = m.enumerate_alphabet(atoms_g)
for lab, v in (('2-atom', L2r), ('3-atom', L3r)):
    vs = m.np.sort(m.np.abs(v))
    for tol in (0.01, 0.001):
        p, cov = m.score(vs, tol, False, 0.0, m.TV_PRED)
        print(lab, tol, round(p, 4), int(cov.sum()), [m.NAMES[i] for i in range(48) if not cov[i]])
```

Output: 81 / 55,280 / 9,533,225 distinct values; 2-atom 1 % → 48/48; 2-atom 0.1 % → 47/48 (m_μ/m_e); 3-atom 1 % → 48/48; **3-atom 0.1 % → 48/48**.
