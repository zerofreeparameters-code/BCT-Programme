#!/usr/bin/env python3
"""
Gate RATIO — Step 0: arithmetic, geometric identities, observable dependence.
Model executing: Claude Opus 4.8.
Verifies (a) the stated radii/product/ratio/xi, (b) that r_oct and r_tet are the
FCC close-packing interstitial radii of a single sphere radius R, hence NOT two
independent inputs, (c) that the ratio r_oct/r_tet is a scale-independent FCC
constant, (d) the power structure of every enumerated observable in the radii.
"""
from mpmath import mp, mpf, sqrt, pi, log
mp.dps = 40

# --- stated inputs (MINIMAL_BCT 1.3) ---
r_oct = (sqrt(2) - 1)/2
r_tet = (sqrt(6) - 2)/4
prod  = r_oct*r_tet
ratio = r_oct/r_tet
xi    = 1/sqrt(8*prod)
a0    = r_oct*r_tet/pi

print("=== stated inputs ===")
print(f"r_oct           = {mp.nstr(r_oct,12)}   (target 0.207106781187)")
print(f"r_tet           = {mp.nstr(r_tet,12)}   (target 0.112372435696)")
print(f"product r_o*r_t = {mp.nstr(prod,12)}    (target 0.023273093451)")
print(f"ratio r_o/r_t   = {mp.nstr(ratio,12)}   (target 1.843038997)")
print(f"xi (a=1)        = {mp.nstr(xi,12)} a     (target 2.3175 a)")
print(f"alpha_0         = {mp.nstr(a0,12)}       (target 0.00740805572755)")

# --- FCC close-packing interstitial identities, single sphere radius R ---
# octahedral hole radius = (sqrt2 - 1) R ; tetrahedral hole radius = (sqrt(3/2)-1) R
R = mpf(1)/2   # spheres of radius 1/2 => centre-centre contact = 1 = lattice unit
r_oct_fcc = (sqrt(2)-1)*R
r_tet_fcc = (sqrt(mpf(3)/2)-1)*R
print("\n=== FCC interstitial identity (single radius R = 1/2) ===")
print(f"(sqrt2-1)R        = {mp.nstr(r_oct_fcc,15)}  == r_oct ? {mp.almosteq(r_oct_fcc,r_oct)}")
print(f"(sqrt(3/2)-1)R    = {mp.nstr(r_tet_fcc,15)}  == r_tet ? {mp.almosteq(r_tet_fcc,r_tet)}")
print("=> BOTH radii are R times fixed pure constants: NOT two independent inputs.")

# --- ratio is scale-independent (same for any R) ---
ratio_const = (sqrt(2)-1)/(sqrt(mpf(3)/2)-1)
print("\n=== ratio is a fixed FCC constant, independent of scale R ===")
print(f"(sqrt2-1)/(sqrt(3/2)-1) = {mp.nstr(ratio_const,15)}")
print(f"equals r_oct/r_tet ?     {mp.almosteq(ratio_const, ratio)}")
for Rtest in [mpf('0.3'), mpf('1'), mpf('7.25')]:
    ro = (sqrt(2)-1)*Rtest; rt=(sqrt(mpf(3)/2)-1)*Rtest
    print(f"  R={float(Rtest):>5}: ratio={mp.nstr(ro/rt,12)} (invariant)")
print("=> The ratio carries ZERO information: it is forced by 'which packing' (FCC).")

# --- power structure of observables in (r_oct, r_tet) ---
# Any quantity depending on the radii ONLY through xi depends only on the PRODUCT.
# Write f ~ r_oct^p * r_tet^q ; product-only <=> p==q.
print("\n=== observable dependence: exponents (p in r_oct, q in r_tet) ===")
obs = [
 ("healing length xi = 1/sqrt(8 r_o r_t)", -0.5, -0.5),
 ("sound speed c_s ~ 1/xi",                +0.5, +0.5),
 ("amplitude gap 2/xi",                    +0.5, +0.5),
 ("vortex core size ~ xi",                 -0.5, -0.5),
 ("circulation quantum 2*pi (topological)", 0.0,  0.0),
 ("vortex energy/length (xi in log)",      -0.5, -0.5),  # only xi-dependence
 ("alpha_0 = r_o r_t / pi",                +1.0, +1.0),
 ("--- STEELMAN quantities reaching the SUBSTRATE radius ---", None, None),
 ("xi / r_oct  = 1/(sqrt8 r_o^{3/2} r_t^{1/2})", -1.5, -0.5),
 ("xi / r_tet  = 1/(sqrt8 r_o^{1/2} r_t^{3/2})", -0.5, -1.5),
]
for name,p,q in obs:
    if p is None:
        print(f"  {name}")
        continue
    tag = "PRODUCT-ONLY (p==q)" if abs(p-q)<1e-12 else "SEPARATE (p!=q) -> depends on RATIO"
    print(f"  p={p:+.1f} q={q:+.1f}  {tag:36s} {name}")

# numeric check of xi/r_oct = 11.19
val = xi/r_oct
print(f"\nxi/r_oct = {mp.nstr(val,8)}  (corpus Letter19 states 11.19)")
print("=> depends on radii SEPARATELY, but requires r_oct as an independent")
print("   observable, which the minimal action (only xi appears) does not provide.")
