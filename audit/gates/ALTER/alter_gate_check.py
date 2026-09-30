#!/usr/bin/env python3
"""
Gate ALTER -- terminal check script (Cold Ledger, fresh context).

Part A: four obstruction checks of card section 3.2, in exact arithmetic
        (fractions.Fraction, plus a minimal exact Q(sqrt2) type for the BCT frame).
Part B: corpus search of card section 3.3 over the corpus tree as of the last
        commit dated on or before 2026-09-30 (0d9600a), excluding audit/ (ledger
        and prior gate results are out of bounds for a Cold Ledger run).

Usage:  python3 alter_gate_check.py [--repo PATH] [--rev 0d9600a] [--skip-corpus]
Written independently; audit/gates/alter_check.py was deliberately not read.
"""
import argparse, itertools, os, re, subprocess, sys, tempfile, zipfile, hashlib
from fractions import Fraction as F
from collections import defaultdict

# --------------------------------------------------------------------------
# Exact Q(sqrt2): numbers a + b*sqrt2 with a, b rational.
# --------------------------------------------------------------------------
class Q2:
    __slots__ = ("a", "b")
    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)
    def _c(self, o): return o if isinstance(o, Q2) else Q2(o)
    def __add__(self, o): o = self._c(o); return Q2(self.a + o.a, self.b + o.b)
    __radd__ = __add__
    def __neg__(self): return Q2(-self.a, -self.b)
    def __sub__(self, o): return self + (-self._c(o))
    def __rsub__(self, o): return self._c(o) - self
    def __mul__(self, o):
        o = self._c(o)
        return Q2(self.a*o.a + 2*self.b*o.b, self.a*o.b + self.b*o.a)
    __rmul__ = __mul__
    def __truediv__(self, o):
        o = self._c(o); n = o.a*o.a - 2*o.b*o.b
        return self * Q2(o.a/n, -o.b/n)
    def __eq__(self, o): o = self._c(o); return self.a == o.a and self.b == o.b
    def __hash__(self): return hash((self.a, self.b))
    def __repr__(self): return f"{self.a}+{self.b}*r2" if self.b else f"{self.a}"

R2 = Q2(0, 1)
half = F(1, 2)

def vec(*xs): return tuple(Q2(x) if not isinstance(x, Q2) else x for x in xs)
def vadd(u, v): return tuple(a + b for a, b in zip(u, v))
def vsub(u, v): return tuple(a - b for a, b in zip(u, v))
def vneg(u): return tuple(-a for a in u)
def dot(u, v): return sum((a*b for a, b in zip(u, v)), Q2(0))

def is_int_combo_fcc_cubic(v):
    """v in cubic frame (cube edge 1, rational). FCC lattice = integer points
    of (Z/2)^3 with even coordinate sum after doubling."""
    w = [2*x for x in v]
    if any(x.denominator != 1 for x in w): return False
    return sum(int(x) for x in w) % 2 == 0

def cubic_from_bct(v):
    """Exact linear map from the BCT frame (a=1, c=sqrt2) to the cubic FCC frame (cube
    edge 1): 45-degree rotation about z composed with scale 1/sqrt2. Returns a rational
    triple, or None if a sqrt2 part survives (i.e. the vector is not rational cubic)."""
    x, y, z = v
    # BCT a1=(1,0,0) -> cubic (1/2, 1/2, 0); a2=(0,1,0) -> (1/2,-1/2,0); c=(0,0,sqrt2) -> (0,0,1)
    xc = (x + y) * half
    yc = (x - y) * half
    zc = z / R2
    out = []
    for q in (xc, yc, zc):
        if q.b != 0: return None
        out.append(q.a)
    return tuple(out)

def check(name, cond, detail=""):
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"  -- {detail}" if detail else ""))
    return cond

# --------------------------------------------------------------------------
# Part A
# --------------------------------------------------------------------------
def part_a():
    ok = True
    print("=" * 78)
    print("PART A -- obstruction checks (card section 3.2), exact arithmetic")
    print("=" * 78)

    # ---- A1: body-centring vector at c/a = sqrt2 is an FCC lattice vector
    print("\nA1. BCT body-centring vector at c/a = sqrt2 is an FCC lattice vector")
    a1, a2, c = vec(1, 0, 0), vec(0, 1, 0), (Q2(0), Q2(0), R2)
    b = (Q2(half), Q2(half), R2 * half)            # corner -> body-centre
    # (i) the map to the cubic frame is an orthogonal similarity (metric check)
    basis = [a1, a2, c]
    img = [cubic_from_bct(v) for v in basis]
    ok &= check("BCT basis maps to rational cubic vectors", all(i is not None for i in img), str(img))
    G_bct = [[dot(u, v) for v in basis] for u in basis]
    G_cub = [[sum(p*q for p, q in zip(u, v)) for v in img] for u in img]
    ratio = G_bct[0][0] / Q2(G_cub[0][0])
    sim = all(G_bct[i][j] == ratio * Q2(G_cub[i][j]) for i in range(3) for j in range(3))
    ok &= check("metric preserved up to one global scale (similarity)", sim, f"scale^2 = {ratio}")
    bc = cubic_from_bct(b)
    ok &= check("body-centring vector in cubic frame", bc is not None, str(bc))
    ok &= check("body-centring vector is an FCC lattice vector", is_int_combo_fcc_cubic(bc))
    # (ii) independent: 12 equal nearest neighbours, Bravais (b is a primitive translation)
    pts = []
    for i, j, k in itertools.product(range(-2, 3), repeat=3):
        base = vadd(vadd(tuple(Q2(i)*x for x in a1), tuple(Q2(j)*x for x in a2)), tuple(Q2(k)*x for x in c))
        pts += [base, vadd(base, b)]
    d2 = sorted({dot(p, p) for p in pts if dot(p, p) != Q2(0)}, key=lambda q: float(q.a) + float(q.b) * 2**0.5)
    nn = d2[0]
    cnt = sum(1 for p in pts if dot(p, p) == nn)
    ok &= check("coordination at nearest distance = 12 (FCC), all equal", cnt == 12, f"|r|^2 = {nn}, count {cnt}")
    # control: at c/a != sqrt2 the body-centre is NOT at the corner-corner distance
    cc = Q2(F(3, 2))
    bb = (Q2(half), Q2(half), cc * half)
    ok &= check("control c/a=3/2: body-centre NOT at the in-plane corner distance (not FCC)", dot(bb, bb) != dot(a1, a1), f"|b|^2 = {dot(bb, bb)}")

    # ---- work in cubic frame from here (cube edge 1), all rational
    fcc = [(F(0), F(0), F(0)), (half, half, F(0)), (half, F(0), half), (F(0), half, half)]
    def mod1(v): return tuple(x % 1 for x in v)
    def cset(basis_pts, shift=(0, 0, 0)): return {mod1(tuple(p + s for p, s in zip(q, shift))) for q in basis_pts}
    S = cset(fcc)

    # ---- A2: oct voids form an FCC translate of sphere sites
    print("\nA2. Octahedral voids form an FCC translate of the sphere sites")
    O = cset(fcc, (half, 0, 0))
    ok &= check("oct set = sphere set + (1/2,0,0) = sphere set + (1/2,1/2,1/2)", O == cset(fcc, (half, half, half)), f"{sorted(O)}")
    ok &= check("oct set closed under every FCC translation",
                all(cset(list(O), t) == O for t in fcc))
    # each oct site has exactly 6 sphere neighbours at distance 1/2 (octahedral)
    def neighbours(p, targets, r2):
        n = 0
        for t in targets:
            for sh in itertools.product((-1, 0, 1), repeat=3):
                d = tuple(t[i] + sh[i] - p[i] for i in range(3))
                if sum(x*x for x in d) == r2: n += 1
        return n
    ok &= check("each oct site has 6 sphere NN at |r|=1/2", all(neighbours(p, S, F(1, 4)) == 6 for p in O))
    ok &= check("oct set != sphere set (distinct sites)", O.isdisjoint(S))

    # ---- A3: tet voids related by inversion, not translation
    print("\nA3. Tet voids (1/4,1/4,1/4) and (3/4,3/4,3/4): inversion, not translation")
    q, tq = F(1, 4), F(3, 4)
    Tp = cset(fcc, (q, q, q)); Tm = cset(fcc, (tq, tq, tq))
    ok &= check("T+ and T- disjoint", Tp.isdisjoint(Tm))
    ok &= check("each tet site has 4 sphere NN at |r|^2=3/16",
                all(neighbours(p, S, F(3, 16)) == 4 for p in Tp | Tm))
    diff = (half, half, half)
    ok &= check("T- - T+ = (1/2,1/2,1/2) is NOT an FCC lattice vector", not is_int_combo_fcc_cubic(diff))
    ok &= check("no sphere-lattice translation maps T+ onto T-",
                all(cset(list(Tp), t) != Tm for t in fcc))
    inv = lambda v: tuple(-x for x in v)
    ok &= check("inversion through a sphere site preserves sphere set", {mod1(inv(p)) for p in S} == S)
    ok &= check("inversion through a sphere site maps T+ onto T-", {mod1(inv(p)) for p in Tp} == Tm)
    # also: C4z about a sphere site maps T+ -> T- (proper rotation also relates them; irrelevant to
    # the altermagnet criterion because the voids alone carry no orientation -- recorded, not used)
    ok &= check("[info] each tet class is invariant under all FCC translations",
                all(cset(list(Tp), t) == Tp and cset(list(Tm), t) == Tm for t in fcc))

    # ---- A4: rutile
    print("\nA4. Rutile: body-centring translation fails on O, 4_2 screw {C4z|1/2,1/2,1/2} succeeds")
    # coordinates as affine functions of u: (const, coeff) per component
    def P(*comps): return tuple((F(a), F(b)) for a, b in comps)
    M_A, M_B = P((0, 0), (0, 0), (0, 0)), P((half, 0), (half, 0), (half, 0))
    Oset = [P((0, 1), (0, 1), (0, 0)), P((0, -1), (0, -1), (0, 0)),
            P((half, 1), (half, -1), (half, 0)), P((half, -1), (half, 1), (half, 0))]
    def translate(p, t): return tuple((a + F(ti), bb) for (a, bb), ti in zip(p, t))
    def C4z(p): (xa, xb), (ya, yb), (za, zb) = p; return ((-ya, -yb), (xa, xb), (za, zb))
    def screw(p): return translate(C4z(p), (half, half, half))
    def coincide_open(p, qq):
        """Return set of u in (0,1/2) where p == q mod 1 (per component), or 'ALL'.
        Component a1+b1 u == a2+b2 u (mod 1). If b1==b2: holds for all u iff a1-a2 in Z,
        else never. If b1 != b2: u = (a2-a1+n)/(b1-b2) for integer n -> finite set in (0,1/2)."""
        sols = "ALL"
        for (a1_, b1_), (a2_, b2_) in zip(p, qq):
            if b1_ == b2_:
                if (a1_ - a2_) % 1 != 0: return set()
                continue
            cand = set()
            db = b1_ - b2_
            for n in range(-4, 5):
                u = (a2_ - a1_ + n) / db
                if 0 < u < half: cand.add(u)
            sols = cand if sols == "ALL" else (sols & cand)
            if not sols: return set()
        return sols
    def maps_set(op, src, dst):
        """True iff op maps src onto dst for EVERY u in (0,1/2) (identically in u)."""
        return all(any(coincide_open(op(p), qq) == "ALL" for qq in dst) for p in src)
    def failing_u(op, src, dst):
        """For each image op(p) with no identical match, the finite u-set where it
        happens to coincide with some member of dst."""
        out = []
        for p in src:
            if any(coincide_open(op(p), qq) == "ALL" for qq in dst): continue
            hits = set()
            for qq in dst:
                s = coincide_open(op(p), qq)
                if s != "ALL": hits |= s
            out.append(hits)
        return out
    tb = lambda p: translate(p, (half, half, half))
    ok &= check("body-centring maps metal A -> metal B", maps_set(tb, [M_A], [M_B]))
    tb_ok = maps_set(tb, Oset, Oset)
    fu = failing_u(tb, Oset, Oset)
    ok &= check("body-centring does NOT map O set to itself (any 0<u<1/2)",
                (not tb_ok) and all(len(h) == 0 for h in fu),
                f"accidental-coincidence u values inside (0,1/2): {[sorted(h) for h in fu]}")
    ok &= check("4_2 screw maps metal A -> metal B", maps_set(screw, [M_A], [M_B]))
    ok &= check("4_2 screw maps metal B -> metal A", maps_set(screw, [M_B], [M_A]))
    ok &= check("4_2 screw maps O set onto itself, identically in u", maps_set(screw, Oset, Oset))
    inv_r = lambda p: tuple((-a, -bb) for a, bb in p)
    ok &= check("[info] inversion at metal A fixes each metal sublattice (does not swap)",
                maps_set(inv_r, [M_A], [M_A]) and maps_set(inv_r, [M_B], [M_B]))
    # rational spot checks
    for uv in (F(3, 10), F(1, 7), F(2, 5)):
        ev = lambda p: tuple((a + bb*uv) % 1 for a, bb in p)
        Os = {ev(p) for p in Oset}
        t_ok = {ev(tb(p)) for p in Oset} == Os
        s_ok = {ev(screw(p)) for p in Oset} == Os
        ok &= check(f"spot u={uv}: translation fails, screw succeeds", (not t_ok) and s_ok)

    print(f"\nPART A overall: {'ALL FOUR CHECKS PASS' if ok else 'FAILURE -> SC-ALTER-4'}")
    return ok

# --------------------------------------------------------------------------
# Part B: corpus search
# --------------------------------------------------------------------------
TERMS = [
    ("orient",     r"orient"),
    ("rotat",      r"rotat"),
    ("stagger",    r"stagger"),
    ("sublattice", r"sub-?lattice"),
    ("alternat",   r"alternat"),
    ("chiral",     r"chiral"),
    ("handed",     r"handed"),
    ("screw",      r"screw"),
    ("glide",      r"glide"),
    ("4_2",        r"4_\{?2\}?|4₂"),
    ("P4_2",       r"P\s*4_\{?2\}?|P4₂"),
    ("D_{4h}",     r"D_\{4h\}|D_\{4\\?,?h\}"),
    ("D4h",        r"D4h|D₄h|D_4h|D_4\{h\}"),
    ("decorat",    r"decorat"),
    ("occupan",    r"occupan"),
]
PROX = [  # (label, anchor, partner-regex, window)
    ("void ±3 of any above", r"void", "|".join(f"(?:{r})" for _, r in TERMS), 3),
    ("hopfion ±3 of sign/±/handed", r"hopfion", r"\bsign|±|\\pm|handed", 3),
    ("winding ±3 of pattern/arrang", r"winding", r"pattern|arrang", 3),
]

def git_tree_files(repo, rev):
    out = subprocess.run(["git", "-C", repo, "ls-tree", "-r", "--name-only", rev],
                         capture_output=True, text=True, check=True).stdout.split("\n")
    return [f for f in out if f and not f.startswith("audit/")]

def blob(repo, rev, path):
    return subprocess.run(["git", "-C", repo, "show", f"{rev}:{path}"], capture_output=True, check=True).stdout

def pdf_text(data):
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as fh:
        fh.write(data); name = fh.name
    try:
        r = subprocess.run(["pdftotext", "-layout", name, "-"], capture_output=True)
        return r.stdout.decode("utf-8", "replace")
    finally:
        os.unlink(name)

def load_corpus(repo, rev):
    docs = {}   # name -> (tier, text)
    for f in git_tree_files(repo, rev):
        low = f.lower()
        if low.endswith(".tex"):
            docs[f] = ("primary", blob(repo, rev, f).decode("utf-8", "replace"))
        elif low.endswith(".pdf"):
            docs[f] = ("primary", pdf_text(blob(repo, rev, f)))
        elif low.endswith(".zip"):
            with tempfile.NamedTemporaryFile(suffix=".zip", delete=False) as fh:
                fh.write(blob(repo, rev, f)); zname = fh.name
            with zipfile.ZipFile(zname) as z:
                for n in z.namelist():
                    if n.lower().endswith(".pdf") and "__MACOSX" not in n:
                        docs[f"{f}::{n}"] = ("primary", pdf_text(z.read(n)))
            os.unlink(zname)
        elif low.endswith((".md", ".txt")):
            docs[f] = ("secondary", blob(repo, rev, f).decode("utf-8", "replace"))
    return docs

def search(docs, ctx_path):
    table = {}
    ctx = open(ctx_path, "w")
    for tier in ("primary", "secondary"):
        for label, rx in TERMS:
            pat = re.compile(rx, re.I if label not in ("4_2", "P4_2", "D_{4h}", "D4h") else 0)
            hits, files = 0, defaultdict(int)
            for name, (t, text) in docs.items():
                if t != tier: continue
                lines = text.split("\n")
                for i, ln in enumerate(lines):
                    if pat.search(ln):
                        hits += 1; files[name] += 1
                        ctx.write(f"### [{tier}] {label} | {name}:{i+1}\n")
                        ctx.write("\n".join(lines[max(0, i-3):i+4]) + "\n\n")
            table[(tier, label)] = (hits, dict(files))
        for label, anchor, partner, w in PROX:
            pa, pp = re.compile(anchor, re.I), re.compile(partner, re.I)
            hits, files = 0, defaultdict(int)
            for name, (t, text) in docs.items():
                if t != tier: continue
                lines = text.split("\n")
                for i, ln in enumerate(lines):
                    if pa.search(ln):
                        win = lines[max(0, i-w):i+w+1]
                        if any(pp.search(x) for x in win):
                            hits += 1; files[name] += 1
                            ctx.write(f"### [{tier}] {label} | {name}:{i+1}\n")
                            ctx.write("\n".join(win) + "\n\n")
            table[(tier, label)] = (hits, dict(files))
    ctx.close()
    return table

def part_b(repo, rev, outdir):
    print("\n" + "=" * 78)
    print(f"PART B -- corpus search (card section 3.3) at rev {rev}, audit/ excluded")
    print("=" * 78)
    docs = load_corpus(repo, rev)
    n_p = sum(1 for t, _ in docs.values() if t == "primary")
    n_s = len(docs) - n_p
    empty = [n for n, (t, x) in docs.items() if t == "primary" and len(x.strip()) < 200]
    print(f"documents: primary (.tex + PDF, incl. zipped Volume) = {n_p}; secondary (.md/.txt) = {n_s}")
    print(f"primary docs with <200 chars extractable text: {empty or 'none'}")
    ctx_path = os.path.join(outdir, "alter_search_context.txt")
    table = search(docs, ctx_path)
    for tier in ("primary", "secondary"):
        print(f"\n-- {tier} --")
        print(f"{'term':32s} {'hits':>6s}  files")
        for (t, label), (h, files) in table.items():
            if t != tier: continue
            fl = ", ".join(f"{os.path.basename(k)}({v})" for k, v in sorted(files.items(), key=lambda kv: -kv[1])[:6])
            more = f" +{len(files)-6} more" if len(files) > 6 else ""
            print(f"{label:32s} {h:6d}  {fl}{more}" if h else f"{label:32s} {h:6d}  ABSENT")
    print(f"\nfull hit contexts written to {ctx_path}")
    return table, docs

# --------------------------------------------------------------------------
# Part C: candidate test (card section 3.4)
# Cubic FCC frame, cube edge 1. BCT frame (a=1, c=sqrt2) maps here by A1's
# similarity: BCT corners A = FCC points with z in Z; BCT body-centres B = FCC
# points with z in Z+1/2 (alternating (001) layers). Body-centring b=(1/2,0,1/2).
# --------------------------------------------------------------------------
def signed_perms():
    mats = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            M = [[0]*3 for _ in range(3)]
            for i in range(3): M[i][perm[i]] = signs[i]
            mats.append(tuple(tuple(r) for r in M))
    return mats

def mat_vec(M, v): return tuple(sum(F(M[i][j]) * v[j] for j in range(3)) for i in range(3))
def mat_mul(M, N): return tuple(tuple(sum(M[i][k]*N[k][j] for k in range(3)) for j in range(3)) for i in range(3))
def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1]) - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
            + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
I3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))

def in_A_lattice(v):
    """A lattice (translation group of the partition): basis (1/2,1/2,0),(1/2,-1/2,0),(0,0,1)."""
    x, y, z = v
    if z.denominator != 1: return False
    return (x + y).denominator == 1 and (x - y).denominator == 1

def classify(R, t):
    d = det3(R)
    if R == I3: return "translation"
    if R == tuple(tuple(-x for x in r) for r in I3): return "inversion"
    n, P = 1, R
    while P != I3: P = mat_mul(P, R); n += 1
    acc, P = (F(0),)*3, I3
    for _ in range(n):
        acc = tuple(a + b for a, b in zip(acc, mat_vec(P, t))); P = mat_mul(P, R)
    w = tuple(a / n for a in acc)
    tr = R[0][0] + R[1][1] + R[2][2]
    intrinsic = not in_A_lattice(w)
    if d == 1: return f"{n}-fold {'screw' if intrinsic else 'rotation'}"
    if n == 2:  # improper, order 2, not -I  -> reflection
        return "glide" if intrinsic else "mirror"
    return f"-{n if n != 6 else 3} rotoinversion"

def part_c():
    print("\n" + "=" * 78)
    print("PART C -- candidate patterns (card section 3.4)")
    print("=" * 78)
    ok = True
    # cell reps mod the cubic cell (the A lattice contains (1,0,0),(0,1,0),(0,0,1))
    A = [(F(0), F(0), F(0)), (half, half, F(0))]
    B = [(half, F(0), half), (F(0), half, half)]
    m1 = lambda v: tuple(x % 1 for x in v)
    q4 = [F(k, 4) for k in range(4)]
    Ts = list(itertools.product(q4, repeat=3))
    ops = [(R, t) for R in signed_perms() for t in Ts]

    # observation: at c/a = sqrt2 the A/B partition is NOT a nearest-neighbour bipartition
    def nn_count(src, dst):
        c = 0
        for q in dst:
            for sh in itertools.product((-1, 0, 1), repeat=3):
                d = tuple(q[i] + sh[i] - src[i] for i in range(3))
                if sum(x*x for x in d) == half: c += 1
        return c
    aa, ab = nn_count(A[0], A), nn_count(A[0], B)
    check("[obs] NN of a corner site at c/a=sqrt2: A-A and A-B counts", True, f"A-A = {aa}, A-B = {ab}, total {aa+ab}")

    def symmetric_ops(label_of, label_rule):
        """label_of: dict site->label for reps; label_rule(R, lab) -> transformed label.
        Return list of (R,t,swaps) that preserve sites and labels."""
        sites = {m1(p): lab for p, lab in label_of.items()}
        out = []
        for R, t in ops:
            good, swaps = True, None
            for p, lab in sites.items():
                q = m1(tuple(a + b for a, b in zip(mat_vec(R, p), t)))
                if q not in sites or sites[q] != label_rule(R, lab): good = False; break
            if good:
                pa = m1(tuple(a + b for a, b in zip(mat_vec(R, A[0]), t)))
                out.append((R, t, pa in [m1(x) for x in B]))
        return out

    def summarise(name, syms):
        swap = [(R, t) for R, t, s in syms if s]
        keep = [(R, t) for R, t, s in syms if not s]
        # quotient by A-lattice translations: t already reduced mod cubic cell; reduce further
        def key(R, t): return (R, tuple(sorted(m1(tuple(t[i] + d[i] for i in range(3)))
                                            for d in [(0, 0, 0), (half, half, 0)])))
        sw = {key(R, t): (R, t) for R, t in swap}; kp = {key(R, t): (R, t) for R, t in keep}
        from collections import Counter
        cs, ck = Counter(classify(R, t) for R, t in sw.values()), Counter(classify(R, t) for R, t in kp.values())
        print(f"\n  {name}")
        print(f"    coset ops mod A-lattice: A->A {len(kp)}  |  A->B {len(sw)}")
        print(f"    A->A types: {dict(ck)}")
        print(f"    A->B types: {dict(cs)}")
        return kp, sw, cs

    # C0 control: bare sphere lattice (no decoration)
    kp, sw, cs = summarise("C0 control: bare FCC sphere sites, no decoration",
                           symmetric_ops({**{p: 0 for p in A}, **{p: 0 for p in B}}, lambda R, l: l))
    ok &= check("C0 A->B contains a pure translation (theorem, sec 0)", cs.get("translation", 0) > 0)

    # C1: App L sec 4.3 -- right-handed Weyl component on A, left-handed on B.
    # Handedness is a pseudoscalar: it flips under improper operations.
    lab = {**{p: +1 for p in A}, **{p: -1 for p in B}}
    kp, sw, cs = summarise("C1: App L sec 4.3 (R on A, L on B), handedness as pseudoscalar",
                           symmetric_ops(lab, lambda R, l: l * det3(R)))
    ok &= check("C1 A->A subgroup is proper-only (chiral point group 422)",
                all(det3(R) == 1 for R, t in kp.values()) and len(kp) == 8)
    ok &= check("C1 no pure translation maps A->B", cs.get("translation", 0) == 0)
    ok &= check("C1 an INVERSION maps A->B (degenerate by card classification)", cs.get("inversion", 0) > 0)
    inv = [t for R, t in sw.values() if classify(R, t) == "inversion"][0]
    print(f"    inversion op: x -> -x + {tuple(str(x) for x in inv)}, centre at {tuple(str(x/2) for x in inv)} (A-B bond midpoint)")
    # space-group identification: P4/nnc (No.126), origin choice 1, tetragonal axes
    # a'=(1/2,1/2,0), b'=(1/2,-1/2,0), c'=(0,0,1): verify the coset structure matches:
    # 422 at origin, inversion at (1/4,1/4,1/4)' , n-glide perp c, n-glide perp a', c-glide perp [110]'
    to_t = lambda v: (v[0] + v[1], v[0] - v[1], v[2])        # cubic -> tetragonal fractional
    inv_t = m1(tuple(x / 2 for x in to_t(inv)))
    ok &= check("C1 inversion centre at (1/4,1/4,1/4) in tetragonal axes, 422 at origin -> P4/nnc (No.126, origin 1)",
                inv_t == (F(1, 4), F(1, 4), F(1, 4)) and len(kp) + len(sw) == 16, str(tuple(str(x) for x in inv_t)))
    # C1' : alternative reading -- treat handedness as the staggered (spin-like) quantity; then the
    # structure it lives on is C0 (bare FCC), where a translation relates A and B.
    print("    C1' (handedness read as the spin-like label): parent structure = C0 -> A->B by translation")

    # C1'': same labels as a plain scalar (no flip under improper ops) -> A and B are different species
    kp2, sw2, cs2 = summarise("C1'': same pattern, labels as scalars (control; L1_0 / CuAu-type)",
                              symmetric_ops(lab, lambda R, l: l))
    ok &= check("C1'' no op maps A->B (distinct species; P4/mmm, 16 ops)", len(sw2) == 0 and len(kp2) == 16)

    # C2 control: Letter 127 -- every oct void carries the same z-axis director (headless).
    # Oct voids: FCC + (1/2,0,0). Director along z is invariant iff R maps z-axis to +-z.
    octs = [m1(tuple(p[i] + (half, F(0), F(0))[i] for i in range(3))) for p in A + B]
    zkeep = lambda R: abs(R[2][2]) == 1
    sites2 = {**{m1(p): "A" for p in A}, **{m1(p): "B" for p in B}, **{o: "oct" for o in octs}}
    syms = []
    for R, t in ops:
        if not zkeep(R): continue
        good = True
        for p, l in sites2.items():
            q = m1(tuple(a + b for a, b in zip(mat_vec(R, p), t)))
            if q not in sites2 or (sites2[q] == "oct") != (l == "oct"): good = False; break
        if good:
            pa = m1(tuple(a + b for a, b in zip(mat_vec(R, A[0]), t)))
            syms.append((R, t, pa in [m1(x) for x in B]))
    kp3, sw3, cs3 = summarise("C2 control: Letter 127 oct-void z-director, uniform on every oct void", syms)
    ok &= check("C2 A->B contains a pure translation (uniform => sublattice-symmetric)", cs3.get("translation", 0) > 0)
    print(f"\nPART C overall: {'checks as expected' if ok else 'UNEXPECTED RESULT'}")
    return ok

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))
    ap.add_argument("--rev", default="0d9600a")
    ap.add_argument("--skip-corpus", action="store_true")
    ap.add_argument("--outdir", default=".")
    a = ap.parse_args()
    okA = part_a()
    if not okA:
        print("STOP: obstruction check failed -> SC-ALTER-4"); sys.exit(2)
    okC = part_c()
    if not a.skip_corpus:
        part_b(a.repo, a.rev, a.outdir)
