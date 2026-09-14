from mpmath import mp, mpf, sqrt, tanh, atanh, pi
mp.dps = 40
r_oct = (sqrt(2)-1)/2
r_tet = (sqrt(6)-2)/4
R = mpf(1)/2
alpha0 = r_tet*r_oct/(4*pi*R**2)

def factor(xi):
    return 4*pi*R*tanh(r_oct/xi)**2

xi_heal = mpf(1)/sqrt(8*pi*alpha0)   # healing length (used in the printed arithmetic)
xi_core = R                           # vortex-core convention used pp.77-81 (xi = R_sphere)
xi_tb   = r_oct                       # tight-binding limit used p.82 (xi = r_oct)

print("Discarded factor 4piR*tanh^2(r_oct/xi) under each xi convention the corpus uses:")
for name,xi in [("xi = a/sqrt(8 pi a0)  [healing, PRINTED]",xi_heal),
                ("xi = R  [vortex core, pp.77-81]        ",xi_core),
                ("xi = r_oct [tight-binding, p.82]       ",xi_tb)]:
    f = factor(xi)
    g = alpha0*f
    print(f"  {name}: xi={mp.nstr(xi,8):>10}  r_oct/xi={mp.nstr(r_oct/xi,8):>10}"
          f"  factor={mp.nstr(f,8):>10}  g={mp.nstr(g,8):>12}  g/alpha0={mp.nstr(f,6)}")

# what xi makes factor exactly 1?
# 2pi*tanh^2(r_oct/xi)=1 -> tanh(r_oct/xi)=1/sqrt(2pi) -> xi = r_oct/atanh(1/sqrt(2pi))
xi_star = r_oct/atanh(1/sqrt(2*pi))
print("\nxi that makes discarded factor exactly 1:", mp.nstr(xi_star,10),
      "  (compare R=0.5, healing=2.3175)")
print("So the boxed 'g~alpha0' holds only for xi ~", mp.nstr(xi_star,6),
      "i.e. essentially the xi=R (vortex-core) convention, NOT the healing length.")
print("\nUnder xi=R the boxed claim is off by only", mp.nstr((1-factor(R))*100,4),"%")
print("Under xi=healing (as printed) it is off by a factor", mp.nstr(1/factor(xi_heal),8))
