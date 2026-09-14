"""Gate PRED2 - Wyler benchmark + inverse-symbolic control restricted to the §2 grammar."""
import math, random, sys, importlib.util, pickle
spec = importlib.util.spec_from_file_location("g","pred2_step2_grammar.py")
g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
random.seed(4242)
ALPHA = 0.0072973525643; INVA = 137.035999177

# ---- Wyler (1969,1971) ----
# NOTE (14 Sep 2026): the first run of this script used two WRONG prefactors, 9/(16 pi^3) and
# 9/(16 pi^4), which give 1/alpha = 87.2 and 274.1 and are NOT Wyler's expression.  The correct
# published form is alpha = (9/(8 pi^4)) * (pi^5/(2^4 * 5!))^(1/4) = 1/137.036082.
# The Wyler benchmark is computed and scored in pred2_step6_wyler.py; it is not repeated here.
# The stale header at the top of the committed control.txt is from that first run - see the
# correction note prepended to that file.

# ---- randomised inverse-symbolic search inside the grammar ----
ATOMN = list(g.ATOMS.items())
def rsample(C):
    if C == 1:
        n,v = random.choice(ATOMN); return v, n
    w = [len(g.UN)*g.N[C-1]] + [len(g.BIN)*g.N[i]*g.N[C-1-i] for i in range(1,C-1)]
    tot = sum(w); r = random.random()*tot; acc = 0
    for idx, wi in enumerate(w):
        acc += wi
        if r <= acc:
            if idx == 0:
                res = rsample(C-1)
                if res is None: return None
                nm, f = g.UN[random.randrange(len(g.UN))]
                v = f(res[0])
                return None if v is None or not math.isfinite(v) else (v, f"{nm}({res[1]})")
            a, b = rsample(idx), rsample(C-1-idx)
            if a is None or b is None: return None
            nm, f = g.BIN[random.randrange(len(g.BIN))]
            v = f(a[0], b[0])
            return None if v is None or not math.isfinite(v) else (v, f"({a[1]}{nm}{b[1]})")
    return None

TG = [('alpha',ALPHA,7,1.294e-4),('m_e/m_P',0.51099895069/1.220890e22,8,9.608e-4),
      ('sin2thW',0.23122,8,1.635e-2),('sin2th13',0.02203,3,8.814e-3),
      ('sin2th12',0.307,6,9.968e-3),('lambda_W',0.22501,11,1.596e-3),
      ('etabar',0.3548,3,4.97e-2),('m_p/m_e',1836.152673426,4,1.882e-5),
      ('beta_deg',65.75,4,3.4e-3),('m_rho/m_pi0',775.26/134.9768,12,3.4e-4)]
N = 1500000
print(f"\ninverse-symbolic control ({N:,} random grammar expressions per target, complexity <= C_corpus)")
print(f"{'target':12s} {'C':>3} {'corpus eps':>11} {'best eps found':>15}  best expression")
res={}
for tag, T, C, ce in TG:
    best = (1e9, None)
    for _ in range(N):
        c = random.randint(1, C)
        s = rsample(c)
        if s is None or s[0] <= 0: continue
        e = abs(s[0]-T)/T
        if e < best[0]: best = (e, s[1])
    res[tag]=best
    flag = ' <-- control BEATS corpus' if best[0] < ce else ''
    print(f"{tag:12s} {C:>3} {ce:>11.3e} {best[0]:>15.3e}  {best[1]}{flag}")
pickle.dump(res, open('control.pkl','wb'))
