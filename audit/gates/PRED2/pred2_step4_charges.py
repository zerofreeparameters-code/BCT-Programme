"""Gate PRED2 Step 2 (cont.) - look-elsewhere, correction-factor and date-order charges."""
import math, pickle, random, sys, importlib.util
spec = importlib.util.spec_from_file_location("g","pred2_step2_grammar.py")
g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
random.seed(7)
rows = pickle.load(open('rawscores.pkl','rb'))

# --- pools of DISTINCT values, for counting candidate correction factors ---
M = 600000
DPOOL = {}
for C in range(1,6): DPOOL[C] = sorted(set(round(v,10) for v in g.levels[C] if v and math.isfinite(v)))
for C in range(6,12):
    s = set()
    for _ in range(M):
        v = g.sample(C)
        if v is not None and math.isfinite(v): s.add(round(v,10))
    DPOOL[C] = sorted(s)
    print(f"distinct-pool C={C}: {len(s)} (from {M} samples)", file=sys.stderr)

def n_candidates(Cf, f_req, window):
    """How many distinct grammar values of complexity <= Cf sit inside the residual window
    the post-hoc factor had to close?  Any of them was available to be tried."""
    tot = 0; detail = []
    for C in range(1, Cf+1):
        pool = DPOOL[min(C,11)]
        k = sum(1 for v in pool if abs(v-f_req) <= window)
        if C > 11: k = int(k * (g.N[C]/g.N[11]))   # scale by structural count if beyond sampled range
        elif C > 5: k = int(k * (g.N[C]/ (M*1.0)) ) if False else k
        tot += k; detail.append((C,k))
    return max(tot,1), detail

# correction factors, from the census: (row tag, factor value required, window it closed, complexity of factor)
CORR = {
 'alpha  = a0(1-2a0)':            [( 0.98506, 0.0152, 3)],
 'alpha  = a0(1-3a0)/(1-a0)':     [( 0.98506, 0.0152, 3), (1.00000, 0.0002, 3)],
 'm_e/m_P = exp(-(pi^5+pi)/6)':   [( 1.010266, 0.688, 4)],
 'm_e/m_P = exp(-S/(1-a0(4pi+1)/pi^2))': [(1.010266,0.688,4),(1.0000027,0.0397,10)],
 'lambda = 2r_tet(1+3a0/8)':      [( 1.002778, 0.0028, 5)],
 'A = (1+r_oct)^-1 (1-a0/2)':     [( 0.996296, 0.0037, 5)],
 'm_d/m_t (n=17-r_tet(1+r_tet/r_oct))': [(1.1076, 0.108, 6)],
 'm_u/m_t (n=18+r_tet-r_tet^2/r_oct)':  [(0.9765, 0.024, 7)],
 'm_b/m_t = pi a0 (1+5a0)':       [( 1.03704, 0.037, 5)],
 'm_rho/m_pi0 = (2 sqrt a0)^-1 (1-3a0/2)': [(0.98889, 0.0111, 7)],
 'Koide phase delta (LO+NLO)':    [( 1.01781, 0.0175, 8)],
}
CENSUS_TRIED = 92          # published sub-1% master table = floor on targets attempted
CENSUS_CLAIMED = 280       # corpus's own claim of predictions made
PER_TARGET_SEARCH = {      # candidate expressions the corpus itself reports testing, per target
 'alpha  = a0(1-2a0)': 67, 'alpha  = a0(1-3a0)/(1-a0)': 67, 'm_e/m_P = exp(-(pi^5+pi)/6)': 4,
 'm_e/m_P = exp(-S/(1-a0(4pi+1)/pi^2))': 4, 'm_b/m_t = pi a0 (1+5a0)': 3,
 'Koide phase delta (LO+NLO)': 2,
}
LE = math.log2(CENSUS_TRIED)
print(f"\nLook-elsewhere over targets: -log2({CENSUS_TRIED}) = {LE:.2f} bits "
      f"(corpus's own 280-prediction claim would give {math.log2(CENSUS_CLAIMED):.2f})\n")
out = []
print(f"{'prediction':42s} {'raw':>6} {'LE':>5} {'srch':>5} {'corr':>6} {'net':>7}  bin")
for (tag,T,eps,C,nc,ccs,post,b,p,d,w,nh,n) in rows:
    srch = math.log2(PER_TARGET_SEARCH.get(tag,1))
    corr = 0.0; cdet=[]
    if post and tag in CORR:
        for (freq, win, Cf) in CORR[tag]:
            k,_ = n_candidates(Cf, freq, win)
            corr += math.log2(k); cdet.append((freq,win,Cf,k))
    net = b - LE - srch - corr
    binlab = 'SURPRISING' if net>=10 else ('suggestive' if net>=3 else 'unsurprising')
    out.append((tag,b,LE,srch,corr,net,binlab,cdet))
    print(f"{tag:42s} {b:>6.2f} {LE:>5.2f} {srch:>5.2f} {corr:>6.2f} {net:>7.2f}  {binlab}")
pickle.dump(out, open('charges.pkl','wb'))
print("\ncorrection-factor detail (required factor, residual window closed, complexity, #grammar candidates in window):")
for tag,b,le,s,c,net,bl,cdet in out:
    for dd in cdet: print(f"  {tag:42s} f={dd[0]:.6f} win=±{dd[1]:.4f} C_f={dd[2]} candidates={dd[3]}")
