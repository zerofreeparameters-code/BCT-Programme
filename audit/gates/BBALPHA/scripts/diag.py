import numpy as np, time, sys
import bbalpha_spectral as B

# fix pinning to EXACT K via argpartition
def build_exact(N, centers, f_target, sigma_i=0.0):
    dm2 = B._dmin2(N, centers)
    K = int(round(f_target*N**3))
    flat = dm2.ravel()
    idx = np.argpartition(flat, K)[:K]
    inside = np.zeros(flat.shape, bool); inside[idx]=True
    inside = inside.reshape(dm2.shape)
    sigma = np.where(inside, sigma_i, 1.0)
    return sigma, inside.mean()

N=48
ft=np.pi/(3*np.sqrt(2))
centers=B.fcc_centers()
sigma,fs=build_exact(N,centers,ft,0.0)
print("N",N,"f_solid",fs,"target",ft)
# monitor sigeff over many iters, print history
t0=time.time()
se,it,rn,hist=B.solve_direction(sigma,0,conv='sigeff',check=50,tol_se=1e-9,maxit=4000,sigma_ref=0.5)
print("final se",se,"iters",it,"res",rn,"t",round(time.time()-t0))
print("history (iter, sigeff):")
for h in hist[::2]:
    print(f"  {h[0]:5d}  {h[1]:.6f}")
