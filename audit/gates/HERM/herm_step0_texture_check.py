import numpy as np
np.random.seed(20260916)

def ckm_and_argdet(Mu, Md):
    # Left-diagonalisation: M M^dagger = V_L diag V_L^dagger
    def left_unitary(M):
        H = M @ M.conj().T
        w, V = np.linalg.eigh(H)      # columns = eigenvectors, ascending
        return V
    VuL = left_unitary(Mu)
    VdL = left_unitary(Md)
    V = VuL.conj().T @ VdL            # CKM
    # Jarlskog: J = Im(V_us V_cb V_ub^* V_cs^*)  (indices 0,1,2 = u/d,c/s,t/b)
    J = np.imag(V[0,1]*V[1,2]*np.conj(V[0,2])*np.conj(V[1,1]))
    argdet = np.angle(np.linalg.det(Mu)*np.linalg.det(Md))
    return J, argdet

# --- Branch A: REAL textures (M -> M*, generalised-CP / reality) ---
Ja=[]; Aa=[]
for _ in range(2000):
    Mu = np.random.randn(3,3)         # real
    Md = np.random.randn(3,3)         # real
    J, a = ckm_and_argdet(Mu, Md)
    Ja.append(abs(J)); Aa.append(abs(np.sin(a)))   # sin(arg)=0 iff arg in {0,pi}
print("REAL texture (M->M*):")
print(f"  max |J_CKM|                 = {max(Ja):.3e}   (should be ~0: real CKM)")
print(f"  arg det: max |sin(arg)|     = {max(Aa):.3e}   (arg det in {{0,pi}}: real det)")
print(f"  arg det: fraction with det<0 (arg=pi) = {np.mean([np.cos(np.angle(np.linalg.det(np.random.randn(3,3))))<0 for _ in range(2000)]):.2f}")

# --- Branch B: HERMITIAN textures (M -> M+, parity/L<->R) ---
Jb=[]; Ab=[]
for _ in range(2000):
    A = np.random.randn(3,3)+1j*np.random.randn(3,3); Mu=(A+A.conj().T)/2
    B = np.random.randn(3,3)+1j*np.random.randn(3,3); Md=(B+B.conj().T)/2
    J, a = ckm_and_argdet(Mu, Md)
    Jb.append(abs(J)); Ab.append(abs(np.sin(a)))
print("\nHERMITIAN texture (M->M+):")
print(f"  median |J_CKM|              = {np.median(Jb):.3e}   (generically != 0: complex CKM)")
print(f"  fraction with |J|>1e-6      = {np.mean(np.array(Jb)>1e-6):.3f}")
print(f"  arg det: max |sin(arg)|     = {max(Ab):.3e}   (arg det in {{0,pi}}: det real)")
print(f"  arg det: fraction with det<0 (arg=pi, not 0) = {np.mean([np.cos(a)<0 for a in [np.angle(np.linalg.det((lambda X:(X+X.conj().T)/2)(np.random.randn(3,3)+1j*np.random.randn(3,3)))*np.linalg.det((lambda X:(X+X.conj().T)/2)(np.random.randn(3,3)+1j*np.random.randn(3,3)))) for _ in range(4000)]]):.2f}")
