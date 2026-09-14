#!/usr/bin/env python3
"""Gate MAD, Step 1: Madelung baseline from BCT's own GP action (App AZ6 eq. SGP,
V = g rho^2/2).  Symbolic (SymPy), 1D for transparency (3D identical term-by-term),
plus a 3D numerical check of the quantum-potential identity at 60 dps.
No BCT-specific input (lattice, void, topology) is used anywhere in this script.
"""
import sympy as sp
hbar,m,g = sp.symbols('hbar m g', positive=True)
# jet variables (all real): rho, rho_x, rho_xx, rho_t, theta_x, theta_xx, theta_t
r,rx,rxx,rt,thx,thxx,tht = sp.symbols('rho rho_x rho_xx rho_t theta_x theta_xx theta_t', real=True)
r = sp.Symbol('rho', positive=True)
# Psi = sqrt(rho) e^{i theta};  derivatives in jet form
s = sp.sqrt(r)
Psi_t  = (rt/(2*s) + sp.I*s*tht)                      # times e^{i theta}
Psi_x  = (rx/(2*s) + sp.I*s*thx)
Psi_xx = (rxx/(2*s) - rx**2/(4*r*s)                    # d/dx of rx/(2 s)
          + sp.I*(rx*thx/(2*s)) + sp.I*(rx*thx/(2*s) + s*thxx) - s*thx**2)
V_prime = g*r                                          # dV/d rho for V = g rho^2/2
# GP: i hbar Psi_t = -hbar^2/2m Psi_xx + V' Psi   ->  E := (i hbar Psi_t + hbar^2/2m Psi_xx - V' Psi)/Psi = 0
E = sp.expand((sp.I*hbar*Psi_t + hbar**2/(2*m)*Psi_xx - V_prime*s)/s)
re, im = E.as_real_imag()
re, im = sp.simplify(re), sp.simplify(im)
v = hbar/m*thx
vx = hbar/m*thxx
cont = rt + rx*v + r*vx                                # d_t rho + d_x(rho v)
Q = hbar**2/(8*m)*(rx**2/r**2 - 2*rxx/r)               # = -hbar^2/2m (sqrt rho)''/sqrt rho  (AZ6 form)
HJ = -hbar*tht - m*v**2/2 - V_prime - Q                # Hamilton-Jacobi with quantum potential
print("Im(E) = +(hbar/(2 rho)) * continuity :", sp.simplify(im - hbar/(2*r)*cont) == 0)
print("Re(E) =  HJ (with quantum potential)  :", sp.simplify(re - HJ) == 0)
print("Q(AZ6 closed form) == -(hbar^2/2m) (sqrt rho)''/sqrt rho :",
      sp.simplify(Q - (-(hbar**2/(2*m))*(rxx/(2*s) - rx**2/(4*r*s))/s)) == 0)
# Reverse direction: the pair {cont=0, HJ=0} is EXACTLY {Im E=0, Re E=0}, i.e. E=0, i.e. GP.
print("Reverse: E == HJ + i (hbar/2rho) cont  :", sp.simplify(E - (HJ + sp.I*hbar/(2*r)*cont)) == 0)
print("=> The map (Psi) <-> (rho, theta) is an algebraic identity in both directions.")
print("   Nothing is added going GP -> fluid.  Going fluid -> GP requires the EXTRA data that")
print("   theta is a single-valued function (equivalently: circulation quantised in 2 pi hbar/m),")
print("   which is not implied by the fluid equations on (rho, v) alone [Wallstrom 1994].")

# 3D numerical check of the Q identity at 60 dps on an arbitrary smooth field (no symmetry)
from mpmath import mp, mpf, cos, sin, exp, sqrt
mp.dps = 60
def rho3(X):
    x,y,z = X
    return mpf(2) + cos(x)*sin(2*y) + exp(-z**2/3)*cos(x+y)
h = mpf('1e-12')
def d(f, X, i, n=1):
    e=[mpf(0)]*3; e[i]=h
    P=[X[k]+e[k] for k in range(3)]; M=[X[k]-e[k] for k in range(3)]
    return (f(P)-f(M))/(2*h) if n==1 else (f(P)-2*f(X)+f(M))/h**2
X=[mpf('0.3'),mpf('-0.7'),mpf('0.4')]
rr=rho3(X); gr=[d(rho3,X,i) for i in range(3)]; lap=sum(d(rho3,X,i,2) for i in range(3))
sq=lambda Y: sqrt(rho3(Y)); lapsq=sum(d(sq,X,i,2) for i in range(3))
lhs = -lapsq/sqrt(rr)                             # (2m/hbar^2) Q
rhs = (sum(gi**2 for gi in gr)/rr**2 - 2*lap/rr)/4
print("3D numerical check |lhs-rhs| =", mp.nstr(abs(lhs-rhs),5))
