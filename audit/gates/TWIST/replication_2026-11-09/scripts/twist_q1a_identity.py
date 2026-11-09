#!/usr/bin/env python3
"""
Gate TWIST — Q1(a).  Verify, on random smooth CP^1 fields chi(x) in C^2 with |chi| = 1,
the identities

    (I1)  sum_i |d_i chi|^2  =  1/4 sum_i |d_i n|^2  +  sum_i a_i^2 ,
          with n = chi^dag sigma chi,  a_i = -i chi^dag d_i chi  (real),
    (I2)  d_i a_j - d_j a_i  =  1/2 n . (d_i n x d_j n)        (Mermin-Ho),
    (I3)  |grad Psi|^2 = (grad sqrt(rho))^2 + rho |grad chi|^2  for Psi = sqrt(rho) chi,
    (I4)  under chi -> e^{i lambda(x)} chi:  n unchanged,  a -> a + grad lambda.

Method: chi is built from a random trigonometric polynomial psi in C^2 (3 Fourier modes per
component), normalised; all derivatives are taken EXACTLY with sympy and evaluated with
mpmath at 60 significant digits at random points.  The card asks for 1e-10; we report the
maximum residual at 40 digits.

Source for the identities: standard CP^1 decomposition (e.g. Babaev, Faddeev & Niemi,
PRB 65, 100512 (2002), eqs. for the two-component GL functional).  Nothing here is
BCT-specific; this step only checks the variables the card uses are consistent.
"""
import random
import sympy as sp
import mpmath as mp

mp.mp.dps = 60
random.seed(20261109)

x, y, z = sp.symbols('x y z', real=True)
X = (x, y, z)

def rand_coef():
    return sp.Rational(random.randint(-9, 9), 4)

def trig_poly(nmodes=3):
    """random complex trigonometric polynomial in (x,y,z)"""
    expr = sp.Rational(random.randint(1, 5), 2) + sp.I * sp.Rational(random.randint(-3, 3), 2)
    for _ in range(nmodes):
        kx, ky, kz = (sp.Rational(random.randint(-2, 2)) for _ in range(3))
        phase = sp.Rational(random.randint(0, 7), 4) * sp.pi
        amp = rand_coef() + sp.I * rand_coef()
        expr += amp * sp.exp(sp.I * (kx * x + ky * y + kz * z + phase))
    return expr

def build_field():
    psi1, psi2 = trig_poly(), trig_poly()
    norm = sp.sqrt(sp.expand(psi1 * sp.conjugate(psi1) + psi2 * sp.conjugate(psi2)))
    chi = sp.Matrix([psi1 / norm, psi2 / norm])
    return chi

def pauli():
    s1 = sp.Matrix([[0, 1], [1, 0]])
    s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    s3 = sp.Matrix([[1, 0], [0, -1]])
    return (s1, s2, s3)

def dag(v):
    return v.H

def main():
    sig = pauli()
    results = {"I1": [], "I2": [], "I3": [], "I4n": [], "I4a": []}
    for trial in range(3):
        chi = build_field()
        chid = dag(chi)
        # n = chi^dag sigma chi (real 3-vector)
        n = sp.Matrix([(chid * s * chi)[0] for s in sig])
        # a_i = -i chi^dag d_i chi
        dchi = [chi.diff(v) for v in X]
        a = [(-sp.I * (chid * dchi[i])[0]) for i in range(3)]
        dn = [n.diff(v) for v in X]
        # I1
        lhs1 = sum((dag(dchi[i]) * dchi[i])[0] for i in range(3))
        rhs1 = sp.Rational(1, 4) * sum((dn[i].T * dn[i])[0] for i in range(3)) + sum(a[i] ** 2 for i in range(3))
        # I2 (all three (i,j) pairs)
        curl_lhs = [a[1].diff(x) - a[0].diff(y), a[2].diff(y) - a[1].diff(z), a[0].diff(z) - a[2].diff(x)]
        curl_rhs = [sp.Rational(1, 2) * n.dot(dn[0].cross(dn[1])),
                    sp.Rational(1, 2) * n.dot(dn[1].cross(dn[2])),
                    sp.Rational(1, 2) * n.dot(dn[2].cross(dn[0]))]
        # I3 with a random smooth positive rho
        rho = 2 + sp.cos(x + 2 * y) ** 2 + sp.Rational(1, 3) * sp.sin(z - x)
        Psi = sp.sqrt(rho) * chi
        dPsi = [Psi.diff(v) for v in X]
        lhs3 = sum((dag(dPsi[i]) * dPsi[i])[0] for i in range(3))
        sq = sp.sqrt(rho)
        rhs3 = sum(sq.diff(v) ** 2 for v in X) + rho * lhs1
        # I4 gauge
        lam = sp.sin(x) * sp.cos(2 * z) + y / 3
        chig = sp.exp(sp.I * lam) * chi
        chigd = dag(chig)
        ng = sp.Matrix([(chigd * s * chig)[0] for s in sig])
        ag = [(-sp.I * (chigd * chig.diff(v))[0]) for v in X]
        gl = [lam.diff(v) for v in X]

        f_lhs1 = sp.lambdify(X, lhs1, 'mpmath'); f_rhs1 = sp.lambdify(X, rhs1, 'mpmath')
        f_cl = [sp.lambdify(X, e, 'mpmath') for e in curl_lhs]
        f_cr = [sp.lambdify(X, e, 'mpmath') for e in curl_rhs]
        f_lhs3 = sp.lambdify(X, lhs3, 'mpmath'); f_rhs3 = sp.lambdify(X, rhs3, 'mpmath')
        f_n = sp.lambdify(X, n, 'mpmath'); f_ng = sp.lambdify(X, ng, 'mpmath')
        f_a = [sp.lambdify(X, e, 'mpmath') for e in a]
        f_ag = [sp.lambdify(X, e, 'mpmath') for e in ag]
        f_gl = [sp.lambdify(X, e, 'mpmath') for e in gl]

        for _ in range(7):
            pt = [mp.mpf(random.random()) * 6 - 3 for _ in range(3)]
            r1 = abs(f_lhs1(*pt) - f_rhs1(*pt))
            r2 = max(abs(f_cl[k](*pt) - f_cr[k](*pt)) for k in range(3))
            r3 = abs(f_lhs3(*pt) - f_rhs3(*pt))
            nn = f_n(*pt); nng = f_ng(*pt)
            r4n = max(abs(nn[k] - nng[k]) for k in range(3))
            r4a = max(abs(f_ag[k](*pt) - f_a[k](*pt) - f_gl[k](*pt)) for k in range(3))
            # sanity: |n| = 1, a real
            assert abs(mp.sqrt(sum(nn[k] ** 2 for k in range(3))) - 1) < mp.mpf('1e-50')
            assert all(abs(mp.im(f_a[k](*pt))) < mp.mpf('1e-50') for k in range(3))
            results["I1"].append(r1); results["I2"].append(r2); results["I3"].append(r3)
            results["I4n"].append(r4n); results["I4a"].append(r4a)

    print("Gate TWIST Q1(a): identity checks, exact derivatives, mpmath 60 dps, 3 random fields x 7 points")
    for key, label in [("I1", "|grad chi|^2 = 1/4|grad n|^2 + a^2"),
                       ("I2", "curl a = 1/2 n.(dn x dn)  (Mermin-Ho)"),
                       ("I3", "|grad Psi|^2 = (grad sqrt rho)^2 + rho|grad chi|^2"),
                       ("I4n", "n gauge-invariant"),
                       ("I4a", "a -> a + grad lambda")]:
        worst = max(results[key])
        print(f"  {key:4s} {label:52s} max residual = {mp.nstr(worst, 5)}   "
              f"{'PASS (<1e-10)' if worst < mp.mpf('1e-10') else 'FAIL'}")

if __name__ == "__main__":
    main()
