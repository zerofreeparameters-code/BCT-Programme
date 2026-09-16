from mpmath import mp, mpf, mpc, sqrt, sin, cos, acos, exp, arg, matrix, det, conj, pi, chop
mp.dps = 40

def unitary_ckm(s12,s23,s13,delta):
    c12,c23,c13 = sqrt(1-s12**2),sqrt(1-s23**2),sqrt(1-s13**2)
    d=mpc(0,delta); em,ep=exp(-d),exp(d)
    R23=matrix([[1,0,0],[0,c23,s23],[0,-s23,c23]])
    U13=matrix([[c13,0,s13*em],[0,1,0],[-s13*ep,0,c13]])
    R12=matrix([[c12,s12,0],[-s12,c12,0],[0,0,1]])
    return R23*U13*R12

def jarlskog(V):
    return (V[0,1]*V[1,2]*conj(V[0,2])*conj(V[1,1])).imag

def hconj(M):
    return matrix([[conj(M[j,i]) for j in range(3)] for i in range(3)])

s12,s23,s13 = mpf('0.2248'),mpf('0.0422'),mpf('0.00365')
dBCT = acos(mpf(1)/3)
U = unitary_ckm(s12,s23,s13,dBCT)            # complex unitary carrying the BCT phase
Sd = matrix([[mpf('4.67'),0,0],[0,mpf('93.4'),0],[0,0,mpf('4180')]])   # real POSITIVE masses

print("="*66)
print("BRANCH 1 — BCT's stated symmetry:  M -> M*  (reality)")
print("="*66)
# reality: take M_d real => use REAL orthogonal rotation (delta=0)
Ureal = unitary_ckm(s12,s23,s13,mpf(0))
Md_real = Ureal*Sd*Ureal.T
Vckm_real = Ureal    # M_u diagonal real => CKM = Ureal (real orthogonal)
print("  M_d real symmetric? max|Im| =", mp.nstr(max(abs(Md_real[i,j].imag) for i in range(3) for j in range(3)),3))
print("  J_CKM  =", mp.nstr(jarlskog(Vckm_real),4), " -> NO CP violation")
print("  arg det M_d =", mp.nstr(chop(arg(det(Md_real))),4), " (real=0, but J=0: dead branch)")

print("="*66)
print("BRANCH 2 — the PARITY solution:  M -> M-dagger  (Hermiticity)")
print("="*66)
Md_herm = U*Sd*hconj(U)                       # Hermitian by construction, eigenvalues = Sd (>0)
Vckm_herm = U                                 # M_u diag real => CKM = U (complex)
maxantiherm = max(abs((Md_herm - hconj(Md_herm))[i,j]) for i in range(3) for j in range(3))
print("  M_d Hermitian? max|M - M-dagger| =", mp.nstr(chop(maxantiherm),3))
print("  off-diagonals complex? |Im M_d[0,1]| =", mp.nstr(abs(Md_herm[0,1].imag),4))
print("  J_CKM  =", mp.nstr(jarlskog(Vckm_herm),6), " -> CP VIOLATION PRESENT")
print("  det M_d =", mp.nstr(det(Md_herm).real,6),"+ i",mp.nstr(chop(det(Md_herm).imag),3))
print("  arg det M_d =", mp.nstr(chop(arg(det(Md_herm))),4), " -> arg det = 0  ✓  (both Barr conditions met)")

print("="*66)
print("RESIDUE — the {0, pi} degeneracy survives even in Branch 2")
print("="*66)
Sd_neg = matrix([[-mpf('4.67'),0,0],[0,mpf('93.4'),0],[0,0,mpf('4180')]])  # one negative eigenvalue
Md_neg = U*Sd_neg*hconj(U)
print("  Hermitian with one negative eigenvalue (same |masses|): arg det M_d =",
      mp.nstr(chop(arg(det(Md_neg))),4), "= pi  -> theta = pi, excluded but NOT forbidden by Hermiticity")
