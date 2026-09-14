#!/usr/bin/env python3
"""Gate MAD, Step 2/3 numerical checks (mpmath, 60 dps working, 40 reported).
(a) App JH eq. (hopf-matching): explicit H=0 configuration satisfying the surface-flux
    condition -> the flux condition does not select the Hopf sector.
(b) App JH E_N = N eps0 vs the Faddeev-Skyrme power law E ~ c N^{3/4} (Ward 2005, read).
(c) Letter 81 "Pauli theorem": the stated capacity rule |H_total| <= n admits 3 hopfions.
(d) Letter 72 N_c = 1/alpha_0, 1/alpha - N_c, tau_D, m_classical arithmetic.
(e) Letter 254 identity cos(pi/4) = 1/(2 r_oct + 1): an algebraic tautology of the definition.
(f) Letter 20 / AZ6 unit convention in the Madelung action.
"""
from mpmath import mp, mpf, sqrt, pi, cos, quad, nstr, exp
mp.dps = 60
S = lambda x: nstr(x, 40)
roct = (sqrt(2)-1)/2
rtet = (sqrt(6)-2)/4
a0   = roct*rtet/pi
print("r_oct =", S(roct)); print("r_tet =", S(rtet)); print("alpha_0 =", S(a0))

# (a) JH flux condition with an H=0 field.  Psi = e^{i chi(r)} (1,0) * sqrt(rho0): n-field constant
# (Hopf charge 0). J.n = (hbar/m) rho0 chi'(r). Need  oint J.n dA = a0 rho0 4 pi R^2.
# Take hbar=m=1, R=1, rho0=1: chi'(R) = a0 does it, with chi(r) = a0 r^2/(2R) smooth at r=0.
R = mpf(1); rho0 = mpf(1)
chi_p = lambda r: a0*r/R           # chi = a0 r^2/(2R)
flux  = rho0*chi_p(R)*4*pi*R**2
target= a0*rho0*4*pi*R**2
print("(a) H=0 field: surface flux =", S(flux), " target =", S(target), " |diff| =", S(abs(flux-target)))
print("    -> JH's 'H=1 is the unique smooth solution of the flux condition' is false; the overall U(1)")
print("       phase carries the flux and is invisible to the S^2 map that carries the Hopf charge.")

# (b) energy scaling: JH claims E_N = N eps0 (linear).  Skyrme-Faddeev law E ~ c N^{3/4}.
for N in range(1,7):
    print(f"(b) N={N}: linear ratio E_N/E_1 = {N}   ;  N^(3/4) = {S(mpf(N)**(mpf(3)/4))[:12]}")
print("    -> at N=2 the two laws differ by 2/2^0.75 = 1.189 (18.9%); at N=6 by 6/6^0.75 = 1.565.")
print("    -> JH's own functional (|grad Psi|^2 + g|Psi|^4, no 4th-order term) admits NO stationary")
print("       nonzero-H soliton at all (Ward 2005 eq.(2) remark; Derrick scaling), so the linear law")
print("       is not a computation inside JH; it is asserted against the cited literature.")

# (c) Letter 81 capacity rule
n=1
configs = {"(+1)":[1], "(+1,+1)":[1,1], "(+1,-1)":[1,-1], "(+1,-1,+1)":[1,-1,1], "(+1,-1,+1,-1)":[1,-1,1,-1]}
for k,v in configs.items():
    print(f"(c) mode n=1, hopfions {k}: |H_total| = {abs(sum(v))}  allowed by |H|<=n ? {abs(sum(v))<=n}")
print("    -> the stated rule admits 3 (indeed any odd number of) hopfions per n=1 mode; 'at most two'")
print("       does not follow from the premise.  The theorem is not proved by its proof.")

# (d) Letter 72 arithmetic (their printed values: N_c ~ 134.99, 1/alpha = 137.018, tau_D = 1.18e-38 s)
Nc = 1/a0
alpha = a0*(1-2*a0)
print("(d) N_c = 1/alpha_0 =", S(Nc)[:14], " printed 134.99 -> OK")
print("    1/alpha = 1/[alpha_0(1-2alpha_0)] =", S(1/alpha)[:12], " printed 137.018 -> OK")
print("    1/alpha - N_c =", S(1/alpha - Nc)[:12], " (printed 'approximately 2': it is 2/(1-2a0) = ", S(2/(1-2*a0))[:10], ")")
c = mpf('299792458'); lP = mpf('1.616255e-35'); Rs = 12*lP
tauD = Rs/(a0**2*c)
print("    tau_D = R_s/(alpha_0^2 c) with R_s = 12 l_P :", nstr(tauD,6), "s   printed 1.18e-38 s -> OK")
mP = mpf('2.176434e-8'); eta = mpf('0.74')
print("    m_classical = m_P/(alpha_0 eta) :", nstr(mP/(a0*eta),6), "kg   printed 3.97e-6 kg -> OK")
print("    -> arithmetic reproduces; the theorem's premise (sum alpha_0 >= 1 forces integer H) is asserted.")

# (e) Letter 254
print("(e) 2 r_oct + 1 =", S(2*roct+1)[:20], " sqrt(2) =", S(sqrt(2))[:20], " -> identity holds by definition of r_oct = (sqrt2-1)/2")
print("    cos(pi/4) = 1/sqrt2: the Tsirelson bound 2 sqrt 2 is a theorem of Hilbert-space QM (assumed), r_oct adds nothing.")

# (f) Letter 20 / AZ6 Madelung action units
print("(f) AZ6 lemma writes -rho hbar d_t theta - rho hbar^2 (grad theta)^2/(2m) = -rho(d_t theta + v^2/2);")
print("    with v = (hbar/m) grad theta the RHS second term is rho m v^2/2 -> equality needs hbar = m = 1.")
print("    Not an obstruction (SC-MAD-3 does not fire): units restore uniquely; recorded as a convention defect.")
