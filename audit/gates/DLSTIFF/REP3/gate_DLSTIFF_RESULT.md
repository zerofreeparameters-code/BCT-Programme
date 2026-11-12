# GATE DL-STIFF — RESULT (blind replication REP3)

**Is the plaquette coupling β of the added link field fixed by the medium plus the void geometry, or
is it a free input of the DL theory?**

- **Model executing this run:** Claude Opus 5.5 (`claude-opus-5-5`).
- **Run:** 12 November 2026, 19:04–19:30 AEDT, one gate, one thread. Blind replication REP3: the
  results of the two earlier runs were not given, not sought and not compared.
- **Card digest (SHA-256 of the file curled to disk before reading):**
  `294da0f50c5d740956bb0b3d64871f580a00f454a0f541701467bba47ee48e21` — **matches**
  `audit/gates/PREREG_20261112_DLSTIFF.sha256` and the run prompt.
- **Record digest:** `682effc99bc12bfee62de437080ccc9054d9ea0e84ecd4de1d62da3fc9dcb696` — matches.
- **Validation script digest:** `dls_deskcheck.py` `332e2d1275196c5720d78fcce6e0364d567c3281476d4795c032010e5989bde5` — matches.
- **Sources:** single shallow commit `9993a2381cdbdd8604975f285644aabb94063325` (tree
  `3b7c44a0a095b32701be66fe81838ffb6f3f44fd`; `git log --oneline | wc -l` = 1). Card §4.1 pins its
  sources by hash at `9114b6e`; every hash verified at `9993a23` before reading (table in §A).
- **Toolchain:** Python 3.13.18, sympy 1.14.0, mpmath 1.3.0 (30 dps working, 10 reported), numpy 2.5.3.
  Every Python run used `python3 -I`.

---

## VERDICT (first)

**SC-DLS-2 — β is a free input of the DL theory.** Tier: **CONJECTURE** (same-session cap).

Every route on the card's fixed list (R1–R5) and every route found in the pinned sources for the
open slot (R6a–R6d) is closed by its pre-registered kill test. No route survives, so Q2 has no
derivation and Q3 has no surviving β.

The single structural fact that closes R2, R3, R4 and R6c together: **in option B the pinned action
is `S_GP[Ψ] + S_W[a]` with no term containing both Ψ and a_e** (the superfluid is neutral — that is
what keeps the photon massless). So the partition function factorises, `Z = Z_GP(J, ξ, Ψ₀)·Z_W(β)`,
and nothing about the medium — its stiffness J, its dipole response, its sphere-surface potential
σ_s — can enter the link field's coupling. The one way to put a term between them, a charge q
(R1), gives the photon the Meissner mass the construction exists to avoid.

**What the run found that the card did not anticipate** (none of it changes the verdict):

1. The target number **2ξ²/a² = 10.74201848 is in the pinned sources already** — as Gate ICE's
   Josephson-to-charging ratio `E_J/E_C = 2 n̄² (ξ/a)²` evaluated at occupation n̄ = 1 (equal to 30
   digits). It is a ratio *inside the superfluid's own sector*, needs n̄ = 1 (ICE: n̄ is not fixed by
   geometry) and one O(1) convention (with `E_C = U/2` it is 21.48), and nothing carries it to a_e.
   This is the sharpest form of R3 and it still fails at the transfer (CN-DLS-05).
2. The **only exact map from a phase stiffness K to a gauge coupling** — particle–vortex duality —
   gives `β_dual = 1/(4π²K)`, *inverse* to the stiffness, and in 3+1D the dual is a 2-form with one
   polarisation, i.e. the phonon re-expressed (PROMOTE CN-PROMOTE-10). R3's `β ∝ K` runs the other
   way and has no derivation (CN-DLS-10).
3. App J's `σ_s = α₀` needs, besides Q = 1 and d = √(r_tet r_oct), a **third** input: the
   Heaviside–Lorentz choice ε₀ = 1. In Gaussian units the same Q and d give σ_s = 4πα₀ (CN-DLS-06).

---

## A. Sources (card §4.1), verified before reading

| File | SHA-256 | Check |
|---|---|---|
| `audit/MINIMAL_BCT.md` | `952ad477…3c77b` | OK |
| `audit/gates/DL/gate_DL_RESULT.md` | `3eff7862…128b4` | OK |
| `audit/gates/DL/gate_DL_step0_network.py` | `7935f7e7…4a4ee` | OK |
| `audit/gates/DL/gate_DL_step1_mass.py` | `6e082574…c93d` | OK |
| `audit/gates/STIFF/STIFF_RESULT.md` | `1d0be869…ee672` | OK |
| `audit/gates/ICE/gate_ICE_RESULT.md` | `b458a3c1…d11bc` | OK |
| `audit/gates/PROMOTE/gate_PROMOTE_result.md` | `761c3bdf…40dca2` | OK |
| `audit/gates/TANH/gate_TANH_RESULT.md` | `090ede61…858eb` | OK |
| `tex/BCT_Appendix_J_SphereAction.tex` | `ad9ecd0c…432df` | OK |
| `audit/scoping/DL_scoping_2026-11-12.md` (hash from the record) | `fede02d1…f8a65` | OK |
| `audit/gates/DLSTIFF/dls_deskcheck.py` | `332e2d12…9bde5` | OK |

Full 64-hex digests as in card §4.1 and the record; checked with `sha256sum -c` (all eleven `OK`).
`audit/gates/DLSTIFF/` contained only `dls_deskcheck.py` at this commit — no other file to report.

**Re-runs of pinned scripts** (outputs saved here): `dls_deskcheck.py` reproduces every card-§7
number (10.74201848; 10.90497833; ratios 10.62, 17.47, 8.73) →
`dls_deskcheck_rerun_output.txt`. `gate_DL_step0_network.py` reproduces V = 3, E = 8, b₁ = 5 per
primitive cell, oct/tet degree 8/4, S = I/3 exactly at L = 2, 3, 4 → `dl_step0_network_rerun_output.txt`.
`gate_DL_step1_mass.py` reproduces m_A² = q²φ₀² (charged) and 0 (neutral) →
`dl_step1_mass_rerun_output.txt`.

---

## Q1. ROUTE LEDGER

All numbers from `rep3_routes.py` (→ `rep3_routes_output.txt`) and `rep3_r2_gp_throat.py`
(→ `rep3_r2_gp_throat_output.txt`). Line numbers refer to the pinned files.

| Route | Statement (with source line) | Inputs (named, tiered) | Kill test (card §6) | Result | β if survives |
|---|---|---|---|---|---|
| **R1** minimal coupling | Condensate charged under a_e, ∂θ → ∂θ − q a (card §2 R1; DL RESULT ll.101–105, 118; `gate_DL_step1_mass.py` ll.9–18) | q ≠ 0 (ASSERTED — contradicts option B's neutrality); J, ρ₀ (§1.2) | m_A² ≠ 0 for q ≠ 0. **Computed:** continuum `J|(∂−iqA)Ψ|² = Jρ₀(A q − ∂θ)²`, unitary-gauge A² coefficient `Jρ₀q²`, `m_A² = 2e²Jρ₀q²`; lattice link `2JΨ₀²(1−cos(Δθ−qa))` → `∂²/∂a² = 2JΨ₀²q²`. Also: tree-level coefficient of (∂A)² is **0** — minimal coupling gives a mass, never a β | **Closed** (contradicts the construction; would not fix β even if allowed) | — |
| **R2** induced Maxwell from dipole response | Neutral medium couples via P·E; integrating out gives −χ/2 on E² (card §2 R2; DL RESULT l.120; STIFF ll.53–56, CN-STIFF-01 ll.228–230) | χ = dP/dE from the pinned action (§1.2) | χ = 0 if no polarisable charge. **Computed:** option-B medium Lagrangian has free symbols {J, Ψ₀, ξ, ψ_r, ψ_i, ∂ψ_r, ∂ψ_i} — no a_e — so P = ∂L/∂E = 0, χ = ∂²L/∂E² = 0. Independent second zero (STIFF re-derived): symmetric-window GP ground state has number dipole p = −1.4×10⁻¹⁶, evenness residual 2.2×10⁻¹⁶; a nonzero p appears only under an imposed odd *number* bias b, linearly (p/b = −0.23861015 for b = 1–8×10⁻⁴), which in option B is a chemical-potential step, not E of a_e. Even a charged medium gives χ = 0 at tree level (a nonzero χ needs charged loops = R5) | **Closed** (χ ≡ 0 from every pinned term) | — |
| **R3** β := phase stiffness | Josephson-array identification (card §2 R3; scoping §4 ll.65–84). Sharpest pinned form: ICE ll.115–125, `E_J/E_C = 2n̄²(ξ/a)²` | J (§1.2 — **no value in §1.3**); n̄ = 1 (ASSERTED; ICE ll.158–160 and CN-ICE-08: not geometry-fixed); E_J = 2tn̄, E_C = U (convention); the identification β ≡ E_J/E_C (ASSERTED) | Is there any term coupling a_e to Ψ? **Computed:** all mixed derivatives ∂²S/∂ψ∂Φ_p = 0; Z factorises; every a_e observable is J-independent. JJ-array analogue: plaquette energy Φ²/(2L_loop), ∂/∂E_J = 0. Steelman value: E_J/E_C at n̄ = 1 = **10.74201848 = β_geom** (residual 0 at 30 digits); 21.48403697 with E_C = U/2; 5.371009241 with E_J = tn̄; 42.96807393 at n̄ = 2 | **Closed** (assertion: no term through which a_e inherits J) | — |
| **R4** α₀ as surface/boundary coupling | App J ll.147–173: σ_s = ΔV·d ≈ Qd²/(4πR²) = α₀ (J/J₀) at Q = 1, d = √(r_tet r_oct); ll.238–255: g = σ_s 4πR²|Ψ(R)|²/(J R Ψ₀²) | Q = 1 (ASSERTED; App J ll.172–173, 385–386 say so; STIFF: the neutral medium has no electric charge); d = √(r_tet r_oct) (ASSERTED); ε₀ = 1 (ASSERTED, unit convention); R = a/2; J = 1 (units) | σ_s = α₀ needs asserted Q, d; g_computed ≠ α₀; and sphere-surface → window-link transfer. **Computed:** σ_s = Qd²/(4πε₀R²); σ_s/α₀ = Qd²/(r_oct r_tet) — **any** (Q, d) with Qd² = r_tet r_oct works (Q = 1, ½, 2, 3 all give 0.007408055728); Gaussian units give 4πα₀ = 0.0930923738. g = **0.0003697506484**, α₀/g = 20.03527447. σ_s multiplies |Ψ|² on sphere surfaces (App J l.111); ∂/∂Φ_p of it = 0. Reaching β would need β := 1/(4πσ_s), a new identification (§4.5) | **Closed** (three asserted inputs, and no term moves σ_s to a_e) | — |
| **R5** induced Maxwell from charged loops | β = c Σq² ln(Λ/m) (card §2 R5) | charged matter (ABSENT: MINIMAL_BCT §1.1 ll.36–43 one neutral scalar; §1.5 vortices of that field; scoping ll.103–104); Λ/m (free); species count (free) | Needs charged matter; coefficient is a log. **Computed:** corpus β_ind = 0. Cutoff ratio for 10.742: card coefficient 1/(12π²): ln(Λ/m) = 1272.233675 (Λ/m ≈ 10^552.5); Dirac 1/(6π²): 636.1168374 (10^276.3); complex scalar 1/(24π²): 2544.467349 (10^1105.0). Illustration over ln(m_P/m_e) = 51.52783097 (App J l.321): one unit-charge Dirac species gives β = 0.8701434707 (< β_c hypercubic); 12.345 Dirac species (24.69 at card coefficient) needed — non-integer, i.e. tuning | **Closed** | — |
| **R6a** particle–vortex duality | Dual of a 3+1D superfluid is a Kalb–Ramond 2-form (PROMOTE l.20; CN-PROMOTE-06, -10 l.33) | K = phase stiffness ∝ JΨ₀² (Ψ₀ / n̄ not in §1.3) | Same four conditions. **Computed:** Villain/Poisson: S_dual = Σ(curl m)²/(2K) → β_dual = 1/(4π²K), dβ/dK < 0; at K = 10.742, 0.002358057375. Polarisations C(D−2, p) in D = 4: 1-form 2, 2-form 1. It is the phonon re-expressed (CN-PROMOTE-10 FALSIFIED "superfluid dual = photon"), not the added a_e | **Closed** (wrong object; inverse scaling) | — |
| **R6b** topological quantisation | Circulation quantised in units of 2π, integer charge, no parameter (MINIMAL_BCT ll.75–77) | n (integer) | **Computed:** e·g_m = 2πn → e = 2π/g_m: fixes a product, not e. Circulation of the neutral field is flux of a_e only with a charge q (R1) | **Closed** | — |
| **R6c** App E.1 §3.3 J = 1/(4πα₀) | Reported in scoping §4 ll.76–77 as a monopole-action parameter; App E.1 itself **unpinned, not read** | J := 1/(4πα₀) (ASSERTED as reported) | Whatever J is, R3's kill test fails at the J → a_e transfer (mixed derivatives 0), so the value of J cannot change the ledger | **Closed via R3** (no SC-DLS-5: evaluable without the unpinned file) | — |
| **R6d** void-network geometry | DL RESULT ll.64–87; step 0 re-run: V = 3, E = 8, b₁ = 5 per primitive cell, S = I/3 | network theorems (PROVEN) | These dimensionless numbers enter the β ↔ 1/e² continuum-matching factor on the graph (DL-BETA's job), not β; compact U(1) on any graph is a one-parameter family in β | **Closed** (no term, no coefficient) | — |

**Ledger result: 9 routes, 9 closed, 0 surviving.**

## Q2. SURVIVING ROUTE(S)

None. No derivation to report; no β to 10 digits.

## Q3. COMPARISON

No surviving β. For orientation only, the hypothetical and closed-route values against β_c
(card §1 conventions; void network: **DL-BETA pending**):

| Value | β | /β_c Z4 1.0111 | /β_c D4 0.6150 (card) | /β_c D4 1.2300 (K–N) | void network |
|---|---|---|---|---|---|
| β_geom = 2ξ²/a² (would be SC-DLS-1) | 10.74201848 | 10.62409107 | 17.46669672 | 8.73334836 | DL-BETA pending |
| 1/(4πα_CODATA) (a fit, for scale) | 10.90497833 | 10.78526192 | 17.73167207 | 8.865836037 | DL-BETA pending |
| R3 steelman E_J/E_C, n̄ = 1, E_C = U (closed) | 10.74201848 | 10.62409107 | 17.46669672 | 8.73334836 | DL-BETA pending |
| R3 steelman E_J/E_C, n̄ = 1, E_C = U/2 (closed) | 21.48403697 | 21.24818214 | 34.93339344 | 17.46669672 | DL-BETA pending |
| R5 one Dirac species over m_P/m_e (closed) | 0.8701434707 | 0.8605909116 | 1.414867432 | 0.707433716 | DL-BETA pending |
| R6a dual coupling at K = β_geom (closed; a 2-form) | 0.002358057375 | 0.002332170285 | 0.003834239635 | 0.001917119817 | DL-BETA pending |

Neither SC-DLS-1 (a surviving β equal to 2ξ²/a²) nor SC-DLS-3 (a surviving β of another value)
applies.

## Q4. EQUIVALENCE STATEMENT (recorded, not scored)

Under the card's §4.4 conventions (Wilson S = βΣ(1 − cos Φ_p), β = 1/e², e² = 4πα, a = 1),
**SC-DLS-1 is the statement α = α₀ for the added link field**: β = 2ξ²/a² ⇔ 1/(4πα) = 1/(4πα₀).
(Caveat CN-DLS-12: on the void network the β ↔ 1/e² continuum matching carries a graph factor not
computed here, so the equivalence holds under §4.4's convention, not as a lattice-independent
fact.) A surviving derivation would have had to be reconciled with:

- **FWD** — per the card (§1), α₀ → α is a selected correction map; a derivation of α = α₀ for a_e
  would still owe the 1.5 % gap to CODATA without that map.
- **STAT** — per the card, the same correction map was closed as a selected fit; a new derivation
  could not borrow it.
- **QED** (chat-side, not in the tree) — per the scoping note (ll.76–77), CN-QED-04 found App E.1
  §3.3's arithmetic around J = 1/(4πα₀) inconsistent; any derivation landing on 10.74 would have to
  say how it differs from that section.
- **BC** (chat-side) — σ_s = α₀ in App J is a two-input fit; re-derived here (CN-DLS-06), with a
  third input (ε₀ = 1) found.
- **TANH** — App J's computed Josephson coupling is g = 0.00036975 = α₀/20.035, not α₀; re-derived
  here (CN-DLS-07); a derivation through App J would have to say which of the two objects it uses.

## Q5. COST COUNT (TWIST cost-table form, as given in the card and scoping note §3)

| Input of the DL theory (option B) | Count | Basis |
|---|---|---|
| The added compact U(1) link field a_e | 1 | Construction; the written medium cannot supply it (STIFF, ICE, PROMOTE) |
| β | **1** | This gate: SC-DLS-2 |
| The charge carrier | 1 | Gate DL-MATTER (open); the only BCT matter, vortex strings, is neutral under a_e |
| The α identification | 1 | That a_e is electromagnetism with coupling α_phys. With β free it is made by choosing β = 1/(4πα_phys) = 10.90497833. It would be 0 only if a derivation delivered the measured α; even SC-DLS-1 would have delivered α₀ = 1/134.988 and still needed FWD/STAT's map |
| **Total** | **4** | (3 if one counts "β fitted to α_CODATA" as a single act rather than two rows) |

---

## §9 DISCLOSURE, SCORED ITEM BY ITEM

Outcome: **SC-DLS-2**.

| Forecast item | Probability | Outcome | Brier term |
|---|---|---|---|
| SC-DLS-2 | 70 % | **occurred** | (1 − 0.70)² = 0.0900 |
| SC-DLS-4 | 15 % | did not | 0.0225 |
| SC-DLS-3 | 10 % | did not | 0.0100 |
| SC-DLS-1 | 5 % | did not | 0.0025 |
| (SC-DLS-0, -5) | 0 % | did not | 0 |

Brier score 0.125 (0 is perfect, 2 is worst); log score ln 0.70 = −0.357 nats (−0.515 bits).

Reasons, one by one:

- *"R1 contradicts the construction"* — **confirmed** (CN-DLS-02); additionally R1 would not fix β
  even if allowed (tree-level minimal coupling has no (∂A)² term).
- *"R2 needs a polarisable charge STIFF says is absent"* — **confirmed, and stronger**: in option B
  no term of the action contains a_e, so χ = 0 before STIFF's symmetry argument is needed; STIFF's
  zero independently re-derived (CN-DLS-03, -04).
- *"R3 is the Josephson-array analogy and the analogue's loop coupling is independent of E_J"* —
  **confirmed**. Not anticipated: the target number is literally present in the pinned sources as
  ICE's E_J/E_C at n̄ = 1, which makes R3 look closer than the disclosure suggests; it still fails at
  the transfer (CN-DLS-05), and duality points the other way (CN-DLS-10).
- *"R4 is BC's fit and a sphere-surface quantity, not a window-link one"* — **confirmed**; a third
  asserted input (ε₀ = 1) found (CN-DLS-06, -08).
- *"R5 needs matter the corpus lacks"* — **confirmed**; cutoff ratios computed (CN-DLS-09).
- *"The 5 % on SC-DLS-1 is the R6 slot"* — four R6 candidates found in the pinned sources; none
  survives.
- *Interest disclosure* — noted. This replication saw the analyst's views only through the card and
  the scoping note (both pinned); the run's reasoning did not depend on them beyond the kill tests
  the card fixes.

---

## CN-DLS NOTICES (numbered within REP3)

Content tiers below; the gate verdict as a whole carries the same-session cap (CONJECTURE).

- **CN-DLS-01 [PROVEN — arithmetic].** 1/(4πα₀) = 1/(4 r_oct r_tet) = 2ξ²/a² = 10.74201848 (30-digit
  residuals 0; exact in sympy). The two written forms of r_tet, (√6 − 2)/4 and (√(3/2) − 1)/2, are
  identical. Card-§7 ratios reproduced.
- **CN-DLS-02 [PROVEN — symbolic].** R1: charged condensate gives m_A² = 2e²Jρ₀q² (continuum) and a
  lattice link curvature 2JΨ₀²q²; zero at q = 0. Minimal coupling contributes no (∂A)² term at tree
  level, so R1 cannot fix β even outside option B.
- **CN-DLS-03 [PROVEN — inspection/symbolic].** R2: the option-B medium action contains no a_e;
  P ≡ 0, χ ≡ 0; the card-§7 coefficient −χ/2 is therefore 0.
- **CN-DLS-04 [PROVEN — numeric; re-derives CN-STIFF-01/03 with an independent solver].**
  Symmetric-window GP: number dipole −1.4×10⁻¹⁶ (a symmetric depletion, monopole −0.9544406131); an
  odd number bias gives p/b = −0.23861015, constant over b = 1–8×10⁻⁴. The medium responds to a
  number bias, not to E of a_e. (Window shape V₀ = 1, w = 0.5a is a modelling choice; the zero holds
  for every even V.)
- **CN-DLS-05 [PROVEN — symbolic; the identification ASSERTED].** ICE's map gives E_J/E_C = 2n̄²ξ²/a²
  exactly; at n̄ = 1 it equals β_geom to 30 digits; with E_C = U/2 it is 21.48403697, with E_J = tn̄
  5.371009241. MINIMAL_BCT §1.3 gives no value for J. The option-B action has zero mixed
  derivatives between Ψ and Φ_p, so a_e cannot inherit E_J, E_C or J. R3 closed.
- **CN-DLS-06 [PROVEN — symbolic].** R4: σ_s = Qd²/(4πε₀R²); σ_s = α₀ ⇔ Qd² = r_tet r_oct, a
  one-parameter family in which R drops out; App J's choice also needs ε₀ = 1 (Gaussian: 4πα₀ =
  0.0930923738). Confirms BC's two-input finding and adds a third input.
- **CN-DLS-07 [PROVEN — arithmetic].** App J §3.1: g = α₀·4πR·tanh²(r_oct/ξ) = 0.0003697506484;
  α₀/g = 20.03527447; discarded factor 0.04991196908. TANH reproduced.
- **CN-DLS-08 [PROVEN — inspection].** σ_s multiplies |Ψ|² on sphere surfaces (App J l.111, l.238);
  no pinned term places it on window loops. β := 1/(4πσ_s) would be a new identification, which
  card §4.5 forbids.
- **CN-DLS-09 [PROVEN — arithmetic, standard one-loop coefficients].** R5 needs ln(Λ/m) = 1272.2
  (card coefficient), 636.1 (Dirac), 2544.5 (complex scalar) for β = 10.742; one Dirac species over
  App J's m_P/m_e gives β = 0.870; 12.35 species would be needed. The corpus has no charged matter.
- **CN-DLS-10 [PROVEN — standard duality, re-derived].** The exact stiffness → gauge-coupling map is
  particle–vortex duality, β_dual = 1/(4π²K), inverse to K; in 3+1D its object is a 2-form with one
  polarisation (PROMOTE CN-PROMOTE-06/10). R3's β ∝ K has no derivation; the one derived map gives
  β ∝ 1/K, and 0.002358 at K = 10.742.
- **CN-DLS-11 [reading of the card, recorded].** §5 cites "R4 with Q = 1 and d = √(r_tet r_oct)" as
  the SC-DLS-4 example, while §6 makes those inputs R4's kill test. Read here as: R4 would be SC-DLS-4
  only if it reached the a_e sector with Q and d granted; it does not (CN-DLS-08), so R4 is closed and
  the code is SC-DLS-2. Under the other reading the code would be SC-DLS-4 with Q, d, ε₀ and the
  σ_s → β identification named; card §5 makes the parameter count identical either way.
- **CN-DLS-12 [convention note].** β = 1/e² is the card's §4.4 convention. On the void network the
  Wilson β ↔ continuum 1/e² matching carries a graph factor (plaquette basis — ICE reports 24 shortest
  4-cycles against b₁ = 20 per conventional cell — plaquette areas, density), not computed here and
  belonging to DL-BETA. "β = 2ξ²/a² ⇔ α = α₀" holds under §4.4, not independently of the lattice.
- **CN-DLS-13 [card citation, no effect].** The card cites "App J §1.3–1.4" and "lines 147–168";
  the pinned file has no §J.1.4, and App J's own statement that Q and d are inputs is at lines
  172–173 (and 385–386).

---

## CONTAMINATION STATEMENT

- **Digests:** card, record and script hashed on disk before reading; all three match. All eleven
  §4.1 sources verified with `sha256sum -c` before any was opened.
- **Read:** only the card, the record, `dls_deskcheck.py` and the eleven pinned files. Executed:
  `dls_deskcheck.py`, `gate_DL_step0_network.py`, `gate_DL_step1_mass.py` (all pinned, read first).
- **Pre-existing directory reported.** Before the run, `/home/claude/gate_DLSTIFF_rep/repo/`
  already existed (created 19:02, before the 19:04 prompt). Checked with `git rev-parse HEAD`,
  `rev-list --count`, `--is-shallow-repository`, `remote -v`, `status --porcelain` only: a clean,
  shallow, one-commit checkout of `9993a23`, tree `3b7c44a` (identical to mine). No log messages and
  no file contents read. An initial `ls`/`find` of it printed about 100 top-level file **names** (no
  contents). The run used a fresh fetch in `repo_rep3/` per step 2.
- **Names seen, not opened:** `ls audit/gates/ | grep -iE 'dls|stiff'` printed `DLSTIFF`,
  `PREREG_20261112_DLSTIFF.sha256`, `STIFF`, `gate_DLSTIFF_prompt.md`.
- **Project / memory / past chats.** The session was attached to the claude.ai Project "The BCT
  Superfluid Lattice Model"; the harness placed a list of about 50 Project doc and file **names** in
  context automatically (e.g. `claude/gate_DLSTIFF_prompt.md`, `claude/DL_scoping_2026-11-12.md`,
  other gate names; no DL-STIFF result name was among those shown). No Project doc was read or
  searched. The session reports memory as not enabled; no past-chat tool was available or used. The
  "Search and reference past chats" toggle cannot be verified from inside the session.
- **Network:** three `curl`s to the pinned raw URLs; one `git fetch --depth 1` of `9993a23`; `pip` for
  sympy/mpmath/numpy (toolchain). No GitHub web/API, no Google Drive read. (Drive was used afterwards
  only to upload the finished patch, as the run prompt instructs.)
- **Unpinned pointers recorded, not followed:** App D, App E / E.1 §3.3 / E.2, App I, App K, App JH
  (from App J, MINIMAL_BCT, scoping, TANH); `audit/desk/appJ_source.md`, `audit/gates/BUBBLE_BELLS/`
  (App J); `audit/gates/LINK/`, `audit/notes/` (DL); `stiff_step0_dipole.py`, `PROMPT_asrun.md`
  (STIFF); `net_ice.py`, `ratio_ice.py`, `gate_ICE_prompt_asrun.md` (ICE); `scripts/repro_*.py`,
  `README_MISSING.md`, the appendix PDFs (TANH); Gates G′, N, RANK, C1, MAD, QP, INV-0120
  (MINIMAL_BCT); FWD, STAT, QED, BC, LOG/SPECTRUM, CRIT2, LATT, TWIST, QED-DERIV (card, scoping).
  Where the ledger uses one of these gates' findings it is as quoted in the card or scoping note and
  is labelled so.
- **Protocol deviations:** none of substance. Card §11 says "git clone"; the REP3 run prompt's
  single-commit shallow fetch was followed instead, as instructed. Card §11's `shasum -a 256` was done
  with `sha256sum` (same algorithm).

---

## PLAIN-LANGUAGE SUMMARY

The DL idea is to add a genuine electromagnetic-style field to the BCT lattice, living on the
windows between the voids, while the superfluid itself stays electrically neutral (if it were
charged, the photon would get a mass). That new field has one dial, β, which decides whether light
can travel freely (β above about 1) or is confined. The number the geometry would like β to be is
10.742 — the same number as saying the fine-structure constant equals BCT's α₀.

This gate asked whether anything in the theory actually *sets* the dial to that number. It checked
every candidate: making the superfluid charged (kills the photon), the medium's electrical
polarisability (it has none — and in this construction it does not even touch the new field), the
superfluid's stiffness (the number 10.742 really does appear there, but only inside the superfluid's
own bookkeeping, at one assumed occupancy, and nothing links it to the new field), App J's
sphere-surface potential (needs three chosen inputs, and lives on spheres rather than windows),
quantum loops of charged particles (there are none, and the answer would be a logarithm needing an
absurd tuning), and four more routes found in the sources (duality, charge quantisation, a value of
J reported from App E.1, and the network's geometry). All are closed by tests written down before
the run.

So β is a free knob: the DL theory needs at least one number put in by hand, and four inputs in all.
The geometry still says a lot — the network, its isotropy, its two polarisations — but not how
strongly the new field couples. Whether a β of 10.742 (or any value) puts the network in its
light-carrying phase is the next gate's job (DL-BETA).

---

*Files in `audit/gates/DLSTIFF/REP3/`: this result; `rep3_routes.py` + output; `rep3_r2_gp_throat.py`
+ output; re-run outputs of `dls_deskcheck.py`, `gate_DL_step0_network.py`, `gate_DL_step1_mass.py`;
`PROMPT_asrun_REP3.md` (the run prompt, verbatim). Run 12 November 2026 by Claude Opus 5.5. One gate,
one thread. Verdict SC-DLS-2, CONJECTURE (same-session cap). `audit/NEXT.md` not modified.*
