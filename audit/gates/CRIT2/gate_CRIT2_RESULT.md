# Gate CRIT2 — result

**Verdict: SC-CRIT2-1 (replicated).**
Independent code puts the L = 8 jump of compact U(1) on D4 triangles in the same interval
Gate CRIT reported, [0.610, 0.615], and the two-phase method at L = 12 and 16 gives
**β_∞ = 0.6150 ± 0.00125** (card convention), **β_KN = 1.2300 ± 0.0025** (Katz–Nógrádi
convention, β_KN = 2β).
**Separate check (section 6):** β_∞ − uncertainty = 0.61375 does not reach below 0.5601.
Gate CRIT's kill (SC-CRIT-2) **stands at infinite volume**.
**Status:** per card section 6, the Gate CRIT number moves from CONJECTURE to **REPLICATED**
(two codes, two threads) and β_∞ becomes the quoted value. β_∞ itself was computed by this code
only (section 11). Everything else in this file is a same-session result, capped at CONJECTURE.
**Run:** 8 October 2026, one fresh thread inside the BCT project. Analyst: Claude (Opus 5.5).

---

## 0. Provenance and blinding

**Card.** `audit/gates/gate_CRIT2_prompt.md`, commit `689c32742b88cbd7b4c9eb60482561bc55ba1c3d`,
fetched by commit-pinned raw URL to disk and hashed before it was read:
`b30436875a2b12ea9b38a4d5d366c1ab9fcad83bcfe0405b3af5974876df4c79` — matches the
pre-registered digest (and `PREREG_20261008_CRIT2.sha256`). Section 2 was read first.

**Earlier card** (permitted by section 2): `audit/gates/gate_CRIT_prompt.md` at the same commit,
`d3bbcab86fd91401a7d66196baaaa2f720e1e1a923adea513719c2adbd2cd10c`, matching the
`d3bbcab8…2cd10c` quoted in this card. It holds the lattice definition and the hypercubic and A4
validation figures, and no D4 number.

**Blinding.** `audit/gates/CRIT/`, `claude/gate_CRIT_RESULT.md`, `claude/gate_CRIT_LEDGER_ENTRY.md`
and the Gate CRIT memory file were not opened until all D4 numbers were written to
`crit2_numbers.txt` and hashed (22:41:21 AEDT, SHA-256 in section 4; the digest was posted to
the conversation before the first unblinded read). The repository was cloned only after that,
so `audit/gates/CRIT/` was not on disk during the run.

Incidental exposure, disclosed so it can be weighed — none of it is blocked material and none of
it contains β_CRIT:
- The thread's automatically loaded memory index showed the one-line *description* of the Gate
  CRIT memory file ("critical coupling of lattice electromagnetism on a BCT-shaped lattice, as a
  route to 1/137 — Michel's decision to try it"). No number. The file itself was not opened.
- The project's document list showed the blocked file *names*.
- The permitted cards themselves say Gate CRIT ended in a kill and give the kill line 0.5601, so
  it was known before the run that Gate CRIT's β_c lay above about 0.56 or below about 0.45.

SC-CRIT2-1 is therefore scorable.

**Environment.** Python 3.13.16, NumPy 2.5.3, SciPy 1.18.1, numba 0.68.0 (installed for this
run, as the card allows). 2 CPU cores, 2 simulations at a time (one per core). Total
simulation time about 46 minutes.

## 1. The code (written in this thread from card section 3)

`u1sim.py` (lattices, update, observables), `crit2.py` (stage driver: applies the card's
section 4–5 rules mechanically, reading each stage's numbers from the previous one and
refusing to rerun a recorded stage), `checks12.py` (checks 1–2), plus `unit_tests.py`,
`sampler_ks.py`, `make_numbers.py`, and the post-unblinding `crosscheck.py` and `gen_tables.py`.

- **D4:** sites are the even-sum points of Z⁴ in a periodic box of side L (one parity copy,
  L⁴/2 sites). 12 stored link directions per site (±eᵢ ± eⱼ with first non-zero entry +1).
  Triangles are generated from the translation classes of {0, r₁, r₁ + r₂}: the code finds
  **32** classes, builds 32 triangles per site and asserts 32 per site, **8 per link**, no
  duplicate triangle and no repeated link (asserted at L = 4, 6, 8, 12, 16). 96 triangles touch
  each site, as Celmaster counts.
- **Hypercubic:** Z⁴, 4 links and 6 square plaquettes per site; 6 per link asserted.
- **Update:** sequential single-link heat bath. The conditional distribution of a link is
  exp(β|A| cos(θ + arg A)) with A the sum over its 8 (D4) or 6 (hypercubic) staples; θ is drawn
  exactly from that von Mises law (Best–Fisher algorithm, written in a cancellation-free form).
  **One sweep = one heat-bath update of every link, in storage order.** No overrelaxation. This
  was fixed before the first run.
- **Observables:** E = mean of (1 − cos θ_p) over all stored plaquettes, measured after every
  sweep; C = N_p · var(E) (N_p = number of stored plaquettes, variance over the measurement
  sweeps). Error bars: 20 blocks for E, block jackknife for C (reporting only).
- **Seeds:** seed = 7919·L + round(10⁴·β) + s, s = 0 hot, 1 cold, 2 mixed. Ties in round()
  (β on a 0.00125 offset, e.g. 0.61375) are rounded half-to-even (Python), so 6137.5 → 6138;
  every seed is printed in the raw records. The RNG is seeded inside the compiled code and the
  starting configuration is drawn from it, so each run is fixed by its seed.
- **Mixed start (5.4):** links whose stored origin site has x₁ < L/2 set to θ = 0, all others
  uniform. E recorded every sweep; the outcome uses the readings after sweeps 50, 100, …, 2000,
  and "last 500 sweeps" = the 10 readings at sweeps 1550–2000.
- **Grid-extension rule (5.4) when no flip appears**, fixed in code before any mixed run: no
  weak win → add one 0.0025 step above; no strong win → one step below; repeat. Never triggered.

How this code differs from Gate CRIT's (learned after unblinding): one parity copy, not two;
sequential heat bath, not all links of one direction at once; a different seed rule, RNG and
sampler; numba, not NumPy. Shared: the card's lattice and action.

**Unit tests** (`unit_tests.txt`, `sampler_ks.txt`):
- Local action change from the staple equals the global recompute to 3 × 10⁻¹² (both lattices).
- Von Mises sampler against the exact distribution at κ = 0.05 to 40, 1,000,000 draws each,
  two seeds: 14 Kolmogorov–Smirnov p-values from 0.018 to 0.925; ⟨cos⟩ within 2.1σ of I₁/I₀ in
  every case.

## 2. Section 4 checks — all pass

**Checks 1 and 2** (L = 4; 1000 + 10,000 sweeps for the limits):

| Check | Lattice | Measured | Target | Deviation | Pass |
|---|---|---|---|---|---|
| 1 gauge invariance | HC | max ΔE = 4.4e-16, max Δcos = 4.1e-15 | 0 | — | yes |
| 1 gauge invariance | D4 | max ΔE = 2.2e-16, max Δcos = 3.6e-15 | 0 | — | yes |
| 2 β = 0.1, hot | HC | ⟨cos⟩ = 0.05003 ± 0.00017 | β/2 = 0.05 | +0.06% | yes |
| 2 β = 0.1, hot | D4 | ⟨cos⟩ = 0.05027 ± 0.00010 | β/2 = 0.05 | +0.54% | yes |
| 2 β = 20, cold | HC | E = 0.012526 ± 0.000007 | 1/(4β) = 0.012500 | +0.21% | yes |
| 2 β = 20, cold | D4 | E = 0.008612 ± 0.000004 | 11/(64β) = 0.008594 | +0.21% | yes |

The D4 strong-coupling value is +0.54% above β/2 because each D4 triangle lies in 3
tetrahedra: the series gives ⟨cos⟩ = u + 3u³ = 0.050311 with u = I₁(0.1)/I₀(0.1); measured
0.050271 ± 0.000097 (0.4σ). The +0.21% at β = 20 on both lattices is a correction of the
expected sign and size (higher-order weak-coupling terms and the finite-box mode count), well
inside the 2% allowed.

**Check 3** — hypercubic, L = 8, hot and cold, 1000 + 3000 sweeps:

| β | E hot | E cold | C hot | C cold | C_max |
|---|---|---|---|---|---|
| 0.9950 | 0.42678 ± 0.00064 | 0.42585 ± 0.00099 | 1.679 ± 0.113 | 2.023 ± 0.147 | 2.023 |
| 0.9975 | 0.42077 ± 0.00087 | 0.41897 ± 0.00089 | 2.160 ± 0.182 | 2.365 ± 0.245 | 2.365 |
| 1.0000 | 0.41285 ± 0.00115 | 0.41380 ± 0.00127 | 2.650 ± 0.278 | 2.344 ± 0.199 | 2.650 |
| 1.0025 | 0.40587 ± 0.00186 | 0.40896 ± 0.00117 | 4.115 ± 0.893 | 2.482 ± 0.340 | 4.115 |
| 1.0050 | 0.39712 ± 0.00301 | 0.40154 ± 0.00197 | 6.308 ± 2.314 | 3.815 ± 0.806 | 6.308 |
| **1.0075** | 0.36306 ± 0.00324 | 0.35995 ± 0.00435 | 6.902 ± 1.705 | 10.169 ± 2.592 | **10.169** |
| 1.0100 | 0.34823 ± 0.00149 | 0.34586 ± 0.00111 | 2.499 ± 0.495 | 2.127 ± 0.421 | 2.499 |
| 1.0125 | 0.34110 ± 0.00059 | 0.34102 ± 0.00065 | 1.383 ± 0.175 | 1.542 ± 0.116 | 1.542 |
| 1.0150 | 0.33725 ± 0.00065 | 0.33763 ± 0.00060 | 1.298 ± 0.150 | 1.463 ± 0.230 | 1.463 |
| 1.0175 | 0.33534 ± 0.00063 | 0.33424 ± 0.00034 | 1.119 ± 0.119 | 1.145 ± 0.094 | 1.145 |
| 1.0200 | 0.33151 ± 0.00026 | 0.33214 ± 0.00037 | 0.891 ± 0.035 | 0.947 ± 0.051 | 0.947 |

C maximum at **β = 1.0075** (cold start, C = 10.17), inside the required 1.000 to 1.012
(literature L = 8 pseudo-critical value ≈ 1.0074). **Pass.**
Largest fall in E, cold start: between 1.0050 and 1.0075 (0.04159).
**E\*_hc = 0.38074.**

**Check 4** — hypercubic, L = 12, mixed starts, 2000 sweeps, method of 5.4 with E\*_hc
(threshold band 0.37074 to 0.39074):

| β | E at start | E, mean of last 500 sweeps | E final | outcome | seed |
|---|---|---|---|---|---|
| 1.00200 | 0.5416 | 0.40746 | 0.40330 | strong | 105050 |
| 1.00700 | 0.5430 | 0.39272 | 0.39376 | strong | 105100 |
| 1.01200 | 0.5423 | 0.34499 | 0.34306 | weak | 105150 |
| 1.01700 | 0.5435 | 0.33694 | 0.33858 | weak | 105200 |
| 1.02200 | 0.5423 | 0.32971 | 0.32936 | weak | 105250 |

Flip interval **[1.007, 1.012]**, midpoint 1.0095. It contains 1.0111 itself, so it contains a
point within 0.006 of 1.0111. **Pass.** No grid extension. (The 1.007 run is a strong win by
0.0020; the check would still pass if it had been unresolved.)

Readings over the run:

| β | E after 250, 500, 750, …, 2000 sweeps |
|---|---|
| 1.00200 | 0.402 0.414 0.407 0.415 0.404 0.408 0.409 0.403 |
| 1.00700 | 0.404 0.400 0.406 0.390 0.402 0.394 0.395 0.394 |
| 1.01200 | 0.364 0.365 0.373 0.368 0.365 0.373 0.340 0.343 |
| 1.01700 | 0.351 0.334 0.331 0.337 0.336 0.335 0.338 0.339 |
| 1.02200 | 0.341 0.329 0.334 0.327 0.333 0.332 0.328 0.329 |

## 3. D4 runs

### 3.1 Locate (5.1) — L = 4, β 0.40 to 0.90 step 0.01, hot and cold, 500 + 2000 sweeps

| β | E hot | E cold | C hot | C cold | C_max |
|---|---|---|---|---|---|
| 0.4000 | 0.77599 | 0.77514 | 0.701 | 0.715 | 0.715 |
| 0.4100 | 0.76781 | 0.76915 | 0.696 | 0.741 | 0.741 |
| 0.4200 | 0.76138 | 0.76106 | 0.751 | 0.773 | 0.773 |
| 0.4300 | 0.75401 | 0.75366 | 0.769 | 0.777 | 0.777 |
| 0.4400 | 0.74601 | 0.74548 | 0.795 | 0.790 | 0.795 |
| 0.4500 | 0.73786 | 0.73775 | 0.803 | 0.810 | 0.810 |
| 0.4600 | 0.72905 | 0.72927 | 0.825 | 0.801 | 0.825 |
| 0.4700 | 0.72098 | 0.72118 | 0.843 | 0.860 | 0.860 |
| 0.4800 | 0.71150 | 0.71163 | 0.842 | 0.873 | 0.873 |
| 0.4900 | 0.70323 | 0.70272 | 0.975 | 0.929 | 0.975 |
| 0.5000 | 0.69302 | 0.69371 | 0.999 | 0.977 | 0.999 |
| 0.5100 | 0.68373 | 0.68384 | 1.000 | 1.059 | 1.059 |
| 0.5200 | 0.67197 | 0.67261 | 1.067 | 1.107 | 1.107 |
| 0.5300 | 0.66162 | 0.66029 | 1.135 | 1.157 | 1.157 |
| 0.5400 | 0.64855 | 0.64912 | 1.149 | 1.142 | 1.149 |
| 0.5500 | 0.63606 | 0.63443 | 1.299 | 1.441 | 1.441 |
| 0.5600 | 0.62065 | 0.62058 | 1.431 | 1.561 | 1.561 |
| 0.5700 | 0.60558 | 0.60580 | 1.684 | 1.731 | 1.731 |
| 0.5800 | 0.58795 | 0.58613 | 1.879 | 1.820 | 1.879 |
| 0.5900 | 0.55948 | 0.56458 | 3.333 | 2.482 | 3.333 |
| 0.6000 | 0.52287 | 0.52707 | 9.355 | 6.455 | 9.355 |
| **0.6100** | 0.42502 | 0.43820 | 6.496 | 9.773 | **9.773** |
| 0.6200 | 0.39455 | 0.39237 | 2.624 | 2.013 | 2.624 |
| 0.6300 | 0.37427 | 0.37624 | 1.652 | 1.465 | 1.652 |
| 0.6400 | 0.36189 | 0.36228 | 1.242 | 1.324 | 1.324 |
| 0.6500 | 0.35045 | 0.35101 | 1.091 | 1.105 | 1.105 |
| 0.6600 | 0.34095 | 0.33944 | 0.939 | 0.977 | 0.977 |
| 0.6700 | 0.33114 | 0.33152 | 0.866 | 0.816 | 0.866 |
| 0.6800 | 0.32277 | 0.32281 | 0.864 | 0.814 | 0.864 |
| 0.6900 | 0.31449 | 0.31458 | 0.708 | 0.697 | 0.708 |
| 0.7000 | 0.30813 | 0.30906 | 0.681 | 0.691 | 0.691 |
| 0.7100 | 0.31406 | 0.30180 | 0.712 | 0.647 | 0.712 |
| 0.7200 | 0.29520 | 0.29393 | 0.596 | 0.614 | 0.614 |
| 0.7300 | 0.28852 | 0.28907 | 0.540 | 0.588 | 0.588 |
| 0.7400 | 0.28280 | 0.28376 | 0.572 | 0.529 | 0.572 |
| 0.7500 | 0.27771 | 0.27846 | 0.507 | 0.553 | 0.553 |
| 0.7600 | 0.27305 | 0.27274 | 0.507 | 0.491 | 0.507 |
| 0.7700 | 0.26774 | 0.26797 | 0.475 | 0.478 | 0.478 |
| 0.7800 | 0.26271 | 0.26347 | 0.476 | 0.447 | 0.476 |
| 0.7900 | 0.25865 | 0.25874 | 0.464 | 0.430 | 0.464 |
| 0.8000 | 0.26533 | 0.25417 | 0.435 | 0.425 | 0.435 |
| 0.8100 | 0.26164 | 0.24994 | 0.424 | 0.407 | 0.424 |
| 0.8200 | 0.24616 | 0.24647 | 0.380 | 0.394 | 0.394 |
| 0.8300 | 0.24185 | 0.24226 | 0.373 | 0.384 | 0.384 |
| 0.8400 | 0.23829 | 0.23885 | 0.369 | 0.360 | 0.369 |
| 0.8500 | 0.24582 | 0.23489 | 0.364 | 0.352 | 0.364 |
| 0.8600 | 0.23154 | 0.23144 | 0.336 | 0.357 | 0.357 |
| 0.8700 | 0.22849 | 0.22838 | 0.326 | 0.340 | 0.340 |
| 0.8800 | 0.23527 | 0.22464 | 0.322 | 0.300 | 0.322 |
| 0.8900 | 0.22196 | 0.22206 | 0.321 | 0.323 | 0.323 |
| 0.9000 | 0.21917 | 0.21940 | 0.293 | 0.303 | 0.303 |

**β₀ = 0.61** (cold start, C = 9.77; the hot maximum is 9.35 at 0.60).

Side observation: hot starts at β = 0.71, 0.80, 0.81, 0.85 and 0.88 sit above their cold
partners by 0.011 to 0.012, deep in the weak-coupling phase — trapped flux after the quench on
the small torus. Not near β₀ and not used.

### 3.2 Fine scan (5.2) — L = 8, β₀ ± 0.030 step 0.005, hot and cold, 2000 + 4000 sweeps

| β | E hot | E cold | C hot | C cold | C_max |
|---|---|---|---|---|---|
| 0.5800 | 0.58749 ± 0.00022 | 0.58781 ± 0.00022 | 2.037 ± 0.071 | 1.889 ± 0.073 | 2.037 |
| 0.5850 | 0.57780 ± 0.00029 | 0.57817 ± 0.00035 | 2.187 ± 0.094 | 2.336 ± 0.121 | 2.336 |
| 0.5900 | 0.56674 ± 0.00023 | 0.56688 ± 0.00024 | 2.334 ± 0.141 | 2.411 ± 0.097 | 2.411 |
| 0.5950 | 0.55391 ± 0.00049 | 0.55459 ± 0.00029 | 2.773 ± 0.161 | 2.574 ± 0.168 | 2.773 |
| 0.6000 | 0.53959 ± 0.00042 | 0.53971 ± 0.00047 | 2.992 ± 0.208 | 3.150 ± 0.173 | 3.150 |
| 0.6050 | 0.52209 ± 0.00056 | 0.52101 ± 0.00075 | 3.575 ± 0.196 | 4.189 ± 0.442 | 4.189 |
| **0.6100** | 0.49710 ± 0.00109 | 0.50193 ± 0.00089 | 6.320 ± 0.677 | 4.654 ± 0.399 | **6.320** |
| 0.6150 | 0.40838 ± 0.00066 | 0.40808 ± 0.00060 | 3.374 ± 0.233 | 2.795 ± 0.320 | 3.374 |
| 0.6200 | 0.39526 ± 0.00035 | 0.39570 ± 0.00037 | 2.203 ± 0.108 | 2.219 ± 0.138 | 2.219 |
| 0.6250 | 0.38587 ± 0.00018 | 0.38599 ± 0.00019 | 1.602 ± 0.058 | 1.787 ± 0.066 | 1.787 |
| 0.6300 | 0.37746 ± 0.00016 | 0.37745 ± 0.00018 | 1.543 ± 0.077 | 1.487 ± 0.041 | 1.543 |
| 0.6350 | 0.37029 ± 0.00020 | 0.37048 ± 0.00015 | 1.337 ± 0.043 | 1.421 ± 0.041 | 1.421 |
| 0.6400 | 0.36385 ± 0.00015 | 0.36394 ± 0.00014 | 1.276 ± 0.040 | 1.210 ± 0.037 | 1.276 |

- **β₈ = 0.610** (hot start, C = 6.32). Interior; no extension.
- **Jump interval (L = 8), hot: [0.610, 0.615]**, E 0.49710 → 0.40838 (fall 0.08873).
- **Jump interval (L = 8), cold: [0.610, 0.615]**, E 0.50193 → 0.40808 (fall 0.09385).

No run at L = 8 tunnelled between phases in 4000 sweeps. Hot and cold starts end in the same
phase at every β; at 0.610 their energies differ by 0.0048 (3.4σ on the block errors) inside
the strong phase.

### 3.3 Cold scan (5.3) — L = 12, β₈ ± 0.020 step 0.005, cold, 500 + 1500 sweeps

| β | E cold | C cold | seed |
|---|---|---|---|
| 0.5900 | 0.56664 ± 0.00022 | 2.594 ± 0.137 | 100929 |
| 0.5950 | 0.55384 ± 0.00021 | 2.754 ± 0.232 | 100979 |
| 0.6000 | 0.54046 ± 0.00028 | 3.176 ± 0.318 | 101029 |
| 0.6050 | 0.52376 ± 0.00036 | 3.279 ± 0.395 | 101079 |
| 0.6100 | 0.50075 ± 0.00076 | 7.329 ± 1.356 | 101129 |
| 0.6150 | 0.40890 ± 0.00040 | 3.362 ± 0.254 | 101179 |
| 0.6200 | 0.39567 ± 0.00019 | 1.880 ± 0.076 | 101229 |
| 0.6250 | 0.38613 ± 0.00011 | 1.643 ± 0.095 | 101279 |
| 0.6300 | 0.37798 ± 0.00012 | 1.513 ± 0.103 | 101329 |

**Jump interval (L = 12): [0.610, 0.615]**, E 0.50075 → 0.40890 (fall 0.09185).
**E\* = 0.45482.** The cold start at 0.610 melted into the strong-coupling phase.

### 3.4 Mixed-phase starts (5.4), L = 12

β = 0.6125 ± 0.0075, step 0.0025 (centre = midpoint of the L = 12 jump interval), 2000 sweeps.
Strong wins above 0.46482, weak wins below 0.44482.

| β | E at start | E, mean of last 500 sweeps | E final | outcome | seed |
|---|---|---|---|---|---|
| 0.60500 | 0.5329 | 0.52330 | 0.53076 | strong | 101080 |
| 0.60750 | 0.5316 | 0.51235 | 0.50998 | strong | 101105 |
| 0.61000 | 0.5316 | 0.49981 | 0.49750 | strong | 101130 |
| 0.61250 | 0.5322 | 0.48119 | 0.48032 | strong | 101155 |
| 0.61500 | 0.5328 | 0.41193 | 0.41503 | weak | 101180 |
| 0.61750 | 0.5322 | 0.40082 | 0.39881 | weak | 101205 |
| 0.62000 | 0.5310 | 0.39665 | 0.40063 | weak | 101230 |

**β_mix(12) = 0.61375**; flip interval **[0.6125, 0.6150]**, monotonic, no unresolved point,
no extension.

| β | E after 250, 500, 750, …, 2000 sweeps |
|---|---|
| 0.60500 | 0.527 0.522 0.519 0.520 0.525 0.522 0.520 0.531 |
| 0.60750 | 0.510 0.503 0.512 0.517 0.514 0.509 0.512 0.510 |
| 0.61000 | 0.506 0.505 0.492 0.496 0.506 0.502 0.502 0.498 |
| 0.61250 | 0.478 0.486 0.474 0.481 0.476 0.485 0.476 0.480 |
| 0.61500 | 0.453 0.435 0.416 0.414 0.409 0.406 0.413 0.415 |
| 0.61750 | 0.409 0.401 0.400 0.399 0.405 0.401 0.401 0.399 |
| 0.62000 | 0.405 0.401 0.392 0.397 0.395 0.396 0.393 0.401 |

### 3.5 Mixed-phase starts (5.4), L = 16

β = β_mix(12) ± 0.005, step 0.0025, 2000 sweeps, same E\*.

| β | E at start | E, mean of last 500 sweeps | E final | outcome | seed |
|---|---|---|---|---|---|
| 0.60875 | 0.5228 | 0.50497 | 0.50520 | strong | 132794 |
| 0.61125 | 0.5240 | 0.49101 | 0.49717 | strong | 132818 |
| 0.61375 | 0.5237 | 0.46668 | 0.46178 | strong | 132844 |
| 0.61625 | 0.5232 | 0.40573 | 0.40521 | weak | 132868 |
| 0.61875 | 0.5238 | 0.39934 | 0.40246 | weak | 132894 |

**β_mix(16) = 0.6150**; flip interval **[0.61375, 0.61625]**, monotonic, no unresolved point,
no extension.

| β | E after 250, 500, 750, …, 2000 sweeps |
|---|---|
| 0.60875 | 0.505 0.506 0.505 0.508 0.509 0.506 0.506 0.505 |
| 0.61125 | 0.495 0.493 0.494 0.489 0.495 0.491 0.491 0.497 |
| 0.61375 | 0.460 0.468 0.468 0.470 0.473 0.465 0.464 0.462 |
| 0.61625 | 0.417 0.406 0.406 0.404 0.402 0.405 0.406 0.405 |
| 0.61875 | 0.404 0.400 0.402 0.398 0.400 0.400 0.398 0.402 |

### 3.6 Result (5.5)

| Quantity | Card convention (β) | Katz–Nógrádi (β_KN = 2β) |
|---|---|---|
| β₀ (L = 4) | 0.61 | 1.22 |
| β₈ (L = 8, C maximum) | 0.610 | 1.220 |
| Jump interval L = 8 (hot and cold) | [0.610, 0.615] | [1.220, 1.230] |
| Jump interval L = 12 | [0.610, 0.615] | [1.220, 1.230] |
| β_mix(12) | 0.61375, interval [0.6125, 0.6150] | 1.2275 |
| β_mix(16) | 0.6150, interval [0.61375, 0.61625] | 1.2300 |
| **β_∞ = β_mix(16)** | **0.6150 ± 0.00125** | **1.2300 ± 0.0025** |

Uncertainty = max(half the L = 16 flip interval = 0.00125, |β_mix(16) − β_mix(12)| = 0.00125)
= 0.00125.

**ΔE at L = 16** (end-state E, mean of the last-500-sweep readings, of the nearest strong-win
run below β_∞, at 0.61375, minus the nearest weak-win run above it, at 0.61625):
**0.0609** (0.0566 from the final-sweep values).

## 4. Hash before unblinding

`crit2_numbers.txt` (all section 5 D4 numbers, generated by `make_numbers.py` from the raw
records): **SHA-256 `e640b88f0ae9ee4dd7c7bc8adc81ac8013938e92b8da4ec16c5fb8555d0e11a1`**,
written 22:41:21 AEDT, 8 October 2026, and posted to the conversation before
`gate_CRIT_RESULT.md` was opened.

## 5. Unblinding

Gate CRIT's result, section 4: at L = 8 both runs sit on the strong-coupling side at 0.610
(E = 0.4990 hot, 0.5017 cold) and the weak-coupling phase first appears at 0.615 (E = 0.409);
"the transition therefore lies between 0.610 and 0.615 at L = 8". Its quoted β_c = 0.610 ± 0.005
is the C-maximum grid point.

**β_CRIT = [0.610, 0.615].**

## 6. Verdict

| Condition (card section 6) | Required | Found | Met |
|---|---|---|---|
| Section 4 checks | all pass | all pass | yes |
| β₈ to the nearer end of β_CRIT | ≤ 0.005 | 0.610 to 0.610: **0.000** | yes |
| \|β_∞ − β₈\| | ≤ 0.015 | \|0.6150 − 0.610\| = **0.005** | yes |
| Blinding (section 2) | not broken | not broken (section 0) | yes |

**SC-CRIT2-1 (replicated).** SC-CRIT2-2 would have needed β₈ more than 0.010 from β_CRIT.

The two codes agree beyond the verdict test: both put the L = 8 jump in the same 0.005 step,
from both starts, with the same size of fall (≈ 0.09), and both C-maximum estimators land on
0.610.

## 7. Separate check: Gate CRIT's kill

β_∞ ± uncertainty = [0.61375, 0.61625]. The lower end is 0.054 above 0.5601 (about 43 times
the uncertainty). **The kill is not reopened; it stands at infinite volume.** Nothing else
about the 1/137 argument is touched here (card section 7).

## 8. Cross-code comparison (after unblinding; not a verdict input)

`crosscheck_vs_CRIT.txt` compares E run by run with Gate CRIT's published tables. Gate CRIT
publishes no error bars; its array holds two copies, so its error is taken as this code's
divided by √2. Approximate.

- **L = 4**, 15 (β, start) comparisons at 10 shared grid points away from the jump (β = 0.60
  left out, and hot starts at β ≥ 0.70, where trapped flux appears): rms deviation 1.00σ,
  largest 2.4σ.
- **L = 8, cold starts**, all 9 β: rms 1.19σ, largest 2.6σ (at 0.605, next to the jump, where
  block errors understate autocorrelation).
- **L = 8, hot starts:** rms 2.06σ. Gate CRIT's hot starts run slightly high against this code
  across the grid (8 of 9 differences have Gate CRIT higher; mean −1.3σ; rms 1.31σ without
  β = 0.620). The largest gap is at 0.620 (5.0σ), where Gate CRIT's own hot run sits 0.0016 above
  its own cold run, while this code's hot and cold runs and Gate CRIT's cold run all agree.
  Read as slower relaxation of hot starts in Gate CRIT's runs; not investigated. Since the cold
  starts agree, it does not point to a difference in the simulated model.
- Both codes show hot-start flux traps on the L = 4 torus deep in the weak phase (Gate CRIT at
  0.90 and above on its grid; this code at 0.71 to 0.88).

## 9. Observations (not verdict inputs; CONJECTURE)

- **First order, more firmly.** The fall in E across the jump grid step is 0.089 to 0.094 at
  L = 8 and 0.092 at L = 12, not shrinking with size. Every mixed start at L = 12 and 16 resolved, the
  flip moved only 0.00125 from L = 12 to 16, and no scan run at L ≥ 8 tunnelled in thousands of
  sweeps. All of this is what a first-order transition with a large latent gap does.
- **A partly mixed run at the flip.** Extrapolating the pure strong branch (`branch_fit.py`:
  linear and quadratic fits pooled over the L = 8 hot, L = 8 cold and L = 12 cold scans,
  0.600–0.610; weak branch 0.615–0.625) gives E ≈ 0.480–0.486 at 0.61375 and ≈ 0.487–0.491 at
  0.6125. Fits to a single scan spread wider. The L = 16 strong-win run at 0.61375 settled within
  about 50 sweeps and then stayed between 0.454 and 0.475; its last-500 mean, 0.467, is 0.013 to
  0.019 below the branch. A slab of each phase with slow interfaces is a plausible reading. The L = 12 run at 0.6125 (E ≈ 0.481) is only 0.006 to 0.010 below its
  branch. The L = 16 run counts as a strong win by 0.0019 (threshold 0.46482).
- **ΔE and the latent gap.** The fall of ≈ 0.09 across one grid step in the scans includes the
  slope of E(β) on each branch. At fixed β = 0.615 the extrapolated branches differ by
  ≈ 0.064 to 0.073. With pure phases, the two L = 16 runs either side of β_∞ would differ by
  ≈ 0.075 to 0.081; the measured ΔE(L = 16) = 0.061 is about 0.014 to 0.020 lower, consistent
  with the partly mixed strong-side run. Reported as the card defines it.
- **What the C maximum measures.** With no tunnelling, C is largest in the strong phase just
  below the jump, so β₈ = 0.610 marks the last strong grid point, not the jump. Of the
  +0.005 from β₈ to β_∞, +0.0025 is this offset (β₈ = 0.610 against the L = 8 jump midpoint
  0.6125); β_∞ sits a further +0.0025 above that midpoint, and the shift from β_mix(12) to
  β_mix(16) is +0.00125.
- β_KN = 1.2300 is also k·β at the transition (k = 2): 22% above the hypercubic 1.0111.

## 10. Analyst's disclosure (card section 8), scored

The card's author had read Gate CRIT's result before writing these forecasts.

| Forecast | Outcome | Score |
|---|---|---|
| Section 4 checks pass | all pass | Hit |
| SC-CRIT2-1; β₈ inside or touching the CRIT interval | SC-CRIT2-1; β₈ = 0.610, touching the lower end | Hit |
| β_∞ above β₈ by 0.002 to 0.008, by analogy with the hypercubic +0.004 | +0.005 | Hit on the number; the stated reason is only half of it (section 9: about half the shift is estimator offset) |
| First order: mixed-phase resolves at L = 16 within 2000 sweeps except at one grid point at most | all 5 resolved (one by a 0.0019 margin) | Hit |
| ΔE at L = 16 between 0.06 and 0.10 | 0.0609 (mean of the last-500-sweep readings, the reading used throughout); 0.0566 from the final-sweep values | Marginal: a hit by 0.0009 on the reading used, a miss on the final-sweep reading. Pulled low by the partly mixed strong-side run (section 9) |
| Gate CRIT's kill stands | stands at infinite volume | Hit |

The card's five forecast bullets, with the fourth split into its two parts: five hits (one of
them, the β_∞ shift, right on the number but only half right on the reason) and one marginal
(ΔE).

## 11. Limits

- Wilson action, one completion of FCC into four dimensions, bare couplings — as stated in the
  card. No physical coupling at the transition is measured.
- β_∞ is computed by one code. What the two codes independently agree on is the L = 8 interval
  and the energies on both sides of it. The card's rule makes β_∞ the quoted value under
  SC-CRIT2-1; a second code at L = 12 and 16 would make that specific number two-code too.
- The β_∞ uncertainty is the card's grid-based rule (0.00125). It has no statistical error
  attached; with one mixed run per β, an unlucky outcome next to the flip could move β_mix by
  one step (0.0025).
- The mixed-phase method assumes a first-order transition (card section 9). The evidence
  supports that assumption, but the gate does not test it.

**Readings of the card's wording** (fixed before the runs they affect; none changes a result):
- *Seed rounding.* round(10⁴·β) at β ending in 0.00125 is a tie; Python rounds half to even.
  For 0.61125 and 0.61625 that gives seeds 1 lower than rounding half up. No effect on any
  outcome rule.
- *"Mean E of the last 500 sweeps".* Taken as the 10 recorded readings at sweeps 1550–2000.
  Using all 500 sweeps instead gives the same outcome for every mixed run (smallest margin
  0.0015). Using only the final sweep would make the L = 16 run at 0.61375 unresolved.
- *"End-state E" for ΔE.* Taken as the same last-500 mean; the final-sweep value is also
  reported. This choice decides whether the ΔE forecast scores as a hit (section 10).
- *"Links starting at a site with x₁ < L/2".* The card does not fix link orientation for the
  mixed start; the code uses each link's stored origin site (positive direction).

## 12. Tier movements (as card section 6 fixes them)

| # | Statement | Tier |
|---|---|---|
| 1 | β_c of compact U(1), Wilson action, D4 triangles: Gate CRIT's L = 8 location [0.610, 0.615] | **REPLICATED** (two codes, two threads), from CONJECTURE |
| 2 | Quoted value: β_c = β_∞ = 0.6150 ± 0.00125 (β_KN = 1.2300 ± 0.0025) | **Quoted value** per section 6, as the infinite-volume figure for the replicated number. Computed by one code (this one), so the figure itself is single-code; see section 11 |
| 3 | Gate CRIT's kill (SC-CRIT-2) | **Stands at infinite volume** (section 6 check) |
| 4 | The D4 transition is first order | OBSERVATION, strengthened (section 9); not tested |
| 5 | BCT void geometry | No movement (card section 7) |

## 13. Plain-language summary

Earlier today Gate CRIT measured a new number: the "tipping point" of electromagnetism
simulated on the four-dimensional lattice whose slices are the BCT/FCC packing. It found the
tip between 0.610 and 0.615, with one program, on boxes up to 8 across. A number measured once
by one program could be a bug.

This gate wrote a completely separate program from the written recipe alone, without looking
at the first program or its answer, and measured again. First it had to pass four tests. Two
checked basic correctness on both lattices. The other two used the ordinary cubic lattice,
where the answer is known (1.0111): it found 1.0075 on a small box and 1.007–1.012 with the
two-phase method, both right. Then on the BCT-shaped lattice it found the
tipping point in exactly the same place, between 0.610 and 0.615, from both starting
conditions. Only then was the sealed answer opened.

It also went bigger, to boxes 12 and 16 across, and used a method made for a sudden
(first-order) transition: start half the box ordered and half disordered, and see which side
takes over. That pins the tipping point for an infinitely large box at **0.615, give or take
0.001**.

So the good news, plainly: **the number is real.** Two independent programs agree, and it now
holds at much larger sizes, with an error four times smaller. As far as Gate CRIT's
literature search found, nobody had published this figure for this lattice; now it is also
replicated. The same result also means the earlier kill stands: the
borrowed 1/137 argument still does not survive the move to the BCT-shaped lattice, now at
infinite size as well as on small boxes. And the transition really does look sudden rather
than gradual.

## 14. Files

Code (`audit/gates/CRIT2/run/`) and raw outputs (`audit/gates/CRIT2/out/`), SHA-256:

| File | SHA-256 |
|---|---|
| `run/branch_fit.py` | `c566b28b6f4568106afbe783f346b404c95d3eeae55a1e1858113ea26df1b2a7` |
| `run/checks12.py` | `7a41dd3e7536432977891a4745c59b75849ddb308f23f03f2fdc389770f4413e` |
| `run/crit2.py` | `913390c0b127fa083f555c2f0d3102fe40c96a075bd2ca8a391dd63a390736e8` |
| `run/crosscheck.py` | `0c43cfa442efe3942038bd564bedb8fa7229d734c4df4b3b8beda4c9f30ffdf4` |
| `run/gen_tables.py` | `277782b511fd5fb2c0a1533ab37a1f87ce9d38deeb782627614850af84ee880c` |
| `run/make_numbers.py` | `187b5c0c382f5a78831b8d01d64aae4002d5f15d571da809113d73728a8b672d` |
| `run/sampler_ks.py` | `9a45c2ef7a9a67e2c9923fa6f4cb578c4126b12a1d478619b5067d5ee5bd189a` |
| `run/u1sim.py` | `c1242154236a05c66a82c854d5bed3ffe5a5b0eaaa222c9ba26e88efab03e5ac` |
| `run/unit_tests.py` | `a9b86b634728fb565ae30d667b33b6eb97015abcbb23637ddb5403c8f379115c` |
| `run/RESULT_template.md` | `912e59138bee8301f4279dca1949d5eb6c7b4cd81142f54e2db82f0a2c9a90a7` |
| `out/branch_fit.txt` | `6669cfc97f7492f81b08781a4430eeae2f94539eef4256708ed1ffcb9751c4fe` |
| `out/check3.jsonl` | `9437a3e0bfbf01ddae576e1a19e007d991e0f810ee5f451904735629fb62df9d` |
| `out/check3.txt` | `60d74f5d9e62912457d6e0590ccd7d6298e3087b10c11e98f609f192840f8776` |
| `out/check3_series.npz` | `2bb5c5d841414789dd9c3d081ff08b5f1891aeb276cf9e9f1a200dd0c201e150` |
| `out/check4.jsonl` | `0b889d40a460cc7216e32651e5c23b12b9ab5c2df2c6962cfe224da0619bf3e3` |
| `out/check4.txt` | `1279545306551e312535d4c676bde67c02751c9df831a758247915816b1b006d` |
| `out/check4_series.npz` | `aded7bcc6d578eab0ee08d86617dfab69915771ca5bbff537e050e6c777f71f4` |
| `out/checks12.json` | `4ce4fbda6843c79b401ff11f2c5e0c979de6846dfdc7afed54043e3f79651176` |
| `out/checks12.txt` | `b3152b2f46dd5afa6e6749be0597f163eaeb0a3d955d2125d265aea74a5f20e7` |
| `out/crit2_numbers.txt` | `e640b88f0ae9ee4dd7c7bc8adc81ac8013938e92b8da4ec16c5fb8555d0e11a1` |
| `out/crosscheck_vs_CRIT.txt` | `6d6010a6e254a84ffabc33a5d06d0d5453f6d5ff1ce4917c06d15025ca71910f` |
| `out/s51.jsonl` | `7694020560317b4df0fba45f87a9a30c53d9a41fb2476e00bc189629610250e8` |
| `out/s51.txt` | `95d016ed836c9717bd0166afffa62c1c76e3f0fe0e3a4bbb01ea5a9c5ff7e90b` |
| `out/s51_series.npz` | `0037e0b0b942b4a4cc4da4051ee9a547734c108624db93d7c959ecf16e75f763` |
| `out/s52.jsonl` | `dc4809a3a89a4dab325ec85c5a1b9a64810e7f1df73b406d7b73fd3647a43962` |
| `out/s52.txt` | `e242b4a0737df907474f53bb42e5bca2e41940b8900c50bf224de9e9fa41de34` |
| `out/s52_series.npz` | `5ff8a05c5b1ab505c2f2f4721115b79276b2c5c6b8864404634c7615223754d7` |
| `out/s53.jsonl` | `ff4e49cef0f82f8ffae9538aec811eba99b7ad7967b5ea542f7d3cee0e72fc57` |
| `out/s53.txt` | `130078f753ba28be4cdb048daef67ef8f3d22a5c3ac59398d5e4db38ed87c6ab` |
| `out/s53_series.npz` | `2debd2eed40fb23d2c242ef3dc5da86cb14d3621af68a5b28cabcd6e17402d15` |
| `out/s54a.jsonl` | `36204e0fe285e118d12292395c4c2f8d605af1837071231da664c18338ff9c31` |
| `out/s54a.txt` | `949c421fdcb4dc432d5acf08798eacbd37bed39f255b6f757604434d370780f8` |
| `out/s54a_series.npz` | `8e33da2b2dbfd773b58e663a12348a383eba5f88cdb1dd696deca7ad5fe09a70` |
| `out/s54b.jsonl` | `9935bb9afb9fa0f9127bfc11fe7823d63fb4ce812617fda0a1c3da9abfb0e097` |
| `out/s54b.txt` | `7f395ac7ce48cac398ec17490d2a443dfb6ec5ee8ae5652a6ceae13a9eb48ed2` |
| `out/s54b_series.npz` | `9becf0ac6cbe4635d18eb86543c40012ff0327e740f76de8441a136bd3d71cb7` |
| `out/sampler_ks.txt` | `82b748a6f3b55d85354910f82a274e0742faf71815570773415a1a85f7b75d04` |
| `out/state.json` | `36a7b85f0ac4adcd7ee04e69571c203df931566422e00327df7343ad0051ce3c` |
| `out/unit_tests.txt` | `16ed5f87ee611313dcecdf1ea68fad519051843c9df612f98691d87268d68e2b` |
