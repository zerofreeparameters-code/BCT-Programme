#!/usr/bin/env python3
"""
Gate BB-ALPHA, Step 2 (independent computation).

Method: Fourier-Galerkin spectral homogenisation (allowed by the card:
"a spectral (Fourier-Galerkin) homogenisation with >= 2 resolutions and a
stated extrapolation"). NEITHER a Cartesian finite-difference grid NOR a
random walk. Derivatives are spectral (multiplication by i*k via rFFT),
the Nyquist mode is zeroed for a consistent real-field derivative.

We solve the periodic conductivity cell problem for the conventional cubic
FCC cell (edge L=1, four spheres), with perfectly INSULATING spheres
(sigma_incl = 0, matrix sigma = 1):
    div( sigma(x) ( Ebar - grad u(x) ) ) = 0,   u periodic, <u>=0 .
A u = b with A = -div(sigma grad .), symmetric PSD, solved by preconditioned
conjugate gradients (preconditioner = inverse homogeneous Laplacian /
reference medium). sigma_eff/sigma_m = < sigma e_d > with <e_d> = 1.

For sigma_incl = 0 the operator has a null space (potentials inside the
insulating voids), so the CG residual can stall while the physical scalar
sigma_eff still converges; we therefore monitor sigma_eff and stop on its
stabilisation (conv='sigeff').

Solid fraction is pinned exactly per resolution (f_target): the K = round(f N^3)
voxels nearest a sphere centre are the solid phase. This removes the
voxel-count scatter so sigma_eff converges cleanly in 1/N.

Outputs JSON.  Run isolated:  python3 -I bbalpha_spectral.py <mode> [args]
"""
import numpy as np
import json, sys, time

# ----------------------------------------------------------------------
def _dmin2(N, centers, L=1.0):
    coord = (np.arange(N) + 0.5) / N * L
    X, Y, Z = np.meshgrid(coord, coord, coord, indexing='ij')
    dm = np.full((N, N, N), np.inf)
    for c in centers:
        dx = X - c[0]; dy = Y - c[1]; dz = Z - c[2]
        dx -= L*np.round(dx/L); dy -= L*np.round(dy/L); dz -= L*np.round(dz/L)
        np.minimum(dm, dx*dx + dy*dy + dz*dz, out=dm)
    return dm

def build_sphere_array(N, centers, R=None, f_target=None, L=1.0,
                       sigma_m=1.0, sigma_i=0.0, aa=False):
    """Voxel conductivity for a periodic sphere array.
    aa=False: sharp interface (voxel centre rule, or pinned to f_target).
    aa=True : antialiased partial-volume theta (one-voxel linear interface
              ramp) with arithmetic mixing sigma = sigma_m + (sigma_i-sigma_m)*theta.
              Smooths the geometry so sigma_eff converges cleanly in 1/N; the
              mixing bias is O(1/N) and is removed by the N->inf extrapolation."""
    dm2 = _dmin2(N, centers, L)
    dm = np.sqrt(dm2)
    if R is None:
        R = (f_target*3.0/(4*np.pi*len(centers)))**(1.0/3.0) if f_target else 0.5
    if aa:
        h = L/N
        theta = np.clip(0.5 - (dm - R)/h, 0.0, 1.0)   # fraction inside spheres
        sigma = sigma_m + (sigma_i - sigma_m)*theta
        return sigma, float(theta.mean())
    if f_target is not None:
        K = int(round(f_target * N**3))
        flat = dm2.ravel()
        idx = np.argpartition(flat, K)[:K]
        inside = np.zeros(flat.shape, dtype=bool); inside[idx] = True
        inside = inside.reshape(dm2.shape)
    else:
        inside = dm2 <= R*R
    sigma = np.where(inside, sigma_i, sigma_m)
    return sigma, float(inside.mean())

def fcc_centers(L=1.0):
    return np.array([[0,0,0],[0,0.5,0.5],[0.5,0,0.5],[0.5,0.5,0]]) * L
def sc_centers(L=1.0):
    return np.array([[0.0,0.0,0.0]]) * L
def bcc_centers(L=1.0):
    return np.array([[0,0,0],[0.5,0.5,0.5]]) * L

# ----------------------------------------------------------------------
def solve_direction(sigma, direction, L=1.0, tol=1e-9, maxit=6000,
                    sigma_ref=None, conv='res', check=20, tol_se=1e-6,
                    use_precond=True):
    N = sigma.shape[0]; s3 = (N,N,N); ax = (0,1,2)
    kf = 2*np.pi*np.fft.fftfreq(N, d=L/N)
    kr = 2*np.pi*np.fft.rfftfreq(N, d=L/N)
    K2 = (kf[:,None,None]**2 + kf[None,:,None]**2 + kr[None,None,:]**2)
    K2[0,0,0] = 1.0
    kfd = kf.copy(); krd = kr.copy()
    if N % 2 == 0:
        kfd[N//2] = 0.0; krd[-1] = 0.0
    Kv = (kfd[:,None,None], kfd[None,:,None], krd[None,None,:])
    if sigma_ref is None:
        sigma_ref = 0.5*(sigma.max()+sigma.min()) if sigma.min() > 0 else 0.5*sigma.max()
    Ebar = np.zeros(3); Ebar[direction] = 1.0

    def grad(u):
        uh = np.fft.rfftn(u)
        return [np.fft.irfftn(1j*Kv[d]*uh, s=s3, axes=ax) for d in range(3)]
    def div(vec):
        acc = 1j*Kv[0]*np.fft.rfftn(vec[0])
        acc += 1j*Kv[1]*np.fft.rfftn(vec[1])
        acc += 1j*Kv[2]*np.fft.rfftn(vec[2])
        return np.fft.irfftn(acc, s=s3, axes=ax)
    def applyA(u):
        g = grad(u); return -div([sigma*g[d] for d in range(3)])
    def precond(r):
        if not use_precond:
            r2 = r - r.mean()   # identity preconditioner (project out global mean)
            return r2
        rh = np.fft.rfftn(r) / (sigma_ref*K2); rh[0,0,0] = 0.0
        return np.fft.irfftn(rh, s=s3, axes=ax)
    def sigeff_of(u):
        g = grad(u); return float(np.mean(sigma*(Ebar[direction]-g[direction])))

    b = -div([sigma*Ebar[d] for d in range(3)])
    bnorm = np.sqrt(np.vdot(b,b).real)
    u = np.zeros(s3)
    if bnorm < 1e-14:
        return sigeff_of(u), 0, 0.0, [sigeff_of(u)]
    r = b - applyA(u); z = precond(r); p = z.copy(); rz = np.vdot(r,z).real
    resnorm = 1.0; se_hist = []; se_prev = None; it = 0
    for it in range(1, maxit+1):
        Ap = applyA(p); pAp = np.vdot(p,Ap).real
        if pAp == 0: break
        al = rz/pAp; u += al*p; r -= al*Ap
        resnorm = np.sqrt(np.vdot(r,r).real)/bnorm
        if conv == 'res' and resnorm < tol:
            break
        if conv == 'sigeff' and it % check == 0:
            se = sigeff_of(u); se_hist.append([it, se])
            if se_prev is not None and abs(se-se_prev) < tol_se*abs(se) and resnorm < 1e-3:
                se_prev = se; break
            se_prev = se
        z = precond(r); rz_new = np.vdot(r,z).real
        p = z + (rz_new/rz)*p; rz = rz_new
    se = sigeff_of(u)
    return se, it, resnorm, se_hist

def sigeff_iso(sigma, dirs=(0,), **kw):
    vals=[]; iters=[]; res=[]
    for d in dirs:
        se, it, rn, _ = solve_direction(sigma, d, **kw)
        vals.append(se); iters.append(it); res.append(rn)
    return float(np.mean(vals)), vals, iters, res

# ----------------------------------------------------------------------
def analytic_tests():
    out = {}
    N=16; sig=np.ones((N,N,N))
    se,_,_,_ = solve_direction(sig,0); out['homogeneous']={'val':se,'exp':1.0}
    N=32; sig=np.ones((N,N,N)); sig[:N//2]=2.0
    sx,_,_,_=solve_direction(sig,0); sy,_,_,_=solve_direction(sig,1)
    out['laminate_series_x']={'val':sx,'exp':2.0/(0.5+1.0)}
    out['laminate_parallel_y']={'val':sy,'exp':1.5}
    return out

def main():
    mode = sys.argv[1] if len(sys.argv)>1 else 'help'
    t0=time.time()
    if mode=='selftest':
        print(json.dumps({'selftest':analytic_tests()},indent=2)); return
    if mode=='run':
        lattice=sys.argv[2]; N=int(sys.argv[3])
        sigma_i=float(sys.argv[4]) if len(sys.argv)>4 else 0.0
        f_target=float(sys.argv[5]) if len(sys.argv)>5 and sys.argv[5]!='-' else None
        ndirs=int(sys.argv[6]) if len(sys.argv)>6 else 1
        conv=sys.argv[7] if len(sys.argv)>7 else ('sigeff' if sigma_i==0.0 else 'res')
        maxit=int(sys.argv[8]) if len(sys.argv)>8 else 6000
        cmap={'fcc':(fcc_centers(),np.sqrt(2)/4.0),
              'sc':(sc_centers(),0.5),'bcc':(bcc_centers(),np.sqrt(3)/4.0)}
        centers,Rt=cmap[lattice]
        ftouch={'fcc':np.pi/(3*np.sqrt(2)),'sc':np.pi/6,'bcc':np.pi*np.sqrt(3)/8}
        ft = f_target if f_target is not None else ftouch[lattice]
        sigma,fsolid = build_sphere_array(N,centers,f_target=ft,sigma_i=sigma_i)
        se,vals,iters,res = sigeff_iso(sigma,dirs=tuple(range(ndirs)),
                                       tol=1e-9,maxit=maxit,sigma_ref=0.5,
                                       conv=conv,check=20,tol_se=1e-6)
        phi=1.0-fsolid; alpha=phi/se if se>0 else None
        print(json.dumps({'lattice':lattice,'N':N,'sigma_i':sigma_i,
            'conv':conv,'f_target':ft,'f_solid':fsolid,'phi':phi,'ndirs':ndirs,
            'sigma_eff_over_sigma_m':se,'per_direction':vals,
            'cg_iters':iters,'cg_res':res,
            'F':(1.0/se if se>0 else None),'alpha':alpha,
            'walltime_s':time.time()-t0},indent=2)); return
    print("modes: selftest | run <lattice> <N> [sigma_i] [f_target|-] [ndirs] [conv] [maxit]")

if __name__=='__main__':
    main()
