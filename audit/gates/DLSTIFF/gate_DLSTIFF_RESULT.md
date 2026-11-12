# GATE DL-STIFF — RESULT

**Is the plaquette coupling β of the added link field fixed by the medium plus the void geometry, or
is it a free input of the DL theory?**

- **Gate type:** hypothetical-construction, analytic. It audits Gate DL's proposed construction
  (option B of the scoping note), not the written corpus. Nothing here can vindicate BCT-as-written.
- **Card:** `audit/gates/gate_DLSTIFF_prompt.md`, SHA-256
  `294da0f50c5d740956bb0b3d64871f580a00f454a0f541701467bba47ee48e21`. **MATCHES pre-registration.**
- **Pre-registration record:** `audit/gates/PREREG_20261112_DLSTIFF.sha256`, SHA-256
  `682effc99bc12bfee62de437080ccc9054d9ea0e84ecd4de1d62da3fc9dcb696`. **MATCHES.**
- **Card-thread validation script:** `audit/gates/DLSTIFF/dls_deskcheck.py`, SHA-256
  `332e2d1275196c5720d78fcce6e0364d567c3281476d4795c032010e5989bde5`. **MATCHES.**
- **Card commit:** `9993a2381cdbdd8604975f285644aabb94063325`. Its parent is
  `9114b6e8da4032f944d141995a0a2baafaf38bce`, the commit §4.1 pins for every other source —
  verified by `git rev-parse HEAD~1`.
- **All eleven §4.1 source hashes verified before reading**: `sha256sum -c` returned OK on every
  line (transcript in `dls_source_verification.txt`).
- **Run date:** 12 November 2026, Australia/Melbourne. Fresh thread, one gate.
- **Model:** the thread opened under Claude Fable 5.1 (fetch, hash verification, source reading) and
  switched to Claude Opus 5 partway through, before any kill test was computed. Recorded because a
  replication would want it; no finding depends on it.
- **Verdict:** **SC-DLS-2 (free input).** Every route, R1–R5 and all four R6 routes found, is closed
  by its pre-registered kill test. β is a parameter of the DL theory. **CONJECTURE** (same-session
  cap, card §8).

---

## VERDICT (first)

**SC-DLS-2. β is a free input of the DL theory.** Not one route survives, and the reason is a single
structural fact that the card's route list approaches five separate ways:

> **The decoupling theorem (CN-DLS-01, PROVEN).** For the pinned action — MINIMAL_BCT §1.2 plus the
> Wilson term `S_gauge = β Σ_p (1 − cos Φ_p)` — the superfluid is neutral under `a_e`, so `S_med`
> contains no `a_e` at all. The partition function factorises,
> `Z = (∫DΨ e^{−S_med}) · ∫Da e^{−S_gauge}`, and the medium contributes **nothing** to the effective
> action for `a`. Hence **β_eff = β_bare exactly**: the medium cannot renormalise β, let alone fix
> it. β enters only as the coefficient the Wilson term was written with.

This closes R2, R3, R5 (absent added charged matter) and the strongest new R6 route in one step,
before any of their individual kill tests is reached. Each kill test was nonetheless computed as the
card requires.

**And the finding worth stating plainly (CN-DLS-02, PROVEN).** The only way to make the medium's
action depend on `a_e` without adding a new coupling is to give the condensate charge, `q ≠ 0` — and
that is exactly what produces the Meissner mass `m_A² = q²ρ_s ≠ 0` (re-derived cold here; Gate DL's
charged branch, Gate LINK's fate). **Neutrality is what buys the photon its masslessness, and
neutrality is what costs the theory β.** The two desiderata of the DL construction are in direct
structural conflict. A medium that can fix β is a medium that gaps the photon.

**Robustness of the label.** R4 and the new R6b fail their kill tests as written, so they are closed.
Under the most charitable possible reading — granting R4 its three asserted inputs, or R6b its
assertion plus `n̄ = 1` — the honest label would be **SC-DLS-4**, which by the card's own §5 is
"equivalent to SC-DLS-2 for the parameter count." **The Q5 cost table is identical under both
readings.** The verdict does not turn on that judgement call.

**No overclaim in the other direction.** This does not refute the void geometry: the packing, the
void network, `r_oct r_tet`, ξ, the edge tensor `I/3` and the two-polarisation isotropy of Gate DL
CN-DL-01/04 all stand untouched. It also does not show β is *outside* the Coulomb phase — it shows
nothing fixes β at all, so CN-DL-06 stays open in the only way it can: as a parameter.

---

## Q1 — ROUTE LEDGER (card §4.2 format)

| Route | Statement (with source) | Inputs (named, tiered) | Kill test (card §6) | Result | β if survives |
|---|---|---|---|---|---|
| **R1** minimal coupling | The condensate is charged under `a_e`: `∂θ → ∂θ − q a` (Gate DL STEP 1 fork (B), charged branch) | `q` **ASSERTED** (not in MINIMAL_BCT §1.1–1.2) | `m_A² = q²ρ_s ≠ 0` for `q ≠ 0`, symbolic | **CLOSED.** Computed: `m_A² = q²φ₀²`. A charged medium is not option B's neutral medium; the route contradicts the construction it serves | — |
| **R2** induced Maxwell from dipole response | Neutral medium couples via `P·E`; integrating out gives `(χ/2)E²`, a contribution to β (Gate DL CN-DL-02: the dipole "renormalises ε") | `χ = dP/dE` **must be exhibited nonzero from the pinned sources** | `χ = 0` if the medium has no polarisable charge | **CLOSED.** `δβ ~ −χ/2`; STIFF CN-STIFF-01/02/03 [PROVEN] give `P ≡ 0` by reflection symmetry, no Smoluchowski second component, nonzero `P` only under an imposed bias. No nonzero χ exists in the pinned sources. Also closed upstream by CN-DLS-01 | — |
| **R3** identification with the phase stiffness | `β := J_dimensionless` (Josephson-array analogy, link coupling `E_J`) | the identification itself **ASSERTED** | a plaquette coupling is a loop-of-**field** energy, `Φ₀²/(2L_loop)`, an independent scale; survives only with a derivation that the added field inherits `J` | **CLOSED.** By inspection: zero occurrences of `a_e` in `S_med`, zero of `Ψ` in `S_gauge`; mixed Hessian block `∂²S/∂a∂Ψ = 0`. `(β, J)` is a two-parameter family with no relation. The analogue itself says the loop coupling is independent | — |
| **R4** α₀ as the surface/boundary coupling | App J §J.1.3: `σ_s = ΔV·d ≈ Q d²/(4πR²)`; with `Q = 1`, `d = √(r_tet r_oct)`, boxed `σ_s = α₀` (lines 147–168); `g = σ_s/J` | `r_oct`, `r_tet`, `R = 1/2` **GEOMETRY**; `Q = 1` **ASSERTED**; `d = √(r_tet r_oct)` **ASSERTED**; `J = 1` **CONVENTION**; `ℓ_P = a = 1` **CONVENTION** | re-derive `σ_s` without `Q = 1` and `d = √(r_tet r_oct)`; show how a sphere-surface potential becomes a window-link plaquette coupling; note `g_computed = 0.00037 ≠ α₀` | **CLOSED on both halves.** `σ_s = α₀` reproduces *as an identity* once the two inputs are inserted — `d²/(4πR²) ≡ α₀/Q` by construction — and cannot be had without them; App J's own footnote says so. The sphere→window step is never taken, and `σ_s/J` has dimension 1/length against β dimensionless. `g = 0.000369750648` re-derived cold, `α₀/g = 20.0353` (TANH SC-TANH-3 reproduced) | (10.74201848 only if three inputs granted → SC-DLS-4) |
| **R5** induced Maxwell from charged matter loops | `β ∝ (1/12π²) Σ q² ln(Λ/m)` (LOG/SPECTRUM "induced light" class) | charged matter **ABSENT**; `Λ/m` **TUNED**; `Σ q²` **TUNED** | needs charged matter absent from the corpus; coefficient is a log of a cutoff ratio, not geometric | **CLOSED.** MINIMAL_BCT §1.1 is one neutral complex scalar; §1.5's vortex strings are neutral under a field the medium is neutral under (the carrier is DL-MATTER's separate input). Quantitatively: `β_geom` needs `ln(Λ/m) = 1272.2337` at `Σq² = 1` (`Λ/m ≈ 10^552.5`), or `Σq² = 24.690` at the corpus's own `m_P/m_e = 2.3892×10²²` — neither integer nor geometric | — |
| **R6a** the one-number form | MINIMAL_BCT §3: α₀ enters only through ξ, and ξ depends on the radii only through their product; Gate RATIO SC-RATIO-2: the geometry supplies one number, `ξ/a = 2.3175` | — (an observation, not a route) | same four conditions | **Not a route; it is the reason the others fail the way they do.** Any dimensionless β from the pinned geometry has the form `c/(r_oct r_tet)`; `β_geom ⇔ c = 1/4` exactly. The card §7 three-way agreement to 30 digits is an identity carrying no information. The whole empirical content of "β is fixed by geometry" is the coefficient `c` | — |
| **R6b** ICE's `E_J/E_C` | ICE CN-ICE-04 [PROVEN]: `E_J/E_C = 2 n̄² (ξ/a)²`, which **equals `β_geom` identically at `n̄ = 1`** | `n̄` **FREE** (ICE: "`n̄ ≳ 1`"); the identification **ASSERTED** | stated from sources ✓; inputs named ✓; **no asserted coefficient ✗**; β computed ✓ | **CLOSED.** It is the control parameter of the medium's own phase sector (rotors on the **nodes**, a global-U(1) matter ratio deciding superfluid vs Mott, SC-ICE-1), not the plaquette coupling of the added field; identifying them is R3's assertion in new clothing, which CN-DLS-01 forbids deriving. It also carries `n̄`, and equality needs `n̄ = 1` asserted. The coincidence is explained by R6a | (10.74201848 only at `n̄ = 1` and with the identification granted → SC-DLS-4) |
| **R6c** speed matching | Demand the added field's wave speed equal the medium's; Gate DL CN-DL-02 notes a neutral dipole shifts the photon **speed** | `β_t/β_s` only | same four conditions | **CLOSED.** In the anisotropic Wilson action the dispersion is `β_t ω² = β_s k²`, so `v² = β_s/β_t`: the speed fixes only the **space–time anisotropy** — the very convention the scoping note §5 already pre-registers for DL-BETA (`β_t = β_s`) — and is blind to the overall β, which is what decides the phase and equals `1/(4πα)` | — |
| **R6d** App E.1 §3.3's `J = 1/(4πα₀) = 10.74` | Identified from the **pinned** scoping note §4: the corpus writes this as a monopole-action parameter; Gate QED CN-QED-04 found that section's arithmetic inconsistent | unknown; `tex/BCT_Appendix_E1` is **not pinned** | same four conditions | **NOT EVALUABLE (SC-DLS-5 for this sub-route only).** App E.1 was not read: §4.1 pins the sources and §4.5 forbids construction. On the pinned description it is a parameter *written down*, which fails §4.3's standard on its face; `1/(4πα₀)` is `c = 1/4` again. Recorded as a follow-up card | — |

**Routes surviving Q1: none.**

---

## Q2 — SURVIVING ROUTE(S): DERIVATIONS

**There are none.** The card requires "for each route that passes its kill test, the derivation in
full, with every input named and tiered, and the resulting β to 10 digits." No route passes, so this
section instead records the two derivations that come *closest*, in full, so that a reader can see
precisely where each stops being a derivation. Both are reported at 10 digits from 30-digit working.

### Q2.1 — R4 in full (the closest thing to a derivation in the corpus)

From App J §J.1.3, eq. (eq:sigma) and (eq:alpha0):

```
σ_s = ΔV · d  ≈  Q d² / (4π R²)                     [App J line 153]
α₀  = r_tet r_oct / (4π R²)                          [App J line 158]
```

Inputs, tiered:

| input | value (10 dig) | tier | source |
|---|---|---|---|
| `r_oct = (√2−1)/2` | 0.2071067812 | GEOMETRY | MINIMAL_BCT §1.3 / App D |
| `r_tet = (√6−2)/4` | 0.1123724357 | GEOMETRY | MINIMAL_BCT §1.3 / App D |
| `R = 1/2` | 0.5 | GEOMETRY | App J (`c/R = 2 m_P c²`; `4πR = 6.2832`) |
| `Q = 1` | 1 | **ASSERTED** | App J line 161, flagged as an input by App J itself |
| `d = √(r_tet r_oct)` | 0.1525552144 | **ASSERTED** | App J line 162, flagged as an input by App J itself |
| `J = 1` | 1 | CONVENTION | App J lines 166–168 |
| `ℓ_P = a = 1` | 1 | CONVENTION | needed to equate a 1/length with a pure number |

Result: `σ_s = 0.007408055728 = α₀` to 30 digits. **This is an identity, not a derivation**: with
`d² = r_tet r_oct` substituted, `Q d²/(4πR²)` *is* `Q α₀`, so `Q = 1` returns `α₀` by construction.
The two asserted inputs do the whole of the work, and App J's summary footnote says exactly that.

Where it stops: nothing in App J, or in any pinned source, carries `σ_s` from a **sphere shell at
`r = R`** to a **plaquette of the void graph**. The two objects differ in dimension (1/length vs
dimensionless), in support (sphere shells vs minimal cycles of the oct–tet window graph), and —
fatally — in role: `σ_s` is a coupling of the medium to the shell, and the added link field does not
appear in it. If one nonetheless asserts `β := 1/(4π σ_s/J)`, the number is **10.74201848**, and it
is that number because `σ_s` was built out of `r_oct r_tet` to begin with.

### Q2.2 — R6b in full (the one route the card's analyst did not list)

From ICE CN-ICE-04 [PROVEN], with `t = ℏ²/(2ma²)`, `U = g/a³`, `ξ² = ℏ²/(2mgn)`:

```
E_J/E_C = 2 n̄² (ξ/a)²            [ICE, ℏ and m cancel exactly]
β_geom  = 2 ξ²/a²                 [card §1]
E_J/E_C ÷ β_geom = n̄²             [symbolic; equal iff n̄ = 1]
```

At `n̄ = 1`: `E_J/E_C = 10.74201848 = β_geom`, exactly. This is the strongest candidate found — a
quantity **already derived in a pinned source**, needing no new coupling, whose value at unit
occupation is precisely the candidate β.

Where it stops, three ways, any one sufficient:

1. **It is the wrong object.** `E_J/E_C` is the control parameter of the medium's own phase sector:
   rotors on the **nodes** (voids), `E_J` the phase rigidity across a window, `E_C` the charging
   energy. ICE uses it to decide superfluid vs Mott (SC-ICE-1). It is a ratio in the matter sector of
   a **global** U(1). The plaquette coupling of the added **gauge** field is a different object, and
   CN-DLS-01 shows no derivation can connect them for the pinned action.
2. **It carries `n̄`.** The occupation is not fixed by the void geometry; ICE treats it as free
   (`n̄ ≳ 1`). Equality needs `n̄ = 1` **asserted** — one asserted coefficient, which card §4.3 makes
   disqualifying. (For scale: `n̄ = 2` gives 42.968; `n̄ = 0.3068` would put it at the hypercubic β_c.)
3. **The coincidence is explained.** Both expressions are dimensionless quantities built from the
   one geometric number, of the form `c/(r_oct r_tet)`, and both happen to carry `c = 1/4`. Two such
   expressions agreeing is not evidence that the objects they describe are the same.

---

## Q3 — COMPARISON AGAINST β_c

| lattice / convention | β_c | β_geom/β_c | source of β_c |
|---|---|---|---|
| hypercubic Z4 (Wilson, standard) | 1.0111 | 10.6241 | standard 4D lattice result |
| D4, CRIT2 card convention | 0.6150 | 17.4667 | Gate CRIT2 |
| D4, Katz–Nógrádi convention | 1.2300 | 8.7334 | Gate CRIT2 |
| **void network (FCC voids × time)** | **PENDING** | — | **DL-BETA pending** |

**Surviving β from this gate: none.** No route passed Q1, so there is no derived β to place in this
table. `β_geom = 10.74201848` is tabulated as the **candidate** number only — the value β would take
*if* some route fixed it — and its status after this gate is unchanged from before it: an identity of
the MINIMAL_BCT §1.3 definitions. Neither **SC-DLS-1** (a surviving β equal to `2ξ²/a²`) nor
**SC-DLS-3** (a surviving β of a different value) is reached, because nothing survives.

**What the table does show, and it is worth recording (CN-DLS-04).** Writing any geometric candidate
as `β = c/(r_oct r_tet)`, the Coulomb-phase condition `β > β_c` requires only

| convention | minimum `c` for the Coulomb phase |
|---|---|
| hypercubic 1.0111 | 0.02353 |
| D4 card 0.6150 | 0.01431 |
| D4 Katz–Nógrádi 1.2300 | 0.02863 |
| **candidate `β_geom`** | **`c = 1/4` exactly** |

So the *phase* conclusion is robust — any coefficient above ~0.03, a factor of nine below 1/4, puts
the theory in the Coulomb phase — while the *value* claim `α = α₀` needs `c = 1/4` to the last digit.
A future route that supplies some other O(1) coefficient would very likely still deconfine, and would
be SC-DLS-3, not SC-DLS-1. This asymmetry is why the card asks for β to 10 digits.

---

## Q4 — EQUIVALENCE STATEMENT (recorded, not scored)

**Recorded.** With the Wilson normalisation `β = 1/e²` and `e² = 4πα`, a geometrically fixed β is the
same statement as a geometrically fixed α for the added field. Since
`1/(4πα₀) = 1/(4 r_oct r_tet) = 2ξ²/a² = 10.74201848` is an exact identity of the MINIMAL_BCT §1.3
definitions, **SC-DLS-1 is equivalent to the claim `α = α₀` for the added link field.** This gate did
not reach SC-DLS-1, so nothing below is scored; it is the reconciliation list a surviving derivation
would have owed.

- **FWD** — a surviving derivation would predict `1/α = 134.9881854` for the added field, and would
  have to be reconciled with FWD's finding (cited from the ledger, card §1) that the step from α₀ to
  the measured `1/α = 137.0359992` is a *selected* correction map: the 1.5 % gap would stop being a
  pending refinement and become a prediction error of the DL theory.
- **STAT** — likewise with STAT's companion finding on the same correction map (card §1): a derived β
  removes the freedom that the correction map was using, so the two cannot both stand.
- **QED** — Gate QED is chat-side and its findings are cited, not re-derived: the pinned scoping note
  §4 records CN-QED-04 finding App E.1 §3.3's arithmetic inconsistent, so a surviving route could not
  lean on the corpus's own `1/(4πα₀) = 10.74`; and the scoping note §5 records CN-QED-09's space–time
  anisotropy question, which must be settled before a single β is even well defined (see R6c).
- **BC** — Gate BC is chat-side and cited: it found App J's `σ_s = α₀` to be a two-input fit
  requiring `Q = 1` and `d = √(r_tet r_oct)`. This run re-derived that dependence cold and found a
  third input (the unit identification), so any surviving route reusing `σ_s` inherits BC's objection
  in a strengthened form.
- **TANH** — SC-TANH-3 found App J §3.1's computed window coupling to be `g = 0.000369750648`, about
  twenty times smaller than α₀; this run reproduced both numbers and the ratio `α₀/g = 20.0353`
  independently. A route claiming the window-link coupling is α₀ must say which of the two numbers is
  the window coupling, and why the other is not.

---

## Q5 — COST TABLE (TWIST form)

Free inputs of the DL theory (option B) after this gate:

| input | cost | why |
|---|---|---|
| the added compact U(1) link field on the void network | **1** | not in the corpus; MINIMAL_BCT §1.1 is one complex scalar (PROVEN, Gate RANK) |
| **β, the plaquette coupling** | **1** | **this gate: SC-DLS-2.** Every route closed; β is an input of `S_gauge` and of nothing else |
| the charge carrier | **1** | Gate DL-MATTER, not run. §1.5's vortex strings are neutral under a field the medium is neutral under |
| the α identification | **0** | subsumed: with β free, β *is* what one fixes by fitting the observed α. Counting both would double-count one parameter |
| **TOTAL** | **3** | |

Notes, so the counting can be checked:

- The α identification scores 0 **because** β is free. One free coupling and one coupling observable
  are the same parameter; the theory buys α by spending β, and predicts neither.
- Had this gate returned SC-DLS-1, the table would read `1 + 0 + 1 + 0 = 2` — and the theory would
  then predict `1/α = 134.988` against the measured `137.036`. **A derived β would not have been a
  free win; it would have been a falsifiable and prima facie false prediction** (CN-DLS-10). This is
  worth saying because the card's §1 frames the number as something that "would suffice if it were
  real," which is true of the *phase* question and not of α.
- Under the most charitable reading of R4 or R6b (SC-DLS-4), β is still carried as an input — by the
  card's §5, "equivalent to SC-DLS-2 for the parameter count." **The table is unchanged.**
- The DL theory's only geometric content remains the lattice itself: isotropy and two polarisations,
  PROVEN already by Gate DL CN-DL-01/04. Exactly the scoping note §6 forecast.

---

## CN-DLS NOTICES (tiered)

- **CN-DLS-01 [PROVEN] — The decoupling theorem.** For the pinned action (MINIMAL_BCT §1.2 + Wilson
  `S_gauge`) with the medium neutral under `a_e`, `S_med` has no `a_e`-dependence; `Z` factorises and
  the medium induces no `a`-dependent term in the effective action. `β_eff = β_bare` exactly. The
  medium cannot renormalise β, let alone fix it. Closes R2, R3, R5-without-added-charged-matter and
  R6b at a stroke. Operator census: every coupling that could evade it
  (`|(∂−iqa)Ψ|²`, `−P·E`, `(χ/2)E²`, `c₁|Ψ|²F²`, higher-dimension `F²` terms) is either absent from
  the pinned action or carries its own new coefficient; card §4.5 forbids adding one, and it would be
  SC-DLS-4 at best if allowed. The Gauss-law constraint that card §1 imposes at the nodes does not
  evade this: `∇·E = ρ`, and a medium neutral under `a_e` contributes `ρ = 0` identically, so the
  constraint is a condition on the gauge sector alone. It becomes a coupling only once something
  carries charge — DL-MATTER's separate input, or R1's Meissner mass for the medium itself.
- **CN-DLS-02 [PROVEN] — The structural tension, and the finding of the gate.** `q ≠ 0` is the only
  way to make `S_med` depend on `a_e` without a new coupling, and it gives `m_A² = q²ρ_s ≠ 0`
  (re-derived cold, reproducing Gate DL's charged branch and Gate LINK's fate). Neutrality buys
  masslessness (CN-DL-02) and pays for it with β. A medium that can fix β is a medium that gaps the
  photon.
- **CN-DLS-03 [PROVEN] — The one-number form.** MINIMAL_BCT §3 and Gate RATIO SC-RATIO-2 leave the
  geometry one number. Any dimensionless β built from it has the form `c/(r_oct r_tet)`;
  `β_geom ⇔ c = 1/4` exactly (checked to 30 digits). The card §7 three-way agreement is an identity
  and carries no information: the entire empirical content of "β is fixed by geometry" is `c`.
- **CN-DLS-04 [PROVEN] — Phase robustness, value fragility.** `β > β_c` needs only `c > 0.02353`
  (hypercubic), `0.01431` (D4 card), `0.02863` (D4 Katz–Nógrádi), against `c = 1/4`. The Coulomb-phase
  conclusion is insensitive to the coefficient by a factor of nine or more; the claim `α = α₀` needs
  it exactly. A future route giving some other O(1) coefficient would be SC-DLS-3 and would probably
  still deconfine.
- **CN-DLS-05 [PROVEN] — R4's input count is three, not two.** `σ_s = α₀` reproduces as an identity
  once `Q = 1` and `d = √(r_tet r_oct)` are inserted (`d²/(4πR²) ≡ α₀/Q` by construction). A third
  input is needed: the unit identification `ℓ_P = a = 1`, without which `σ_s/J` (dimension 1/length,
  it sits beside `1/ξ` in `κ cot(κR) = −1/ξ + σ_s/J`) cannot be equated with a dimensionless β. This
  is consistent with CN-TANH-09's finding of undeclared unit conventions in the same neighbourhood.
  `g = 0.000369750648` and `α₀/g = 20.0353` reproduced cold (TANH SC-TANH-3 confirmed).
- **CN-DLS-06 [PROVEN] — R6b, not in the card's list.** ICE's `E_J/E_C = 2n̄²(ξ/a)²` equals `β_geom`
  identically at `n̄ = 1` — a quantity already derived in a pinned source, needing no new coupling,
  landing on the candidate number. It fails because it is a node-rotor/matter control parameter rather
  than a plaquette coupling, because it carries the free occupation `n̄`, and because the numerical
  coincidence is explained by CN-DLS-03.
- **CN-DLS-07 [PROVEN] — R6c, not in the card's list.** In the anisotropic Wilson action the
  dispersion is `β_t ω² = β_s k²`, so `v² = β_s/β_t`. The one physical requirement a neutral medium
  can impose on the added field — that light travel at the medium's own speed — therefore fixes the
  **space–time anisotropy** (the convention the scoping note §5 already pre-registers for DL-BETA)
  and is blind to the overall β. The orthogonal combination `√(β_t β_s)`, which sets `e² = 4πα`, is
  untouched.
- **CN-DLS-08 [PROVEN] — R5, quantified.** With the card's pinned form
  `β = (1/12π²) Σ q² ln(Λ/m)`: reaching `β_geom` needs `ln(Λ/m) = 1272.2337` at `Σq² = 1`
  (`Λ/m ≈ 3.34×10⁵⁵²`), or `Σq² = 24.690` at the corpus's own largest ratio
  `m_P/m_e = 2.3892×10²²`. Neither an integer nor a geometric quantity: the route delivers a tuned
  logarithm, as the card anticipated.
- **CN-DLS-09 [ASSERTED / NOT EVALUABLE] — R6d.** App E.1 §3.3's `J = 1/(4πα₀) = 10.74` monopole-action
  parameter was identified from the pinned scoping note §4 but **not read**: `tex/BCT_Appendix_E1` is
  not among the §4.1 sources and §4.5 forbids construction. On the pinned description it is a
  parameter written down, which fails §4.3's standard on its face, and Gate QED CN-QED-04 is recorded
  as having found that section's arithmetic inconsistent. **Recommended follow-up: a card that pins
  App E.1 and asks whether §3.3 derives or assumes the number.** This is the one place a future gate
  could, in principle, still disturb this verdict.
- **CN-DLS-10 [PROVEN] — What SC-DLS-1 would have been worth.** A derived `β = 2ξ²/a²` predicts
  `1/α = 134.9881854` against `1/α = 137.0359992` (CODATA), a 1.5 % miss, and closing that gap is
  precisely what FWD/STAT closed as a selected correction map. So the favourable verdict would have
  converted a free parameter into a probably-false prediction. The *phase* conclusion (`β ≫ β_c`)
  would have survived; the *α* conclusion would not.

---

## §9 DISCLOSURE, SCORED ITEM BY ITEM

**Forecast as pre-registered:** SC-DLS-2 ≈ 70 %; SC-DLS-4 ≈ 15 %; SC-DLS-3 ≈ 10 %; SC-DLS-1 ≈ 5 %.

| forecast item | outcome |
|---|---|
| **SC-DLS-2, 70 %** | **HIT.** This is the verdict. |
| SC-DLS-4, 15 % | Not the verdict, but the near-miss band was correctly identified: R4 and the new R6b are each SC-DLS-4 if their asserted inputs are granted, and the card's §5 makes that equivalent to SC-DLS-2 for the parameter count. |
| SC-DLS-3, 10 % | Did not occur. No route survived, so no different number was produced. |
| SC-DLS-1, 5 % (the R6 slot) | Did not occur. The R6 slot was the right place to look — it produced the one candidate the analyst had not listed (R6b) — and that candidate failed too. |

Reason-by-reason:

| stated reason | outcome |
|---|---|
| "R1 contradicts the construction" | **CONFIRMED**, computed: `m_A² = q²φ₀² ≠ 0`. |
| "R2 needs a polarisable charge STIFF says is absent" | **CONFIRMED and strengthened**: CN-DLS-01 closes R2 before χ is reached, because with no `Ψ`–`a` term there is nothing to integrate out that knows about `a`. |
| "R3 is the Josephson-array analogy and the analogue's loop coupling is independent of `E_J`" | **CONFIRMED**; mixed Hessian block is identically zero. |
| "R4 is BC's fit and a sphere-surface quantity, not a window-link one" | **CONFIRMED and strengthened**: three asserted inputs rather than two (CN-DLS-05), both halves of the kill test failed, and TANH's `g` reproduced cold. |
| "R5 needs matter the corpus lacks" | **CONFIRMED and quantified** (CN-DLS-08). |
| "The 5 % on SC-DLS-1 is the R6 slot" | **Well placed.** R6 yielded three genuinely new routes (R6b, R6c, R6d) plus the R6a observation; none survived. |

**Interest, restated as a caution.** The card's analyst wrote the scoping note that proposed this
gate, wrote the 12 Nov NEXT.md, and had argued in the same thread that the written theory cannot carry
a photon. The analyst forecast SC-DLS-2 at 70 %, and **this run returned SC-DLS-2** — the outcome
agrees with the forecaster's stated prior, which is exactly the situation in which a result most needs
independent replication. Per card §8 this result is capped at **CONJECTURE** regardless. Two things
cut mildly the other way and are recorded for a replicator to weigh: the run found a route the analyst
had not listed and which landed *on* the favourable number (R6b), and it closed R4 on a stricter basis
than the card anticipated rather than a looser one. Neither removes the need for a blind replication.

---

## WHAT THIS GATE DID **NOT** ESTABLISH

- It did **not** show that β is outside the Coulomb phase, or inside it. It showed nothing fixes β.
  CN-DL-06 remains open — as a parameter, not as a pending calculation of the medium.
- It did **not** compute β_c on the void network. That is Gate DL-BETA's (CN-DLS-07 does, however,
  settle the physical content of DL-BETA's pre-registered `β_t = β_s` convention: speed matching fixes
  that ratio and nothing else).
- It did **not** read `tex/BCT_Appendix_E1`, so R6d is recorded unevaluated (CN-DLS-09).
- It did **not** address what carries the charge (DL-MATTER), the dipole brick of option A, or the α
  correction map (FWD/STAT/QED remain as they were; Q4 rescored nothing).
- It did **not** refute the void geometry. The packing, the void network, `r_oct r_tet`, ξ, the edge
  tensor `I/3` and the two-polarisation isotropy of CN-DL-01/04 stand untouched.
- It did **not** vindicate BCT-as-written: this is a hypothetical construction (card §3, Gate DL §0.5).

---

## PLAIN-LANGUAGE SUMMARY

Gate DL left one brick unlaid. It had shown that if you add a magnetic-field-like U(1) field to the
links of the void network and keep the superfluid *neutral* under it, the photon escapes the mass that
killed every earlier attempt. What was left open was the strength of that field's self-coupling, β,
which decides whether the photon is massless or confined — and whether the theory has a free
parameter. There was a tempting number waiting: `1/(4πα₀) = 1/(4 r_oct r_tet) = 2ξ²/a² = 10.742`,
built out of nothing but the two void radii. If β were that number, the theory's coupling would be
geometry, not a dial.

**It is not.** The reason is almost embarrassingly simple once written down. "The superfluid is
neutral under the new field" means the superfluid's energy does not mention the new field anywhere.
Two things that do not appear in each other's equations cannot determine each other's constants: the
medium's partition function factors straight out of the calculation, and β comes out exactly as it
went in. β is a dial.

And the two things the construction wants turn out to be the same thing seen from opposite sides. The
*only* way to make the medium's energy depend on the new field, without inventing a new coupling, is
to give the superfluid electric charge — which is exactly what gives the photon a mass. So neutrality
is not a lucky feature of the double layer; it is a trade. You can have a medium that fixes β, or a
massless photon, but not both.

The five routes the card named all fail for versions of this, and the four I found in the open slot
fail for the same reason wearing different hats. The closest call was a genuine surprise: Gate ICE had
already derived a ratio, `E_J/E_C = 2n̄²(ξ/a)²`, which at unit occupation *is* 10.742 exactly. But
that ratio describes whether the superfluid itself is a superfluid or an insulator — a different
object on different variables — and it carries the occupation `n̄`, which geometry does not fix. The
agreement is explained by something duller: the geometry supplies only one number, so *every*
dimensionless quantity you can build from it is that number times a coefficient. Getting 10.742 out
tells you the recipe used ξ/a and a factor of two. The whole question was ever only about the
coefficient.

Two things are worth keeping. First, the phase question is much more robust than the number: almost
any O(1) coefficient would still put the theory in the Coulomb phase, so the photon can plausibly be
massless *with* a free β — it just costs a parameter. Second, had β come out geometric, it would have
predicted `1/α = 134.99` against the measured `137.036`. That is a 1.5 % miss, and closing it is
exactly the selected correction map earlier gates already closed. So the favourable verdict would have
traded a free parameter for a wrong prediction. The honest result is better than it looks: the DL
theory is a three-input lattice gauge theory on a void network whose genuine geometric content is the
lattice — the isotropy and the two polarisations that Gate DL already proved.

One door was left shut rather than closed: the corpus writes this same 10.74 into Appendix E.1 §3.3 as
a monopole-action parameter, and that file is not among the sources this card pinned, so I did not read
it. On the pinned description it is a number written down rather than derived, and Gate QED is on
record finding that section's arithmetic inconsistent. A follow-up card that pins App E.1 is the one
place this verdict could still be disturbed.

---

## CONTAMINATION STATEMENT

- Card, pre-registration record and card-thread validation script fetched by commit-pinned
  `raw.githubusercontent.com` URL with `curl` to disk; SHA-256 computed **before** reading the card;
  all three digests **match** the expected values given in the as-run prompt and in
  `PREREG_20261112_DLSTIFF.sha256`.
- Repository cloned at `9993a238…`; its parent verified as `9114b6e8…`; **every §4.1 hash verified
  with `sha256sum -c` before any source was read** (all OK, transcript in
  `dls_source_verification.txt`).
- **Sources read: exactly the eleven pinned in §4.1, and nothing else from the repository.**
  `tex/BCT_Appendix_E1`, `audit/NEXT.md`, `audit/notes/`, every other `audit/gates/*/` directory, and
  every other `tex/` file were **not** read. No memory summary, no past chat, no concurrent gate.
  "Search and reference past chats" and "Generate memory from chats" are the user's to set; this run
  consulted neither and nothing from either reached it.
- `audit/gates/DLSTIFF/` was inspected only with `ls` to confirm the pre-registration left exactly one
  file there (`dls_deskcheck.py`). **No result file existed, so none was opened**, per the as-run
  prompt's instruction.
- Gate BC and Gate QED are chat-side and not in the tree; their findings are **cited from the ledger**
  (the card §1/§6 and the pinned scoping note) and are not re-derived, except Gate TANH's `g`, which
  is in the tree and which this run reproduced cold from App J.
- Standard results used as mathematical machinery, flagged as cited not computed: compact-U(1) lattice
  gauge theory and its (3+1)D Coulomb phase; Polyakov 3D confinement; the Anderson–Higgs–London mass;
  Josephson-junction-array electrodynamics; one-loop vacuum polarisation in the form the card pinned.
  `β_c` values are quoted from the card with their conventions named, not computed here.
- All numerical and symbolic claims come from the four deterministic scripts in this directory
  (mpmath 1.3.0 at 30 digits, 10 reported; sympy 1.14.0). No Monte Carlo, no stochastic step. Scripts
  were run with `python3 -I` from a directory separate from the cloned repository.
- No route, kill test, convention or verdict code was changed after the run started (card §8). The
  route list R1–R5 was taken as fixed; R6a–R6d are entries in the card's own open slot, each stated
  from a pinned source with its inputs named.
- Same-session result: **capped at CONJECTURE.** A blind replication in a second fresh thread is
  required before this moves tier, and the §9 interest disclosure makes that replication more, not
  less, necessary.

---

*Gate DL-STIFF executed 12 November 2026. One gate, one thread. Deliverable, four scripts, their
captured outputs, the source-verification transcript and the as-run prompt committed under
`audit/gates/DLSTIFF/`. `audit/NEXT.md` not modified.*
