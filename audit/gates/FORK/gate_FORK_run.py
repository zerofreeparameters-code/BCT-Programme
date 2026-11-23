#!/usr/bin/env python3
"""
Gate FORK -- run script (gate_FORK_run.py)

Pre-registration : audit/gates/gate_FORK_prompt.md
                   SHA-256 c21bc5d6a6c13b25016c6835966adf86d8bdb330b4cc5fb9c082a4947fc59e09
                   (audit/gates/PREREG_20261011.sha256; checked with `sha256sum -c` before the prompt was read)
Checkout         : zerofreeparameters-code/BCT-Programme @ bc5c87dc2f5b978d014d0da876bd718c3f20aada

Usage            : python3 -I gate_FORK_run.py --repo <checkout> --prompt <downloaded prompt> --out <dir>

EXPLICIT SOURCING
 S1  J1-J5 copied byte-for-byte from audit/gates/PRED/scripts/pred_step2_nullmodel.py at the commit above:
       judgement text  = docstring lines 5-16  -> PRED_J_TEXT below
       implementation  = code lines 18-77      -> the VERBATIM CODE block below (atoms, unary, clean, binary,
                         L1..L3r, target dict T, names/tv, Nmenu, hit_stats).
     At run time the script re-reads that file from --repo and asserts byte identity of both slices; the
     SHA-256 of each slice is hard-coded below and written into the result.
 S2  Forks, branches, enumeration rules, targets, scoring, verdicts, sensitivity: gate_FORK_prompt.md sec. 2-6.
 S3  Geometry: computed here in mpmath at 60 dps (40 reported). Closed forms are used ONLY as cross-checks
     (sec. 7), never as inputs. Void radii come from exhaustive nearest-lattice-point search.
 S4  Comparison value for 1/alpha in the F6xF7 sweep: 137.035999, the PRED J4 value (sec. 4 H_alpha).

FORK JUDGEMENT CALLS -- fixed in this file before any branch alphabet was scored
 K1  Primary scoring configuration = PRED J1-J3 as listed in prompt sec. 2 ("unary menu as in ... J1-J3"):
     3-atom bound, correction layer (J3) ON, all PRED J4 targets, tolerances 1% (C) and 0.1% (C0.1).
     The J3 layer uses the branch's own alpha0 (the atom it replaces).
 K2  "Scored alphabet" = distinct (atom set, target vector). Rows whose atom set and targets are identical
     at 40 dps (e.g. every F7 branch, HCP) are one scored alphabet; the map records every such identity.
     Reported convention sensitivity (does not enter the verdict): no de-duplication.
 K3  Percentile of * = scipy.stats.percentileofscore default (kind='rank', average rank of ties), * included
     in the reference array. 'strict', 'weak' and 'mean' are reported alongside.
     "Central 80%" = 10 <= PR <= 90 ; "at or above the 95th percentile" = PR >= 95.
 K4  F2 continuum (c/a = 1.00 ... 2.00 step 0.01) is scored for plotting and is NOT in the one-step
     reference set (prompt: "about 200" scored alphabets; continuum is "so the scored quantities can be
     plotted"). Reported convention sensitivity: continuum included.
 K5  F2 shell crossings: every c/a in [sqrt(2/3), 2] (the span of the named points) at which two distinct
     BCT lattice-vector classes of length <= 2a become degenerate. 2a is the smallest bound that recovers all
     five named points (sqrt(3) and 2 are crossings at exactly 2a). Exact rational arithmetic.
 K6  F2 voids at general c/a: the BCT sites continuous with the * octahedral and tetrahedral voids, i.e. the
     parameter-free I4/mmm Wyckoff sites 2b (1/2,1/2,0) and 4d (0,1/2,1/4). Their circumradii are found by
     exhaustive nearest-lattice-point search at 60 dps; D is the numerically found nearest-neighbour
     distance. A Delaunay/Voronoi pass (float) records which Voronoi-vertex classes exist at each named c/a.
 K7  F4 alternative radii use the hole polyhedron whose vertices are the atom centres at the void's
     circumradius: polyhedron circumradius, polyhedron inradius (centre-to-face), and their mean.
 K8  F1xF3 units per lattice: R = D/2; D; a_cubic = conventional cubic edge (n/a for HCP); c = c-axis of the
     conventional cell (= a_cubic for cubic lattices; sqrt(8/3) D for HCP); oct/tet void diameter = 2 rho of the
     first/second void (tet n/a for one-void lattices); r_WS from the volume per lattice point in the
     lattice's own dimension. RCP is "noted, not scored separately" (prompt F1).
 K9  Sensitivity (d) "tolerance 0.5%" replaces the 1% tolerance (C -> C0.5); C0.1 is defined at 0.1% and is
     unchanged. Sensitivity (c) restricts targets to the eleven headline targets, mapped to PRED keys.
 K10 SC-FORK-0 trigger: any sensitivity variant (a)-(d) changes the verdict set, or changes *'s membership of
     the central band [10,90] or the top band [95,100] on C or C0.1, or F2/F4 numerics fail to close.
 K11 L_alpha primary threshold = H_alpha(*) itself (prompt: "within 0.013% ... (the taken path's own
     error)"), inclusive; the literal 1.3e-4 is reported alongside.
 K12 SC-FORK-3 "exclusive hits of its own" = the sec. 4 definition for untaken branches (targets the branch
     reaches at 0.1% that * does not). The "<5% of scored alphabets" version is reported alongside.
 K13 Alternative F2 reading, reported only: voids = Voronoi-vertex classes (Delaunay circumcentres re-solved at
     60 dps); the two deepest enter, one class -> one void. K6 stays primary because it keeps F5 held at *
     (the octahedral and tetrahedral voids enter) while c/a moves; at c/a = 1 the Voronoi reading has only the
     tetrahedral class, contradicting F1's two-void BCC.
"""
# >>>>> BEGIN VERBATIM J-TEXT: pred_step2_nullmodel.py lines 5-16 >>>>>
PRED_J_TEXT = r'''
JUDGEMENT CALLS (stated per gate §'A note on care'):
 J1 Alphabet = atoms actually observed in the corpus's printed formulas (Step 1):
    integers {1,2,3,4,5,6,8,9,12}, pi, sqrt2, sqrt3, sqrt6, r_oct, r_tet, alpha0, S_D4=pi^5/6.
 J2 Complexity bound = <=3 atoms, <=2 binary ops, <=1 unary op at a leaf and <=1 at the root.
    This matches every core formula in the recomputed set (e.g. (1-5a0)/pi has 3 atoms, 2 ops).
 J3 Correction layer = optional factor (1+N*alpha0) with N drawn from the corpus's own printed
    'N-class' menu.  Reported both with and without the layer.
 J4 Targets: fixed BEFORE enumeration (list below), dimensionless, PDG/CODATA/Planck 2018-2024
    central values as quoted in the corpus or standard.  The corpus's hadron sector uses Lambda=220 MeV
    as a chosen anchor; hadron targets are therefore ratios to that anchor and to m_pi0.
 J5 Tolerance: 1% (the corpus's headline 'sub-1%') and 0.1% (its 'sub-0.1%' tier).
Sensitivity to J1-J5 is reported in the deliverable.
'''
# <<<<< END VERBATIM J-TEXT <<<<<
# >>>>> BEGIN VERBATIM CODE: pred_step2_nullmodel.py lines 18-77 >>>>>
import numpy as np, itertools, math, sys
pi=math.pi; s2=math.sqrt(2); s3=math.sqrt(3); s6=math.sqrt(6)
roct=(s2-1)/2; rtet=(s6-2)/4; a0=roct*rtet/pi; SD4=pi**5/6
atoms={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'8':8,'9':9,'12':12,'pi':pi,'sqrt2':s2,'sqrt3':s3,'sqrt6':s6,
       'roct':roct,'rtet':rtet,'a0':a0,'SD4':SD4}
A=np.array(list(atoms.values()))
def unary(v):
    out=[v, np.sqrt(v), np.cbrt(v), v**2, 1/v]
    with np.errstate(all='ignore'):
        out.append(np.exp(-v)); out.append(np.log(np.abs(v)))
    return np.concatenate(out)
def clean(v):
    v=v[np.isfinite(v)]; v=v[(np.abs(v)>1e-6)&(np.abs(v)<1e6)]
    return np.unique(np.round(v,10))
L1=clean(unary(A))                      # 1 atom
def binary(X,Y):
    x=X[:,None]; y=Y[None,:]
    with np.errstate(all='ignore'):
        r=np.concatenate([(x+y).ravel(),(x-y).ravel(),(x*y).ravel(),(x/y).ravel()])
    return r
L2=clean(binary(L1,L1))                  # 2 atoms (unary at leaves)
L2r=clean(np.concatenate([L2,np.sqrt(np.abs(L2)),1/L2,L2**2]))  # root unary
L3=clean(binary(L2,L1))                  # 3 atoms
L3r=clean(np.concatenate([L3,np.sqrt(np.abs(L3)),1/L3]))
print(f"distinct values: 1-atom {len(L1)}, 2-atom {len(L2r)}, 3-atom {len(L3r)}")
# ---- fixed target list (dimensionless), set before running ----
Lam=220.0; mpi0=134.9768
T={ '1/alpha':137.035999, 'sin2thW(MSbar,mZ)':0.23122, 'sin2th12':0.307, 'sin2th13':0.02203,
    'sin2th23':0.57, 'n_s':0.9649, 'alpha_s(mZ)':0.1180, 'Omega_L':0.685, 'Y_p':0.245,
    'm_p/m_e':1836.153, 'm_mu/m_e':206.768, 'm_tau/m_mu':16.817, 'Koide_Q':0.666661,
    'm_rho/m_pi0':775.26/mpi0, 'm_K/m_pi0':493.677/mpi0, 'm_eta/m_pi0':547.862/mpi0,
    "m_eta'/m_pi0":957.78/mpi0, 'm_omega/m_rho':782.66/775.26, 'm_K*/m_rho':891.67/775.26,
    'm_phi/m_rho':1019.461/775.26, 'm_p/m_rho':938.272/775.26, 'm_n/m_p':939.565/938.272,
    'm_Delta/m_p':1232/938.272, 'm_p/Lam':938.272/Lam, 'm_rho/Lam':775.26/Lam, 'T_c/Lam':156.5/Lam,
    'r_p*m_rho/hbarc':0.84075*775.26/197.327, 'r_pi*m_rho/hbarc':0.659*775.26/197.327,
    'm_b/m_t':4.183/172.57, 'm_c/m_t':1.273/172.57, 'm_s/m_c':0.0935/1.273, 'm_d/m_u':4.70/2.16,
    'm_s/m_d':93.5/4.70, 'm_H/v':125.2/246.22, 'm_t/v':172.57/246.22, 'm_W/m_Z':80.369/91.188,
    'g_A':1.2754, 'mu_p':2.79285, 'V_us':0.2245, 'V_cb':0.0410, 'V_ub':0.00382,
    'ln(mP/me)':math.log(1.220890e22/0.51099895), 'ln(mP/mp)':math.log(1.220890e22/938.272),
    'ln(mP/v)':math.log(1.220890e22/246220), 'ln(mP/Lam)':math.log(1.220890e22/Lam),
    'sigma8':0.811, 'H0/100':0.674, 'Omega_m':0.315 }
names=list(T); tv=np.array([T[k] for k in names])
print(f"targets fixed: {len(tv)}")
Nmenu=[3/8,3/4,1,3/2,2,9/4,3,4,5,6,8,9]; Nmenu=sorted(set(Nmenu+[-n for n in Nmenu]))
def hit_stats(vals, tol, with_N=False):
    """fraction of distinct |values| within tol of ANY target (interval union via searchsorted); per-target coverage"""
    v=np.sort(np.abs(vals))
    facs=[1+n*a0 for n in Nmenu]+[1.0] if with_N else [1.0]
    ints=[]; covered=np.zeros(len(tv),bool)
    for j,t in enumerate(tv):
        for f in facs:
            lo,hi=t/f*(1-tol), t/f*(1+tol)
            ints.append((lo,hi))
            if np.searchsorted(v,hi,'right')-np.searchsorted(v,lo,'left')>0: covered[j]=True
    ints.sort(); merged=[]
    for lo,hi in ints:
        if merged and lo<=merged[-1][1]: merged[-1][1]=max(merged[-1][1],hi)
        else: merged.append([lo,hi])
    n=sum(np.searchsorted(v,hi,'right')-np.searchsorted(v,lo,'left') for lo,hi in merged)
    return n/len(v), covered
# <<<<< END VERBATIM CODE <<<<<

# ============================================================================================
# FORK LAYER  (everything below is new code for Gate FORK; the block above is PRED's, verbatim)
# ============================================================================================
import os, re, csv, json, hashlib, subprocess, argparse, time, resource, itertools as _it
from fractions import Fraction
import mpmath as mpm
import scipy, scipy.stats
from scipy.spatial import Delaunay

mpm.mp.dps = 60
REP = 40                      # reported significant digits
KEYDIG = 35                   # digits used to decide alphabet identity (K2)
PIN_COMMIT = 'bc5c87dc2f5b978d014d0da876bd718c3f20aada'
PROMPT_REL = 'audit/gates/gate_FORK_prompt.md'
PROMPT_SHA256 = 'c21bc5d6a6c13b25016c6835966adf86d8bdb330b4cc5fb9c082a4947fc59e09'
PRED_REL = 'audit/gates/PRED/scripts/pred_step2_nullmodel.py'
PRED_FILE_SHA256 = 'e8ddc17136a521ed5f8e015cc1587fbeccd16521bedab3a004bc06b341aabc82'
PRED_J_SHA256 = '9536c70969886038d7e0b3ab20fedbf96a486d847961474a7dd592708cdadd9f'      # lines 5-16
PRED_CODE_SHA256 = 'aff0ef8a9e654d63e2347c83e711e0a31592584e2cfad363726ba9f6e4495c9c'   # lines 18-77
INV_ALPHA_OBS = mpm.mpf('137.035999')                                                    # PRED J4 value

# keep PRED's own * objects from the verbatim block, then free the big intermediate
ATOMS_PRED = dict(atoms)
STAR_PRED_L2r, STAR_PRED_L3r = L2r, L3r
TV_PRED = tv.copy(); NAMES = list(names)
del L3

LOG = []
def log(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); LOG.append(s)

def S(x, n=REP):
    if x is None: return ''
    return mpm.nstr(mpm.mpf(x), n, strip_zeros=False)

def sha256_bytes(b): return hashlib.sha256(b).hexdigest()
def sha256_file(p):
    with open(p, 'rb') as f: return sha256_bytes(f.read())

# --------------------------------------------------------------------------------------------
# 0. provenance and byte-for-byte verification of the verbatim block
# --------------------------------------------------------------------------------------------
def verify_verbatim(repo):
    me = open(os.path.abspath(__file__), 'rb').read().splitlines(keepends=True)
    def between(start, end):
        i = next(k for k, l in enumerate(me) if l.startswith(start))
        j = next(k for k, l in enumerate(me) if k > i and l.startswith(end))
        return b''.join(me[i + 1:j])
    jtext = between(b"PRED_J_TEXT = r'''", b"'''")
    code = between(b'# >>>>> BEGIN VERBATIM CODE', b'# <<<<< END VERBATIM CODE')
    out = dict(j_sha=sha256_bytes(jtext), code_sha=sha256_bytes(code))
    out['j_ok_hardcoded'] = out['j_sha'] == PRED_J_SHA256
    out['code_ok_hardcoded'] = out['code_sha'] == PRED_CODE_SHA256
    pp = os.path.join(repo, PRED_REL)
    if os.path.exists(pp):
        pl = open(pp, 'rb').read().splitlines(keepends=True)
        out['pred_file_sha'] = sha256_file(pp)
        out['j_ok_live'] = b''.join(pl[4:16]) == jtext
        out['code_ok_live'] = b''.join(pl[17:77]) == code
    if not (out['j_ok_hardcoded'] and out['code_ok_hardcoded'] and out.get('j_ok_live', True) and out.get('code_ok_live', True)):
        raise SystemExit('HALT: verbatim J1-J5 block is not byte-identical to PRED source')
    return out

def provenance(repo, prompt_dl):
    head = subprocess.run(['git', '-C', repo, 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()
    p_repo = sha256_file(os.path.join(repo, PROMPT_REL))
    p_dl = sha256_file(prompt_dl) if prompt_dl else None
    if head != PIN_COMMIT: raise SystemExit(f'HALT: checkout {head} != pinned {PIN_COMMIT}')
    if p_repo != PROMPT_SHA256 or (p_dl is not None and p_dl != PROMPT_SHA256):
        raise SystemExit('HALT: prompt SHA-256 mismatch')
    return dict(commit=head, prompt_sha256_repo=p_repo, prompt_sha256_downloaded=p_dl,
                numpy=np.__version__, mpmath=mpm.__version__, scipy=scipy.__version__,
                python=sys.version.split()[0])

# --------------------------------------------------------------------------------------------
# 1. geometry (mpmath, 60 dps). Closed forms appear ONLY in cross_checks().
# --------------------------------------------------------------------------------------------
H = mpm.mpf(1) / 2
TINY = mpm.mpf(10) ** -50

def d2(p, q): return mpm.fsum([(a - b) ** 2 for a, b in zip(p, q)])

def nearest(site, pts):
    """distance from site to nearest lattice point (excluding coincident) and the number of points at it"""
    ds = sorted(x for x in (d2(site, p) for p in pts) if x > TINY)
    m = ds[0]; coord = sum(1 for x in ds if x - m < mpm.mpf(10) ** -45 * max(1, m))
    return mpm.sqrt(m), coord, [p for p in pts if abs(d2(site, p) - m) < mpm.mpf(10) ** -45 * max(1, m)]

def bct_points(r, n=3):
    pts = []
    for i, j, k in _it.product(range(-n, n + 1), repeat=3):
        pts.append((mpm.mpf(i), mpm.mpf(j), k * r))
        pts.append((i + H, j + H, (k + H) * r))
    return pts

def bct_voids(r):
    pts = bct_points(r)
    D, zD, _ = nearest((0, 0, 0), pts)
    c2b, z2b, n2b = nearest((H, H, 0), pts)
    c4d, z4d, n4d = nearest((0, H, r / 4), pts)
    ra = (c2b - D / 2) / D; rb = (c4d - D / 2) / D
    zero_a = abs(ra) < TINY; zero_b = abs(rb) < TINY
    if zero_a: ra = mpm.mpf(0)
    if zero_b: rb = mpm.mpf(0)
    return dict(D=D, coordD=zD, circ_a=c2b, coord_a=z2b, circ_b=c4d, coord_b=z4d, r_a=ra, r_b=rb,
                zero_a=zero_a, zero_b=zero_b, V=r / 2, verts_a=n2b, verts_b=n4d, site_a=(H, H, 0), site_b=(0, H, r / 4))

def fcc_cubic_voids():          # FCC in its cubic cell (= FCT at c/a = 1): literal reading of sec. 7
    basis = [(0, 0, 0), (H, H, 0), (H, 0, H), (0, H, H)]
    pts = [(i + b[0], j + b[1], k + b[2]) for i, j, k in _it.product(range(-2, 3), repeat=3) for b in basis]
    pts = [tuple(mpm.mpf(x) for x in p) for p in pts]
    D, _, _ = nearest((0, 0, 0), pts)
    co, zo, _ = nearest((H, H, H), pts); q = mpm.mpf(1) / 4
    ct, zt, _ = nearest((q, q, q), pts)
    return dict(D=D, r_a=(co - D / 2) / D, r_b=(ct - D / 2) / D, coord_a=zo, coord_b=zt)

def sc_voids():
    pts = [tuple(mpm.mpf(x) for x in p) for p in _it.product(range(-2, 3), repeat=3)]
    D, zD, _ = nearest((0, 0, 0), pts); c, z, _ = nearest((H, H, H), pts)
    return dict(D=D, coordD=zD, r_a=(c - D / 2) / D, coord_a=z, V=mpm.mpf(1))

def diamond_voids():
    q = mpm.mpf(1) / 4
    fcc = [(0, 0, 0), (H, H, 0), (H, 0, H), (0, H, H)]
    basis = fcc + [(b[0] + q, b[1] + q, b[2] + q) for b in fcc]
    pts = [(mpm.mpf(i + b[0]), mpm.mpf(j + b[1]), mpm.mpf(k + b[2])) for i, j, k in _it.product(range(-2, 3), repeat=3) for b in basis]
    D, zD, _ = nearest((0, 0, 0), pts); c, z, _ = nearest((H, H, H), pts)
    c2, z2, _ = nearest((3 * q, 3 * q, 3 * q), pts)
    return dict(D=D, coordD=zD, r_a=(c - D / 2) / D, coord_a=z, r_a_check=(c2 - D / 2) / D, V=mpm.mpf(1) / 8)

def hcp_voids():
    c = mpm.sqrt(mpm.mpf(8) / 3); s3 = mpm.sqrt(3)
    a1 = (mpm.mpf(1), mpm.mpf(0)); a2 = (H, s3 / 2)
    pts = []
    for i, j, k in _it.product(range(-3, 4), range(-3, 4), range(-2, 3)):
        x = i * a1[0] + j * a2[0]; y = i * a1[1] + j * a2[1]
        pts.append((x, y, k * c)); pts.append((x + H, y + s3 / 6, (k + H) * c))
    D, zD, _ = nearest((0, 0, 0), pts)
    co, zo, _ = nearest((mpm.mpf(1), s3 / 3, c / 4), pts)
    ct, zt, _ = nearest((0, 0, 3 * c / 8), pts)
    return dict(D=D, coordD=zD, r_a=(co - D / 2) / D, coord_a=zo, r_b=(ct - D / 2) / D, coord_b=zt,
                c_axis=c, V=(s3 / 2) * c / 2)

def hex2d_voids():
    s3 = mpm.sqrt(3)
    pts = [(i + j * H, j * s3 / 2) for i, j in _it.product(range(-3, 4), repeat=2)]
    pts = [tuple(mpm.mpf(x) for x in p) for p in pts]
    D, zD, _ = nearest((0, 0), pts); c, z, _ = nearest((H, s3 / 6), pts)
    return dict(D=D, coordD=zD, r_a=(c - D / 2) / D, coord_a=z, V=s3 / 2)

def d4_voids():
    pts = [tuple(mpm.mpf(x) for x in p) for p in _it.product(range(-2, 3), repeat=4) if sum(p) % 2 == 0]
    D, zD, _ = nearest((0, 0, 0, 0), pts)
    c1, z1, _ = nearest((1, 0, 0, 0), pts)
    c2, z2, _ = nearest((H, H, H, H), pts)
    c3, z3, _ = nearest((H, H, H, -H), pts)
    basis = mpm.matrix([[1, 1, 0, 0], [1, -1, 0, 0], [0, 1, -1, 0], [0, 0, 1, -1]])
    V = abs(mpm.det(basis))
    return dict(D=D, coordD=zD, r_a=(c1 - D / 2) / D, coord_a=z1, r_b=(c2 - D / 2) / D, coord_b=z2,
                r_c=(c3 - D / 2) / D, coord_c=z3, V=V)

def polyhedron_radii(site, verts):
    """circumradius and inradius (centre to nearest face plane) of the hole polyhedron with vertices verts"""
    circ = mpm.sqrt(d2(site, verts[0]))
    e2 = min(d2(p, q) for p, q in _it.combinations(verts, 2))
    tol = mpm.mpf(10) ** -40
    faces = [f for f in _it.combinations(verts, 3) if all(abs(d2(p, q) - e2) < tol for p, q in _it.combinations(f, 2))]
    def plane_dist(f):
        u = [f[1][i] - f[0][i] for i in range(3)]; v = [f[2][i] - f[0][i] for i in range(3)]
        n = (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])
        w = [site[i] - f[0][i] for i in range(3)]
        return abs(mpm.fsum([n[i] * w[i] for i in range(3)])) / mpm.sqrt(mpm.fsum([x * x for x in n]))
    inr = min(plane_dist(f) for f in faces)
    return circ, inr, len(faces), len(verts)

def ws_radius(V, dim):
    if dim == 3: return (3 * V / (4 * mpm.pi)) ** (mpm.mpf(1) / 3)
    if dim == 4: return (2 * V / mpm.pi ** 2) ** (mpm.mpf(1) / 4)
    if dim == 2: return mpm.sqrt(V / mpm.pi)

def shell_crossings(lo2=Fraction(2, 3), hi2=Fraction(4), dmax2=Fraction(4)):
    """K5: c/a values in [sqrt(2/3),2] where two distinct BCT vector classes of length <= 2a coincide."""
    cl = set()
    hv = [Fraction(k, 2) for k in range(-8, 9)]
    for x, y, z in _it.product(hv, repeat=3):
        integer = all(v.denominator == 1 for v in (x, y, z)); half = all(v.denominator == 2 for v in (x, y, z))
        if (integer or half) and (x, y, z) != (0, 0, 0):
            cl.add((x * x + y * y, z * z))
    cross = {}
    for (p1, q1), (p2, q2) in _it.combinations(sorted(cl), 2):
        if q1 == q2: continue
        r2 = (p2 - p1) / (q1 - q2)
        if r2 < lo2 or r2 > hi2: continue
        dd = p1 + r2 * q1
        if dd > dmax2: continue
        cross.setdefault(r2, []).append(((p1, q1), (p2, q2), dd))
    return cross

def ca_label(r2):
    if r2.denominator == 1 and int(mpm.sqrt(r2.numerator)) ** 2 == r2.numerator: return str(int(mpm.sqrt(r2.numerator)))
    return f'sqrt({r2})'

def delaunay_classes(r, with_reps=False):
    """Voronoi-vertex (Delaunay circumcentre) classes of BCT at c/a=r inside one cell (float pass; QJ joggle).
    Returns (rho/D rounded, simplices, of which circumcentre inside simplex, distinct sites in cell)."""
    try:
        pts = []
        for i, j, k in _it.product(range(-3, 4), repeat=3):
            pts.append((i, j, k)); pts.append((i + .5, j + .5, k + .5))
        P = np.array(pts, float) * [1, 1, float(r)]
        tri = Delaunay(P, qhull_options='QJ Qbb Qc')
        D = float(bct_voids(r)['D'])
        cls = {}
        for s in tri.simplices:
            V = P[s]; A = 2 * (V[1:] - V[0]); b = (V[1:] ** 2).sum(1) - (V[0] ** 2).sum()
            try: cc = np.linalg.solve(A, b)
            except np.linalg.LinAlgError: continue
            if not (0 <= cc[0] < 1 and 0 <= cc[1] < 1 and 0 <= cc[2] < float(r)): continue
            rad = np.sqrt(((V - cc) ** 2).sum(1)).max()
            T = np.vstack([V.T, np.ones(4)]); lam = np.linalg.solve(T, np.append(cc, 1))
            key = round(rad / D - .5, 6)
            e = cls.setdefault(key, [0, 0, set(), s])
            e[0] += 1; e[1] += int(lam.min() >= -1e-9)
            e[2].add(tuple(np.round(np.mod(cc / [1, 1, float(r)], 1.0), 3) % 1.0))
        res = sorted((k, v[0], v[1], len(v[2])) for k, v in cls.items())
        if with_reps: return res, {k: [pts[i] for i in v[3]] for k, v in cls.items()}
        return res
    except Exception as ex:
        return f'Delaunay failed: {ex}'

def vv_voids(r):
    """Alternative F2 reading (reported only): voids = Voronoi-vertex classes, each circumcentre re-solved at 60 dps
    from its Delaunay simplex and confirmed as a Voronoi vertex by exhaustive nearest-point search."""
    res, reps = delaunay_classes(r, with_reps=True)
    pts = bct_points(r); D, _, _ = nearest((0, 0, 0), pts)
    out = []
    for k, n, nin, nsite in res:
        V = [(mpm.mpf(p[0]), mpm.mpf(p[1]), mpm.mpf(p[2]) * r) for p in reps[k]]
        A = mpm.matrix([[2 * (V[i][j] - V[0][j]) for j in range(3)] for i in range(1, 4)])
        b = mpm.matrix([mpm.fsum([V[i][j] ** 2 - V[0][j] ** 2 for j in range(3)]) for i in range(1, 4)])
        x = mpm.lu_solve(A, b); cc = (x[0], x[1], x[2])
        rad = mpm.sqrt(d2(cc, V[0])); nn, coord, _ = nearest(cc, pts)
        out.append(dict(rho=(rad - D / 2) / D, nsite=nsite, local_max=(nin == n), coord=coord, vertex_ok=abs(nn - rad) < mpm.mpf(10) ** -45))
    out.sort(key=lambda d: -d['rho'])
    return out

def cross_checks():
    """sec. 7: must reproduce closed forms to 40 dps or the run halts."""
    s2, s3, s5, s6 = (mpm.sqrt(x) for x in (2, 3, 5, 6))
    tol = mpm.mpf(10) ** -REP
    res = []
    def chk(name, val, ref):
        ok = abs(val - ref) <= tol * abs(ref); res.append((name, S(val), S(ref), ok)); return ok
    v = bct_voids(s2); f = fcc_cubic_voids(); b = bct_voids(mpm.mpf(1))
    ok = all([chk('BCT c/a=sqrt2  r_oct (2b)', v['r_a'], (s2 - 1) / 2), chk('BCT c/a=sqrt2  r_tet (4d)', v['r_b'], (s6 - 2) / 4),
              chk('FCC cubic cell (FCT c/a=1) r_oct', f['r_a'], (s2 - 1) / 2), chk('FCC cubic cell (FCT c/a=1) r_tet', f['r_b'], (s6 - 2) / 4),
              chk('BCT c/a=1 (BCC) r_oct (2b)', b['r_a'], (2 - s3) / (2 * s3)), chk('BCT c/a=1 (BCC) r_tet (4d)', b['r_b'], (s5 - s3) / (2 * s3))])
    if not ok: raise SystemExit('HALT: sec. 7 cross-check failed\n' + '\n'.join(map(str, res)))
    return res

def closure_checks(named_r):
    """F2/F4 closure: numerics vs piecewise closed form, and 60 vs 80 dps stability, all at 40 digits."""
    out = []; tol = mpm.mpf(10) ** -REP; okall = True
    for lab, r2 in named_r:
        r = mpm.sqrt(mpm.mpf(r2.numerator) / r2.denominator)
        v = bct_voids(r)
        D_cf = min(mpm.sqrt(H + r ** 2 / 4), mpm.mpf(1), r)
        ra_cf = (min(1 / mpm.sqrt(2), r / 2) - D_cf / 2) / D_cf
        rb_cf = (mpm.sqrt(mpm.mpf(1) / 4 + r ** 2 / 16) - D_cf / 2) / D_cf
        with mpm.workdps(80):
            v80 = bct_voids(mpm.sqrt(mpm.mpf(r2.numerator) / r2.denominator))
        ok = all(abs(x - y) <= tol * max(abs(y), 1) for x, y in ((v['r_a'], ra_cf), (v['r_b'], rb_cf), (v['r_a'], v80['r_a']), (v['r_b'], v80['r_b'])))
        okall &= ok; out.append((lab, ok))
    return out, okall

# --------------------------------------------------------------------------------------------
# 2. branch rows
# --------------------------------------------------------------------------------------------
FIXED_MP = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '8': 8, '9': 9, '12': 12, 'pi': mpm.pi, 'sqrt2': mpm.sqrt(2),
            'sqrt3': mpm.sqrt(3), 'sqrt6': mpm.sqrt(6), 'SD4': mpm.pi ** 5 / 6}
ANCHORS = [('220MeV', mpm.mpf(220)), ('m_pi0', mpm.mpf('134.9768')), ('m_rho', mpm.mpf('775.26')),
           ('m_p', mpm.mpf('938.272')), ('v', mpm.mpf('246220'))]
HEADLINE = ['1/alpha', 'sin2th13', 'n_s', 'm_p/m_e', 'm_mu/m_e', 'Koide_Q', 'm_H/v', 'V_us', 'Omega_L', 'H0/100', 'ln(mP/me)']
STAR_DEF = dict(lattice='FCC=BCT(sqrt2)', c_over_a='sqrt(2)', unit='D', radius_def='inscribed', voids='oct+tet',
                coupling='product/pi', correction='N=-2,s=+1', dim=3, anchor='220MeV')
G_LIST = ['product', 'ratio_a/b', 'ratio_b/a', 'sum', 'absdiff', 'geomean', 'ra^2', 'rb^2']
K_LIST = [('1', mpm.mpf(1)), ('2', mpm.mpf(2)), ('pi', mpm.pi), ('2pi', 2 * mpm.pi), ('4pi', 4 * mpm.pi), ('pi^2', mpm.pi ** 2),
          ('e', mpm.e), ('sqrt2', mpm.sqrt(2)), ('sqrt3', mpm.sqrt(3))]
N_EXACT = sorted(set([Fraction(3, 8), Fraction(3, 4), Fraction(1), Fraction(3, 2), Fraction(2), Fraction(9, 4), Fraction(3),
                      Fraction(4), Fraction(5), Fraction(6), Fraction(8), Fraction(9)]) |
                 set(-x for x in [Fraction(3, 8), Fraction(3, 4), Fraction(1), Fraction(3, 2), Fraction(2), Fraction(9, 4),
                                  Fraction(3), Fraction(4), Fraction(5), Fraction(6), Fraction(8), Fraction(9)]))

def gfun(g, a, b):
    return {'product': a * b, 'ratio_a/b': a / b, 'ratio_b/a': b / a, 'sum': a + b, 'absdiff': abs(a - b),
            'geomean': mpm.sqrt(a * b), 'ra^2': a * a, 'rb^2': b * b}[g]

def alpha0_star_form(ra, rb):
    return ra * rb / mpm.pi if rb is not None else ra * ra / mpm.pi   # F6 * ; F5 rule for one void

def inv_alpha_star(a0):
    if a0 == 0: return None
    return 1 / (a0 * (1 - 2 * a0))

def make_row(rid, sets, fork, branch, ra, rb, a0=None, **kw):
    d = dict(STAR_DEF); d.update(kw)
    a0 = alpha0_star_form(ra, rb) if a0 is None else a0
    row = dict(row_id=rid, sets=list(sets), fork=fork, branch=branch, r_a=ra, r_b=rb, alpha0=a0, status='scored', note='')
    row.update(d)
    row['inv_alpha_starF7'] = inv_alpha_star(a0)
    geo = [ra, rb if rb is not None else ra, a0]
    vals = sorted(set([S(x, KEYDIG) for x in list(FIXED_MP.values()) + geo]))
    row['key'] = (tuple(vals), row['anchor'])
    row['defn'] = (row['lattice'], row['c_over_a'], row['unit'], row['radius_def'], row['voids'], row['coupling'],
                   row['correction'], row['dim'], row['anchor'])
    return row

def build_rows(G):
    rows = []
    s = G['star']
    star = make_row('STAR', ['one_step', 'F1xF3'], '*', '* (all forks taken)', s['r_a'], s['r_b'])
    rows.append(star)
    # ---- F1 lattice (u = D, inscribed, both voids, product/pi)
    L = G['lattices']
    rows.append(make_row('F1:SC', ['one_step'], 'F1', 'SC', L['SC']['r_a'], None, lattice='SC', c_over_a='', voids='cube'))
    rows.append(make_row('F1:BCC', ['one_step'], 'F1', 'BCC (BCT c/a=1)', L['BCC']['r_a'], L['BCC']['r_b'], lattice='BCC', c_over_a='1'))
    rows.append(make_row('F1:HCP', ['one_step'], 'F1', 'HCP (ideal)', L['HCP']['r_a'], L['HCP']['r_b'], lattice='HCP', c_over_a=''))
    rows.append(make_row('F1:Diamond', ['one_step'], 'F1', 'Diamond cubic', L['Diamond']['r_a'], None, lattice='Diamond', c_over_a='', voids='T'))
    rows.append(make_row('F1:D4', ['one_step'], 'F1', 'D4 (4-dim)', L['D4']['r_a'], L['D4']['r_b'], lattice='D4', c_over_a='', dim=4, voids='hole[1]+hole[2]'))
    r = make_row('F1:RCP', [], 'F1', 'Random close packing', s['r_a'], s['r_b'], lattice='RCP', c_over_a='')
    r['status'] = 'map-only (prompt F1: noted, not scored separately)'; rows.append(r)
    # ---- F2 axial ratio (named + crossings)
    for lab, rr, extra in G['F2_named']:
        if lab == 'sqrt(2)': continue
        v = G['bct'][lab]
        row = make_row(f'F2:c/a={lab}', ['one_step'], 'F2', f'c/a = {lab}' + (' [shell crossing]' if extra else ''), v['r_a'], v['r_b'],
                       lattice=f'BCT({lab})', c_over_a=lab)
        if v['zero_a']: row['note'] = 'oct-continuation (2b) void has zero radius at this c/a'
        rows.append(row)
    # ---- F2 alternative reading (K13; reported only): voids = the two deepest Voronoi-vertex classes
    for lab, rr, extra in G['F2_named']:
        if lab == 'sqrt(2)': continue
        vv = G['F2_vv'][lab]
        rows.append(make_row(f'F2vv:c/a={lab}', ['F2_VV_alt'], 'F2vv', f'c/a = {lab} (Voronoi-vertex voids)', vv[0]['rho'],
                             vv[1]['rho'] if len(vv) > 1 else None, lattice=f'BCT({lab})', c_over_a=lab, voids='VV'))
    # ---- F3 unit (FCC)
    for u in ['R', 'a_cubic', 'c', 'oct_void_diameter', 'tet_void_diameter', 'r_WS']:
        f = G['units']['FCC'][u]
        rows.append(make_row(f'F3:u={u}', ['one_step'], 'F3', f'u = {u}', s['r_a'] / f, s['r_b'] / f, unit=u))
    # ---- F4 radius definition
    for rd in ['polyhedron_circumradius', 'polyhedron_inradius', 'mean_in_circ']:
        ra, rb = G['F4'][rd]
        rows.append(make_row(f'F4:{rd}', ['one_step'], 'F4', rd, ra, rb, radius_def=rd))
    # ---- F5 which voids
    rows.append(make_row('F5:{oct}', ['one_step'], 'F5', 'oct only', s['r_a'], None, voids='oct'))
    rows.append(make_row('F5:{tet}', ['one_step'], 'F5', 'tet only', s['r_b'], None, voids='tet'))
    # ---- F6 coupling form
    for g in G_LIST:
        for kn, kv in K_LIST:
            if (g, kn) == ('product', 'pi'): continue
            rows.append(make_row(f'F6:{g}/{kn}', ['one_step'], 'F6', f'{g}/{kn}', s['r_a'], s['r_b'],
                                 a0=gfun(g, s['r_a'], s['r_b']) / kv, coupling=f'{g}/{kn}'))
    # ---- F7 correction form (alphabet unchanged; recorded so the identity is visible)
    for N, sg in [(None, None)] + [(n, t) for n in N_EXACT for t in (1, -1)]:
        if (N, sg) == (Fraction(-2), 1): continue
        lab = 'none' if N is None else f'N={N},s={sg:+d}'
        row = make_row(f'F7:{lab}', ['one_step'], 'F7', lab, s['r_a'], s['r_b'], correction=lab)
        a0 = row['alpha0']
        row['inv_alpha_branchF7'] = 1 / a0 if N is None else 1 / (a0 * (1 + mpm.mpf(N.numerator) / N.denominator * a0) ** sg)
        rows.append(row)
    # ---- F8 dimension
    rows.append(make_row('F8:d=2', ['one_step'], 'F8', 'd = 2 (triangular lattice)', L['HEX2D']['r_a'], None,
                         lattice='HEX2D', c_over_a='', dim=2, voids='triangle'))
    rows.append(make_row('F8:d=4', ['one_step'], 'F8', 'd = 4 (D4)', L['D4']['r_a'], L['D4']['r_b'], lattice='D4', c_over_a='',
                         dim=4, voids='hole[1]+hole[2]'))
    # ---- F9 anchor
    for an, _ in ANCHORS[1:]:
        rows.append(make_row(f'F9:Lambda={an}', ['one_step'], 'F9', f'anchor = {an}', s['r_a'], s['r_b'], anchor=an))
    # ---- F1 x F3
    for lat in ['SC', 'BCC', 'FCC', 'HCP', 'Diamond', 'D4']:
        for u in ['R', 'D', 'a_cubic', 'c', 'oct_void_diameter', 'tet_void_diameter', 'r_WS']:
            f = G['units'][lat].get(u)
            lv = L[lat]
            nm = f'F1xF3:{lat}|{u}'
            two = lv.get('r_b') is not None
            kw = dict(lattice=('FCC=BCT(sqrt2)' if lat == 'FCC' else ('BCC' if lat == 'BCC' else lat)),
                      c_over_a={'FCC': 'sqrt(2)', 'BCC': '1'}.get(lat, ''), unit=u, dim=4 if lat == 'D4' else 3,
                      voids={'SC': 'cube', 'Diamond': 'T', 'D4': 'hole[1]+hole[2]'}.get(lat, 'oct+tet'))
            if f is None:
                row = make_row(nm, [], 'F1xF3', f'{lat} x u={u}', lv['r_a'], lv.get('r_b'), **kw)
                row['status'] = 'n/a (unit undefined for this lattice, K8)'
            else:
                row = make_row(nm, ['F1xF3'], 'F1xF3', f'{lat} x u={u}', lv['r_a'] / f, (lv['r_b'] / f) if two else None, **kw)
            rows.append(row)
    r = make_row('F1xF3:RCP|*', [], 'F1xF3', 'RCP x all units', s['r_a'], s['r_b'], lattice='RCP')
    r['status'] = 'map-only (prompt F1: RCP noted, not scored separately)'; rows.append(r)
    # ---- F2 continuum (plot set, K4)
    for k in range(100, 201):
        lab = f'{k / 100:.2f}'; v = G['continuum'][lab]
        rows.append(make_row(f'F2c:c/a={lab}', ['F2_continuum'], 'F2c', f'c/a = {lab}', v['r_a'], v['r_b'],
                             lattice=f'BCT({lab})', c_over_a=lab))
    return rows

def build_geometry():
    s2 = mpm.sqrt(2)
    G = {}
    G['checks'] = cross_checks()
    cross = shell_crossings()
    named = {Fraction(2, 3): 'named', Fraction(1): 'named', Fraction(2): 'named', Fraction(3): 'named', Fraction(4): 'named'}
    F2 = []; F2r2 = []
    for r2 in sorted(set(cross) | set(named)):
        lab = ca_label(r2); rr = mpm.sqrt(mpm.mpf(r2.numerator) / r2.denominator)
        F2.append((lab, rr, r2 not in named)); F2r2.append((lab, r2))
    fp = lambda t: f'({t[0]}, {t[1]})'
    G['F2_named'] = F2; G['F2_crossings'] = {ca_label(k): [(fp(a), fp(b), str(c)) for a, b, c in v] for k, v in cross.items()}
    G['bct'] = {lab: bct_voids(rr) for lab, rr, _ in F2}
    G['F2_closure'], G['F2_closure_ok'] = closure_checks(F2r2)
    G['delaunay'] = {lab: delaunay_classes(rr) for lab, rr, _ in F2}
    G['F2_vv'] = {lab: vv_voids(rr) for lab, rr, _ in F2}
    star = G['bct']['sqrt(2)']; G['star'] = star
    L = {}
    L['SC'] = sc_voids()
    b = G['bct']['1']; L['BCC'] = dict(b)
    L['FCC'] = dict(star)
    L['HCP'] = hcp_voids(); L['Diamond'] = diamond_voids(); L['D4'] = d4_voids(); L['HEX2D'] = hex2d_voids()
    G['lattices'] = L
    # units u/D per lattice (K8); None = undefined
    U = {}
    def common(lv, dim):
        Vd = lv['V'] / lv['D'] ** dim
        return {'R': H, 'D': mpm.mpf(1), 'oct_void_diameter': 2 * lv['r_a'],
                'tet_void_diameter': (2 * lv['r_b']) if lv.get('r_b') is not None else None, 'r_WS': ws_radius(Vd, dim)}
    U['SC'] = common(L['SC'], 3); U['SC'].update(a_cubic=1 / L['SC']['D'], c=1 / L['SC']['D'])
    U['BCC'] = common(L['BCC'], 3); U['BCC'].update(a_cubic=1 / L['BCC']['D'], c=1 / L['BCC']['D'])    # a=c=1 in BCT units
    U['FCC'] = common(L['FCC'], 3); U['FCC'].update(a_cubic=s2 / L['FCC']['D'], c=s2 / L['FCC']['D'])  # cubic edge = sqrt2 a_BCT; BCT c = sqrt2 a
    U['HCP'] = common(L['HCP'], 3); U['HCP'].update(a_cubic=None, c=L['HCP']['c_axis'] / L['HCP']['D'])
    U['Diamond'] = common(L['Diamond'], 3); U['Diamond'].update(a_cubic=1 / L['Diamond']['D'], c=1 / L['Diamond']['D'])
    U['D4'] = common(L['D4'], 4); U['D4'].update(a_cubic=2 / L['D4']['D'], c=2 / L['D4']['D'])
    G['units'] = U
    # F4 polyhedra around the * voids
    pa = polyhedron_radii(star['site_a'], star['verts_a']); pb = polyhedron_radii(star['site_b'], star['verts_b'])
    G['F4_poly'] = dict(oct=pa, tet=pb)
    D = star['D']
    G['F4'] = {'polyhedron_circumradius': (pa[0] / D, pb[0] / D), 'polyhedron_inradius': (pa[1] / D, pb[1] / D),
               'mean_in_circ': ((pa[0] + pa[1]) / (2 * D), (pb[0] + pb[1]) / (2 * D))}
    s3, s6 = mpm.sqrt(3), mpm.sqrt(6)
    G['F4_closedform'] = all(abs(x - y) < mpm.mpf(10) ** -REP for x, y in [
        (pa[0] / D, 1 / s2), (pa[1] / D, 1 / s6), (pb[0] / D, s6 / 4), (pb[1] / D, s6 / 12)])
    G['continuum'] = {f'{k / 100:.2f}': bct_voids(mpm.mpf(k) / 100) for k in range(100, 201)}
    return G

# --------------------------------------------------------------------------------------------
# 3. F6 x F7 sweep (1/alpha only)
# --------------------------------------------------------------------------------------------
def alpha_sweep(G):
    s = G['star']; ra, rb = s['r_a'], s['r_b']
    rows = []
    for g in G_LIST:
        for kn, kv in K_LIST:
            a0 = gfun(g, ra, rb) / kv
            for N, sg in [(None, None)] + [(n, t) for n in N_EXACT for t in (1, -1)]:
                if N is None: al = a0
                else:
                    base = 1 + mpm.mpf(N.numerator) / N.denominator * a0
                    al = a0 * base ** sg if base != 0 else None
                inv = (1 / al) if (al is not None and al != 0) else None
                Hh = abs(inv - INV_ALPHA_OBS) / INV_ALPHA_OBS if inv is not None else None
                rows.append(dict(g=g, k=kn, alpha0=a0, N='none' if N is None else str(N), s='' if sg is None else f'{sg:+d}',
                                 alpha=al, inv_alpha=inv, H=Hh, star=(g == 'product' and kn == 'pi' and N == Fraction(-2) and sg == 1)))
    Hstar = next(r['H'] for r in rows if r['star'])
    lit = mpm.mpf('0.00013')
    for r in rows:
        h = r['H']
        r['w_Hstar'] = h is not None and h <= Hstar
        r['w_lit'] = h is not None and h <= lit
        r['w_01'] = h is not None and h <= mpm.mpf('0.001')
        r['w_1'] = h is not None and h <= mpm.mpf('0.01')
    return rows, Hstar

# --------------------------------------------------------------------------------------------
# 4. enumeration and scoring (PRED's own functions; per-branch replay of PRED lines 23, 32, 38-41)
# --------------------------------------------------------------------------------------------
def enumerate_alphabet(atoms_b):
    with np.errstate(all='ignore'):
        A = np.array(list(atoms_b.values()))
        L1 = clean(unary(A))
        L2 = clean(binary(L1, L1))
        L2r = clean(np.concatenate([L2, np.sqrt(np.abs(L2)), 1 / L2, L2 ** 2]))
        L3 = clean(binary(L2, L1))
        L3r = clean(np.concatenate([L3, np.sqrt(np.abs(L3)), 1 / L3]))
    return L1, L2, L2r, L3r

def score(vals, tol, with_N, a0_b, tv_b):
    """PRED's hit_stats, unmodified, called with the branch's alpha0 and target vector bound as its globals."""
    global a0, tv
    sv = (a0, tv); a0, tv = a0_b, tv_b
    try:
        with np.errstate(all='ignore'):
            p, cov = hit_stats(vals, tol, with_N)
    finally:
        a0, tv = sv
    return float(p), cov.copy()

T_SRC = None
def targets_for(anchor_value):
    """re-evaluate PRED's target-dict literal (verbatim text) with Lam bound to the anchor (F9)."""
    ns = {'Lam': float(anchor_value), 'mpi0': 134.9768, 'math': math}
    Td = eval(T_SRC, ns)
    return np.array([Td[k] for k in NAMES])

def atoms_for(row):
    a = dict(ATOMS_PRED)
    a['roct'] = float(row['r_a']); a['rtet'] = float(row['r_b'] if row['r_b'] is not None else row['r_a'])
    a['a0'] = float(row['alpha0'])
    return a

FULL_CFGS = ['P_3N_1', 'P_3N_01', 'a_2N_1', 'a_2N_01', 'b_3x_1', 'b_3x_01', 'c_3N_1', 'c_3N_01', 'd_3N_05']
PLOT_CFGS = ['P_3N_1', 'P_3N_01']
CFG = {'P_3N_1': ('3', .01, True, 'all'), 'P_3N_01': ('3', .001, True, 'all'), 'a_2N_1': ('2', .01, True, 'all'),
       'a_2N_01': ('2', .001, True, 'all'), 'b_3x_1': ('3', .01, False, 'all'), 'b_3x_01': ('3', .001, False, 'all'),
       'c_3N_1': ('3', .01, True, 'head'), 'c_3N_01': ('3', .001, True, 'head'), 'd_3N_05': ('3', .005, True, 'all')}
HEAD_IDX = None

def run_scoring(rows):
    groups = {}
    for r in rows:
        if r['status'] != 'scored' or not r['sets']: continue
        groups.setdefault(r['key'][0], {}).setdefault(r['anchor'], []).append(r)
    TV = {an: targets_for(v) for an, v in ANCHORS}
    assert np.array_equal(TV['220MeV'], TV_PRED), 'target re-evaluation does not reproduce PRED tv'
    results = {}; t0 = time.time(); n = len(groups)
    for gi, (akey, byanchor) in enumerate(groups.items()):
        rep = next(iter(byanchor.values()))[0]
        atoms_b = atoms_for(rep); a0b = atoms_b['a0']
        L1, L2, L2r_b, L3r_b = enumerate_alphabet(atoms_b)
        v3 = np.sort(np.abs(L3r_b)); v2 = np.sort(np.abs(L2r_b))
        need_full = any(s in ('one_step', 'F1xF3', 'F2_VV_alt') for rs in byanchor.values() for r in rs for s in r['sets'])
        cfgs = FULL_CFGS if need_full else PLOT_CFGS
        for an, rs in byanchor.items():
            tvb = TV[an]; out = dict(n1=len(L1), n2=len(L2r_b), n3=len(L3r_b))
            for c in cfgs:
                lev, tol, wn, tg = CFG[c]
                vals = v3 if lev == '3' else v2
                tvv = tvb if tg == 'all' else tvb[HEAD_IDX]
                out[c] = score(vals, tol, wn, a0b, tvv)
            results[(akey, an)] = out
        del L1, L2, L2r_b, L3r_b, v3, v2
        if gi % 10 == 0 or gi == n - 1:
            log(f'  scored alphabet {gi + 1}/{n}  elapsed {time.time() - t0:.0f}s  maxrss {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB')
    for r in rows:
        if r['status'] == 'scored' and r['sets']:
            r['res'] = results[(r['key'][0], r['anchor'])]
    return results

# --------------------------------------------------------------------------------------------
# 5. expression recovery for logged hits (labelled replay of the same grammar)
# --------------------------------------------------------------------------------------------
UN_LAB = ['{}', 'sqrt({})', 'cbrt({})', '({})^2', '1/({})', 'exp(-{})', 'ln|{}|']
OPS = ['+', '-', '*', '/']
LABEL = {'roct': 'r_a', 'rtet': 'r_b', 'a0': 'alpha0', 'SD4': 'S_D4'}

def _clean_idx(v):
    idx = np.nonzero(np.isfinite(v))[0]; w = v[idx]
    m = (np.abs(w) > 1e-6) & (np.abs(w) < 1e6); idx = idx[m]; w = w[m]
    u, first = np.unique(np.round(w, 10), return_index=True)
    return u, idx[first]

def find_expr(atoms_b, t, tol, with_N, a0b):
    names = [LABEL.get(k, k) for k in atoms_b]; A = np.array(list(atoms_b.values())); nA = len(A)
    with np.errstate(all='ignore'):
        L1v, L1i = _clean_idx(unary(A))
        L1lab = [UN_LAB[i // nA].format(names[i % nA]) for i in L1i]
        n1 = len(L1v)
        L2v, L2i = _clean_idx(binary(L1v, L1v))
    def lab2(k):
        op = k // (n1 * n1); rem = k % (n1 * n1); return f'({L1lab[rem // n1]} {OPS[op]} {L1lab[rem % n1]})'
    facs = ([(n, 1 + n * a0b) for n in Nmenu] + [(None, 1.0)]) if with_N else [(None, 1.0)]
    def hits(w):
        aw = np.abs(w); best = None
        for n, f in facs:
            if not (np.isfinite(f) and f > 0): continue
            lo, hi = t / f * (1 - tol), t / f * (1 + tol)
            m = np.nonzero((aw >= lo) & (aw <= hi))[0]
            if len(m):
                err = aw[m] * f / t - 1; j = m[np.argmin(np.abs(err))]; e = aw[j] * f / t - 1
                if best is None or abs(e) < abs(best[0]): best = (e, j, n)
        return best
    b = hits(L1v)
    if b: return dict(level=1, expr=L1lab[b[1]], N=b[2], err=b[0], value=float(abs(L1v[b[1]])))
    with np.errstate(all='ignore'):
        roots2 = [('{}', L2v), ('sqrt|{}|', np.sqrt(np.abs(L2v))), ('1/{}', 1 / L2v), ('({})^2', L2v ** 2)]
    best = None
    for rl, w in roots2:
        wv, wi = _clean_idx(w); b = hits(wv)
        if b and (best is None or abs(b[0]) < abs(best[0])): best = (b[0], rl.format(lab2(L2i[wi[b[1]]])), b[2], float(abs(wv[b[1]])))
    if best: return dict(level=2, expr=best[1], N=best[2], err=best[0], value=best[3])
    for jy in range(n1):
        y = L1v[jy]
        for oi in range(4):
            with np.errstate(all='ignore'):
                z = [L2v + y, L2v - y, L2v * y, L2v / y][oi]
                zv, zi = _clean_idx(z)
                for rl, w in (('{}', zv), ('sqrt|{}|', np.sqrt(np.abs(zv))), ('1/{}', 1 / zv)):
                    wv, wi = _clean_idx(w); b = hits(wv)
                    if b and (best is None or abs(b[0]) < abs(best[0])):
                        k2 = L2i[zi[wi[b[1]]]]
                        best = (b[0], rl.format(f'({lab2(k2)} {OPS[oi]} {L1lab[jy]})'), b[2], float(abs(wv[b[1]])))
    if best: return dict(level=3, expr=best[1], N=best[2], err=best[0], value=best[3])
    return None

# --------------------------------------------------------------------------------------------
# 6. ranks, look-elsewhere counts, verdicts
# --------------------------------------------------------------------------------------------
def pct(arr, x, kind):
    arr = np.asarray(arr); n = len(arr); left = int((arr < x).sum()); right = int((arr <= x).sum())
    v = {'rank': (left + right + (1 if right > left else 0)) * 50.0 / n, 'strict': left * 100.0 / n,
         'weak': right * 100.0 / n, 'mean': (left + right) * 50.0 / n}[kind]
    assert abs(v - scipy.stats.percentileofscore(arr, x, kind=kind)) < 1e-9
    return v

VARIANTS = {'primary': ('P_3N_1', 'P_3N_01'), '(a) 2-atom': ('a_2N_1', 'a_2N_01'), '(b) N-layer off': ('b_3x_1', 'b_3x_01'),
            '(c) 11 headline targets': ('c_3N_1', 'c_3N_01'), '(d) tolerance 0.5%': ('d_3N_05', 'P_3N_01')}

def dedupe(rows, by='key'):
    seen = set(); out = []
    for r in rows:
        k = r[by]
        if k in seen: continue
        seen.add(k); out.append(r)
    return out

def evaluate(star, onestep, general, La_star, var, kind='rank'):
    cC, c01 = VARIANTS[var]
    C = np.array([r['res'][cC][1].sum() for r in onestep]); C01 = np.array([r['res'][c01][1].sum() for r in onestep])
    sC, s01 = int(star['res'][cC][1].sum()), int(star['res'][c01][1].sum())
    prC, pr01 = pct(C, sC, kind), pct(C01, s01, kind)
    covG = np.array([r['res'][c01][1] for r in general])
    Lt = covG.sum(0); nG = len(general)
    tnames = NAMES if var != '(c) 11 headline targets' else HEADLINE
    starcov = star['res'][c01][1]
    excl_star = [tnames[i] for i in range(len(tnames)) if starcov[i] and Lt[i] < 0.05 * nG]
    br = []
    for r in onestep:
        if r is star: continue
        ex = [tnames[i] for i in range(len(tnames)) if r['res'][c01][1][i] and not starcov[i]]
        ex5 = [t for t in ex if Lt[tnames.index(t)] < 0.05 * nG]
        if ex: br.append((r['row_id'], int(r['res'][cC][1].sum()), int(r['res'][c01][1].sum()), ex, ex5))
    sc1 = prC >= 95 and pr01 >= 95 and len(excl_star) >= 2 and La_star <= 3
    sc2 = (10 <= prC <= 90) or (10 <= pr01 <= 90) or La_star >= 10
    sc3 = [b for b in br if b[1] > sC and b[2] > s01 and len(b[3]) >= 2]
    if sc2: sc1 = False
    vs = sorted(([1] if sc1 else []) + ([2] if sc2 else []) + ([3] if sc3 else []))
    return dict(var=var, n_onestep=len(onestep), n_general=nG, C_star=sC, C01_star=s01, PR_C=prC, PR_C01=pr01,
                C_dist=dict(zip(*np.unique(C, return_counts=True))), C01_dist=dict(zip(*np.unique(C01, return_counts=True))),
                excl_star=excl_star, branch_excl=br, sc3=sc3, verdicts=vs, Lt=dict(zip(tnames, Lt.tolist())),
                bands=dict(C_central=10 <= prC <= 90, C_top=prC >= 95, C01_central=10 <= pr01 <= 90, C01_top=pr01 >= 95),
                cross80=dict(C=prC >= 80, C01=pr01 >= 80), ntargets=len(tnames))

# --------------------------------------------------------------------------------------------
# 7. outputs
# --------------------------------------------------------------------------------------------
def fmt(x, n=16): return '' if x is None else mpm.nstr(mpm.mpf(x), n)

def write_scores_csv(rows, path, alph_id):
    cols = ['row_id', 'sets', 'fork', 'branch', 'status', 'lattice', 'c_over_a', 'unit', 'radius_def', 'voids', 'coupling',
            'correction', 'dim', 'anchor', 'r_a', 'r_b', 'alpha0', 'inv_alpha_starF7', 'alphabet_id', 'n_distinct_1atom',
            'n_distinct_2atom', 'n_distinct_3atom', 'P_hit_1pct', 'P_hit_0.1pct', 'C_1pct', 'C_0.1pct', 'a_C_1pct', 'a_C_0.1pct',
            'b_C_1pct', 'b_C_0.1pct', 'c_C_1pct', 'c_C_0.1pct', 'd_C_0.5pct', 'missed_targets_0.1pct', 'note']
    with open(path, 'w', newline='') as f:
        w = csv.writer(f, lineterminator='\n'); w.writerow(cols)
        for r in rows:
            res = r.get('res')
            def C(c): return '' if not res or c not in res else int(res[c][1].sum())
            def P(c): return '' if not res or c not in res else f'{res[c][0]:.6f}'
            miss = '' if not res else ';'.join(NAMES[i] for i in range(len(NAMES)) if not res['P_3N_01'][1][i])
            w.writerow([r['row_id'], '|'.join(r['sets']), r['fork'], r['branch'], r['status'], r['lattice'], r['c_over_a'], r['unit'],
                        r['radius_def'], r['voids'], r['coupling'], r['correction'], r['dim'], r['anchor'], S(r['r_a']),
                        S(r['r_b']), S(r['alpha0']), S(r['inv_alpha_starF7']), alph_id.get(r['key'], ''),
                        res['n1'] if res else '', res['n2'] if res else '', res['n3'] if res else '',
                        P('P_3N_1'), P('P_3N_01'), C('P_3N_1'), C('P_3N_01'), C('a_2N_1'), C('a_2N_01'), C('b_3x_1'), C('b_3x_01'),
                        C('c_3N_1'), C('c_3N_01'), C('d_3N_05'), miss, r['note']])

def write_sweep_csv(sw, path):
    cols = ['idx', 'g', 'k', 'alpha0', 'N', 's', 'alpha', 'inv_alpha', 'H_alpha', 'within_Hstar', 'within_0.013pct_literal',
            'within_0.1pct', 'within_1pct', 'is_star']
    with open(path, 'w', newline='') as f:
        w = csv.writer(f, lineterminator='\n'); w.writerow(cols)
        for i, r in enumerate(sw):
            w.writerow([i + 1, r['g'], r['k'], S(r['alpha0']), r['N'], r['s'], S(r['alpha']), S(r['inv_alpha']), S(r['H']),
                        int(r['w_Hstar']), int(r['w_lit']), int(r['w_01']), int(r['w_1']), int(r['star'])])

F10 = [
    ('S¹ ★', 'ℤ', '0', '0', 1, 'integer-charged vortex lines (π₁); no point defects, no hopfions, no skyrmions',
     'RANK SC-RANK-3 (field content undetermined by the corpus; CN-RANK-10 [CONJECTURE] reads intent as the c-axis rotor ≅ S¹); '
     'PROMOTE SC-PROMOTE-1 ("S¹ stands"); PT pre-registered, no result at this commit'),
    ('S²', '0', 'ℤ', 'ℤ (Hopf)', 2, 'hedgehogs / baby-skyrmion sheets (π₂), hopfions (π₃); no ℤ vortex charge',
     'JHF SC-JHF-1 (App JH has no stabilised S² field theory; Derrick); PROMOTE SC-PROMOTE-1 (geometry selects no promotion)'),
    ('S³ ≅ SU(2)', '0', '0', 'ℤ', 3, 'skyrmions (π₃); no line or point defects',
     'PROMOTE SC-PROMOTE-1 (no promotion beyond S¹ selected); RANK table A6 (interior ℂ² doublet recorded as internal structure, not lattice field)'),
    ('SO(3) ≅ RP³', 'ℤ₂', '0', 'ℤ', 3, 'only one non-trivial line-defect class (ℤ₂); no integer vortex charge',
     'RANK §reconciliation (c) and (iii): rotor reading loses ℤ vortex charge'),
    ('ℂ² with |Ψ|² = ρ₀', '0', '0', 'ℤ', 3, 'the constrained doublet is S³; its normalised map n̂ = Ψ†σΨ is S³ → S² (Hopf), as App JH uses',
     'RANK table A6; JHF SC-JHF-1'),
]

def write_map(G, rows, sw, Hstar, alph_id, path):
    R = {r['row_id']: r for r in rows}; out = []; A = out.append
    def aid(r): return alph_id.get(r['key'], '—') if r['status'] == 'scored' and r['sets'] else '—'
    def tr(r, extra=''):
        ia = fmt(r['inv_alpha_starF7'], 10) if r['inv_alpha_starF7'] is not None else '— (α₀ = 0)'
        return f"| {fmt(r['r_a'])} | {fmt(r['r_b']) if r['r_b'] is not None else '—'} | {fmt(r['alpha0'])} | {ia} | {aid(r)} |{extra}"
    L = G['lattices']; star = R['STAR']
    A('# Gate FORK — the map'); A('')
    A('Every fork, every branch, and what each branch produces. No verdicts are attached to the map (prompt §0); scores are in '
      '`fork_scores.csv` and the verdict in `gate_FORK_RESULT.md`.'); A('')
    A('Conventions. Geometry in mpmath at 60 dps. Tables show 16 significant digits; the ledger at the end and `fork_scores.csv` carry '
      '40. Lengths are in the branch\'s unit u (u = D, the nearest-neighbour distance, unless the row says otherwise). r_a, r_b are the '
      'two void radii (one-void branches have no r_b); α₀ is the branch\'s coupling value; "1/α (★F7)" applies the taken correction '
      'α₀(1−2α₀). "Alphabet" is the scored atom set: rows that share an alphabet id are one scored alphabet (judgement call K2).'); A('')
    A('## ★ — the taken path'); A('')
    A(f"FCC written as BCT at c/a = √2; u = D; inscribed radius ρ = circumradius − R; octahedral + tetrahedral voids; "
      f"α₀ = r_oct·r_tet/π; α = α₀(1−2α₀); d = 3; Λ = 220 MeV."); A('')
    A('| quantity | value (40 significant digits) |'); A('|---|---|')
    A(f"| r_oct = r_a | {S(star['r_a'])} |"); A(f"| r_tet = r_b | {S(star['r_b'])} |"); A(f"| α₀ | {S(star['alpha0'])} |")
    A(f"| 1/α = 1/[α₀(1−2α₀)] | {S(star['inv_alpha_starF7'])} |"); A(f"| H_α(★) = \\|1/α − 137.035999\\|/137.035999 | {S(Hstar)} |"); A('')
    A('## F1 — lattice / packing (u = D, inscribed, all voids, α₀ = r_a r_b/π; one void → r²/π)'); A('')
    A('| branch | voids (coordination of each site) | r_a | r_b | α₀ | 1/α (★F7) | alphabet | note |'); A('|---|---|---|---|---|---|---|---|')
    A(f"| FCC = BCT √2 ★ | oct ({L['FCC']['coord_a']}), tet ({L['FCC']['coord_b']}) " + tr(star, ' taken |'))
    A(f"| SC | cube centre ({L['SC']['coord_a']}) " + tr(R['F1:SC'], ' one void |'))
    A(f"| BCC (BCT c/a = 1) | distorted oct 2b ({L['BCC']['coord_a']}), distorted tet 4d ({L['BCC']['coord_b']}) " + tr(R['F1:BCC'], ' oct site is a 2-neighbour saddle, not a Voronoi vertex |'))
    A(f"| HCP (ideal c/a) | oct ({L['HCP']['coord_a']}), tet ({L['HCP']['coord_b']}) " + tr(R['F1:HCP'], ' stacking-blind: alphabet identical to ★ |'))
    A(f"| Diamond cubic | T site ({L['Diamond']['coord_a']}); second T site check ρ/D = {fmt(L['Diamond']['r_a_check'])} " + tr(R['F1:Diamond'], ' one large void, ρ = R |'))
    A(f"| D4 (d = 4) | hole[1] (1,0,0,0) ({L['D4']['coord_a']}), hole[2] (½⁴) ({L['D4']['coord_b']}); hole[3] ρ/D = {fmt(L['D4']['r_c'])} " + tr(R['F1:D4'], ' the three hole classes have equal radius (triality) |'))
    A(f"| Random close packing | as FCC (stacking-blind) " + tr(R['F1:RCP'], ' noted, not scored separately |')); A('')
    A('## F2 — axial ratio c/a of the BCT family (u = D(c/a), voids = continuations 2b / 4d of the ★ oct / tet sites)'); A('')
    A('Shell crossings enumerated by K5 (exact rational arithmetic; vector classes written (x²+y², z²) in units of a², c/a = r):'); A('')
    A('| c/a | origin | degenerate vector classes (x²+y², z²) ≡ (x²+y², z²) at common \\|v\\|²/a² |'); A('|---|---|---|')
    for lab, rr, extra in G['F2_named']:
        cr = G['F2_crossings'].get(lab, [])
        A(f"| {lab} = {fmt(rr, 10)} | {'crossing found by enumeration' if extra else 'named in prompt'} | " +
          '; '.join(f"{a} ≡ {b} at {c}" for a, b, c in cr[:6]) + (' …' if len(cr) > 6 else '') + ' |')
    A('')
    A('| c/a | D-shell coordination | r_a (2b) | r_b (4d) | α₀ | 1/α (★F7) | alphabet | Voronoi-vertex classes in one cell: ρ/D (simplices, of which local maxima, distinct sites) |')
    A('|---|---|---|---|---|---|---|---|')
    for lab, rr, extra in G['F2_named']:
        v = G['bct'][lab]; r = star if lab == 'sqrt(2)' else R[f'F2:c/a={lab}']
        dl = G['delaunay'][lab]
        dls = dl if isinstance(dl, str) else '; '.join(f"{k:.6f} ({n},{m},{s})" for k, n, m, s in dl)
        A(f"| {lab}{' ★' if lab == 'sqrt(2)' else ''} | {v['coordD']} " + tr(r, f" {dls} |"))
    for lab, rr, extra in G['F2_named']:
        if lab != 'sqrt(2)' and R[f'F2:c/a={lab}']['note']:
            A(''); A(f"Note, c/a = {lab}: {R[f'F2:c/a={lab}']['note']} (the two axial neighbours touch, c = D); r_a = α₀ = 0, so this alphabet carries r_b as its only geometric atom.")
    A(''); A('Closure: numerics vs piecewise closed form and 60 vs 80 dps, all agree to 40 digits: ' +
             ', '.join(f"{l}: {'yes' if ok else 'NO'}" for l, ok in G['F2_closure'])); A('')
    A('Alternative reading K13 (reported only): voids = Voronoi-vertex classes re-solved at 60 dps (two deepest enter):'); A('')
    A('| c/a | Voronoi-vertex classes: ρ/D (sites per cell, local max, coordination, vertex confirmed) | r_a | r_b | α₀ | alphabet |'); A('|---|---|---|---|---|---|')
    for lab, rr, extra in G['F2_named']:
        vv = G['F2_vv'][lab]
        cl = '; '.join(f"{fmt(d['rho'], 12)} ({d['nsite']}, {'max' if d['local_max'] else 'not max'}, {d['coord']}, {'ok' if d['vertex_ok'] else 'NO'})" for d in vv)
        r = star if lab == 'sqrt(2)' else R[f'F2vv:c/a={lab}']
        A(f"| {lab} | {cl} | {fmt(r['r_a'])} | {fmt(r['r_b']) if r['r_b'] is not None else '—'} | {fmt(r['alpha0'])} | {aid(r)} |")
    A('')
    A('### F2 continuum (c/a = 1.00 … 2.00, step 0.01; plotted quantities, K4)'); A('')
    A('| c/a | r_a (2b) | r_b (4d) | α₀ | 1/α (★F7) | alphabet |'); A('|---|---|---|---|---|---|')
    for k in range(100, 201):
        lab = f'{k / 100:.2f}'; A(f"| {lab} " + tr(R[f'F2c:c/a={lab}']))
    A('')
    A('## F3 — length unit (FCC, inscribed, both voids)'); A('')
    A('| unit u | u / D | r_a | r_b | α₀ | 1/α (★F7) | alphabet |'); A('|---|---|---|---|---|---|---|')
    A(f"| D ★ | 1 " + tr(star))
    for u in ['R', 'a_cubic', 'c', 'oct_void_diameter', 'tet_void_diameter', 'r_WS']:
        A(f"| {u} | {fmt(G['units']['FCC'][u])} " + tr(R[f'F3:u={u}']))
    A('')
    pa, pb = G['F4_poly']['oct'], G['F4_poly']['tet']
    A('## F4 — void radius definition (FCC, u = D)'); A('')
    A(f"Hole polyhedra found numerically: octahedral site → {pa[3]} vertices, {pa[2]} faces; tetrahedral site → {pb[3]} vertices, {pb[2]} faces. "
      f"Closed-form agreement to 40 digits (1/√2, 1/√6, √6/4, √6/12): {'yes' if G['F4_closedform'] else 'NO'}."); A('')
    A('| definition | r_a | r_b | α₀ | 1/α (★F7) | alphabet |'); A('|---|---|---|---|---|---|')
    A('| inscribed: circumradius − R ★ ' + tr(star))
    for rd in ['polyhedron_circumradius', 'polyhedron_inradius', 'mean_in_circ']: A(f"| {rd} " + tr(R[f'F4:{rd}']))
    A('')
    A('## F5 — which voids enter (FCC, u = D; one void → α₀ = r²/π)'); A('')
    A('| voids | r_a | r_b | α₀ | 1/α (★F7) | alphabet |'); A('|---|---|---|---|---|---|')
    A('| oct + tet ★ ' + tr(star)); A('| oct only ' + tr(R['F5:{oct}'])); A('| tet only ' + tr(R['F5:{tet}'])); A('')
    A('## F6 — coupling form α₀ = g(r_oct, r_tet)/k (FCC, u = D)'); A('')
    A(f"The rule lists 8 functions g and 9 constants k: {len(G_LIST) * len(K_LIST)} forms (the prompt's \"9 × 9 = 81\" is an arithmetic slip; see result §defects)."); A('')
    A('| g / k | α₀ | 1/α (★F7) | alphabet |'); A('|---|---|---|---|')
    for g in G_LIST:
        for kn, _ in K_LIST:
            r = star if (g, kn) == ('product', 'pi') else R[f'F6:{g}/{kn}']
            A(f"| {g}/{kn}{' ★' if r is star else ''} | {fmt(r['alpha0'])} | {fmt(r['inv_alpha_starF7'], 10)} | {aid(r)} |")
    A('')
    A('## F7 — correction form α = α₀(1 + Nα₀)^s (★ α₀)'); A('')
    A('α does not appear in the PRED atom list, so every F7 branch has the ★ alphabet; F7 acts only on 1/α (the F6 × F7 sweep).'); A('')
    A('| correction | 1/α | H_α | alphabet |'); A('|---|---|---|---|')
    A(f"| N=-2,s=+1 ★ | {fmt(star['inv_alpha_starF7'], 12)} | {fmt(Hstar, 6)} | {aid(star)} |")
    for N, sg in [(None, None)] + [(n, t) for n in N_EXACT for t in (1, -1)]:
        if (N, sg) == (Fraction(-2), 1): continue
        lab = 'none' if N is None else f'N={N},s={sg:+d}'; r = R[f'F7:{lab}']; inv = r['inv_alpha_branchF7']
        A(f"| {lab} | {fmt(inv, 12)} | {fmt(abs(inv - INV_ALPHA_OBS) / INV_ALPHA_OBS, 6)} | {aid(r)} |")
    A('')
    A(f"## F6 × F7 — {len(sw)} forms, single target 1/α"); A('')
    A('| threshold | forms within |'); A('|---|---|')
    for lab, key in [(f'H_α(★) = {fmt(Hstar, 6)}', 'w_Hstar'), ('0.013 % literal', 'w_lit'), ('0.1 %', 'w_01'), ('1 %', 'w_1')]:
        A(f"| {lab} | {sum(r[key] for r in sw)} |")
    A(''); A('Forms within 1 % of 1/α (all of them):'); A('')
    A('| g/k | N | s | 1/α | H_α |'); A('|---|---|---|---|---|')
    for r in sorted([r for r in sw if r['w_1']], key=lambda r: r['H']):
        A(f"| {r['g']}/{r['k']}{' ★' if r['star'] else ''} | {r['N']} | {r['s']} | {fmt(r['inv_alpha'], 12)} | {fmt(r['H'], 6)} |")
    A('')
    A('## F8 — dimension (u = D, inscribed)'); A('')
    A('| d | lattice | r_a | r_b | α₀ | 1/α (★F7) | alphabet |'); A('|---|---|---|---|---|---|---|')
    A(f"| 2 | triangular, one void ({L['HEX2D']['coord_a']}) " + tr(R['F8:d=2'])); A('| 3 ★ | FCC ' + tr(star)); A('| 4 | D4 ' + tr(R['F8:d=4'])); A('')
    A('## F9 — energy anchor (alphabet unchanged; anchor-ratio targets re-expressed)'); A('')
    A('| anchor | value (MeV) | m_p/Λ | m_ρ/Λ | T_c/Λ | ln(m_P/Λ) | alphabet |'); A('|---|---|---|---|---|---|---|')
    for an, val in ANCHORS:
        tvv = targets_for(val); r = star if an == '220MeV' else R[f'F9:Lambda={an}']
        A(f"| {an}{' ★' if an == '220MeV' else ''} | {fmt(val, 10)} | " + ' | '.join(f"{tvv[NAMES.index(k)]:.10g}" for k in ['m_p/Lam', 'm_rho/Lam', 'T_c/Lam', 'ln(mP/Lam)']) + f" | {aid(r)} |")
    A('')
    A('## F10 — target manifold of the field (mapped, not scored)'); A('')
    A('| manifold | π₁ | π₂ | π₃ | components (polarisations) | permits / forbids | gate that already ruled |'); A('|---|---|---|---|---|---|---|')
    for m in F10: A(f"| {m[0]} | {m[1]} | {m[2]} | {m[3]} | {m[4]} | {m[5]} | {m[6]} |")
    A(''); A('None of these produces a number at the α₀ layer.'); A('')
    A('## F1 × F3 — lattice × unit (α₀ and alphabet; n/a = unit undefined, K8)'); A('')
    units = ['R', 'D', 'a_cubic', 'c', 'oct_void_diameter', 'tet_void_diameter', 'r_WS']
    A('| lattice | ' + ' | '.join(units) + ' |'); A('|---|' + '---|' * len(units))
    for lat in ['SC', 'BCC', 'FCC', 'HCP', 'Diamond', 'D4']:
        cells = []
        for u in units:
            r = R[f'F1xF3:{lat}|{u}']
            cells.append('n/a' if r['status'] != 'scored' else f"{fmt(r['alpha0'], 6)} ({aid(r)})")
        A(f'| {lat} | ' + ' | '.join(cells) + ' |')
    A('| RCP | ' + ' | '.join(['as FCC, not scored'] * len(units)) + ' |'); A('')
    A('## Ledger — every scored alphabet at 40 significant digits'); A('')
    A('| alphabet | rows | r_a | r_b | α₀ |'); A('|---|---|---|---|---|')
    byk = {}
    for r in rows:
        if r['status'] == 'scored' and r['sets']: byk.setdefault(alph_id[r['key']], []).append(r)
    for k in sorted(byk):
        rs = byk[k]; r0 = rs[0]
        names_ = ', '.join(x['row_id'] for x in rs[:6]) + (f' … (+{len(rs) - 6})' if len(rs) > 6 else '')
        A(f"| {k} | {names_} | {S(r0['r_a'])} | {S(r0['r_b']) if r0['r_b'] is not None else '—'} | {S(r0['alpha0'])} |")
    A('')
    with open(path, 'w') as f: f.write('\n'.join(out))

def write_tables(summary, EV, conv, rows, onestep, f1f3, general, sw, alph_id, path):
    out = []; A = out.append
    A('### ★ rank and verdict tests, primary and sensitivity runs (one-step set)'); A('')
    A('| run | n one-step | C★ | PR(C) | C₀.₁★ | PR(C₀.₁) | C distribution | C₀.₁ distribution | excl. hits of ★ | branches beating ★ on both with ≥2 excl. | verdicts met |')
    A('|---|---|---|---|---|---|---|---|---|---|---|')
    for v, e in EV.items():
        A(f"| {v} | {e['n_onestep']} | {e['C_star']}/{e['ntargets']} | {e['PR_C']:.2f} | {e['C01_star']}/{e['ntargets']} | {e['PR_C01']:.2f} | "
          f"{', '.join(f'{int(k)}:{int(n)}' for k, n in e['C_dist'].items())} | {', '.join(f'{int(k)}:{int(n)}' for k, n in e['C01_dist'].items())} | "
          f"{len(e['excl_star'])} {e['excl_star'] if e['excl_star'] else ''} | {len(e['sc3'])} | {e['verdicts'] if e['verdicts'] else 'none'} |")
    A('')
    A('### Convention sensitivity (reported; not part of the verdict rule)'); A('')
    A('| convention | n one-step | PR(C) | PR(C₀.₁) | excl. hits of ★ | verdicts met |'); A('|---|---|---|---|---|---|')
    for k, e in conv.items():
        A(f"| {k} | {e['n_onestep']} | {e['PR_C']:.2f} | {e['PR_C01']:.2f} | {len(e['excl_star'])} | {e['verdicts'] if e['verdicts'] else 'none'} |")
    A('')
    A('### ★ rank in the F1 × F3 set'); A('')
    for c, d in summary['f1f3_rank'].items():
        A(f"- {c}: " + ', '.join(f"{k} {v:.2f}" for k, v in d.items()))
    A('')
    e = EV['primary']; nG = e['n_general']
    A(f'### Per-target look-elsewhere count L(t), primary (0.1 %, N-layer on, 3-atom), out of {nG} scored alphabets'); A('')
    A('| target | L(t) | fraction |'); A('|---|---|---|')
    for t, n in sorted(e['Lt'].items(), key=lambda x: x[1]): A(f'| {t} | {n} | {n / nG:.3f} |')
    A('')
    A('### Untaken branches with targets ★ misses at 0.1 % (primary)'); A('')
    if not e['branch_excl']: A('None.')
    for b in e['branch_excl']: A(f"- {b[0]}: C={b[1]}, C₀.₁={b[2]}, targets {b[3]} (of which <5 % of alphabets: {b[4]})")
    A('')
    for v, ev in EV.items():
        if v == 'primary': continue
        if ev['branch_excl']:
            A(f'Variant {v}: ' + '; '.join(f"{b[0]} {b[3]}" for b in ev['branch_excl'][:40]) + (' …' if len(ev['branch_excl']) > 40 else ''))
            A('')
    A('### F1 × F3 grid: C / C₀.₁ (primary)'); A('')
    units = ['R', 'D', 'a_cubic', 'c', 'oct_void_diameter', 'tet_void_diameter', 'r_WS']
    R = {r['row_id']: r for r in rows}
    A('| lattice | ' + ' | '.join(units) + ' |'); A('|---|' + '---|' * len(units))
    for lat in ['SC', 'BCC', 'FCC', 'HCP', 'Diamond', 'D4']:
        cells = []
        for u in units:
            r = R[f'F1xF3:{lat}|{u}']
            cells.append('n/a' if r['status'] != 'scored' else f"{int(r['res']['P_3N_1'][1].sum())}/{int(r['res']['P_3N_01'][1].sum())}")
        A(f'| {lat} | ' + ' | '.join(cells) + ' |')
    A('')
    A('### One-step rows: C / C₀.₁ / P_hit(1 %) (primary), de-duplicated'); A('')
    A('| row | alphabet | C | C₀.₁ | P_hit 1 % | P_hit 0.1 % | missed at 0.1 % |'); A('|---|---|---|---|---|---|---|')
    for r in onestep:
        res = r['res']
        miss = [NAMES[i] for i in range(len(NAMES)) if not res['P_3N_01'][1][i]]
        A(f"| {r['row_id']} | {alph_id[r['key']]} | {int(res['P_3N_1'][1].sum())} | {int(res['P_3N_01'][1].sum())} | {res['P_3N_1'][0]:.4f} | {res['P_3N_01'][0]:.4f} | {', '.join(miss)} |")
    A('')
    A('### F2 continuum: C / C₀.₁ / P_hit(1 %) (primary)'); A('')
    A('| c/a | C | C₀.₁ | P_hit 1 % |'); A('|---|---|---|---|')
    for k in range(100, 201):
        r = R[f'F2c:c/a={k / 100:.2f}']; res = r['res']
        A(f"| {k / 100:.2f} | {int(res['P_3N_1'][1].sum())} | {int(res['P_3N_01'][1].sum())} | {res['P_3N_1'][0]:.4f} |")
    with open(path, 'w') as f: f.write('\n'.join(out))

def main():
    global T_SRC, HEAD_IDX
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', required=True); ap.add_argument('--prompt', default=None); ap.add_argument('--out', required=True)
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)
    t_start = time.time()
    prov = provenance(args.repo, args.prompt); vb = verify_verbatim(args.repo)
    log('provenance', json.dumps(prov)); log('verbatim', json.dumps(vb))
    me = open(os.path.abspath(__file__), encoding='utf-8').read()
    vbcode = me.split('# >>>>> BEGIN VERBATIM CODE')[1].split('# <<<<< END VERBATIM CODE')[0]
    T_SRC = vbcode[vbcode.index('T={') + 2: vbcode.index('}', vbcode.index('T={')) + 1]
    HEAD_IDX = np.array([NAMES.index(h) for h in HEADLINE])
    # equivalence of the per-branch replay with PRED's own module-level enumeration
    _, _, l2r, l3r = enumerate_alphabet(ATOMS_PRED)
    eq = dict(L2r_equal=bool(np.array_equal(l2r, STAR_PRED_L2r)), L3r_equal=bool(np.array_equal(l3r, STAR_PRED_L3r)),
              n2=len(STAR_PRED_L2r), n3=len(STAR_PRED_L3r))
    if not (eq['L2r_equal'] and eq['L3r_equal']): raise SystemExit('HALT: per-branch replay != PRED enumeration')
    pred_star = {}
    v3 = np.sort(np.abs(l3r))
    for tol in (.01, .001):
        for wn in (False, True):
            p, cov = score(v3, tol, wn, ATOMS_PRED['a0'], TV_PRED); pred_star[f'tol={tol} N={wn}'] = (round(p, 4), int(cov.sum()))
    del l2r, l3r, v3
    log('replay==PRED', json.dumps(eq), json.dumps(pred_star))
    # geometry
    G = build_geometry()
    for c in G['checks']: log('cross-check', c)
    log('F2 closure', G['F2_closure'], 'F4 closed form', G['F4_closedform'])
    rows = build_rows(G)
    sw, Hstar = alpha_sweep(G)
    La = dict(Hstar=sum(r['w_Hstar'] for r in sw), lit=sum(r['w_lit'] for r in sw), p01=sum(r['w_01'] for r in sw),
              p1=sum(r['w_1'] for r in sw), n=len(sw))
    log('F6xF7 sweep', len(sw), 'rows; H*(alpha) =', S(Hstar), json.dumps(La))
    # scoring
    run_scoring(rows)
    star = rows[0]
    star_mpfloats_vs_pred = {k: (round(star['res'][c][0], 4), int(star['res'][c][1].sum())) for k, c in
                             [('tol=0.01 N=True', 'P_3N_1'), ('tol=0.001 N=True', 'P_3N_01'), ('tol=0.01 N=False', 'b_3x_1'), ('tol=0.001 N=False', 'b_3x_01')]}
    onestep = dedupe([r for r in rows if 'one_step' in r['sets']])
    f1f3 = dedupe([r for r in rows if 'F1xF3' in r['sets']])
    general = dedupe([r for r in rows if ('one_step' in r['sets'] or 'F1xF3' in r['sets'])])
    alph_id = {}
    for r in rows:
        if r['status'] == 'scored' and r['sets'] and r['key'] not in alph_id: alph_id[r['key']] = f'A{len(alph_id) + 1:03d}'
    La_star = La['Hstar']
    EV = {v: evaluate(star, onestep, general, La_star, v) for v in VARIANTS}
    prim = EV['primary']
    flip = {v: (EV[v]['verdicts'] != prim['verdicts'] or EV[v]['bands'] != prim['bands']) for v in VARIANTS if v != 'primary'}
    numerics_ok = G['F2_closure_ok'] and G['F4_closedform']
    if not numerics_ok or any(flip.values()): final = 'SC-FORK-0'
    elif prim['verdicts']: final = ' + '.join(f'SC-FORK-{k}' for k in prim['verdicts'])
    else: final = 'none of SC-FORK-1/2/3 met (see result)'
    # F1xF3 percentiles
    def rank_in(setrows, cfg):
        a = np.array([r['res'][cfg][1].sum() for r in setrows]); x = star['res'][cfg][1].sum()
        return {k: pct(a, x, k) for k in ('rank', 'strict', 'weak', 'mean')}
    f1f3_rank = {c: rank_in(f1f3, c) for c in ('P_3N_1', 'P_3N_01')}
    # convention sensitivities (reported only)
    conv = {}
    onestep_P1 = [r for r in rows if 'one_step' in r['sets']]          # every fork-branch row as listed, * once
    for kind in ('strict', 'weak', 'mean'):
        conv[f'percentile kind={kind}'] = evaluate(star, onestep, general, La_star, 'primary', kind)
    d1 = set(r['defn'] for r in onestep_P1)
    gen_P1 = onestep_P1 + [r for r in rows if 'F1xF3' in r['sets'] and 'one_step' not in r['sets'] and r['defn'] not in d1]
    conv['no de-duplication (K2 off)'] = evaluate(star, onestep_P1, gen_P1, La_star, 'primary')
    with_cont = dedupe(onestep + [r for r in rows if 'F2_continuum' in r['sets']])
    conv['continuum in reference set (K4 off)'] = evaluate(star, with_cont, general, La_star, 'primary')
    with_vv = dedupe([r for r in onestep if r['fork'] != 'F2'] + [r for r in rows if 'F2_VV_alt' in r['sets']])
    gen_vv = dedupe([r for r in general if r['fork'] != 'F2'] + [r for r in rows if 'F2_VV_alt' in r['sets']])
    conv['F2 voids = Voronoi-vertex classes (K13)'] = evaluate(star, with_vv, gen_vv, La_star, 'primary')
    # logged hits with expressions (primary)
    clues = []
    for b in prim['branch_excl']:
        r = next(x for x in rows if x['row_id'] == b[0])
        tvb = targets_for(dict(ANCHORS)[r['anchor']])
        for t in b[3]:
            e = find_expr(atoms_for(r), tvb[NAMES.index(t)], .001, True, float(r['alpha0']))
            clues.append(dict(branch=b[0], target=t, expr=e))
    star_excl = []
    for t in prim['excl_star']:
        e = find_expr(atoms_for(star), TV_PRED[NAMES.index(t)], .001, True, float(star['alpha0']))
        star_excl.append(dict(target=t, expr=e))
    # files
    write_scores_csv(rows, os.path.join(args.out, 'fork_scores.csv'), alph_id)
    write_sweep_csv(sw, os.path.join(args.out, 'fork_alpha_sweep.csv'))
    summary = dict(provenance=prov, verbatim=vb, replay=eq, pred_star_PRED_floats=pred_star, star_mpmath_floats=star_mpfloats_vs_pred,
                   Hstar=S(Hstar), La=La, final=final, flip=flip, numerics_ok=bool(numerics_ok),
                   EV={k: {kk: (vv if not isinstance(vv, dict) else {str(a): (int(b) if hasattr(b, 'item') else b) for a, b in vv.items()})
                           for kk, vv in v.items()} for k, v in EV.items()},
                   conv={k: {kk: v[kk] for kk in ('PR_C', 'PR_C01', 'verdicts', 'n_onestep', 'excl_star', 'bands')} for k, v in conv.items()},
                   f1f3_rank=f1f3_rank, n_onestep=len(onestep), n_f1f3=len(f1f3), n_general=len(general),
                   n_rows_onestep_literal=len(onestep_P1), clues=clues, star_excl=star_excl,
                   runtime_s=round(time.time() - t_start), maxrss_GB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6)
    with open(os.path.join(args.out, 'fork_summary.json'), 'w') as f: json.dump(summary, f, indent=1, default=str)
    write_map(G, rows, sw, Hstar, alph_id, os.path.join(args.out, 'fork_map.md'))
    write_tables(summary, EV, conv, rows, onestep, f1f3, general, sw, alph_id, os.path.join(args.out, 'fork_tables.md'))
    import pickle
    with open(os.path.join(args.out, 'fork_state.pkl'), 'wb') as f:
        pickle.dump(dict(rows=rows, G={k: v for k, v in G.items()}, sw=sw, EV=EV, conv=conv, alph_id=alph_id,
                         onestep=[r['row_id'] for r in onestep], f1f3=[r['row_id'] for r in f1f3],
                         general=[r['row_id'] for r in general], summary=summary), f)
    with open(os.path.join(args.out, 'run_log.txt'), 'w') as f: f.write('\n'.join(LOG) + '\n')
    log('FINAL', final, 'runtime', summary['runtime_s'], 's')

if __name__ == '__main__':
    main()
