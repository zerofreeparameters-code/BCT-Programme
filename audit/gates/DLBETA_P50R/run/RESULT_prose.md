# Gate DL-BETA P50R — result

**Verdict: SC-DLBPR-5 (void method failed).** At void L = 6 one branch run's 20 block means spread wider than the
card's integrity limit: the hot run at β = 1.2450 has a span of 0.00919 against 0.25·G = 0.00809, a ratio of 1.14.
Card §5 tests that before any comparison with Gate DL-BETA P50, so the gate stops there. **Nothing changes.
P50's β_c = 1.25771 ± 0.00107 stays CONJECTURE** — it is neither moved to REPLICATED nor flagged as not
reproduced. Every number is reported below.

**What the numbers say, for the record.** The second code's own measurement is
**β_c(P50R) = 1.25801 ± 0.00111** (so 1/e²_c = 0.88955 ± 0.00079), against P50's 1.25771 ± 0.00107:

> **D = β_c(P50R) − β_c(P50) = +0.00030**, with **U_D = 0.00155 (|D| = 0.19 U_D)** and
> **σ_D = 0.00042 (|D| = 0.71 σ_D)**. Both are inside their 2× thresholds.

Had the void integrity test passed, the ordered code would have been **SC-DLBPR-1** — agreement at statistical
precision. It did not pass, so that is a counterfactual, not the verdict. The two codes' β₅₀ at void L = 8 differ
by 0.00003 (0.14 σ_boot); at void L = 6 by 0.00076 (1.63 σ_boot).

**Checks.** K1 passes. All four K2 runs are within 2 % of their targets and **all four are bit-identical** to Gate
DL-BETA's stored series, comparing exact bits. K3 passes: Z4 at L = 12 is clean, bracketed and converged, with
β₅₀ = 1.01003 inside [1.0051, 1.0171]. No bracket extension was triggered on any lattice. On Z4 the same estimator
extrapolates to β_∞ = 1.01066 ± 0.00109, which is −0.44 U from the literature value 1.0111331 (Q6, not a verdict
input).

**Run.** 13 November 2026, 05:00–10:10 UTC (16:00–21:10 AEDT). Analyst: Claude; this session was configured as
`claude-fable-5-1`, and the runtime reported serving-model fallbacks to `claude-opus-5-5` and `claude-opus-5`
during the run, so the model serving any given step is not certain (§0). Simulation
05:03:35–09:51:22 UTC: 136 runs, 575.5 core-minutes (9.59 core-hours) on 2 cores. **This run was started as a
scheduled task (a fresh cloud session) at the user's request, rather than in a hand-opened thread inside the BCT
Project** (§0). Same-session results are capped at CONJECTURE.

---

## 0. Provenance and disclosures

**Card.** I fetched `audit/gates/gate_DLBETA_P50R_prompt.md` at commit
`dcf22c72170e55613be779718a19488f726ecc9e` with `curl` from its commit-pinned raw URL, wrote it to disk and hashed
it **before reading it**. Its record, `audit/gates/PREREG_20261113_DLBETA_P50R.sha256`, was hashed the same way.

| file | SHA-256 | expected | |
|---|---|---|---|
| `gate_DLBETA_P50R_prompt.md` | `767be760e0ccbfb0bd73c4da3d6748816ec77dd5f4daf0c671f9c041f9a05f3b` | same | match |
| `PREREG_20261113_DLBETA_P50R.sha256` | `7a640a088e9fd866401d4121a82444dc6e4e49baba0462ca1fc6f640833378a2` | same | match |

The record's content is the card's digest (`767be760…5f3b`).

**Repository.** `zerofreeparameters-code/BCT-Programme` was cloned and checked out at `dcf22c72…`; `origin/main`
was at the same commit, so the card's commit was also the head of main. All eleven §4.1 files were hash-checked
before use and all eleven match (`as_run/pins_check.txt`). The three code files were copied into a work directory
outside the repository and hashed again there; all three match.

**Environment.** Python 3.13.18, NumPy 2.5.3, SciPy 1.18.1, numba 0.68.1 (from `pip install numba==0.68.1`),
llvmlite 0.50.0. 2 cores, 7 GB RAM, 2 workers, one chain per core. These versions are exactly the toolchain Gate
DL-BETA recorded, which is what K2's bit-identity depends on.

**Disclosures.**

- **Scheduled task.** This run was started as a scheduled task (a fresh cloud session) at the user's request,
  rather than in a hand-opened thread inside the BCT Project. Card §10 asks the user to switch off "Search and
  reference past chats" and "Generate memory from chats" before opening such a thread. This session cannot see
  those settings. It called no memory, past-chat or Project tool, and read nothing but the §4.1 paths.
- **Analyst identity.** The session was configured as `claude-fable-5-1`. Partway through the simulation the
  runtime reported that the serving model had fallen back, first to `claude-opus-5-5` and then to `claude-opus-5`.
  Which model served which step is not recoverable from here, so no single model is claimed. This cannot affect a
  number: every number in this file was produced by the pinned code, and all of them are reproduced independently
  in §8.
- **Not blind.** The card states P50's result in §1, and so did this run. Under §4.7, `dlbpr_numbers.txt` was
  written, hashed and its hash posted in the conversation **before** the verdict step opened P50's `analysis.json`.
- **Seeds.** The 132 gate seeds run from 5,073,152 to 6,575,979, all distinct, all in the card's 5,000,000 (Z4)
  and 6,000,000 (void) families, and every one follows the §4.4 formula (verified independently, §8). None can
  coincide with Gate DL-BETA's, REP1's or P50's, which lie in lower families. K2 reuses Gate DL-BETA's four K3
  seeds on purpose.
- **Clean repository (R6).** The driver set `sys.dont_write_bytecode` and pointed numba's cache at the work
  directory. `git status` in the clone was empty before and after the run: running the original code wrote nothing
  into the repository.
- **Scripts written during the run.** `run/dlbpr_report.py` (Markdown tables) was written while the void chains
  ran. `run/dlbpr_crosscheck.py` (§8) and `run/dlbpr_assemble.py` (this file's assembly) were written after the
  verdict. None computes a verdict input; the report and assembler compute nothing at all.
- **Delivery.** The run prompt asked for a push first. This session cannot push: `gh auth status` reports the
  token invalid, and `git push --dry-run` is refused by the git proxy — "zerofreeparameters-code/BCT-Programme is
  not in this session's authorized repository set" — and no `add_repo` tool exists in this session. The proxy's
  README says policy denials are not to be retried or routed around. Delivery is therefore the card's
  `git format-patch` fallback, adding `audit/gates/DLBETA_P50R/` only, on top of `dcf22c72…`.

## 1. Code and checks (Q1)

**Card versus code.** Before running, I read `dlbpr_driver.py` and `dlbpr_rules.py` against the card:

- the two seed families and the round-half-even rule (§4.4);
- the four lattices, their branch points, windows, step and chain counts (§4.4);
- the 500 + 1500 branch runs and the 3000-sweep mixed chains, with row 0 of each series being the start (§4.2);
- E_end from the last 10 of the 50-sweep readings and E_mid from sweeps 1050–1500;
- the import of P50's `dlbp_analysis.py` unmodified, hash-checked at both the driver and the rules module, which
  is what makes every estimator, the bracket rule, the extension rule, the bootstrap seeds and the σ floor P50's;
- σ_∞,stat as √[((1+k)·σ_boot,big)² + (k·σ_boot,small)²], with no floor (§4.5 b);
- the verdict order and thresholds of §5, and the §4.7 refusals (no hash file, wrong P50 hash).

All agree. The driver calls the original simulator only through `run_job(spec)`, as §4.2 R2 requires. No mismatch
between card and code was found, before or after the run: **there is no correction notice** (§9).

{{KTABLE}}

K1 passes. Each K2 run is within 2 % of its target. **K2 bit-identity: yes for all four.** Every byte of every
series matches Gate DL-BETA's stored series, on both complexes and both starts — the forecast's 80 % branch. That
is consistent with the matching toolchain recorded above, and it means this session's rebuild of the original code
reproduces it exactly, not merely statistically. K3 passes.

## 2. Branches, φ and crossings, lattice by lattice (Q2, Q3)

Window chains ran 3000 sweeps from the mixed start: 4 chains per point on Z4, 6 on the void. Every chain's E_end,
f, E_mid and seed is in Appendix A. **No bracket extension was triggered on any lattice**: the driver's
`state.json` records `ext = []` for all four, so every grid is the card's fixed window and every seed is a fixed
one.

{{LATTICES}}

{{MARGINS}}

### The integrity failure at void L = 6 (the verdict)

The one failing run is **void L = 6, hot, β = 1.2450, seed 6059964**: E = 0.34018 ± 0.00052, block span 0.00919
against the limit 0.25·G = 0.00809 (ratio 1.14). Its 20 block means, each over 75 measurement sweeps, are

```
0.33502 0.33641 0.33996 0.34222 0.34054   0.33959 0.34039 0.33936 0.34142 0.34157
0.33810 0.33933 0.33675 0.34186 0.34421   0.34301 0.33916 0.34102 0.34229 0.34139
```

The minimum is the **first** block (0.33502) and the maximum is block 14 (0.34421). E at the end of the 500
thermalisation sweeps is 0.33620, and the first 100 measurement sweeps average 0.3350 against ≈0.3400 for the
rest: the chain was still relaxing upward from the hot start when measurement began. Excluding block 0 alone, the
span would be 0.00780, inside the limit. The run's mean is not anomalous — it sits +0.11 σ from P50's value at the
same point (0.34011 ± 0.00038) — so this is a within-run spread, not a disagreement about E.

Three observations, none of them a change to anything (§6's no-fit clause forbids that):

- β = 1.2450 is the hot branch point **closest to the transition**, where relaxation is slowest, and it is also
  where the limit is tightest, because G(β) is smallest there. It is the design's most fragile point by
  construction. P50's run at the same point had ratio 0.78 with the nearly identical limit 0.00820.
- The margin is thin on both codes and both gates: this run's z4 L = 8 worst ratio is 0.99 (hot, β = 0.9950), and
  P50's worst was 0.90 (hot, β = 0.990). A 500-sweep thermalisation against a 0.25·G spread limit is close to the
  edge wherever the branch nears the transition.
- The failure is **confined to one branch run on one lattice**. Every other branch run on all four lattices is
  clean, both branches are strictly decreasing everywhere, G > 0 at every window point, all four windows bracket
  the crossing without extension, and all four probit fits converge with zero bootstrap failures.

## 3. Result (Q4)

{{EXTRAP}}

**What U is made of.** Every σ_boot is below the 0.0007 floor (0.00034 at void L = 6, 0.00017 at void L = 8), so
both void σ are the floor, and σ_∞ is the floor's 1.53 × 0.0007 = 0.00107. The extrapolation shift is +0.00029
(β₅₀(6) − β₅₀(8) = −0.00063 unrounded), which raises U to 0.00111. The statistical part alone would give 0.00029. This is
P50R's own figure, a same-session single-code measurement, **CONJECTURE**, and under a verdict of SC-DLBPR-5 it
changes nothing in the ledger.

## 4. Diagnostics (Q5) and calibration (Q6) — reported, not verdict inputs

{{DIAG}}

- **Monotone.** φ has exactly one interpolation crossing on every lattice; none is flagged non-monotone.
- **Estimator spread on the void.** As in P50, the interpolation crossing sits above the probit β₅₀ (+0.00019 at
  L = 6, +0.00033 at L = 8) and the weak-fraction crossing higher still (+0.00042, +0.00078). Both are inside U.
- **φ's strong-side floor.** φ at the lowest window point is 0.134 (L = 6) and 0.088 (L = 8), against P50's 0.158
  and 0.109; at the top it reaches 0.958 and 0.953, against P50's 0.978 and 0.970. The same asymmetry P50 reported
  — φ does not reach 0 on the strong side but nearly reaches 1 on the weak side — appears on the second code, at
  slightly smaller magnitude. It is a property of the method, not of either implementation.
- **Time drift.** Between sweeps 1050–1500 and 2550–3000 the void crossings move down by 0.00127 (L = 6) and
  0.00053 (L = 8); P50's moved by 0.00020 and 0.00024. The L = 6 drift is larger than P50's and is about 1.1 U.
  It points the same way as the integrity failure above: at L = 6 this code's chains were still settling.
- **Cross-code branch energies** (§4.5 b R5; the 32 branch points are identical in the two gates, so they compare
  point by point):

| lattice | z (hot then cold) | rms \|z\| | max \|z\| |
|---|---|---|---|
| z4 L = 8 | 1.64, −0.97, −0.41, −2.03, 1.37, 2.01, 1.17, −0.93 | 1.42 | 2.03 |
| z4 L = 12 | −0.11, −0.59, −0.68, −0.24, 0.36, −0.15, 0.38, 0.33 | 0.40 | 0.68 |
| void L = 6 | 1.13, 1.41, −0.30, 0.11, 0.52, −0.50, −0.33, −0.89 | 0.77 | 1.41 |
| void L = 8 | 0.99, 0.83, 0.44, −1.34, 1.96, 2.55, 0.76, −0.70 | 1.37 | 2.55 |

  On both void lattices the rms is ≤ 1.5, the forecast's bound. The two codes agree on the energies themselves;
  the largest single deviation, 2.55 at void L = 8 cold β = 1.2700, is one point out of 32 and both runs are
  short-error runs where σ_E ≈ 10⁻⁴.

- **Cross-code β₅₀ and φ.**

| lattice | β₅₀(P50R) | β₅₀(P50) | difference | in σ (floor) | in σ_boot |
|---|---|---|---|---|---|
| z4 L = 8 | 1.00747 | 1.00640 | +0.00107 | +1.08 | +1.26 |
| z4 L = 12 | 1.01003 | 1.01045 | −0.00042 | −0.42 | −1.18 |
| void L = 6 | 1.25708 | 1.25784 | −0.00076 | −0.76 | −1.63 |
| **void L = 8** | **1.25772** | **1.25775** | **−0.00003** | **−0.03** | **−0.14** |

  φ(P50R) − φ(P50) at the common window points is small everywhere except at the steep middle of each window,
  where a difference in φ of 0.17 (void L = 6 at 1.2575) or 0.18 (z4 L = 8 at 1.0050) corresponds to a shift in β
  of well under one step: full lists are in `OUT/verdict.txt`.

- **Z4 calibration (Q6).** β_∞(Z4) = 1.01066 ± 0.00109, against 1.0111331 (hep-lat/0210010): **−0.00048 = −0.44 U**.
  P50 gave +0.00031 = +0.23 U on the same grid. The two codes bracket the literature value: they differ from each
  other by 0.00079 in β, which is 0.46 of their combined error (0.00172), and each error is dominated by the
  common floor and the extrapolation shift. Both are calibration observations, not verdict inputs.

## 5. Hash before comparison (§4.7)

| file | SHA-256 | hashed (UTC) | posted (UTC) |
|---|---|---|---|
| `dlbpr_numbers.txt` | `{{NUMHASH}}` | {{HASHED_AT}} | 09:54 (SendUserMessage), before the verdict step at {{VERDICT_AT}} |

The numbers step opened nothing of P50's and compared nothing; the verdict step is the only step that read
`DLBETA_P50/OUT/analysis.json`, and it verified that file's pinned hash before using it. There was one numbers
pass and one verdict run; no file was superseded.

## 6. Comparison and verdict (Q7)

`OUT/verdict.txt`:

```
{{VERDICT}}
```

Card §5's codes are tested in order, and the first that matches is the verdict:

- **SC-DLBPR-0** (method failed): K1, K2 and K3 all pass, so it does not apply.
- **SC-DLBPR-5** (void method failed): at void L = 6 the branches are **not clean** — the hot run at β = 1.2450
  has a block span of 0.00919 against its limit of 0.00809. **This matches, and it is the verdict.**
- The later codes are not reached. For the record, with |D| = 0.00030, U = 0.00111 and the two thresholds
  2 U_D = 0.00309 and 2 σ_D = 0.00084, the ordered code **had the void integrity passed** would have been
  SC-DLBPR-1 (|D| ≤ 2 σ_D). That is stated as a counterfactual and carries no weight.

**Effect.** Nothing changes. P50's β_c = 1.25771 ± 0.00107 (1/e²_c = 0.88933 ± 0.00076) **remains the quoted
value and remains CONJECTURE**: this gate neither raises it to REPLICATED nor flags it as not reproduced.
P50R's own β_c = 1.25801 ± 0.00111 is recorded beside it as a same-session figure, also CONJECTURE, and no
average is formed. The located transition [1.250, 1.255] is unaffected, and remains REPLICATED on its own
footing.

**What a re-run would need.** Card §5 says of SC-DLBPR-0 that one fixes the cause and re-runs under a new digest;
SC-DLBPR-5 says only that nothing changes and every number is reported. The cause here is not a code defect — the
code is Gate DL-BETA's own, bit-reproducing its stored series — but a thermalisation budget that is thin at the
branch point nearest the transition. Any successor card would be choosing a new sweep budget or a new integrity
rule, which is a design decision for a new pre-registration, not for this run.

**Also reported (§5):**

- D = +0.00030 = 0.19 U_D = 0.71 σ_D;
- the cross-code diagnostics of §4 above;
- Z4 calibration: −0.44 U (P50R) against +0.23 U (P50);
- K2 bit-identity: **yes, all four**;
- time drift: −0.00127 at void L = 6, −0.00053 at void L = 8.

## 7. Analyst's forecasts (card §8), scored

The card's forecasts were written by P50's analyst, who had seen P50's raw data but not this run's.

| forecast | outcome | score |
|---|---|---|
| K1–K3 pass: 90 % | all three pass | **hit** (Brier 0.010) |
| K2 bit-identical, all four: 80 % | all four bit-identical | **hit** (Brier 0.040) |
| Verdict: SC-DLBPR-1 55 %; -2 25 %; -0 7 %; **-5 5 %**; -3 5 %; -4 3 % | **SC-DLBPR-5** | **miss** — the outcome fell in a 5 % bin (multi-class Brier 1.276) |
| \|D\| ≤ 0.0005: 55 % | 0.00030 | **hit** (Brier 0.203) |
| \|β₅₀(void, L = 8; P50R) − 1.25775\| ≤ 0.001: 70 % | 0.00003 | **hit** (Brier 0.090) |
| Branch cross-code rms z ≤ 1.5 on both void lattices: 70 % | 0.77 and 1.37 | **hit** (Brier 0.090) |

Five of six hit. The one miss is the one that mattered: the forecast put 88 % on the run reaching a comparison at
all (codes -1, -2, -3, -4), 5 % on the void method failing and 7 % on a check failing. The physics forecasts were
well calibrated — |D| and β₅₀(L = 8) both came in far inside their bounds, and the cross-code rms z held — while
the forecast that the *procedure* would complete was overconfident. A single branch run out of 32, at the one
point where the margin was always thin, decided the gate.

## 8. Verification (after the verdict; not a verdict input)

`run/dlbpr_crosscheck.py` recomputes §4.5 from the raw `.npz` series rather than from the records' summary fields,
with different routines (`numpy.polyfit`, `scipy.optimize.curve_fit` with bounds) and re-derives every seed from
the §4.4 formula:

```
{{CROSSCHECK}}
```

**CROSS-CHECK PASS.** All 136 series hashes match their records; every gate seed follows §4.4 and all 132 are
distinct; every branch E, σ_E, E_end and E_mid is reproduced exactly from the series; the lines, every β₅₀ and w
match to 10⁻⁶; an independent 300-replica bootstrap with a different RNG gives σ_boot 0.00066, 0.00026, 0.00034
and 0.00018 (pinned: 0.00061, 0.00029, 0.00034, 0.00017); both extrapolations and all three verdict inputs are
reproduced; and the integrity verdict at every one of the 32 branch points — including the single FAIL — is
reproduced independently.

## 9. Correction notices

**None.** No mismatch between the card and the pinned code was found, before or after the run. No lattice, size,
grid, chain count, sweep count, seed rule, estimator, threshold or extension rule was changed. The numbers file
was written, hashed and posted once, and the verdict was run once.

## 10. Limits

- **The gate did not reach its question.** SC-DLBPR-5 means the second code's void measurement did not satisfy the
  card's own quality test, so this run is not evidence either way about whether the two codes agree. The agreement
  figures in §3 and §6 are reported, not established.
- **It replicates the code, not the method** (card §9). The estimator, grids, branch points, windows, chain counts
  and floor are P50's, so the method's systematics are shared and untested: the fixed-time estimator, straight
  branch lines, φ's strong-side floor, two sizes, and a U set by its floor. The present failure is in fact a
  symptom of one of those shared choices — the thermalisation budget — showing up on a different code.
- **Partly independent codes** (card §9). The two simulators were written in different threads, but share the
  card's model specification, numba's RNG and the Best–Fisher method.
- **K2 bit-identity tests the toolchain, not the physics** — though here it does establish that this session
  reproduced Gate DL-BETA's original code byte for byte.
- **The earlier cards' limits apply:** Wilson action only, β_t = β_s only, one spatial complex, bare couplings,
  a tree-level k, two sizes, and the order of the transition is not addressed.
- **Same-session cap.** Everything measured here is CONJECTURE.

## 11. Plain-language summary

The question was whether a number measured last night survives being measured again by a different program. The
number is the "tipping point" of electromagnetism simulated on the network of gaps between packed spheres, with
time added: below it the field is trapped, above it light travels freely. An earlier gate measured it as
1.25771 ± 0.00107 using one simulator. This gate re-ran exactly the same measurement — same box sizes, same
settings, same scoring, same arithmetic, only new random seeds — on the *other* simulator the programme had
written months earlier in a different session.

The second program agreed, and closely. It gives 1.25801 ± 0.00111, a difference of 0.0003, which is about a fifth
of the combined error bar and well inside even the much tighter purely statistical comparison. On the larger of the
two boxes the two programs' crossings differ by 0.00003 — three parts in a hundred thousand. As a side check, both
programs were pointed at an ordinary cubic lattice where the right answer is known from the literature; one lands
just above it and the other just below, each well within its error.

But the gate still fails, and it fails on a technicality that was written into the card in advance for good
reason. Before the comparison is allowed, each reference simulation must be *steady*: its output, chopped into
twenty consecutive chunks, must not wander by more than a quarter of the gap between the two phases. On the smaller
box, one of the eight reference runs wandered by 14 % more than that limit. Looking at it afterwards, the reason is
plain: the chunk that is furthest off is the very first one, and the simulation was still visibly settling down
from its starting state when measurement began. It needed a longer warm-up. That run sits at the setting closest to
the tipping point, where settling is slowest and where the allowed wander is smallest — the hardest spot in the
whole design, and the margin was thin for both programs everywhere near it.

The card's rules are applied in a fixed order, and "a reference run was not steady" is tested before "do the two
answers agree". So the verdict is that the method failed on this run, and the earlier number keeps exactly the
status it had: a conjecture resting on one program. It has not been contradicted — if anything the opposite — but
it has not been confirmed either, because the confirmation was not permitted to count. Fixing this would mean a new
card with a longer warm-up, which is a decision for the next pre-registration, not something this run may change.

One genuinely good piece of news came out of the checks. The four calibration runs that re-ran the original
program's own test cases came back *byte for byte identical* to the series stored months ago. The program was
rebuilt in a fresh machine from the repository and reproduced its old output exactly, not just statistically.

## 12. Files

Everything below `audit/gates/DLBETA_P50R/` is listed with SHA-256 in `MANIFEST.sha256`.

| path | what |
|---|---|
| `gate_DLBETA_P50R_RESULT.md` | this file |
| `as_run/gate_DLBETA_P50R_prompt.md`, `as_run/PREREG_20261113_DLBETA_P50R.sha256` | the card and its record, as fetched |
| `as_run/run_prompt.txt` | the run prompt (scheduled task) |
| `as_run/P50R_RUN_LOG.md` | timestamped log |
| `as_run/pins.sha256`, `as_run/pins_check.txt` | the §4.1 pins and their check |
| `run/dlbpr_driver.py`, `run/dlbpr_rules.py`, `run/dlbp_analysis.py` | the pinned code as run (hashes as §4.1) |
| `run/dlbpr_report.py`, `run/dlbpr_crosscheck.py`, `run/dlbpr_assemble.py` | report tables; independent cross-check; this file's assembly |
| `OUT/records/*.json`, `OUT/series/*.npz` | 136 run records (seeds, E, block means, readings every 50 sweeps, series hashes) and full series (E, E_s, E_t after every sweep, row 0 = start) |
| `OUT/state.json`, `OUT/analysis.json` | driver state (K1, K2, extensions); all estimators |
| `OUT/dlbpr_numbers.txt`, `OUT/dlbpr_numbers.sha256`, `OUT/dlbpr_numbers_hashed_at.txt` | numbers, their hash and the time |
| `OUT/verdict.txt`, `OUT/verdict_run_at.txt`, `OUT/verdict_stdout.txt` | verdict |
| `OUT/driver_log.txt`, `OUT/driver_stdout.txt`, `OUT/numbers_stdout.txt` | logs |
| `OUT/environment.txt` | host, cores, toolchain versions, commit |
| `OUT/tables.md`, `OUT/crosscheck_output.txt` | tables used here; cross-check output |

## 13. Timing

{{TIMING}}

The budget (card §4.6) was 615 core-minutes; the run took 575.5. Void L = 8 ran at 221 ms/sweep against the
card's 236, void L = 6 at 71 against 75, Z4 L = 12 at 39 against 42, Z4 L = 8 at 7.0 against 7.6. No sweep budget
was shortened.

## Appendix A — every mixed chain

{{APPA}}
