# ADDENDUM — ROUTE C RECONCILIATION: public-repo clone findings (16 Sep 2026)

Added after a shallow clone of the PUBLIC repo (zerofreeparameters-code/BCT-Programme @ b588f1b)
and a primary-source search. Sharpens the desk check; does not replace it.

## Finding 1 — the gate deliverables are not public
`audit/gates/` in the public repo contains: C1, INT, JHF, KAUDIT, LINK, MAD, MP, PRED, PRED2,
PROMOTE, PSI2, RANK, RATIO, TANH, XI, YM2. **No T/, IG/, BZ/, QP/, AM/, N/, R2/.** The two
confirmations therefore cannot run against the public repo — they need the LOCAL ~/BCT-Programme,
BCT-Programme-PRIVATE, or the original Gate T/IG/BZ threads.

## Finding 2 — the specific Route C artifact was not located in public sources
`G_ind = 0.984752 ℓ_P²` (truncated-octahedron BZ integral) returns NO hits in the public .tex.
Its primary source is elsewhere (private repo / volume-PDF zips / IG thread).

## Finding 3 — THREE distinct Newton's-constant derivations exist; do not conflate
1. **Letter 20** (`BCT_Letter20_GR_AllOrders.tex`): quantum-potential → Gauss-Bonnet → Einstein-Hilbert,
   `G = c⁴/(8π K_BCT)`. This is the route **Gate QP closed** (√−g R = −6 Ω □Ω, zero fluid content).
2. **Letter 37** (`BCT_Letter37_NewtonsConstant.tex`): instanton amplitude
   `m_P = Λ_QCD e^{S_QCD}`, `S_QCD = (π⁵/6)(1 − r_tet + α₀/2) = 45.461`. NOT a BZ integral, NOT a
   heat-kernel. Its "verification" is circular (`S_obs = ln(m_P/Λ_QCD)` needs m_P) — the **Gate MP**
   Planck-mass-circularity route.
3. **Route C / Gate IG** BZ-integral induced-G `0.984752 ℓ_P²` — no public primary source found.

The ONLY "Brillouin-zone integral" visible in the public corpus (Letter 20, line 455) computes
`S_D4 = π⁵/6` — the instanton action feeding Letter 37 — **not G directly.**

## Consequence for the reconciliation
The open-item-6-vs-CN-BZ contradiction may be a symptom of a deeper **three-way conflation** across
Letters 20/37 and the IG thread. Before applying any "Route C closed" ledger edit, Reconciliation 2
should FIRST pin down which induced-G object Route C/Gate IG actually refers to:
- If Route C = the Letter-20 QP curvature identity → already closed by Gate QP (redundant with QP).
- If Route C = the Letter-37 instanton `S_D4` BZ sum → that is a lattice sum feeding m_P, audited by
  Gate MP (circularity), NOT an induced-G momentum integral; CN-BZ's "heat-kernel" critique may not
  even apply to it.
- If Route C = a genuinely separate one-loop induced-G with `0.984752 ℓ_P²` → locate its source
  (private/threads) and only then classify its measure (heat-kernel vs BZ) per Reconciliation 2.

## Mac commands to finish the confirmation (run in ~/BCT-Programme; add the PRIVATE checkout if separate)
```
cd ~/BCT-Programme
# locate the Route C / IG induced-G artifact wherever it lives (local may have more than public)
grep -rilE '0\.984752|G_ind|truncated octahed|induced.*(G_N|newton)' . ../BCT-Programme-PRIVATE 2>/dev/null
# classify its integral measure once found: BZ momentum integral vs proper-time heat-kernel
#   look for \int d^3k / \int_{BZ}  vs  \int ds/s Tr e^{-s...}
# Gate T primary: confirm area-law kappa is direction-DEPENDENT (no single eta)
grep -rilE 'area.?law|entanglement.*entropy|kappa|\\kappa|directional|no single' . 2>/dev/null | grep -iE 'gate.?T|area|entangle'
```

*Bottom line: the reconciliation is not blocked, but it is bigger than a two-entry cleanup. Do not
apply "Route C closed" until the IG object is identified against the local/private source — otherwise
the ledger risks recording a closure of the wrong object.*
