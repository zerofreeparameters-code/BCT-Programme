#!/usr/bin/env python3
"""Gate PRED — Step 4 sensitivity: alphabet and tolerance variants at the 2-atom level (fast) — coverage and hit rate."""
import numpy as np, math
src=open('pred_step2_nullmodel.py').read()
exec(src.split("L3=clean")[0])
tail=src.split("Lam=220.0; mpi0=134.9768")[1].split("names=list(T)")[0]; Lam=220.0; mpi0=134.9768; exec(tail)
names=list(T); tv=np.array([T[k] for k in names])
Nmenu=[3/8,3/4,1,3/2,2,9/4,3,4,5,6,8,9]; Nmenu=sorted(set(Nmenu+[-n for n in Nmenu]))
exec(src[src.index("def hit_stats"):src.index("for lab,vals in")])
def build(at):
    A=np.array(list(at.values())); L1=clean(unary(A)); L2=clean(binary(L1,L1))
    return clean(np.concatenate([L2,np.sqrt(np.abs(L2)),1/L2,L2**2]))
variants={
 'baseline (17 atoms)': atoms,
 'reduced: drop 5,8,9,12,sqrt3 (12 atoms)': {k:v for k,v in atoms.items() if k not in ('5','8','9','12','sqrt3')},
 'geometry-only: pi,sqrt2,sqrt6,roct,rtet,a0 + 1,2,3,4 (10 atoms)': {k:v for k,v in atoms.items() if k in ('1','2','3','4','pi','sqrt2','sqrt6','roct','rtet','a0')},
 'enlarged: +7,+10,+sqrt5,+e (21 atoms)': dict(atoms, **{'7':7,'10':10,'sqrt5':math.sqrt(5),'e':math.e}),
}
for lab,at in variants.items():
    V=build(at)
    for tol in (0.01,0.005,0.001):
        for wn in (False,True):
            p,cov=hit_stats(V,tol,wn)
            print(f"{lab:62s} |S2|={len(V):6d} tol={tol:<6} N={str(wn):5s} p_hit={p:.4f} cov={cov.sum()}/48")
