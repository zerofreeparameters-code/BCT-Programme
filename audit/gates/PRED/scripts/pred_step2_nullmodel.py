#!/usr/bin/env python3
"""Gate PRED — Step 2/3: null model for 'expressions built from pi, alpha0, void radii and small
integers landing within tolerance of SOME measured quantity'.  Deterministic enumeration; no sampling.

JUDGEMENT CALLS (stated per gate §'A note on care'):
 J1 Alphabet = atoms actually observed in the corpus's printed formulas (Step 1):
    integers {1,2,3,4,5,6,8,9,12}, pi, sqrt2, sqrt3, sqrt6, r_oct, r_tet, alpha0, S_D4=pi^5/6.
 J2 Complexity bound = <=3 atoms, <=2 binary ops, <=1 unary op at a leaf and <=1 at the root.
    This matches every core formula in the recomputed set (e.g. (1-5a0)/pi has 3 atoms, 2 ops).
 J3 Correction layer = optional factor (1+N*alpha0) with N drawn from the corpus's own printed
    'N-class' menu.  Reported both with and without the layer.
 J4 Targets: fixed BEFORE enumeration (list below), dimensionless, PDG/CODATA/Planck 2018-2024
    central values as quoted in the corpus or standard.  The corpus's hadron sector uses Lambda=220 MeV
    as a chosen anchor; hadron targets are therefore ratios to that anchor and to m_pi0.
 J5 Tolerance: 1% (the corpus's headline 'sub-1%') and 0.1% (its 'sub-0.1%' tier).
Sensitivity to J1-J5 is reported in the deliverable.
"""
import numpy as np, itertools, math, sys
pi=math.pi; s2=math.sqrt(2); s3=math.sqrt(3); s6=math.sqrt(6)
roct=(s2-1)/2; rtet=(s6-2)/4; a0=roct*rtet/pi; SD4=pi**5/6
atoms={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'8':8,'9':9,'12':12,'pi':pi,'sqrt2':s2,'sqrt3':s3,'sqrt6':s6,
       'roct':roct,'rtet':rtet,'a0':a0,'SD4':SD4}
A=np.array(list(atoms.values()))
def unary(v):
    out=[v, np.sqrt(v), np.cbrt(v), v**2, 1/v]
    with np.errstate(all='ignore'):
        out.append(np.exp(-v)); out.append(np.log(np.abs(v)))
    return np.concatenate(out)
def clean(v):
    v=v[np.isfinite(v)]; v=v[(np.abs(v)>1e-6)&(np.abs(v)<1e6)]
    return np.unique(np.round(v,10))
L1=clean(unary(A))                      # 1 atom
def binary(X,Y):
    x=X[:,None]; y=Y[None,:]
    with np.errstate(all='ignore'):
        r=np.concatenate([(x+y).ravel(),(x-y).ravel(),(x*y).ravel(),(x/y).ravel()])
    return r
L2=clean(binary(L1,L1))                  # 2 atoms (unary at leaves)
L2r=clean(np.concatenate([L2,np.sqrt(np.abs(L2)),1/L2,L2**2]))  # root unary
L3=clean(binary(L2,L1))                  # 3 atoms
L3r=clean(np.concatenate([L3,np.sqrt(np.abs(L3)),1/L3]))
print(f"distinct values: 1-atom {len(L1)}, 2-atom {len(L2r)}, 3-atom {len(L3r)}")
# ---- fixed target list (dimensionless), set before running ----
Lam=220.0; mpi0=134.9768
T={ '1/alpha':137.035999, 'sin2thW(MSbar,mZ)':0.23122, 'sin2th12':0.307, 'sin2th13':0.02203,
    'sin2th23':0.57, 'n_s':0.9649, 'alpha_s(mZ)':0.1180, 'Omega_L':0.685, 'Y_p':0.245,
    'm_p/m_e':1836.153, 'm_mu/m_e':206.768, 'm_tau/m_mu':16.817, 'Koide_Q':0.666661,
    'm_rho/m_pi0':775.26/mpi0, 'm_K/m_pi0':493.677/mpi0, 'm_eta/m_pi0':547.862/mpi0,
    "m_eta'/m_pi0":957.78/mpi0, 'm_omega/m_rho':782.66/775.26, 'm_K*/m_rho':891.67/775.26,
    'm_phi/m_rho':1019.461/775.26, 'm_p/m_rho':938.272/775.26, 'm_n/m_p':939.565/938.272,
    'm_Delta/m_p':1232/938.272, 'm_p/Lam':938.272/Lam, 'm_rho/Lam':775.26/Lam, 'T_c/Lam':156.5/Lam,
    'r_p*m_rho/hbarc':0.84075*775.26/197.327, 'r_pi*m_rho/hbarc':0.659*775.26/197.327,
    'm_b/m_t':4.183/172.57, 'm_c/m_t':1.273/172.57, 'm_s/m_c':0.0935/1.273, 'm_d/m_u':4.70/2.16,
    'm_s/m_d':93.5/4.70, 'm_H/v':125.2/246.22, 'm_t/v':172.57/246.22, 'm_W/m_Z':80.369/91.188,
    'g_A':1.2754, 'mu_p':2.79285, 'V_us':0.2245, 'V_cb':0.0410, 'V_ub':0.00382,
    'ln(mP/me)':math.log(1.220890e22/0.51099895), 'ln(mP/mp)':math.log(1.220890e22/938.272),
    'ln(mP/v)':math.log(1.220890e22/246220), 'ln(mP/Lam)':math.log(1.220890e22/Lam),
    'sigma8':0.811, 'H0/100':0.674, 'Omega_m':0.315 }
names=list(T); tv=np.array([T[k] for k in names])
print(f"targets fixed: {len(tv)}")
Nmenu=[3/8,3/4,1,3/2,2,9/4,3,4,5,6,8,9]; Nmenu=sorted(set(Nmenu+[-n for n in Nmenu]))
def hit_stats(vals, tol, with_N=False):
    """fraction of distinct |values| within tol of ANY target (interval union via searchsorted); per-target coverage"""
    v=np.sort(np.abs(vals))
    facs=[1+n*a0 for n in Nmenu]+[1.0] if with_N else [1.0]
    ints=[]; covered=np.zeros(len(tv),bool)
    for j,t in enumerate(tv):
        for f in facs:
            lo,hi=t/f*(1-tol), t/f*(1+tol)
            ints.append((lo,hi))
            if np.searchsorted(v,hi,'right')-np.searchsorted(v,lo,'left')>0: covered[j]=True
    ints.sort(); merged=[]
    for lo,hi in ints:
        if merged and lo<=merged[-1][1]: merged[-1][1]=max(merged[-1][1],hi)
        else: merged.append([lo,hi])
    n=sum(np.searchsorted(v,hi,'right')-np.searchsorted(v,lo,'left') for lo,hi in merged)
    return n/len(v), covered
for lab,vals in [('2-atom',L2r),('3-atom',L3r)]:
    for tol in (0.01,0.001):
        for wn in (False,True):
            p,cov=hit_stats(vals,tol,wn)
            print(f"{lab:7s} tol={tol:<6} N-layer={str(wn):5s}  P(random expr hits some target)={p:.4f}   targets covered={cov.sum()}/{len(tv)}")
# per-target: best 3-atom expression (no N) and with N, at 1% and 0.1%
print("\nPer-target coverage, 3-atom, tol 0.1%: (no-N / with-N)")
p1,c1=hit_stats(L3r,0.001,False); p2,c2=hit_stats(L3r,0.001,True)
for k,a,b in zip(names,c1,c2): print(f"  {k:22s} {'Y' if a else '-'} / {'Y' if b else '-'}")
# base-within-X% correctable fraction under the N menu
print("\nN-layer reach: a base value with fractional offset d from a target can be brought within tol if some (1+N a0) closes it.")
for tol in (0.01,0.001):
    d=np.linspace(-0.10,0.10,20001); ok=np.zeros_like(d,bool)
    for n in Nmenu+[0]:
        ok|= np.abs((1+d)*(1+n*a0)-1)<tol
    print(f"  tol={tol}: fraction of base offsets in [-10%,+10%] that the menu can fix = {ok.mean():.3f}; widest contiguous fixable band ≈ ±{max(abs(d[ok]))*100:.1f}%")
np.save('L3r.npy',L3r)
