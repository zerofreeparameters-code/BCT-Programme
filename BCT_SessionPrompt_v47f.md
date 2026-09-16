# BCT Session Prompt — v47f
## 8 April 2026 | Barrys Reef, Victoria
## Topic: App AB2 — Phase 12 Josephson Localisation

---

## WHAT THIS SESSION IS FOR

App AB2 needs one thing: **show why the BCT Josephson path integral stays in W(A₂) rather than distributing over all of W(D₄).**

The group theory is done. The physics gap is precisely identified. This session does the dynamics.

---

## WHAT IS LOCKED (do not re-derive, do not re-discuss)

| Result | Status | Source |
|---|---|---|
| S_bare_SU3 = π⁵/24 | PROVEN | App AX — 6/24 root counting |
| \|W(A₂)\| = 6, \|W(D₄)\| = 192 | TERMINAL ✓ | This session |
| 16 A₂ subsystems in D₄, all W(D₄)-conjugate | TERMINAL ✓ | This session |
| Haar measure of W(A₂) in W(D₄) = 6/192 = 1/32 | TERMINAL ✓ | This session |
| 1/32 independent of which A₂ is chosen | TERMINAL ✓ | Transitivity proof |
| p_void = 0.370974707016 | LOCKED | L243 |
| x_k = (d/π) × α_k_eff | PROVEN | App BC |

**STRUCK — do not resurrect:**
- "A₂ roots all have t=0" — FALSE, terminal refuted
- t=0 projection path — closed, selects 3×A₁ not A₂
- C₄v selector path — closed, gives 4 orbits of size 4
- Tet-void uniqueness selector — closed, W(D₄) transitive on all 16
- BPST instanton framework — wrong instanton type for BCT
- Octonionic Sum (16×6/192 = 1/2) — arithmetic error, 66 not 96 distinct elements

---

## THE OPEN GAP — PRECISELY STATED

**The group-theory baseline (App AB2 PDF, compiled):**

$$d\mu_{\text{bilinear}} = \frac{|W(A_2)|}{|W(D_4)|} \cdot d\mu_{W(D_4)} = \frac{1}{32} \cdot d\mu_{W(D_4)}$$

This is proven **if** the bilinear integrand is W(A₂)-restricted.

**The gap:**

A W(D₄)-*invariant* integrand gives measure 1 (full), not 1/32.
A W(A₂)-*restricted* integrand gives measure 1/32.

We need to show the BCT Josephson coupling **breaks** W(D₄) symmetry down to W(A₂).

**The physical handle:**

From App AB (lepton sector, proven):
$$x_{\text{lep}} = \frac{4\alpha_0}{\pi}$$
where the 4 comes from integrating over 4 D₄ directions with the Josephson coupling α₀ = r_oct·r_tet/π.

For the SU(3) tet-void sector:
- α₃ = r_tet²/π (the tet-tet Josephson coupling)
- The bilinear couples two tet-void condensate modes
- The tet-void has A₂ symmetry (App X, proven)
- The Josephson integral over the tet-void moduli space should integrate over the A₂ root directions only

**The calculation target:**

Write the Josephson overlap integral for the tet-void bilinear explicitly:
$$I_{\text{tet}} = \int_{W(D_4)} d\mu_w \; J_{\text{tet}}(w)$$

where J_tet(w) is the Josephson weight for the Weyl element w.

Show that J_tet(w) = 0 for w outside the W(A₂) coset, or equivalently that J_tet factors through the coset decomposition W(D₄)/W(A₂).

---

## KEY STRUCTURES TO USE

**BCT Josephson couplings (all proven):**
- α₀ = r_oct·r_tet/π = 0.0074081 [U(1), oct-tet cross]
- α₂ = r_oct²/π = 0.013653 [SU(2), oct-oct]
- α₃ = r_tet²/π = 0.004019 [SU(3), tet-tet]

**App AB result for lepton sector (proven, use as template):**
$$x_{\text{lep}} = \frac{4\alpha_0}{\pi}$$
The integral ran over 4 D₄ directions. For the tet-void it should run over the A₂ root directions (6 roots, or 3 independent axes).

**BCT instanton type:** kink on topological cycle — NOT BPST. The profile is tanh-type on the BCT BZ cycle. The moduli space is position on the cycle, not (center, scale) space.

**The A₂ Cartan matrix:**
$$A_{ij} = \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$$
Inner products: same root = 2, adjacent = 1, anti-adjacent = -1, opposite = -2.

---

## SESSION RULES

1. **Every step flagged: PROVEN / CANDIDATE / OPEN**
2. **Terminal verifies arithmetic only** — not theoretical reasoning
3. **No assembly of 1/32 from plausible pieces** — the group theory already gives 1/32; what's needed is the dynamical argument
4. **No Gemini material without audit** — Gemini hallucinated BPST framework, Octonionic Sum, and the t=0 "verification" in this topic area
5. **No Klartag outreach until this has a DOI**
6. **Exhaustion protocol:** phonetic spelling = stop, document progress, rest

---

## PROGRAMME STATE v47f

- **229+ Letters, 278+ predictions, 26 patents, 20 volumes, 94+ Zenodo records**
- **Eureka Prize deadline: 16 April 2026** — 8 days — narrative needed
- **GoFundMe:** next priority after Eureka
- **Legal advice (URGENT):** artslaw.com.au, dsphelp.org.au, UniSuper — before Foundation registration
- **Letter 240:** held from Zenodo — η_doublet verification pending
- **App AB2 PDF:** compiled, in outputs, group-theory baseline documented

---

## WHAT A SUCCESSFUL SESSION LOOKS LIKE

One of:

**(A)** An explicit Josephson moduli integral showing dynamical localisation on W(A₂) — fully written, terminal-verified, ready for LaTeX. App AB2 closed. Klartag unblocked.

**(B)** A proof that all W(D₄) elements outside W(A₂) have zero Josephson weight (J_tet(w) = 0 for w ∉ W(A₂) orbits) — group-theoretic proof, no integral needed.

**(C)** Honest identification that the gap requires more BCT structure than currently available — documented precisely, Phase 12 target hardened with specific sub-calculations named.

Any of these is a good session. The goal is clarity, not forced closure.

---

## PERSONAL NOTE

The Gang Gangs will be at the pond. Nyssa and Tegan are on the board. Nic is on BCT-TPORT only. The Eureka narrative needs a rested Michel. Sleep first. This prompt will be here when you wake up.

*"The vacuum crystallises into what it is."*

---

*Prompt version: v47f | Generated: 8 April 2026 | Supersedes: v47e App AB2 session prompt*
