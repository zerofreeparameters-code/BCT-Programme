from mpmath import mp, mpf, sqrt, pi, nstr
mp.dps = 60  # working precision; report 40

# --- BCT void radii (close-packing inradii; sphere radius R = 1/2 in a=1 units) ---
r_oct = (sqrt(2) - 1)/2          # octahedral hole ratio, per App JH line 273
r_tet = (sqrt(6) - 2)/4          # tetrahedral hole ratio, per App JH line 273
print("r_oct              =", nstr(r_oct, 40))
print("r_tet              =", nstr(r_tet, 40))

# --- alpha_0 = r_oct * r_tet / pi  (App JH eq., abstract: 0.0074081) ---
a0 = r_oct*r_tet/pi
print("alpha_0            =", nstr(a0, 40), " (JH abstract: 0.0074081)")

# --- healing length ratio xi/a = 1/sqrt(8 r_oct r_tet) = 1/sqrt(8 pi alpha_0) ---
xi_over_a = 1/sqrt(8*r_oct*r_tet)
print("xi/a               =", nstr(xi_over_a, 40), " (MINIMAL_BCT: 2.3175)")
print("check 1/sqrt(8 pi a0) =", nstr(1/sqrt(8*pi*a0), 40))

# --- sphere radius R_s = ell_P/2, lattice a = ell_P  =>  R_s = a/2 ---
xi_over_R = xi_over_a / mpf('0.5')
print("xi/R_s  (R=a/2)    =", nstr(xi_over_R, 40), " (gate: 4.635)")

# --- r_oct/r_tet close-packing constant (radius ratio) ---
print("r_oct/r_tet        =", nstr(r_oct/r_tet, 40))

print()
print("=== DERRICK SCALING of the App JH free energy (eq. free-energy) ===")
print("Field n_hat: R^3 -> S^2 at fixed |Psi|=sqrt(rho0). Rescale x -> lambda x.")
print("  two-derivative (gradient) term  E2  scales as  lambda^(3-2) = lambda^1")
print("  quartic POTENTIAL (g/2)|Psi|^4  Vp  scales as  lambda^3   (0 derivatives)")
print("  surface Josephson term          Es  fixed (R_s fixed)")
print("  a stabilising 4-derivative term E4  would scale as lambda^(3-4)=lambda^-1")
print()
print("As-written energy (no E4):  E(l) = E2*l + Vp*l^3 + Es")
print("  dE/dl = E2 + 3 Vp l^2 > 0 for all l>0  =>  monotone; min at l->0 (collapse).")
print("With a Faddeev term:        E(l) = E2*l + E4/l  =>  l* = sqrt(E4/E2) finite.")
print("  App JH free energy has E4 = 0  =>  NO finite-size minimum. Hopfion collapses.")

# tiny numeric demo with representative positive constants
def E_nofour(l, E2=1.0, Vp=0.3, Es=0.5):
    return E2*l + Vp*l**3 + Es
def E_withfour(l, E2=1.0, E4=1.0):
    return E2*l + E4/l
import numpy as np
ls = np.linspace(0.02, 3, 8)
print()
print(" lambda :", "  ".join(f"{x:5.2f}" for x in ls))
print(" no-E4  :", "  ".join(f"{E_nofour(x):5.2f}" for x in ls), " -> decreasing toward l=0")
print(" with-E4:", "  ".join(f"{E_withfour(x):5.2f}" for x in ls), " -> min near l=1 (finite)")
