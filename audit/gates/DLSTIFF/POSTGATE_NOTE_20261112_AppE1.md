# POST-GATE NOTE — App E.1 §3.3, the R6d door

**Status: NOT PART OF GATE DL-STIFF. This note cannot move that gate's verdict, and does not.**
Card §8's no-fit clause forbids changing any route, kill test, convention or verdict code after the
run starts, and App E.1 is not among the §4.1 pinned sources. `gate_DLSTIFF_RESULT.md` is sealed and
is **not** edited by this note. Everything below is desk-level work done afterwards, at Michel's
request ("Read pls"), on the one item the gate recorded as unevaluable.

**Written:** 12 November 2026, Australia/Melbourne, in the DL-STIFF run thread, **after** the gate's
`git format-patch` bundle had been produced.

---

## 0. Provenance, and the contamination this note incurs

The gate was delivered first; this read came second. The gate's own contamination statement
("sources read: exactly the eleven pinned in §4.1") was true when written and remains true **of the
run**. This note records what was read afterwards, so the record is complete:

| file read after the gate was sealed | SHA-256 | how |
|---|---|---|
| `BCT_Appendices_Volume1_2026_compressed_Part1.pdf` (holds App E.1; §3.3 at pp. 54–55) | `6e14b6c0183d089c8b1f56701878addef43f9b21d4533ddf5dccf464a00dbb8b` | `pdftotext -layout`, read at the located page |
| `audit/gates/LINK/gate_LINK_deliverable.md` | `7d2e94a8820124e78b2302c93ec51820fa781f2e223ebc3b1974e530633af0a4` | **grep-level only** — the matching lines for `10.74`, not the document |
| `audit/gates/LINK/gate_LINK_RESULT.md` | `fff9af0d33c57572e2e373d8c446c9c8982f57756d81d59c4034553127043bd7` | **grep-level only**, same search |

**Consequence to record: this session is no longer eligible as the blind replicator for Gate
DL-STIFF**, nor for any future gate pinning App E.1 or Gate LINK. The replication card §8 calls for
must go to a fresh thread that has read none of the above.

**A correction to the scoping note's attribution.** `audit/scoping/DL_scoping_2026-11-12.md` §4
credits the finding on this section to Gate QED (CN-QED-04). The section was in fact audited by
**Gate LINK** — CN-LINK-03, CN-LINK-08 and CN-LINK-09 — which is in the tree. Whether Gate QED also
covered it is not determined here. The misattribution is recorded so a future card pins the right
file; it changes nothing in DL-STIFF, which cited the scoping note only for the *existence* of the
parameter and never relied on the attribution.

Notices below are prefixed **PGN-** and not **CN-DLS-**, because they are not gate findings.

---

## 1. What §3.3 actually says

The section's chain, as printed (App E.1 §3.3, "BCT Vacuum is in the Coulomb Phase: The Monopole
Suppression", pp. 54–55):

```
S_monopole = (2π/e)² × (ρ_s/2) × a = 4π² ρ_s a
In BCT units where a = l_P and ρ_s = J/l_P:   S_monopole = 4π² J
...
J = 1/(4πα₀) ≈ 10.74
S_monopole = 4π²/(α4πα₀) = π/(4α₀α) ≈ 34
P_monopole ~ exp(−34) ≈ 2 × 10⁻¹⁵
```

and the sentence that introduces the number:

> "The lattice stiffness J must be large for the BCT medium to be physically rigid (it is the
> Planck-scale coupling). **Taking** J = 1/g₀² where g₀² = 4πα₀ is the bare electromagnetic
> coupling."

§3.4 then states the identification explicitly — "the Wilson plaquette action … giving the Maxwell
action with coupling `1/e² = J`" — and the correction map
`1/e²_ren = 1/(4πα)` with `α = α₀(1−3α₀)/(1−α₀)`.

---

## 2. Findings

**PGN-01 [PROVEN from the text] — the parameter is asserted, in the section's own word.** "*Taking*
J = 1/g₀² where g₀² = 4πα₀." No derivation of `J = 1/(4πα₀)` appears in §3.1–3.4. The gate's R6d
entry — "a parameter *written down*, which fails §4.3's standard on its face" — is confirmed by
direct reading. **R6d is closed as an assertion; SC-DLS-2 stands unchanged.**

**PGN-02 [PROVEN from the text] — the only argument offered is largeness, which is the wrong
target.** §3.3 argues that J *must be large* "for the BCT medium to be physically rigid". By the
gate's CN-DLS-04, largeness is all the Coulomb phase ever required: `β > β_c` needs only
`c > 0.0235` (hypercubic) against the candidate's `c = 1/4`. So E.1's argument bears on the **phase**
and is silent on the **value** — exactly the asymmetry CN-DLS-03/04 recorded, now visible in the
corpus's own reasoning.

**PGN-03 [PROVEN, new here] — E.1's route is R1, and E.1 derives R1's Meissner mass itself.** §3.1
sets `A_μ = (1/e)∂_μθ`: the gauge field **is** the medium's compact phase. That is why β can relate
to `ρ_s` there — the medium is not neutral under the field, it *is* the field. §3.1 then derives
`L = (ρ_s e²/2)A_μA^μ`, i.e. `m_γ = e√ρ_s`, the Meissner mass, and escapes it by appealing to §3.2's
Coulomb phase "where the superfluid stiffness ρ_s → 0 at long range". But §3.3's monopole suppression
is built from a **large** `ρ_s` (`S = 4π²ρ_s a` with `ρ_s a = J = 10.74`). The section therefore uses
`ρ_s` for two quantities that §3.2 requires to differ: one large at the lattice scale, one vanishing
at long range. A bare-versus-renormalised reading would rescue this, but §3.3 does not say so — it
writes a single `ρ_s` and sets it to `J/l_P`.
**This is the gate's CN-DLS-02 appearing inside the corpus:** the construction that lets the medium
fix β is the construction that gives the photon a mass, and E.1 pays that bill by making `ρ_s`
vanish in the same breath as it uses `ρ_s` being large.

**PGN-04 [PROVEN, arithmetic] — five values for one quantity.** For `S_monopole`, on E.1's own
`J = 10.74201848` and §3.4's own `1/e² = J` (`e1_33_check.py`, mpmath 30 digits):

| expression | value | status |
|---|---|---|
| (a) `(2π/e)²(ρ_s/2)a`, using `1/e² = J` | 2277.726275 | E.1's own first expression |
| (b) `4π²J` | 424.0778916 | E.1's own next line; **the correct value of (b)** |
| (c) `4π²/(α·4πα₀) = π/(αα₀)` | 58113.9376 | literal reading of the printed form |
| (d) `π/(4α₀α)` | 14528.4844 | the printed second form |
| (e) `πJ` | 33.74704635 | **what the printed "≈ 34" equals** |

E.1 prints (a) = (b) and (b) = (c) = (d) ≈ 34. Every one of those equalities fails: (a)/(b) = 5.371
— (a) = (b) would need `e² = 1/2`, contradicting §3.4's `1/e² = J`; (c)/(b) = 137.036 = `1/α`;
(d)/(b) = 34.259 = `1/(4α)`; and **(b)/(e) = 4π exactly**, so the printed answer is the correct
`4π²J` short by a factor of `4π`. Gate LINK recorded (b), (d) and (e) as CN-LINK-03/08; (a) and (c)
are added here.

**PGN-05 [PROVEN, arithmetic] — the error runs toward the conclusion, not away.** `exp(−34)` is
`1.714×10⁻¹⁵`, consistent with the printed `≈ 2×10⁻¹⁵`, so the slip is upstream of the exponential.
On the correct `S = 424.0779`, `P ~ exp(−424.08) = 6.688×10⁻¹⁸⁵`. The true suppression on E.1's own
numbers is ~10⁻¹⁸⁴, not ~10⁻¹⁵: **monopoles are far more suppressed than claimed, so the
Coulomb-phase conclusion is strengthened, not weakened, by fixing the arithmetic.** Consistent with
CN-LINK-03's "direction unchanged; conclusion strengthened".

**PGN-06 [PROVEN, cross-check] — the corpus asserts two incompatible bare couplings.** Reproducing
CN-LINK-09's point cold: App JH4's `g² = π⁵/6 = 51.0033` is a Wilson `β = 1/g² = 0.01960658`, **deep
confined**; E.1's `β = 1/e² = J = 10.74201848` is **deep Coulomb**. They differ by a factor of
547.88 and sit on opposite sides of `β_c = 1.0111`. A number the corpus states two incompatible
values for is not a number the corpus derives.

**PGN-07 [PROVEN, arithmetic; settled elsewhere] — the §3.4 correction map.**
`α_map = α₀(1−3α₀)/(1−α₀) = 0.007297477982`, i.e. `1/α_map = 137.033644` against CODATA
`137.0359992` — a relative error of `1.72×10⁻⁵`. Correspondingly `β_bare = 10.74201848` and
`β_ren = 10.90479091` against `10.90497833` at CODATA α. The map's accuracy is not evidence that it
is a derivation; that is the question **FWD/STAT already closed** as a selected correction map, and
nothing here reopens it. Recorded because it is the bare-versus-renormalised reading that makes the
gate's CN-DLS-10 say the 1.5 % gap *is* what FWD/STAT closed, rather than calling it a plain error.

---

## 3. Effect on Gate DL-STIFF

- **Verdict: unchanged. SC-DLS-2, CONJECTURE.** R6d is closed as an assertion, which is what the gate
  recorded without reading it (PGN-01). The reading strengthens the verdict; it does not disturb it.
- **CN-DLS-09's recommendation is downgraded.** The gate recommended "a card that pins App E.1 and
  asks whether §3.3 derives or assumes the number", and called it "the one place a future gate could,
  in principle, still disturb this verdict." §3.3 **assumes** it, in the word "Taking". **There is
  nothing left to adjudicate on β.** What remains in the section is arithmetic that Gate LINK already
  recorded (PGN-04/05), and a correction map FWD/STAT already closed (PGN-07). A card pinning App E.1
  is no longer needed for the β question; if one is ever written, it should be about the `ρ_s`
  conflation in PGN-03, which is a question about E.1's internal consistency, not about β.
- **The replication called for by card §8 is unaffected and still outstanding** — and must go to a
  thread that has not read §0's three files.

---

*Script: `e1_33_check.py`, output `e1_33_check_output.txt` (deterministic; mpmath 1.3.0 at 30 digits,
10 reported). Run with `python3 -I`. `gate_DLSTIFF_RESULT.md` is unmodified by this note.*
