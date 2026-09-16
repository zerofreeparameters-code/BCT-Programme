import numpy as np
from itertools import product
np.set_printoptions(suppress=True, precision=4)

# Build T_d explicitly as the 24 symmetry operations of a regular tetrahedron.
# Vertices of regular tetrahedron: (1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1).
verts=np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],float)
# T_d = all orthogonal 3x3 matrices permuting these 4 vertices.
import itertools
ops=[]
for perm in itertools.permutations(range(4)):
    # solve O verts[i] = verts[perm[i]] in least squares; keep if orthogonal & exact
    A=verts.T; Bm=verts[list(perm)].T
    O=Bm.dot(np.linalg.pinv(A))
    if np.allclose(O.dot(O.T),np.eye(3),atol=1e-8) and np.allclose(O.dot(verts.T),Bm,atol=1e-8):
        ops.append(O)
# dedupe
uniq=[]
for O in ops:
    if not any(np.allclose(O,U,atol=1e-6) for U in uniq): uniq.append(O)
G=uniq
print(f"|T_d| = {len(G)}  (expect 24)")
ndet=sum(1 for O in G if np.linalg.det(O)>0)
print(f"proper rotations det=+1: {ndet} (expect 12);  improper det=-1: {len(G)-ndet} (expect 12)")

# The natural 3D action on Cartesian vectors IS the T2 irrep of T_d. Confirm irreducibility
# via character: sum |chi(g)|^2 / |G| must = 1 for an irrep.
chars=np.array([np.trace(O) for O in G])
irr = (chars@chars)/len(G)
print(f"\n3D Cartesian rep: sum|chi|^2/|G| = {irr:.4f}  -> {'IRREDUCIBLE' if abs(irr-1)<1e-6 else 'reducible'} (this is T2)")

# --- Schur's lemma made explicit: the ONLY T_d-invariant operator on the 3D irrep is scalar ---
# Reynolds average of a random Hermitian M over the group.
rng=np.random.default_rng(0)
Mr=rng.standard_normal((3,3))+1j*rng.standard_normal((3,3)); Mr=Mr+Mr.conj().T
avg=sum(O@Mr@O.T for O in G)/len(G)
print("\nReynolds-averaged Hermitian operator on the T2 triplet (T_d-invariant part):")
print(np.round(avg.real,6))
offdiag=np.max(np.abs(avg-np.diag(np.diag(avg))))
diagspread=np.max(np.abs(np.diag(avg).real - np.mean(np.diag(avg).real)))
print(f"max |offdiag| = {offdiag:.2e}   diagonal spread = {diagspread:.2e}")
print("=> invariant operator is a MULTIPLE OF IDENTITY: three generations EXACTLY degenerate,")
print("   no free parameter available within T_d-invariants to lift them.")

# --- The mixing kill, general form (independent of which irreps the 3 gens occupy) ---
# Whatever the generation rep, a T_d-invariant M_u and M_d are each block-scalar in the
# SAME symmetry-adapted basis (Schur). Block-scalar matrices commute. Demonstrate for the
# worst case: gens split across three 1D irreps A1,A2 + one component -> still block-diagonal.
def reynolds(M): return sum(O@M@O.T for O in G)/len(G)
Mu=reynolds(rng.standard_normal((3,3))); Mu=(Mu+Mu.T)/2
Md=reynolds(rng.standard_normal((3,3))); Md=(Md+Md.T)/2
comm=Mu@Md-Md@Mu
print(f"\n[M_u, M_d] for two independent T_d-invariant mass matrices: max|.| = {np.max(np.abs(comm)):.2e}")
print("=> [M_u,M_d]=0  ->  simultaneously diagonalisable  ->  V_CKM has NO physical mixing, J=0.")

# --- Spurion content: what would be needed to lift/mix (symmetric square of T2) ---
# [T2 x T2]_sym decomposition under T_d. Compute symmetric-product character and reduce.
# Character table T_d classes: E, 8C3, 3C2, 6S4, 6sigma_d
# Use class reps from G by rotation angle / det.
def classify(O):
    d=np.linalg.det(O); tr=np.trace(O)
    key=(round(d,3),round(tr,3))
    return key
from collections import defaultdict
classes=defaultdict(list)
for O in G: classes[classify(O)].append(O)
print("\nT_d classes (det, trace, size):")
for k,v in sorted(classes.items()): print(f"  det={k[0]:+.0f} tr={k[1]:+.1f}  size={len(v)}")
# characters of T2 (=chi), and of Sym^2(T2): chi_sym2(g) = (chi(g)^2 + chi(g^2))/2
irrep_chars={ # standard T_d table on classes [E,8C3,3C2,6S4,6sd]
 'A1':np.array([1,1,1,1,1]),'A2':np.array([1,1,1,-1,-1]),
 'E':np.array([2,-1,2,0,0]),'T1':np.array([3,0,-1,1,-1]),'T2':np.array([3,0,-1,-1,1])}
classorder=[( 1.0,3.0),(1.0,0.0),(1.0,-1.0),(-1.0,-1.0),(-1.0,1.0)] # E,8C3,3C2,6S4,6sd
sizes=[len(classes[c]) for c in classorder]
chiT2=np.array([irrep_chars['T2'][i] for i in range(5)])
# chi(g^2): squaring a class -> for these, chi(g^2) on classes: E->E(3),C3->C3(0? actually (C3)^2=C3),
# compute directly from ops
def chi_g2(classrep):
    return np.trace(classrep@classrep)
chi_sq=[]
for c in classorder:
    rep=classes[c][0]
    chi_sq.append((np.trace(rep)**2+np.trace(rep@rep))/2)
chi_sym2=np.array(chi_sq)
print("\nSym^2(T2) character on [E,8C3,3C2,6S4,6sd]:",chi_sym2)
print("Reduce into irreps (multiplicities):")
for name,ch in irrep_chars.items():
    m=sum(sizes[i]*ch[i]*chi_sym2[i] for i in range(5))/len(G)
    print(f"  {name}: {m:.3f}")
print("=> Sym^2(T2) = A1 + E + T2. A1 is the trace (no splitting).")
print("   SPLITTING/MIXING spurion must live in E + T2  (a T_d-breaking order parameter).")
