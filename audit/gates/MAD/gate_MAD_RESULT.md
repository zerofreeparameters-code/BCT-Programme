# GATE MAD — RESULT
## Does BCT derive quantum mechanics, or restate it via Madelung?

**Cold Ledger gate. Run 14 September 2026, one thread.**
**Model:** Claude Fable 5.1 (Anthropic).
**Verdict: SC-MAD-1.** Every adjudicable quantum claim in the corpus falls in bin A, C or D. Bin B is empty.

---

## 0. Digest, quarantine, contamination

**Digest.** Prompt received as a commit-pinned `raw.githubusercontent.com` URL
(`aa709432f55b5424435551ceafea93398776439e`, `audit/gates/gate_MAD_prompt.md`).
`curl` to disk, then `sha256sum`:

```
dc6106cd33cad38c23075a3c1dd12f802a0ef84487af7186db4b843464f741cd  gate.md   (7499 bytes)
```

Byte-exact match to the pre-registered digest and size. Hashed before reading. The same
file in the checkout at the pinned commit hashes identically. As-run copy in this folder.

**Contamination statement.** The Cold Ledger auto-loaded into the session and was read in
full before the fetch: the audit-findings file (closed sectors G′, PH, N, F/Fb, T, IG, U″,
SCR, BZ, QP, AM, SYM, FWD, STAT, KND, OP, R2, P, J, YM, LINK, plus the JH/BB2 repo-sweep
notes), the RANK/MP/PRED summary, and the ways-of-working file. None states an expected MAD
outcome; `audit/NEXT.md` (repo and project mount) lists MAD as queued with no verdict. One
prior-knowledge item was in view before I opened Appendix JH: the ledger's note that JH gives
the interior an S² order parameter. The 9–11 Sep threads, BCT-X / Sandbox TOP, and the
concurrent LINK thread were not consulted.

**External literature (§0.3).** Permitted and used. §8 lists exactly what was opened.

---

## 1. Search-space coverage (before any other number)

**Repository.** `git clone` at `aa709432`. Tarball via `git archive --format=tar HEAD`:
SHA-256 `55af6be6a7a1e1cc8b876a94442a16faf42cf8f289d02dea4e49612ec2214943`, 48 926 720 bytes.
**134 `.tex` files, 26 at the tree root outside `tex/`.** 210 files in total. Matches §0.5.

**Mount (`/mnt/project`, 95 files).** Every file typed with `file(1)`:

| type | count | handling | pages covered |
|---|---|---|---|
| ZIP archives (page JPEGs + `.txt` layers + `manifest.json`) | **33** | `unzip` of `*.txt` | 387 pages; JPEG count = txt count in every archive (100% text-layer coverage); 7 near-empty pages, all in the *Accidentally Solved* book files |
| true PDFs | **14** | `pdftotext -layout` | 92 pages |
| raw UTF-8 text reported as `data` | **2** | `cp` (Appendices Vol 1 Part 1: 849 709 B; Part 2: 713 071 B) | no page structure; whole file |
| `.tex`, `.md`, `.py`, `.html`, images | remainder | copied / not text | — |

Matches §0.5 exactly. Assembled corpus text: 4 535 414 bytes.

**Step 0 search, stated.** Case-insensitive grep over repo `tex/` + root `.tex`/`.md` + all
mount text for: Madelung, Schr, quantum potential, Bohm, Nelson, commutator, Planck's constant,
`\hbar`, Born rule, Hilbert, entangle, superposition, wave-particle, measurement problem,
collapse, Pauli, half-integer, spin-1/2, uncertainty, de Broglie, "derive … quantum
mechanics", "quantum mechanics". Findings on the search itself:

- 30 of 38 "Madelung" hits are the **Madelung constant** (electrostatics, App D.0), not the
  transformation. The transformation appears in Letter 60, Letter 20, App AZ6, One Medium §7,
  Letters Vol 2b p.16 (Letter 26).
- "quantum potential" appears **nowhere** in the corpus. "Nelson" appears only as Nelson–Barr.
- "Born rule" appears in exactly one document (Letter 72), which defers it to an appendix
  (JH6) that does not exist in the tree.
- "Hilbert space" as a *derived* object appears nowhere; as a declared *input* it appears in
  One Medium §2 and §12.

---

## 2. Verdict, stated first

**SC-MAD-1.** BCT's quantum sector is inherited from the condensate axiom (bin A, where
correctly attributed), restated (bin C), or presented as analogy (bin D). No claim uses
BCT-specific structure to yield something Madelung/Bohm/Nelson hydrodynamics does not.

The corpus's own flagship synthesis already says this. One Medium (Journal Edition, July
2026), §2 "Scope statement (read first)":

> What is not derived: quantum mechanics itself. The Gross–Pitaevskii description of the OHC
> is a quantum object from its first line; ℏ, the superposition principle and the
> Hilbert-space postulates are inputs.

and §12 "Honest open problems", item (i): the quantum formalism "is the outermost frontier."
This statement is correct. The Letters and appendices enumerated in §3 below contradict it,
and the contradiction is the main corpus-consistency finding of this gate.

The nearest miss to bin B is Letter 72's collapse threshold N_c = 1/α₀ (row 4 in §5). It uses
a BCT-specific input and produces a number the baseline does not; it is not in bin B because
the step from Σα₀ ≥ 1 to "H must snap" is asserted, not derived, and because the state it
acts on — a superposition of two classical field configurations — is undefined for the
c-number GP field the corpus works with. §9 states what would move it.

---

## 3. Step 0 — enumeration of QM claims (location · claim quoted · derived from · own tier)

| # | location | claim (verbatim) | derived from | tier its own document assigns |
|---|---|---|---|---|
| 1a | `tex/BCT_Appendix_JH_FINAL.tex` L284–290 (also `_JH.tex`, `_JH (1).tex`, `_JH_GRRRRRRRR.tex`) | "The energy spectrum E_N = N·ε₀ with N ∈ ℤ provides energy quantisation without axiom." | E_N ∝ N_H citing Faddeev–Niemi [Hopfion1, Hopfion2] | "Topological, exact" (summary table) |
| 1b | same, L290–301 | "[x̂,p̂] = iħ follows from the Hopf fibration structure: if the position operator x̂ is associated with the S² base and the momentum operator p̂ with the S¹ fibre, the non-commutativity of the fibre bundle is precisely the Dirac quantisation condition. The commutator is not postulated in BCT; it is a consequence of the N_H=1 topology." | Hopf fibration | "Topological, exact" |
| 2 | same, L303–325 | "A particle that threads the OHC interior traverses one Hopf fibre S¹, accumulating a phase of π (not 2π) per traversal … half-integer spin is not a separate input." | SU(2)→SO(3) double cover | exact |
| 3 | same, L210–233 | "the interior field must carry exactly N_H=1 Hopf winding to satisfy [the surface-flux condition]… the N_H=0 solution cannot satisfy this boundary flux condition without discontinuity; the N_H=1 hopfion is the unique smooth solution." | Josephson boundary condition | exact |
| 4 | `tex/BCT_Letter72_MeasurementProblem.tex` and `tex/BCT_Letter72_Measurement.tex` (two variants, same date) | "We resolve the quantum measurement problem … Collapse … occurs when the system's Josephson coupling … reaches Σα₀ ≥ 1, requiring entanglement with N_c = 1/α₀ ≈ 135 OHC Planck spheres." Also: "The Born rule … follows from the D4 symmetry of the OHC … A full derivation … is deferred to Appendix JH6." Also (variant 2): "Why is ħ quantised? Because H ∈ ℤ … [x̂,p̂] = iħ follows from Hopf fibration topology, not from postulate." | α₀ = r_oct r_tet/π; H ∈ ℤ | "Theorem"; "exact" (Letter 75 repeats "(Letter 72, exact)") |
| 5 | `BCT_Letter254_Entanglement.tex` (root) | "An entangled pair … is a single Hopf charge configuration … The configuration's geometry is fixed at creation, not at measurement … A single extended Hopf configuration does reproduce [the Bell violations], exactly." And: "cos(π/4) = 1/(2r_oct+1) … The Tsirelson bound follows." | Hopf charge conservation; r_oct | PROVEN (algebraic identity) |
| 6 | `tex/BCT_Letter64.tex` | "quantum mechanics emerges from non-Markovian OHC stochastics" (Theorem I); classicality from topological redundancy (Theorem II). | Bogoliubov dispersion; Hopf integral non-locality | "theorems", zero free parameters |
| 7 | `tex/BCT_Letter81_TwoTheorems.tex`, `Letter78`, `Appendix_KA4` | "The n-th OHC mode supports |H_total| ≤ n … Therefore at most two Hopfions may coexist in one mode, and they must have opposite phase orientations." | capacity rule | "Theorem", "exact proofs" |
| 8 | Appendices Vol 1 Part 1 (data file), App E.2 | "The unification of electromagnetism and quantum mechanics in the form of QED is not assumed — it is a consequence of the compact U(1) topology of the BCT phase field." | Wigner-type uniqueness under four constraints, constraint 3 being "Linearity in ψ̄ and ψ: to give a linear (first-quantised) equation of motion" | derived; the same document marks the spin-structure step "the key unproven claim" |
| 9 | `tex/BCT_Letter129_EmergentDistance.tex` L197–202 | "ΔS ~ ħα₀ … connects the discreteness of distance to the discreteness of action (Planck's constant)." | void-hop counting | unstated |
| 10 | `tex/BCT_Letter60.tex` §"Madelung Acceleration Mechanism"; `tex/BCT_Letter20_GR_AllOrders.tex` eq. SGP; `tex/BCT_Appendix_AZ6.tex` §Madelung; One Medium §7 | Use of Ψ = √ρ e^{iθ}, the quantum Euler equation and the "quantum pressure (Bohm potential)" as tools. | standard | not claimed as QM results |
| 11 | `tex/BCT_Letter27_GPAxiom.tex` | "This axiom [GP with |Ψ|⁴] has been used but never derived. We derive it in three independent arguments." | (i) Bose–Hubbard t/U; (ii) selection of n=2 by the α formula; (iii) C4v representation | "elevate the GP axiom to a theorem" |
| 12 | `BCT_Letter210_GeometryOfUncertainty.tex` (root) | Bessel-modal priors, bounded distributions. | — | out of scope: classical statistics, not QM |

**Not adjudicable.** Appendix JH6 (Born rule) and Letter 183 ("The Measurement Problem",
cited by Letters 204 and L204b) are cited and **do not exist in the tree** — phantom deferrals
of the App-FG kind already on the ledger. Letters 45–46 (Hopf charge as particles) are also
absent from the tree.

---

## 4. Step 1 — the Madelung baseline, with the algebra

**BCT's GP action as it appears in the corpus** (App AZ6 eq. SGP; the time-independent form
in App JH eq. GP is its stationary reduction):

$$S_{\rm GP}=\int d^4x\Big[\tfrac{i\hbar}{2}(\Psi^*\partial_t\Psi-\Psi\partial_t\Psi^*)-\tfrac{\hbar^2}{2m}|\nabla\Psi|^2-V(|\Psi|^2)\Big],\qquad V=\tfrac{g}{2}\rho^2 .$$

Its Euler–Lagrange equation is $i\hbar\partial_t\Psi=-\frac{\hbar^2}{2m}\nabla^2\Psi+g|\Psi|^2\Psi$.

**Forward (GP → fluid).** Put $\Psi=\sqrt\rho\,e^{i\theta}$, divide the equation by $\Psi$
(where $\Psi\neq0$), and separate real and imaginary parts. With $v=(\hbar/m)\nabla\theta$
and $Q=-\frac{\hbar^2}{2m}\frac{\nabla^2\sqrt\rho}{\sqrt\rho}$:

$$\text{Im}: \quad +\frac{\hbar}{2\rho}\Big[\partial_t\rho+\nabla\!\cdot(\rho v)\Big]=0,$$
$$\text{Re}: \quad -\hbar\partial_t\theta-\tfrac{m}{2}v^2-g\rho-Q=0,$$

and the gradient of the Re equation is the quantum Euler equation
$m\,Dv/Dt=-\nabla(g\rho)-\nabla Q$, i.e. Letter 60's eq. (correct as printed). AZ6's closed
form $Q=\frac{\hbar^2}{8m}\big[(\nabla\rho)^2/\rho^2-2\nabla^2\rho/\rho\big]$ is an identity
(verified symbolically; and in 3D on an arbitrary smooth test field at 60 dps, residual
$1.1\times10^{-25}$).

**Reverse (fluid → GP).** Writing $E:=(i\hbar\partial_t\Psi+\frac{\hbar^2}{2m}\nabla^2\Psi-g\rho\Psi)/\Psi$,
SymPy confirms the exact identity $E \equiv \text{HJ}+i\frac{\hbar}{2\rho}\,\text{cont}$, so
$\{\text{cont}=0,\ \text{HJ}=0\}\iff E=0\iff$ GP. **Nothing is added in the forward direction.**
In the reverse direction one datum is added that the pair (ρ, v) does not contain: **θ must be
a single-valued function**, equivalently $\oint v\cdot dl = 2\pi n\hbar/m$ on every loop
(Wallstrom 1994, abstract read; condition (9) as reproduced in Hushwater 2010, read in full;
Reddiger 2015 Thm 3.2 gives the local equivalence with topological condition $b_1(\Omega_t)=0$,
and Remark 3.3 the quantisation condition, both read). Whether that datum is "auxiliary" or
"a property of all non-spurious solutions" is disputed in the literature (Hushwater argues the
latter); either way it is the datum a *superfluid* carries by definition — the single-valued
complex order parameter — and it is exactly the datum BCT declares when it declares the
medium a condensate.

**Where ħ enters.** (i) In the action's kinetic terms, as written; (ii) in the definition
$v=(\hbar/m)\nabla\theta$; (iii) in Letter 20's background density $\rho_0=c^5/(\hbar G^2)$.
It is an **input** in every document, and One Medium says so. No document derives it.

**Convention defect (not an obstruction).** AZ6 Lemma "GP → Superfluid action in TF limit"
and Letter 20 eq. SGP write $-\rho\hbar\partial_t\theta-\rho\hbar^2(\nabla\theta)^2/2m
=-\rho(\partial_t\theta+v^2/2)$. With $v=(\hbar/m)\nabla\theta$ the right-hand side's second
term is $\rho m v^2/2$; the equality holds only at $\hbar=m=1$, unmarked. Units restore
uniquely, so **SC-MAD-3 does not fire**; recorded as CN-MAD-09.

**This is the baseline.** A BCT claim that reproduces any line above has reproduced a 1927
change of variables.

Scripts: `mad_step1_madelung.py` → `mad_step1_out.txt`.

---

## 5. Step 2 — the four-bin table

| # | claim | bin | reason |
|---|---|---|---|
| 1a | E_N = N·ε₀ "quantisation without axiom" | **D** | The linear law is attributed to Faddeev–Niemi. The Faddeev–Skyrme energy law is $E\approx cN^{3/4}$ (Ward 2005, read; there attributed to Vakulenko–Kapitanski 1979, Battye–Sutcliffe 1998/99, Lin–Yang 2004). At N=2 the two laws differ by 19%, at N=6 by 57%. More basic: JH's functional $\int[\frac{\hbar^2}{2m}|\nabla\Psi|^2+\frac g2|\Psi|^4]$ has no quartic-derivative (Skyrme) term, and an energy of that form "does not admit stationary soliton solutions with nonzero H" (Ward 2005 eq. (2) remark; Derrick scaling in 3D). The linear law is not computed in JH; it is asserted against the literature it cites. |
| 1b | [x̂,p̂]=iħ from base/fibre non-commutativity | **D** | No operators are defined, no Hilbert space, no computation. "Position ↔ S² base, momentum ↔ S¹ fibre" is a resemblance; ħ appears on the right-hand side of the thing being "derived". |
| 2 | spin-½ from phase π per fibre traversal | **D** | SU(2)→SO(3) is a fact about groups. The field content available (one complex scalar per Gates G′/RANK on the ledger; JH's ℂ² interior is a separate commitment, Gate INT) does not carry a spinor representation, and the "particle threading the interior" that accumulates a Berry-type phase is already a quantum object. |
| 3 | N_H=1 is "the unique smooth solution" of the flux condition | **premise falsified** (PROVEN by construction) | Take $\Psi=\sqrt{\rho_0}\,e^{i\chi(r)}(1,0)^T$ with $\chi=\alpha_0 r^2/2R$: the S² map is constant (H=0), smooth everywhere, and $\oint J\cdot\hat n\,dA=(\hbar/m)\rho_0\chi'(R)4\pi R^2=\alpha_0\rho_0 4\pi R^2$ to zero residual. The overall U(1) phase carries the surface flux and is invisible to the S² map that carries the Hopf charge. The flux condition constrains neither. |
| 4 | collapse at Σα₀ ≥ 1; N_c = 1/α₀ | **D** (nearest miss to B) | Uses α₀ (BCT-specific) and yields numbers the baseline does not. Arithmetic reproduces: N_c = 134.988; 1/α − N_c = 2.030 (variant 2 says "exactly 2", variant 1 says "2 + O(α₀)" — the second is right); τ_D = 1.179×10⁻³⁸ s; m_classical = 3.970×10⁻⁶ kg. But: (i) the "Theorem" premise — that Σα₀ ≥ 1 overconstrains the topology — has no derivation, only the sentence "the combined topology is overconstrained"; (ii) the state $a|H{=}{+}1\rangle+b|H{=}{-}1\rangle$ is undefined for a c-number GP field: a superposition of two classical configurations is not a configuration, and if the field is second-quantised so that it *is* a state, QM is the input; (iii) no equation of motion for the coefficients exists anywhere in the corpus. What breaks if α₀ is removed: the number 135, not the mechanism, which has none. |
| 5 | entanglement as one classical Hopf configuration; CHSH "reproduced exactly" | **D**, self-contradictory (PROVEN via Bell) | Letter 254 describes outcomes as local readings of a configuration "fixed at creation". In Bell's formulation (Bell 1964 §II, read) that is a local-hidden-variable model — λ = the field configuration, outcomes A(a,λ), B(b,λ) — and every such model satisfies |CHSH| ≤ 2. The letter cites Bell's theorem and then asserts its negation. The "identity" 2r_oct+1 = √2 holds because r_oct is *defined* as (√2−1)/2; cos(π/4)=1/√2 is arithmetic; the Tsirelson bound 2√2 is a theorem of the Hilbert-space QM being assumed. r_oct adds nothing. |
| 6 | QM "emerges" from non-Markovian OHC stochastics | **C** | The OHC is a GP condensate — a quantum field from line one (One Medium §2). Showing that its dynamics are non-Markovian is a statement about a quantum theory, not an emergence of one; Barandes's correspondence runs between QM and a *classical* indivisible process, and the OHC is not classical. Theorem II (redundancy) is a statement about a classical topological charge and is fine as such; it does not touch the quantum sector. |
| 7 | Pauli exclusion from |H_total| ≤ n | **D** | The capacity rule is postulated, not derived. And it does not yield the theorem: (+1, −1, +1) has |H_total| = 1 ≤ 1, so three (any odd number of) hopfions sit in one n=1 mode. "At most two" does not follow from the stated premise. |
| 8 | Dirac/QED "not assumed" | **C** | App E.2's uniqueness argument takes as constraints: ψ transforms as a Dirac spinor (constraint 1), and "Linearity in ψ̄ and ψ: to give a linear (first-quantised) equation of motion" (constraint 3). Linearity and spin are inputs; the output is the unique action with those inputs. The document itself flags the spin-structure step as unproven. |
| 9 | ħ from distance granularity (ΔS ~ ħα₀) | **D** | ħ is on the right-hand side. |
| 10 | Madelung/Bohm potential as used in L60, L20, AZ6, One Medium §7 | **A** | Correct results, correctly attributed by name ("quantum pressure (Bohm potential)"). Not a failure of BCT — this is the one place the corpus does exactly what §3 of the prompt asks. The GR derivation built on it is outside this gate. |
| 11 | GP axiom "derived" | **C** | Argument (i) starts from a Bose–Hubbard model — a second-quantised quantum many-body system; the quantum content is put in there. Argument (ii) selects n=2 because it reproduces α — a selection against the target, in the corpus's own words. Argument (iii) is representation theory of the lattice and does not bear on quantisation. |

**Bin B: empty.** Every row that uses BCT-specific structure (3, 4, 5, 7, 9, 11) either
assumes the quantum feature it recovers or does not derive what it asserts.

Scripts: `mad_step2_checks.py` → `mad_step2_out.txt`.

---

## 6. Step 3 — the five hard ones

1. **Linearity and superposition.** Not addressed. No document disposes of the GP
   nonlinearity or explains why an effective linear equation should govern excitations of a
   nonlinear medium. One Medium declares the superposition principle an input. *Finding:
   not addressed.*
2. **Born rule.** Not addressed. The only mention (Letter 72) says "the three triality
   states have equal weight under ℤ₃" and defers the derivation to Appendix JH6, which does
   not exist. |Ψ|² is a density everywhere in the corpus (ρ₀ = Planck density); it is never
   argued to be a probability. *Finding: not addressed; phantom deferral.*
3. **Hilbert space and operators.** Not addressed. Declared input in One Medium §2/§12.
   App JH names x̂ and p̂ without defining a space they act on. *Finding: not addressed.*
4. **Entanglement.** Addressed, and gets it backwards (§5 row 5). A single classical field
   on ℝ³ with locally-read outcomes is the model Bell's theorem excludes. *Finding: engaged,
   and the engagement contradicts a theorem the letter itself cites.*
5. **Measurement.** Addressed with vocabulary (§5 rows 4, 6). "Topological snap" and
   "locking" have no equation of motion; the trigger Σα₀ ≥ 1 is a count, not a dynamics.
   *Finding: vocabulary only.*

---

## 7. CN-MAD notices

Revised clause by clause against §§3–6 above.

**CN-MAD-01 — PROVEN (computed).** BCT's GP action ⇔ Madelung fluid pair is an algebraic
identity in both directions (§4). Every quantum feature recovered from that pair is inherited
from the condensate axiom. Affects: nothing in the void-geometry layer; affects the framing
of every document in §3 rows 1a, 1b, 2, 4, 6, 9.

**CN-MAD-02 — PROVEN (explicit counterexample).** App JH §"Topological Selection" eq.
(hopf-matching) is satisfied by an H=0 configuration; the claimed uniqueness of N_H=1 is
false. Consequence: JH Result 1 (the OHC ground state is a hopfion) has no derivation in JH.
Results 2–6 of JH inherit N_H=1 from Result 1. This is independent of, and adds to, the
ledger's Gate INT finding of three interior commitments.

**CN-MAD-03 — PROVEN (literature read).** JH's E_N = N·ε₀ contradicts the N^{3/4} law of
the model it cites for it; and JH's energy functional (no Skyrme term) admits no stationary
nonzero-H solution at all. "Energy quantisation" in JH Result 2 is therefore unsupported
twice over.

**CN-MAD-04 — PROVEN (Bell's theorem).** Letter 254's mechanism is, by its own description,
a local-hidden-variable model and cannot violate CHSH. Its "Tsirelson identity" is
definitional. Tier claimed PROVEN; correct tier for the physical claim: falsified; for the
identity: trivially true, contentless.

**CN-MAD-05 — PROVEN (arithmetic).** Letter 81's capacity rule admits three hopfions per
n=1 mode. The Pauli "theorem" (also Letter 78, App KA4, Chemistry Vol K Theorem 1) is not
proved by its proof. The capacity rule itself is unsourced.

**CN-MAD-06 — ASSERTED (corpus tier: "theorem"; correct tier: ASSERTED).** Letter 72's
collapse threshold: the premise is unargued and the object it acts on is undefined for a
classical field. The numbers N_c, τ_D, m_classical reproduce from α₀ but are consequences of
an assertion. m_classical ≈ 4 μg is **not on the prediction registry** and should not be
scored by PRED2 as a prediction unless the mechanism is supplied.

**CN-MAD-07 — CONJECTURE (corpus-consistency).** One Medium §2/§12 is the correct programme
statement. Letters 64, 72 (both variants), 75 §"Measurement Problem", 78, 81, 254, App JH
Results 2–3, App E.2's closing claim, Chemistry Vol K Theorem 1 and App KA4 contradict it and
need retraction or downgrade to "interpretation". The *Geometry of Everything* v4 line "The
Measurement Problem — Solved" and *Accidentally Solved* p.13 inherit the contradiction.

**CN-MAD-08 — ASSERTED (phantom deferral).** Appendix JH6 and Letter 183 are cited (L72;
L204, L204b) and absent from the tree. Add to the App-FG list.

**CN-MAD-09 — minor, PROVEN.** (a) Hopf-invariant normalisation: Letter 254 writes
1/(16π²)∫F·A, Letter 64 writes 1/(4π²)∫F·A for the same quantity; the former matches the
standard 1/(32π²)∫εFA (Ward 2005 eq. (1)). (b) AZ6/L20 use ħ=m=1 unmarked inside an
ħ-explicit derivation.

**Positive notices (must be reported as plainly).**
- Letters 20, 60, App AZ6 and One Medium §7 use the Madelung transformation correctly and
  credit it to Madelung/Bohm by name. Letter 60's quantum Euler equation is right as printed.
- One Medium §2 and §12 state the correct position on QM without hedging. Nothing in this
  gate touches the void-geometry layer (r_oct, r_tet, α₀, c/a = √2).
- Letter 72's arithmetic is internally consistent (§5 row 4), and the m_classical ≈ 4 μg
  boundary is the kind of number a mechanism *could* make falsifiable.

---

## 8. External citations — what was actually opened

| source | status in this session |
|---|---|
| T. C. Wallstrom, Phys. Rev. A **49**, 1613 (1994) | **abstract only**, via ADS; body paywalled. Cited only for the abstract's statement. |
| V. Hushwater, arXiv:1005.2420 (Comment on Wallstrom) | **read in full.** Source for Wallstrom's condition (9) and the counter-argument. |
| M. Reddiger, arXiv:1509.00467, "The Madelung Picture as a Foundation of Geometric Quantum Theory" | **read §1.2, §3 (Thm 3.2, Remark 3.3), §4–5.1.** Source for the local-equivalence theorem, the b₁ condition, and the Madelung 1927 quotation. |
| R. S. Ward, arXiv:hep-th/0512024, "Hopf solitons on the lattice" | **read in full.** Source for E ≈ cH^{3/4}, the no-soliton remark for E=∫[|∂ψ|²+V], and the Hopf normalisation. |
| J. S. Bell, Physics **1**, 195 (1964) | **read §I–II** (UC Davis copy). Source for the local-hidden-variable formulation. |
| E. Madelung, Z. Phys. **40**, 322 (1927) | **not opened.** Cited only through Reddiger's quotation. |
| D. Bohm, Phys. Rev. **85**, 166, 180 (1952) | **not opened** (paywalled). Nothing attributed to it beyond its existence. |
| E. Nelson, Phys. Rev. **150**, 1079 (1966) | **not opened.** Nothing attributed to it. |
| L. Faddeev & A. J. Niemi, Nature **387**, 58 (1997) | **abstract only** (ADS/Nature). The N^{3/4} attribution is Ward's, not mine. |

---

## 9. §0.6 — reproduced verbatim

> Recovering the Schrödinger equation from a condensate is **necessary and nowhere near
> sufficient** for deriving quantum mechanics. Madelung's transformation is invertible: obtaining
> NLSE from GP is a change of variables, not an explanation. A favourable verdict here means BCT
> has a **non-trivial** quantum sector — it does not mean BCT has derived measurement, the Born
> rule, entanglement, linearity, or Hilbert space. **Gate MAD cannot deliver quantum mechanics. At
> most it delivers the right to ask which of those five BCT can reach.** A favourable verdict is a
> ticket to a harder gate.

---

## 10. What the gate did **not** establish

- It did not test whether a different interior field content (Gate OP's E1 survivor, or a
  genuinely spinorial order parameter) could reach bin B. That is a construction question,
  not an audit of the present corpus.
- It did not read Bohm 1952, Nelson 1966, Madelung 1927 or Faddeev–Niemi 1997 in the body;
  nothing above depends on their content beyond what the read sources report of them.
- It did not score m_classical ≈ 4 μg as a prediction; it is unregistered.
- It did not adjudicate the GR derivation that sits on the same Madelung step (Letters 20/26,
  AZ6); that is the QP/G′ sector on the ledger.
- It did not settle the Wallstrom–Hushwater dispute; the gate's verdict does not depend on
  which side is right, because BCT's medium carries single-valuedness by fiat either way.
- **What would move row 4 to bin B:** (i) a definition, within the c-number GP theory or a
  stated second-quantisation of it, of the object $a|H{=}{+}1\rangle+b|H{=}{-}1\rangle$;
  (ii) a dynamical equation whose solution exhibits a transition at Σα₀ = 1; (iii) a
  derivation of the Born weights from it. Any one of the three would be new; all three would
  be a quantum sector.

---

## 11. Files in this folder

- `gate_MAD_prompt_asrun.md` — byte-identical to the pre-registered prompt (digest above).
- `mad_step1_madelung.py`, `mad_step1_out.txt` — the Madelung derivation, both directions.
- `mad_step2_checks.py`, `mad_step2_out.txt` — the JH flux counterexample, the N^{3/4}
  comparison, the Pauli capacity check, the Letter 72 arithmetic, the Letter 254 identity, the
  AZ6 unit convention.
- `gate_MAD_RESULT.md` — this file.

*Closed 14 September 2026.*
