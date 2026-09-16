# Gate THETA — Addendum: the quark mass matrix, written down

**Purpose.** Corrects one overstated sentence in `gate_THETA_RESULT.md` and replaces it with the explicit matrices and a cold numerical demonstration. **Verdict unchanged: SC-THETA-1 — θ_QCD = 0 imported / CONJECTURE.** Within-thread, CONJECTURE-capped (Whopper). Prompted by Michel: "check this and write it down."

## Update — App JG6 subsequently provided and read (does not change verdict)

App JG6 ("CKM CP Phase: Non-Perturbative BCT Yukawa Assessment", Phase 76B, Feb 2026; SHA-256 `ab97bf077104b89593f733cef6687c2d07756fc04e3cc1bcc9ea7bf6fcada5f9`) — flagged below as TOC-only — was uploaded mid-thread and read. **It does not do the Barr job.** JG6 produces a *number* for δ_CKM by two routes, neither of which is a complex quark mass matrix:
- **GT formula** (arithmetic verified, `jg6_check.py`): δ = π/2 − arctan(r_tet/r_oct) + arctan(√α₀) = **1.1595 rad, −3.0%** — a best-of-family scalar fit ("exhaustive search over D4h-motivated combinations of r_oct, r_tet, α₀"), not even sub-1%.
- **"Phase 26 definitive"**: δ = 1.197 rad (+0.08%) from "the full BCT CKM matrix elements derived from the **Wolfenstein parameterisation** with BCT-predicted input observables" — i.e. the phase inserted into the unitary V_CKM, populated with BCT angles (the inherited, non-independent route already flagged by Gate MIX/PRED2).

JG6 computes **no M_q, no arg det M_q, and does not address θ ∈ {0,π}**. It explicitly defers the actual object: *"Full non-perturbative BCT Yukawa tensor: Phase 77 target."* So the CP phase is confirmed to live **in V_CKM as an assigned value**, decoupled from any written-down mass-matrix texture whose arg det could be tested against zero — exactly the situation this addendum describes. The "referenced but absent" characterisation below is superseded by "present, read, does not resolve Barr"; the three THETA sub-questions remain unresolved. **SC-THETA-1 stands.**

**Deferral chain closed (App JO6, "Phase 77 Review"; SHA-256 `a8bdbfaa661dd9ce3b1d497afbaf8446490f1d6440617a379d1470e8163deaf3`, uploaded mid-thread).** Phase 77 did **not** deliver the Yukawa tensor JG6 promised for it. JO6 contains zero mentions of Yukawa, CKM, CP, θ, or mass matrix — Phase 77 delivered vector-meson spectroscopy (m_K\*, m_φ, Γ_ρ, g_ρππ), domain-wall dark matter, proton spin, and g−2 HVP instead. The Phase 78 roadmap in JO6 (m_K\* sub-1%, κ_p, DW simulation, F/D values, HVP integral) does not schedule it either. So the complex quark Yukawa texture needed to *attempt* Barr was promised (76B) → deferred (Phase 77 target) → dropped (Phase 77 delivered other physics) → unscheduled (Phase 78). It is not merely unbuilt; it was abandoned mid-programme. Strengthens, does not change, SC-THETA-1.

## Correction (Cold Ledger honesty)

The THETA result claimed **"no quark mass matrix M_q is written down anywhere."** That is **FALSE and is retracted.** The corpus does write down fermion textures:
- **App EL** ("Yukawa Matrix: Complete Fermion Mass and Mixing Structure", Part2) — body present.
- **App AD** ("Democratic Mass Matrix", Part1) — body present.
- **App IQ5** ("The BCT Yukawa Matrix: D4h Crystal Symmetry") and **App JG6** ("CKM CP Phase: Non-Perturbative BCT Yukawa") — **referenced in the TOC, bodies ABSENT from the provided mount.**

The corrected finding is stronger, not weaker.

## What is actually written down — and it is REAL

**App EL** gives diagonal Yukawas Y^diag = diag(m)/v and, in EL.4, the CKM texture explicitly:

    V_CKM = U_u† U_d ,   U_u ≈ 1 (identity),
    U_d  = real rotation, θ_d = arctan(|V_us|) = 12.57°, 1–2 sector.

Everything is real. Reconstructed mass matrices:

    M_u = diag(m_u, m_c, m_t)                         (real)
    M_d = U_d(12.57°) · diag(m_d, m_s, m_b)           (real orthogonal × real diagonal)

**App AD** gives a real rank-1 democratic matrix:

    M₀ = m_BCT · (w ⊗ wᵀ),  w = (1, 1, √2)  →  [[1,1,√2],[1,1,√2],[√2,√2,2]]   (real symmetric).

Both textures are **real**. A real quark texture has two automatic consequences:
- arg det M_q = 0  ✓ (trivially — a real matrix has real determinant), **and**
- J_CKM = 0        ✗ (a real V_CKM is orthogonal ⇒ δ_CKM = 0 ⇒ no CP violation).

**Verified cold** (`argdet_crux.py`, mpmath 50 dps): with the real texture (δ = 0), **J = 0.0 exactly**. With δ = arccos(1/3), **J = 3.18×10⁻⁵** (matches the corpus headline 3.08×10⁻⁵, §9.4). So the one explicit quark texture in the mount (EL) is CP-conserving and **cannot** be the origin of the claimed δ_CKM = arccos(1/3). The CP phase is inserted directly into the already-diagonal unitary V_CKM in §9.3–9.4 ("the T_d quaternion structure acting on the CKM unitary matrix"), not produced by any written-down complex mass matrix. The appendix titled to do that job — **JG6, "CKM CP Phase: Non-Perturbative BCT Yukawa"** — is **not in the corpus** to check.

## The deeper point: arg det M_q is NOT a function of the real masses

θ̄ = θ_QCD + arg det(M_u M_d) is a physical parameter **independent** of the quark masses and of the CKM matrix. {J, θ̄} are independent CP invariants of the quark sector — neither determines the other, and neither is fixed by the (real, positive) physical masses.

**Demonstration** (cold, `argdet_crux.py`). Fix M_u = diag(real). Write M_d = V_CKM · diag(m_d,m_s,m_b) · W†, where W is a **right-handed** unitary — physically unobservable (it does not enter the W-boson couplings, does not change V_CKM, does not change J). Then arg det(M_u M_d) = −arg det W is whatever W's phase is:

| choice of right-handed W | masses | V_CKM | J | **arg det(M_u M_d)** |
|---|---|---|---|---|
| W = I | identical | identical | 3.18×10⁻⁵ | **0 rad** |
| W = diag(e^{i·0.7}, 1, 1) | identical | identical | 3.18×10⁻⁵ | **0.7 rad** |
| W = diag(e^{i·1.9}, 1, 1) | identical | identical | 3.18×10⁻⁵ | **1.9 rad** |
| W = diag(e^{−i·2.4}, 1, 1) | identical | identical | 3.18×10⁻⁵ | **−2.4 rad** |

Identical masses, identical CKM, identical CP violation — yet arg det M_q (hence θ̄) takes any value. **θ̄ is free.** Therefore "all quark masses are real ⇒ arg det M_q = 0" is a non-sequitur: arg det M_q is set by the right-handed rotations and the overall Yukawa phase, which BCT never specifies. (Aside, also verified: det V_CKM = 1 for any δ — the CP phase never enters det V_CKM. That is precisely why arg det can be 0 while J ≠ 0, i.e. why a Nelson–Barr texture is *possible* — but it must be *built and protected*, not read off real masses.)

## Corrected statement for the ledger / RESULT

Replace the retracted sentence with:

> The corpus writes down quark/fermion textures (App EL, App AD), but every one whose body is in the mount is **real** — so it yields arg det M_q = 0 and J_CKM = 0 *together*, i.e. it is CP-conserving and cannot produce the claimed δ_CKM = arccos(1/3). The appendix that would carry a complex, Barr-compatible quark texture (App JG6) is referenced but absent. And θ̄ = θ_QCD + arg det(M_u M_d) is provably independent of the real masses and of V_CKM (right-handed-rotation demonstration), so "real masses ⇒ arg det M_q = 0" is a non-sequitur regardless.

## Net

SC-THETA-1 stands. θ_QCD = 0 remains a CONJECTURE (parity / Nelson–Barr *class*; the Barr tightrope is open and, on the written textures, not attempted). To close it, BCT must exhibit App JG6's complex quark texture explicitly and show, from that one texture: (a) arg det(M_u M_d) = 0, (b) J_CKM ≠ 0, (c) radiative protection — the standard Nelson–Barr requirements. Does not touch the geometry.

*Scripts: `argdet_crux.py` (mpmath, 50 dps). Sources: App EL (Part2, hash 7a09746…), App AD (Part1, plain text), Monograph §9.3–9.4/§11 (hash b057829…). TOC-only absences: IQ5, JG6 (Part1).*
