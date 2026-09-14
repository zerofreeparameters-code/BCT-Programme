import math, random, importlib.util
spec = importlib.util.spec_from_file_location("g","pred2_step2_grammar.py")
g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
random.seed(11)
ALPHA = 0.0072973525643
for num,den,lbl in [(9,8,'9/(8 pi^4)'),(9,16,'9/(16 pi^4)')]:
    w = (num/(den*math.pi**4))*(math.pi**5/(2**4*math.factorial(5)))**0.25
    print(f"Wyler {lbl} (pi^5/(2^4 5!))^(1/4):  alpha={w:.12f}  1/alpha={1/w:.6f}  eps={(w-ALPHA)/ALPHA:+.3e}")
W = (9/(8*math.pi**4))*(math.pi**5/(2**4*math.factorial(5)))**0.25
eps_W = abs(W-ALPHA)/ALPHA
C_W = 20     # node count of the Wyler expression written in the §2 grammar (9=3^2, 5!=24*(4+1))
M = 900000
pool=[]
for _ in range(M):
    v = g.sample(C_W)
    if v is not None and math.isfinite(v) and v>0: pool.append(v)
lt = math.log(ALPHA)
for wdw in (0.005,0.01,0.02,0.05,0.1,0.2):
    hits=[v for v in pool if abs(math.log(v)-lt)<=wdw]
    if len(hits)>=60: break
dens = len(hits)/(len(pool)*2*wdw); p = min(1.0,dens*2*eps_W)
print(f"Wyler: eps={eps_W:.3e}  C={C_W}  window=±{wdw}  hits={len(hits)}/{len(pool)}  raw bits={-math.log2(p):.2f}")
print(f"  minus look-elsewhere over 92 targets ({math.log2(92):.2f}) = {-math.log2(p)-math.log2(92):.2f} net bits"
      f"  [Wyler targeted ONE number, so the honest LE charge for him is 0.00 -> net {-math.log2(p):.2f}]")
