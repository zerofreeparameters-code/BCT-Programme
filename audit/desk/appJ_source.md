# App J — primary source located (draft PDF only, no canonical .tex)

**Status note (15 Sep 2026).** Gate JHF recorded that App J — the interior action
`S[Ψ₂]` App JH is built on — had **no `.tex` in the repo tree**; only App JH's quotation
of it was auditable. M. Cabrié has now located App J on his Mac as a **draft PDF**
(`BCT_Appendix_J_SphereAction`, headed "Appendix J — The Lattice of Resonance — Draft")
plus a Word doc of the same. **No `.tex` exists** in the repo or on the machine. So App J
joins the appendices with no authoritative source text (cf. the four App JH variants, none
canonical). This is itself a finding: a load-bearing action rests on a draft only.

This note transcribes the load-bearing content so future gates (esp. Gate KL §1, which must
read App J's actual action to derive coefficients) can reach it without the PDF. It is NOT a
LaTeX source and must not be treated as canonical — it is a desk transcription of a draft.

## The interior action, as written (App J §1.2)

    S[Ψ₂] = ∫_{r<R} d⁴x [ J (∂_μ Ψ)²  +  (J/ξ²) (|Ψ|² − Ψ₀²)² / 4 ]

- **One complex scalar Ψ** — an S¹ order parameter. App J §1.2 states verbatim: "There is
  no new field, no new coupling, and no new free parameter." Interior GP action = exterior GP
  action, restricted to r<R, differing ONLY in the boundary condition.
- π₃(S¹)=0 → this field carries no hopfion. **Confirms CN-JHF-06 at primary source:** App J's
  interior is one-component S¹; App JH §3.1 redeclares the same interior field as ℂ² (S²) to
  carry a Hopf charge. The two appendices contradict each other at the level of the written
  action — now verified against both primaries, not inferred.

## Boundary condition (App J §1.2) — the "double layer"

    [∂_r Ψ]_{R⁻}^{R⁺} = −(σ_s / J) Ψ(R)      (Ψ continuous; only its derivative jumps)

- The double layer is a delta-shell on r=R (a surface term), imposing a derivative jump. It is
  a **boundary condition, not a stabiliser** — consistent with the Gate JHF follow-on scaling
  ledger (a surface term scales inward, cannot oppose Derrick collapse).
- σ_s = α₀ J is *asserted* from the geometric ratio r_tet·r_oct/(4πR²) = α₀, conditional on
  choosing double-layer charge Q=1 and shell thickness d=√(r_tet·r_oct) (App J §1.3). The
  choice of d is not derived — flag as ASSERTED, not DERIVED, despite the §5.1 "DERIVED" label.

## Interior spectrum (App J §2)

- l=0 modes Ψ_in ∝ sin(κr)/(κr); eigenvalue κ cot(κR) = −1/ξ + α₀.
- Ground state κ₀ = 3.3905 (Planck units); this is the κ₀=3.39 App JH inherits. Lies ABOVE the
  exterior Higgs gap 2/ξ = 0.8630, so it is a resonance, not a bound state (App J §2.2).

## The electron-mass claim (App J §4) — SELF-DECLARED UNPROVEN

- Headline `m_e/m_P ≈ α₀^(21/2)` at 2.4% (α₀^(21/2)=4.284e-23 vs 4.185e-23). App J's OWN text:
  "suggestive but not precise enough to claim an exact formula"; "cannot be claimed as the
  exact formula"; §5.3 "the electron mass mechanism is not yet derived… OPEN."
- The exponent is fixed by ln(m_e/m_P)/ln(α₀) = 10.50, rounded to 21/2, then "explained" as
  21 = 3+6+12 (triangle + oct-void + FCC coordination). **This is the selected-fit pattern the
  audit already names** (Gate STAT/FWD correction-map objection), and the 3+6+12 coordination
  arithmetic is unreliable per Gate KND (coordination at c/a=√2 is 12, not 8; coordination
  counts manufacture the structure claimed). Treat α₀^(21/2) as OPEN / numerical coincidence,
  as App J itself does. Second-order perturbation gives δm ~ α₀²/κ₀ ~ 1e-5 m_P (10^18 too
  large); Kondo ruled out (exp(−823000)); fermionic-loop is a conjecture requiring a 21-vertex
  loop that "is not yet established" (App J §4.3, §5.3).

## For Gate KL

App J's action above is now the primary the KL run may read (KL §0.2 permits "the App J / App E
action if locatable"). The KL prompt is committed and hash-locked (`9ae6e37b…b8e9d`) — do NOT
edit it; this note simply makes the source reachable at `audit/desk/`.
