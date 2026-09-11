from mpmath import mp, mpf, sqrt, pi, tanh, atanh, log
mp.dps = 40
r_tet=(sqrt(6)-2)/4; r_oct=(sqrt(2)-1)/2; R=mpf(1)/2
alpha0=r_tet*r_oct/(4*pi*R**2); xiGP=1/sqrt(8*pi*alpha0)

print("=== A. What must xi be for the discarded factor 4*pi*R*tanh^2(r_oct/xi) to equal 1? ===")
need_t2 = 1/(4*pi*R)                 # tanh^2 required
need_t  = sqrt(need_t2)
x_req   = atanh(need_t)              # = r_oct/xi
xi_req  = r_oct/x_req
print("  required tanh^2      =", need_t2, " (=1/2pi)")
print("  required r_oct/xi    =", x_req)
print("  required xi          =", xi_req)
print("  R                    =", R, "   xi_required/R =", xi_req/R)
print()
print("=== B. The three xi conventions the corpus actually uses ===")
for name,xi,src in [("xi_GP = 1/sqrt(8 pi a0)", xiGP, "AppF L3003/3006/3739; App J S2.2 uses it (2/xi=0.8630)"),
                    ("xi = R  (vortex core)",   R,    "AppVol1 L2846,2900,2921,2975,2991,3093"),
                    ("xi = r_oct (tight-bind)", r_oct,"AppVol1 L3031")]:
    t2=tanh(r_oct/xi)**2; fac=4*pi*R*t2; g=alpha0*fac
    print(f"  {name:26s} xi={mp.nstr(xi,8):10s} r_oct/xi={mp.nstr(r_oct/xi,6):9s} "
          f"factor={mp.nstr(fac,6):9s} g={mp.nstr(g,6):11s} g/alpha0={mp.nstr(fac,6)}")
    print(f"       source: {src}")
print()
print("=== C. Does the 'leading order in the tanh suppression' defence work? ===")
t2_lead = (r_oct/xiGP)**2            # tanh x ~ x, small-argument leading order
print("  tanh^2 exact            =", t2_lead*0+tanh(r_oct/xiGP)**2)
print("  leading order (x^2)     =", t2_lead)
print("  g under leading order   =", alpha0*4*pi*R*t2_lead)
print("  ratio alpha0/g          =", 1/(4*pi*R*t2_lead))
print("  -> small-argument leading order does NOT send tanh^2 to 1; it sends it to 0.00799.")
print()
print("=== D. Steelman winner: xi = R ===")
facR = 4*pi*R*tanh(r_oct/R)**2
print("  4*pi*R*tanh^2(r_oct/R) =", facR, "  deviation from 1:", (facR-1)*100, "%")
print("  g(xi=R)                =", alpha0*facR)
print("  near-identity: tanh(sqrt2-1) =", tanh(sqrt(2)-1), " vs 1/sqrt(2pi) =", 1/sqrt(2*pi))
