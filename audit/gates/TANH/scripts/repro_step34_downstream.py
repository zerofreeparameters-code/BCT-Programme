from mpmath import mp, mpf, sqrt, tanh, exp, pi
mp.dps = 40
r_oct=(sqrt(2)-1)/2; r_tet=(sqrt(6)-2)/4; R=mpf(1)/2
alpha0=r_tet*r_oct/(4*pi*R**2)
xi=mpf(1)/sqrt(8*pi*alpha0)
g_box=alpha0
g_true=alpha0*4*pi*R*tanh(r_oct/xi)**2   # 0.00036975

kappa0=mpf("3.39"); xi_geom=mpf("0.05")   # App J 3.2 inputs
def dE(g): return -g**2/(kappa0-xi_geom)
print("=== App J 3.2 second-order shift (only in-corpus numeric use of g, MECHANISM REJECTED) ===")
print("dE(g=alpha0, boxed) =", mp.nstr(dE(g_box),6), "m_P   (printed -1.6429e-5)")
print("dE(g=alpha0/20,true)=", mp.nstr(dE(g_true),6), "m_P")
print("m_e target          = 4.2e-23 m_P")
print("boxed too large by  :", mp.nstr(dE(g_box)/mpf('-4.2e-23'),4), "x")
print("true  too large by  :", mp.nstr(dE(g_true)/mpf('-4.2e-23'),4), "x  -> STILL rejected")

print("\n=== App J 4.1 Kondo (MECHANISM REJECTED) ===")
rho=mpf("1.6e-4")
def kondo(g): return -1/(rho*g)   # exponent
print("exponent -1/(rho*g), g=alpha0 :", mp.nstr(kondo(g_box),6), " (printed ~ -823000)")
print("exponent -1/(rho*g), g=true   :", mp.nstr(kondo(g_true),6), " -> even smaller mass, STILL rejected")

print("\n=== The identity claim, numerically ===")
print("interior<->void overlap coupling g  =", mp.nstr(g_true,8), "= alpha0/", mp.nstr(alpha0/g_true,7))
print("surface/boundary coupling sigma_s/J =", mp.nstr(alpha0,8), "= alpha0 (correct, App D & J-1.3)")
print("'g = alpha0 exactly' (Vol2 p457)    : FALSE for overlap coupling; TRUE only for sigma_s/J")
