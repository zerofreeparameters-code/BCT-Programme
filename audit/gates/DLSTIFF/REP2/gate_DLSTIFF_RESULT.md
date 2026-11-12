# GATE DL-STIFF — RESULT (blind replication, REP2)

**Is the plaquette coupling β of the added link field fixed by the medium plus the void geometry, or is
it a free input of the DL theory?**

- **Model executing this run:** Claude Opus 5.5 (`claude-opus-5-5`).
- **Run:** 12 November 2026, from 18:09 AEDT. One gate, one fresh thread. Blind replication: the earlier
  run's result was not sought, not seen, and is not present at the pinned commit (`audit/gates/DLSTIFF/`
  held only `dls_deskcheck.py`).
- **Card:** `audit/gates/gate_DLSTIFF_prompt.md`, SHA-256
  `294da0f50c5d740956bb0b3d64871f580a00f454a0f541701467bba47ee48e21` (16033 B). Fetched by
  commit-pinned raw URL with `curl` to disk and hashed **before reading**; matches the replication
  prompt's expected digest and the card's entry in `PREREG_20261112_DLSTIFF.sha256`
  (`682effc99bc12bfee62de437080ccc9054d9ea0e84ecd4de1d62da3fc9dcb696`, 282 B).
- **Validation script:** `audit/gates/DLSTIFF/dls_deskcheck.py`, SHA-256
  `332e2d1275196c5720d78fcce6e0364d567c3281476d4795c032010e5989bde5` (3972 B). Matches.
- **Commit:** `9993a2381cdbdd8604975f285644aabb94063325` (Michel Robert Cabrié, 12 Nov 2026
  15:31:59 +1100, "Pre-register Gate DL-STIFF …"), fetched alone at depth 1; `git log --oneline | wc -l`
  = 1.
- **Sources:** the eleven files of card §4.1, every SHA-256 verified OK before any was opened (§P.1).
- **Toolchain:** Python 3.13.18, mpmath 1.3.0 (30 digits working, 10 reported), sympy 1.14.0,
  numpy 2.5.3 (only to rerun Gate DL's network script).
- **Tier:** everything below is **CONJECTURE** (same-session cap, card §8). Notices name their basis
  (identity, inspection, standard result, interpretation) so a later comparison can see what is checkable.

---

## VERDICT (first)

**SC-DLS-2 — free input. CONJECTURE.**

Every route on the card's list fails its own §6 kill test, and so do the four further candidates (R6a–d)
this run found in the pinned sources. β is a parameter of the DL theory: option B is a one-parameter
theory in its gauge sector at minimum, and four inputs by the Q5 table.

The structural reason is one line. In option B the superfluid is neutral under `a_e`, so the action
splits, `S = S_GP[Ψ; J, ξ, Ψ₀] + β Σ_p (1 − cos Φ_p)`, and the partition function factorises,
`Z = Z_GP(J) · Z_W(β)`. Nothing in the medium can set a number that appears only in the other factor
(`∂² ln Z / ∂J ∂β = 0`, computed). Every route that would fix β either breaks that factorisation, which
means making the medium charged (R1, and R2/R5 by the back door), or asserts an identification across
it (R3, R4, R6a).

The number the card asks about, `β_geom = 1/(4πα₀) = 10.74201848`, does occur natively in one pinned
source. It is Gate ICE's Josephson ratio `E_J/E_C = 2 n̄² (ξ/a)²` at occupation `n̄ = 1` (R6a). That is a
coupling of the scalar's own phase and number, not of `a_e`. It needs `n̄ = 1` asserted, and it equals
10.742 only if `a` is the sphere diameter: with the void-network spacing it is 28.6.

---

## Q1 — ROUTE LEDGER (card §4.2 format)

Input tiers: **§1.3** = a quantity in MINIMAL_BCT §1.3; **net** = a theorem about the FCC void network;
**free** = a quantity not fixed by §1.3 or the network; **asserted** = a value or identification put in
without derivation; **absent** = not present in the pinned sources.

| Route | Statement (with source line) | Inputs (named, tiered) | Kill test (from §6) | Result | β if survives |
|---|---|---|---|---|---|
| **R1** minimal coupling | Condensate charged under `a_e`: `∂θ → ∂θ − q a` (card l.55–58; DL l.101–105; `gate_DL_step1_mass.py` l.9–18) | q (**free**; ≠ 0 contradicts option B), J, Ψ₀ (**free**) | `m_A² = q²ρ_s ≠ 0` | **Closed.** Coefficient of A² = `J Ψ₀² q²` ≠ 0; and on the lattice the matter term is link-local (Hessian diagonal), so it gives a mass and **no** plaquette term even when charged | — |
| **R2** induced Maxwell from dipole response | Neutral medium couples via P·E; integrating out gives (χ/2)E² (card l.59–62; DL l.104–105, l.118–121) | P (**absent**: no P·E term in MINIMAL §1.2; STIFF P ≡ 0), e* (**free**, STIFF CN-STIFF-05) | χ = dP/dE; χ = 0 without polarisable charge | **Closed.** In option B Γ_medium[a] does not depend on a, so χ ≡ 0. The one nonzero response in the sources (STIFF CN-STIFF-03, to a *number* bias) reaches `a_e` only with q ≠ 0, which is R1, and then gives a screening mass `J Ψ₀² q² a₀²`, not χE² | — |
| **R3** β := phase stiffness | β = J_dimensionless, Josephson-array analogy (card l.63–66; DL l.40–42, l.164–165, l.172–173; scoping l.72–84) | J, Ψ₀ (**free**: not in §1.3); identification β = K (**asserted**) | Is there any term coupling `a_e` to Ψ? | **Closed.** MINIMAL §1.2 has two terms, neither containing `a_e`; Z factorises. Even granting β = K = JΨ₀², reaching 2ξ²/a² needs a further asserted value. The medium's own exact dual gauge field has coupling ∝ 1/K (inverse) and is a 2-form | — |
| **R4** α₀ as surface coupling | σ_s = r_tet r_oct/(4πR²) = α₀(J/J₀), boxed σ_s = α₀; g = σ_s/J (App J l.147–173, l.238–260; card l.67–71) | Q = 1 (**asserted**; STIFF: no electric charge), d = √(r_tet r_oct) (**asserted**), ε₀ = 1 and J = J₀ = 1 (**asserted** units), R = a/2 (§1.3 geometry) | Re-derive σ_s without Q, d; show sphere-surface potential → window-link plaquette coupling | **Closed.** `σ_s = Q d²/(4π ε₀ R²)`: σ_s/J = α₀ is **one** equation in four inputs. The σ_s term `σ_s ∮\|Ψ\|² dS` does not depend on `a_e`, so no sphere→link map exists to carry a coefficient. Computed g = 0.0003697506484 = α₀/20.03527447 | — |
| **R5** induced Maxwell from charged loops | β ∝ Σ q² ln(Λ/m) (card l.72–75) | charged species and q (**absent**), Λ/m (**free**) | Needs charged matter; coefficient is a log, not geometric | **Closed.** No charged matter in the sources. Hitting 10.742 needs ln(Λ/m) = 636.1168374 (one unit-charge Dirac fermion) or 2544.467349 (one complex scalar) | — |
| **R6a** ICE Josephson ratio | `E_J/E_C = 2 n̄² (ξ/a)²` (ICE l.115–125, CN-ICE-04) | n̄ = 1 (**asserted**; **free** per CN-ICE-08), a = d_nn (**asserted** unit), β := E_J/E_C (**asserted**) | R6's four conditions + R3's coupling test | **Closed.** Equals β_geom **exactly** at n̄ = 1, a = d_nn, but it is a ratio of the Ψ-sector's own couplings, with `a_e` in neither. It is unit-dependent (28.645 with the link length), and the classical lattice coupling it maps to is √(E_J/E_C) = 3.2775 | — |
| **R6b** dual of the medium | KR 2-form dual of a 3+1D superfluid (PROMOTE l.20, CN-PROMOTE-06/10) | K = 2JΨ₀² (**free**) | R6 conditions | **Closed.** Coupling 1/(8π²K), inverse to the stiffness; a 2-form with one polarisation, not `a_e` | — |
| **R6c** lattice–continuum matching on the network | Wilson action on the void network (DL l.86–87, CN-DL-01/04) | κ_p = \|\*p\|/\|p\| (**net**), 1/e² (**free**) | R6 conditions | **Closed.** S_W is homogeneous of degree 1 in β and the 4D lattice spacing cancels. Geometry fixes relative plaquette weights κ_p, never the overall 1/e² | — |
| **R6d** STIFF's charitable double layer | `S ~ (e*/ε₀)(2m/ħ²) ξ / f` (STIFF l.149–166) | e*, ε₀ (**free**) | R6 conditions | **Closed.** n̄ cancels, e*/ε₀ does not (re-derived); the only pinned expression containing the added field's normalisation leaves it free | — |

No route survives. Scripts: `dls_rep2_routes.py` (output `dls_rep2_routes_output.txt`), with the card's
`dls_deskcheck.py` rerun (`dls_deskcheck_output.txt`).

---

## DERIVATIONS — each kill test, computed

### R1 — minimal coupling

MINIMAL §1.2's kinetic term with `∂ → ∂ − iqA` and `Ψ = Ψ₀ e^{iθ}`:
`L = J Ψ₀² (∂θ − qA)² = J Ψ₀² q² A² − 2 J Ψ₀² q A ∂θ + J Ψ₀² (∂θ)²`. In unitary gauge the A² coefficient
is **`J Ψ₀² q² = q² ρ_s`**. It is nonzero for any q ≠ 0, which is DL's charged branch (DL l.102–103), and
the kill test fires.

On the void network the same term is `2 J Ψ₀² Σ_e [1 − cos(θ_j − θ_i − q a_e)]`. On a girth-4 loop
O–T–O–T (ICE l.64–65) the Hessian in (a₁…a₄) at a = 0 is `diag(2JΨ₀²q², …)` with **every off-diagonal
entry zero**. At tree level the charged medium therefore gives each link a mass and supplies no
multi-link (plaquette, flux) term. R1 does not fix β even in the theory it would turn option B into.
Plaquette terms from a charged medium arise only from loops, which is R5's class with q as an input.

### R2 — induced Maxwell term from the medium's dipole response

*(a) Option B.* The medium's action (MINIMAL §1.2, l.48) contains Ψ only. Its effective action
`Γ_med[a] = −ln ∫DΨ e^{−S_GP}` is independent of `a`, so `χ = −∂²Γ/∂E² = 0` identically. This is
stronger than, and consistent with, STIFF's P ≡ 0.

*(b) The ⟨P⟩ versus χ point.* χ is a response, so a symmetric ground state with ⟨P⟩ = 0 could still
be polarisable. In the pinned sources it is: STIFF CN-STIFF-03 (l.234–236) finds a window dipole linear
in an imposed void-to-void **number** bias. For that to be a response to `a_e`, the number density must
couple to `a₀`. That is the time component of minimal coupling, i.e. R1 (or an assigned charge e*,
which STIFF CN-STIFF-05, l.241–243, finds free). Computed: `J Ψ₀² (∂₀θ − q a₀)²` gives an `a₀²` term
at k⁰, with coefficient `J Ψ₀² q²`. That is a screening mass, not a `χ k² a₀²` dielectric term.

So the only polarisability the sources contain is in the wrong currency (number, not charge under
`a_e`). Converting it is R1. A neutral, gauge-invariant alternative would need a new coupling, which
card §4.5 forbids. The kill test fires.

*Sign note.* The desk check's "−χ/2" is the energy convention. In the Lagrangian the induced term is
+χ/2. It is zero either way.

### R3 — β identified with the phase stiffness

*Kill test (by inspection, card §6).* MINIMAL §1.2 has exactly two terms, `J(∂_μΨ)*(∂^μΨ)` and
`(J/4ξ²)(|Ψ|² − Ψ₀²)²`. Neither contains `a_e`. In option B none may be added (the medium is neutral,
DL CN-DL-02 and card §1). Hence `Z = Z_GP(J)·Z_W(β)` and `∂² ln Z/∂J ∂β = 0` (computed). No observable
ties β to J, and "β := J" is an assertion. DL's own sentences that β is "fixed by the stiffness of the
underlying medium" (l.40–42) and "if the vacuum medium is stiff … β is large" (l.164–165) are proposals
of exactly this assertion. DL itself lists the derivation as unlaid (l.170–174).

*What the identification would need even if granted.* The phase stiffness of the §1.2 action is
`K = J Ψ₀²` (`J|∂Ψ|² → JΨ₀²(∂θ)²`). Neither J nor Ψ₀ is in §1.3. Setting K = 2ξ² gives
`J = 2ξ²/Ψ₀²`, one equation in two unfixed symbols. So "β = J_dimensionless = 2ξ²/a²" carries a second
asserted value on top of the identification.

*Which direction the medium itself points.* PROMOTE (l.20; CN-PROMOTE-06/10) records the exact dual of a
3+1D superfluid: a Kalb–Ramond 2-form with one polarisation. Re-derived by Hubbard–Stratonovich,
`∫dj e^{−j²/2K + ijv} = √(2πK) e^{−Kv²/2}`. The stiffness K maps to a current action j²/2K and, with
`j = (1/2π)*dB`, to a 2-form coefficient `1/(8π²K)`. The medium's native gauge coupling is **inverse**
to its stiffness and lives on a 2-form, not on the link field `a_e`. That is the opposite of the
direction R3 needs, and it is consistent with the desk check's §4 remark that in a Josephson array the
loop coupling is set independently.

### R4 — α₀ as the surface / boundary coupling (App J §1.3, lines 147–173)

*Re-derivation with every input named.* A sphere of radius R carries charge Q, so σ = Q/(4πR²). The
double layer of thickness d has potential step ΔV = σd/ε₀. App J's definition σ_s = ΔV·d (l.150, l.114)
gives

  **`σ_s = Q d² / (4π ε₀ R²)`**  (App J l.153 with ε₀ = 1).

The condition σ_s/J = α₀ = r_oct r_tet/(4πR²) (App J l.158) is `Q d²/(ε₀ J) = r_oct r_tet`: **one
equation, four inputs** (Q, d, ε₀, J). Solving for d gives d = √(J ε₀ r_oct r_tet / Q). App J's choice
Q = 1, ε₀ = 1, J = J₀ = 1, d = √(r_tet r_oct) is one point of a three-parameter family. App J says so
itself: "The choice Q=1, d=√(r_tet r_oct) is an input to this identification" (l.172–173; again
l.385–386). That sits in tension with its own l.143–145 ("no new coupling, and no new free parameter").

Two further facts:
- In Gaussian units the same step gives σ_s = Q d²/R². The "identical structure" with α₀'s 1/(4πR²)
  (l.156–160) holds only in rationalised units with ε₀ = 1.
- The neutral medium has no electric charge and no ε₀ (STIFF l.39, l.84–87), so Q has no referent and is
  STIFF's e*, a free input (CN-STIFF-05).

The first clause of the kill test (re-derive without Q, d) **fails**. This independently reproduces
Gate BC's finding as the card reports it (a two-input fit). The run re-derived it rather than citing the
ledger.

*Second clause: sphere-surface potential → window-link plaquette coupling.* σ_s is the strength of a
scalar delta-shell potential acting on |Ψ|² (App J l.108–117). Its only use as a coupling is
`H_int = σ_s ∮_{r=R}|Ψ|² dS` (l.238). That is a function of the neutral scalar's density on a sphere of
radius R = a/2 and has `∂H_int/∂a_e = 0`. App J contains no link field, no window, no plaquette and no
flux. No step in the pinned sources maps a sphere-shell potential onto the Wilson coefficient of the
window links, and the term the step would start from does not involve the field it would have to
couple. This clause **fails**.

*TANH's computed coupling, reproduced.* `g = α₀ · 4πR · tanh²(r_oct/ξ) = 0.0003697506484`, so
`α₀/g = 20.03527447` (TANH l.48, l.102). App J's "g ≈ α₀ to leading order" (l.256) is false at the ξ
App J itself uses. TANH also records that it "did not verify that σ_s/J = α₀ is itself physically
correct" (l.312–314).

### R5 — induced Maxwell term from charged matter loops

One loop, with Wilson β = 1/e²: `dβ/d ln μ = −b q²/(8π²)`, where b = 4/3 per Dirac fermion and 1/3 per
complex scalar. An induced coupling (β(Λ) = 0) is `β(m) = (b q²/8π²) ln(Λ/m)`. For one unit charge:

| species | coefficient | ln(Λ/m) for β = 10.742 | log₁₀(Λ/m) |
|---|---|---|---|
| Dirac fermion | 1/(6π²) = 0.01688686394 | 636.1168374 | 276.2620323 |
| complex scalar | 1/(24π²) = 0.004221715985 | 2544.467349 | 1105.048129 |

The card's "(1/12π²) ln(Λ/m)" is the Dirac coefficient written with ln(Λ²/m²). The pinned sources
contain no charged matter: MINIMAL §1.1 has one neutral scalar, and §1.5's vortex strings are neutral
under a field the superfluid is neutral under. The coefficient is a logarithm of a cutoff ratio that
would have to be tuned to a 276-decade hierarchy. The kill test fires.

### R6 — routes in the pinned sources not listed above

- **R6a — ICE's Josephson ratio.** Re-derived: with t = ħ²/(2ma²), U = g/a³, n = n̄/a³ and
  ξ² = ħ²/(2mgn), `E_J/E_C = 2tn̄/U = ħ² a n̄/(mg) = 2 n̄² ξ²/a²` (ratio to ICE's form = 1). At n̄ = 1
  and a = d_nn this is **10.74201848, equal to β_geom to 30 digits**. It fails all four R6 conditions:
  (i) E_J and E_C are couplings of θ and of number, with `a_e` in neither, so it fails R3's test;
  (ii) n̄ = 1 is asserted (CN-ICE-08: n̄ "not fixed by the void geometry", l.159);
  (iii) ICE's `a` is the rotor-lattice spacing, and on the void network that is the oct–tet link
  (2ξ²/a² = 28.64538262) or the per-void cell size (28.15205249), not the sphere diameter;
  (iv) the classical (3+1)D lattice coupling of a quantum rotor model, at isotropic Trotter step, is
  `K = √(E_J/E_C)` = 3.277501866, not E_J/E_C.
  This is the closest thing to a favourable R6 the sources hold, and it is a coincidence of a
  scalar-sector ratio with the target. It is not a route to β.
- **R6b — the medium's dual.** See R3. It is a 2-form with coupling 1/(8π²K): wrong form degree, one
  polarisation, inverse direction, and K is not in §1.3.
- **R6c — the network itself (the "theorem about the FCC void network" slot of §4.3).** Per plaquette
  of a 4D hypercubic complex, `a_L⁴ F²/(2e²)` with F = Φ/a_L² gives `Φ²/(2e²)`. Matching Wilson's βΦ²/2
  gives β = 1/e², and the lattice spacing cancels. On an irregular complex the matching gives
  β_p = κ_p/e² with κ_p = |\*p|/|p| a pure number of the network, and S_W(λβ) = λS_W(β). So geometry
  fixes the *relative* plaquette weights, never the overall 1/e². Compactness of `a_e ∈ (−π, π]`
  quantises charge but leaves β free (it is the parameter of the compact-U(1) phase diagram, DL l.37,
  CN-DL-06). κ_p for the void network was not computed; it is DL-BETA's lattice set-up and does not
  bear on the verdict.
- **R6d — STIFF's charitable double layer.** Re-derived: `S = ΔΦ/E_J = 2 e* m ξ/(ε₀ f ħ²)`, with
  `∂S/∂n̄ = 0`. Occupation cancels and e*/ε₀ does not. This is the only pinned expression carrying the
  added field's normalisation, and it leaves that normalisation free.
- **Recorded, not evaluated:** the scoping note (l.76–77) reports that App E.1 §3.3 writes
  J = 1/(4πα₀) = 10.74 as a monopole-action parameter. App E.1 is not pinned and was not opened.
  Whatever it says about J, R3's kill test concerns the option-B action, in which no term lets `a_e`
  see J, so no value of J becomes β.

---

## Q2 — SURVIVING ROUTES

**None.** No derivation of β exists in the pinned sources. No β is reported to 10 digits.

## Q3 — COMPARISON

No surviving β. The geometric target is shown for orientation only (card §1), against the β_c values the
card names:

| β_c (convention) | β_c | β_geom = 10.74201848 → β_geom/β_c | β_CODATA = 10.90497833 → ratio |
|---|---|---|---|
| hypercubic Z⁴, Wilson | 1.0111 | 10.62409107 | 10.78526192 |
| D4, CRIT2 card convention | 0.6150 | 17.46669672 | 17.73167207 |
| D4, Katz–Nógrádi convention | 1.2300 | 8.73334836 | 8.865836037 |
| FCC void network × time | **DL-BETA pending** | — | — |

Neither SC-DLS-1 (a surviving β = 2ξ²/a²) nor SC-DLS-3 (a surviving β ≠ 2ξ²/a²) is available.

## Q4 — EQUIVALENCE STATEMENT (recorded, not scored)

SC-DLS-1 is the same statement as **α = α₀ for the added field**: with β = 1/e² and e² = 4πα,
β = 1/(4πα₀) = 1/(4 r_oct r_tet) is α = α₀ (identity, desk check §1). A derivation surviving here would
have had to be reconciled with each of the following. The first four sentences report the card and
scoping note; those gates are not pinned and were not read or re-derived.
- **FWD:** found α₀ → α to be a selected correction map (card l.40–41); an α = α₀ link field would have to say where the 1.5 % to CODATA goes without that map.
- **STAT:** named with FWD as closing α₀ → α as a selected correction map (card l.40–41); a derivation would carry the same reconciliation burden.
- **QED:** found App E.1 §3.3's arithmetic, where J = 1/(4πα₀) is written, inconsistent (CN-QED-04, scoping l.76–77); a derivation reusing that number would have to bypass that section.
- **BC:** found App J's σ_s = α₀ a two-input fit (card l.14–16, l.68–69). This run re-derived the same fact (R4: one equation in Q, d, ε₀, J), so any R4-based derivation would contradict it.
- **TANH** (pinned, re-derived): App J's computed Josephson coupling is g = α₀/20.035, not α₀. A derivation using "the Josephson coupling = α₀" would have to say which of TANH's two objects it means. PROMOTE adds (CN-PROMOTE-12) that r_oct r_tet survives any promotion but "/π and the identification as EM coupling" do not.

## Q5 — COST COUNT (TWIST cost-table form, as the card specifies)

| Input of the DL theory (option B) | Count after this gate | Basis |
|---|---|---|
| The added compact U(1) link field `a_e` | 1 | DL construction; scoping note option B (l.58) |
| β (plaquette coupling) | **1** | this gate: SC-DLS-2 |
| The charge carrier (what couples to `a_e`) | 1 | Gate DL-MATTER; not touched here |
| The α identification (α of `a_e` = α₀, or = α_CODATA) | **1** | no route gives α = α₀; card range 0–1 |
| **Total** | **4** | |

Footnote, not a change of form: with β free, "α = α₀" amounts to choosing β = 1/(4πα₀), so a reader
who refuses to double-count would merge the last row into β, giving a total of 3. The card's form
counts it separately. The space–time anisotropy β_t/β_s, which the scoping note (l.96–97) assigns to
DL-BETA as a pre-registered convention, is not counted.

---

## §9 — ANALYST'S DISCLOSURE, SCORED ITEM BY ITEM

**Forecast versus outcome (SC-DLS-2).**

| code | forecast p | outcome |
|---|---|---|
| SC-DLS-2 | 0.70 | **occurred** |
| SC-DLS-4 | 0.15 | did not occur |
| SC-DLS-3 | 0.10 | did not occur |
| SC-DLS-1 | 0.05 | did not occur |
| SC-DLS-0 / -5 | 0 (implicit) | did not occur |

Scores: multi-class Brier **0.125** (a uniform forecast over six codes scores 0.833; 0 is best). Log
score ln 0.70 = **−0.3566749439**.

**The reasons, item by item.**
- *"R1 contradicts the construction"* — **confirmed.** Also: even when charged, the tree-level term is a
  link mass, not a plaquette term.
- *"R2 needs a polarisable charge STIFF says is absent"* — **confirmed, refined.** The medium is
  polarisable by a *number* bias (STIFF CN-STIFF-03). What kills R2 is that number is not charge under
  `a_e` in option B; converting it is R1 and yields a screening mass.
- *"R3 is the Josephson-array analogy and the analogue's loop coupling is independent of E_J"* —
  **confirmed** by the factorisation `∂²ln Z/∂J∂β = 0`. Also: the medium's own dual coupling runs
  *inverse* to its stiffness.
- *"R4 is BC's fit and a sphere-surface quantity, not a window-link one"* — **confirmed** on both
  counts, re-derived (one equation in Q, d, ε₀, J; `∂H_int/∂a_e = 0`).
- *"R5 needs matter the corpus lacks"* — **confirmed**. Matching would need ln(Λ/m) = 636 or more.
- *"The 5 % on SC-DLS-1 is the R6 slot"* — R6 held four candidates and none survived. The one numerical
  match (R6a, E_J/E_C at n̄ = 1) is in the wrong sector and depends on the length unit.
- *Interest disclosure* — noted. This replication was run by a different model in a fresh thread with
  no access to the first run. The replicator recorded no forecast before reading the card, so none is
  scored.

---

## CN-DLS NOTICES (all CONJECTURE by the same-session cap; basis in brackets)

- **CN-DLS-01** [identity + inspection] R1 closed. `J|(∂−iqA)Ψ|²` gives an A² coefficient
  `J Ψ₀² q² = q²ρ_s ≠ 0` for q ≠ 0, contradicting option B's neutrality. On the void network the
  tree-level matter term is link-local (diagonal Hessian on a girth-4 loop): a mass, not a contribution
  to β.
- **CN-DLS-02** [identity + inspection] R2 closed. In option B, Γ_medium is a-independent, so χ ≡ 0.
  The only polarisability in the pinned sources is to a number bias (STIFF CN-STIFF-03). It reaches
  `a_e` only via R1 and then gives a screening mass `JΨ₀²q²a₀²` (k⁰), not a dielectric term. The desk
  check's −χ/2 is the energy-sign convention.
- **CN-DLS-03** [identity + inspection] R3 closed. No term of MINIMAL §1.2 contains `a_e`;
  `Z = Z_GP(J)Z_W(β)`. The phase stiffness K = JΨ₀² is not fixed by §1.3, so "β = K = 2ξ²/a²" needs a
  second assertion. The medium's exact dual (KR 2-form) has coupling 1/(8π²K): inverse direction, wrong
  form degree.
- **CN-DLS-04** [identity + inspection] R4 closed. `σ_s = Q d²/(4π ε₀ R²)`; σ_s/J = α₀ is one equation
  in (Q, d, ε₀, J), and App J's Q = 1, d = √(r_tet r_oct) is one point of a three-parameter family (App
  J l.172–173 says so). The 1/(4πR²) match needs rationalised units with ε₀ = 1. `H_int = σ_s∮|Ψ|²dS`
  has `∂/∂a_e = 0`, so the sphere→window-link clause fails. g = 0.0003697506484 = α₀/20.03527447
  (TANH reproduced).
- **CN-DLS-05** [standard result + inspection] R5 closed. No charged matter in the sources. An induced
  β = 10.742 needs ln(Λ/m) = 636.1168374 (Dirac, q = 1) or 2544.467349 (complex scalar), i.e. 10²⁷⁶ or
  10¹¹⁰⁵.
- **CN-DLS-06** [identity] The target number occurs natively in one pinned source:
  `E_J/E_C = 2n̄²ξ²/a²` (ICE CN-ICE-04) equals 1/(4πα₀) = 10.74201848 exactly at n̄ = 1, a = d_nn. It is
  a ratio of the scalar sector's couplings, with `a_e` in neither. n̄ = 1 is asserted (CN-ICE-08). With
  the void-network spacing it is 28.645, and the classical coupling it maps to is √(E_J/E_C) = 3.2775.
  It is not a route to β (R6a closed).
- **CN-DLS-07** [identity + standard result] R6b, R6c and R6d closed. The network fixes only relative
  plaquette weights κ_p; S_W is homogeneous of degree 1 in β, and the 4D lattice spacing cancels in
  β = 1/e². STIFF's e*/ε₀ survives the cancellation (re-derived).
- **CN-DLS-08** [identity] **Units.** "2ξ²/a² = 10.742" holds with a = d_nn, the sphere diameter.
  That is MINIMAL's unit: r_oct and r_tet are rebuilt from Gate DL's cubic-cell coordinates as
  0.2071067812 and 0.1123724357 d_nn. With Gate DL's cubic edge the same expression is 5.371009241;
  with the oct–tet link 28.64538262; with the per-void cell size 28.15205249. The unit-free statement is
  β_geom = 1/(4πα₀) = 1/(4 r_oct r_tet). Recommendation for the ledger and DL-BETA: quote β_geom in that
  form.
- **CN-DLS-09** [interpretation] **R4 is coded "closed", not SC-DLS-4.** Card §5 offers "R4 with Q = 1
  and d = √(r_tet r_oct)" as an example of SC-DLS-4. That would apply if R4's second clause (sphere
  surface → window-link plaquette) had been shown and only Q and d remained asserted. Here the second
  clause fails structurally (`∂H_int/∂a_e = 0`), so there is no derivation to carry an asserted
  coefficient, and §8 keeps a failed kill test failed. A reader who treats the missing map as one more
  asserted coefficient would code SC-DLS-4. Card §5 makes SC-DLS-4 equivalent to SC-DLS-2 for the
  parameter count, so Q5 is unchanged either way.
- **CN-DLS-10** [identity; outside the gate's question, recorded only] The amplitude mode of the
  MINIMAL §1.2 action has `m² = Ψ₀²/ξ²`, i.e. m = Ψ₀/ξ. MINIMAL §1.4 prints 2/ξ = 0.8630, which needs
  Ψ₀ = 2 or a different normalisation. This adds to MINIMAL §4's own list of undeclared conventions and
  does not affect any route.
- **CN-DLS-11** [inspection] App J l.143–145 ("no new coupling, and no new free parameter") is
  contradicted by App J's own l.172–173 and l.385–386 (Q and d are inputs). Recorded because R4 rests on
  that section.

---

## PROTOCOL RECORD

### P.1 Source hashes (all verified before opening; `sha256sum -c`, all OK)

| File | SHA-256 | bytes |
|---|---|---|
| `audit/MINIMAL_BCT.md` | 952ad4775d1a927df7983b1e2fee57e39e32990674eab882a9d26fb639d3c77b | 6461 |
| `audit/gates/DL/gate_DL_RESULT.md` | 3eff786202696bd1613187bdb35c3ac2b9a9918a27138995999b6a90d3c128b4 | 18115 |
| `audit/gates/DL/gate_DL_step0_network.py` | 7935f7e7a8a784c03c3465349a539d3fce95665957009a6b88d4b9b93874a4ee | 4250 |
| `audit/gates/DL/gate_DL_step1_mass.py` | 6e082574e208e849facf18cd1fc9d9240e718dd1902f92e2aed364c3fff8c93d | 2301 |
| `audit/gates/STIFF/STIFF_RESULT.md` | 1d0be8691c9c49db3489d567d238d2f29591ef722356cfcc8b7f0a021ceee672 | 20811 |
| `audit/gates/ICE/gate_ICE_RESULT.md` | b458a3c1ed8bbd323db483dcb05187b70d702a40bd241e5d76c831ad4d8d11bc | 17804 |
| `audit/gates/PROMOTE/gate_PROMOTE_result.md` | 761c3bdf17f0c4cb1e9c3cd9fb7e75f428a68fedbe0e63c1468534552c40dca2 | 7205 |
| `audit/gates/TANH/gate_TANH_RESULT.md` | 090ede6120d3bb4210e26c3d6ed5db50cdb68d4c2f39cfa0bf43419fc37858eb | 21613 |
| `tex/BCT_Appendix_J_SphereAction.tex` | ad9ecd0c6ddb899a57bee0e1445e7c8cb70067deed2f9ee4fd0f561c633432df | 19154 |
| `audit/scoping/DL_scoping_2026-11-12.md` | fede02d1514563e11d30c05aa136a416b38cdd40ab1d6af15e95d7b8009f8a65 (from PREREG) | 10249 |
| `audit/gates/DLSTIFF/dls_deskcheck.py` | 332e2d1275196c5720d78fcce6e0364d567c3281476d4795c032010e5989bde5 | 3972 |
| `audit/gates/gate_DLSTIFF_prompt.md` (in-tree copy) | 294da0f50c5d740956bb0b3d64871f580a00f454a0f541701467bba47ee48e21 | 16033 |
| `audit/gates/PREREG_20261112_DLSTIFF.sha256` (in-tree copy) | 682effc99bc12bfee62de437080ccc9054d9ea0e84ecd4de1d62da3fc9dcb696 | 282 |

### P.2 Deviations from card §11 (all on the replication prompt's instruction, or immaterial)

1. **Depth-1 fetch of the single pre-registration commit instead of `git clone`** (replication prompt
   step 2). HEAD~1 is not available; the §4.1 hashes establish the sources.
2. The card pins sources "at 9114b6e, scoping note and card added by the pre-registration commit". This
   run read them at `9993a23`. Every hash matches the card, so the content is identical.
3. `sha256sum` used for the card's `shasum -a 256`: the same algorithm.
4. Order of the PREREG check: the card's digest was compared with the replication prompt's expected value
   before the card was read. The PREREG file (itself matching its expected digest) was opened in the same
   step as the card, and its line for the card matches.
5. Deliverable placed under `audit/gates/DLSTIFF/REP2/`, not `audit/gates/DLSTIFF/` (replication prompt
   step 5).
6. Settings ("Search and reference past chats", "Generate memory from chats") are user-side. This
   session reported Claude's memory as not enabled, and no past-chat tool was used.

### P.3 Contamination statement

- **Read:** the card, the PREREG record, `dls_deskcheck.py`, and the eleven §4.1 files. Nothing else
  from the repository was opened.
- **Commands that touched other paths:**
  - `ls audit/gates/DLSTIFF/` showed only `dls_deskcheck.py`, so no other file under that directory
    exists to report.
  - `git show --stat` printed four unrelated file *paths* (`tex/BCT_Monograph_PLB.tex`,
    `tex/BCT_OneMedium_JournalEdition_v2.txt`, `tex/BCT_PRL_Letter.tex`,
    `tools/download_zenodo_BCT_v6.py`), no contents.
- **Project knowledge base:** not opened. The session context listed Project document *titles*
  automatically, among them `claude/gate_DLSTIFF_prompt.md` and `claude/DL_scoping_2026-11-12.md`. None
  was read, and `project_search` was not used. No title in the visible list names a DL-STIFF result.
- **Past chats and memory:** not used.
- **Web:** none beyond the three raw.githubusercontent.com fetches and the git fetch of the pinned
  commit.
- **First run:** not sought, not compared.
- **Standard results used as machinery** (not computed here):
  - one-loop QED β-function coefficients (b = 4/3 Dirac, 1/3 complex scalar);
  - quantum-rotor → classical XY Trotter/Villain mapping;
  - XY ↔ Kalb–Ramond duality (as recorded in PROMOTE);
  - continuum ↔ Wilson matching on a 4D hypercubic lattice.

### P.4 Unpinned pointers recorded and not followed

- **MINIMAL_BCT:** Apps D, E, J; Gates RANK, QP, N, G′, LINK, C1, MAD, PRED2, XI; census INV-0120;
  CN-FWD-02, CN-TANH-09, CN-Ψ2-18; Barceló–Liberati–Visser gr-qc/0011026.
- **DL RESULT:** `audit/gates/LINK/`; the DL prompt; base commit `dfb2591`.
- **STIFF:** `stiff_step0_dipole.py`, `PROMPT_asrun.md`.
- **ICE:** `net_ice.py`, `ratio_ice.py`, `gate_ICE_prompt_asrun.md`.
- **PROMOTE:** `gate_PROMOTE_prompt.md`.
- **TANH:** `scripts/repro_step0.py`, `repro_step1_steelman.py`, `repro_step34_downstream.py`,
  `README_MISSING.md`; Appendices Vol 1/2 PDFs.
- **App J:** `audit/desk/appJ_source.md`, `audit/gates/BUBBLE_BELLS/`; Apps D, E.2, G, I, JH, K.
- **Scoping note:** App E.1 §3.3 (see R6, "recorded, not evaluated"); Gates QED (CN-QED-04), CRIT2, LATT,
  QED-DERIV (T2), TWIST, FWD, STAT; `NEXT.md`.
- **Card:** Gates BC and QED (chat-side), FWD, STAT, LOG, SPECTRUM, RATIO, CRIT2, TWIST.

### P.5 Files in this deliverable (`audit/gates/DLSTIFF/REP2/`)

| File | SHA-256 | role |
|---|---|---|
| `gate_DLSTIFF_RESULT.md` | see `SHA256SUMS` | this result |
| `dls_rep2_routes.py` | d0188d22c66fc2e8e9da23de63af28fe971ac5f7d6fd5269020324f378874330 | route ledger: every kill test computed |
| `dls_rep2_routes_output.txt` | 2fe2480ffd82216379f75e583c75f0a86d9f27f651b2e662e70ef943f2a06fc9 | its output (deterministic; two runs, same digest) |
| `dls_deskcheck_output.txt` | de83e05991482eb7aae1807925f613b9affb8f9c9bd206fdbf6b4241357052cb | card §7 script, rerun; reproduces §7 |
| `dl_step0_rerun_output.txt` | c55ec97ef398fc389f3b8f73ef55fde101ef7d3b132cf7aefc53e73ef2121de8 | Gate DL network, rerun (b₁ = 5/primitive cell, S = I/3) |
| `dl_step1_rerun_output.txt` | f1703f0e2a55de09061267f38fa96c9c89af46a6348a8e13e6ee4309b56d9b1d | Gate DL mass fork, rerun |
| `REP2_prompt_asrun.md` | see `SHA256SUMS` | the replication prompt as received |
| `SHA256SUMS` | — | digests of all of the above |

Reproduce: `python3 -I dls_rep2_routes.py | sha256sum` should print `2fe2480f…06fc9` with sympy 1.14.0
and mpmath 1.3.0.

---

## WHAT THIS RUN DID NOT ESTABLISH

- It did not compute β_c on the void network (DL-BETA), the Hodge weights κ_p, or the lattice-Maxwell
  band structure.
- It did not decide what carries the charge of `a_e` (DL-MATTER), or anything about α beyond recording
  the Q4 equivalence.
- It did not read FWD, STAT, QED or BC. Their Q4 sentences report the card and scoping note; only BC's
  finding was independently re-derived (via R4).
- It did not consider routes outside the pinned sources (card §4.5).
- It does not refute the void geometry: r_oct, r_tet, α₀, ξ, the network, its isotropy and b₁ = 5
  stand. The result is about one coupling of an added field.

---

## PLAIN-LANGUAGE SUMMARY

The proposed DL theory adds a new electromagnetic-like field that lives on the "windows" between the
gaps in the sphere packing. The superfluid medium is deliberately left uncharged under that field, which
is what keeps the field's light massless. The question was whether the medium or the geometry fixes how
strongly that field couples (β), or whether β is simply a number one has to choose.

It is a number one has to choose. Because the medium is uncharged, the field and the medium do not
interact at all, so the medium cannot set the field's coupling. Every proposed way around this either
makes the medium charged, which gives the light a mass and defeats the purpose, or simply declares the
two to be equal. The appealing value 10.74 (equivalent to α = α₀) does appear in the sources, but as a
ratio of the medium's own tunnelling and interaction energies at an assumed occupation of one particle
per void, and only in one particular choice of length unit.

The DL theory therefore has at least one free coupling, and four inputs in all.
