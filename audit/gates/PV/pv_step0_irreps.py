"""
GATE PV - Step 0. O_h irrep decomposition of the symmetric rank-2 tensor gauge
field A_{ij}, computed cold from the explicit 48 signed-permutation matrices
(O_h ~ signed permutation matrices in 3D, |O_h| = 3! * 2^3 = 48).

We need two facts:
  (a) A_{ij} (symmetric, 6-dim) decomposes as A1g (+) Eg (+) T2g  [all gerade].
  (b) The Maxwell vector potential A_i transforms as T1u (polar vector).
      Multiplicity of T1u inside Sym^2(vector) must be 0
      -> the tensor gauge field contains NO vector (photon) component.
"""
import itertools, numpy as np

# --- build O_h as signed permutation matrices ---
perms = list(itertools.permutations(range(3)))
signs = list(itertools.product([1,-1], repeat=3))
G = []
for p in perms:
    for s in signs:
        R = np.zeros((3,3))
        for i in range(3):
            R[i, p[i]] = s[i]
        G.append(R)
assert len(G) == 48, len(G)

# --- induced action on symmetric 2-tensors (6-dim basis) ---
# basis order: xx, yy, zz, xy, xz, yz
sym_idx = [(0,0),(1,1),(2,2),(0,1),(0,2),(1,2)]
def sym_rep(R):
    M = np.zeros((6,6))
    for a,(i,j) in enumerate(sym_idx):
        # image of basis tensor e_i (x) e_j symmetrised under R
        for b,(k,l) in enumerate(sym_idx):
            # (R T R^T)_{ij} coefficient of basis b
            val = R[i,k]*R[j,l] + (0 if (i==j) else R[i,l]*R[j,k])
            if k==l:
                M[b,a] += val
            else:
                M[b,a] += val
    return M

# character of vector rep = tr(R);  character of Sym^2 = tr(sym_rep(R))
chi_vec  = np.array([np.trace(R) for R in G])
chi_sym2 = np.array([np.trace(sym_rep(R)) for R in G])

# multiplicity of irrep r in rep X:  (1/|G|) sum_g conj(chi_r(g)) chi_X(g)
def mult(chi_irrep, chi_X):
    return np.round(np.vdot(chi_irrep, chi_X).real / len(G), 6)

# A1g (trivial) character = all 1
chi_A1g = np.ones(48)
# T1u character = character of the polar vector = tr(R)  (this IS T1u for O_h)
chi_T1u = chi_vec

print("mult(A1g in Sym^2 vector) =", mult(chi_A1g, chi_sym2), " (expect 1: the trace/delta_ij part)")
print("mult(T1u in Sym^2 vector) =", mult(chi_T1u, chi_sym2), " (expect 0: NO vector/photon part)")
print("dim(Sym^2 vector)         =", int(round(chi_sym2[0].real)), " (expect 6)")

# Confirm the standard split A1g(1) + Eg(2) + T2g(3): build Eg and T2g characters
# T2g character: the {xy,xz,yz} sector transforms as T2g; its character = tr on that 3-dim block.
# Easier: <chi_sym2,chi_sym2> tells us sum of squared multiplicities.
norm = np.round(np.vdot(chi_sym2, chi_sym2).real/len(G),6)
print("<chi_sym2,chi_sym2>       =", norm, " (=1^2+1^2+1^2=3 for three distinct irreps A1g,Eg,T2g)")
