# Gate SINGLET — RESULT
## Can written BCT structure supply a signed measure?

**Verdict: SC-SINGLET-2 (IMPORT).** The singlet curve can be built on BCT's variables, but only by adding the signed-measure ingredients. On the written S¹ phase, all three ingredients are added: the Z₂ sign, the non-negative local process and the squared readout. On the ℂ² branch, the Z₂ sign comes with the field, but the process and the readout are still added. BCT supplies nothing the prior construction had to assume, except, on the contested ℂ² branch, a Z₂ that it gets by positing a spinor field. SC-SINGLET-5 is not triggered: the corpus writes the same field two ways (S¹ and ℂ²), but the verdict is the same on both branches.

Run 25 Oct 2026, fresh thread, one gate. Runner: Claude Opus 5.5. Tier cap: none (fresh thread).

---

## 0. Digest and run record

| Item | Value |
|---|---|
| Card URL | `https://raw.githubusercontent.com/zerofreeparameters-code/BCT-Programme/fc4b63261eafb042922c929ce6d5b9d8446a96d7/audit/gates/gate_SINGLET_prompt.md` |
| Card bytes on disk | 10,238 |
| **SHA-256 computed on disk, before reading** | `272dca3d944518233b2f8e1846f179974fccfd1290006d3ed9dc8dfcb94ed16e` |
| **SHA-256 in `audit/gates/PREREG_20261025_SINGLET.sha256` @ fc4b632** | `272dca3d944518233b2f8e1846f179974fccfd1290006d3ed9dc8dfcb94ed16e` |
| Match | yes; the card was opened only after the match. The repo copy at fc4b632 has the same digest. |
| Repo | cloned over HTTPS, `git checkout fc4b63261eafb042922c929ce6d5b9d8446a96d7` confirmed |
| Letter 254 pin | `git show 501ea79:BCT_Letter254_Entanglement.tex`, SHA-256 `d849e96dd52ec43c43f581d98e4cae0e3586f3bd38d0c3397f2aa6dc4863b32d` (matches card §0.2). No later revision read. |
| As-run prompt | `gate_SINGLET_prompt_asrun.md` = the card, byte-identical (same SHA-256) |
| Hsieh files (supplied by the user as attachments; Zenodo downloads were blocked from the workspace) | `z2_holonomy_bell_correlations_zenodo.pdf` 176,216 B, SHA-256 `a10c8ab8…3d31`; `Holographic Fiber Theory_v22.pdf` 446,341 B, `8efb4cd7…9e25`; `chsh_sandbox.py` `9466a2be…9996`; `nosignaling_completeness.py` `b014ec98…6887`; `kernel_universality.py` `18091474…79e2`; `fr_identity.py` `3900e4e2…c3dc`; `feynman_kac_enumeration.py` `81526aa8…aa03c`; `appH_bell_sandbox.py` `77b9fb56…2bea`. Sizes match the Zenodo record listings. |

**Appendix JH: which version is canonical.** `tex/` holds four copies:

- **Treated as canonical: `BCT_Appendix_JH_FINAL.tex`.**
  - It is the file named FINAL and carries the Zenodo DOI 10.5281/zenodo.18975018 in its date line.
  - `BCT_Appendix_JH (1).tex` is byte-identical to it.
  - `BCT_Appendix_JH_GRRRRRRRR.tex` differs only in one bibliography string (l.521).
  - `BCT_Appendix_JH.tex` differs only in front matter (title layout, section-number macros, abstract label, table of contents) and two bibliography entries.
  - The physics text and every equation are identical across all four, so the choice does not affect the result.
- **Not a JH version: `BCT_Appendix_JH4_YangMills_v2_CORRECTED.tex`.** It is a separate appendix (SU(3) Yang–Mills scope). It was read only for its transfer-matrix passage (§4, ingredient (i)), and that is disclosed.

---

## 1. Verdict

**SC-SINGLET-2 (IMPORT).**

**What must be added, by branch:**

| | S¹ branch (written complex scalar) | ℂ² branch (App JH interior field) |
|---|---|---|
| (a) double cover of the phase register with the antiperiodic (q = ½) sector, i.e. a half-flux on the register | **added** | comes with the field (SU(2) centre −1) |
| (b) a non-negative local Markov kernel on the register, run to the coarse-grained limit | **added** | **added** (inert, see §4) |
| (c) a squared readout, two outcomes, complete on the coarse-grained doublet | **added** | **added** |
| (d) a source emitting two registers a half-turn apart, summed over source framing | **added** | **added** |
| (e) identification of measurement settings with register angles (S¹) or with SU(2) rotations of Ψ₂ (ℂ²) | **added** | **added** |

**What BCT supplies that the prior construction assumed:**
- **S¹ branch: nothing.** BCT's written U(1) phase is the same kind of object as Hsieh's phase register, but both are postulated. Any U(1) field supplies such a circle. The harmonics of the written single-valued field are integer, so the field points to the periodic sector, not the antiperiodic one.
- **ℂ² branch: the Z₂ sign.** It arrives with a two-component field, which is more structure than the single sign Hsieh adds. That field is contradicted elsewhere in the corpus (§3). The point is moot for SC-1 in any case, because SC-1 also requires (i) and (iii) to be written.

**Stop conditions not triggered:**
- **SC-SINGLET-1:** (i) and (iii) are written nowhere in the permitted sources (§4).
- **SC-SINGLET-3:** a carrier is minimally addable on the S¹ branch (the antiperiodic sector of the written phase), and a ℂ² state space is written on the other branch.
- **SC-SINGLET-4:** no construction reaches −cos θ while a marginal depends on the distant setting.
  - With the singlet source, marginals are exactly ½ at every walk length t.
  - With a tilted source, the finite-t leak is n = 3 mode contamination, C(β)·β·(λ₃/λ₁)ᵗ with C constant in t for t ≥ 200 (C = 0.978 at β = 0.3, 0.917 at β = 0.6), and it vanishes in the limit (§6).
- **SC-SINGLET-5:** the S¹/ℂ² conflict is real (§3), but the verdict does not differ between branches.

**Stated prior: SC-SINGLET-2.** It was overturnable: the positive control (§2) shows the gate can find a survivor when the ingredients are present. The verdict rests on the citations and computations below, not on the prior.

---

## 2. Step 0 — baseline and positive control

Code: `singlet_step0.py`, output `singlet_step0_output.txt`. Written before reading Hsieh's paper or code, from the card's one-line description only.

**Baseline.** All 16 deterministic local strategies were enumerated: max |S| = **2** for S = E(a,b) − E(a,b′) + E(a′,b) + E(a′,b′). Every local-hidden-variable mixture is in their convex hull.

**Construction (runner's own):**
- **Base circle:** m sites, φⱼ = 2πj/m.
- **Double cover:** 2m sites ψₖ = 2πk/m ∈ [0, 4π).
- **Walk:** lazy nearest-neighbour Markov kernel, K[k,k] = 1 − p, K[k,k±1] = p/2 (non-negative, local, row-stochastic).
- **Z₂ sign:** the signed endpoint count G_t(k,j) = Kᵗ[k,j] − Kᵗ[k,j+m]. Equivalently, the walk on the m-site base circle with holonomy −1 on the seam bond. The two forms agree to 4×10⁻¹⁷ at t = 60; the seam form is used because it avoids cancelling the even modes.
- **Source:** walker A starts at k and walker B at k + m/2; k is summed over the cover.
- **Settings and outcomes:** setting a at site j_a; outcome + reads j_a, outcome − reads j_a + m/2.
- **Amplitude:** M(A,B) = Σₖ G_t(k, j_A) G_t(k + m/2, j_B).
- **Readout:** P = M²/Σ M².
- **Closed form:** by the semigroup property, M = c·g₂ₜ(j_A − j_B + m/2), with g₂ₜ(x) = (1/m) Σ_{n odd} λₙ^{2t} cos(πnx/m) and λₙ = 1 − p + p cos(πn/m).
- **Limit:** as t → ∞ only n = ±1 survives (cos ψ/2 and sin ψ/2), so P(++) = P(−−) = ½ sin²((a−b)/2), P(+−) = P(−+) = ½ cos²((a−b)/2), and **E = −cos(a − b)** with a setting-independent normalisation.

**Positive control result** (m = 24, p = ½, t = 3200, all 576 setting pairs):

| Check | Value | Card target |
|---|---|---|
| max over all (a,b) of \|E + cos(b − a)\| | **8.9×10⁻¹⁶** | < 10⁻³ |
| S at (0, π/2, π/4, 3π/4) | **−2.828427124746190** (2√2 = 2.828427124746190) | 2√2 ± 10⁻³ |
| max spread of P_A(+\|a,b) over the distant b (and of P_B over a) | **4.4×10⁻¹⁶** | < 10⁻⁹ |
| relative variation of the normalisation N(a,b) = Σ M² | 1.4×10⁻¹⁵ | — |
| relative variation of the local completeness C_a(k,k′) = Σ_A u_{a,A}(k)u_{a,A}(k′) | 4.2×10⁻¹⁶ | — |
| mpmath (40 dps) closed form at 45°, 90°, 135° | agrees with the matrix result to ≤ 10⁻¹⁵ | — |

**Convergence** (from the output): max |E + cos θ| = 1.5×10⁻³ (t = 100), 1.5×10⁻⁶ (200), 1.5×10⁻¹² (400), 7×10⁻¹⁶ (800). The rate is (λ₃/λ₁)^{2t}, with λ₃/λ₁ = 0.966072207083.

**The gate can find a survivor.**

**Ablations, with one qualification the card did not anticipate:**

1. **Z₂ sign dropped** (periodic sector = the plain walk on the base circle), square kept. In the limit the n = 0 mode dominates: |S| < 10⁻¹⁵ and E ≡ 0.
   - **However, at short t the per-pair-normalised readout reaches |S| = 4.000** (t = 2, with 144 of 576 pairs undefined because N = 0), 3.9946 (t = 10) and 2.537 (t = 40), with marginals flat to 10⁻¹⁶.
   - The antiperiodic sector shows the same short-t excess: |S| = 3.99 at t = 10, with the spread of N, (max − min)/mean, equal to 2.0.
   - The excess is bought by the normalisation N(a,b), which depends on both settings.
   - **When N is required to be setting-independent (relative variation < 10⁻³), the periodic sector's best is |S| = 0.177; the antiperiodic sector's is 2.8298, at t = 121.** The antiperiodic value's 1.3×10⁻³ excess over 2√2 is the finite-t residue that a 10⁻³ tolerance on N still allows; it vanishes as the tolerance tightens.
   - So the card's claim holds once the normalisation is required to be local. Without that requirement it fails at short t.
2. **Square dropped, sign kept** (linear readout of the signed sum).
   - The normalised "probabilities" at (0°, 45°) are [[0.5, 1.207], [−1.207, 0.5]], with negative entries.
   - Lifting setting a to the other sheet flips the sign of M(+,·). A linear readout is therefore not even a function of the setting on the phase circle; the square is what makes the readout well defined on the base.
3. **Square replaced by a local sign readout** (A = sign G(k, j_a), mixed over k): max |S| over all 24⁴ setting quadruples = **2.000000000000**, as Bell requires.
4. **Readout exponent.** |M|^q, Z₂ kept, t = 3200:

| q | 0.5 | 1 | 1.5 | **2** | 3 | 4 | 8 | 32 |
|---|---|---|---|---|---|---|---|---|
| \|S\| | 0.867 | 1.657 | 2.316 | **2.828** | 3.469 | 3.771 | 3.993 | 4.000 |
| rel. var. N(a,b) | 0.45 | 0.33 | 0.17 | **1.4×10⁻¹⁵** | 0.35 | 0.67 | 1.6 | 3.6 |

   - The marginals are ½ for every q, because the outcome flip a → a + π swaps the two terms of Σ_B |M|^q.
   - In closed form, Σ_AB |M|^q = 2(|sin θ/2|^q + |cos θ/2|^q), which is setting-independent **if and only if q = 2**.
   - **Non-negativity plus flat marginals do not force the square.** Exponents q > 2 give |S| > 2√2, rising to 4, with no signalling, but only after a normalisation that depends on both settings.
   - **The square is singled out by requiring a setting-independent normalisation (completeness).**
5. **Kernel and m independence.**
   - Five kernels give the same limit within 1.5×10⁻¹⁴: nearest-neighbour with p = 0.5, 0.9 and 0.1; nearest plus next-nearest; and a binomial kernel of range 3.
   - m = 8, 16, 24, 48 and 96 give the same limit within 1.7×10⁻¹⁴.
   - **The walk only filters down to the lowest antiperiodic harmonic. The curve lives in ingredients (ii) and (iii).**

---

## 3. Step 1 — the carrier (spin-½ readout)

**Topology first.**

| Field | Target and homotopy |
|---|---|
| Written scalar Ψ = √ρ e^{iθ} | **S¹**; π₁(S¹) = ℤ; π₂ = π₃ = π₄ = 0 |
| App JH unit field Ψ₂/\|Ψ₂\| ∈ ℂ² | **S³**, not S²; π₁(S³) = 0, π₃(S³) = ℤ, π₄(S³) = ℤ₂ |
| Hopf projection n̂ = χ†σχ of that field | **S²**; π₃(S²) = ℤ, π₄(S²) = ℤ₂ |

These are standard homotopy groups; the S³ and S² targets are checked numerically in `singlet_step3.py` §C1.

| Candidate | Written source | Two-outcome readout with overlap cos(θ/2)? | Status |
|---|---|---|---|
| **Written S¹ phase θ** | AZ6 eq:SGP (l.128–135, "complex scalar order parameter"); App J eq:GP (l.102–104), eq:action (l.133–137); Letter 60 GP (l.70); AZ7 axiom Ψ ∈ ℂ (l.84–88) and Thm "Scalar order parameter" (l.397–410) | No. A single-valued Ψ has integer harmonics e^{iqθ}, q ∈ ℤ, and no half-angle overlap. No readout rule is written anywhere. | **absent** as a spin-½ carrier; **addable**: double cover + antiperiodic sector + readout (§2) |
| **Vortex strings** (frame register) | Letter 60 profile f″ + f′/r − H²f/r² + (1−f²)f = 0 (l.78), i.e. Ψ = f(r)e^{iHφ} | Rotating space by α about the axis gives Ψ → e^{−iHα}Ψ. The condensate phase is therefore a frame locked to spatial rotation, but **with integer locking**: a 2π rotation gives e^{−2πiH} = +1 (step3 §A1). The periodic sector only. | **absent** (a half-quantum vortex e^{iφ/2} is not single-valued; step3 §A3) |
| **App JH ℂ² interior field** | App JH l.194–198: Ψ₂: B³(R_s) → ℂ², \|ψ₊\|² + \|ψ₋\|² = ρ₀; eq:free-energy (l.201–207); eq:hopf-invariant (l.166–171) | The state space is written. The real-spinor circle χ(ψ) = (cos ψ/2, sin ψ/2) double-covers a great circle of Bloch vectors, with \|⟨χ(a)\|χ(b)⟩\| = \|cos((a−b)/2)\| (step3 §C2). **No readout, projector, measurement rule or setting identification is written** (no "Born", "projector" or "readout" hit in the permitted files; §4). | **state space written; readout absent** |
| OneMedium "two-component order parameter of the octahedral void condensate" | OneMedium l.702 (prose; source of SU(2)_L) | prose only; no equation | absent (prose) |
| Letter 254 "single Hopf configuration" | L254 l.86–88 (Hopf integral, a definition), l.93–105, 109–118 (prose) | No readout equation; the mechanism is read-a-pre-fixed-value (§8, CN-SINGLET-10) | absent |

**Branch conflict** (the card's SC-5 example):
- **The same symbol Ψ₂ is declared both ways:**
  - App J, which App JH builds on, writes Ψ₂ as one complex scalar and calls its action "the same GP action as the exterior" (l.71, l.139).
  - App JH redeclares Ψ₂ as ℂ² (l.194).
- **The surrounding sources split too:**
  - AZ7's theorem makes the order parameter a spin-0 complex scalar and explicitly excludes two-component spinors (l.359–410).
  - Letter 60 calls Ψ₂ a map S³ → S² (l.64) but writes its dynamics as a scalar GP equation (l.70).
  - Letter 64 cites Letter 27 for a GP equation with |Ψ|⁴ potential (l.80–81), yet uses the map Ψ/|Ψ|: ℝ³ → S² (l.110), which needs two components.
  - OneMedium makes the octahedral (exterior) condensate two-component in prose (l.702).
- **Two further defects of the ℂ² branch** (side findings, CN-SINGLET-11):
  - App JH's "Ψ̂₂ maps S³ → S²" conflates the field map (target S³) with the Hopf projection.
  - Under App JH's own constraint |Ψ₂|² = ρ₀, the free energy reduces to a constant plus a Dirichlet energy, which has **no minimiser in any nonzero-degree class**. The H = 1 "unique smooth ground state" is therefore not selected by the written F.

---

## 4. Step 2 — the three ingredients

Search script `singlet_search.py` (output `singlet_search_output.txt`) covers exactly the card's file list, plus JH4 (disclosed). Every hit line was read in context.

| Ingredient | S¹ branch (written / addable / absent) | ℂ² branch (written / addable / absent) | Citations | Minimal addition (what "addable" means) |
|---|---|---|---|---|
| **(i) Non-negative local process on the phase variable** | **absent** (NONE FOUND); addable | **absent** (NONE FOUND); addable | See the hit list below. | A non-negative, rotation-invariant, local Markov kernel on the 2m-site register, run to the coarse-grained limit. Any lazy local kernel gives the same limit (§2 ablation 5), so the content of the addition is "filter to the lowest antiperiodic harmonic". On the ℂ² branch the walk is **inert**: the readout vector ⟨χ(a)\|χ(ψ)⟩ is already the pure n = ±1 harmonic (step3 §C3). |
| **(ii) Z₂ sign on loops of a double cover** | **absent** (NONE FOUND); addable. See (ii-a) to (ii-d) below. | **written as structure, unconnected.** The unit field lies in S³ = SU(2) and the free energy F is U(2)-invariant, so the SU(2) centre −1 is present and the real-spinor circle is automatically antiperiodic (step3 §C2). Nothing written connects this sign to a readout or a setting. App JH's own statement of it is prose: "phase π per traversal" (l.313–318); eq:double-cover (l.309–312) is just the symbol SU(2) → SO(3). | App JH l.86–89, 303–324; L36 l.167–175; OneMedium l.547 and Monograph l.1558–1568 ("π phase under 2π rotation", prose) | S¹: the double cover with the antiperiodic sector, i.e. a half-flux on the register. ℂ²: the identification of settings with SU(2) rotations of Ψ₂. |
| **(iii) Squared readout of a signed sum** | **absent** (NONE FOUND); addable | **absent** (NONE FOUND); addable | "Born": 0 hits; "readout", "read out", "projector": 0 hits; "probabilit": 3 hits (L64 l.54, Barandes context; JH4 ×2, Wilson measure). OneMedium l.361–363: ħ, superposition and the Hilbert-space postulates **are inputs**, i.e. the corpus postulates QM as a whole and writes no readout rule of its own. | The squared two-outcome readout P = M²/N, complete on the doublet (normalisation setting-independent). |

**Ingredient (i): what the search found.**
- No stochastic rule, master equation, Langevin equation, random walk or transfer operator on the phase is written anywhere in the permitted files.
- **L64 Theorem I** (l.86–123) invokes Barandes's stochastic processes, but writes no process. It asserts that **no Markovian stochastic process can reproduce the OHC dynamics** (l.88–89, 117), which is the opposite of the Markovian walk the route uses.
- **AZ6, App J and L60** write only the deterministic GP flow or static equations.
- **App J** mentions a "lattice path integral" (l.86, 377) and a "path integral" (l.332, 351, 395) but never writes one.
- **JH4** writes a positive transfer matrix (l.92) for SU(3) Wilson link variables, not for the phase.

**Ingredient (ii), S¹ branch: the four places a sign could come from.**
- **(ii-a) The field itself.** Single-valued Ψ has integer charges only, giving holonomy +1 per turn (step3 §A1–A2). Built on the written register, the construction gives **|S| = 0, E ≡ 0**; with q = ½ added it gives 2√2.
- **(ii-b) Vortices.** No half-quantum vortices (π₁(S¹) = ℤ; step3 §A3), and integer vortex locking.
- **(ii-c) Lattice point group** (step3 §D).
  - The c/a = √2 lattice is fcc: 12 nearest neighbours at one distance, point group of order 48 with 3-fold axes, i.e. O_h. AZ7 l.340 uses C₄ᵥ.
  - Of the 8 spin structures on the lattice torus, **O_h and O each leave exactly one invariant, the trivial (periodic) one**. D₄h and C₄ᵥ leave two (the trivial one, and the one antiperiodic along the body-centring translations while periodic along a, b and c), and the choice between them is then free.
  - Either way the point group does not supply an antiperiodic sector, and a spin structure of space acts on spatial loops, not on the internal register.
  - AZ7's "spinor excluded" lemma mislabels the E irrep of C₄ᵥ, which is single-valued (C₄⁴ = +1).
- **(ii-d) The Monograph's "D₄ ℤ₂ centre"** (l.1086–1118, 1511–1520) is a global symmetry r → −r, not a holonomy.

---

## 5. Step 3 — curve, signalling, and the construction on BCT variables

(i)–(iii) are not all supplied, so the card's conditional build is not a BCT construction. What follows is the construction on BCT's variables with the named additions, to show what the additions buy and that no BCT input enters.

**E(θ) table** (t = 3200, a = 0, b = θ; the S¹ register with the q = ½ sector added, which is the same construction as the positive control):

| θ (°) | E(θ) | −cos θ | \|ΔE\| |
|---|---|---|---|
| 0 | −1.000000000000000 | −1.000000000000000 | 0 |
| 15 | −0.965925826289068 | −0.965925826289068 | 1×10⁻¹⁶ |
| 30 | −0.866025403784439 | −0.866025403784439 | 1×10⁻¹⁶ |
| 45 | −0.707106781186547 | −0.707106781186548 | 1×10⁻¹⁶ |
| 60 | −0.500000000000000 | −0.500000000000000 | 0 |
| 75 | −0.258819045102521 | −0.258819045102521 | 2×10⁻¹⁶ |
| 90 | −0.000000000000000 | −0.000000000000000 | 5×10⁻¹⁷ |
| 105 | +0.258819045102521 | +0.258819045102521 | 6×10⁻¹⁷ |
| 120 | +0.500000000000000 | +0.500000000000000 | 2×10⁻¹⁶ |
| 135 | +0.707106781186547 | +0.707106781186547 | 1×10⁻¹⁶ |
| 150 | +0.866025403784439 | +0.866025403784439 | 0 |
| 165 | +0.965925826289068 | +0.965925826289068 | 0 |
| 180 | +1.000000000000000 | +1.000000000000000 | 0 |

**CHSH, marginals and normalisation:** as in §2 (S = −2√2 to 15 digits; marginals flat to 4×10⁻¹⁶). On the ℂ² branch, with the walk, readout and source added, the same values hold: max |E + cos θ| = 7.9×10⁻¹⁶, |S| = 2.828427124746, marginal spread 5.6×10⁻¹⁶ (step3 §C3).

**Figure:** `singlet_E_theta.png`. It shows E(θ) for the squared readout (on −cos θ), the |M|⁴ readout and the site-complete hemisphere readout. The same numbers are in the tables of §2 and §6.

**No BCT number enters** (step3 §B). Each of the following gives max |E + cos θ| ≤ 3.4×10⁻¹⁴ and |S| = 2√2 to 13 digits:

| Choice | Origin |
|---|---|
| p = α₀ = 0.007408055727548 | AZ7 Lemma: hopping t = α₀ |
| m = 8, p = α₀ | coordination z = 8 |
| m = 48, p = 2α₀ | — |
| m = 24, p = ½ | Hsieh's reference values |

BCT inputs change only the convergence rate (t from 468 to 63,708). r_oct, r_tet, ξ/a and the Letter 254 identity 1/(2r_oct + 1) = cos(π/4) play no part. The 2√2 comes from cos(π/4) at the optimal settings, as in any qubit model.

**Signalling:**
- **Singlet source:** no construction signals. The marginals are exactly ½ at every t, by the a → a + π symmetry.
- **Tilted source** (Hsieh's β test): the per-pair-renormalised two-outcome readout leaks at finite t by C(β)·β·(λ₃/λ₁)ᵗ (C = 0.978 at β = 0.3, 0.917 at β = 0.6; constant in t for t ≥ 200). Projected onto the doublet it leaks ≤ 7×10⁻¹⁶ for every β (§6).
- SC-4 is not triggered.

---

## 6. Prior-art comparison

**Hsieh, Zenodo 21301391 (10 Jul 2026, v1), read in full.**

*What the construction is.* My independent construction matches its eq. (9) term for term: lazy walk on Z₂ₘ, antiperiodic projection eq. (2), source framing l with wing B at l + π, squared readout, normalisation Z(a,b) = 2 in the coarse-grained limit. Running his `chsh_sandbox.py` reproduces his values (CHSH −2.828427 at N = 300; variants B, C and D as stated). The output is filed here.

*Its assumptions, in its own terms:*
- **Register:** a phase register Z_m, m even, explicitly a regulator (§5.2).
- **Process:** Assumptions 1–4 (phase homogeneity, cocycle, locality/isotropy/laziness, base-measurable readout).
- **Z₂:** "The single topological datum **we add** is a flat Z₂ connection" (§2.2).
- **Readout:** a forward path paired with a backward path, "the amplitude doubling of the Born rule", giving the pairing measure μ = |Σwχ|² (eq. 4).
- **Source:** a singlet source with oppositely oriented frames, plus F2 (relational anchoring) for Theorem 2.
- **Limit:** the coarse-grained limit N ≫ τ_mix.

*Three findings about the prior construction from this run* (none changes Theorem 3's limit statement):

1. **The square is definitional, not derived.** Theorem 4's (G1) is linearity "in the pairing measure", and eq. (4) defines that measure as already squared. In the construction itself, non-negativity plus flat marginals do not force q = 2: |M|^q with q > 2 is no-signalling and exceeds 2√2. What singles out q = 2 is a setting-independent normalisation (§2 ablation 4). The square is therefore assumed via (G1)/eq. (4), or via completeness. Hsieh's "unique non-negative valuation" holds only relative to those axioms; his §4.4 says as much in "Relation to Gleason".
2. **"The Tsirelson value is a consequence of locality" needs the readout assumption.**
   - With per-pair normalisation, the same local kernels give |S| up to 4 at short t, in both sectors (§2 ablation 1), and for q > 2 at any t.
   - Hsieh's exclusion-table entry D mentions a transient in the periodic sector only.
   - His own text concedes that the upper bound "is inherited rather than reproven" from qubit quantum mechanics (§4.3).
   - Locality (his Remark 3) fixes which harmonic survives; the value 2√2 additionally needs q = 2 with a local normalisation.
3. **Proposition 7's numerical demonstration uses a readout that does not violate CHSH.**
   - Running his `nosignaling_completeness.py` (output filed):
     - The complete site readout E1 leaks at machine zero.
     - But E1 gives E(θ) = −0.4007 cos θ and **CHSH = −1.133**, below the local bound.
   - My code (`singlet_priorart.py`) confirms the limit: visibility V → 4/π² (0.400663 at m = 24, 0.405212 at m = 192; 4/π² = 0.405285) and |S| → 1.1463. E1 is an unsharp (POVM) readout of the doublet.
   - The readout that gives −cos θ is E0. Its tilted-source leak is **not** a post-selection artefact: it is n = 3 contamination: leak/(β(λ₃/λ₁)ᵗ) = 0.9790, 0.9780, 0.9780, 0.9780 at β = 0.3 and 0.9185, 0.9175, 0.9174, 0.9174 at β = 0.6, for t = 200, 300, 400, 600. At t = 300, β = 0.3 the leak is 9.340×10⁻⁶, Hsieh's printed value. The coefficient depends on β (≈ 1 as β → 0) but not on t. It vanishes on the doublet.
   - The construction is sound in the limit; the robustness demonstration in §5 is mislabelled.

*Does BCT supply anything this construction assumed?*

| Hsieh assumes | BCT |
|---|---|
| a compact phase register | **shared, not supplied.** BCT postulates a U(1) field (AZ7 calls the GP axiom a foundational postulate, l.47 and l.82); its harmonics are integer. |
| the antiperiodic (Z₂) sector, "added" | **S¹: not supplied** (the written field points to periodic). **ℂ²: supplied by positing a spinor field**, i.e. by assuming more. |
| a non-negative local Markov process | not supplied; L64 asserts non-Markovianity |
| the squared readout (eq. 4) | not supplied; OneMedium takes QM as input |
| a singlet source with opposite frames | not supplied. L254 describes a singlet as an "H = 0 configuration" with ±1 projections (l.98–101, 164–166), in prose, with no sign or square. |
| F2 (relational frame anchoring) | not supplied; vortex frames lock with integer winding |

**HFT v22, App. H** (Zenodo 21207025, v22, 7 Jul 2026). Read: App. H (pdftotext l.1892–1955), the Born-rule passage of App. F.4 (l.1825–1840), and the "Structural exclusions" paragraph of §9 (l.956–963). `appH_bell_sandbox.py` is the same program as `chsh_sandbox.py` (variable renamed; same output, filed). The Z₂ there is called the "vertex-exchange sign". App. H calls itself "a high-symmetry proof-of-concept, not the general theorem". Everything said above about 21301391 applies.

**Christian, R. Soc. Open Sci. 5, 180526 (2018)** (arXiv:1806.02392, abstract read), with its published responses:
- **What it claims:** a locally causal, deterministic and realistic account of quantum correlations from spinors of an 8-dimensional geometric algebra (S⁷), with the Bell bound extended to 2√2.
- **Gill, "Comment on …"** (arXiv:2106.03169v2, read; published as RSOS 9 (2), 2022, doi:10.1098/rsos.201909, per a search-result listing only): the algebra has zero divisors and contradicts Hurwitz; the challenge to Bell rests on algebra and calculus errors; the simulation code computes −a·b directly rather than from ±1 outcomes.
- **Royal Society Open Science expressions of concern:** 10 Apr 2019, rsos.190530 (metadata read via PubMed; text not readable), and a later one "following post-publication assessment", rsos.201777 (title and DOI only, from a search result).
- **Contrast.** Christian claims a non-negative local realist model, which Bell's theorem excludes. Hsieh's route is explicit about giving up positivity. Letter 254's rhetoric ("global topology", "not local hidden variables") resembles Christian's claim but writes no model at all. Neither escapes Bell without dropping positivity.

**Mosseri & Dandoloff, J. Phys. A 34, 10243 (2001)** (arXiv:quant-ph/0108137, abstract read; DOI 10.1088/0305-4470/34/47/324). The Hopf fibration that is "entanglement sensitive" is S⁷ → S⁴ (fibre S³) of the *two-qubit state space*. It presupposes the Hilbert space. Letter 254's "45° in the Hopf fibre bundle" (l.135–136) and App JH's S³ → S² of a *classical* ℂ² field are different objects.

**Quasi-probability literature:**
- **Al-Safi & Short, PRL 111, 170403 (2013)** (arXiv:1301.2170, abstract and theorem statements read; not cited by Hsieh). Every non-signalling correlation can be written as a local model with a signed, setting-independent hidden-variable distribution and non-negative local response functions. So **the signed-measure route is not specific to quantum correlations**: by itself it reaches PR boxes. This is consistent with the |M|^q family of §2. The quantum curve needs the extra readout assumption.
- **Spekkens.** Hsieh's [3] is the 2007 *toy theory* (PRA 75, 032110; not opened). From the runner's knowledge, not from this run, it uses non-negative epistemic states and cannot violate Bell. The negativity result is Spekkens, "Negativity and contextuality are equivalent notions of nonclassicality" (arXiv:0710.5549, abstract read; journal reference not shown on the page).
- **Wigner 1932** (Phys. Rev. 40, 749): not opened; it is the standard quasi-probability reference.
- **Fine 1982** (PRL 48, 291): not opened directly. Its content is as characterised in a secondary source (arXiv:quant-ph/0001017, read).

**Spin from a soliton (ℂ²/S² branch only).** Fermionic (Finkelstein–Rubinstein) quantisation of Hopf solitons with odd Hopf charge is possible (arXiv:hep-th/0503067, abstract read; authors Krusch & Speight per the search listing; journal reference not confirmed). The relevant π₄(S²) = π₄(S³) = ℤ₂, whereas π₄(S¹) = 0. It requires quantising the soliton, which adds quantum mechanics, and it is unavailable on the S¹ branch.

---

## 7. Step 4 — steelman, both directions

**For (BCT supplies the route):**

1. *The compact S¹ phase is the same kind of object as Hsieh's register.* **True as far as it goes.**
   - Hsieh says his Z₂ "requires only a carrier with nontrivial loops"; π₁(S¹) = ℤ.
   - His m is a regulator, and the continuum phase is the m → ∞ limit, where the construction still works (§2, m up to 96).
   - But the loops only make a Z₂ sector *possible*. H¹(S¹;ℤ₂) = ℤ₂ offers two sectors, and functions of the single-valued written Ψ live in the periodic one.
   - The register's Bell role, a frame locked to measurement rotations, appears in BCT only through vortex locking, which is integer.
   - **The point fails at the sector choice.**
2. *A ℂ² field carries an SU(2) double cover.* **This point succeeds, on the ℂ² branch, for ingredient (ii).** App JH writes Ψ₂ ∈ ℂ² with a U(2)-invariant free energy. The real-spinor circle is automatically antiperiodic, with no free choice, and Hsieh had to add exactly this datum. It does not move the verdict:
   - (i) and (iii) are still absent.
   - The Z₂ is obtained by positing a spinor field, which is more structure than Hsieh's single sign and is the very kinematics he derives.
   - App JH writes no readout and no setting identification.
   - The ℂ² field is static, confined to a sphere of radius ℓ_P/2, and contradicted by App J and AZ7.
   - Under App JH's own constraint, its free energy does not select the claimed H = 1 configuration.
3. *The corpus already invokes stochastic processes* (L64). **Fails.** L64 writes no process, asserts non-Markovianity (excluding a Markov walk), and appeals to Barandes, whose indivisible processes are equivalent to quantum mechanics, i.e. an import.
4. *JH4 writes a positive transfer matrix.* **Fails.** It acts on SU(3) link variables, not on the phase.
5. *OneMedium and the Monograph state "π phase under 2π rotation".* **Fails.** It is prose, false for the written scalar (§3), and obtainable on the ℂ² branch only by Finkelstein–Rubinstein quantisation, which is again an import.

**Against (BCT does not supply it):**

1. *A spin structure is extra data a scalar field does not fix.* **Succeeds, and more strongly.** The written field does fix a sector, the periodic one. The lattice point group (O_h for c/a = √2) fixes the spatial spin structure to the trivial one, and spatial spin structures do not act on the internal register.
2. *A scalar condensate has no half-quantum vortices.* **Succeeds.** π₁(S¹) = ℤ. On the ℂ² branch with U(2)-invariant F, the vacuum manifold is S³ with π₁ = 0, so there are no stable vortices at all.
3. *`MINIMAL_BCT.md` records per-sphere interior structure as closed (ξ > a).* **Partly sustained on re-check.**
   - ξ = 2.3175a against R_s = a/2 closes independent *amplitude* structure inside a sphere. App J also makes Ψ continuous across the shell (l.127).
   - A constant-density *direction* texture of a ℂ² field is not excluded by ξ alone. But the written F has no term that stabilises one: its Dirichlet energy scales with size, so it has no minimiser in any nonzero-degree class (step3 §E).
4. *The squared readout is a postulate in the prior construction too.* **Succeeds.** Eq. (4) defines the readout event as a squared pairing, and Theorem 4's (G1) is linearity in that measure. The construction itself does not force q = 2 without a completeness requirement (§2 ablation 4).

**Summary.** The steelman against succeeds on all four points, the third partly. The steelman for succeeds on one point, the ℂ² branch's Z₂ (stated prominently above), and that does not change the verdict.

---

## 8. CN-SINGLET notices

Tiers: PROVEN = derived or computed in this run, with code; CONJECTURE; ASSERTED = a corpus or literature claim recorded, not established here.

**CN-SINGLET-01 — PROVEN (computation).** Positive control.
- (a) An independent re-implementation of the signed-measure construction gives E(θ) = −cos θ at all 576 setting pairs (|ΔE| ≤ 9×10⁻¹⁶), |S| = 2√2 (15 digits) and distant-setting-independent marginals (≤ 4.4×10⁻¹⁶), in the coarse-grained limit.
- (b) It agrees term for term with Hsieh's eq. (9)–(10) and with his sandbox output.
- (c) The gate could therefore find a survivor.

**CN-SINGLET-02 — PROVEN (computation).** Ablations.
- (a) With a setting-independent normalisation required (relative variation < 10⁻³), dropping the Z₂ sign caps |S| at 0.177 (→ 0); dropping the square gives non-probabilities; a local sign readout gives |S| ≤ 2 exactly.
- (b) Without that requirement, per-pair normalisation produces |S| up to 4 with flat marginals at short walk lengths, in both sectors.

**CN-SINGLET-03 — PROVEN (computation and closed form).** Readout exponent.
- (a) In the construction, a readout |M|^q is no-signalling for every q > 0, with |S| rising monotonically from 0 to 4.
- (b) q = 2 is the unique exponent with a setting-independent normalisation.
- (c) Hence non-negativity does not force the Born square; completeness does.
- (d) Hsieh's Theorem 4 obtains uniqueness by defining the readout event as already squared (eq. 4).

**CN-SINGLET-04 — PROVEN (computation; prior art).** Hsieh's Proposition 7 demonstration.
- (a) The robustly no-signalling site-complete readout (E1) gives E = −V cos θ, V → 4/π², |S| → 1.146 < 2: no violation.
- (b) The violating two-outcome readout (E0) leaks under a tilted source by C(β)·β·(λ₃/λ₁)ᵗ (C constant in t for t ≥ 200; 0.978 at β = 0.3, 0.917 at β = 0.6), a finite-walk contamination that vanishes in the limit and on the doublet; it is not a post-selection artefact.
- (c) The prior construction's limit statement (Theorem 3) is unaffected.

**CN-SINGLET-05 — PROVEN (search and reading).** Ingredient (i).
- (a) No non-negative local process on the phase variable is written in any permitted source.
- (b) L64 asserts the opposite (no Markovian process) and writes none.
- (c) JH4's positive transfer matrix acts on SU(3) links.
- (d) Minimal addition: a lazy local Markov kernel on a 2m-site register, run to t → ∞. Its details do not matter (5 kernels, m = 8–96).

**CN-SINGLET-06 — PROVEN.** Ingredient (ii).
- (a) S¹ branch: single-valued Ψ admits only integer charges, so the written register is in the periodic sector (built on it, the construction gives |S| = 0).
- (b) No half-quantum vortices; vortex frames lock with integer winding.
- (c) The c/a = √2 lattice is fcc (point group O_h, order 48). Its point group leaves only the trivial (periodic) spin structure invariant; C₄ᵥ (used by AZ7) and D₄h leave the choice free. A spatial spin structure does not act on the internal register.
- (d) ℂ² branch: the SU(2) centre −1 is present and the real-spinor circle is automatically antiperiodic, but it is connected to no written readout or setting.
- (e) The Monograph's D₄ ℤ₂ centre is a global symmetry, not a holonomy.

**CN-SINGLET-07 — PROVEN (search) / ASSERTED (corpus position).** Ingredient (iii).
- (a) No readout rule is written ("Born", "readout", "projector": 0 hits).
- (b) OneMedium l.361–363 declares the Hilbert-space postulates inputs; the readout is postulated, not derived.

**CN-SINGLET-08 — PROVEN.** Carrier.
- (a) S¹ branch: no written spin-½ readout; minimally addable as the antiperiodic sector of the written phase plus a readout.
- (b) ℂ² branch: the spin-½ state space is written (target S³; Hopf projection to S²; overlaps cos(θ/2)); the readout is absent.
- (c) The written definitions conflict for the same Ψ₂ (App J and AZ7 scalar; App JH ℂ²; L60 and L64 mixed; OneMedium two-component in prose). The verdict is SC-2 on both branches, so SC-5 is not triggered.

**CN-SINGLET-09 — PROVEN (computation).** No BCT number enters E(θ).
- (a) m, p and t are regulators.
- (b) BCT-derived choices (p = α₀; m = 8 for z = 8; m = 48, p = 2α₀) give the same limit to ≤ 3.4×10⁻¹⁴.
- (c) The Letter 254 identity 1/(2r_oct + 1) = cos(π/4) plays no role and scores zero.

**CN-SINGLET-10 — PROVEN (Bell's theorem, re-traced from the written text).** Letter 254 @ 501ea79.
- (a) It writes one definition (the Hopf integral, l.86–88, normalised 1/16π²), the CHSH inequality and the r_oct identity; no dynamics and no readout.
- (b) Its mechanism, the configuration "fixed at creation" with measurement reading "the local projection" (l.103–105), is the local-hidden-variable form, so |S| ≤ 2 (16 strategies).
- (c) It has neither the Z₂ sign nor the square, so the signed-measure route does not rescue it without adding (i)–(iii).
- (d) Its claim that a single extended configuration reproduces the violations "exactly" (l.120–124) stays withdrawn.
- (e) This re-checks CN-MAD-04 and agrees with it.

**CN-SINGLET-11 — PROVEN (scaling argument and quadrature; side finding, not part of the verdict).** App JH topology and ground state.
- (a) The unit field Ψ₂/|Ψ₂| takes values in S³; "S³ → S²" in App JH (l.137–143, 197–198) is the Hopf projection, not the field map.
- (b) Under App JH's constraint |Ψ₂|² = ρ₀, eq:free-energy equals a constant plus (ħ²ρ₀/2m)·D with D the Dirichlet energy. A degree-1 texture of size ε has D = 53.908·ε (in units of R_s), so the H = 1 class has infimum equal to the H = 0 value and no minimiser.
- (c) App JH's selection of H = 1 rests on eq:hopf-matching (l.224–228), a net current out of a closed surface, which is not part of F.

**CN-SINGLET-12 — PROVEN (standard group theory, checked; side finding).** AZ7 "Argument 3".
- (a) The "E (spinor doublet)" representation of C₄ᵥ is the single-valued 2D representation (C₄⁴ = +1); spinor representations belong to the double group.
- (b) The c/a = √2 Bravais lattice has holohedry O_h, not C₄ᵥ.
- (c) AZ7's scalar conclusion stands only as a stated commitment.

**CN-SINGLET-13 — ASSERTED (prior art).** Al-Safi & Short (2013). Signed hidden-variable distributions with non-negative local responses reproduce every non-signalling correlation. The signed-measure exit from Bell is therefore generic; it singles out quantum correlations only together with an additional readout or completeness assumption, consistent with CN-SINGLET-03.

---

## 9. Untraced second-hand claims

| Claim | Where met | Status here |
|---|---|---|
| "Field content … PROVEN by Gate RANK" (one complex scalar) | `MINIMAL_BCT.md` §1.1 | Gate RANK not readable under quarantine. Re-checked only against AZ6, App J, AZ7 and L60 (scalar) and App JH and OneMedium (ℂ² / two-component). It is not true of every written source, hence the branch analysis. |
| "Cannot — per-sphere interior structure (ξ > a; Gate C1, SC-C1-1)" | `MINIMAL_BCT.md` §2 | Gate C1 not readable. Partly re-derived (§7, against 3). |
| XY/sine-Gordon lattice Hamiltonian H = −J Σ cos(θᵢ − θⱼ) (Vol 1 App E.1) | PILOT table D6 | Volume 1 is not in the card's file list. Not traced and not used. A Gibbs measure of it would be a static, non-negative measure, not a walk, and temperature is not written. |
| "The electron vortex is a fermion (spin ½, Appendices E.2 and G)" | App J l.331 | App E.2 and App G are not in the card's file list. Not traced. The allowed sources contain only prose versions (OneMedium l.547; Monograph l.1558–1568). |
| Barandes: QM equivalent to indivisible non-Markovian stochastic processes | L64 l.50–56 | Barandes's papers not opened. Used only as L64's own stated position. |
| App J transcription header: "interior field is one complex scalar (S¹); App JH redeclares … C² (S²)" | App J l.11–12 (a comment by whoever transcribed it) | Re-derived independently from the equations, with one correction: the unit ℂ² field is S³-valued; S² is its Hopf image. |
| CN-MAD-04 (Letter 254 is a local-hidden-variable model) | MAD RESULT | Re-traced to L254 @ 501ea79 (CN-SINGLET-10). |
| Hsieh's Theorem 2 (spin–statistics) and its hypothesis F2 | 21301391 §4.2 | Not assessed; outside this gate. |
| Content of the Christian expressions of concern | rsos.190530, rsos.201777 | Not read (PMC returned a verification page). Existence and DOIs only. |

---

## 10. Scripts and outputs (all in `audit/gates/SINGLET/`)

| File | What it does | Output |
|---|---|---|
| `singlet_step0.py` | 16 strategies; positive control (seam-sign kernel, double-cover cross-check, convergence, E table, CHSH, marginals, normalisation, local completeness, mpmath closed form); ablations (periodic sector, linear, sign-LHV, \|M\|^q, kernels, m) | `singlet_step0_output.txt` |
| `singlet_priorart.py` | tilted-source leak scaling vs t and on the doublet; site-complete hemisphere readout, visibility vs m | `singlet_priorart_output.txt` |
| `singlet_step3.py` | S¹ branch (integer charges, q = 1 vs q = ½, half-quantum-vortex check); BCT-number independence; ℂ² branch (S³ target, Hopf map, spinor circle, construction); lattice point group and spin structures; App JH Dirichlet scaling | `singlet_step3_output.txt` |
| `singlet_search.py` | corpus search over the card's file list (+ JH4), every hit line printed | `singlet_search_output.txt` |
| `singlet_plot.py` | the E(θ) figure | `singlet_E_theta.png` |
| `hsieh_chsh_sandbox_output.txt`, `hsieh_nosignaling_completeness_output.txt`, `hsieh_appH_bell_sandbox_output.txt` | output of Hsieh's own scripts (CC BY 4.0, Zenodo 21301391 / 21207025), run unmodified as `python3 -I <script>`; script SHA-256 in each header | — |

Run, from `audit/gates/SINGLET/`:
```
python3 -I singlet_step0.py singlet_step0_output.txt
python3 -I singlet_priorart.py singlet_priorart_output.txt
python3 -I singlet_step3.py singlet_step3_output.txt
python3 -I singlet_search.py <repo_root> <file from: git show 501ea79:BCT_Letter254_Entanglement.tex> singlet_search_output.txt
python3 -I singlet_plot.py singlet_E_theta.png
```
Requires numpy, scipy, mpmath and matplotlib (run with numpy 2.5.3, scipy 1.18.1, mpmath 1.4.1, matplotlib 3.11.2).

---

## 11. Contamination statement

- **Card.** Fetched by URL, hashed on disk, and opened only after the digest matched.
- **Memory listing.** The session began with an automatically injected *memory listing*: file names plus one-line descriptions of this project's memory files.
  - Some descriptions carry verdict codes of other gates (e.g. "Gate PILOT … pre-registered 6 Oct … located 25 Oct …", SC-ALTER-2, SC-EDM, SC-FORK-2).
  - None mentions SINGLET. **No memory file was opened.**
- **Project documents and files.** A list of project document names, and the project's attached files (paths only), were also in context. **None was opened.**
- **Past chats.** No past chat was searched or read.
- **Handoff text.** The user's message contained the terminal output of the apply script. It shows the subjects of the five commits applied on 25 Oct, including "Gate PILOT: run and close — SC-PILOT-3 (IMPORT)", "Gate PLASMOID: run and close (SC-PLASMOID-3 halt …)" and "Letter 254: Tsirelson status per CN-MAD-04 …".
- **Not read:** the 25 Oct drafting chat, any concurrent gate, and `audit/notes/`.
- **`audit/gates/PILOT/`, read under §0.2:**
  - Read in full: the RESULT, the as-run prompt, `pilot_tests.py` and its output, and the three `search_*.txt` files.
  - Read in part: the head of `search.py`; the head of `pilot_dispersion.py` and of its output.
  - The JSON files were inspected only for their keys.
- **`audit/gates/MAD/gate_MAD_RESULT.md`.**
  - Read: the verdict lines (l.1–9), §2 "Verdict, stated first" (l.70–94), and l.237–250.
  - **Overreach, disclosed:** l.237–250 included CN-MAD-05 and CN-MAD-06, beyond the permitted CN-MAD-04. A heading grep also exposed the section titles and short fragments at l.27, 296–299 and 314. None of these bears on the verdict.
- **`audit/MINIMAL_BCT.md`.** Lines 1–100 (§0–§2) read; a heading grep showed the §3–§5 titles.
- **Corpus.**
  - Letter 254 read only at 501ea79. The later revision (commit 9c1953e) was not opened; only its subject line was seen, in the handoff text and in `git log`.
  - JH4 read in part, as disclosed in §0 and §4.
  - A directory listing of `tex/` showed other file names (e.g. `BCT_Letter36_D4Qubit.tex`); none opened.
- **Literature.**
  - Hsieh's two papers and scripts were supplied by the user mid-run.
  - Of HFT v22, only App. H, App. F.4 and the §9 paragraph were read.
  - The other literature was read as recorded in §6, at the depth stated there.
- **Independence of the positive control.** It was written and run before Hsieh's paper or code was opened.

---

## 12. §0.6 — reproduced verbatim

> This gate asks whether BCT's own written structure supplies the one route to quantum
> correlations that Gate PILOT did not test. It does **not** test quantum mechanics:
> E(θ) = −cos θ is already confirmed by loophole-free Bell experiments, so reproducing it is a
> consistency requirement, not a prediction. **A survivor does not vindicate BCT** — it shows BCT
> can host entanglement by the signed-measure route, and counts only if BCT supplies an
> ingredient the prior construction had to assume. **An import or a kill does not refute the rest
> of BCT** — it means entanglement must be added to BCT rather than explained by it, and Letter
> 254's physical claim stays withdrawn. A single number equal to cos 45°, or 2√2 at one setting,
> does not count: the whole curve is required.

---

## 13. What the gate did **not** establish

- **Quantum mechanics.** It does not test QM, and it does not show that entanglement *cannot* be explained within some extension of BCT. It shows only that the written corpus does not supply the signed-measure route.
- **Choice of field.** It does not decide between the S¹ and ℂ² definitions. That remains a corpus decision; the verdict does not depend on it.
- **Sources outside the card's list.** It did not read Volumes 1–2, Appendices E.2 and G, Letters 27 and 72, or any other source outside the card's list. A written stochastic rule or readout there would not have been seen. PILOT's searches of the volumes found no "Born", "Fock" or "wave functional" hits (premise, not re-run).
- **Hsieh's other results.** It does not assess Hsieh's Theorem 2 (spin–statistics), the Feynman–Kac lemma script, or HFT's other claims.
- **Multipartite correlations.** It does not test three-party (GHZ/Mermin) correlations in the signed-measure route.
- **Expressions of concern.** It does not establish the content of the RSOS expressions of concern.
- **Uniqueness of the square.** The CN-SINGLET-03 statement is for this construction (two outcomes, the doublet); it is not a general derivation of the Born rule.
