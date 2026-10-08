"""Post-unblinding comparison: CRIT2 (this code) vs Gate CRIT published tables (L=8 stage C, L=4 stage A).
Gate CRIT's errors are not published; its lattice array holds two copies, so its error is taken as
mine/sqrt(2) and the combined sigma as mine*sqrt(1.5). Approximate; not a verdict input."""
import json, numpy as np
crit_L8 = {0.590:(0.56646,0.56638),0.595:(0.55454,0.55421),0.600:(0.54031,0.53982),0.605:(0.52228,0.52336),
           0.610:(0.49897,0.50168),0.615:(0.40904,0.40811),0.620:(0.39740,0.39583),0.625:(0.38590,0.38598),
           0.630:(0.37798,0.37777)}
crit_L4 = {0.40:(0.77600,0.77538),0.45:(0.73738,0.73747),0.50:(0.69242,0.69316),0.55:(0.63639,0.63554),
           0.60:(0.53282,0.52868),0.65:(0.35052,0.35020),0.70:(0.30796,0.30772),0.75:(0.27795,0.27795),
           0.80:(0.25406,0.25405),0.85:(0.23483,0.23502),0.90:(0.22452,0.21909)}
def load(tag):
    d={}
    for l in open(f"/root/crit2/out/{tag}.jsonl"):
        r=json.loads(l); d[(round(r['beta'],4),r['start'])]=r
    return d
for tag, ref, L in (("s52",crit_L8,8),("s51",crit_L4,4)):
    d=load(tag); print(f"== L={L}: beta  start   CRIT2      Gate CRIT   diff      z(approx)")
    zs=[]
    for b,(eh,ec) in sorted(ref.items()):
        for s,e in (("hot",eh),("cold",ec)):
            r=d[(round(b,4),s)]; diff=r['E']-e; sig=r['E_err']*np.sqrt(1.5); z=diff/sig
            zs.append((b,s,z))
            print(f"   {b:.3f}  {s:5s}  {r['E']:.5f}   {e:.5f}   {diff:+.5f}  {z:+.2f}")
    if L == 4:
        far=[z for b,s,z in zs if abs(b-0.6125)>0.02 and not (s=='hot' and b>=0.70)]
        print(f"   L=4 comparisons away from the jump (beta=0.60 left out; hot starts at beta>=0.70 left out, "
              f"trapped flux): n={len(far)}, rms z={np.sqrt(np.mean(np.square(far))):.2f}, max|z|={np.max(np.abs(far)):.2f}")
    else:
        for s in ("cold","hot"):
            z=np.array([zz for b,ss,zz in zs if ss==s])
            print(f"   L=8 {s:4s} starts, all 9 grid points: rms z = {np.sqrt(np.mean(z**2)):.2f}, "
                  f"max|z| = {np.abs(z).max():.2f}, mean z = {z.mean():+.2f}, negative: {(z<0).sum()}/9")
        zh=np.array([zz for b,ss,zz in zs if ss=='hot' and abs(b-0.620)>1e-9])
        print(f"   L=8 hot starts without beta=0.620: rms z = {np.sqrt(np.mean(zh**2)):.2f}")
        for b in (0.620, 0.630):
            eh,ec=ref[b]; mh=d[(b,'hot')]['E']; mc=d[(b,'cold')]['E']
            print(f"   within-code hot-cold split at L=8, beta={b:.3f}: Gate CRIT {eh-ec:+.5f}, CRIT2 {mh-mc:+.5f}")
