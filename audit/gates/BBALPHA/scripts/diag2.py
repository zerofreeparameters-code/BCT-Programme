import numpy as np, time
import bbalpha_spectral as B
ft=np.pi/(3*np.sqrt(2)); centers=B.fcc_centers()
for N in [48]:
    sigma,fs=B.build_sphere_array(N,centers,f_target=ft,sigma_i=0.0)
    t0=time.time()
    se,it,rn,hist=B.solve_direction(sigma,0,conv='sigeff',check=100,tol_se=1e-7,
                                     maxit=6000,use_precond=False)
    print(f"N={N} f={fs:.6f} final_se={se:.6f} iters={it} res={rn:.2e} t={time.time()-t0:.0f}s")
    print("history (iter, sigeff, alpha):")
    for h in hist:
        print(f"  {h[0]:5d}  se={h[1]:.6f}  alpha={(1-fs)/h[1]:.4f}")
