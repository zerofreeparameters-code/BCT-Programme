#!/usr/bin/env python3
# GATE KAUDIT — Script 2: THE BAND (single FCC band, cold).
# The c/a=sqrt2 lattice is FCC (Script 1: A,B equivalent). Correct tight-binding
# is SINGLE-band E(k) = -t * Gamma(k). Two equivalent forms:
#   (i) BCT coords : Gamma = 8 cx2 cy2 cz + 2 cos kx + 2 cos ky ,  cz=cos(kz/sqrt2)
#   (ii) std FCC   : Gamma = 4[cos(kx/2)cos(ky/2)+cos(ky/2)cos(kz/2)+cos(kz/2)cos(kx/2)]
# We confirm both give the SAME band range, then use (ii) for DOS/G_loc.
# Compare against App K's bipartite 2-band claim E=+-t|gamma8| (symmetric about 0).
import numpy as np
SQRT2=np.sqrt(2.0)
t=1.0  # work in band units (t); multiply by alpha0 at the end
alpha0=0.00740805572755

# ---- (a) confirm the two structure functions share a band range ----
def gamma_bct(kx,ky,kz):
    return 8*np.cos(kx/2)*np.cos(ky/2)*np.cos(kz/SQRT2) + 2*np.cos(kx) + 2*np.cos(ky)
def gamma_fcc(kx,ky,kz):
    cx,cy,cz=np.cos(kx/2),np.cos(ky/2),np.cos(kz/2)
    return 4*(cx*cy+cy*cz+cz*cx)
# scan for ranges
M=120
lin=np.linspace(0,4*np.pi,M,endpoint=False)
KX,KY,KZ=np.meshgrid(lin,lin,lin,indexing='ij')
gb=gamma_bct(KX,KY,KZ*SQRT2/2*2)   # kz enters bct via cos(kz/sqrt2); pass raw kz
# careful: recompute cleanly on raw kz
gb=8*np.cos(KX/2)*np.cos(KY/2)*np.cos(KZ/SQRT2)+2*np.cos(KX)+2*np.cos(KY)
gf=gamma_fcc(KX,KY,KZ)
print("=== structure-function ranges (E = -t*Gamma) ===")
print(f"  BCT-coord Gamma range: [{gb.min():.4f}, {gb.max():.4f}]  -> E in [{-t*gb.max():.4f}, {-t*gb.min():.4f}] t")
print(f"  std-FCC   Gamma range: [{gf.min():.4f}, {gf.max():.4f}]  -> E in [{-t*gf.max():.4f}, {-t*gf.min():.4f}] t")
print(f"  E(Gamma-point,k=0): BCT {-t*gamma_bct(0,0,0):+.4f} t ,  FCC {-t*gamma_fcc(0,0,0):+.4f} t  (= -coordination*t = -12t)")

# ---- (b) DOS via dense histogram on std-FCC single band ----
N=220
lin=np.linspace(0,4*np.pi,N,endpoint=False)
KX,KY,KZ=np.meshgrid(lin,lin,lin,indexing='ij')
E=(-t*gamma_fcc(KX,KY,KZ)).ravel()   # single band
Emin,Emax=E.min(),E.max()
print(f"\n=== SINGLE FCC BAND (N={N}^3 k-points) ===")
print(f"  band range: [{Emin:.4f}, {Emax:.4f}] t   width {Emax-Emin:.4f} t")
print(f"  band centre (mid): {(Emin+Emax)/2:+.4f} t   -> asymmetric about E=0 if != 0")
# PH-symmetry test: is DOS(E)=DOS(-E)? compare histogram symmetry
nb=400
hist,edges=np.histogram(E,bins=nb,range=(-13,13),density=True)
centres=0.5*(edges[:-1]+edges[1:])
# symmetry metric
from numpy import interp
rho=hist
rho_flip=interp(-centres,centres,rho,left=0,right=0)
asym=np.sum(np.abs(rho-rho_flip))/np.sum(rho+rho_flip)
print(f"  PH-symmetry asymmetry metric  sum|rho(E)-rho(-E)|/sum(...) = {asym:.4f}  (0=symmetric)")
# first moment (should be -4t if perfectly asymmetric mean; mean of E over BZ)
print(f"  <E> band-average = {E.mean():+.4f} t   (PH-symmetric band would give 0)")

# ---- (c) half-filling Fermi level (median of occupied states) ----
Ef=np.median(E)
print(f"\n  half-filling Fermi level E_F = median(E) = {Ef:+.4f} t   (PH-symmetric => 0)")

# ---- (d) DOS at E=0 and local Green's function G_loc(0) ----
# rho(0):
i0=np.argmin(np.abs(centres-0.0))
rho0=rho[i0]
print(f"  DOS at E=0:  rho(0) = {rho0:.4f} /t   (finite & nonzero => E=0 is INSIDE the band)")
print(f"  DOS at band bottom vs top: rho(-11.5t)={rho[np.argmin(np.abs(centres+11.5))]:.4f}, rho(+3.5t)={rho[np.argmin(np.abs(centres-3.5))]:.4f}")

# G_loc(omega) = (1/N) sum_k 1/(omega+i*eta - E_k). At omega=0:
for eta in [0.20,0.10,0.05,0.02]:
    G=np.mean(1.0/(0.0+1j*eta - E))
    print(f"  G_loc(0; eta={eta:.2f} t) = {G.real:+.4f} {G.imag:+.4f}i  /t   (ReG=PV -int rho/E)")
print("  --> Re G_loc(0) != 0  ==>  T2 non-renormalization (needs G_loc(0)=0) FAILS.")

# ---- (e) contrast: App K's bipartite 2-band model E=+-t|gamma8| ----
g8=np.abs(8*np.cos(KX/2)*np.cos(KY/2)*np.cos(KZ/SQRT2)).ravel()
Eb=np.concatenate([+t*g8,-t*g8])
print(f"\n=== App K's (incorrect) 2-band model E=+-t|gamma8| ===")
print(f"  range [{Eb.min():.4f},{Eb.max():.4f}] t, symmetric about 0 (mean {Eb.mean():+.2e}); this is the artefact.")

print(f"\n=== physical scale (t=alpha0={alpha0}) ===")
print(f"  bandwidth = 16 t = {16*alpha0:.6f} (Planck units)  [matches App K's 0.11853]")
print(f"  band range = [{-12*alpha0:.6f}, {+4*alpha0:.6f}] (Planck units)")
