#!/usr/bin/env python3
# GATE ICE - STEP 2 (soft branch): does the GP stiffness J cancel, and what ratio controls the phase?
# Rotor/Josephson mapping of a Gross-Pitaevskii lattice superfluid on the void network.
import sympy as sp
hbar,m,a,xi,nbar,g,t,U,n = sp.symbols('hbar m a xi nbar g t U n', positive=True)

# Josephson (phase) energy per link and charging (number) energy per site, large-nbar rotor limit:
E_J = 2*t*nbar                       # Josephson coupling  (t = single-particle tunnelling scale)
E_C = U                              # charging energy
t_expr  = hbar**2/(2*m*a**2)         # tunnelling scale over void spacing a
# number density n = nbar/a^3 ; healing length xi^2 = hbar^2/(2 m g n)  ->  solve g
n_expr  = nbar/a**3
g_expr  = sp.solve(sp.Eq(xi**2, hbar**2/(2*m*g*n_expr)), g)[0]
U_expr  = g_expr/a**3                # on-site interaction = g / void volume

ratio = (E_J/E_C).subs({t:t_expr, U:U_expr}).subs(g, g_expr)
ratio = sp.simplify(ratio)
print("E_J =", sp.simplify(E_J.subs(t,t_expr)))
print("E_C = U =", sp.simplify(U_expr))
print("E_J/E_C =", ratio)                       # expect 2*nbar^2*(xi/a)^2
print("hbar in ratio?", hbar in ratio.free_symbols, "| m in ratio?", m in ratio.free_symbols)
print("free symbols of ratio:", ratio.free_symbols)
# superfluid (single Goldstone phonon) when ratio >~ 1  <=>  nbar*(xi/a) >~ 1/sqrt(2)
print("superfluid threshold nbar*(xi/a) =", sp.sqrt(sp.Rational(1,2)))
