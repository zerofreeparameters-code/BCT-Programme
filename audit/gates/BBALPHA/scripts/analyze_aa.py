#!/usr/bin/env python3
"""Analyse the antialiased sweep: N->inf then sigma_i->0 extrapolation."""
import numpy as np, json, sys
from collections import defaultdict

PHI = 1.0 - np.pi/(3*np.sqrt(2))   # 0.25951951

rows=[]; iso=None
for line in open('/home/claude/work/aa_out.jsonl'):
    d=json.loads(line)
    if d.get('isotropy_check'): iso=d; continue
    rows.append(d)

bysi=defaultdict(list)
for d in rows: bysi[d['sigma_i']].append((d['N'],d['sigma_eff']))

def fit_poly_invN(pts, order):
    N=np.array([p[0] for p in pts],float); y=np.array([p[1] for p in pts])
    x=1.0/N
    A=np.vstack([x**k for k in range(order+1)]).T
    coef,*_=np.linalg.lstsq(A,y,rcond=None)
    return coef[0], coef  # intercept (N->inf) = coef[0]

print(f"{'sigma_i':>8} {'Ndata':>18} {'se_inf(lin)':>12} {'se_inf(quad)':>13}")
siinf={}
for si in sorted(bysi):
    pts=sorted(bysi[si])
    lin,_=fit_poly_invN(pts,1)
    quad,_=fit_poly_invN(pts,2) if len(pts)>=3 else (lin,None)
    siinf[si]=(lin,quad)
    ndata=",".join(f"{p[1]:.4f}" for p in pts)
    print(f"{si:>8} {ndata:>18} {lin:>12.5f} {quad:>13.5f}")

# sigma_i -> 0 extrapolation using the N->inf (quad) values
sis=np.array(sorted(siinf))
yq=np.array([siinf[s][1] for s in sis])
yl=np.array([siinf[s][0] for s in sis])
def extrap0(sx,sy,order):
    A=np.vstack([sx**k for k in range(order+1)]).T
    c,*_=np.linalg.lstsq(A,sy,rcond=None); return c[0]
print("\nsigma_i -> 0 extrapolation of se_inf(quad):")
for od in (1,2,3):
    if len(sis)>od:
        se0=extrap0(sis,yq,od)
        print(f"  order {od}: sigma_eff(0,inf) = {se0:.5f}  -> alpha = {PHI/se0:.4f}  F={1/se0:.4f}")
print("sigma_i -> 0 extrapolation of se_inf(lin):")
for od in (1,2,3):
    if len(sis)>od:
        se0=extrap0(sis,yl,od)
        print(f"  order {od}: sigma_eff(0,inf) = {se0:.5f}  -> alpha = {PHI/se0:.4f}")
if iso: print("\nisotropy (3 dirs):", iso['per_direction'])
print(f"\nPHI={PHI:.6f}  claim alpha=1.64 -> sigma_eff=0.15824")
