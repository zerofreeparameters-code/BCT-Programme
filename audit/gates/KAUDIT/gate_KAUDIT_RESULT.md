# GATE KAUDIT — RESULT

**Do App K's three theorems survive on the real c/a=√2 lattice?**

**Executing model:** Claude Opus 4.8 (Anthropic). Single gate, fresh thread, Cold Ledger.
**Date executed:** 15 September 2026.

---

## 0 — HANDOFF DIGEST

Gate prompt received as a file at a commit-pinned `raw.githubusercontent.com` URL
(`.../BCT-Programme/2b6e3d9/audit/gates/gate_KAUDIT_prompt.md`), `curl`ed to disk **before**
reading:

```
SHA-256  c6da27858da0d675cf525df68a882c45055234a3ce3d22dc1b76367176f0a0e1   gate.md
size     9678 bytes
```

Matches the pre-registration in the invocation exactly. Digest claimed.

---

## VERDICT — **SC-KAUD-1**

**T1 (Bipartite) and T2 (Non-Renormalization) both FAIL on the correct lattice; T3's "20× too
weak" conclusion also fails, and inverts.** Derived cold:

- The c/a=√2 lattice is **FCC, coordination 12** (not 8), **non-bipartite** (explicit triangle,
  **C_A(3)=48**), single Bravais lattice (A and B sites equivalent → **single band, not a bipartite
  2-band model**).
- The single FCC band is **E ∈ [−12t, +4t]** (width 16t), **PH-asymmetric** (half-filling
  E_F = +0.92 t ≠ 0; DOS asymmetric, metric 0.51). Hence **Re G_loc(0) ≈ −0.20/t ≠ 0**.
- **T1 false:** odd loops exist; the 21-vertex loop is still excluded, but by **low-order
  dominance** (shortest loop = triangle, L_min=3), not by parity.
- **T2 false:** no PH symmetry ⇒ G_loc(0)≠0 ⇒ the zero mode is **not protected**. A leading
  perturbative self-energy is generated at ~α₀^{3/2}…α₀ ≈ 10⁻⁶–10⁻³ (Planck), i.e. **≈15–20 orders
  of magnitude too LARGE**. The diagnosis **inverts**: not "too weak / protected to zero" but the
  ordinary hierarchy problem (why is m_e so tiny).
- **T3:** the "coupling ~20× too weak" rested on a linear (Dirac-like) DOS with a finite critical
  coupling. On the correct FCC band ρ(0)≠0 ⇒ **no critical coupling**; a mass is generated for any
  coupling. The "too weak" statement does not survive.
- **Photon/graviton corollary:** App K's claim that they are *exactly* massless *by PH protection*
  **loses its proof** (PH symmetry is absent). The one genuinely-massless mode is the U(1)
  **Goldstone phonon**, protected by Goldstone's theorem — a single scalar mode, neither a
  2-polarisation photon nor a spin-2 graviton.
- **n=16 accident:** App K's "numerical accident" verdict is **correct** (null model ≈1.3 bits at a
  factor-4 window). Bonus cold catch: App K's *printed* `a_16 = 1.0962×10⁻²⁶` is a **×1000
  transcription error**; the value its own formula gives is `1.096×10⁻²³`, and *that* is what sits a
  factor ≈3.8 from m_e/m_P — an accident all the same.

This is the legitimate, honest outcome flagged by SC-KAUD-1. **It does not refute the geometry**
(α₀, the void radii, the surviving LO layer are untouched); it means App K's proofs, and its
exactly-massless corollary, must be redone on the correct lattice — which is what App K's own
(audit-added) banner already anticipates. The headline "no *correct-magnitude* perturbative m_e"
survives, but for the **opposite reason** App K gave.

---

## 1 — SEARCH-SPACE COVERAGE (where App K actually lives)

- **App K under test:** `tex/BCT_Appendix_K_GreenFunction.tex` — a **recovered draft**
  ("Transcribed into LaTeX from the draft PDF … App K … had no `.tex`; recovered as a draft PDF 15
  Sep 2026"). It carries an **audit banner** (see §Contamination). 196 lines.
- **App J (parent):** `tex/BCT_Appendix_J_SphereAction.tex`, 421 lines. Confirms t = Josephson
  coupling g = α₀; states the 21 = 3+6+12 loop conjecture; and — importantly — its **own** text
  (lines 344–347) already invokes "FCC coordination 12" and a "minimum closed loop of 3 (triangle
  of three mutually touching spheres)". App K's later 8-coordination/bipartite premise is thus
  inconsistent with its own parent appendix.
- **App E (fermion/Dirac):** **not located** as a single-letter appendix under `tex/`. Only
  `tex/BCT_Appendix_J_*` and `tex/BCT_Appendix_K_*` exist among low-letter appendices; higher
  `K*`/`L*` files are ARS-leptogenesis, unrelated. The fermion tight-binding content needed for the
  recomputation is fully contained in App K itself, so App E's absence is not blocking (no
  SC-KAUD-4 halt).
- **`audit/MINIMAL_BCT.md`:** read for canonical constants and field content.

Canonical inputs used (from `audit/MINIMAL_BCT.md` §1.3 and App K/J):

```
r_oct = (√2−1)/2      = 0.207106781187
r_tet = (√6−2)/4      = 0.112372435696
α₀    = r_oct·r_tet/π = 0.00740805572755      (hopping t = g = α₀)
m_e/m_P               = 4.185×10⁻²³
```

---

## 2 — STEP 0: THE LATTICE, COUNTED COLD  (`kaudit_1_lattice.py`)

Built the point set from its definition — A (corners) at (n₁,n₂,n₃√2), B (body centres) at
(n₁+½,n₂+½,(n₃+½)√2), a=1, c=√2 — and enumerated the neighbour shells of a corner site by brute
force:

| distance | multiplicity | composition |
|---|---|---|
| **1.000000** | **12** | 8 × B `(±½,±½,±√2/2)` + 4 × A `(±1,0,0),(0,±1,0)` |
| 1.414214 | 6 | A: `(0,0,±√2),(±1,±1,0)` |
| 1.732051 | 24 | mixed |

- **Coordination = 12.** App K's "8 NN, δ=(±½,±½,±√2/2)" captures only the 8 body-centre bonds; the
  **four in-plane corner–corner bonds (±1,0,0),(0,±1,0) sit at the *same* distance 1** and are
  omitted. Explicitly verified: |(1,0,0)| = |(½,½,√2/2)| = 1.000000.
- **Bipartite? NO.** O=(0,0,0), P=(1,0,0), Q=(½,½,√2/2) are pairwise at distance 1 — a **length-3
  triangle**. `|O−P|=|O−Q|=|P−Q|=1.000000`.
- **C_A(3) = (A³)_ii = 48** (24 triangles per site), computed from a finite-cluster adjacency
  matrix, identical for an A site and a B site.
- **A and B sites have identical 12-NN environments** ⇒ they are equivalent points of **one FCC
  Bravais lattice**. The correct tight-binding model is therefore **single-band**; App K's
  two-sublattice (A/B, chiral σ_±) construction is reducible and, at c/a=√2, spurious.

**C_A(3) ≠ 0 ⇒ Theorem 1 is FALSE.**

---

## 3 — STEP 1: THEOREM 1 (no odd-length closed walks)

FALSE on the correct graph (C_A(3)=48). Consequence for the 21-vertex conjecture: it is **not**
killed by parity (App K's stated reason is void — parity no longer forbids odd loops). It is instead
excluded by **low-order dominance**: with a length-3 triangle present, the shortest loop sets the
scale. Using the gate's stated per-loop counting α₀^{L_min/2} with L_min = 3:

```
α₀^{3/2} = 6.38×10⁻⁴   ≫  m_e/m_P = 4.19×10⁻²³   (ratio 1.5×10¹⁹)
```

A triangle-dominated mass would be ~19 orders **too large**; a would-be 21-loop contribution
α₀^{21/2} ≈ 4.3×10⁻²³ is utterly subdominant to it. So the 21-loop is irrelevant not because it
can't exist (it can — odd loops exist) but because far shorter loops dominate the expansion by ~19
orders. (See §5 for the mass-scale inversion this implies.)

---

## 4 — STEP 2: THEOREM 2 (particle–hole symmetry / non-renormalization)  (`kaudit_2_band.py`)

**Band.** Single FCC band E(k) = −t·Γ(k). Verified in two coordinatisations that agree exactly:

```
BCT coords : Γ = 8 cos(k_x/2)cos(k_y/2)cos(k_z/√2) + 2cos k_x + 2cos k_y
std FCC    : Γ = 4[cos(k_x/2)cos(k_y/2)+cos(k_y/2)cos(k_z/2)+cos(k_z/2)cos(k_x/2)]

band range   E ∈ [−12t, +4t]     width 16t     E(Γ-point)=−12t = −(coordination)·t
```

- **PH-symmetric? NO.** The spectrum is **not** symmetric about E=0: it runs 12t below zero but only
  4t above. Asymmetry metric Σ|ρ(E)−ρ(−E)|/Σ(…) = **0.51**. Half-filling **E_F = +0.92 t ≠ 0**.
  (Note: Tr H = 0 forces the band *mean* ⟨E⟩=0; this is **not** PH symmetry and does not give
  ρ(E)=ρ(−E). App K's ±t|γ₈| model gave a spurious symmetric [−8t,+8t] spectrum precisely because
  the two-sublattice chiral form enforces E→−E, an artifact of dropping the A–A/B–B bonds.)
- **G_loc(0).** ρ(0) = 0.110/t is **finite** (E=0 lies inside the band, near the top). The local
  Green's function G_loc(ω)=(1/N)Σ_k 1/(ω+iη−E_k) extrapolates to

```
Re G_loc(0) ≈ −0.20/t   (≠ 0),     Im G_loc(0) = −π ρ(0) ≈ −0.35/t.
```

**G_loc(0) ≠ 0 ⇒ Theorem 2 (which requires G_loc(0)=0 at every order) is FALSE.** The zero mode is
**not** protected; each self-energy order no longer carries a vanishing factor.

**Self-energy magnitude** (`kaudit_3_...py`). The leading perturbative mass, across every
power-counting convention consistent with App K/J:

| convention | value (Planck) | ratio to m_e/m_P | verdict |
|---|---|---|---|
| Σ ~ t²·\|G_loc(0)\| ≈ 0.2 α₀ | 1.48×10⁻³ | 3.5×10¹⁹ | ~20 orders too large |
| α₀^{L_min/2} = α₀^{3/2} (gate's stated counting) | 6.38×10⁻⁴ | 1.5×10¹⁹ | ~19 orders too large |
| a₃ = α₀³·C_A(3)/3 (integer closed-walk) | 6.51×10⁻⁶ | 1.6×10¹⁷ | ~17 orders too large |

The exact exponent depends on an **undeclared vertex power-counting convention** (integer t^n
hopping vs half-integer α₀^{ℓ/2} per loop; whether g=α₀ enters once or as √). This is a genuine
imprecision (notice CN-KAUD-05, ASSERTED). But the **sign and rough size of the inversion are
robust**: every convention gives a perturbative mass **15–20 orders too large**, never a protected
zero. **Corrected conclusion: m_e is not protected — it is generated at the wrong (far too large)
magnitude.**

**Photon/graviton corollary.** App K adds that the photon and graviton, as zero modes, are
*exactly* massless by the same PH protection. Since PH symmetry is absent, **that proof fails**.
Derived cold from the field content (single complex scalar Ψ = √ρ e^{iθ}, vacuum manifold S¹;
`MINIMAL_BCT.md` §1.1–1.5): the theory has exactly **one** guaranteed gapless mode — the U(1)
**Goldstone phonon (θ)** — massless by **Goldstone's theorem**, entirely independent of any lattice
PH symmetry. That protection is real but it protects **one scalar mode**. It does **not** deliver a
photon (needs 2 transverse polarisations) or a graviton (needs helicity ±2); a scalar Goldstone
supplies neither. So App K's corollary loses both its stated *proof* (PH) and its *subject* (there
is no photon/graviton in a one-component scalar theory to protect). Consistent with — but derived
independently of — the field-content findings.

---

## 5 — STEP 3: THEOREM 3 (gap equation) AND THE n=16 ACCIDENT  (`kaudit_3_...py`)

**Density of states.** App K's ρ(E) ~ E·ln(1/E) came from three assumed nodal planes of the
2-band ±|γ₈| structure — an artifact of the incorrect bipartite model. The correct **single FCC
band has a finite DOS across the interior**, ρ(0)=0.110/t, with a square-root band edge at −12t and
a van-Hove peak toward the top (ρ(+3.5t)=0.19 vs ρ(−11.5t)=0.005). It is **not** linear-with-log
and **not** nodal at E=0.

**Gap equation.** For 1 = g·∫ρ(E)/(E²+m²)dE:

```
FCC   :  I(m) = 0.29, 1.1, 3.5, 12.4, 39.2  at m = 1, 0.3, 0.1, 0.03, 0.01   → diverges as m→0
         (because ρ(0)≠0: I(m) ~ πρ(0)/m).   Critical coupling g_c = 1/I(0⁺) → 0.
LINEAR:  I(m→0) = 0.205  (converges)  → finite critical coupling g_c = 4.87  (a real threshold).
```

App K's "BCT coupling ~20× too weak" was the statement "g_BCT below the *finite* linear-DOS
threshold." **On the correct FCC DOS there is no threshold at all** — ρ(0)≠0 means a mass is
generated for *any* coupling. The corrected "factor" is therefore not 20 but **∞** (any coupling
suffices); the conclusion does not merely shift, it **inverts**, and the generated mass lands at the
~10⁻³ Planck scale of §4 — again far too large. Same destination as the perturbative estimate.

**n=16 near-coincidence — accident, confirmed (and a typo caught).** Reproduced the monotone even
series a_n = α₀^n C_A(n)/n from App K's (bipartite) counts:

```
n :   2        4        6        8        10       14       16
a_n:  2.20e-4  1.63e-7  2.20e-10 3.89e-13 7.97e-16 4.33e-21 1.10e-23
```

- Mean geometric ratio ≈ **9.8×10⁻⁴ per +2 in n (≈3.0 decades/step)**, confirming App K's "monotone
  series sweeping through the m_e/m_P scale" picture.
- **Null model.** A monotone ladder with ~3-decade steps places its nearest term within a factor f
  of any fixed target with expected multiplicity ~2·log₁₀(f)/(decades per step): **0.20 hits at
  f=2 (≈2.3 bits), 0.40 at f=4 (≈1.3 bits), 0.67 at f=10 (≈0.6 bits)**. The observed "a_16 within
  ≈factor 3.8 of m_e/m_P" is a **≈1-bit** event — an accident, exactly as App K states.
- **Typo caught:** App K's printed `a_16 = 1.0962×10⁻²⁶` disagrees with its own listed
  `t¹⁶C_A(16) = 1.7525×10⁻²²` by a factor of ~1000 (1.7525×10⁻²²/16 = **1.096×10⁻²³**, not
  10⁻²⁶). The correct a_16 = 1.096×10⁻²³ is what actually gives "≈ m_e/4" (m_e/4m_P = 1.05×10⁻²³,
  4.7% off). So App K's *narrative* is right and its *printed number* is a transcription slip;
  neither changes the verdict — it is a numerical accident. **App K's anti-numerology is correct and
  commendable.**

---

## 6 — STEP 4: THE STEELMAN (required)

**Strongest case that App K's theorems survive: an effectively bipartite / PH-symmetric electron
sector.** Two versions, presented at full strength, then tested.

**(S1) Pure sphere↔void Josephson hopping.** App J's hopping is the Josephson coupling between a
*sphere interior* and the *oct-void electron vortex* — an A↔B process by construction. If the
physical amplitude were **only** sphere↔void, with sphere–sphere (A–A) and void–void (B–B)
amplitudes exactly zero, the effective hopping graph would be bipartite (coordination 8), all closed
walks even, PH-symmetric — and App K's T1/T2 would stand, with the 8-coordination model the correct
*effective* description despite the geometric 12-coordination.

*Why it fails.* The in-plane A–A bonds are at the **identical** distance (1) as the A–B bonds, so
nothing suppresses them geometrically; a vanishing A–A amplitude would need a symmetry/selection
rule. App J's **own** minimal-loop count invokes "a triangle of three mutually touching spheres"
(line 344–347) — i.e. it treats sphere–sphere contact as a real bond, directly contradicting
A–A = 0. And under FCC point symmetry all 12 NN are equivalent, so no consistent rule zeroes 4 of
them while keeping 8. S1 is not available.

**(S2) Integrate out the spheres; electron on an interstitial sublattice.** The sphere on-site
energy is Planckian (κ₀ ≈ 3.4 m_P) while the electron vortex sits near zero, so the spheres could be
integrated out, leaving the electron on the **oct-void** sublattice — which one might hope is simple
tetragonal (bipartite, PH-symmetric).

*Why it fails.* The octahedral interstitial sites of an FCC lattice **themselves form an FCC
lattice** (coordination 12, non-bipartite). Integrating out the spheres does not produce a bipartite
electron lattice; it reproduces an FCC connectivity (now with sphere-mediated effective A–A/B–B
paths that *further* break PH symmetry). No interstitial sublattice of FCC is bipartite.

**Neither steelman succeeds.** The only lattice on which App K's T1/T2 hold is the 8-coordination
graph obtained by discarding same-distance bonds, and no physical or symmetry argument licenses that
discard at c/a=√2. **The theorems do not survive.**

---

## 7 — CN-KAUD NOTICES (tiered)

- **CN-KAUD-01 [FALSIFIED].** App K Theorem 1 (lattice bipartite; C_A(odd)=0). Refuted:
  C_A(3)=48, explicit triangle. `kaudit_1_lattice.py`.
- **CN-KAUD-02 [FALSIFIED].** App K coordination-8 premise (δ=(±½,±½,±√2/2), 8 NN). Refuted:
  coordination 12 (8 B + 4 in-plane A, all at distance 1). `kaudit_1_lattice.py`.
- **CN-KAUD-03 [PROVEN].** At c/a=√2 the A and B sublattices are equivalent points of one FCC
  Bravais lattice; the correct model is single-band. App K's ±t|γ₈| chiral 2-band spectrum is an
  artifact of an unnecessary sublattice split. `kaudit_1_lattice.py`, `kaudit_2_band.py`.
- **CN-KAUD-04 [FALSIFIED].** App K Theorem 2 (exact PH symmetry ⇒ G_loc(0)=0 ⇒ all-orders
  non-renormalization). Refuted: single FCC band [−12t,+4t] is PH-asymmetric (E_F=+0.92t);
  Re G_loc(0)≈−0.20/t ≠ 0. `kaudit_2_band.py`.
- **CN-KAUD-05 [ASSERTED].** The unprotected zero mode acquires a leading perturbative self-energy
  ~10⁻⁶–10⁻³ (Planck), i.e. 15–20 orders **above** m_e. The **sign/scale of the inversion is
  robust**; the exact exponent is ASSERTED pending a declared vertex power-counting convention
  (integer vs half-integer powers of α₀). `kaudit_3_selfenergy_gap_n16.py`.
- **CN-KAUD-06 [FALSIFIED].** App K Theorem 3 ("coupling ~20× too weak for dynamical mass"). On the
  correct FCC DOS ρ(0)≠0 ⇒ no critical coupling; a mass is generated for any coupling. The "too
  weak" conclusion inverts. `kaudit_3_selfenergy_gap_n16.py`.
- **CN-KAUD-07 [FALSIFIED / PROVEN].** App K's corollary "photon & graviton *exactly* massless by
  PH protection." FALSIFIED as stated (PH absent). PROVEN replacement: the U(1) Goldstone phonon is
  massless by Goldstone's theorem — but it is one scalar mode, not a 2-polarisation photon or a
  spin-2 graviton. Derived from field content, not inherited.
- **CN-KAUD-08 [PROVEN / FALSIFIED-minor].** App K's "a₁₆≈m_e/4 is a numerical accident" is correct
  (null model ≈1.3 bits at f=4) — PROVEN. Minor FALSIFIED: the *printed* a_16=1.0962×10⁻²⁶ is a
  ×1000 transcription error; the correct value 1.096×10⁻²³ is the one that matches the narrative.
  `kaudit_3_selfenergy_gap_n16.py`.
- **CN-KAUD-09 [PROVEN].** The steelman (S1 pure-Josephson-bipartite; S2 integrate-out-spheres)
  fails: same-distance in-plane bonds, FCC equivalence of all 12 NN, App J's own sphere–sphere
  triangle, and the FCC (non-bipartite) structure of the oct-void interstitial sublattice each block
  an effectively bipartite electron sector.

**Stop condition matched: SC-KAUD-1.** No stop condition licensed this verdict a priori; it is the
outcome of the recomputation.

---

## 8 — SCRIPTS (deterministic)

- `kaudit_1_lattice.py` — cold NN enumeration, bipartite/triangle test, C_A(3), A/B equivalence.
- `kaudit_2_band.py` — single FCC band, two-coordinatisation range check, PH-symmetry metric, DOS,
  ρ(0), half-filling E_F, G_loc(0).
- `kaudit_3_selfenergy_gap_n16.py` — self-energy magnitudes, gap-equation critical-coupling test
  (FCC vs linear DOS), n=16 series reproduction + null-model bits.

No randomness; fixed k-grids (up to 220³) and closed-form lattices. Re-run to reproduce every number
in this document.

---

## 9 — CONTAMINATION STATEMENT

Inheritance is forbidden by §0.3; the following prior findings *reached* me and are declared. **None
was used as an input.** Every quantitative claim above was re-derived from the lattice definition and
standard field theory by the three scripts.

1. **The gate prompt itself** states Gate KND's conclusion (12-coordination, FCC, non-bipartite,
   PH-asymmetric band) in its framing (lines 17–22) and specifies the α₀^{L_min/2} counting. This is
   unavoidable context. I re-counted the shell, exhibited the triangle, and computed C_A(3), the
   band and G_loc(0) from scratch rather than citing it.
2. **The App K `.tex` I read carries an "audit banner"** (explicitly marked "audit addition, not the
   author's text", lines 69–95) that **pre-states the expected conclusions** — FCC, coordination 12,
   C_A(3)≠0, band PH-asymmetric, "T1 fails / T2 fails," low-order dominance ~α₀^{3/2}, self-energy
   ~10⁻⁴ "~19 orders too large," inverted diagnosis, even the band written as [−4t,+12t]. This is
   heavy contamination. I treated the banner as claims to check: I derived the coordination, triangle,
   C_A(3), band range **and its sign** (I find E=−tΓ ∈ [−12t,+4t]; the banner's [−4t,+12t] is the
   same band under the opposite sign of t, E=+tΓ), G_loc(0), the self-energy scale and the DOS
   independently. My agreement with the banner is a *reproduction*, not an inheritance.
3. **`audit/MINIMAL_BCT.md`** (permitted) summarises several prior gate verdicts (RANK, MAD, LINK,
   N, G′). I used only its statements of the *theory's field content* (single complex scalar, S¹,
   one Goldstone) and the *canonical constants* (r_oct, r_tet, α₀) as primary inputs; I did not
   inherit its gate verdicts as conclusions. The photon/graviton corollary was re-derived from the
   field content directly.
4. **My own persistent memory** lists prior-gate files (`gate-jhf`, `gates-closed-archive`,
   `gates-rank-mp-pred`, the Cold Ledger `audit-findings`, `ledger-provisional-obs`). Per §0.2
   quarantine I **did not open any of them** during this gate. I also did not read `audit/notes/` or
   any `audit/gates/*/` deliverable; the repo tarball was extracted but only App K, App J and
   `MINIMAL_BCT.md` were read from it.

App E was searched for (single-letter appendix under `tex/`) and **not found**; its absence did not
block the recomputation (App K contains the needed model), so SC-KAUD-4 was not triggered.

---

## 10 — §0.5 REPRODUCED VERBATIM

> This gate decides whether App K's three theorems are sound on the real c/a=√2 FCC lattice. It does
> not by itself decide whether BCT can ever produce m_e — that awaits a PH-breaking mechanism (App
> K's Candidates 1–3), each a separate later gate. A verdict of "theorems fail" does not refute the
> geometry (α₀, void radii, the surviving LO layer are untouched) — it means App K's proofs, and its
> corollary that the photon/graviton are *exactly* massless by PH protection, must be redone on the
> correct lattice. A verdict of "the corrected route still cannot give m_e at the right magnitude"
> is a legitimate sharpening of the hierarchy problem, not a vindication of the rest of BCT.

---

## 11 — WHAT THIS GATE DID **NOT** ESTABLISH

- It did **not** construct a PH-breaking mass mechanism. App K's Candidates 1–3 (quark–lepton
  r_tet≠r_oct asymmetry; Chern–Simons; Wilson/temporal mass) remain untested and are each a separate
  later gate. This gate only audits the three written theorems by recomputation.
- It did **not** show BCT *can* produce m_e at the correct magnitude. The perturbative route fails
  (mass far too large); whether some geometry-fixed PH-breaking lands at 4×10⁻²³ with no new
  parameter (SC-KAUD-3) is **not** decided here and was not built.
- It did **not** refute the geometry. α₀, the void radii, and the surviving LO layer are untouched
  by this result.
- The exact self-energy **exponent** is left ASSERTED (CN-KAUD-05): the BCT fermion vertex
  power-counting is not declared precisely enough to fix integer vs half-integer powers of α₀. The
  *band* and *Green's function* were well-defined enough to recompute (so no SC-KAUD-4 halt); only
  the leading-mass exponent carries this residual imprecision.

*Gate KAUDIT executed by Claude Opus 4.8, 15 September 2026. Verdict SC-KAUD-1. Digest
c6da27858da0d675cf525df68a882c45055234a3ce3d22dc1b76367176f0a0e1.*
