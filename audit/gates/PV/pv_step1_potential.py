"""
GATE PV - Step 1 (P-transfer test). Static charge-charge interaction of the
vector-charge theory, derived cold in Fourier space.

Static: E^{ij} = -d^{(i} phi^{j)}  (phi^j = A^{0j}, the vector scalar potential).
Gauss:  d_i E^{ij} = rho^j
     => -(1/2)( laplacian phi^j + d^j (d_i phi^i) ) = rho^j.

In Fourier space (d_i -> i k_i):
   (1/2)( k^2 phi^j + k^j (k.phi) ) = rho^j(k).
Solve for phi^j(k), then interaction V(k) = phi^j(k) rho*^j(k) between two
point vector charges q1, q2; inverse-transform the angular structure.
"""
import sympy as sp

k1,k2,k3 = sp.symbols('k1 k2 k3', real=True)
k = sp.Matrix([k1,k2,k3])
k2n = (k1**2+k2**2+k3**2)
q = sp.Matrix(sp.symbols('q1 q2 q3', real=True))     # source vector charge rho^j

# operator M_{jl} phi^l = rho^j :  M = (1/2)(k^2 I + k k^T)
I3 = sp.eye(3)
M = sp.Rational(1,2)*(k2n*I3 + k*k.T)
Minv = sp.simplify(M.inv())
phi = sp.simplify(Minv*q)                            # phi^j(k)

# interaction with a second charge q2 (use symbols p = q2)
p = sp.Matrix(sp.symbols('p1 p2 p3', real=True))
Vk = sp.simplify((phi.T*p)[0])                       # V(k) = phi.p
print("V(k) =", Vk)

# Split into (q.p)/k^2  and  (q.k)(p.k)/k^4 structure:
qp = (q.T*p)[0]
qk = (q.T*k)[0]
pk = (p.T*k)[0]
# propose V(k) = a*(q.p)/k^2 + b*(q.k)(p.k)/k^4 ; solve a,b
a,b = sp.symbols('a b')
ansatz = a*qp/k2n + b*qk*pk/k2n**2
res = sp.simplify(Vk - ansatz)
sol = sp.solve([sp.Poly(sp.numer(sp.together(res)), q[0],q[1],q[2],p[0],p[1],p[2]).coeff_monomial(m)
                for m in [q[0]*p[0], q[0]*p[1]]], [a,b], dict=True)
print("fit a,b :", sol)

# Real-space: (q.p)/k^2 -> (q.p)/(4 pi r) isotropic.
# (q.k)(p.k)/k^4 -> orientation-dependent dipolar kernel ~ [ (q.p) + (q.rhat)(p.rhat) ]/r
print()
print("Structure of V(k): an isotropic (q.p)/k^2 piece PLUS a (q.k)(p.k)/k^4 piece.")
print("The second term inverse-transforms to an ANGLE-DEPENDENT kernel")
print("   ~ [ (q.p) - 3 (q.rhat)(p.rhat) ] type / r  (a dipolar / inner-product-with-")
print("   orientation-dependent-sign structure), NOT an isotropic scalar Coulomb.")
