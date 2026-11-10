# Gate BULK card-thread validation (NOT the run): dimensional check of G = c^4/(8 pi K)
# with the corpus's own K = rho_0 c^2, rho_0 = rho_Planck.  CODATA 2022.
from mpmath import mp, mpf, pi, sqrt
mp.dps = 60
c  = mpf('299792458')
h  = mpf('6.62607015e-34'); hbar = h/(2*pi)
G  = mpf('6.67430e-11')
lP = sqrt(hbar*G/c**3)
FP = c**4/G                       # Planck force  [N]
rhoP = c**5/(hbar*G**2)           # Planck mass density [kg m^-3]
PP = rhoP*c**2                    # Planck pressure [Pa]
K_AZ6 = rhoP*c**2                 # AZ6 / Letter 20: K_BCT = rho_0 c^2 with rho_0 = rho_Planck
G_from_K = c**4/(8*pi*K_AZ6)      # printed formula evaluated in SI
print("Planck force   c^4/G        = %s N"  % mp.nstr(FP, 12))
print("Planck pressure rho_P c^2   = %s Pa" % mp.nstr(PP, 12))
print("ratio (c^4/G)/(rho_P c^2)   = %s m^2 ; l_P^2 = %s m^2" % (mp.nstr(FP/PP, 12), mp.nstr(lP**2, 12)))
print("c^4/(8 pi rho_P c^2)        = %s  (units m^5 kg^-1 s^-2, NOT G's m^3 kg^-1 s^-2)" % mp.nstr(G_from_K, 12))
print("  = G * l_P^2/(8 pi) ?  ->  %s" % mp.nstr(G_from_K/(G*lP**2/(8*pi)), 40))
# the length^2 that closes the identity: L^2 = l_P^2/(8 pi)
print("closing length L/l_P = 1/sqrt(8 pi) = %s" % mp.nstr(1/sqrt(8*pi), 40))
print("1/(8 pi)                    = %s" % mp.nstr(1/(8*pi), 40))
# geometry at c/a = sqrt2 (FCC, touching spheres)
print("FCC packing pi/(3 sqrt2)    = %s" % mp.nstr(pi/(3*sqrt(2)), 40))
print("FCC void fraction           = %s" % mp.nstr(1-pi/(3*sqrt(2)), 40))
print("App AI/AL rho_D4 = pi^2/16  = %s" % mp.nstr(pi**2/16, 40))
# App AI.4 as printed: G_eff = c^4/(16 pi rho_P) = hbar G^2/(16 pi c)  [units s, per App AL]
print("App AI.4 c^4/(16 pi rho_P)  = %s  (dimension: time, per App AL)" % mp.nstr(c**4/(16*pi*rhoP), 12))
