import numpy as np, time
import bbalpha_spectral as B
centers=B.fcc_centers()
def run(ft, si, Ns, aa=True, tol=1e-9, maxit=4000):
    res=[]
    for N in Ns:
        t0=time.time()
        sigma,fs=B.build_sphere_array(N,centers,f_target=ft,sigma_i=si,aa=aa)
        se,vals,its,rn=B.sigeff_iso(sigma,dirs=(0,),tol=tol,maxit=maxit,sigma_ref=0.5,conv='res')
        res.append((N,fs,se,its[0],time.time()-t0))
        print(f"  N={N:3d} f={fs:.5f} se={se:.5f} iters={its[0]} t={time.time()-t0:.0f}s")
    return res
print("CONDUCTING FCC f=0.5 sigma_i=10 (S-A target 2.82), antialiased:")
r=run(0.5,10.0,[48,64,96])
# 1/N extrapolation (linear) from last two
(N1,_,s1,_,_),(N2,_,s2,_,_)=r[-2],r[-1]
ext=s2+(s2-s1)/(1.0/N2-1.0/N1)*(0.0-1.0/N2)
print(f"  -> 1/N extrap (N={N1},{N2}): {ext:.4f}  (S-A exact 2.82)")
print("INSULATING-ish FCC touching sigma_i=0.1, antialiased (smoothness check):")
ft=np.pi/(3*np.sqrt(2))
run(ft,0.1,[48,64,96])
