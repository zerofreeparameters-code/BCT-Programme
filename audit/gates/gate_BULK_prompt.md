# Gate BULK — pre-registration card

**Programme:** BCT Cold Ledger
**Card written:** 11 November 2026, Claude (Fable 5.1), at Michel's request ("lets gate it")
**Status:** PRE-REGISTERED, NOT RUN. No input ledger has been built and no Q4 number has been computed.
**Type:** a provenance audit with a measurement attached. Not a derivation of G.
**Depends on:** Gate MP (SC-MP-1 + SC-MP-3: m_P is an input wherever the corpus does physics; the lattice
spacing is set to ℓ_P by declared assumption), Gate RATIO (SC-RATIO-2: the geometry supplies one number,
ξ/a = 2.31754, and no absolute scale), Gate IG/BZ (closed: G_ind = (3/π)^(1/3) a² is an O(1) consistency
check at a = ℓ_P, not a prediction), Gate BUBBLE_BELLS (SC-BB-2, CONJECTURE: condensate confined to the
FCC void network, c_eff = c_s/√α_∞, α_∞ = 1.64 ± 0.03, implied m/m_P = 0.238), and the same-session desk
check of new_approach-6/7 (11 November 2026, Project doc `claude/desk_check_new_approach_6_7_2026-11-11.md`;
not a gate).

---

## 1. Background (stated, not a result of this card)

**The claim under test.** Two PDFs written on 11 November 2026 (new_approach-6, "Summary of New
Discoveries & Zero-Parameter Gravity Derivation", and new_approach-7, a journal edition built on it) assert
G = c⁴/(8πK_BCT) with the vacuum stiffness placed in the interstitial voids, a void fraction
f_BCT = 1/(8π) at the Bain point c/a = 1/√2, and status "Exact / Zero Param". The desk check found that
the G step as written is an identity (K := f·c⁴/G_true, so G_true is the input), that f ≠ 1/(8π) at
c/a = 1/√2 under every sphere-radius convention, and that c/a = 1/√2 is incompatible with the α₀ layer at
c/a = √2. The desk check is not a gate. What survives it is a hypothesis — *the vacuum stiffness lives in
the voids, and G follows from it* — and this card is the gate on that hypothesis with K computed from the
equation of state rather than read off G.

**What the corpus already prints.** At commit 9582c54 the corpus carries at least three distinct
identifications of K_BCT (or of ρ₀) with G, with three different coefficients:

- (a) **App AZ6 and Letter 20.** G = c⁴/(8πK_BCT), K_BCT = ρ₀c² (AZ6 lines 91–92); G = c²/(8πρ₀) with
  ρ₀ = m_P n₀ (AZ6 lines 373–374); Letter 20 states the equation of state P = c²ρ²/(2ρ₀) with
  ρ₀ = ρ_Planck = c⁵/(ħG²) (lines 138–141) and m = m_P (line 230). AZ6 line 397 then says the direct
  computation of ρ₀ from the equation of state "is self-referential".
- (b) **App E.3 §3.2** (Appendices Vol 1 Part 1, p. 71). Second-order action matching gives
  G = c²/(4πρ₀); "the BCT equation of state ρ₀ = 2K_BCT/c²" turns this into G = c⁴/(8πK_BCT) with
  **K_BCT = 8 M_FCC α₀/(9√2)**, "derived from the Madelung energy (Appendix D)". The same paragraph says
  the formula "cannot be numerically verified without first deriving the electron mass".
- (c) **App AI.4 and App AL** (Appendices Vol 1 Part 1, pp. 272–274). G = c⁴/(16πρ_BCT) with
  ρ_BCT = (π²/16)·ρ_Planck. App AL's own key result 1: "G CANNOT be derived numerically from BCT first
  principles alone. The structural formula G = c⁴/(16πρ_BCT) is dimensionally self-referential." Its part 2
  (G from the hierarchy residual, Prediction #100) takes the measured electron mass as input and is not an
  equation-of-state route.
- Letter 9 (Volume 1 Foundations summary, line 211): the derivation "reproduces G to the accuracy of the
  input Planck mass."
- Symbol collision, for the record: K_BCT also denotes the Koide quantity 0.970375 (Vol 1 Part 1, near
  line 12997 of the text extract). That K is not this K.

**Checked in the card thread (§7).** With K = ρ₀c² and ρ₀ = ρ_Planck as printed in (a),
c⁴/(8πK) = G·ℓ_P²/(8π) exactly: the printed chain has dimension m⁵ kg⁻¹ s⁻², not G's m³ kg⁻¹ s⁻²;
c⁴/G is a force (the Planck force, 1.210×10⁴⁴ N) while ρ₀c² is a pressure (4.633×10¹¹³ Pa), and their
ratio is ℓ_P². A length² must multiply K before the identification is dimensionally consistent, and the
length² that closes the identity is ℓ_P²/(8π). A "geometric factor 1/(8π)" found afterwards is that closure
read backwards.

**Prior gates that bound this card.** Gate MP, Gate RATIO and Gate IG/BZ as listed above. Gate QP:
the GP equation of state is not c_s = const. Gate WHY√2 / LH7: c/a = √2 is a structural choice (FCC over
BCC), selected not derived; the void constants at √2 are untouched. The gravity routes N, F/Fb, T, IG/BZ,
QP, AM, R2 and J are closed and **are not reopened by this card**: the validity of the fluid-action to
Einstein–Hilbert matching is not under test. Only the content of K is.

## 2. Question

1. **Provenance (Q1).** For every K_BCT (or ρ₀) the corpus prints as the quantity in G = c⁴/(8πK) —
   variants (a), (b), (c) above and any further one located in the run — build the input ledger of §4.2
   down to terminal inputs. For each variant state the SI dimension of the printed K and of c⁴/(8πG), and
   whether the printed identification is dimensionally consistent as written.
2. **G-free scale (Q2).** Does the corpus's equation of state fix an absolute SI value of K using only ħ,
   c and corpus-derived dimensionless numbers, with no forbidden input (§4.3)? Answered separately for:
   - (i) the GP quartic V = (g/2)(|Ψ|² − n₀)² with the Josephson condition g = mc²/n₀ (AZ6, Lemma
     "BCT satisfies Theorem JP", hypothesis (i));
   - (ii) the Bose–Hubbard reading, U = μ = t_kin = ħ²/(2mξ²) with n₀ = 1 per site (AZ7 Lemma "BCT
     on-site repulsion"; Letter 27 §I);
   - (iii) the Madelung bulk modulus K_BCT = 8 M_FCC α₀/(9√2) of App E.3 / App D;
   - (iv) the void-localised (Bubble Bells) variant: g = α_∞ mc²/n₀, condensate confined to the void
     network of porosity φ = 1 − π/(3√2) at c/a = √2, c_eff = c_s/√α_∞ (AZ6 audit note of 10 November;
     `audit/gates/BUBBLE_BELLS/`).
3. **G from K (Q3, conditional).** Only if Q2 is YES for at least one variant: compute G_BULK = c⁴/(8πK)
   for that variant by the rule of §5 and compare with CODATA 2022.
4. **Measurement, no verdict (Q4).** For every variant whose K is defined up to the lattice scale, report
   at 40 reported digits (60 working): the dimensionless stiffness number κ ≡ K a⁴/(ħc) with K as a
   pressure; the lattice spacing a†/ℓ_P at which c⁴/(8πKa²) = G_CODATA, i.e. the only dimensionally
   consistent completion that uses the lattice spacing as the hidden length; and, for variant (iv), the
   ratio f_K ≡ K_void/K_bulk under the §3 convention. Tabulate beside 1/(8π) = 0.039789, 1/√(8π) =
   0.199471, φ = 0.259520 and α_∞ = 1.64, with no verdict attached.

## 3. Choices made by the analyst, and what they cost

- **c/a = √2 throughout.** The corpus's value (FCC). The Bain point c/a = 1/√2 of new_approach-6/7 is not
  run: the desk check already found its number false and the ratio incompatible with α₀. Cost: the specific
  number in those PDFs is not re-tested here, by design; the hypothesis is tested, not the number.
- **K is the thermodynamic bulk modulus** of the stated equation of state, K ≡ ρ ∂P/∂ρ at the ground state
  (equivalently ρ₀c_s²). For the GP quartic, P = gn²/2 and K = g n₀² exactly. For the γ = 2 polytrope of
  Letter 20, K = ρ₀c². No other definition is used.
- **Void-localised convention for (iv).** Rigid-sphere superleak, equivalent-fluid rule, as in Gate
  BUBBLE_BELLS: the condensate occupies the volume fraction φ, c_eff = c_s/√α_∞, and the effective modulus
  per unit total volume is K_eff ≡ ρ_eff c_eff² with ρ_eff = φρ₀. This is a choice. Cost: other
  homogenisation conventions exist (per unit fluid volume, Biot/JKD equivalent-fluid with K_f/φ); the run
  reports under this one and may list the others' values in the Q4 table with no verdict.
- **Sphere radius at √2:** half the nearest-neighbour distance (touching spheres), so the void fraction is
  the exact 1 − π/(3√2).
- **Reference value:** CODATA 2022, G = 6.67430(15)×10⁻¹¹ m³ kg⁻¹ s⁻² (relative uncertainty 2.2×10⁻⁵).
- **Out of scope by choice:** the hierarchy-formula route (App AL part 2, AZ6 "Prediction #100"), which
  takes m_e as input and was scored by Gates PRED/STAT; and any route that adds a field, a coupling or a
  scale not in the pinned sources (§4.6). If a K-variant's chain passes through the hierarchy formula, the
  ledger records it and flags it; it is not followed.

## 4. Fixed rules

**4.1 Sources, pinned.** Repository zerofreeparameters-code/BCT-Programme at commit
`9582c54b6f22fc78eee0dc356f6d49cdfadd68b3`. Files and SHA-256 (verify before reading):

| File | SHA-256 |
|---|---|
| `tex/BCT_Appendix_AZ6.tex` | 7495750530f385e74d0d9ef00286939cc7244f468f49d941c039005e004677e7 |
| `tex/BCT_Letter20_GR_AllOrders.tex` | 4e2a625c64eec455fddcd0706d5b9868cbbc33092f1992b55b95ee0fb34d7ed5 |
| `tex/BCT_Appendix_AZ7.tex` | ef27d5dea9c5104791919b24431859d2965a0c98e7f4b6b6f079e51b25280476 |
| `tex/BCT_Letter27_GPAxiom.tex` | d15dbf6c6949a3a2f51e187525c4e49193478de845967f1cb77247d2aa81270e |
| `BCT_Volume1_Foundations.tex` | 5787bd00ced79bffadd82369ce60e11985facee64144e1da469ec1979fe5dde3 |
| `BCT_Appendices_Volume1_2026_compressed_Part1.pdf` (11,428,679 B) | 6e14b6c0183d089c8b1f56701878addef43f9b21d4533ddf5dccf464a00dbb8b |
| `audit/gates/BUBBLE_BELLS/` (directory, as committed) | — |

Appendices Vol 1 Part 1 is a real PDF at this commit; extract with `pdftotext -layout`. App E.3 §3.2 is
on p. 71 of that volume, App AI.4 and App AL on pp. 272–274. **App D** (the Madelung-energy derivation
cited by E.3) is to be located in the run, in the pinned sources only; if it is not there, the ledger
records variant (iii) as ABSENT (as-of-date) and does not reconstruct it. The new_approach-6/7 PDFs are not
sources; their claim is quoted in §1 and nothing is taken from them.

**4.2 Input ledger.** One table per variant, columns: Symbol | Value | SI dimension | Source (file@commit
and line, or volume and page) | Terminal inputs | G-bearing (Y/N) | Notes. A terminal input is ħ, c, k_B,
a measured constant with its CODATA value, or a corpus-declared assumption quoted verbatim. A quantity is
G-bearing if any terminal input in its chain is G, m_P, ℓ_P, t_P, E_P, ρ_P, the Planck force c⁴/G, or any
quantity the corpus defines by "= Planck …" or "at the Planck scale".

**4.3 Forbidden as inputs to a G-free K:** everything in the G-bearing list of §4.2. **Permitted:** ħ, c;
dimensionless corpus numbers (c/a = √2, π/(3√2), r_oct, r_tet, α₀ = r_oct r_tet/π, ξ/a = 2.31754,
α_∞ = 1.64 ± 0.03, M_FCC and other Madelung constants with their definitions quoted); the equation-of-state
forms as printed. Any absolute scale — a, m, n₀, ξ in metres, g in SI — counts as G-free only if its own
ledger line shows no forbidden terminal input.

**4.4 The condensate particle mass.** The corpus prints m = m_P (Letter 20 line 230) and Gate BUBBLE_BELLS
implies m = 0.238 m_P. Both are G-bearing. If a variant needs m, the ledger says which value is used and
flags it; no third value is introduced.

**4.5 Arithmetic.** mpmath, 60 digits working, 40 reported. Scripts saved under `audit/gates/BULK/`
and named in the result. Every Q4 number traces to ledger lines.

**4.6 No construction.** The run audits the corpus plus variant (iv). No new field, coupling, scale,
boundary condition or convention may be added to make a K G-free. If the analyst sees a way to do it, that
is a sentence in the result and a card for another day.

## 5. The rule that connects K to G (fixed here, before the run)

    G_BULK ≡ c⁴ / (8π K),   K in SI,   Δ ≡ G_BULK / G_CODATA − 1.

The coefficient is 8π, taken from the claim under test and from (a) and (b); the 4π of E.3's
intermediate step and the 16π of (c) are recorded in the ledger as corpus inconsistencies, not used.
If the K of a variant is a pressure, G_BULK as defined has dimension m⁵ kg⁻¹ s⁻² and is not G: the rule
then returns DIMENSIONALLY INCONSISTENT for that variant, Q3 is not evaluated for it, and the a²-completion
of Q4 is reported instead, with no verdict. The hypercubic/lattice-spacing completion c⁴/(8πKa²) is a
measurement only; no verdict code is attached to its value.

## 6. Verdict codes

- **SC-BULK-0 (unposable).** No K_BCT with a stated equation of state can be located in the pinned sources.
  (§1 lists three; this code is not expected.)
- **SC-BULK-1 (inherits MP / RATIO).** Every variant of K needs a G-bearing input to acquire an SI value,
  or is dimensionally inconsistent as printed. G = c⁴/(8πK) is then an identity in G. The
  stiffness-in-the-voids hypothesis yields no G without G; App AL's own conclusion stands; the
  "Exact / Zero Param" status of new_approach-6/7 is withdrawn.
- **SC-BULK-2 (G-free, number wrong).** At least one variant fixes K in SI with no forbidden input, and
  |Δ| > 1% for every such variant. Report Δ. This falsifies the number, not the structure, and is itself a
  finding against Gate RATIO that must be reconciled in a separate card.
- **SC-BULK-3 (G-free, number right).** At least one variant fixes K in SI with no forbidden input and
  |Δ| ≤ 1%. This would contradict Gate RATIO (SC-RATIO-2) and Gate MP; the result stays CONJECTURE and
  opens a reconciliation gate. It is not a derivation of G until that gate closes.
- **SC-BULK-4 (inconclusive).** A located variant's chain cannot be traced to terminal inputs within the
  pinned sources (not merely ABSENT: present but untraceable). Report which, and why.

Q1 ledgers and Q4 numbers are reported whatever the code.

## 7. Validation already done (why the card is not blind to the dimensional point)

In the card-writing thread, 11 November 2026, `bulk_dimcheck.py` (SHA-256
41fbc4ef284dee15a23610e9b5e2fd27e6ecf000381f27b354717cf3377b4674, 1755 B; committed alongside this
card under `audit/gates/BULK/`), mpmath at 60 digits, CODATA 2022:

- c⁴/G = 1.21025556434×10⁴⁴ N; ρ_P c² = 4.6329467879×10¹¹³ Pa; ratio = 2.61228030397×10⁻⁷⁰ m² = ℓ_P².
- c⁴/(8π ρ_P c²) = 6.93722275424×10⁻⁸² m⁵ kg⁻¹ s⁻² = G·ℓ_P²/(8π), ratio 1.0 to 40 digits.
- Closing length L/ℓ_P = 1/√(8π) = 0.19947114020071633897; 1/(8π) = 0.03978873577297383394.
- FCC packing π/(3√2) = 0.74048048969306104117; void fraction 0.25951951030693895883.
  App AI/AL's "ρ_D4 = π²/16" = 0.61685027506808491368 differs from the FCC packing fraction; the run
  records which density (c) means and does not reconcile them.
- App AI.4 as printed, c⁴/(16π ρ_P) = 3.117×10⁻⁶⁵ in SI, has the dimension of time (App AL says so itself).

No ledger was built, no variant was traced, and no Q4 number (κ, a†, f_K) was computed.

## 8. No-fit clause

- No equation of state, convention, coefficient, sphere-radius rule, reference value or tolerance may be
  changed after the run starts.
- No result may be described as deriving G. SC-BULK-3 would mean one variant is G-free to 1%; it would then
  have to survive a reconciliation with Gate RATIO in a separate gate before any tier above CONJECTURE.
- If κ, f_K or a†/ℓ_P lands near a simple number — 1/(8π), 1/√(8π), φ, 1/α_∞, a ratio of small integers,
  a power of π — that is not a finding. It goes in the Q4 table and the run moves on.
- The closed gravity routes are not reopened. The run does not assess whether S_SF → S_EH holds; a sentence
  noting that the matching is already closed (Gates T, IG/BZ, QP, AM, J) is the most it may say.
- Variant (iv) rests on CONJECTURE-tier input (Gate BUBBLE_BELLS); a result built on it inherits that tier.
- The run computes the K's that exist. It does not search for a formula that produces G.
- Same-session results are capped at CONJECTURE.

## 9. Analyst's disclosure

- **Forecast: SC-BULK-1 for all four variants, about 90%.** (a) and (c) set ρ₀ = ρ_Planck and m = m_P in
  their own text. (ii) sets n₀ = 1 per site, which needs a, and U = ħ²/(2mξ²), which needs m; the corpus
  has no G-free value for either (Gate MP, Gate RATIO). (iii) is a pure number and needs a unit; the only
  unit-bearing scale in the corpus is a = ℓ_P by declared assumption, and E.3's own text defers the
  evaluation to m_e/m_P, which is the hierarchy route scoped out in §3. (iv) multiplies (a) by factors
  built from φ and α_∞, which are dimensionless and cannot remove G.
- The residual 10% is that App D, when located, supplies a Madelung energy with an absolute unit the
  analyst has not seen — a Coulomb energy per site in terms of e and ε₀, say. Even then a lattice spacing
  is needed, and the analyst expects it to be ℓ_P.
- **Q4 guesses, recorded so they can be scored.** Variant (a) as printed: κ = 1 identically at a = ℓ_P
  (ρ_P c² ℓ_P⁴ = ħc), so a†/ℓ_P = 1/√(8π) ≈ 0.1995. Variant (iv) under the §3 rule: f_K = φ ≈ 0.2595, so
  a†/ℓ_P = 1/√(8π φ) ≈ 0.3916. Variant (iii): no guess for κ (M_FCC's definition unknown to the analyst);
  the number is of order α₀ ≈ 0.0931 times a Madelung constant of order 1. These are forecasts, not
  reference answers, and the run must not steer toward them.
- The analyst notes that App AL already states the forecast's conclusion for variant (c). The value of
  running the gate is (i) deciding the void-localised variant, which App AL did not consider, (ii) the Q4
  table, which replaces "f = 1/(8π)" with what the corpus's own equation of state gives, and (iii) a ledger
  entry that settles new_approach-6/7 by a fresh-thread run rather than by a desk check.
- The analyst wrote the line being gated ("it just needs K computed from the equation of state rather than
  read off G") and has an interest in it being a real question. The forecast says it is a real question with
  a known answer.

## 10. Known limitations (stated in advance)

- Provenance is audited; the action-matching step is not (closed elsewhere). A G-free K would not by
  itself make G = c⁴/(8πK) true.
- The homogenisation convention for variant (iv) is a choice (§3); the Q4 table may list alternatives.
- "ABSENT" for App D is as-of-date at the pinned commit (ledger-drift lesson of 19 September 2026).
- The sphere-radius convention at √2 is touching spheres; App AI/AL's π²/16 is recorded, not reconciled.
- The reference G has relative uncertainty 2.2×10⁻⁵; the 1% band of §6 is the programme's LO tolerance,
  not CODATA's.

## 11. Run protocol

- Fresh thread inside the BCT Project. Before opening it, switch off "Search and reference past chats" and
  "Generate memory from chats" in Settings; switch them back on after the run. One gate per thread.
- Fetch this card by commit-pinned raw URL with curl to disk; `shasum -a 256` (or `sha256sum`) it there and
  compare with `audit/gates/PREREG_20261111_BULK.sha256` **before reading it**. Record the digest and the
  commit.
- `git clone --depth 1` the repository, `git checkout 9582c54b6f22fc78eee0dc356f6d49cdfadd68b3` (or fetch
  each §4.1 file by raw URL at that commit), and verify every §4.1 hash before reading any source.
- Build the Q1 ledgers first, Q2 per variant second, Q3 only if opened, Q4 last.
- Deliverable: `audit/gates/BULK/gate_BULK_RESULT.md` with the Q1 ledgers, the Q2 answers per variant, Q3 if
  reached, the Q4 table, the verdict code, the §9 disclosure scored item by item, correction notices
  CN-BULK-nn, and a plain-language summary; the scripts; and a copy of the as-run prompt. The session cannot
  push, so the deliverable comes back as a `git format-patch` bundle for Michel to apply.
- Same-session results are capped at CONJECTURE.
