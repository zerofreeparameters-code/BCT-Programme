# GATE KL — Step 0 cold numerics. Deterministic, re-runnable.
# Computes void radii, alpha0, healing length xi/a, sphere radius, and natural knot size.
from mpmath import mp, mpf, sqrt, pi, nstr
mp.dps = 60

r_oct = (sqrt(2) - 1)/2                      # octahedral void inradius (BCT units)
r_tet = (sqrt(6) - 2)/4                      # tetrahedral void inradius (BCT units)
alpha0 = r_oct*r_tet/pi                       # BCT coupling  (~1/135)
prod   = r_oct*r_tet
ratio  = r_oct/r_tet

# Two stated forms of the healing length; must be identical:
xi_gate = 1/sqrt(8*pi*alpha0)                 # gate form:      1/sqrt(8*pi*alpha0)
xi_min  = 1/sqrt(8*r_oct*r_tet)              # MINIMAL_BCT:    1/sqrt(8*r_oct*r_tet)

R_s = xi_min/mpf('4.6')                       # implied by MINIMAL_BCT "xi spans 4.6 sphere radii"

def p(name, val, d=40):
    print(f"{name:32s} = {nstr(val, d)}")

print("=== Void geometry (BCT units, a = lattice period) ===")
p("r_oct = (sqrt2-1)/2", r_oct)
p("r_tet = (sqrt6-2)/4", r_tet)
p("alpha0 = r_oct*r_tet/pi", alpha0)
p("1/alpha0", 1/alpha0)
p("product r_oct*r_tet", prod)
p("ratio  r_oct/r_tet", ratio)
print()
print("=== Healing length: two forms must agree ===")
p("xi/a  [1/sqrt(8*pi*alpha0)]", xi_gate)
p("xi/a  [1/sqrt(8*r_oct*r_tet)]", xi_min)
p("difference", xi_gate - xi_min)
print(f"forms identical to 55 dps? {abs(xi_gate-xi_min) < mpf(10)**(-55)}")
print()
print("=== Sizes in units of the lattice period a ===")
p("xi/a", xi_min)
p("R_s/a (implied, ~a/2)", R_s)
p("xi / R_s  (knot size in sphere radii)", xi_min/R_s)
print()
print("=== The load-bearing ratio: natural knot size vs FCC period ===")
p("lambda* ~ xi, period = a  ->  lambda*/period", xi_min)   # one charge per primitive cell, period=a
print("  -> natural texture size is ~2.32x the period it is asked to sit in.")
