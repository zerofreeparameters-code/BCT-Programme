#!/usr/bin/env python3
"""
GATE KL - Step 1/2: periodic stability of an FCC S^2 knot/skyrmion crystal
under the geometry-fixed Faddeev/BFN energy  E = c2 |dn|^2 + c4 F^2,
F_ij = n.(d_i n x d_j n).  Discrete field strength identity used:
   F_ij(x) = det[ n(x), n(x+i), n(x+j) ]   (derived in deliverable).
Deterministic, re-runnable. numpy only.
Central claims tested:
  (1) E >= 0 pointwise, = 0 iff uniform  -> uniform is the global minimum.
  (2) every modulated periodic texture has E > 0 = E_uniform.
  (3) gradient flow: trivial sector -> uniform (E->0);
      charged sector never dips below 0.
  (4) natural size lambda* ~ xi > cell (no sub-cell geometry-fixed size).
"""
import numpy as np
np.random.seed(0)

XI = 2.317543794911664963            # xi/a from Step 0
C2 = 1.0
C4 = XI**2                           # geometry-fixed c4/c2 = xi^2

# ---------- discrete energy on a periodic cubic box (a=1, dx=1/N) ----------
def roll(n, sh, ax): return np.roll(n, -sh, axis=ax)   # n(x+e_ax)

def energy(n, dx):
    # n shape (N,N,N,3), unit vectors. periodic.
    e2 = 0.0
    for ax in range(3):
        d = (roll(n,1,ax) - n)/dx
        e2 += np.sum(d*d)
    e2 *= C2 * dx**3
    # four-derivative term via triple-product identity
    e4 = 0.0
    for (i,j) in [(0,1),(0,2),(1,2)]:
        ni = roll(n,1,i); nj = roll(n,1,j)
        F = np.sum(n*np.cross(ni,nj), axis=-1)/dx**2     # det[n,ni,nj]/dx^2
        e4 += np.sum(F*F)
    e4 *= C4 * dx**3
    return e2, e4, e2+e4

def grad(n, dx):
    g = np.zeros_like(n)
    # E2 gradient from link definition:  d/dn(x) [ c2 dx sum_links |Dn|^2 ]
    for ax in range(3):
        g += 2*C2*dx*( (n-roll(n,1,ax)) + (n-roll(n,-1,ax)) )
    # E4 gradient:  E4 = (c4 dx^3/dx^4) sum F^2, F=det[n(x),n(x+i),n(x+j)]
    #   dF/dn(x)=ni x nj ; dF/dn(x+i)=nj x n ; dF/dn(x+j)=n x ni  (triple-product cyclicity)
    coef = 2*C4*dx**3/dx**4
    for (i,j) in [(0,1),(0,2),(1,2)]:
        ni = roll(n,1,i); nj = roll(n,1,j)
        F  = np.sum(n*np.cross(ni,nj), axis=-1)[...,None]
        g += coef*F*np.cross(ni,nj)                 # site x
        g += np.roll(coef*F*np.cross(nj,n), 1, i)   # move x+i -> x
        g += np.roll(coef*F*np.cross(n,ni), 1, j)   # move x+j -> x
    return g

def normalize(n):
    return n/np.linalg.norm(n, axis=-1, keepdims=True)

def flow(n, dx, steps, eta):
    traj=[]
    for k in range(steps):
        g = grad(n,dx)
        g = g - np.sum(g*n,axis=-1,keepdims=True)*n     # tangent projection
        n = normalize(n - eta*g)
        if k%(max(1,steps//8))==0 or k==steps-1:
            traj.append((k,)+energy(n,dx))
    return n, traj

def sky_number_z(n):
    # baby-skyrmion number of each xy-section (finite-diff), averaged
    dx_n = roll(n,1,0)-n; dy_n = roll(n,1,1)-n
    q = np.sum(n*np.cross(dx_n,dy_n),axis=-1)/(4*np.pi)
    return q.sum(axis=(0,1)).mean()

# ---------------- (1)&(2) uniform vs textures ----------------
N=16; dx=1.0/N
X,Y,Z=np.meshgrid(*[ (np.arange(N)+0.5)/N ]*3, indexing='ij')

uni=np.zeros((N,N,N,3)); uni[...,2]=1.0
print("=== (1) uniform state ===")
print("  E2,E4,Etot =", tuple(round(v,6) for v in energy(uni,dx)))

rnd=normalize(np.random.randn(N,N,N,3))
e2,e4,et=energy(rnd,dx)
print("=== (2) random texture ===")
print(f"  E2={e2:.4f} E4={e4:.4f} Etot={et:.4f}  (>0)")

# baby-skyrmion tube along z, size R (compact cosine profile), Q=1 per section
def tube(R):
    xc,yc=0.5,0.5
    r=np.sqrt((X-xc)**2+(Y-yc)**2)
    phi=np.arctan2(Y-yc,X-xc)
    Th=np.where(r<R, np.pi*0.5*(1+np.cos(np.pi*np.clip(r/R,0,1))), 0.0)
    n=np.empty((N,N,N,3))
    n[...,0]=np.sin(Th)*np.cos(phi); n[...,1]=np.sin(Th)*np.sin(phi); n[...,2]=np.cos(Th)
    return normalize(n)
tb=tube(0.35)
e2,e4,et=energy(tb,dx)
print("=== baby-skyrmion tube (R=0.35a) ===")
print(f"  E2={e2:.4f} E4={e4:.4f} Etot={et:.4f}  Q_section~{sky_number_z(tb):.3f}  (>0)")

print("\n=== (3) gradient flow (monotone; never below uniform E=0) ===")
_,tr=flow(rnd.copy(),dx,steps=400,eta=2e-4)
print("  random init -> ", "  ".join(f"[{k}]{et:.3f}" for k,_,_,et in tr))
_,tr2=flow(tb.copy(),dx,steps=400,eta=2e-4)
print("  tube  init  -> ", "  ".join(f"[{k}]{et:.3f}" for k,_,_,et in tr2))

# ---------------- (4) 3D hopfion Derrick: natural size ----------------
print("\n=== (4) 3D Hopf ansatz Derrick -> natural size lambda* ===")
M=40; L=8.0; h=L/M
c=(np.arange(M)+0.5)*h - L/2
xx,yy,zz=np.meshgrid(c,c,c,indexing='ij')
r2=xx**2+yy**2+zz**2
den=1+r2
X1=2*xx/den; X2=2*yy/den; X3=2*zz/den; X4=(1-r2)/den   # S^3 (inverse stereo)
z1=X1+1j*X2; z2=X3+1j*X4                                # Hopf -> S^2
nx=2*np.real(z1*np.conj(z2)); ny=2*np.imag(z1*np.conj(z2)); nz=np.abs(z1)**2-np.abs(z2)**2
nh=np.stack([nx,ny,nz],axis=-1); nh=nh/np.linalg.norm(nh,axis=-1,keepdims=True)
def shape_integrals(n,dx):
    I2=0.0
    for ax in range(3):
        d=(np.roll(n,-1,ax)-n)/dx; I2+=np.sum(d*d)
    I2*=dx**3
    I4=0.0
    for (i,j) in [(0,1),(0,2),(1,2)]:
        ni=np.roll(n,-1,i); nj=np.roll(n,-1,j)
        F=np.sum(n*np.cross(ni,nj),axis=-1)/dx**2; I4+=np.sum(F*F)
    I4*=dx**3
    return I2,I4
I2,I4=shape_integrals(nh,h)
shape_ratio=np.sqrt(I4/I2)     # dimensionless, O(1)
lam_star_over_a = XI*shape_ratio
print(f"  shape integrals: I2={I2:.3f}  I4={I4:.3f}  sqrt(I4/I2)={shape_ratio:.3f}")
print(f"  lambda*/a = xi * sqrt(I4/I2) = {lam_star_over_a:.3f}  vs cell period a=1")
print(f"  -> knot size {'EXCEEDS' if lam_star_over_a>1 else 'fits within'} one FCC cell")

# 2D size scan: does a sub-cell equilibrium size exist? (tube energy vs R)
print("\n=== 2D tube energy vs size R (looking for a sub-cell minimum) ===")
for R in [0.15,0.20,0.25,0.30,0.35,0.40,0.45]:
    e2,e4,et=energy(tube(R),dx)
    print(f"  R={R:.2f}a  Etot={et:.4f}")
