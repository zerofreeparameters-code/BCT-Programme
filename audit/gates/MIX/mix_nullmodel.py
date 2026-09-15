#!/usr/bin/env python3
# GATE MIX null model — deterministic. Grammar over {r_oct, r_tet, a0, ints 1..6},
# ops {+,-,*,/,sqrt,square,arccos,arcsin}. Honest look-elsewhere across ALL angles
# the BCT programme assigns a geometric formula to.
import itertools, math
from fractions import Fraction

# ---- canonical constants (from gate defs; reconstructed, not inherited) ----
r_oct = (math.sqrt(2)-1)/2
r_tet = (math.sqrt(6)-2)/4
a0    = r_oct*r_tet/math.pi
print(f"r_oct={r_oct:.9f}  r_tet={r_tet:.9f}  a0={a0:.9f}")

# ---- the four survivors: value, and MEASURED target with 1-sigma ----
# measured values: NuFIT-class neutrino, PDG electroweak/CKM
survivors = {
 'beta=arccos(2 r_oct)'      : dict(val=math.degrees(math.acos(2*r_oct)), obs=65.5, sig=3.5, unit='deg'),
 'sin2th13 = 3 a0'           : dict(val=3*a0,                              obs=0.02219, sig=0.0006, unit=''),
 'sin2th12 = 1/3 - r_tet r_oct': dict(val=1/3 - r_tet*r_oct,              obs=0.307,   sig=0.013,  unit=''),
 'sin2thW = r_tet^2/(r_oct^2+r_tet^2)': dict(val=r_tet**2/(r_oct**2+r_tet**2), obs=0.23122, sig=0.00004, unit=''),
}
print("\n=== SURVIVOR VALUES vs MEASURED ===")
for k,d in survivors.items():
    fe = (d['val']-d['obs'])/d['obs']*100
    nsig = (d['val']-d['obs'])/d['sig']
    print(f"  {k:42s} val={d['val']:.6f}  obs={d['obs']:.6f}  err={fe:+.3f}%  ({nsig:+.1f} sigma)")

# ---- grammar enumeration ----
ATOMS = {'r_oct':r_oct, 'r_tet':r_tet, 'a0':a0}
INTS  = {str(i):float(i) for i in range(1,7)}
base = {**ATOMS, **INTS}

def unary(v):
    out={}
    if v>=0: out['sqrt']=math.sqrt(v)
    out['sq']=v*v
    if -1<=v<=1:
        out['acos']=math.acos(v); out['asin']=math.asin(v)
    return out

def build(max_complexity=3, valcap=2e6):
    # pool: value -> (complexity, repr)
    pool={}
    def add(val,comp,rep):
        if not math.isfinite(val): return
        if abs(val)>valcap: return
        key=round(val,7)
        if key not in pool or comp<pool[key][0]:
            pool[key]=(comp,rep)
    for r,v in base.items(): add(v,0,r)
    cur=dict(pool)
    for comp in range(1,max_complexity+1):
        new={}
        vals=list(pool.items())  # (key,(comp,rep))
        # unary on everything so far
        for key,(c,rep) in vals:
            if c<comp:
                for op,uv in unary(key).items():
                    new_key=round(uv,7)
                    if new_key not in pool and (new_key not in new or comp<new[new_key][0]):
                        new[new_key]=(comp,f"{op}({rep})")
        # binary between pairs whose combined ops < comp
        keys=[k for k,_ in vals]
        for a,b in itertools.product(keys,repeat=2):
            ca=pool[a][0]; cb=pool[b][0]
            if ca+cb+1!=comp: continue
            ra=pool[a][1]; rb=pool[b][1]
            for op in ('+','-','*','/'):
                try:
                    if op=='+': val=a+b
                    elif op=='-': val=a-b
                    elif op=='*': val=a*b
                    else:
                        if abs(b)<1e-12: continue
                        val=a/b
                except: continue
                new_key=round(val,7)
                if new_key not in pool and (new_key not in new or comp<new[new_key][0]):
                    new[new_key]=(comp,f"({ra}{op}{rb})")
        pool.update(new)
    return pool

pool = build(max_complexity=3)
print(f"\nGrammar pool size (complexity<=3): {len(pool)} distinct values")

# ---- census of ALL angle targets the programme assigns a formula to ----
# (measured value, sigma, type). Compiled from the corpus (EQ, O, EJ, BY, BF, BJ,
#  Letters 87-90, CKM appendices). type 'x' = dimensionless (sin^2 / ratio), 'deg' = angle.
targets = {
 'PMNS sin2 th12':      (0.307,   0.013, 'x'),
 'PMNS sin2 th13':      (0.02219, 0.0006,'x'),
 'PMNS sin2 th23':      (0.558,   0.02,  'x'),
 'PMNS delta_CP(deg)':  (234.0,   35.0,  'deg'),
 'Weinberg sin2 thW':   (0.23122, 0.00004,'x'),
 'CKM sin th12(Cabibbo)':(0.2265, 0.001, 'x'),
 'CKM sin th23':        (0.0405,  0.001, 'x'),
 'CKM sin th13':        (0.00365, 0.0001,'x'),
 'CKM delta/CP(deg)':   (65.5,    3.5,   'deg'),
 'Wolfenstein A':       (0.826,   0.01,  'x'),
 'Wolfenstein eta_bar': (0.3392,  0.01,  'x'),
 'Wolfenstein rho_bar': (0.159,   0.01,  'x'),
 'Lepton Koide angle(deg)':(130.0,3.0,   'deg'),  # arccos(-r_oct/Sr)~130.4
 'Up Koide angle(deg)':  (110.0, 5.0,    'deg'),
 'Down Koide angle(deg)':(130.0, 5.0,    'deg'),
}
N = len(targets)
print(f"\nAngle targets the programme assigns geometric formulas to: N = {N}")

# grammar values split by plausible range
vals_x  = [k for k in pool if 0<k<1.2]           # dimensionless sin^2/ratios
vals_deg= [math.degrees(k) for k in pool if 0<k<math.pi*1.05]  # angles from acos/asin etc.
# also allow direct-degree hits from acos/asin results already in radians -> convert
print(f"pool values in (0,1.2): {len(vals_x)} ;  angle-candidate values: {len(vals_deg)}")

def hits_within(target, sig, kind, tol_frac):
    lo=target*(1-tol_frac); hi=target*(1+tol_frac)
    if kind=='x':
        cand=vals_x
    else:
        cand=vals_deg
    return sum(1 for v in cand if lo<=v<=hi), (len(cand))

print("\n=== JOINT LOOK-ELSEWHERE: how many programme angles does the grammar hit? ===")
for tol in (0.01, 0.015, 0.02, 0.03):
    hit_targets=0; total_density=0.0
    for name,(obs,sig,kind) in targets.items():
        h,pl = hits_within(obs,sig,kind,tol)
        total_density += h/pl
        if h>0: hit_targets+=1
    print(f"  tol={tol*100:>4.1f}%:  {hit_targets}/{N} targets have >=1 grammar hit | "
          f"expected hits per target (mean density x pool) approx {total_density/N*100:.3f}% of pool")

print("\n=== PER-SURVIVOR density & naive bits (grammar hits within achieved error) ===")
ach = {
 'beta=arccos(2 r_oct)':(65.5,3.5,'deg', abs(math.degrees(math.acos(2*r_oct))-65.5)/65.5),
 'sin2th13 = 3 a0':(0.02219,0.0006,'x', abs(3*a0-0.02219)/0.02219),
 'sin2th12 = 1/3 - r_tet r_oct':(0.307,0.013,'x', abs((1/3-r_tet*r_oct)-0.307)/0.307),
 'sin2thW = r_tet^2/(r_oct^2+r_tet^2)':(0.23122,0.00004,'x', abs(r_tet**2/(r_oct**2+r_tet**2)-0.23122)/0.23122),
}
for name,(obs,sig,kind,err) in ach.items():
    err=max(err,1e-4)
    h,pl=hits_within(obs,sig,kind,err)
    p=h/pl
    naive_bits=-math.log2(p) if p>0 else float('inf')
    # look-elsewhere: charge trials = pool size (forms tried) x N angles
    trials=pl*N
    le_bits = -math.log2(min(1.0,p*trials)) if p*trials>0 else 0.0
    nsig=(ach[name][0]-obs) # placeholder
    print(f"  {name:42s} err={err*100:.3f}%  grammar-hits={h}/{pl}  p={p:.4f}  "
          f"naive={naive_bits:4.1f} bits  after LEE(xN x pool)={max(le_bits,0):4.1f} bits")

# measurement-precision ceiling: bits cannot exceed what the data resolves
print("\n=== MEASUREMENT-PRECISION CEILING (a match tighter than the data is not information) ===")
for name,d in survivors.items():
    res_frac = d['sig']/d['obs']
    ach_frac = abs(d['val']-d['obs'])/d['obs']
    verdict = "match is INSIDE 1 sigma (no tension)" if abs(d['val']-d['obs'])<=d['sig'] else f"match is {abs(d['val']-d['obs'])/d['sig']:.0f} sigma OFF (a miss)"
    print(f"  {name:42s} data known to {res_frac*100:5.2f}% ; formula err {ach_frac*100:5.2f}% -> {verdict}")

print("\n=== FAIR LOOK-ELSEWHERE (charge = forms actually tried per angle x N angles) ===")
# multiplicities m = number of distinct geometric forms the corpus writes for that angle
mult = {
 'beta=arccos(2 r_oct)': 2,               # arccos(2r_oct) vs arccos(1/3) for the CP phase
 'sin2th13 = 3 a0': 3,                     # 3a0 ; arcsin(r_tet)+arctan(a0/r_oct) ; a0 r_tet/(r_oct+r_tet)
 'sin2th12 = 1/3 - r_tet r_oct': 3,        # 1/3-r_tet r_oct ; (1/pi)(1-5a0) ; pi/4-arcsin(r_oct)  (+ CKM leading forms)
 'sin2thW = r_tet^2/(r_oct^2+r_tet^2)': 1, # (single tree form found)
}
Nang=15
for name,(obs,sig,kind,err) in ach.items():
    err=max(err,1e-4)
    h,pl=hits_within(obs,sig,kind,err); p=h/pl
    naive=-math.log2(p) if p>0 else float('inf')
    m=mult[name]
    per_angle = naive - math.log2(m)          # charge only the forms tried for THIS angle
    joint     = naive - math.log2(m*Nang)     # charge forms x all angles addressed
    tag = "MISS vs data" if name.startswith('sin2thW') else ""
    print(f"  {name:42s} naive={naive:4.1f}  -log2(m)->{per_angle:4.1f}  -log2(m*N)->{joint:4.1f} bits {tag}")

print("\nNOTE: sin2thW is a 95-sigma miss vs the measured value; its 'bits' above are")
print("computed against its own 1.6% self-reported error and are not a match to data.")
