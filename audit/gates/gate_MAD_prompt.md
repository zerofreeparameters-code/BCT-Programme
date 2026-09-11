# GATE MAD — DOES BCT DERIVE QUANTUM MECHANICS, OR RESTATE IT?
## Cold Ledger gate. Fresh thread. Pre-register by SHA-256 **from the file the session receives.**

**The question.**

> A Gross–Pitaevskii condensate and a nonlinear Schrödinger equation are the same equation. The
> Madelung transformation moves between them by a change of variables. BCT's medium is a GP
> condensate. **So: what, exactly, does BCT obtain about quantum mechanics that was not put in when
> the medium was declared to be a condensate — and what does it obtain that standard Madelung /
> Bohm / Nelson hydrodynamics does not already give?**

Notices **CN-MAD-01** onward.

## 0 — HANDOFF, QUARANTINE, SCOPE

**0.1 — HANDOFF.** Receive as a file at a commit-pinned `raw.githubusercontent.com` URL. `curl` to
disk, `sha256sum`, record the digest, **then** read. If you received pasted text, claim no digest
and say so in §1.

**0.2 — QUARANTINE.** Do not consult the 9–11 Sep 2026 threads, BCT-X / Sandbox TOP, or any
concurrent gate. The Cold Ledger auto-loads and cannot be partially read — if you read it,
**declare it** and name the unpermitted summaries you saw.

**0.3 — EXTERNAL LITERATURE IS PERMITTED AND EXPECTED HERE.** Unlike most gates in this series,
this one cannot be run from the corpus alone: the question is what BCT adds to a known
correspondence. Madelung (1927), Bohm (1952), Nelson (1966), and the standard GP/NLSE literature
are admissible and should be read rather than paraphrased from memory. **Cite what you actually
read.** Do not attribute a result to a paper you have not opened.

**0.4** Construction permitted.

**0.5 — SEARCH-SPACE AUDIT, MANDATORY, REPORTED BEFORE ANY CONCLUSION.**
- **Repo:** tarball, digest recorded. **134 `.tex`, 26 at the tree root outside `tex/`.**
- **Mount:** 33 ZIP archives of page images with `.txt` layers, 14 true PDFs, and **2 raw UTF-8
  text files** that `file` reports as `data` and that no PDF or ZIP tool will open. **Type every
  file with `file`.** Report page-level coverage.

## 0.6 — WHAT PASSING THIS BUYS. Reproduce verbatim in the deliverable, whatever the verdict.

> Recovering the Schrödinger equation from a condensate is **necessary and nowhere near
> sufficient** for deriving quantum mechanics. Madelung's transformation is invertible: obtaining
> NLSE from GP is a change of variables, not an explanation. A favourable verdict here means BCT
> has a **non-trivial** quantum sector — it does not mean BCT has derived measurement, the Born
> rule, entanglement, linearity, or Hilbert space. **Gate MAD cannot deliver quantum mechanics. At
> most it delivers the right to ask which of those five BCT can reach.** A favourable verdict is a
> ticket to a harder gate.

## 1 — STEP 0: WHAT DOES BCT ACTUALLY CLAIM ABOUT QM?

Enumerate, from primary source, every place the corpus claims to derive, explain or obtain a
quantum-mechanical feature. Do not work from a list supplied here; build it by search and state the
search. For each, record: location, the exact claim quoted, what it is derived **from**, and the
tier its own document assigns.

Expect at minimum claims about: energy quantisation, the canonical commutator, half-integer spin,
the Pauli principle, wave–particle behaviour, and measurement or collapse. **Record what you find,
not what this list expects.**

## 2 — STEP 1: THE MADELUNG BASELINE

Establish, by explicit calculation rather than citation:

- Write BCT's own GP equation as it appears in the corpus.
- Apply the Madelung substitution Ψ = √ρ·e^{iθ} and derive the resulting continuity and
  Euler-type equations, including the quantum-potential term. Show the algebra.
- Run it in reverse: from the fluid equations, recover the Schrödinger form. **State plainly
  whether anything was added in either direction.**
- Identify precisely where ħ enters, and whether it is an input, a definition, or an output.

**This is the baseline any BCT quantum claim must beat.** A claim that reproduces a Madelung result
has reproduced a 1927 change of variables.

## 3 — STEP 2: THE DISCRIMINATION TEST

For each claim enumerated in §1, place it in exactly one bin, with the reason stated:

| bin | meaning |
|---|---|
| **A — inherited** | follows from the medium being a condensate; standard Madelung/Bohm/Nelson content |
| **B — genuine addition** | uses BCT-specific structure (the lattice, the void geometry, the topology) and yields something the baseline does not |
| **C — restatement** | the quantum feature is assumed in the setup and recovered at the end |
| **D — analogy** | a structural resemblance presented as a derivation |

**Bin B is the whole point of the gate.** For anything placed in B, state exactly which BCT-specific
input it uses and what breaks if that input is removed.

Be even-handed: a claim landing in A is not a failure of BCT — it is a correct result with the
wrong attribution. Say which.

## 4 — STEP 3: THE FIVE HARD ONES

Standard hydrodynamic approaches to QM have known difficulties. For each, establish what BCT says,
if anything, and whether it engages the difficulty or passes it by:

1. **Linearity and superposition** — the GP equation is nonlinear; Schrödinger is linear. How is
   the nonlinearity disposed of?
2. **The Born rule** — is |Ψ|² a probability, or a density? On what argument?
3. **Hilbert space and operators** — where does the vector-space structure come from?
4. **Entanglement** — does a single classical field on ℝ³ support configuration-space correlations?
5. **Measurement** — is anything said, and is it more than vocabulary?

**"Not addressed" is a legitimate and useful finding.** Record it as such rather than searching for
something to credit.

## 5 — STOP CONDITIONS

**SC-MAD-1.** All claims fall in bins A, C or D. → BCT's quantum sector is inherited or
restated; report the bin assignment with reasons.
**SC-MAD-2.** One or more claims fall in bin B. → **Report them precisely**, name the BCT-specific
input each uses, and state what §4 difficulty each does or does not engage. This is the favourable
outcome and must be reported as plainly as the unfavourable one.
**SC-MAD-3.** BCT's GP equation cannot be brought to Madelung form as written — a missing term, an
inconsistent convention, an undefined quantity. → Halt on the comparison; report the obstruction.
**SC-MAD-4.** The corpus makes no adjudicable quantum claim. → Report; the gate is void.

**If the outcome matches no stop condition, record it as a prompt defect** rather than force-fitting
it. **No stop condition licenses a favourable conclusion, and none licenses an unfavourable one.**
If BCT has a genuine quantum result, this gate must be able to find it.

## 6 — DELIVERABLE

Digest or explicit refusal · **search-space coverage before any other number** · verdict first ·
the §1 enumeration in full · the Madelung derivation with its algebra shown · the four-bin table
with a reason per row · the five hard questions answered or marked not-addressed · external
citations, each one actually read · CN-MAD notices tiered PROVEN / CONJECTURE / ASSERTED · scripts
· contamination statement · **§0.6 reproduced verbatim** · what the gate did **not** establish.

**Revise notices clause by clause.** **Commit deliverable, scripts and as-run prompt to
`audit/gates/MAD/` at close, and update `audit/NEXT.md`.**

*Written 11 September 2026. Not executed. Pre-register before use.*
