# Gate FORK — pre-registration

**Working backwards through the forks of the BCT derivation, with a scored null model.**

Drafted 11 Oct 2026 for M. R. Cabrié. Status: PRE-REGISTERED, UNRUN. To be committed to `audit/gates/gate_FORK_prompt.md`, digest recorded in `audit/gates/PREREG_20261011.sha256`, and run in a fresh thread with "Search and reference past chats" and "Generate memory from chats" switched off for the run. One gate per thread. Same-session results capped at CONJECTURE.

---

## 0. The question

BCT was reached by a sequence of choices. At each one, a branch was taken and the others were not. This gate stands at every fork, enumerates the branches that were not taken, computes what each branch produces, and scores every branch, taken and untaken, against the same fixed target list by the same rule.

Two things come out:

1. **The map.** Every fork, every branch, what each branch produces. No verdicts attached to the map itself.
2. **The score.** For each branch: how many of the fixed targets does its geometric alphabet reach within 1% (and 0.1%)? The taken path is then one row in a table of rows. Its rank in that table is the finding.

This gate cannot turn a "match" into a "derivation". It can only say whether the taken path's matches are rarer than the matches an untaken path would have produced. That is the base-rate question Gate PRED raised (113 expressions near 137.036; random expression hits some target about half the time at 1%) and did not settle, because PRED varied the expression and held the geometry fixed. FORK varies the geometry.

Anything found down an untaken branch is a **candidate** for its own gate, nothing more. It is logged, not promoted.

## 1. What is fixed before any branch is evaluated

Everything in sections 2 to 5. The digest of this file is the record. No fork, branch, target, tolerance, scoring rule or threshold is added, removed or re-weighted after the digest is taken. Any such change requires a new file, a new digest and a new run.

## 2. The forks

A fork is a point in the forward derivation where the corpus made a choice that it does not derive. The list is seeded from choices the ledger has already identified as selected rather than forced (WHY√2, R8, U″, PRED, Chain-of-Necessity audit) plus the remaining undischarged choices in the α₀ layer. Branch sets are enumerated by a stated rule so that they are not hand-picked.

Each fork has a **taken branch** (marked ★) and an **enumeration rule** that generates the rest.

### F1 — Lattice / packing
Taken ★: FCC-equivalent close packing, written as BCT at c/a = √2.
Rule: every 3-dimensional lattice or periodic packing in which the interstitial voids are standard and their inscribed radii are closed-form in the sphere radius R. Branch set:
- SC (simple cubic): one cubic void
- BCC (BCT at c/a = 1): distorted octahedral and tetrahedral voids
- FCC = BCT at √2 ★
- HCP: same oct/tet radii as FCC (stacking-blind; included to record that fact in the map, expected to duplicate ★'s numbers)
- Diamond cubic: one large void
- Random close packing: oct/tet radii as FCC (stacking-blind), noted, not scored separately
- D4 (4-dimensional) with its two hole types, scored in its own dimension

### F2 — Axial ratio c/a of the BCT family
Taken ★: √2.
Rule: the values of c/a at which some coordination shell of the BCT lattice becomes degenerate with another (the cubic points and the shell-crossing points), plus the continuum between 1 and 2 sampled at 0.01 so the scored quantities can be plotted as functions of c/a. Named points: 1 (BCC), √2 (FCC) ★, √(2/3), √3, 2, and any shell-crossing found by the enumeration script. Void radii for general c/a are computed numerically from the Voronoi/Delaunay geometry, not assumed.

### F3 — Length unit
Taken ★: u = D = 2R (nearest-neighbour distance; equals a_BCT at √2).
Rule: every length that the lattice defines without a free parameter. Branch set: R (sphere radius), D = 2R ★, a_cubic (conventional cubic cell edge of FCC = √2·D), c (BCT axial length), the octahedral void diameter, the tetrahedral void diameter, the Wigner–Seitz radius.

### F4 — Void radius definition
Taken ★: inscribed-sphere radius of the interstitial site minus R, i.e. ρ = circumradius − R.
Rule: the standard alternative radii of the interstitial polyhedron. Branch set: inscribed (★), circumradius of the hole polyhedron itself, in-radius to the nearest face, mean of in- and circumradius.

### F5 — Which voids enter
Taken ★: the octahedral and the tetrahedral void, both.
Rule: every subset of the lattice's void types of size 1 or 2 (FCC has two types; SC and diamond have one; BCC has two distorted types; D4 has two hole types). For one-void branches the coupling form is applied with the single radius squared where a product is required.

### F6 — Coupling form
Taken ★: α₀ = r_oct · r_tet / π.
Rule: every expression of the form `g(r_a, r_b) / k` with g ∈ {product, ratio (both orders), sum, difference (abs), geometric mean, r_a², r_b²} and k ∈ {1, 2, π, 2π, 4π, π², e, √2, √3}. That is 9 × 9 = 81 forms per void pair; the taken form is one of them.

### F7 — Correction form
Taken ★: α = α₀(1 − 2α₀).
Rule: `α₀ · (1 + N α₀)^s` with N from the corpus's own printed menu {±3/8, ±3/4, ±1, ±3/2, ±2, ±9/4, ±3, ±4, ±5, ±6, ±8, ±9} and s ∈ {+1, −1}, plus no correction. 49 forms.

### F8 — Dimension
Taken ★: 3.
Branch set: 2 (hexagonal close packing in the plane, one void type), 3 ★, 4 (D4, from F1).

### F9 — Energy anchor (dimensionful)
Taken ★: Λ_QCD = 220 MeV.
Rule: the anchors the corpus itself names anywhere: 220 MeV ★, m_π0, m_ρ, m_p, v = 246.22 GeV. Enters only the hadron-ratio targets (as in PRED J4), where the target is re-expressed as a ratio to the branch's anchor.

### F10 — Target manifold of the field (non-numeric fork, mapped not scored)
Taken ★: S¹ (one compact scalar; RANK, PT, JHF). Branches: S², S³, SO(3), ℂ² with constraint. These produce no numbers at the α₀ layer; the map records for each what it would and would not permit (π₂, π₃, number of polarisations) and cites the gate that already ruled on it. No score.

### Design of the branch space
The full Cartesian product of F1–F9 is of order 10⁵ geometric alphabets and would itself become a look-elsewhere machine. The scored set is therefore:

- **One-step neighbours**: every branch of every single fork with all other forks held at ★. (F1: 7, F2: 5 named + continuum, F3: 7, F4: 4, F5: ≤4, F6: 81, F7: 49, F8: 3, F9: 5.)
- **The coupled pair F1 × F3**: lattice and unit together, because R8 showed the unit choice is what makes a given lattice's rationals appear. All lattice × unit combinations (7 × 7).
- **The coupled pair F6 × F7**: coupling form and correction form together, because this is the pair that produces 1/α. All 81 × 49 = 3,969 combinations, scored on the single target 1/α only, as a separate look-elsewhere count for the headline result.

Total scored alphabets: about 200 for the general score, plus 3,969 single-target evaluations. Each alphabet is scored with the same enumeration as PRED (≤3 atoms, ≤2 binary ops, unary menu as in `pred_step2_nullmodel.py` J1–J3), with the branch's own r_a, r_b, α₀ replacing the ★ values in the atom list and everything else in the atom list unchanged.

## 3. Targets

The PRED J4 list, unchanged, 47 dimensionless targets (1/α, sin²θ_W, PMNS angles, n_s, α_s, Ω_Λ, Y_p, lepton and quark mass ratios, Koide, hadron ratios to m_π0 and to the anchor, m_H/v, m_t/v, m_W/m_Z, g_A, μ_p, V_us, V_cb, V_ub, Planck logs, σ₈, H₀/100, Ω_m). Values as in that script, copied verbatim into the FORK script before the digest. Hadron-anchor targets are recomputed per F9 branch.

Tolerances: 1% and 0.1%, both reported.

## 4. Scoring

For each scored alphabet b:

- **P_hit(b)**: fraction of distinct expression values in the enumeration that fall within tolerance of *some* target (PRED's statistic, interval-union, so a value near two targets counts once).
- **C(b)**: number of targets covered by at least one expression.
- **C₀.₁(b)**: same at 0.1%.
- **H_α(b)**: for the F6 × F7 sweep only, |1/α_b − 137.035999| / 137.035999.

Then:

- **Rank of ★**: the percentile of the taken path's C and C₀.₁ among the one-step-neighbour set and, separately, among the F1 × F3 set.
- **Per-target look-elsewhere count, L(t)**: for each target t, the number of scored alphabets that reach it within 0.1%. A target reached by most branches is reachable by the alphabet's richness, not by the geometry.
- **Headline count, L_α**: the number of the 3,969 F6 × F7 forms that land within 0.013% of 1/α (the taken path's own error), and within 0.1%, and within 1%.
- **Exclusive hits of ★**: targets that ★ reaches at 0.1% and fewer than 5% of scored alphabets reach.
- **Exclusive hits of untaken branches**: for each untaken branch, targets it reaches at 0.1% that ★ does not. These are the "clues". Each is logged with the branch, the expression and the error, and marked CANDIDATE.

## 5. Verdicts (fixed now)

- **SC-FORK-1 (selection informative).** ★ is at or above the 95th percentile on both C and C₀.₁ among one-step neighbours **and** has at least two exclusive hits at 0.1% **and** L_α at 0.013% ≤ 3. The geometry choice does better than the branches around it by a margin the null does not reproduce. Opens: a gate per exclusive hit.
- **SC-FORK-2 (selection is base rate).** ★ lies within the central 80% on C or C₀.₁, **or** L_α at 0.013% ≥ 10. The clean numbers of the forward chain are what any branch produces; the forks did not discriminate. Closes: the claim that the α₀ layer's agreement is evidence for the lattice/unit/form choices. Does not touch the void geometry as geometry (R8 scope note stands).
- **SC-FORK-3 (an untaken branch outranks ★).** At least one untaken one-step branch exceeds ★ on both C and C₀.₁ with at least two exclusive hits of its own at 0.1%. Logs those branches as CANDIDATE for separate gates. Does not promote them.
- **SC-FORK-0 (no verdict).** Sensitivity run (§6) moves ★'s percentile across the 80/95 boundaries, or the branch enumeration for F2/F4 fails to close in closed form or stable numerics.

Verdicts 1 and 3 can co-occur. Verdict 2 excludes 1.

## 6. Sensitivity (reported, cannot change the verdict rule)

Re-run the scoring with: (a) 2-atom instead of 3-atom bound; (b) the N-layer on and off; (c) targets restricted to the eleven the corpus calls headline (1/α, sin²θ₁₃, n_s, m_p/m_e, m_μ/m_e, Koide, m_H/v, V_us, Ω_Λ, H₀/100, ln(m_P/m_e)); (d) tolerance 0.5%. Report ★'s percentile under each. Verdict uses the primary rule only; if the primary verdict flips under any of (a)–(d), record SC-FORK-0 instead.

## 7. Verification

- All geometry in mpmath at 60 dps working, 40 reported; void radii for general c/a cross-checked against the closed forms at c/a = 1 and √2 (must reproduce (√2−1)/2 and (√6−2)/4 under u = D to 40 dps or the run halts).
- Enumeration deterministic; no sampling. Script saved with explicit sourcing. Target list and atom menu copied byte-for-byte from `pred_step2_nullmodel.py` at the commit named below.
- The run records the commit SHA-1 of the checkout and the SHA-256 of this prompt file inside it.
- Deliverable: `gate_FORK_RESULT.md`, `fork_map.md` (the map, all forks, all branches, what each produces), `fork_scores.csv` (one row per scored alphabet), `fork_alpha_sweep.csv` (3,969 rows), `gate_FORK_run.py`. Null result is a finding and is filed as one.

## 8. What this gate does not do

It does not evaluate the physics of any branch. It does not ask whether BCC or D4 is a better vacuum. It does not re-derive any prediction. It does not use any target the corpus has not already claimed. It asks one thing: standing at each fork, does the branch that was taken land on more of the world's numbers than the branches that were not, after the richness of the expression alphabet has been subtracted out?

## 9. Pre-registration record

- Prompt file: `audit/gates/gate_FORK_prompt.md`
- Source script to copy J1–J5 from: `pred_step2_nullmodel.py` (project copy dated 13 Sep 2026; repo copy at `audit/gates/PRED/`)
- Digest: see `PREREG_20261011.sha256` (computed on this file as committed)
- Run thread: fresh; memory and past-chat search off for the run; one gate per thread.

