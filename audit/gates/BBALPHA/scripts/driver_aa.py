#!/usr/bin/env python3
"""Step-2 antialiased double-extrapolation sweep for Gate BB-ALPHA (FCC, insulating)."""
import numpy as np, json, time, sys
import bbalpha_spectral as B

ft = np.pi/(3*np.sqrt(2))   # 0.7404805
centers = B.fcc_centers()
plan = [(0.10,[48,64,96,128]),(0.05,[48,64,96,128]),
        (0.02,[48,64,96,128]),(0.01,[48,64,96])]

out = open('/home/claude/work/aa_out.jsonl','w')
for si,Ns in plan:
    for N in Ns:
        t0=time.time()
        sigma,fs=B.build_sphere_array(N,centers,f_target=ft,sigma_i=si,aa=True)
        se,vals,its,rn=B.sigeff_iso(sigma,dirs=(0,),tol=1e-9,maxit=5000,
                                    sigma_ref=0.5,conv='res')
        rec={'sigma_i':si,'N':N,'f_solid':fs,'sigma_eff':se,
             'iters':its[0],'res':rn[0],'t':round(time.time()-t0,1)}
        out.write(json.dumps(rec)+'\n'); out.flush()
        print(json.dumps(rec)); sys.stdout.flush()
# isotropy check (cubic symmetry -> 3 directions equal)
sigma,fs=B.build_sphere_array(64,centers,f_target=ft,sigma_i=0.05,aa=True)
se,vals,its,rn=B.sigeff_iso(sigma,dirs=(0,1,2),tol=1e-9,maxit=5000,sigma_ref=0.5,conv='res')
rec={'isotropy_check':True,'sigma_i':0.05,'N':64,'per_direction':vals}
out.write(json.dumps(rec)+'\n'); out.flush(); print(json.dumps(rec))
out.close(); print("DONE")
