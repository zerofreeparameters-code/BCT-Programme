#!/usr/bin/env python3
"""Gate PRED — Step 3/4 scoring: expected sub-1% matches by chance vs observed; bits; search-effort correction."""
from mpmath import mp, binomial, mpf, log, nsum, inf
mp.dps=30
def P_ge(k,n,p): return nsum(lambda i: binomial(n,i)*p**i*(1-p)**(n-i), [k,n])
a0=0.0074080557
# per-attempt sub-1% success given a base within ±8% and the corpus's 24-value N menu (step-2 result)
q1=0.770; q01=0.247
print("Search-effort record (corpus's own): 94 phases; 457-473 appendices; revisit counts per quantity found:")
print("  T_c>=9 formulas, m_DM>=6, r_p>=6, m_e>=6, m_p>=4, sin2thW>=4, Koide angle>=4, m_rho>=4, v 4 loop-orders, 1/alpha 3, m_b 3, m_K 2, M_R 2")
print("  Level-1 (1-5%) mentions: see step-count; explicit 'Level-1 -> sub-1%' pipeline; N-class menu extended on demand (N=5 'NEW', N=-5 'NEW', N=-4).")
for T,natt in [(100,1),(130,1),(130,3),(180,3),(130,9)]:
    q=1-(1-q1)**natt
    exp_hits=T*q
    for obs in (92,28):
        if obs<=T:
            P=P_ge(obs,T,q); bits=-log(P,2)
            print(f"T={T:3d} attempts/target={natt}  per-target P(sub-1%)={q:.3f}  E[sub-1%]={exp_hits:6.1f}  observed={obs:3d}  P(X>=obs)={float(P):.3g}  surprise={float(bits):.2f} bits")
print("\nUPPER BOUND (counterfactual, not the corpus's procedure): 28 eligible sub-1% hits, each a single PRE-FIXED 3-atom expression, no correction layer, one attempt:")
p=0.108; print(f"  P = {p}^28 -> {float(-28*log(p,2)):.1f} bits   (only valid if every formula was fixed before its comparison and was the only one tried)")
print("  At 0.1% tolerance for the 11 sub-0.1% eligible hits, same counterfactual:", f"{float(-11*log(0.0115,2)):.1f} bits")
print("\nRealistic (corpus procedure: physically-motivated base within a few %, then a menu correction, >=3 attempts per quantity): ~0 bits.")
