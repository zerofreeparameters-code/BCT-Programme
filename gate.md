# GATE KAUDIT — DO APPENDIX K'S THREE THEOREMS SURVIVE ON THE REAL c/a=√2 LATTICE?
## Cold Ledger gate. Fresh thread. Pre-register by SHA-256 **from the file the session receives.**
## Supersedes the withdrawn Gate M21 (the 21-vertex selection-rule framing): App K already
## addresses the loop question; the live question is whether its proofs are sound.

**The question.**

> App K ("The BCT Lattice Green's Function", draft, now archived) carries out App J's deferred
> electron-mass loop programme and delivers three theorems: **T1 (Bipartite)** — the BCT lattice is
> bipartite (A/B sublattices, 8 nearest neighbours), all closed walks even, so the 21-vertex loop
> cannot exist (21 odd) and C_A(odd)=0; **T2 (Non-Renormalization)** — exact particle-hole (PH)
> symmetry gives G_loc(0)=0, so a zero-energy fermion gets zero self-energy at all orders (electron
> stays massless perturbatively, and photon/graviton masslessness is exact); **T3 (Gap Equation)** —
> the Schwinger–Dyson gap equation needs c·t²≈0.02 but BCT gives ≈0.001, 20× too weak. It also
> (correctly) calls the a₁₆≈m_e/4 proximity a numerical accident.
>
> **But T1 and T2 assume coordination 8 and a bipartite lattice, and Gate KND (ledger item 10)
> established that at c/a=√2 the coordination is 12, the lattice is FCC and NOT bipartite (explicit
> triangle, C_A(3)≠0), and the band is −12t…+4t (PH-asymmetric). Do App K's three theorems survive
> when recomputed on the correct 12-coordinated FCC lattice — and if they do not, does the
> perturbative route to m_e still fail (and by what mechanism: protection to zero, or generation at
> the wrong magnitude)?**
>
> A verdict that the theorems fail does not by itself refute the geometry; it means App K's proofs
> must be redone and its "exactly massless photon/graviton" corollary re-examined. A verdict that
> the corrected calculation still forbids a correct-magnitude m_e sharpens the same hierarchy
> problem App K names, with sound proofs.

Notices **CN-KAUD-01** onward.

## 0 — HANDOFF, QUARANTINE, SCOPE

**0.1 — HANDOFF.** Receive as a file at a commit-pinned `raw.githubusercontent.com` URL. `curl`
to disk, `sha256sum`, record the digest, **then** read. If pasted, claim no digest and say so.

**0.2 — QUARANTINE.** Do not consult the 9–15 Sep 2026 threads, BCT-X / Sandbox TOP, `gate-jhf`,
`gates-closed-archive`, or any concurrent gate. **Do not read `audit/notes/` or any
`audit/gates/*/` deliverable.** You **may and must** read the primary sources under test: App K
(`BCT_Appendix_K_GreenFunction*` — locate it; may be a draft PDF/`.tex` under `tex/` or `audit/`),
App J (`tex/BCT_Appendix_J_SphereAction.tex`), the App E fermion/Dirac content if locatable, and
`audit/MINIMAL_BCT.md`. Standard references on bipartite tight-binding, particle-hole symmetry,
FCC band structure, and Schwinger–Dyson dynamical mass generation are allowed.

**0.3 — INHERITANCE IS FORBIDDEN.** Derive **yourself**, cold, from the lattice geometry and field
theory: (a) the nearest-neighbour shell at c/a=√2 (count it — do not assume 8 or 12); (b) whether
the NN bond graph is bipartite (look for odd closed walks / triangles among mutual NN); (c) the
tight-binding band E(k) and whether it is PH-symmetric; (d) the local Green's function G_loc(0) on
that band; (e) the leading fermionic self-energy contribution and its magnitude. If a prior finding
(Gate KND's 12-coordination/non-bipartite/asymmetric-band result, low-order dominance, or App K's
own theorems) reaches you, declare it in the contamination statement and re-derive from scratch.
Treat App K's theorems as claims to be checked, not inputs.

**0.4 — SCOPE.** This gate audits a written document's three theorems by recomputation; it does not
construct a new mass mechanism (that would be doing App K's Phase-35/PH-breaking job). Permitted
outputs: "theorem T_i holds / fails on the correct lattice," and "the perturbative route fails
because X / succeeds," not "here is the PH-breaking action that fixes it."

## 0.5 — WHAT SETTLING THIS BUYS. Reproduce verbatim in the deliverable, whatever the verdict.

> This gate decides whether App K's three theorems are sound on the real c/a=√2 FCC lattice. It does
> not by itself decide whether BCT can ever produce m_e — that awaits a PH-breaking mechanism (App
> K's Candidates 1–3), each a separate later gate. A verdict of "theorems fail" does not refute the
> geometry (α₀, void radii, the surviving LO layer are untouched) — it means App K's proofs, and its
> corollary that the photon/graviton are *exactly* massless by PH protection, must be redone on the
> correct lattice. A verdict of "the corrected route still cannot give m_e at the right magnitude"
> is a legitimate sharpening of the hierarchy problem, not a vindication of the rest of BCT.

## 1 — STEP 0: THE LATTICE (count it cold)

- From the BCT lattice at c/a=√2, enumerate the nearest-neighbour shell of a site. State the
  coordination number and the NN vectors. Does App K's "8 NN, δ=(±½,±½,±½√2)" capture all NN at the
  minimum distance, or are there same-distance bonds it omits? (Check the in-plane (±1,0,0),(0,±1,0)
  corner–corner separations.)
- Determine whether the NN bond graph is bipartite: exhibit an odd closed walk (triangle) if one
  exists, and compute C_A(3). A single triangle refutes T1.

## 2 — STEP 1: THEOREM 1 (bipartite / no odd loops)

- On the correct NN graph, is C_A(n)=0 for odd n? If not, T1 is FALSE. State the consequence for
  the 21-vertex conjecture: is it killed by parity (App K's reason) or does it survive T1's failure
  and require a different argument (low-order dominance: the shortest odd/even loop dominates the
  coupling expansion, setting a mass scale α₀^{L_min/2} — compute it and compare to m_e).

## 3 — STEP 2: THEOREM 2 (particle-hole symmetry / non-renormalization)

- Compute the tight-binding band E(k) on the 12-coordinated lattice and test PH symmetry (is the
  spectrum symmetric about E=0? what is the band range and the half-filling Fermi level?).
- Recompute G_loc(0). Is it zero (App K) or non-zero? If the band is PH-asymmetric, G_loc(0)≠0 and
  the non-renormalization theorem fails: the zero mode is NOT protected. Then determine whether the
  electron acquires a perturbative self-energy and its **magnitude** (leading loop ~α₀^{L_min/2}).
  State the corrected conclusion: is m_e protected to zero, or generated at the wrong magnitude?
- Re-examine App K's corollary that the photon and graviton are *exactly* massless by the same PH
  protection. If PH symmetry fails, does that corollary fail too, or is photon/graviton
  masslessness secured by a different (correct) argument? (Cross-check against Gates G′, LINK, RANK
  — but derive, don't inherit.)

## 4 — STEP 3: THEOREM 3 (gap equation) AND THE n=16 ACCIDENT

- Recompute the density of states on the correct band (App K's ρ(E)~E·ln(1/E) came from the wrong
  nodal-plane structure). Does the gap-equation conclusion (coupling ~20× too weak) survive on the
  corrected DOS? Report the corrected factor.
- Confirm or refute App K's (correct-in-spirit) statement that a₁₆≈m_e/4 is a numerical accident:
  reproduce the monotone series and the null-model weight.

## 5 — STEP 4: THE STEELMAN

**Required.** Construct the strongest case that App K's theorems survive — e.g. that some emergent
sub-sector is effectively bipartite/PH-symmetric, or that the omitted A–A bonds are suppressed so
the 8-coordination model is the right effective description. If it succeeds, say so **prominently**.

## 6 — STOP CONDITIONS

**SC-KAUD-1.** T1 and/or T2 FAIL on the correct lattice (odd loops exist / band PH-asymmetric /
G_loc(0)≠0). → Report which theorems fall and the corrected mechanism by which the perturbative
route to m_e still fails (protection-to-zero vs wrong-magnitude), plus the fate of the
exactly-massless photon/graviton corollary. Legitimate, honest outcome.
**SC-KAUD-2.** The theorems SURVIVE (the correct lattice is, for the relevant fermion sector,
effectively bipartite/PH-symmetric). → App K stands; record the justification.
**SC-KAUD-3.** The corrected calculation reveals a geometry-fixed PH-breaking that generates m_e at
the right magnitude with no new parameter. → **Favourable; flag for independent replication** and
hand any mass-mechanism construction to a separate later gate. Do not build it here.
**SC-KAUD-4.** App K or the BCT fermion action is not defined well enough to recompute the band /
Green's function. → **Halt and report;** the action must be pinned first.

**If the outcome matches no stop condition, record it as a prompt defect.** **No stop condition
licenses a favourable conclusion, and none licenses an unfavourable one.**

## 7 — DELIVERABLE

Digest or refusal · **search-space coverage first** (where App K actually lives; note it is a
recovered draft) · verdict first · the cold NN count · T1 / T2 / T3 recomputations with the
corrected band, G_loc(0), and self-energy magnitude · the photon/graviton-corollary check · the
n=16 null-model · the steelman · CN-KAUD notices tiered PROVEN / CONJECTURE / ASSERTED / FALSIFIED
· scripts (deterministic) · contamination statement · **§0.5 reproduced verbatim** · what the gate
did **not** establish (it does not supply a PH-breaking mass mechanism).

**Revise notices clause by clause.** **At close, produce a `git format-patch` adding the
deliverable, scripts and as-run prompt under `audit/gates/KAUDIT/`. Do NOT modify `audit/NEXT.md`.**

*Written 15 September 2026. Not executed. Pre-register before use.*
