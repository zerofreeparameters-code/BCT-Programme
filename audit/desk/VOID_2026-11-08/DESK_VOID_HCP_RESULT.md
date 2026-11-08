# Desk-check VOID-HCP: does the void-network fluid choose FCC over HCP?

**Date:** 8 November 2026, evening (Melbourne). Claude Opus 5.5, same chat as Gate TWIST and the VOID checks.
**Status:** desk-check, **not a gate**. Same-session work is capped at **CONJECTURE**; re-run it cold before moving any tier.
**Scripts:**
- `desk_VOID_hcp.py` (part 1) → `desk_VOID_hcp_output.txt`
- `desk_VOID_hcp2.py` (part 2, matched grid) → `desk_VOID_hcp2_fine_output.txt`, `desk_VOID_hcp2_coarse_output.txt`, `desk_VOID_hcp2_coarse_w10000_output.txt`

Each run takes about 5 to 15 minutes on 1 core.

## The question
Touching equal spheres pack equally densely (74.05%) as FCC (stacking ABC, which is BCT's lattice) or as HCP (stacking AB). The membrane check ended with "FCC versus HCP needs a tie-breaker". **Does the void-network fluid of VOID-Q1 prefer one of them?**

**The geometric difference:**
- In **FCC** every octahedral void opens only into tetrahedral voids.
- In **HCP** the octahedral voids are stacked in columns along c, 0.8165 a apart, and each pair **shares a triangular face**. That never happens in FCC.

## Part 1: a first comparison, which turned out to be a grid artefact
Part 1 compared an HCP cell with the cubic FCC cell used in Q1, at the same grid spacing. It reported HCP's octahedral level **+0.84 higher** than FCC (+1.24 at wall 10000).

That difference turned out to be a **sampling artefact**:
- The two grids place the sphere surfaces at different sub-cell offsets.
- A shift of a few per cent of one grid step in the effective sphere radius moves the level by about 1 unit.
- The give-away was that two symmetry-equivalent HCP columns already differed by 0.066 inside the same run.

(The word "weakly" in part 1's Reading block is also a mislabel. U/t_c ≈ 3 there means the columns are *not* locked into a Mott state.)

## Part 2: matched-grid control
Both packings were built as stacks of the **same triangular layers on the same grid**, with every sphere centre on a grid node. An octahedral cage between layers A and B is then **bit-identical** in HCP and FCC. Only what lies beyond its faces differs, so any difference is physics.

| Wall 3000 | HCP | FCC | HCP − FCC |
|---|---|---|---|
| on-site level e₀ (fine, h ≈ 0.022) | 128.33265 | 128.33260 | **+0.00005** |
| band bottom (fine) | 128.30082 | 128.33133 | **−0.0305** |
| on-site level e₀ (coarse, h ≈ 0.029) | 128.54581 | 128.54885 | −0.003 |
| octahedral hopping (fine) | t_c = **0.0157** (column, through the face) | t = **1.26×10⁻⁴** (matches Q1's 1.3×10⁻⁴) | ratio **124** |
| octahedral hopping (coarse) | t_c = 0.0158 | — | converged |
| wall 10000 (coarse): e₀ and t_c | e₀ diff −0.003; t_c = 0.0084 | Q1: t = 2.9×10⁻⁵ | ratio ≈ 290 |

**Reading.**
1. **The cages are identical in energy** to 5 parts in 10⁶, as they must be: same six spheres, same windows.
2. **The only difference is hopping.** HCP's face-sharing columns couple 120 to 290 times more strongly than any FCC pair.

## What that does to the fluid
- **Energy: HCP is lower.** With identical on-site levels, adding hopping can only lower a boson ground state (positive amplitudes, Perron–Frobenius). HCP's two strong column bonds outweigh FCC's six extra weak bonds by a wide margin.
  - Low filling: HCP lower by 2t_c ≈ **0.03** per particle.
  - Mott liquid at n̄ = 1: virtual hopping gains Σt² n̄(n̄+1)/U. That is 4.9×10⁻⁴ against 1.9×10⁻⁷ in FCC (×2600), so HCP is lower by ≈ **5×10⁻³ per void**, about 3% of g n₀.
- **The liquid: FCC keeps it, HCP mostly loses it.** In HCP each column is a 1D chain with U/t_c = 11.9/n̄.
  - The 1D Mott state at n̄ = 1 needs U/t > 3.37 (DMRG, (t/U)_c = 0.297), so it survives at n̄ = 1.
  - It is lost by n̄ ≈ 2 to 3. A mean-field count over all bonds (U / Σt = 5.8/n̄ against 5.83) puts even n̄ = 1 at the edge.
  - In FCC, Q1's liquid holds up to n̄ = 4 to 11.

## Score (desk): **NO TIE-BREAKER, and it points the wrong way**
The void fluid **prefers HCP**. It gains energy from the face-sharing octahedral columns, which FCC lacks. FCC is where Q1's quantum liquid lives, but the fluid would rather stack AB.

So FCC stays an **input** of BCT, as it was before. It must now also be held against a small pull towards HCP, about 3% of g n₀ per void at n̄ = 1.

**Context.** For classical hard spheres FCC wins, by an entropy of 0.00115 k_B per sphere (Mau & Huse 1999). That is a finite-temperature effect, though, and it does not act at T = 0.

**Survives as geometric facts:**
- HCP's octahedral voids form face-sharing columns, with hopping about 120 to 290 times FCC's.
- The octahedral cage level itself is the same in both packings.

## Sources
- [Kühner, White & Monien, PRB 61, 12474 (2000): 1D Bose–Hubbard Mott tip (t/U)_c = 0.297 ± 0.010 (as tabulated in arXiv:1110.0743)](https://arxiv.org/abs/1110.0743)
- [Mau & Huse, Stacking entropy of hard-sphere crystals, PRE 59, 4396 (1999)](https://arxiv.org/abs/cond-mat/9810287)
