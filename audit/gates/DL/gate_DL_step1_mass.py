# GATE DL — STEP 1/2: the decisive fork, symbolically (deterministic, sympy).
# Q: which couplings produce a photon MASS term (coefficient of A^2 at zero derivative
#    of the matter phase = London/Meissner mass), and which do not?
import sympy as sp

A, phi0, q, p, k = sp.symbols('A phi0 q p k', real=True)
dth = sp.symbols('dtheta', real=True)   # gradient of matter phase (would-be Goldstone)

# (1) CHARGED scalar, minimal coupling |(d - i q A) phi|^2 with phi = phi0 e^{i theta}.
#     Gauge-covariant kinetic term -> phi0^2 (dtheta - q A)^2  (standard).
L_charged = phi0**2 * (dth - q*A)**2
L_charged = sp.expand(L_charged)
# In unitary gauge (eat the Goldstone: dtheta -> 0) the A^2 coefficient IS the mass^2.
mass2_charged = sp.diff(L_charged.subs(dth,0), A, 2)/2
print("CHARGED condensate  |(d-iqA)phi|^2 :")
print("   L =", L_charged)
print("   photon mass^2 (unitary gauge) = (1/2) d^2L/dA^2 =", sp.simplify(mass2_charged))
print("   -> NONZERO for q!=0, phi0!=0.  This is the London/Meissner mass. (Gate LINK's fate.)\n")

# (2) NEUTRAL DIPOLE (double layer): net charge q = 0. The dipole couples to the FIELD
#     STRENGTH (polarisation P.E), i.e. through derivatives of A, not A itself.
#     Model coupling: L_dip = -P . E  with E ~ k*A in Fourier (a derivative coupling).
P = sp.symbols('P', real=True)
E = k*A                      # field strength ~ one derivative of A
L_dip = -P*E                 # dipole-field coupling (linear, a polarisation/source term)
print("NEUTRAL dipole (double layer), q=0, couples via P.E ~ derivative of A :")
print("   L_dip =", sp.expand(L_dip))
print("   photon mass^2 = (1/2) d^2 L_dip/dA^2 =", sp.diff(L_dip,A,2)/2)
print("   -> ZERO.  A linear/derivative dipole coupling gives NO A^2 term: no mass.\n")

# (3) A neutral quadratic polarisation term renormalises epsilon (the coeff of E^2),
#     i.e. the coeff of (kA)^2, NOT of A^2 -> shifts the SPEED, still massless.
chi = sp.symbols('chi', real=True)  # susceptibility
L_pol = sp.Rational(1,2)*chi*E**2
c_speed_term = sp.diff(L_pol,A,2)/2
print("NEUTRAL polarisation (1/2)chi E^2 :")
print("   coeff of A^2 (mass^2) =", sp.diff(L_pol.subs(k,0),A,2)/2, " (k->0: NO mass)")
print("   coeff structure ~", sp.simplify(c_speed_term), " (proportional to k^2 -> renormalises SPEED c, not mass)")
