import numpy as np

r_oct=(np.sqrt(2)-1)/2; r_tet=(np.sqrt(6)-2)/4; alpha0=r_oct*r_tet/np.pi
me_over_mP=4.185e-23

def Gamma(kx,ky,kz):
    cx,cy,cz=np.cos(kx/2),np.cos(ky/2),np.cos(kz/2)
    return 4.0*(cx*cy+cy*cz+cz*cx)

N=220
ks=(np.arange(N)+0.5)/N*(4*np.pi)-2*np.pi
KX,KY,KZ=np.meshgrid(ks,ks,ks,indexing='ij')
E=(-Gamma(KX,KY,KZ)).ravel()
Emin,Emax=E.min(),E.max()
print(f"alpha0={alpha0:.12f}  band=[{Emin:.3f},{Emax:.3f}] width={Emax-Emin:.3f} (units t)")

# fine DOS
nb=8000
hist,edges=np.histogram(E,bins=nb,range=(Emin-1e-9,Emax+1e-9),density=True)
ctr=0.5*(edges[:-1]+edges[1:]); dE=ctr[1]-ctr[0]

# rho(0) and slope near 0 by local linear fit
win=np.abs(ctr)<0.4
p=np.polyfit(ctr[win],hist[win],1)      # hist ~ p[0]*E + p[1]
rho0=p[1]; rhop=p[0]
print(f"rho(0)={rho0:.5f}/t  rho'(0)={rhop:+.5f}/t^2  (finite DOS at Dirac energy)")

# Re G_loc(0) = PV int rho(E)/(-E) dE
# split |E|<delta (local, analytic) + |E|>delta (trapezoid)
delta=0.4
far=np.abs(ctr)>=delta
farint=np.sum(-hist[far]/ctr[far])*dE
# near: rho~rho0+rhop*E ; PV int_{-d}^{d} (rho0+rhop E)/(-E) dE = -rhop*2d (rho0 term cancels)
nearint=-rhop*2*delta
ReG=farint+nearint
print(f"Re G_loc(0) = {ReG:+.4f}/t   (far={farint:+.4f}, near={nearint:+.4f})")

# independent check: eta-sum with eta^2 + eta*log fit is messy; instead
# Hilbert via same DOS at small offset to confirm sign/scale
for eta in (0.04,0.02):
    rg=np.sum(-hist*ctr/(ctr**2+eta**2))*dE
    print(f"   DOS eta-check eta={eta}: {rg:+.4f}/t")

c0=ReG
print("\n"+"="*60)
print("Sigma(0)=g^2 Re G_loc(0);  t=alpha0 (Planck units); one coupling => g=t")
print("="*60)
Sigma=(alpha0**2)*(c0/alpha0)   # = c0*alpha0
m=abs(Sigma)
print(f"g=t=alpha0:  Sigma = c0*alpha0 = {Sigma:+.4e} m_P   (exponent p=1, DERIVED)")
print(f"  |m|/m_P = {m:.3e}   vs target {me_over_mP:.3e}   -> {m/me_over_mP:.2e}x too heavy")
gt=np.sqrt(me_over_mP*alpha0/abs(c0))/alpha0
print(f"  g/t needed to hit m_e = {gt:.2e}  (no second coupling that small exists)")
print(f"\n  robustness: for any c0 in [0.2,0.6], m/m_P in "
      f"[{0.2*alpha0:.2e},{0.6*alpha0:.2e}] -> {0.2*alpha0/me_over_mP:.1e}..{0.6*alpha0/me_over_mP:.1e}x")
