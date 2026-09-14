from mpmath import mp, mpf, sqrt, tanh, pi
mp.dps = 40

# Geometric inputs (units of edge length a = 1 = l_P), from App D.2 p.27 / App C p.24-26
r_oct = (sqrt(2) - 1)/2          # (√2-1)/2
r_tet = (sqrt(6) - 2)/4          # (√6-2)/4
R     = mpf(1)/2                 # sphere radius R = a/2

# alpha0 = fine structure candidate, App D: r_tet*r_oct/(4 pi R^2)
alpha0 = r_tet*r_oct/(4*pi*R**2)

# healing length, App I/J region p.81: xi = a/sqrt(8 pi alpha0)
xi = mpf(1)/sqrt(8*pi*alpha0)

# App J 3.1 factors
four_pi_R      = 4*pi*R                     # printed 6.2832
arg            = r_oct/xi                   # printed 0.0894
tanh2          = tanh(arg)**2               # printed 0.007944
g_computed     = alpha0 * four_pi_R * tanh2 # printed 0.00036975
g_boxed        = alpha0                     # boxed "g ~ alpha0"
ratio          = g_boxed/g_computed
discarded      = four_pi_R * tanh2          # the factor dropped to claim g~alpha0

print("=== Independent 40-dps reproduction of App J 3.1 ===")
print("r_oct              =", mp.nstr(r_oct, 20), "   (printed 0.207107)")
print("r_tet              =", mp.nstr(r_tet, 20), "   (printed 0.112372)")
print("R                  =", mp.nstr(R, 20),     "   (printed 0.500000)")
print("alpha0 = rtet*roct/(4 pi R^2) =", mp.nstr(alpha0, 20), " (printed 0.00740806)")
print("xi = a/sqrt(8 pi alpha0)      =", mp.nstr(xi, 20),    " (implied ~2.3177)")
print("xi/r_oct            =", mp.nstr(xi/r_oct, 10), " (p.96 table: 11.1901)")
print("2/xi                =", mp.nstr(2/xi, 10),     " (p.114: 0.8630)")
print("4 pi R              =", mp.nstr(four_pi_R, 12), " (printed 6.2832)")
print("r_oct/xi (arg)      =", mp.nstr(arg, 12),       " (printed 0.0894)")
print("tanh^2(arg)         =", mp.nstr(tanh2, 12),     " (printed 0.007944)")
print("--- the two values ---")
print("g_computed = alpha0*4piR*tanh^2 =", mp.nstr(g_computed, 12), " (printed 0.00036975)")
print("g_boxed    = alpha0             =", mp.nstr(g_boxed, 12),    " (boxed 'to leading order')")
print("RATIO g_boxed/g_computed        =", mp.nstr(ratio, 12))
print("discarded factor 4piR*tanh^2    =", mp.nstr(discarded, 12), " (= 1/ratio)")
