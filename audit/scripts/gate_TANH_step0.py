from mpmath import mp, mpf, sqrt, pi, tanh, cot, findroot
mp.dps = 40

# --- geometry, derived from corpus primary source, not from App J's printed numbers ---
# AppVol1 Part1 L1007-1008, L3362-3363 : r_tet=(sqrt6-2)/4, r_oct=(sqrt2-1)/2  (units a = l_P = 1)
# AppVol1 Part1 L4909               : R = 1/2  =>  4*pi*R^2 = pi
r_tet = (sqrt(6)-2)/4
r_oct = (sqrt(2)-1)/2
R     = mpf(1)/2
# App D  : alpha_0 = r_tet*r_oct/(4 pi R^2)
alpha0 = r_tet*r_oct/(4*pi*R**2)
# App F  : xi = 1/sqrt(8 pi alpha_0)   (AppVol1 Part1 L3003,L3006,L3739)
xi_GP = 1/sqrt(8*pi*alpha0)

print("r_tet          =", r_tet)
print("r_oct          =", r_oct)
print("R              =", R)
print("alpha_0        =", alpha0, "   (App J prints 0.00740806)")
print("xi_GP          =", xi_GP,  "   (corpus prints 2.3175)")
print("2/xi_GP        =", 2/xi_GP,"   (App J S2.2 prints 0.8630)")
print("r_oct/xi_GP    =", r_oct/xi_GP, "   (App J S3.1 prints 0.0894)")
print("-1/xi + alpha0 =", -1/xi_GP+alpha0, " (App J S2.1 prints -0.424083)")
print()
# --- reproduce every printed factor of S3.1 ---
fourPiR = 4*pi*R
t2      = tanh(r_oct/xi_GP)**2
g_full  = alpha0*fourPiR*t2
print("FACTOR  4*pi*R            =", fourPiR, "  (App J prints 6.2832)")
print("FACTOR  tanh^2(r_oct/xi)  =", t2,      "  (App J prints 0.007944)")
print("PRODUCT g (computed)      =", g_full,  "  (App J prints 0.00036975)")
print("BOXED   g = alpha_0       =", alpha0)
print("RATIO   boxed/computed    =", alpha0/g_full)
print("DISCARDED FACTOR 4piR*t2  =", fourPiR*t2, "   1/that =", 1/(fourPiR*t2))
print()
# --- check App J's own printed-number arithmetic is self-consistent ---
pj = mpf('0.00740806')*mpf('6.2832')*mpf('0.007944')
print("App J printed-factor product =", pj, " vs its printed result 0.00036975")
