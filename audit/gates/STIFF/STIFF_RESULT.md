# GATE STIFF — RESULT

**Is the double-layer stiffness (dipole density / potential jump) fixed by the packing, or a free input?**

Cold Ledger gate. Run 15 September 2026. Hypothetical-construction gate (audits one isolated brick,
not BCT-as-written).

---

## DIGEST / CONTAMINATION

- **Digest.** The gate prompt reached this session **pasted** (delivered as an in-context document),
  not as a commit-pinned `raw.githubusercontent.com` file. Per §0.1 I therefore **claim no SHA-256
  digest** and record that the pre-registration hash cannot be certified from this run.
- **Contamination statement.** I did **not** read any `gate-*` memory summary, any
  `audit/gates/*/` deliverable (specifically not ICE, DL, or LINK), `audit/notes/`, BCT-X/Sandbox,
  or the 9–15 Sep 2026 threads. No ICE/DL/LINK number (E_J, a charging or stiffness ratio,
  an occupation threshold, `r = 2 n̄²(ξ/a)²`, `b₁`, the girth) reached this session. I had general
  project context (that BCT is a GP-condensate-on-a-void-lattice programme) but no prior-gate
  physics. `audit/MINIMAL_BCT.md` was **not** available locally in this session, so field content
  and constants (m, g, ξ, α₀, n̄) were carried **symbolically** from standard GP physics rather
  than read; if the corpus fixes n̄ or a specific window geometry differently, the symbolic
  derivation below is unaffected (the verdict turns on symmetry and component-count, not on values).
- The two inherited benchmark facts (compact-U(1)-on-windows; soft-by-default / hard-only-if-stiff)
  were **re-derived**, not trusted — see §2 and §4-note.

---

## SEARCH-SPACE COVERAGE (the double-layer-object build — §1 first)

A "double layer" is a **dipole sheet**: a surface carrying a dipole moment per unit area
`P = ∫ z ρ(z) dz`, i.e. a genuine charge `+σ` on one face and `−σ` on the other across the window.
For P to be a well-defined, nonzero, geometry-fixed object there must be (i) a genuine charge density
ρ and (ii) an **odd** (sign-changing across the window plane) separation of it. I enumerated every
candidate charge a neutral single-component GP condensate could offer:

| # | Candidate charge for the layer | Present? | Gives an **odd** (dipole) profile fixed by packing? |
|---|--------------------------------|----------|------------------------------------------------------|
| a | Genuine **electric** charge | **No** — the condensate is neutral; the base theory has no gauge field, no e, no ε₀ | — (there is no ρ at all) |
| b | **Number / U(1)-Noether** charge δn=|ψ|²−n̄ | Yes | **No** — for a reflection-symmetric window V(z)=V(−z) the GP ground state ψ is real, nodeless, unique ⇒ n(z) is **even** ⇒ transverse dipole `∫ z δn dz = 0` |
| c | **Smoluchowski surface dipole** (as in a neutral metal's work-function) | **No** — this needs *two* charge distributions with different profiles (electrons vs ion cores); a single complex scalar has only one profile and no independent charged scaffold to be displaced against | — |
| d | **Phase-gradient / current** dipole (superflow through the window) | Only in a *driven / biased* state | **No** — a persistent current or a void-to-void bias is a boundary condition put in by hand, not an equilibrium packing feature (see numeric §B) |
| e | **Spontaneous parity-breaking** dipole (a ferroelectric-like instability) | Not exhibited by the symmetric GP/Bose–Hubbard ground state | **No / conjecture** — no such instability arises for the symmetric lattice; and were one tuned into existence its magnitude would be set by the tuning coupling, not by ξ/a |

Every route to a genuine, geometry-fixed nonzero P fails at the object level. The load-bearing one is
(b): the only local charge the neutral condensate actually has is **number**, and its window profile
is **even**, so its dipole moment is **identically zero by symmetry**. This is proven, not fitted.

---

## VERDICT (first)

**Primary: `SC-STIFF-5`.** A neutral GP condensate hosts **no genuine, well-defined double layer** on
its void windows. The only local charge is particle number (the U(1)-Noether charge), not electric
charge; and for a reflection-symmetric window the number-density perturbation is **even**, so the
surface dipole density is **P = 0 by symmetry** — not small, not soft, but *identically absent*.
"Double layer" is a **borrowed word**: it silently imports the electrolyte/electrode setting's genuine
ions and symmetry-breaking electrode potential, neither of which the neutral single-component
condensate possesses. With P undefined/zero, the potential jump `ΔΦ = P/ε₀` and hence the stiffness
`S = ΔΦ/E_J` are undefined. **The premise of the window-photon route is unfounded at the root.**

**Fallback under the most charitable reading: `SC-STIFF-1`.** If one insists on the Josephson-junction
reading — "the window is a junction between two voids and the layer is the number-imbalance across
it" — then (i) a nonzero imbalance/dipole exists **only** when a void-to-void bias is imposed by hand
(numeric §B: `p` is linear in the bias and vanishes with it), so any nonzero P carries a **free input**
(the bias / an assigned effective charge e*), not a pure function of ξ/a; and (ii) the only genuine
dimensionless "stiffness" is then the charging ratio `E_C/E_J`, which is **the same object** as the
GP superfluid-vs-Mott/ice control, not a new lever (§2).

**Either way: ICE's `SC-ICE-2` is NOT upgraded to `SC-ICE-3`.** The masslessness of a two-polarisation
photon on this lattice would still be **bought, not derived**; the link-variable routes to a massless
two-polarisation photon remain **exhausted — here, at the root.**

*No overclaim in the other direction: this does not refute the void geometry. The packing, the
octet-truss network, α₀, and ξ stand untouched. What fails is specifically the claim that a
geometry-fixed **charge separation** exists to be made stiff.*

---

## §1 — THE PHYSICAL-OBJECT DETERMINATION (P, or the ill-defined finding)

**What is being separated?** In the GP energy functional
`E[ψ] = ∫ d³r [ (ℏ²/2m)|∇ψ|² + (g/2)(|ψ|²−n̄)² ]`, the field ψ = √n e^{iθ} carries one local density
n = |ψ|² and one phase θ. The continuous symmetry is the **global phase** θ → θ+const; its Noether
charge is **particle number** `Q = ∫(n−n̄)`. There is no electromagnetic gauge field, no elementary
electric charge, no ε₀, and no long-range Coulomb interaction (the GP interaction `g|ψ|⁴` is contact,
i.e. short-range). So the *only* candidate "charge" to build a layer from is the number deviation δn.

**Is its separation a dipole?** For a symmetric window (the physical case: identical voids either side
of the aperture, potential V(z)=V(−z) along the window axis), the GP ground state is real and nodeless
(the standard Perron–Frobenius uniqueness for the lowest state of `−∇² + V + g|ψ|²`), hence **even**:
n(z) = n(−z). The transverse dipole moment is therefore

  `p = ∫ z (n(z) − n̄) dz = 0`   (odd integrand).

This is a **theorem**, not a numerical coincidence. Numerically (script `stiff_step0_dipole.py`,
imaginary-time GP in a symmetric throat potential): evenness residual `max|n−flip(n)|/max n ≈ 4.5×10⁻³`
(convergence-limited) while the dipole integral itself is `p = −2.3×10⁻⁹` — zero to machine level. The
window's healing physics does redistribute density (a symmetric **depletion** in the throat over a
length ξ), but a symmetric depletion is a **monopole-type** perturbation, not a dipole sheet. There is
no double layer.

**The Smoluchowski disqualifier of the "neutral things still have surface dipoles" objection.** A
neutral *metal* has a real surface dipole because it has **two** charge distributions — delocalised
electrons that spill outward past the localised ion cores — whose different profiles make a dipole.
The GP condensate is **one** complex scalar; there is no second, independently-profiled charged
component (the void lattice is built *of* the condensate's own structure, not an external charged
scaffold), so the Smoluchowski mechanism has nothing to work with. This is the cleanest structural
reason P = 0 rather than merely small.

**Conclusion (§1):** the object is **ill-defined / absent** ⇒ this is the `SC-STIFF-5` condition.

---

## §2 — THE STIFFNESS S, AND WHETHER IT IS THE GP CHARGING RATIO

Because ΔΦ = P/ε₀ is undefined (P = 0, and there is no ε₀ in the theory), S = ΔΦ/E_J is undefined as
written. The only way to give "stiffness" any meaning in the neutral condensate is to reinterpret the
window as a **Josephson junction** between two number-reservoirs (the two voids). Then two scales are
genuine and first-principles:

- **Josephson coupling** `E_J` — the phase-rigidity across the throat, extracted here from the energy
  vs relative phase `E(φ) = E₀ − E_J cos φ` (numeric §C).
- **Charging energy** `E_C` — the cost to move one unit of number across the junction, set by the
  interaction and the throat capacity, `E_C ~ g / (throat volume)`.

Their **ratio `E_C/E_J`** is the standard control parameter of the Josephson-junction-array /
Bose–Hubbard phase diagram: `E_C/E_J` small ⇒ phase-coherent **superfluid** (a gapless phonon);
`E_C/E_J` large ⇒ number-**pinned** Mott/ice (charge blockaded). **This is exactly the
superfluid-vs-Mott/ice control** — i.e. the same on-site charging ratio that already decides the
phase. So: the "stiffness," to the extent it means anything here, is **the SAME object** as the GP
charging ratio, **not an independent lever.** The proposed "stiff double layer" is just the
large-`E_C/E_J` regime of a quantity that already exists — it is not a new degree of freedom that could
have been geometry-fixed on its own.

A crucial re-derivation of the inherited "hard-only-if-stiff" fact, with the sign made explicit:
"stiff" (large `E_C/E_J`) does pin number and *does* impose a hard constraint — but the deep-`E_C`
limit is the **gapped, trivially-ordered/confined** regime, **not** the gapless Coulomb phase. A
gapless emergent photon (the quantum-ice mechanism) lives in an **intermediate** window: hard enough
to define the constrained ("ice") manifold, yet with ring-exchange strong enough to deconfine. So
"stiffer is better" is **backwards** — maximal stiffness kills the photon by gapping/confining. Even
granting a knob, the target is a fine-tuned interval, not a limit; and there is no geometric argument
placing `E_C/E_J` in that interval. (This is the re-derivation of benchmark fact (ii); it stands.)

---

## §3 — THE GEOMETRY-FIXED TEST (explicit cancellation)

Write the would-be layer's dipole density with every input explicit. The most charitable construction
is: charge-separation length = healing length ξ; surface charge = an effective charge e* times the
condensate density n̄ times ξ. Then

  `P ~ e* · n̄ · ξ`,  `ΔΦ = P/ε₀ ~ e* n̄ ξ / ε₀`,  `E_J ~ (ℏ²/2m) n̄ · f(ξ/a, network)`,

  `S = ΔΦ/E_J ~ (e*/ε₀) · (2m/ℏ²) · ξ / f(ξ/a, network)`.

Run the cancellation, exactly as ICE ran it for the GP stiffness J:

- **n̄ cancels** (it multiplies both P and E_J). Good — occupation drops out.
- **But `e*/ε₀` does NOT cancel.** There is no electric charge and no ε₀ in the neutral condensate,
  so e* is an **assigned quantum** put in by hand, and ε₀ is imported from the electrostatic analogy.
  This factor is **not a function of ξ/a or any network number.**

**A free input survives the cancellation: the effective charge e* (with ε₀).** By the corpus's own
product-vs-ratio test, the geometry does **not** do the work — a fresh dimensionful number (the charge
assignment) decides the stiffness. This is the `SC-STIFF-1` condition *for the charitable reading*.
And note this test only even runs after pretending P ≠ 0; the honest §1 result is that P = 0, which is
the deeper `SC-STIFF-5` failure that makes the whole test moot.

---

## §4 — CONDITIONAL DECONFINEMENT / POLARISATIONS

**Not reached.** §3 does not return "geometry-fixed **and** stiff": it returns either P = 0 (no
object, `SC-STIFF-5`) or a surviving free charge (`SC-STIFF-1`). The gate's own gating condition for
§4 ("only if geometry-fixed AND stiff") is not met, so no deconfinement or polarisation claim is made,
and **no scalar-phonon-false-positive question arises** (there is no candidate transverse vector to
test). This gate therefore does **not** establish deconfinement or a two-polarisation photon — it
removes the object that would have been their prerequisite.

---

## §5 — PARAMETER AUDIT

After this gate, what remains a free input (i.e. not a pure function of ξ/a and the network)?

- **The very existence of a separable charge.** The premise "there is a double layer" is not merely
  under-determined — under the honest reading it is **false** (P = 0 by symmetry). This is not a
  parameter cost; it is a missing object.
- **Under the charitable Josephson reading only:** an **effective charge e*** (with ε₀) and the
  **placement of `E_C/E_J`** in the narrow Coulomb-phase interval. Both are free inputs. The
  occupation n̄ is **not** a residual cost — it cancels.
- **Deconfinement** is not even assessable, because the constraint whose deconfinement one would test
  does not exist.

Nothing is derived to be free-parameter-free here; the honest statement is that the route has **no
object to make geometry-fixed.**

---

## §6 — THE STEELMAN (required)

*Strongest case for a geometry-fixed photon:* Take the charge-separation length to be the healing
length ξ (packing-fixed), the surface charge to be set by the condensate density n̄ (packing-fixed),
so `P ~ e* n̄ ξ` and, after n̄ cancels in `S = ΔΦ/E_J`, `S` is a pure function of ξ/a and the window
geometry. If ξ/a lands S in the stiff regime, the octet truss inherits a hard ice-rule constraint;
the girth-short loops carry strong ring-exchange; in 3+1D compact U(1) a genuine deconfined Coulomb
phase exists (unlike 2+1D Polyakov), so the constrained truss could sit in a Coulomb phase with a
massless, two-isotropic-polarisation photon (O_h ⇒ response ∝ δ_ij) — a geometry-fixed photon,
upgrading `SC-ICE-2` to `SC-ICE-3`.

*Where it breaks — the exact brick.* The steelman's second premise, **"the surface charge is set by
the condensate density,"** conflates **number density** with a **separable electric charge**. The
condensate density n̄ is a *scalar* magnitude, not a signed charge that can be split `+σ / −σ` across a
sheet; splitting it requires either (α) a genuine electric charge e* — which the neutral theory does
not contain and which §3 shows does not cancel (free input), or (β) an **odd** number-density profile
across the window — which reflection symmetry **forbids** in the ground state (§1, P = 0). The
steelman needs a charge to separate and a symmetry-breaking to separate it oddly; the neutral,
single-component, symmetric condensate supplies **neither**. So the steelman does **not** succeed, and
the unfilled brick it exposes is precisely the one named: *there is no genuine separable charge on the
window at all.* (Because that first brick fails, the downstream bricks — this lattice deconfining
rather than confining; the photon being a true vector — are not reached.)

---

## CN-STIFF NOTICES

- **CN-STIFF-01 — PROVEN.** For a reflection-symmetric void window, the GP ground state is even, so the
  transverse dipole moment of the number-charge vanishes identically: `∫ z δn dz = 0`. The neutral
  condensate's only local charge (number) forms **no dipole sheet**. (Analytic + numeric, `p ≈ 10⁻⁹`.)
- **CN-STIFF-02 — PROVEN.** A single complex scalar has one charged profile and no independent charged
  scaffold, so the Smoluchowski (two-component) surface-dipole mechanism does not apply — P = 0 is
  structural, not merely small.
- **CN-STIFF-03 — PROVEN (numeric).** A nonzero window dipole appears only under an **imposed** void-to-void
  bias, linearly in the bias, vanishing with it: any nonzero P is bias-fixed / hand-input, not
  packing-fixed.
- **CN-STIFF-04 — ASSERTED (standard, re-derived).** The only well-defined dimensionless "stiffness" in
  the neutral condensate is the Josephson charging ratio `E_C/E_J`, which **is** the GP
  superfluid-vs-Mott/ice control — not an independent lever. The gapless emergent photon requires an
  *intermediate* value, so maximal stiffness confines/gaps: "stiffer is better" is backwards.
- **CN-STIFF-05 — ASSERTED.** Under the charitable Josephson reading, the charitable P forces an
  effective charge e* (with ε₀) that does not cancel; occupation n̄ **does** cancel. A free charge
  input survives ⇒ the fallback `SC-STIFF-1`.
- **CN-STIFF-06 — CONJECTURE.** No spontaneous parity-breaking (ferroelectric-like) dipole instability
  arises for the physical GP/Bose–Hubbard parameter range on the symmetric lattice; if one were tuned
  into existence, its magnitude would be set by the tuning coupling, not by ξ/a. (Argued, not
  exhaustively excluded over all couplings.)
- **CN-STIFF-07 — FALSIFIED.** The premise "a neutral condensate hosts a genuine double layer whose
  dipole density is geometry-fixed" is falsified at the object level: there is no odd charge to
  separate.

---

## §0.5 (reproduced verbatim)

> This audits **one isolated brick** of a hypothetical new construction, not a repair of the written
> theory. The corpus is a single S¹ complex scalar; the constrained-U(1)-on-windows theory is new,
> and this gate asks only whether its stiffness is bought or free. A verdict of "geometry-fixed,
> stiff, deconfined" does **not** vindicate BCT-as-written — it upgrades exactly one earlier
> parameter-cost route (ICE's `SC-ICE-2`) to a geometry-fixed one, identifying a *new theory worth
> writing down*, which would then still owe, separately and later, (1) that the constrained octet
> truss is genuinely deconfined for this lattice (not merely by pyrochlore analogy), (2) the
> photon's coupling to matter, (3) reproduction of QED, and (4) a derivation of α. A verdict of
> "free input," "geometry-fixed but soft," "confined," or "no genuine double layer" means the
> stiffness cannot be derived from packing, and — with Gate LINK (massive), Gate DL (no Higgs mass),
> and Gate ICE (soft → single phonon; hard only at a parameter cost) — the audited link-variable
> routes to a massless two-polarisation photon on the BCT lattice **remain exhausted.** A verdict of
> "needs a tuned charge/occupation" is the same epistemic situation the census closed for any
> dimensionful input fixed after the fact.

## §0.6 (reproduced verbatim)

> This gate decides whether the one brick Gate ICE isolated — that a genuine double layer is a hard,
> stiff constraint fixed by geometry — can be laid. It does not decide whether the resulting photon
> couples correctly to matter, reproduces QED, or yields α, nor even (on its own) whether the
> constrained lattice is deconfined rather than confined; each is a separate later gate or a
> conditional sub-step here. A "geometry-fixed, stiff, deconfined" verdict is the first route in the
> whole audit to clear the representation wall (G′) **without a free parameter** — significant, but
> only the beginning of a new theory, not a vindication of BCT. A "free input," "geometry-fixed but
> soft," "confined," or "no genuine double layer" verdict does not refute the void geometry (the
> packing, the network, α₀, ξ stand) — it means the stiffness needed for a photon cannot be built
> from the packing, and the link-variable routes are exhausted.

---

## WHAT THIS GATE DID NOT ESTABLISH

- It did **not** prove QED, matter coupling, or a value of α (out of scope).
- It did **not** reach §4, so it establishes **nothing** about whether the (nonexistent) constrained
  theory would deconfine or confine, and nothing about photon polarisation count or isotropy.
- It did **not** refute the void geometry itself: the packing, the octet-truss network, α₀, and ξ are
  untouched. The negative result is specific — there is no geometry-fixed **charge separation** on the
  windows to make "stiff."
- The `SC-STIFF-6/CONJECTURE` (no spontaneous dipole instability) is argued, not exhaustively proven
  across all couplings; a dedicated instability analysis could sharpen it, though it would not change
  the verdict (a tuned instability is still a free input, `SC-STIFF-1`).

---

*Scripts: `stiff_step0_dipole.py` (deterministic). As-run prompt: `PROMPT_asrun.md`.*
*Run 15 September 2026. Outcome matches a defined stop condition (`SC-STIFF-5`, fallback `SC-STIFF-1`);
no prompt defect recorded.*
