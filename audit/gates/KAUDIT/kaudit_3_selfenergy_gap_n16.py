#!/usr/bin/env python3
# GATE KAUDIT — Script 3: self-energy magnitude, gap-equation (T3), n=16 accident.
import numpy as np
SQRT2=np.sqrt(2.0)
alpha0=0.00740805572755
me_over_mP=4.185e-23   # electron/Planck mass ratio (9.109e-31/2.176e-8)

print("="*70)
print("SELF-ENERGY MAGNITUDE (leading perturbative mass on the unprotected mode)")
print("="*70)
# From Script 2: Re G_loc(0) ~ -0.20 / t (extrapolated eta->0).
ReGloc = 0.20   # |Re G_loc(0)| in units 1/t
t=alpha0
# Convention A: 2nd-order (t^2) rainbow, Sigma(0) ~ t^2 * |G_loc(0)| ~ t^2*(0.2/t)=0.2 t
SigmaA = 0.2*t
# Convention B (gate's stated per-loop counting): shortest loop L_min=3 -> alpha0^{3/2}
SigmaB = alpha0**1.5
# Convention C: integer closed-walk amplitude a_3 = t^3 C_A(3)/3 = alpha0^3 * 48/3
SigmaC = alpha0**3 * 48/3
for name,val in [("A: t^2*|G_loc(0)| ~ 0.2*alpha0", SigmaA),
                 ("B: alpha0^{L_min/2}=alpha0^{3/2}", SigmaB),
                 ("C: a_3 = alpha0^3 * C_A(3)/3     ", SigmaC)]:
    print(f"  {name} = {val:.3e} (Planck)   ratio to m_e/m_P = {val/me_over_mP:.2e}  "
          f"(~{np.log10(val/me_over_mP):.0f} orders too LARGE)")
print("  All conventions: the generated perturbative mass is 15-20 orders ABOVE m_e.")
print("  Diagnosis INVERTS: not 'protected to zero / too weak', but 'far too heavy'.")

print("\n"+"="*70)
print("T3: GAP EQUATION on the CORRECTED FCC DOS (critical-coupling test)")
print("="*70)
# Build FCC single-band DOS
N=200
lin=np.linspace(0,4*np.pi,N,endpoint=False)
KX,KY,KZ=np.meshgrid(lin,lin,lin,indexing='ij')
cx,cy,cz=np.cos(KX/2),np.cos(KY/2),np.cos(KZ/2)
E=(-4.0*(cx*cy+cy*cz+cz*cx)).ravel()   # t=1 band units
nb=1200
hist,edges=np.histogram(E,bins=nb,range=(E.min()-1e-9,E.max()+1e-9),density=True)
ctr=0.5*(edges[:-1]+edges[1:]); dE=edges[1]-edges[0]
rho=hist
def I_of_m(m, rho, ctr, dE, E0=0.0):
    return np.sum(rho/((ctr-E0)**2+m**2))*dE
# FCC: integral as m->0 (measured at Fermi energy E0=0, the 'zero mode')
for m in [1.0,0.3,0.1,0.03,0.01]:
    print(f"  FCC  I(m={m:5.2f}) = {I_of_m(m,rho,ctr,dE):8.3f}  (grows as m->0 => rho(0)!=0)")
I_fcc_small=I_of_m(0.01,rho,ctr,dE)
gc_fcc=1.0/I_fcc_small
print(f"  => FCC critical coupling g_c = 1/I(0+) -> 0 (no threshold). At m=0.01: g_c~{gc_fcc:.4f}")
# Linear Dirac-like DOS on same support for contrast: rho_lin ~ |E|
rho_lin=np.abs(ctr); rho_lin/=np.sum(rho_lin)*dE
for m in [1.0,0.3,0.1,0.03,0.01]:
    pass
I_lin_small=I_of_m(0.01,rho_lin,ctr,dE)
I_lin_0=I_of_m(1e-6,rho_lin,ctr,dE)
print(f"  LINEAR (App K nodal) I(m->0) converges to {I_lin_0:.3f} => finite g_c={1.0/I_lin_0:.4f} (a real threshold)")
print("  CONCLUSION: App K's 'coupling ~20x too weak' assumed the linear DOS with a finite")
print("  critical coupling. The correct FCC band has rho(0)!=0 => NO critical coupling:")
print("  a mass is generated for ANY coupling. The '20x too weak' statement does not survive;")
print("  it inverts to a mass generated far too large (see self-energy block).")

print("\n"+"="*70)
print("n=16 ACCIDENT: reproduce monotone series + null-model information content")
print("="*70)
# App K even-n closed-walk amplitudes a_n = t^n C_A(n)/n  (his bipartite table)
CA={2:8,4:216,6:8000,8:343000,10:16003008,14:4.04e11,16:2.13e12}
print("  n   t^n C_A(n)        a_n=t^nC_A/n")
a={}
for n,c in sorted(CA.items()):
    val=alpha0**n * c
    a[n]=val/n
    print(f"  {n:2d}  {val:.4e}    {a[n]:.4e}")
# geometric decay per +2 in n
ns=sorted(a); ratios=[a[ns[i+1]]/a[ns[i]] for i in range(len(ns)-1) if ns[i+1]-ns[i]==2]
import numpy as np
gm=np.exp(np.mean(np.log(ratios))) if ratios else float('nan')
print(f"  mean geometric ratio per +2 in n ~ {gm:.3e}  ({-np.log10(gm):.2f} decades per step)")
# The series sweeps from ~1e-4 down through ~1e-26 monotonically -> it MUST cross m_e/m_P.
dec_per_step=-np.log10(gm)
# Null model: expected # of terms within factor f of a fixed target hit by a
# geometric ladder with step 'dec_per_step' decades:  ~ 2*log10(f)/dec_per_step
for f in [2,4,10]:
    exp_hits=2*np.log10(f)/dec_per_step
    bits=-np.log2(min(exp_hits,1.0)) if exp_hits<1 else 0.0
    print(f"  target within factor {f:2d}: expected hits along ladder = {exp_hits:.2f}  "
          f"=> information content ~ {bits:.2f} bits")
print("  a_16 = %.3e ; App K compares to ~m_e/4. m_e/mP=%.2e."%(a[16],me_over_mP))
print("  With ~2-3 decades per step and free choice of divisor & which n, a factor-of-a-few")
print("  'hit' is expected (<~1 bit). App K's 'numerical accident' verdict is CONFIRMED.")
print("  NB: these C_A are App K's BIPARTITE counts (odd=0). On the real FCC lattice odd")
print("  C_A!=0 (C_A(3)=48), so the actual series differs, but the anti-numerology holds a fortiori.")
