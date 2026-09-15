# Scoping note — App K §K.7 electron-mass candidates (retirement by parametrics)

**Status:** NON-GATE scoping note. Not a Cold Ledger gate; no pre-registered digest, no
stop conditions. Purpose: decide whether App K's three §K.7 mass candidates each warrant a
full gate, or can be retired on parametric grounds first.
**Executing model:** Claude Opus 4.8 (Anthropic).
**Date:** 15 September 2026.
**Rests on:** Gate KAUDIT (RUN AND CLOSED 15 Sep 2026, verdict SC-KAUD-1) and a cold
in-session recomputation of the FCC local Green's function (below). App K text read from
`tex/BCT_Appendix_K_GreenFunction.tex` at commit `2b6e3d9` (recovered draft; carries an
audit banner — see Contamination).

---

## 0. One-line verdict

All three candidates as written (quark–lepton asymmetry, Chern–Simons, Wilson/temporal)
**cannot reach m_e**. Each produces a fermion mass at *leading* order in α₀ — an O(α₀) mass,
~10²⁰ too large — and none has the half-integer / 21st-order / instanton structure the
corpus's own target m_e ~ α₀^{21/2} demands. They break a particle–hole symmetry that Gate
KAUDIT already showed the lattice breaks by itself, so their stated purpose is moot and their
magnitude is unsuppressed. **Recommendation: retire C1–C3; do not open three gates.**

---

## 1. Inputs (geometry only; no inheritance beyond the stated constants)

- r_oct = (√2−1)/2 = 0.207106781187
- r_tet = (√6−2)/4 = 0.112372435696
- α₀ = r_oct·r_tet/π = 0.00740805572755   (App K hopping t = α₀)
- m_e/m_P = 4.185×10⁻²³   (target)
- Cold this session (two methods, `selfenergy_vertex2.py`): on the FCC 12-NN band
  E(k) = −t·Γ(k) ∈ [−12t,+4t], PH-asymmetric, ρ(0) ≈ 0.11/t finite,
  **Re G_loc(0) = −0.20/t** (local-subtraction principal value; DOS η-check consistent;
  matches KAUDIT). Denote c₀ ≡ |Re G_loc(0)|·t = 0.20.

## 2. App K §K.7, as written

1. **Quark–lepton asymmetry** ("most promising"): unit cell holds one lepton (oct void) and
   two quarks (tet voids) at different energies because r_tet ≠ r_oct; the coupled gap
   equation Σ_e = t²[G_e + G_u + G_d] breaks PH via the geometric asymmetry.
2. **Chern–Simons:** the k=1 CS level (App G) is PH-odd; induced mass ~ α₀ × (flux through
   the oct void), unevaluated.
3. **Wilson/temporal mass:** the 3+1D Dirac operator (App E.2) carries a Wilson mass
   m_W ≈ r_W/a_t²; temporal structure and r_W unspecified.

## 3. The target's parametric structure (using the corpus's own claim)

m_e/m_P = α₀^{10.5048}; App K claims m_e ~ α₀^{21/2} (§5.3, self-declared UNPROVEN).
α₀^{21/2} = 4.284×10⁻²³ (2.4% high). **The half-integer power is the whole story.** Writing
the amplitude-level coupling as g with α₀ = g² (fine-structure convention), g = √α₀ = 0.0861:

  m_e ~ α₀^{21/2} = g²¹   — a **21st-order** amplitude (g²¹ = 4.284×10⁻²³, verified).

Reaching order 21 perturbatively requires orders 1–20 to **vanish by a symmetry** — the exact
protection KAUDIT showed the non-bipartite FCC lattice does NOT provide. The nonperturbative
alternative is e^{−S} with **S = −ln(m_e/m_P) = 51.53**, an instanton whose action geometry
would have to supply. Either route is a high-order-protected or nonperturbative object.

## 4. Candidate-by-candidate retirement (order-of-magnitude, on App K's own formulas)

| candidate | natural scale | \|m\|/m_P | overshoot |
|---|---|---|---|
| 1 quark–lepton asymmetry | t²·3·\|G\| ~ 3c₀α₀ | 4.4×10⁻³ | ~1×10²⁰ |
| 1 steelman (near-cancellation) | α₀c₀·(Δr/r) | 4.4×10⁻⁴ | ~1×10¹⁹ |
| 2 Chern–Simons | α₀·flux, flux~O(1) | 7.4×10⁻³ | ~2×10²⁰ |
| 2 flux ~ oct area | α₀·r_oct² | 3.2×10⁻⁴ | ~8×10¹⁸ |
| 3 Wilson/temporal | r_W/a_t² ~ cutoff | ~1 (m_P) | ~10²³ (or tune r_W~10⁻²³) |

Asymmetry factors are O(1), not small: (r_oct−r_tet)/(r_oct+r_tet) = 0.30, r_tet/r_oct = 0.54.
So even a mass proportional to the asymmetry lands at ~α₀, not below it.

**C1.** Σ_e = t²[G_e+G_u+G_d] with t = α₀ and G ~ c₀/t gives Σ_e ~ 3c₀α₀ ~ 4×10⁻³ m_P.
The geometric asymmetry makes the sum PH-asymmetric — redundantly, since the lattice already
is — but does not touch the magnitude, which is fixed by t²·G ~ α₀, first order.

**C2.** α₀ × flux. A quantised/topological flux is O(1) → α₀ ~ 10⁻³ m_P; an area-scaled flux
r_oct² = 0.043 → 3×10⁻⁴ m_P. One power of α₀ times an O(1)–O(0.01) geometric factor. (Also:
CS masses live naturally in 2+1D; the 3+1D "flux through the oct void" is undefined here.)

**C3.** A Wilson term is a doubler-removal device — cutoff-scale by construction (the WRONG
sign of mechanism: it makes modes heavy, to decouple them). Reaching 10⁻²³ requires tuning
r_W ≈ 10⁻²³ by hand, with no principle. Worst of the three.

## 5. Steelman of C1 (the "most promising" one)

Could Σ_e = t²[G_e+G_u+G_d] be small by cancellation among the three voids? It is a dilemma
with no middle:
- **Generic cancellation** — O(1) parts cancel, the asymmetry residual survives at
  ~α₀·(Δr/r) ~ 10⁻³ m_P (10¹⁹ too big).
- **Symmetry-enforced cancellation** — exact → m = 0, App K's original over-protection.

There is no natural landing at α₀^{10.5} between "generic → α₀" and "symmetric → 0"; hitting
it needs a ~20-digit tuning nothing supplies. The steelman fails.

## 6. Inherited dependency (applies to all three)

Every candidate presupposes a fermion field: C1 needs leptons/quarks occupying voids; C3
invokes "the 3+1D Dirac operator (App E.2)." **Gate F** closed the fermion sector — the actual
field content (M = S¹) carries no fermionic content (π₂(S¹) = π₃(S¹) = 0, Derrick). So even
setting the scale problem aside, all three inherit the unresolved step-1 question: *what
fermion?* This must be settled before any mass mechanism has an object to act on.

## 7. Findings (tiered)

- **SK7-01 [PROVEN, arithmetic].** m_e/m_P = α₀^{10.5048}; α₀^{21/2} = 4.284×10⁻²³ (2.4% high);
  g²¹ = α₀^{21/2} with g = √α₀. The target is a half-integer power = 21st order in g.
- **SK7-02 [PROVEN, computation].** Re G_loc(0) = −0.20/t on the FCC 12-NN band (this session,
  two methods; matches KAUDIT). ρ(0) ≠ 0, PH-asymmetric — no protection.
- **SK7-03 [ESTIMATE, dimensional].** Each of C1–C3 yields an O(α₀) (or cutoff-scale) mass →
  ~10²⁰ too heavy. Order-of-magnitude on App K's own formulas; O(1) coefficients and
  non-fine-tuned cancellations do not close a 20-order gap.
- **SK7-04 [ANALYSIS].** All three are leading-order, integer-power (C1, C2) or cutoff-scale
  (C3) mechanisms; none produces a half-integer power, a 21st-order effect, or an e^{−S}
  suppression. They are structurally disjoint from the target power, before any coefficient.
- **SK7-05 [ANALYSIS].** The candidates' stated function (break PH to permit a nonzero mass)
  is moot post-KAUDIT: the lattice already breaks PH and already generates a (too-large) mass.
- **SK7-06 [DEPENDENCY].** All three presuppose a Dirac/lattice fermion absent from the M = S¹
  field content (Gate F). Step 1 (fermion existence) gates all mass work regardless.

## 8. Gateable propositions (the redirect — what WOULD have the right structure)

If m_e is to come from BCT at all, the parametric target (g²¹ or e^{−51.53}) points away from
§K.7 entirely, toward:
- **P1.** A mode whose mass is protected to vanish through order 20 in g and first appears at
  order 21 — requires identifying the symmetry doing the protecting on the FCC lattice (KAUDIT
  showed the obvious sublattice/chiral candidate is absent). Gate only if such a symmetry can
  be named.
- **P2.** A geometric instanton/tunnelling configuration with action S ≈ 51.53 derivable from
  the void geometry (the half-integer power is consistent with a one-instanton fluctuation
  determinant, ∝ det^{−1/2}). Gate: does any BCT saddle have S ≈ 51.5 with no free input?
- **P0 (precedes both).** Settle fermion existence (SK7-06 / Gate F). Without it, P1 and P2
  have no object.

## 9. What this note did NOT establish

- It did not *compute* any candidate's mass — §4 is order-of-magnitude on App K's own
  formulas. A candidate could in principle carry an unnoticed suppression; but closing a
  20-order gap by an O(1) coefficient is not available, and the power-mismatch (SK7-04) is
  coefficient-independent.
- It did not evaluate the CS flux (App G) or the Wilson temporal structure (App E.2) at
  source; both are declared "unspecified/unevaluated" in App K, which is itself the point.
- It does not touch the geometry (α₀, void radii) — untouched, as in KAUDIT.
- α₀^{21/2} is the corpus's claim, not derived here; SK7 uses it as the target to test the
  candidates against, and the candidates fail even granting it.

## 10. Contamination

App K's `.tex` is a recovered draft carrying an audit banner that pre-states KAUDIT's
conclusions (PH-asymmetric band, Γ_loc(0) ≠ 0, "headline survives for the opposite reason").
Re G_loc(0) was recomputed cold this session and matches; the candidate scale estimates use
only App K's §K.7 formulas and the canonical constants. The Cold Ledger auto-loads, so prior
gate verdicts (KAUDIT, KND, F) were in view — used only as named dependencies, not re-derived.

## 11. Reproduction

`selfenergy_vertex2.py` (FCC band, DOS, Re G_loc(0), self-energy) and the scale-table
one-liner in this note's §4 are deterministic. Constants as in §1.
