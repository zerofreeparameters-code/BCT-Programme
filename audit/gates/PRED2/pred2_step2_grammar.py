"""Gate PRED2 Step 1 - the grammar. Written and run BEFORE any target is scored.
Atoms and operations taken only from those the census (step 1) shows the corpus using.
Complexity = node count of the expression tree (atom=1; unary adds 1; binary adds 1)."""
import math, random, json, sys
random.seed(20260914)  # grammar v2: trig added because the census shows the corpus using acos, tan, cos

a0    = ((math.sqrt(2)-1)/2)*((math.sqrt(6)-2)/4)/math.pi
ATOMS = {
 '1':1.0,'2':2.0,'3':3.0,'4':4.0,'6':6.0,'8':8.0,'12':12.0,'24':24.0,'48':48.0,
 'pi':math.pi,'sqrt2':math.sqrt(2),'sqrt3':math.sqrt(3),'sqrt6':math.sqrt(6),'e':math.e,
 'a0':a0,'r_tet':(math.sqrt(6)-2)/4,'r_oct':(math.sqrt(2)-1)/2,'R':0.5,
 'S_D4':math.pi**5/6,'x_lep':4*a0/math.pi,
}
AV = list(ATOMS.values())
LIM = 1e60
def _p(x,n):
    try:
        v = x**n
        return v if abs(v)<LIM else None
    except (OverflowError,ZeroDivisionError,ValueError): return None
UN = []
UN.append(('sqrt', lambda x: math.sqrt(x) if x>=0 else None))
for n in (2,3,4,5): UN.append((f'^{n}',  (lambda n: lambda x: _p(x,n))(n)))
for n in (1,2,3,4,5): UN.append((f'^-{n}',(lambda n: lambda x: _p(x,-n) if x!=0 else None)(n)))
UN.append(('exp', lambda x: math.exp(x) if -700<x<130 else None))
UN.append(('ln',  lambda x: math.log(x) if x>0 else None))
UN.append(('1/(1-x)', lambda x: 1.0/(1-x) if abs(1-x)>1e-12 else None))
UN.append(('cos', lambda x: math.cos(x) if abs(x)<1e6 else None))
UN.append(('tan', lambda x: (lambda t: t if abs(t)<1e12 else None)(math.tan(x)) if abs(x)<1e6 else None))
UN.append(('acos',lambda x: math.acos(x) if -1<=x<=1 else None))
UN.append(('atan',lambda x: math.atan(x)))
BIN = [('+',lambda a,b:a+b), ('-',lambda a,b:a-b), ('*',lambda a,b:a*b if abs(a*b)<LIM else None),
       ('/',lambda a,b:a/b if b!=0 and abs(a/b)<LIM else None)]
NA, NU, NB = len(AV), len(UN), len(BIN)

# ---- exact expression counts N(C) (structural; before value-dedup) ----
CMAX = 20
N = [0]*(CMAX+1); N[1] = NA
for C in range(2, CMAX+1):
    tot = NU*N[C-1]
    for i in range(1, C-1):
        tot += NB*N[i]*N[C-1-i]
    N[C] = tot

# ---- exhaustive enumeration of DISTINCT VALUES to C = CEX ----
CEX = 5
levels = [None, [v for v in AV]]
distinct = [0,0]
seen = set()
def key(v): return round(v, 12) if abs(v) < 1e-6 else float(f"{v:.12e}")
for v in levels[1]: seen.add(key(v))
distinct[1] = len(seen)
for C in range(2, CEX+1):
    out = []
    for _,f in UN:
        for v in levels[C-1]:
            r = f(v)
            if r is not None and abs(r) < LIM and not math.isnan(r): out.append(r)
    for i in range(1, C-1):
        for _,g in BIN:
            for a in levels[i]:
                for b in levels[C-1-i]:
                    r = g(a,b)
                    if r is not None and not math.isnan(r): out.append(r)
    levels.append(out)
    s = set(key(v) for v in out)
    distinct.append(len(s))
    print(f"C={C}: generated {len(out)} values, {len(s)} distinct at 12 s.f.", file=sys.stderr)

# ---- uniform sampling of expressions of exactly complexity C, for C > CEX ----
def sample(C):
    if C == 1: return random.choice(AV)
    w = [NU*N[C-1]] + [NB*N[i]*N[C-1-i] for i in range(1, C-1)]
    tot = sum(w); r = random.random()*tot; acc = 0
    for idx, wi in enumerate(w):
        acc += wi
        if r <= acc:
            if idx == 0:
                v = sample(C-1)
                return None if v is None else UN[random.randrange(NU)][1](v)
            i = idx
            a, b = sample(i), sample(C-1-i)
            if a is None or b is None: return None
            return BIN[random.randrange(NB)][1](a,b)
    return None

if __name__ == '__main__':
    M = int(sys.argv[1]) if len(sys.argv)>1 else 400000
    print("N(C) = number of grammar expressions of complexity exactly C (structural count)")
    print(f"{'C':>3} {'N(C)':>18} {'distinct values (exhaustive)':>30}")
    for C in range(1, CMAX+1):
        d = f"{distinct[C]:,}" if C <= CEX else "(sampled - see below)"
        print(f"{C:>3} {N[C]:>18,} {d:>30}")
    # sampled distinct-fraction + value pool per complexity, saved for the scorer
    pools = {}
    for C in range(6, 13):
        vals = []
        for _ in range(M):
            v = sample(C)
            if v is not None and not math.isnan(v) and abs(v) < LIM and v != 0:
                vals.append(v)
        pools[C] = vals
        print(f"sampled C={C}: {len(vals)}/{M} finite; distinct {len(set(round(x,10) for x in vals)):,}", file=sys.stderr)
    import pickle
    pickle.dump({'N':N,'distinct':distinct,'levels_small':{c:levels[c] for c in range(1,CEX+1)},
                 'pools':pools,'M':M,'CEX':CEX}, open('grammar.pkl','wb'))
