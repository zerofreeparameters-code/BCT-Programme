#!/usr/bin/env python3
"""Gate PRED — Step 3: per-target multiplicity and bits. Uses L3r.npy from step 2 and re-derives 2-atom set."""
import numpy as np, math
exec(open('pred_step2_nullmodel.py').read().split("L3=clean")[0])   # rebuild atoms, L1, L2, L2r
L3r=np.load('L3r.npy'); v3=np.sort(np.abs(L3r)); v2=np.sort(np.abs(L2r))
Lam=220.0; mpi0=134.9768
exec(open('pred_step2_nullmodel.py').read().split("names=list(T)")[0].split("Lam=220.0; mpi0=134.9768")[1])
names=list(T); tv=np.array([T[k] for k in names])
def count(v,t,tol): return int(np.searchsorted(v,t*(1+tol),'right')-np.searchsorted(v,t*(1-tol),'left'))
print("%-22s %10s %10s %10s %10s  %s"%('target','2at@1%','2at@0.1%','3at@1%','3at@0.1%','bits(one 3-atom expr, 0.1%) = -log2(n/|S|)'))
tot=[]
for k,t in zip(names,tv):
    c=[count(v2,t,.01),count(v2,t,.001),count(v3,t,.01),count(v3,t,.001)]
    bits=-math.log2(c[3]/len(v3)) if c[3] else float('inf')
    tot.append(c); print("%-22s %10d %10d %10d %10d  %6.1f"%(k,*c,bits))
tot=np.array(tot)
print("\nmedian multiplicity: 2-atom@1% %d, 2-atom@0.1% %d, 3-atom@1% %d, 3-atom@0.1% %d"%tuple(np.median(tot,axis=0)))
print("targets with >=1 two-atom expression within 1%%: %d/48; within 0.1%%: %d/48"%((tot[:,0]>0).sum(),(tot[:,1]>0).sum()))
print("targets with >=10 three-atom expressions within 0.1%%: %d/48"%((tot[:,3]>=10).sum()))
# probability that a target-directed search of n expressions (random from S3) finds a sub-1% / sub-0.1% hit
p1=np.median(tot[:,2])/len(v3); p01=np.median(tot[:,3])/len(v3)
for n in (10,30,100,300,1000):
    print(f"n={n:5d} random 3-atom trials per target: P(>=1 hit @1%)={1-(1-p1)**n:.3f}   @0.1%={1-(1-p01)**n:.3f}")
print(f"single-trial: p(1%)={p1:.2e}  p(0.1%)={p01:.2e}   |S3|={len(v3)}")
