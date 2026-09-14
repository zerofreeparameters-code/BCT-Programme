"""Gate PRED2 Step 2 - scoring. Uses the grammar fixed in pred2_step2_grammar.py.
Thresholds pre-registered in the prompt: >=10 bits surprising; 3-10 suggestive; <3 unsurprising."""
import math, random, pickle, sys
import importlib.util
spec = importlib.util.spec_from_file_location("g", "pred2_step2_grammar.py")
g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
random.seed(99)

M = 700000
POOL = {}
for C in range(1, 6): POOL[C] = [v for v in g.levels[C] if v and math.isfinite(v) and v != 0]
for C in range(6, 20):
    vals = []
    for _ in range(M):
        v = g.sample(C)
        if v is not None and math.isfinite(v) and v != 0: vals.append(v)
    POOL[C] = vals
    print(f"pool C={C}: {len(vals)}", file=sys.stderr)

def logdensity(C, T):
    """distinct grammar values per unit ln(x) near T, with the window used and the hit count."""
    pool = POOL[C]; n = len(pool); lt = math.log(abs(T))
    for w in (0.002,0.005,0.01,0.02,0.05,0.1,0.2,0.4,0.8):
        hits = [v for v in pool if v > 0 and abs(math.log(v)-lt) <= w]
        if len(hits) >= 60:
            return len(hits)/(n*2*w), w, len(hits), n
    hits = [v for v in pool if v > 0 and abs(math.log(v)-lt) <= 0.8]
    return (len(hits)+1)/(n*1.6), 0.8, len(hits), n

def score(T, eps, C):
    d, w, nh, n = logdensity(C, T)
    p = min(1.0, d*2*abs(eps))
    return (-math.log2(p) if p > 0 else float('inf')), p, d, w, nh, n

TARGETS = [
 # tag, target value, |eps| achieved by corpus expr (recomputed), C_expr, n_corr, corr complexities, date-order post-hoc?
 ('alpha  = a0(1-2a0)',            0.0072973525643, 1.294e-4, 7,  1, [3], True),
 ('alpha  = a0(1-3a0)/(1-a0)',     0.0072973525643, 1.719e-5, 11, 2, [3,3], True),
 ('m_e/m_P = exp(-(pi^5+pi)/6)',   0.51099895069/1.220890e22, 9.608e-4, 8, 1, [4], True),
 ('m_e/m_P = exp(-S/(1-a0(4pi+1)/pi^2))', 0.51099895069/1.220890e22, 1.412e-4, 15, 2, [4,10], True),
 ('sin2thW(tree)',                 0.23122,        1.635e-2, 8,  0, [], False),
 ('sin2th13 = 3a0',                0.02203,        8.814e-3, 3,  0, [], False),
 ('sin2th12 = 1/3 - r_tet r_oct',  0.307,          9.968e-3, 6,  0, [], False),
 ('lambda = 2r_tet(1+3a0/8)',      0.22501,        1.596e-3, 11, 1, [5], True),
 ('A = (1+r_oct)^-1 (1-a0/2)',     0.820,          6.5e-3,   10, 1, [5], True),
 ('etabar = 3 r_tet',              0.3548,         4.97e-2,  3,  0, [], False),
 ('beta = acos(2 r_oct) [deg]',    65.75,          3.4e-3,   4,  0, [], False),
 ('delta_CKM = acos(1/3) [deg]',   65.75,          7.3e-2,   3,  0, [], False),
 ('m_s/m_t (Td orbit n=12)',       93.5/172570.,   0.0977,   12, 0, [], False),
 ('m_d/m_t (n=17-r_tet(1+r_tet/r_oct))', 4.70/172570., 1.94e-2, 17, 1, [6], True),
 ('m_u/m_t (n=18+r_tet-r_tet^2/r_oct)',  2.16/172570., 8.33e-3, 18, 1, [7], True),
 ('m_b/m_t = pi a0 (1+5a0)',       4183./172570.,  7.59e-3,  9,  1, [5], True),
 ('m_rho/m_pi0 = (2 sqrt a0)^-1 (1-3a0/2)', 775.26/134.9768, 3.4e-4, 12, 1, [7], True),
 ('m_p/m_e = 6 pi^5',              1836.152673426, 1.882e-5, 4,  0, [], False),
 ('Koide phase delta (LO+NLO)',    2.316580,       2.0e-5,   19, 1, [8], True),
]
print(f"{'target':42s} {'C':>3} {'eps':>10} {'p_raw':>11} {'raw bits':>9} {'window':>7} {'hits':>6}")
rows = []
for tag, T, eps, C, nc, ccs, post in TARGETS:
    b, p, d, w, nh, n = score(T, eps, C)
    rows.append((tag,T,eps,C,nc,ccs,post,b,p,d,w,nh,n))
    print(f"{tag:42s} {C:>3} {eps:>10.3e} {p:>11.3e} {b:>9.2f} {w:>7.3f} {nh:>6}")
pickle.dump(rows, open('rawscores.pkl','wb'))
