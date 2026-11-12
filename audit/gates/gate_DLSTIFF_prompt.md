# Gate DL-STIFF — pre-registration card

**Programme:** BCT Cold Ledger — DL construction track ("building the DL theory from scratch").
**Card written:** 12 November 2026, Claude (Fable 5.1), at Michel's request ("Proceed pls"), in the
SONO review thread, after the scoping note `audit/scoping/DL_scoping_2026-11-12.md` (committed with
this card; orientation only).
**Status:** PRE-REGISTERED, NOT RUN. No route has been evaluated beyond the §7 desk check.
**Type:** hypothetical-construction gate, analytic. It audits a proposed new theory (Gate DL's
construction), not the written corpus. Nothing here can vindicate BCT-as-written; see §3.
**Depends on:** Gate DL (SC-DL-1 falsified; CN-DL-06/07: β unestablished, Coulomb phase needs β > β_c),
Gate STIFF (SC-STIFF-5: no double layer in the neutral single-component medium), Gate ICE (SC-ICE-1:
a soft window coupling is not a gauge theory), Gate PROMOTE (SC-PROMOTE-1/5: no geometry-selected
promotion; a hard Gauss law needs inputs the packing does not fix), Gate TANH (SC-TANH-3: App J's
computed window coupling g = 0.00037 is not α₀), Gate RATIO (SC-RATIO-2: the geometry supplies one
number, ξ/a = 2.3175). Gate BC (chat-side, not in the tree) found App J's σ_s = α₀ a two-input fit;
the run may cite it from the ledger but must re-derive anything it uses.

---

## 1. Background (stated, not a result of this card)

**The construction under audit (option B of the scoping note).** The FCC void network — nodes = the
octahedral and tetrahedral voids, links = the triangular windows between them; 1 oct + 2 tet nodes
and 8 links per primitive cell, cycle rank b₁ = 5 per cell, edge tensor exactly I/3 (Gate DL,
CN-DL-01/04) — carries a compact U(1) link field a_e with the Wilson action
S_gauge = β Σ_p (1 − cos Φ_p), Φ_p the plaquette flux, Gauss's law imposed at the nodes. The
superfluid of MINIMAL_BCT §1.1–1.2 (one complex scalar, GP action with stiffness J and healing length
ξ) is **neutral** under this field; that neutrality is what spares the photon the Meissner mass
(Gate DL, CN-DL-02). Gate DL left one brick unlaid: the value of β, which decides whether the theory is
in its (3+1)D Coulomb phase (massless photon, β > β_c) or confined.

**What "β fixed by geometry" would have to mean.** With the Wilson normalisation β = 1/e² and
e² = 4πα, a geometrically fixed β is the same statement as a geometrically fixed α for the added
field. The corpus's geometric coupling is α₀ = r_oct r_tet/π, and by the definitions in
MINIMAL_BCT §1.3,

    1/(4π α₀)  =  1/(4 r_oct r_tet)  =  2 ξ²/a²  =  10.742018   (exact identity; §7).

So the only geometric candidate is β_geom = 2ξ²/a² = 10.74, and claiming it is claiming α = α₀ for
the link field. That claim's earlier forms were closed by FWD/STAT (α₀ → α is a selected correction
map) and by BC (σ_s = α₀ in App J is a two-input fit). This gate asks whether the **new** field offers
a route those gates did not cover.

**Why the number would suffice if it were real.** β_geom/β_c ≈ 10.6 (hypercubic), 8.7–17.5 (D4, the
two CRIT2 conventions). The void network's own β_c is Gate DL-BETA's job; no known lattice has β_c
above ~1.3, so β ≈ 10.7 would be deep in the Coulomb phase. This gate is about whether anything makes
β equal to that number, not whether it suffices.

## 2. Question

**Is the plaquette coupling β of the added link field fixed by the medium plus the void geometry, or
is it a free input of the DL theory?**

1. **Route ledger (Q1).** For each candidate route by which β could be fixed, state it from the
   pinned sources, name its inputs, and apply its kill test (§6). The fixed list:
   - **R1 — minimal coupling.** The condensate is charged under a_e (∂θ → ∂θ − q a). Kill test: the
     Meissner mass m_A² = q²ρ_s ≠ 0 (Gate DL's charged branch, LINK). A charged medium cannot be the
     neutral medium of option B; the route contradicts the construction.
   - **R2 — induced Maxwell term from the medium's dipole response.** The neutral medium couples via
     P·E; integrating it out gives (χ/2)E², i.e. a contribution to β. Kill test: χ = 0 if the medium has
     no polarisable charge distribution (STIFF: P ≡ 0 for the written medium). The run must exhibit a
     nonzero χ from the pinned sources to keep this route.
   - **R3 — identification with the phase stiffness.** β := J_dimensionless (the Josephson-array
     analogy, where the link coupling is E_J). Kill test: a plaquette coupling is the energy of a loop
     of *field*, not of phase; in the analogue it is Φ₀²/(2L_loop), an independent scale. The route
     survives only with a derivation that the added field inherits J — otherwise it is an assertion.
   - **R4 — α₀ as the surface/boundary coupling.** App J §1.3–1.4: σ_s = r_tet r_oct/(4πR²) = α₀ (J/J₀),
     boxed σ_s = α₀; the dimensionless Josephson coupling g = σ_s/J. Kill test: BC (ledger) found σ_s = α₀
     requires Q = 1 and d = √(r_tet r_oct), both asserted; TANH found the computed g = 0.00037 ≠ α₀.
     The route must re-derive σ_s without those two inputs and show how a *sphere-surface* potential
     becomes a *window-link* plaquette coupling.
   - **R5 — induced Maxwell term from charged matter loops.** Integrating out charged fields gives
     β ∝ (1/12π²) Σ q² ln(Λ/m) (the LOG/SPECTRUM "induced light" class). Kill test: needs charged
     matter absent from the corpus, and the coefficient is a logarithm of a cutoff ratio, not a
     geometric number; recording that β comes out as 10.74 would require tuning the ratio.
   - **R6 — any route in the pinned sources not listed above.** The favourable slot. The run states it,
     names its inputs, and applies the same kill-test discipline.
2. **Surviving route(s) (Q2).** For each route that passes its kill test, the derivation in full, with
   every input named and tiered, and the resulting β to 10 digits.
3. **Comparison (Q3).** Each surviving β against β_c: hypercubic 1.0111; D4 0.6150 (card convention) and
   1.2300 (Katz–Nógrádi); the void network's β_c marked "DL-BETA pending". A surviving β equal to
   2ξ²/a² to within its own stated tolerance is SC-DLS-1; a surviving β with a different value is
   SC-DLS-3.
4. **Equivalence statement (Q4).** Record, without scoring, that SC-DLS-1 is equivalent to α = α₀ for
   the added field, and list which earlier gates (FWD, STAT, QED, BC, TANH) a surviving derivation would
   have to be reconciled with — a sentence each, no rescoring.
5. **Cost count (Q5).** The DL theory's free inputs after this gate, in TWIST's cost-table form: the
   added field (1), β (0 or 1 by this gate's verdict), the charge carrier (1, Gate DL-MATTER), the α
   identification (0 or 1). One table.

## 3. Choices made by the analyst, and what they cost

- The construction audited is option B of the scoping note (fundamental link field, neutral
  superfluid). Cost: a route that fixes β only by making the medium charged (R1) is recorded as
  closed, not as a different theory worth scoring.
- The route list is fixed at R1–R5 plus the open R6. Cost: an exotic route the analyst did not think
  of lands in R6 and is scored by the same kill-test discipline; the run may not add a route without
  naming its inputs.
- Kill tests are stated in the card (§6), before the run. Cost: a route killed by its stated test is
  closed even if the run finds it attractive.
- Out of scope: the value of β_c on the void network (DL-BETA); what carries charge (DL-MATTER); the
  dipole brick of option A; whether the written corpus has a photon (closed: G′, PH, LINK, XI, PSI2,
  ICE, STIFF, PROMOTE, PV, QED, QED-DERIV).

## 4. Fixed rules

**4.1 Sources, pinned.** Repository zerofreeparameters-code/BCT-Programme at commit
`9114b6e8da4032f944d141995a0a2baafaf38bce` (the scoping note and this card are added by the
pre-registration commit; every other file is at `9114b6e`). SHA-256 (verify before reading):

| File | SHA-256 |
|---|---|
| `audit/MINIMAL_BCT.md` (field content, action, constants) | 952ad4775d1a927df7983b1e2fee57e39e32990674eab882a9d26fb639d3c77b |
| `audit/gates/DL/gate_DL_RESULT.md` (the construction; CN-DL-01…07) | 3eff786202696bd1613187bdb35c3ac2b9a9918a27138995999b6a90d3c128b4 |
| `audit/gates/DL/gate_DL_step0_network.py` (the void network, reusable) | 7935f7e7a8a784c03c3465349a539d3fce95665957009a6b88d4b9b93874a4ee |
| `audit/gates/DL/gate_DL_step1_mass.py` (the Higgs/dipole fork, symbolic) | 6e082574e208e849facf18cd1fc9d9240e718dd1902f92e2aed364c3fff8c93d |
| `audit/gates/STIFF/STIFF_RESULT.md` (P = 0 for the written medium) | 1d0be8691c9c49db3489d567d238d2f29591ef722356cfcc8b7f0a021ceee672 |
| `audit/gates/ICE/gate_ICE_RESULT.md` (soft coupling ≠ gauge theory) | b458a3c1ed8bbd323db483dcb05187b70d702a40bd241e5d76c831ad4d8d11bc |
| `audit/gates/PROMOTE/gate_PROMOTE_result.md` (no selected promotion; input list) | 761c3bdf17f0c4cb1e9c3cd9fb7e75f428a68fedbe0e63c1468534552c40dca2 |
| `audit/gates/TANH/gate_TANH_RESULT.md` (g vs α₀ in App J §3.1) | 090ede6120d3bb4210e26c3d6ed5db50cdb68d4c2f39cfa0bf43419fc37858eb |
| `tex/BCT_Appendix_J_SphereAction.tex` (R4's source: σ_s, g) | ad9ecd0c6ddb899a57bee0e1445e7c8cb70067deed2f9ee4fd0f561c633432df |
| `audit/scoping/DL_scoping_2026-11-12.md` (orientation only; at the pre-registration commit) | — (hash in `PREREG_20261112_DLSTIFF.sha256`) |
| `audit/gates/DLSTIFF/dls_deskcheck.py` (card-thread validation, §7) | 332e2d1275196c5720d78fcce6e0364d567c3281476d4795c032010e5989bde5 |

**4.2 Route ledger format.** One table: Route | Statement (with source line) | Inputs (named, tiered) |
Kill test (from §6) | Result (closed / survives) | β if survives.

**4.3 What counts as "fixed by geometry".** A derivation from the pinned action and the void network
whose every input is a quantity in MINIMAL_BCT §1.3 or a theorem about the FCC void network, with no
asserted coefficient. One asserted coefficient makes the route SC-DLS-4 (parametered), not SC-DLS-1.

**4.4 Conventions.** Wilson action S = β Σ_p (1 − cos Φ_p); β = 1/e²; e² = 4πα; lattice unit a = 1.
Critical couplings as quoted in §1 with their conventions named. mpmath 30 digits working, 10
reported; sympy for symbolic steps. Scripts under `audit/gates/DLSTIFF/`.

**4.5 No construction.** No new coupling, no new field, no new definition of α. R6 must come from the
pinned sources.

## 5. Verdict codes

- **SC-DLS-0 (unposable).** The construction or the routes cannot be stated from the pinned sources.
  Not expected.
- **SC-DLS-1 (derived).** A route survives its kill test with no asserted coefficient and gives
  β = 2ξ²/a² (α = α₀ for the link field). The DL theory has no free coupling. CONJECTURE until a
  blind replication; opens a reconciliation card against FWD/STAT/QED/BC/TANH (Q4).
- **SC-DLS-2 (free input).** Every route is closed by its kill test. β is a parameter of the DL theory;
  the theory is one-parameter at minimum.
- **SC-DLS-3 (derived, different number).** A route survives and gives a β ≠ 2ξ²/a². Report the number
  against β_c; the theory has no free coupling but its α is not α₀.
- **SC-DLS-4 (parametered derivation).** A route survives only with ≥ 1 asserted coefficient (e.g.
  R4 with Q = 1 and d = √(r_tet r_oct)). Equivalent to SC-DLS-2 for the parameter count; the named
  input is recorded.
- **SC-DLS-5 (inconclusive).** A route cannot be evaluated from the pinned sources.

Q1–Q5 are reported whatever the code.

## 6. Kill tests (fixed here, before the run)

| Route | Kill test | Computed how |
|---|---|---|
| R1 | m_A² = q²ρ_s ≠ 0 for q ≠ 0 | symbolic, as `gate_DL_step1_mass.py` |
| R2 | induced coefficient −χ/2 with χ = dP/dE; χ = 0 if the medium has no polarisable charge | symbolic (§7 script, part 3), then from the pinned sources: does any term give χ ≠ 0 |
| R3 | plaquette coupling is a loop-of-field energy; identification with J needs a derivation that the link field inherits J; absent that, assertion | by inspection of the pinned action: is there any term coupling a_e to Ψ |
| R4 | σ_s = α₀ requires Q = 1 and d = √(r_tet r_oct) (asserted); g_computed = 0.00037 ≠ α₀ | re-derive σ_s from App J §1.3 lines 147–168 with inputs listed |
| R5 | needs charged matter in the corpus; coefficient ∝ ln(Λ/m), not geometric | by inspection; if used, state the cutoff ratio that would give 10.74 |
| R6 | the same four conditions: stated from sources, inputs named, no asserted coefficient, β computed | as above |

## 7. Validation already done (why the card is not blind to the arithmetic)

`dls_deskcheck.py` (SHA-256 332e2d12…9bde5, 3972 B), 12 Nov 2026, card thread, mpmath 30 digits +
sympy 1.14:

- 1/(4πα₀) = 1/(4 r_oct r_tet) = 2ξ²/a² = 10.74201848, the three forms agreeing to 30 digits
  (exact by definition). 1/(4πα_CODATA) = 10.90497833.
- β_geom/β_c = 10.62 (hypercubic 1.0111), 17.47 (D4, 0.6150), 8.73 (D4, 1.2300).
- Symbolic: a medium with dipole response P = P₀ + χE contributes −χ/2 to the E² coefficient;
  with P ≡ 0 the contribution is zero. This is R2's kill test written down, not its evaluation.
- No route was evaluated; no source beyond those pinned was read for this purpose.

## 8. No-fit clause

- No route, kill test, convention or verdict code may be changed after the run starts.
- A route that fails its kill test stays failed; the run may note what would revive it in a sentence.
- Same-session results are capped at CONJECTURE. A favourable SC-DLS-1 is CONJECTURE until a blind
  replication in a second fresh thread.

## 9. Analyst's disclosure

- **Forecast: SC-DLS-2, about 70 %; SC-DLS-4, about 15 %; SC-DLS-3, about 10 %; SC-DLS-1, about 5 %.**
  R1 contradicts the construction; R2 needs a polarisable charge STIFF says is absent; R3 is the
  Josephson-array analogy and the analogue's loop coupling is independent of E_J; R4 is BC's fit and a
  sphere-surface quantity, not a window-link one; R5 needs matter the corpus lacks. The 5 % on SC-DLS-1
  is the R6 slot.
- **Interest.** The analyst wrote the scoping note that proposed this gate and the 12 Nov NEXT.md, and
  argued in the same thread that the written theory cannot carry a photon; the forecast is consistent
  with that and is recorded so it can be scored against the outcome.

## 10. Known limitations

- Analytic gate: its evidence is the pinned sources and standard lattice-gauge physics; it does not
  simulate. The void-network β_c is DL-BETA's.
- Gate BC and Gate QED are chat-side (not in the tree); their findings are cited from the ledger and
  must be re-derived by the run where used.
- "Fixed by geometry" (§4.3) is a strict standard; a route that is suggestive but carries one
  coefficient is SC-DLS-4 by construction.

## 11. Run protocol

- Fresh thread inside the BCT Project. Before opening it, switch off "Search and reference past chats"
  and "Generate memory from chats" in Settings; switch them back on after the run. One gate per thread.
- Fetch this card by commit-pinned raw URL with curl to disk; `shasum -a 256` it there and compare with
  `audit/gates/PREREG_20261112_DLSTIFF.sha256` **before reading it**. Record the digest and the commit.
- `git clone` the repository at the pre-registration commit; verify every §4.1 hash before reading any
  source.
- Build Q1 first (the ledger, with each kill test computed), Q2–Q5 in order.
- Deliverable: `audit/gates/DLSTIFF/gate_DLSTIFF_RESULT.md` with the route ledger, derivations, the
  comparison table, the Q4 equivalence statement, the Q5 cost table, the verdict code, the §9
  disclosure scored item by item, correction notices CN-DLS-nn, and a plain-language summary; the
  scripts; and a copy of the as-run prompt. The session cannot push: deliver a `git format-patch`
  bundle adding `audit/gates/DLSTIFF/` only.
- Same-session results are capped at CONJECTURE.
