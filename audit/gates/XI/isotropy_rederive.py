import numpy as np

# Independent re-derivation of the transverse-sound anisotropy of a CENTRAL-FORCE
# cubic solid, to check One Medium's "order 15%" figure without accepting it.
#
# Model: monatomic lattice, central-force (bond-stretching) springs only.
# A central force between atoms separated by unit vector n gives a 3x3
# force-constant matrix Phi = gamma * (n outer n).  (Pure bond-stretching;
# this is the DEFINITION of a central-force solid and it is what enforces the
# Cauchy relation C12 = C44.)
#
# Dynamical matrix: D(k) = (1/m) * sum_bonds gamma*(n n^T) * (1 - cos(k.R))
# Long-wavelength: expand -> D(k) ~ sum_bonds gamma*(n n^T)*( (k.R)^2 / 2 )
# giving an acoustic tensor; eigenvalues = (rho) v^2 along each polarisation.

def acoustic_tensor(khat, neighbors, gamma=1.0, m=1.0):
    # Long-wavelength dynamical matrix coefficient (the "Christoffel"/acoustic tensor)
    # D ~ (1/m) sum gamma (n n^T) (k.R)^2/2 ; factor out |k|^2, set a=1.
    G = np.zeros((3,3))
    for R in neighbors:
        r = np.linalg.norm(R)
        n = R/r
        kdotR = np.dot(khat, R)
        G += gamma*np.outer(n,n)*(kdotR**2)/2.0
    return G/m

def speeds(khat, neighbors):
    G = acoustic_tensor(khat, neighbors)
    w = np.linalg.eigvalsh(G)          # rho v^2 (proportional)
    w = np.sort(w)                     # ascending: two transverse then longitudinal
    return np.sqrt(np.clip(w,0,None))

def build_bcc():
    # BCC nearest neighbours: 8 along <111>/2 ... use conventional: NN at (+-1,+-1,+-1)*0.5*a with a=1
    nn=[]
    for sx in (-1,1):
        for sy in (-1,1):
            for sz in (-1,1):
                nn.append(0.5*np.array([sx,sy,sz]))
    return nn

def build_bcc_nn_nnn():
    nn=build_bcc()
    # next-nearest: 6 along <100> at distance 1
    nnn=[np.array(v,float) for v in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]]
    return nn, nnn

def build_fcc():
    # FCC nearest neighbours: 12 along <110>/... at (+-1,+-1,0)*0.5 and perms
    nn=[]
    base=[(1,1,0),(1,-1,0),(-1,1,0),(-1,-1,0),
          (1,0,1),(1,0,-1),(-1,0,1),(-1,0,-1),
          (0,1,1),(0,1,-1),(0,-1,1),(0,-1,-1)]
    for b in base: nn.append(0.5*np.array(b,float))
    return nn

dirs = {'[100]':np.array([1,0,0.]),
        '[110]':np.array([1,1,0.])/np.sqrt(2),
        '[111]':np.array([1,1,1.])/np.sqrt(3)}

def report(name, neighbors_list, weights=None):
    if weights is None: weights=[1.0]*len(neighbors_list)
    # combine multiple shells with relative stiffness weights
    alln=[]; 
    combined=[]
    for shell,w in zip(neighbors_list,weights):
        for R in shell: combined.append((R,w))
    print(f"\n=== {name} ===")
    # compute speeds per direction with weighted shells
    def G_of(khat):
        G=np.zeros((3,3))
        for R,w in combined:
            r=np.linalg.norm(R); n=R/r; kdotR=np.dot(khat,R)
            G+=w*np.outer(n,n)*(kdotR**2)/2
        return G
    trans=[]
    for d,kh in dirs.items():
        w=np.sort(np.sqrt(np.clip(np.linalg.eigvalsh(G_of(kh)),0,None)))
        print(f"  {d}: v_T1={w[0]:.4f}  v_T2={w[1]:.4f}  v_L={w[2]:.4f}")
        trans+= [w[0],w[1]]
    trans=np.array([t for t in trans if t>1e-9])
    if len(trans):
        spread=(trans.max()-trans.min())/trans.mean()
        print(f"  --> transverse-speed spread (max-min)/mean = {100*spread:.1f}%")
        # also fast/slow ratio
        print(f"  --> transverse fast/slow ratio = {trans.max()/trans.min():.3f}")

report("BCC, NN central force only", [build_bcc()])
nn,nnn=build_bcc_nn_nnn()
report("BCC, NN+NNN central force (equal stiffness)", [nn,nnn],[1.0,1.0])
report("BCC, NN+NNN central force (NNN half stiffness)", [nn,nnn],[1.0,0.5])
report("FCC (=BCT c/a=sqrt2), NN central force only", [build_fcc()])

# Zener anisotropy check for a general cubic central-force solid:
# Cauchy relation C12=C44 (central force). Isotropy needs C11-C12=2C44=2C12 -> C11=3C12.
# Report Zener A=2C44/(C11-C12) for the NN models by extracting C's from acoustic tensor.
def elastic_from_model(combined):
    # C11 from [100] long: rho vL^2 = C11 ; C44 from [100] trans: = C44
    def G_of(khat):
        G=np.zeros((3,3))
        for R,w in combined:
            r=np.linalg.norm(R); n=R/r; kdotR=np.dot(khat,R)
            G+=w*np.outer(n,n)*(kdotR**2)/2
        return G
    kh=np.array([1,0,0.])
    w=np.sort(np.linalg.eigvalsh(G_of(kh)))
    C44=w[0]; C11=w[2]
    kh=np.array([1,1,0.])/np.sqrt(2)
    w2=np.sort(np.linalg.eigvalsh(G_of(kh)))
    # [110] slow transverse (pol [1-10]) = (C11-C12)/2
    C11_C12_over2=w2[0]
    C12=C11-2*C11_C12_over2
    A=2*C44/(C11-C12) if (C11-C12)!=0 else float('inf')
    return C11,C12,C44,A

for label,comb in [("BCC NN",[(R,1.0) for R in build_bcc()]),
                   ("FCC NN",[(R,1.0) for R in build_fcc()])]:
    C11,C12,C44,A=elastic_from_model(comb)
    print(f"\n{label}: C11={C11:.4f} C12={C12:.4f} C44={C44:.4f}  Cauchy(C12=C44)? {abs(C12-C44)<1e-9}  Zener A=2C44/(C11-C12)={A:.3f}")
