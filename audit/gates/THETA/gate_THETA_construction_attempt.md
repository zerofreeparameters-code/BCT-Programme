# Gate THETA — Construction attempt: can the rescue be built from BCT ingredients?

**Within-thread desk-check, CONJECTURE-capped (Whopper). Verdict unchanged: SC-THETA-1.**
Prompted by Michel: "proceed." Attempts the Nelson–Barr checklist — write down complex M_u, M_d with (a) arg det = 0, (b) J ≠ 0, (c) radiative protection — and locates exactly where BCT-as-written fails. Script: `nelson_barr_attempt.py` (mpmath, 40 dps).

## The fork: reality vs Hermiticity

The strong-CP angle is θ̄ = θ_bare + arg det(M_u M_d). Two ways a symmetry can make arg det real:

- **M → M\* (reality)** — BCT's stated transformation (App DI step 2: "Under D4 Z₂: det M_q → det M_q\*"; §11.2 "all Yukawa couplings real"). A real vacuum forces M real.
- **M → M† (Hermiticity)** — the *parity* solution to strong CP (Babu–Mohapatra / left–right symmetric class). A Hermitian M has real determinant.

These are different branches, and only one carries CP violation. Demonstrated cold:

| branch | M_d structure | J_CKM | arg det M_d | outcome |
|---|---|---|---|---|
| **1. Reality** (BCT's M→M\*) | real symmetric | **0.0** | 0 | dead — no CP violation |
| **2. Hermiticity** (parity, M→M†) | Hermitian, complex off-diag (\|Im M_d[0,1]\|=0.61) | **3.18×10⁻⁵** | **0** | **both Barr conditions met** ✓ |

Branch 2 is an explicit existence proof: M_d = U · diag(m_d,m_s,m_b) · U† with U the BCT-phased CKM (δ = arccos 1/3) is Hermitian, has real positive determinant (arg det = 0), yet gives J = 3.18×10⁻⁵. So **θ̄ = 0 with J ≠ 0 IS constructible** — the mechanism exists.

## Why BCT-as-written cannot reach Branch 2

1. **Wrong transformation.** BCT states M → M\* (reality), which is Branch 1 (J = 0). The mechanism that works is M → M† (Hermiticity). BCT never invokes Hermiticity; its "real quark masses / real Yukawa couplings" language is precisely the dead branch.
2. **No field content for Hermiticity.** A Hermitian quark mass matrix is not generic — it is imposed by a **parity** relating left- and right-handed quarks (left–right symmetric structure: W_R, extra Higgs, the P operation Q_L ↔ Q_R). The Nelson–Barr alternative (impose CP, break it spontaneously, keep det real) instead needs **vector-like quarks** in the Bento–Branco–Parada texture. BCT has *neither*: its quarks are the six SM quarks with real scalar orbit masses m_q = m_t·exp(−S_Td·n_q/24), no left–right partners, no vector-like sector, no spontaneous-CP field. There is nothing to make M Hermitian.
3. **The {0, π} residue persists even in Branch 2.** Hermiticity gives det **real**, not real-**positive**: with one negative eigenvalue (same physical \|masses\|), arg det M_d = **π** (verified). So even the working branch lands on θ ∈ {0, π}; θ = π is experimentally excluded but not forbidden by Hermiticity — an even number of negative eigenvalues must be *separately* enforced. THETA sub-question 2 survives the rescue.
4. **Radiative protection (c) not reached.** Moot until (a)+(b) hold from real BCT structure; the parity solution is 1-loop-stable in principle, but that is a property of the L–R model, not derivable from BCT's stated ingredients.

## Conclusion

The rescue is **constructible for a different theory** (one with left–right parity or vector-like quarks), not for BCT as written. BCT's own symmetry statement (M → M\*) is the CP-conserving branch that kills J; to get θ̄ = 0 as a genuine output it would have to (i) replace reality with Hermiticity, (ii) supply the field content that makes the quark mass matrix Hermitian (a left–right sector) or the vector-like quarks for Nelson–Barr, and (iii) fix the sign of det to kill θ = π. Each is a new theoretical ingredient, not a wording fix — and (ii) would forfeit the "zero new fields" claim.

**SC-THETA-1 stands: θ_QCD = 0 is imported / CONJECTURE.** Now with a precise diagnosis — *wrong symmetry branch, missing field content* — and an explicit statement of what a real derivation would require. Does not touch the geometry.
