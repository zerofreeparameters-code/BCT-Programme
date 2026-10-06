# Gate LOG — pre-registration card

**Programme:** "Nothing says why 1/137" (successor to the BCT Cold Ledger)
**Card written:** 7 October 2026, Claude, at Michel's request
**Status:** PRE-REGISTERED, NOT RUN. Nothing in this card has been computed to standard.
**Type:** baseline measurement, not a blind test (see section 8).

---

## 1. Question

If light is emergent ("induced") rather than fundamental, with its cutoff at the
Planck scale, and the only charged matter is the known Standard Model particles,
what low-energy value of 1/α does the standard one-loop formula give, with no
adjustments?

Secondary question: how far does 1/α drift between the Planck scale and zero
energy, and is a "bare" value of 1/α₀ = π/(r_oct·r_tet) at the Planck scale
compatible with that drift?

## 2. Why this gate exists

The Cold Ledger closed the claim that BCT derives α (Gates FWD, STAT, QED,
QED-DERIV). The surviving question is whether α could be an emergent quantity
of the form "particle count × logarithm of a scale ratio", as it is in real
emergent-photon systems (superfluid ³He-A; Zel'dovich's induced electrodynamics,
1967). This gate measures the size of the gap for that idea using known
particles only. It does not test BCT geometry.

## 3. Fixed rules

**3.1 Formula (one loop, step thresholds).**

    1/α(0) = 1/α(Λ) + (1/2π) · Σ_i b_i · ln(Λ / m_i)

with

- b_i = (4/3) · N_c · Q² for each charged Dirac fermion (N_c = 3 quarks, 1 leptons)
- b_W = −7 for the W± boson (transverse part −22/3, charged Goldstone +1/3)
- no other charged fields

Above the electroweak scale, 1/α is defined as 1/α₂ + 1/α_Y. At one loop this
combination runs with the same coefficients, so the formula applies unchanged.

**3.2 Induced condition.** 1/α(Λ) = 0.

**3.3 Inputs (fixed here; these are the values to use, whatever any later
table says).**

| Particle | Q | N_c | Mass (GeV) |
|---|---|---|---|
| e | −1 | 1 | 0.00051099895 |
| μ | −1 | 1 | 0.1056583755 |
| τ | −1 | 1 | 1.77686 |
| u | +2/3 | 3 | 0.00216 |
| d | −1/3 | 3 | 0.00470 |
| s | −1/3 | 3 | 0.0935 |
| c | +2/3 | 3 | 1.273 |
| b | −1/3 | 3 | 4.183 |
| t | +2/3 | 3 | 172.57 |
| W± | ±1 | n/a | 80.3692 |

- Planck mass: M_P = 1.220890 × 10¹⁹ GeV
- Reduced Planck mass: M_P / √(8π)
- Measured value for comparison: 1/α(0) = 137.035999
- r_oct = (√2 − 1)/2, r_tet = (√6 − 2)/4

**3.4 Variants. All four are run and all four are reported. None is "the"
answer; V1 is the headline.**

- **V1 (headline):** all ten particles, Λ = M_P.
- **V2:** fermions only (no W), Λ = M_P. This is the original 1960s form.
- **V3:** as V1, with Λ = reduced Planck mass.
- **V4:** as V1, with the light-quark thresholds replaced by constituent-style
  values (u = d = 0.3 GeV, s = 0.5 GeV), to show the sensitivity to
  low-energy quark physics, which one loop does not describe properly.

## 4. Outputs

- **O1.** 1/α(0) under the induced condition, for V1–V4.
- **O2.** The bare value 1/α(Λ) that would be needed to land on 137.035999,
  for V1, V3 and V4.
- **O3.** The total drift 1/α(0) − 1/α(Λ) for V1, compared with the drift the
  "bare 1/α₀ → 137" story needs, namely 137.035999 − π/(r_oct·r_tet).
- **O4.** The energy scale μ* at which the one-loop 1/α(μ*) equals
  π/(r_oct·r_tet), running down from the measured value, for V1 and V4.
- **O5 (diagnostic only, labelled as a fit).** The cutoff Λ that would give
  exactly 137.035999 under the induced condition in V1. One free parameter
  tuned to one number carries zero evidential weight and must be reported
  with that sentence attached.

## 5. Verdict codes

- **SC-LOG-1:** V1 gives 1/α(0) within 1% of 137.036. Flag for a follow-up
  gate. Not evidence on its own: threshold conventions (V3, V4) must agree.
- **SC-LOG-2:** V1 is the right order of magnitude (between 50 and 300) but
  not within 1%. Report the gap and what O2 says is missing.
- **SC-LOG-3:** V1 is outside 50–300. Known particles with a Planck cutoff do
  not reach the ballpark; the idea needs additional charged content or a
  different mechanism.

Independently of the code above, report plainly whether O3 supports or
contradicts the "bare 1/α₀ at the Planck scale" reading.

## 6. No-fit clause

- No variant, particle, mass or cutoff may be added, removed or changed after
  the run starts.
- No result may be described as "deriving" α.
- Whatever the outcome, it is not evidence for or against BCT void geometry,
  which enters only through the comparison number in O3 and O4.

## 7. Known limitations (stated in advance)

- One loop only. Two-loop terms and scheme dependence are ignored.
- Step-function thresholds. Real thresholds are smooth.
- Light-quark masses are not physical thresholds; the true low-energy
  hadronic contribution is measured, not computed. V4 brackets this crudely.
- No gravitational or beyond-Standard-Model contributions.
- The Planck scale as cutoff is an assumption, not an output.

## 8. Analyst's disclosure (why this is not a blind test)

The ingredients are textbook, and Claude made a rough mental estimate before
writing this card. Recorded here so it cannot be hidden later:

- V2 (fermions only) is expected near 75–80.
- V1 (with the W) is expected near 30–35.
- O2 is expected near 105.
- O3 is expected to show a drift of roughly 30, against the roughly 2 that
  the "bare 1/α₀ → 137" story needs.

On 7 October 2026, in chat, Claude told Michel this calculation "lands in the
right ballpark, around 100". That figure was loose: it fits the fermions-only
form at best, and the estimate above suggests the full answer is lower. The
run decides.

## 9. Run protocol

- Fresh thread, inside the BCT project. One gate per thread.
- Fetch this file from the repo by commit-pinned raw URL, hash it on disk
  (SHA-256) before reading, and record the digest and commit.
- Python with mpmath, 60 dps working, 40 dps reported. Script saved and
  delivered with the result.
- Deliverable: `gate_LOG_RESULT.md` with O1–O5, the verdict code, and a
  plain-language summary.
- Same-session results are capped at CONJECTURE.
