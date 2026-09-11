#!/usr/bin/env python3
"""
LOAD-BEARING QUESTION: are the BCT exact identities physics, or algebra?

Method, in two parts.

PART 1 (algebraic, decisive).  Reduce each claimed identity and see whether
they are independent facts.

PART 2 (statistical, quantitative).  Build a control population of quadratic
surds of comparable complexity to r_oct and r_tet, run the SAME identity
hunt over all of them, and ask where BCT's two sit in that distribution.
If a typical surd yields as many clean identities, BCT's yield no evidence.

Scoring follows Gate STAT: surprise in bits = -log2(P(hit by chance)).
"""
from fractions import Fraction
import math, itertools, collections

# ---------- exact arithmetic in Q(sqrt(D)) : a + b*sqrt(D) ----------
class S:
    __slots__ = ('a', 'b', 'D')
    def __init__(s, a, b, D): s.a, s.b, s.D = Fraction(a), Fraction(b), D
    def __add__(s, o): o = s._c(o); return S(s.a + o.a, s.b + o.b, s.D)
    def __sub__(s, o): o = s._c(o); return S(s.a - o.a, s.b - o.b, s.D)
    def __mul__(s, o):
        o = s._c(o); return S(s.a * o.a + s.b * o.b * s.D, s.a * o.b + s.b * o.a, s.D)
    def __truediv__(s, o):
        o = s._c(o); d = o.a * o.a - o.b * o.b * s.D
        if d == 0: raise ZeroDivisionError
        return S((s.a * o.a - s.b * o.b * s.D) / d, (s.b * o.a - s.a * o.b) / d, s.D)
    def _c(s, o): return o if isinstance(o, S) else S(o, 0, s.D)
    def rational(s): return s.b == 0
    def val(s): return s.a  # only call when rational()

def simple(fr, maxden=64):
    """is this a 'clean' rational?  small denominator, small numerator."""
    return fr.denominator <= maxden and abs(fr.numerator) <= 64

# ---------- the identity hunt, applied uniformly ----------
def hunt(r):
    """Return the set of simple-expression LABELS that land on a clean rational."""
    hits = set()
    one = S(1, 0, r.D)
    forms = {
        'r(1+r)':      lambda x: x * (one + x),
        'r(1-r)':      lambda x: x * (one - x),
        'r(2+r)':      lambda x: x * (S(2,0,x.D) + x),
        'r^2':         lambda x: x * x,
        'r^2+r':       lambda x: x * x + x,
        'r^2-r':       lambda x: x * x - x,
        '1-r-r^2':     lambda x: one - x - x * x,
        '1/r':         lambda x: one / x,
        '1/r - r':     lambda x: one / x - x,
        '1/r + r':     lambda x: one / x + x,
        'r/(1-r)':     lambda x: x / (one - x),
        'r/(1+r)':     lambda x: x / (one + x),
        '(1-r)/(1+r)': lambda x: (one - x) / (one + x),
        'r^3':         lambda x: x * x * x,
        'r^2(1+r)':    lambda x: x * x * (one + x),
        '4r^2+4r':     lambda x: S(4,0,x.D) * (x * x + x),
    }
    for lbl, f in forms.items():
        try:
            v = f(r)
        except ZeroDivisionError:
            continue
        if v.rational() and simple(v.val()):
            hits.add(lbl)
    return hits

# ---------- control population ----------
# surds of the same shape and complexity as BCT's: (sqrt(n) - m)/k
POP = []
for n in range(2, 40):
    if int(math.isqrt(n)) ** 2 == n:   # skip perfect squares (not irrational)
        continue
    for m in range(1, 7):
        for k in range(1, 9):
            r = S(Fraction(-m, k), Fraction(1, k), n)
            v = float(r.a) + float(r.b) * math.sqrt(n)
            if 0.01 < v < 0.99:        # plausible void inradius in units a=1
                POP.append(((n, m, k), r, v))

print("=" * 74)
print("CONTROL POPULATION")
print("=" * 74)
print(f"  surds of the form (sqrt(n) - m)/k with 2<=n<40, 1<=m<=6, 1<=k<=8,")
print(f"  restricted to 0.01 < value < 0.99  ->  {len(POP)} candidates")

BCT = {'r_oct': (2, 1, 2), 'r_tet': (6, 2, 4)}
counts = []
lookup = {}
for key, r, v in POP:
    h = hunt(r)
    counts.append(len(h))
    lookup[key] = (len(h), h, v)

dist = collections.Counter(counts)
print(f"\n  identity-hits per surd, distribution over the population:")
tot = len(POP)
cum = 0
for k in sorted(dist):
    cum += dist[k]
    print(f"     {k:2d} hits : {dist[k]:4d} surds ({100*dist[k]/tot:5.1f}%)   cumulative {100*cum/tot:5.1f}%")
mean = sum(counts) / tot
print(f"\n  mean hits per surd = {mean:.3f}")

print()
print("=" * 74)
print("WHERE DO BCT's TWO SIT?")
print("=" * 74)
for lbl, key in BCT.items():
    n_h, h, v = lookup[key]
    better = sum(1 for c in counts if c > n_h)
    equal = sum(1 for c in counts if c == n_h)
    pct = 100 * (better + equal) / tot
    print(f"\n  {lbl}  = (sqrt{key[0]} - {key[1]})/{key[2]} = {v:.9f}")
    print(f"    clean identities found: {n_h}")
    print(f"    surds in the population doing as well or better: {better+equal} of {tot}  ({pct:.1f}%)")
    print(f"    its hits: {sorted(h)}")

print()
print("=" * 74)
print("SURPRISE, IN BITS")
print("=" * 74)
print("""  P(a random surd from this population yields >= as many clean identities
  as r_oct does) -- and the same for r_tet.  Surprise = -log2(P).""")
for lbl, key in BCT.items():
    n_h, h, v = lookup[key]
    p = sum(1 for c in counts if c >= n_h) / tot
    bits = -math.log2(p) if p > 0 else float('inf')
    print(f"    {lbl:6s}  P = {p:.4f}   surprise = {bits:.3f} bits")

print("""
  For scale: 1 bit is a coin flip.  Gate STAT scored S_D4 = pi^5/6 at ZERO
  bits.  A result carrying real information would need tens of bits.
""")

print("=" * 74)
print("THE CONTROL THAT MATTERS MOST")
print("=" * 74)
print("""  Both BCT radii have the special form k = 2m:
      r_oct = (sqrt2 - 1)/2   n=2, m=1, k=2 = 2m
      r_tet = (sqrt6 - 2)/4   n=6, m=2, k=4 = 2m
  For ANY surd of that shape,  r(1+r) = (n - m^2)/(4m^2)  -- always rational,
  by the difference of squares.  So the headline identity is not a property
  of sphere packing at all; it is a property of writing a number as
  (sqrt(n) - m)/(2m).  Count how many of the population share that form:""")
k2m = [(key, lookup[key]) for key in lookup if key[2] == 2 * key[1]]
hits_k2m = [1 for key, (n_h, h, v) in k2m if 'r(1+r)' in h]
print(f"    surds with k = 2m in the population: {len(k2m)}")
print(f"    of those, how many satisfy 'r(1+r) = clean rational': {sum(hits_k2m)}")
print(f"    hit rate: {100*sum(hits_k2m)/max(len(k2m),1):.1f}%")
print("""
  If that rate is 100%, the identity carries exactly zero information about
  BCT geometry: it is true for every number of that form, chosen or not.
""")
