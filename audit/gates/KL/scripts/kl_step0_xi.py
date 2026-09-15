#!/usr/bin/env python3
"""
GATE KL - Step 0: geometry-fixed coefficients, cold.
Derives xi/a and the natural Faddeev knot size lambda* from the void radii ONLY.
No ledger, no note, no prior gate consulted. mpmath, 60 dps, report 40.
"""
from mpmath import mp, mpf, sqrt, pi, nstr
mp.dps = 60

# --- Void radii (given geometric facts; §1 of the prompt) ---
r_oct = (sqrt(2) - 1) / 2            # (sqrt2 - 1)/2
r_tet = (sqrt(6) - 2) / 4            # (sqrt6 - 2)/4

# --- Geometric dimensionless coupling ---
alpha0 = r_oct * r_tet / pi          # a0 = r_oct r_tet / pi

# --- Healing length in lattice units ---
# GP healing length xi^2 = hbar^2/(2 m g rho0); in BCT lattice units the
# geometry fixes the dimensionless coupling so that  xi/a = 1/sqrt(8 pi a0).
xi_over_a  = 1 / sqrt(8 * pi * alpha0)
# cross-check the equivalent closed form 1/sqrt(8 r_oct r_tet):
xi_alt     = 1 / sqrt(8 * r_oct * r_tet)

# --- Faddeev natural size: lambda* = sqrt(c4/c2) * sqrt(I4/I2).
# BFN reduction gives c4/c2 = kappa * xi^2 with kappa = O(1); the shape ratio
# sqrt(I4/I2) is O(1). With kappa = 1 and shape ratio = 1 (order-of-magnitude,
# stated as such), lambda*/a ~ xi/a. Report the scale, not a tuned number.
lam_over_a = xi_over_a               # order-of-magnitude: lambda* ~ xi

# --- FCC / BCT geometry ---
c_over_a   = sqrt(2)                 # BCT with c/a=sqrt2 == FCC

def show(name, val):
    print(f"{name:<28} = {nstr(val, 40)}")

print("=== GATE KL Step 0 : geometry-fixed inputs (cold, 40 dps) ===")
show("r_oct = (sqrt2-1)/2", r_oct)
show("r_tet = (sqrt6-2)/4", r_tet)
show("alpha0 = r_oct r_tet / pi", alpha0)
show("xi/a = 1/sqrt(8 pi a0)", xi_over_a)
show("xi/a = 1/sqrt(8 r_o r_t)", xi_alt)
print(f"  consistency |diff|        = {nstr(abs(xi_over_a-xi_alt),5)}")
show("lambda*/a  (~ xi/a, O(1))", lam_over_a)
show("c/a (BCT->FCC identity)", c_over_a)
print()
print(f"xi/a rounded               = {nstr(xi_over_a, 6)}")
print(f"knot size vs cell: lambda*/a = {nstr(lam_over_a,6)}  -> "
      f"{'EXCEEDS' if lam_over_a>1 else 'fits'} the lattice period a")
