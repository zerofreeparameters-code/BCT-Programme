#!/usr/bin/env python3
"""Gate VOID, §2.3 and §2.4 — Letter 127 re-evaluation and the p_void arithmetic.

Everything other than the void volume and the void eigenvalue is held exactly
as the corpus states it (tex/BCT_Letter127_EWQCDScales_v2.tex, BCT_GP_STATE_SAVE.md,
BCT_Master_State_v35_update.md):

    S_EW  = pi^5/12,  S_QCD = pi^5/24
    alpha0 = r_oct * r_tet / pi
    NLO    = alpha0 * (4 pi + 1) / pi^2
    x_EW   = mu_oct * V_oct / S_EW  * (1 + NLO)                      [GP_STATE_SAVE; L127 abstract]
    x_SU3  = 2 * mu_tet * V_tet / S_QCD * (1 - NLO)                   [GP_STATE_SAVE, NLO only]
    x_SU3  = 2 * mu_tet * V_tet / S_QCD * (1 - NLO) * (1 - NLO (1 - 8 alpha0)/4)   [L127 eq. (xSU3), NNLO]

with the three substitutions fixed by the gate card:
    (i)   corpus:   mu = pi^2/R^2 (inscribed ball),   V = 4 pi R^3 / 3 (inscribed ball)
    (ii)  true V:   mu = pi^2/R^2,                     V = true chamber volume
    (iii) true both: mu = per-chamber Neumann-window eigenvalue (void_eigen.py), V = true chamber

Letter 127 v2 also prints a different closed form for x_EW in its boxed
equation, x_EW = 1/3 + pi alpha0 / 7 = 0.33666, that does not come from the GP
integral at all; it is evaluated here for the record only.

Targets (read AFTER void_numbers.txt was hashed; see gate_VOID_RESULT.md):
    App AY back-solved x_EW: 0.33934 (GP_STATE_SAVE) / 0.33663 (Letter 127 v2)
    App AY back-solved x_SU3: 0.71959
"""
from __future__ import annotations

import sys
import mpmath as mp
import sympy as sp

mp.mp.dps = 60

# --- corpus constants, exact -------------------------------------------------
R_OCT = (sp.sqrt(2) - 1) / 2
R_TET = (sp.sqrt(6) - 2) / 4
S_EW = sp.pi ** 5 / 12
S_QCD = sp.pi ** 5 / 24
ALPHA0 = R_OCT * R_TET / sp.pi
NLO = ALPHA0 * (4 * sp.pi + 1) / sp.pi ** 2
NNLO_FACTOR = 1 - NLO * (1 - 8 * ALPHA0) / 4

# --- true chamber geometry (from void_geometry.py, repeated here so the file is standalone)
V_TET_TRUE = sp.sqrt(2) / 12 - sp.acos(sp.Rational(23, 27)) / 6
V_OCT_TRUE = sp.sqrt(2) / 3 - sp.asin(sp.Rational(1, 3))
V_TET_BALL = sp.Rational(4, 3) * sp.pi * R_TET ** 3
V_OCT_BALL = sp.Rational(4, 3) * sp.pi * R_OCT ** 3
MU_TET_BALL = sp.pi ** 2 / R_TET ** 2
MU_OCT_BALL = sp.pi ** 2 / R_OCT ** 2


def N(e, dps=60):
    return mp.mpf(str(sp.N(e, dps + 10)))


def x_ew(mu, V):
    return mu * V / N(S_EW) * (1 + N(NLO))


def x_su3(mu, V, nnlo=False):
    v = 2 * mu * V / N(S_QCD) * (1 - N(NLO))
    return v * N(NNLO_FACTOR) if nnlo else v


def evaluate(mu_oct_true, mu_tet_true):
    """mu_*_true: per-chamber Neumann-window eigenvalues from void_eigen.py (mpf)."""
    rows = {}
    rows["(i) corpus"] = dict(
        x_EW=x_ew(N(MU_OCT_BALL), N(V_OCT_BALL)),
        x_SU3_NLO=x_su3(N(MU_TET_BALL), N(V_TET_BALL)),
        x_SU3_NNLO=x_su3(N(MU_TET_BALL), N(V_TET_BALL), nnlo=True),
    )
    rows["(ii) true V, ball mu"] = dict(
        x_EW=x_ew(N(MU_OCT_BALL), N(V_OCT_TRUE)),
        x_SU3_NLO=x_su3(N(MU_TET_BALL), N(V_TET_TRUE)),
        x_SU3_NNLO=x_su3(N(MU_TET_BALL), N(V_TET_TRUE), nnlo=True),
    )
    rows["(iii) true V, true mu"] = dict(
        x_EW=x_ew(mu_oct_true, N(V_OCT_TRUE)),
        x_SU3_NLO=x_su3(mu_tet_true, N(V_TET_TRUE)),
        x_SU3_NNLO=x_su3(mu_tet_true, N(V_TET_TRUE), nnlo=True),
    )
    rows["L127 boxed (not GP)"] = dict(x_EW=N(sp.Rational(1, 3) + sp.pi * ALPHA0 / 7))
    return rows


def hierarchy_scale(S, x, m_P_GeV=mp.mpf("1.220890e19")):
    """scale = m_P exp(-S/(1-x)); returns None if x >= 1 (formula undefined)."""
    if x >= 1:
        return None
    return m_P_GeV * mp.exp(-S / (1 - x))


# --- §2.4 p_void -------------------------------------------------------------
P_VOID_EXPR = sp.tanh(1 / sp.sqrt(2)) ** 2 + R_TET ** 2 * R_OCT / sp.pi ** 2
P_FLOOR_EXPR = sp.tanh(1 / sp.sqrt(2)) ** 2
VOID_FRACTION_GEOM = 1 - sp.pi / (3 * sp.sqrt(2))


def p_void_40():
    return (mp.nstr(N(P_VOID_EXPR), 40), mp.nstr(N(P_FLOOR_EXPR), 40),
            mp.nstr(N(R_TET ** 2 * R_OCT / sp.pi ** 2), 40), mp.nstr(N(VOID_FRACTION_GEOM), 40))


def main(mu_oct_true, mu_tet_true):
    print("# Gate VOID §2.3 — Letter 127 x re-evaluation (60 dps, printed to 10)")
    print(f"S_EW={mp.nstr(N(S_EW),12)} S_QCD={mp.nstr(N(S_QCD),12)} alpha0={mp.nstr(N(ALPHA0),12)} NLO={mp.nstr(N(NLO),12)} NNLO_factor={mp.nstr(N(NNLO_FACTOR),12)}")
    print(f"mu_oct_ball={mp.nstr(N(MU_OCT_BALL),12)} mu_tet_ball={mp.nstr(N(MU_TET_BALL),12)} mu_oct_true={mp.nstr(mu_oct_true,12)} mu_tet_true={mp.nstr(mu_tet_true,12)}")
    print(f"V_oct_ball={mp.nstr(N(V_OCT_BALL),12)} V_oct_true={mp.nstr(N(V_OCT_TRUE),12)} V_tet_ball={mp.nstr(N(V_TET_BALL),12)} V_tet_true={mp.nstr(N(V_TET_TRUE),12)}")
    rows = evaluate(mu_oct_true, mu_tet_true)
    for k, d in rows.items():
        print(f"{k:24s} " + "  ".join(f"{kk}={mp.nstr(v, 10)}" for kk, v in d.items()))
    print("\n# §2.4 p_void arithmetic (40 digits)")
    p, pf, dp, vg = p_void_40()
    print(f"tanh^2(1/sqrt2) + r_tet^2 r_oct/pi^2 = {p}")
    print(f"tanh^2(1/sqrt2)                      = {pf}")
    print(f"r_tet^2 r_oct/pi^2                   = {dp}")
    print(f"geometric void fraction 1-pi/(3sqrt2) = {vg}")
    return rows


if __name__ == "__main__":
    mo = mp.mpf(sys.argv[1]) if len(sys.argv) > 1 else mp.mpf("146.236549832")
    mt = mp.mpf(sys.argv[2]) if len(sys.argv) > 2 else mp.mpf("434.977196795")
    main(mo, mt)
