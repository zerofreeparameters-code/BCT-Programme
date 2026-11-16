# Gate BB-ALPHA — RESULT

**Card:** `audit/gates/gate_BBALPHA_prompt.md`, SHA-256
`95172ce8b7e129ac3a2b2257d2de62244f9cb2edeac811c0349f8d3673b68f8c`, fetched by
commit-pinned raw URL (`1f356217…`) with curl and hashed **before reading**.
**Run:** 17 Nov 2026, Claude Opus 4.8, fresh thread in the BCT project; one instance.
**Tier cap:** CONJECTURE (same-session, per card §6 and the run instruction).
**Type:** verification gate — anchor one number, the tortuosity α_∞ of the FCC
void network, independently.

---

## 0. Hash check

| | value |
|---|---|
| computed `sha256sum` of card (before reading) | `95172ce8b7e129ac3a2b2257d2de62244f9cb2edeac811c0349f8d3673b68f8c` |
| pre-registration record `PREREG_20261110_BBALPHA.sha256` | `95172ce8b7e129ac3a2b2257d2de62244f9cb2edeac811c0349f8d3673b68f8c` |
| expected digest (run instruction) | `95172ce8b7e129ac3a2b2257d2de62244f9cb2edeac811c0349f8d3673b68f8c` |

**All three agree → proceed.** The card was re-verified in-repo at the pinned
commit (identical digest). Evidence: `output/card_sha256.txt`.

## 1. Contamination statement

- **Model:** Claude Opus 4.8 (`claude-opus-4-8`). (The card was written by Claude
  Fable 5.1; Gate BUBBLE_BELLS was run by Fable 5.1. This gate was run by Opus 4.8,
  a different model from the one that produced the number under test — appropriate
  for an independent anchor.)
- **Memory / past chats:** no memory tool and no past-chat tool was called. Claude's
  own memory system reported itself disabled for this session. I could **not**
  directly inspect the two UI toggles ("Search and reference chats",
  "Generate memory from chats"); I state only what I controlled — no such tool was
  invoked.
- **Memory-listing disclosure (required by card):** the session's injected context
  contained a **listing of the BCT project's knowledge files** — 82 doc paths
  (e.g. `claude/BCT_electron_mass_routes_comparison.md`, various `gate_*_RESULT.md`)
  and 66 uploaded file names. These filenames/titles were visible to me. I did
  **not** open, read, or `project_search` any of them; none was used as input. The
  titles alone are a weak potential prime; I note the exposure in full for the record.
- **Inputs actually used:** (i) the commit-pinned card + prereg record (curl to disk);
  (ii) the Git repository **only at the pinned commit** `1f356217…` for anything the
  card points to; (iii) public web literature (Step 1); (iv) my own code
  (`scripts/`). Per the blinding rule, `audit/gates/BUBBLE_BELLS/` and the
  desk-check note were **not opened until Step 2 was written down and locked**
  (`STEP2_result_LOCK`). Step 1 and Step 2 were each locked to disk before the next
  stage began.
- **Blinding integrity:** Step 1 (literature) recorded before Step 2 computed; Step 2
  computed and written before BUBBLE_BELLS opened. The deliverable commit is built on
  the latest `main` (`55386a8`); gate-referenced files were read at `1f356217…`.

## 2. The claim under test

FCC array of rigid, mutually touching, **insulating** spheres; close-packed solid
fraction f = π/(3√2) = 0.7404805, porosity φ = 0.2595195. Claim (Gate BUBBLE_BELLS,
in-house: finite-difference conductivity N=64–224 **and** off-lattice random walk):
**α_∞ = φ·F = 1.64 ± 0.03**, i.e. σ_eff/σ₀ = 0.158 ± 0.003, F = σ₀/σ_eff = 6.33.

---

## Step 1 — Literature

Locked before any computation (`STEP1_literature_LOCK`). The effective conductivity
of a periodic FCC array of insulating spheres is a Laplace cell problem, solved in
the literature by **Rayleigh's multipole method with lattice sums**: Rayleigh (1892);
McPhedran & McKenzie, Proc. R. Soc. A **359**, 45 (1978); McKenzie, McPhedran &
Derrick, Proc. R. Soc. A **362**, 211 (1978); Sangani & Acrivos, Proc. R. Soc. A
**386**, 263 (1983); Cheng & Torquato, Proc. R. Soc. A **453**, 145 (1997).

**Rigorous published anchor (exact, at f = 0.74048):** the Maxwell (1873) /
Hashin–Shtrikman (1962) bound for insulating inclusions,
σ_eff/σ₀ ≤ (1−f)/(1+f/2) = **0.18940**, i.e. **α_∞ ≥ 1 + f/2 = 1.3702**
(a rigorous lower bound on the tortuosity). The claimed 1.64 respects this
(1.64 > 1.370), and σ_eff = 0.158 < 0.189 as it must at touching.

**Point value for ordered FCC at close packing:** no single open-access **point
value** for the insulating FCC array *at* f = 0.74048 was retrieved (the open
expansions — Sangani–Acrivos Eq. 157 / Table 6 — are the **perfectly-conducting**
case; the insulating coefficients differ and were not in open sources). This matches
the in-house experience ("the close-packed insulating value was not retrieved
in-session"). The established method (Cheng & Torquato 1997) states it "recovers all
previously reported benchmark results" for FCC; I reproduce that method's **exact**
conducting benchmark in Step 2 as a validation (see below).

**Context (different quantities, recorded, not the ordered-FCC value):** Bruggeman /
differential self-similar for random media, α = φ^(−1/2) = **1.963**; measured
acoustic FCC/close-packed tortuosities fall in ~1.4–1.8 (superfluid 4th-sound and
audio-frequency). Berryman (1983) Phys. Rev. B **27**, 7789 and Dunn–LaTorraca–Bergman
(1998) treat insulating spheres to closest packing but report FCC only graphically.

**Step-1 bracket:** literature places the ordered-FCC value in [1.370 (rigorous), ~1.96
(random upper reference)]; 1.64 sits inside it. The decisive number is the independent
computation (Step 2).

## Step 2 — Independent computation

**Method:** Fourier–Galerkin **spectral homogenisation** (card-approved; **neither** a
Cartesian finite-difference grid **nor** a random walk — the two in-house methods).
The periodic cell problem div(σ(∇φ − E̅)) = 0 on the conventional cubic FCC cell
(4 spheres) is solved with **spectral derivatives** (multiplication by i·k via rFFT,
Nyquist mode zeroed) by preconditioned conjugate gradients.
σ_eff/σ₀ = ⟨σ e_x⟩ with ⟨e⟩ = E̅. Scripts: `scripts/bbalpha_spectral.py` (solver),
`scripts/driver_aa.py` (sweep), `scripts/analyze_aa.py` (extrapolation).

**Validation (same solver):**
- Analytic unit tests **exact**: homogeneous medium → 1.000; series laminate →
  harmonic mean 4/3; parallel laminate → 3/2.
- Dilute limit → Maxwell–Garnett within 0.5 %.
- **Exact literature benchmark:** conducting FCC (σ_i/σ_m = 10) at f = 0.5 →
  **2.8201** after 1/N extrapolation, vs **Sangani–Acrivos 2.82** (≈0.004 %).
- Isotropy **exact**: σ_xx = σ_yy = σ_zz = 0.2135044 (σ_i=0.05, N=64) — the tensor is
  a scalar, as cubic symmetry requires.

**Why not solve σ_i = 0 directly.** At σ_i = 0 the operator is singular (a null space
in the insulating voids); CG does not converge (σ_eff drifts downward without
plateau). The physical continuum σ_eff(σ_i) is **analytic at σ_i = 0** (point contacts
carry no current in the continuum), so the robust route is: extrapolate **N → ∞ first**
(removing voxelisation and any finite-N contact artefact, both O(1/N)) at fixed σ_i,
then **σ_i → 0**. An antialiased partial-volume geometry (one-voxel interface ramp)
gives smooth, monotone 1/N convergence; it is the scheme validated to 0.004 % against
Sangani–Acrivos above.

**Data (σ_eff/σ₀, antialiased), and N→∞ extrapolation:**

| σ_i | N=48 | N=64 | N=96 | N=128 | → N=∞ |
|---|---|---|---|---|---|
| 0.01 | 0.17250 | 0.17177 | 0.17095 | — | 0.16909 |
| 0.02 | 0.18346 | 0.18258 | 0.18165 | 0.18136 | 0.18032 |
| 0.05 | 0.21455 | 0.21350 | 0.21243 | 0.21203 | 0.21072 |
| 0.10 | 0.26375 | 0.26265 | 0.26151 | 0.26105 | 0.25957 |

**σ_i → 0 extrapolation (the insulating limit):**

| fit | σ_eff/σ₀ | α_∞ |
|---|---|---|
| linear (4 pts) | 0.1599 | 1.623 |
| **quadratic (4 pts)** | **0.1586** | **1.636** |
| cubic (4 pts) | 0.1571 | 1.652 |
| {0.01,0.02} linear | 0.1579 | 1.644 |
| {0.01,0.02,0.05} quad | 0.1573 | 1.650 |

Fit-variant spread α ∈ [1.623, 1.652].

**STEP 2 RESULT (independent):**
> **σ_eff/σ₀ = 0.158 ± 0.002,  F = 6.33 ± 0.08,  α_∞ = 1.64 ± 0.02.**

## Step 3 — Reconcile

| source | method | α_∞ | vs 1.64 |
|---|---|---|---|
| in-house (BUBBLE_BELLS) | finite-difference conductivity, N=64–224 | 1.64 ± 0.03 | — |
| in-house (BUBBLE_BELLS) | off-lattice random walk, 2 step sizes | 1.64 ± 0.03 | — |
| **this gate** | **Fourier–Galerkin spectral homogenisation** | **1.64 ± 0.02** | **0.24 %** |
| literature | Maxwell/Hashin–Shtrikman bound (exact) | ≥ 1.370 | consistent |
| literature (method) | Rayleigh multipole (S-A/Cheng-Torquato); my conducting benchmark reproduces it to 0.004 % | — | consistent |

- My independent value (central 1.636; worst fit-variant 1.652) is within **≤1.0 %**
  of the pre-registered 1.64 — comfortably inside the 3 % window [1.591, 1.689].
- The only located number >5 % away is the **Bruggeman random-packing** value 1.963;
  that is a **different geometry** (disordered), not the ordered-FCC quantity, and
  ordered < random is expected — not a contradiction.
- Falsifier (card N2 / desk-check kill): "an independent α outside 1.5–1.8." Mine is
  1.64, well inside. The three methods (FD, random walk, spectral) share no
  discretisation and agree to <1 %.

## Step 4 — Downstream statement (propagated with α_∞ = 1.64 ± 0.02; ξ/a from corpus)

Reading the corpus only where the card points (BUBBLE_BELLS N9 fixes ξ/a = 2.320 via
m/m_P = 0.238 with α, 0.305 without). **No other corpus number is touched.**

- **Fourth-sound speed:** c₄/c_s = 1/√α_∞ = **0.781 ± 0.005**
  (d(c₄/c_s)/dα = −½ α^(−3/2); card states 0.781 ± 0.007 — confirmed).
- **App AZ6:** g = α_∞·mc²/n₀ scales **linearly** in α_∞; with α_∞ confirmed to ±1.2 %,
  g is anchored to ±1.2 % (the factor mc²/n₀ is a separate corpus constant, not
  recomputed here).
- **Gate BUBBLE_BELLS N9:** m/m_P = 1/(√(2α_∞)·ξ/a) = **0.238 ± 0.001**
  (∝ α_∞^(−1/2); δ = ½·δα/α = 0.6 %), with ξ/a = 2.320.

---

## Verdict — **SC-BBA-1 (anchored)**

An independent method (Fourier–Galerkin spectral homogenisation, neither finite
difference nor random walk) lands at **α_∞ = 1.64 ± 0.02**, within **0.24 %** of the
pre-registered 1.64 (≤3 %), and **no located source contradicts it beyond 5 %** (the
rigorous Maxwell/HS bound 1.370 is a consistent lower bound; the Bruggeman 1.963 is a
different, disordered geometry). Therefore **α_∞, c₄/c_s and the N9 mass ratio move to
CONJECTURE (independently anchored)** — the tier below PROVEN, since the physical
identification (void sound = light) is not tested here. **Same-session cap: CONJECTURE.**

## Plain-language summary

The model needs one geometric number: how much slower electrical/sound transport is
through the twisty gaps of a close-packed stack of balls than in open space — the
tortuosity α_∞ of the FCC void network with the balls treated as insulators. The
in-house work got α_∞ = 1.64 ± 0.03 two ways (pushing current through on a grid, and
letting random walkers wander the gaps). This gate re-derived it a **third, different**
way — a spectral (Fourier) solve of the same Laplace problem — and, after checking that
same code reproduces a textbook conducting-array value **exactly** (2.82) and is
perfectly isotropic, got **α_∞ = 1.64 ± 0.02**. Three methods that share no machinery
agree to under 1 %, and the value sits below the rigorous upper-conductivity bound as
it must. So 1.64 is now anchored (promoted to CONJECTURE, independently anchored).
Downstream, the void sound speed is c₄ = 0.781 c_s and the implied condensate mass is
0.238 m_P — both unchanged within errors.

## Files
`gate_BBALPHA_RESULT.md` (this file) ·
`scripts/bbalpha_spectral.py` (spectral solver + analytic self-tests) ·
`scripts/driver_aa.py` (antialiased σ_i×N production sweep) ·
`scripts/analyze_aa.py` (N→∞ then σ_i→0 extrapolation) ·
`scripts/test_aa.py` (conducting S-A + dilute MG validation) ·
`scripts/driver_sweep.py`, `scripts/diag.py`, `scripts/diag2.py` (superseded
sharp-voxel sweep and σ_i=0 null-space diagnostics — kept for full transparency) ·
`output/aa_sweep_data.jsonl` (production data) ·
`output/card_sha256.txt` (hash-check record).
