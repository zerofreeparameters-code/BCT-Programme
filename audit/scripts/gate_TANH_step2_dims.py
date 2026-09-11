from mpmath import mp, mpf, sqrt, pi, tanh, cos, sin, findroot
mp.dps = 40
r_tet=(sqrt(6)-2)/4; r_oct=(sqrt(2)-1)/2; R=mpf(1)/2
a0=r_tet*r_oct/(4*pi*R**2); xi=1/sqrt(8*pi*a0)

print("=== Verify App J S2 (kappa_0) is independent of the S3.1 defect ===")
rhs = -1/xi + a0
f = lambda k: k*cos(k*R)/sin(k*R) - rhs
roots=[]
for guess in [3.4, 9.5, 15.8]:
    roots.append(findroot(f, mpf(guess)))
print("  RHS = -1/xi + alpha0 =", rhs, " (App J prints -0.424083)")
for i,k in enumerate(roots,1):
    print(f"  mode {i}: kappa = {mp.nstr(k,8)}   (App J prints 3.3905 / 9.5139 / 15.762)")
print("  -> S2 reproduces exactly. kappa_0 uses sigma_s/J = alpha0, NOT g. S2 is untouched.")
print()
print("=== Dimensional audit of the S3.1 expression ===")
print("  BC:  [d_r Psi] = -(sigma_s/J) Psi(R)      => sigma_s/J has units 1/length")
print("  S2.1 kappa cot(kR) = -1/xi + sigma_s/J    => consistent, both 1/length  OK")
print("  S1.3 'in units J=1: sigma_s = alpha0'     => alpha0 here carries 1/length")
print("  S3.1 g = (sigma_s/J) * 4 pi R^2 / R       => (1/len)*(len) = dimensionless OK")
print("  BUT alpha_0 = r_tet r_oct/(4 pi R^2) is DIMENSIONLESS by construction.")
print("  So 'sigma_s/J = alpha_0' silently sets l_P = 1; sigma_s/J = alpha_0 / l_P.")
print("  Restoring l_P:  g = alpha0 * (4 pi R / l_P) * tanh^2  -> with R = l_P/2:")
print("     4 pi R / l_P =", 4*pi*R, " = 2 pi, NOT 1.")
print("  => even with tanh -> 1 the boxed g = alpha0 needs 2pi -> 1. It does not.")
print("     g(tanh->1) =", a0*4*pi*R, " = 2 pi alpha0 =", (4*pi*R))
print()
print("=== GP profile convention: standard wall solution carries 1/sqrt(2) ===")
t2_std = tanh(r_oct/(sqrt(2)*xi))**2
print("  App J uses tanh(r_oct/xi)      -> tanh^2 =", tanh(r_oct/xi)**2)
print("  Standard GP tanh(x/(sqrt2 xi)) -> tanh^2 =", t2_std)
print("  g under standard GP convention =", a0*4*pi*R*t2_std)
print("  ratio alpha0/g                 =", 1/(4*pi*R*t2_std))
print("  -> the convention question is live and moves the answer by a further 2x.")
