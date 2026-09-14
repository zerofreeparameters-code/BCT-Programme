#!/usr/bin/env python3
"""Gate PRED — Step 0: recompute every closed-form BCT prediction exactly as printed.
Deterministic, mpmath, no seeds.  Model: Claude Fable 5.1 (see deliverable)."""
from mpmath import mp, mpf, sqrt, pi, exp, atan, cos, log
mp.dps = 30
# ---- ingredient constants (as printed in corpus) ----
roct = (sqrt(2)-1)/2
rtet = (sqrt(6)-2)/4
a0   = roct*rtet/pi
SD4  = pi**5/6
STd  = SD4*(rtet/roct)**2
Nc   = 3
Lam  = mpf(220)              # chosen anchor, MeV
hbarc= mpf('197.3269804')
mpi  = mpf('135.0')          # measured input: corpus uses m_pi0 rounded to 135.0 (784.2448 = 135.0/(2 sqrt a0))
mphi = mpf('1019.461')       # measured input
mP_obs = mpf('1.220890e22')  # MeV, measured (used as input by corpus in several places)
v_BCT = mpf('244400')        # MeV, BCT 3-loop value (NOT recomputable here)
print(f"r_oct={roct}\nr_tet={rtet}\nalpha0={a0}\nS_D4={SD4}\nS_Td={STd}")
rows=[]  # (name, formula, bct_print, recomputed, obs, obs_unc, class)
def add(name, formula, printed, val, obs, unc, cls):
    rows.append((name, formula, printed, val, obs, unc, cls))
# ---- A. geometry-only, dimensionless ----
add('1/alpha','1/[a0(1-2a0)]',137.018, 1/(a0*(1-2*a0)), 137.035999177, 2.1e-8,'GEO')
add('1/alpha (all-orders variant)','1/[a0(1-3a0)/(1-a0)]',137.0336, (1-a0)/(a0*(1-3*a0)), 137.035999177, 2.1e-8,'GEO')
add('sin2th13','3a0',0.02222, 3*a0, 0.02203, 0.00058,'GEO')
add('sin2th12','(1-5a0)/pi',0.30652, (1-5*a0)/pi, 0.307, 0.013,'GEO')
add('n_s','1-12/pi^5',0.9608, 1-2/SD4, 0.9649, 0.0042,'GEO')
add('sin2thW (tree)','rtet^2/(roct^2+rtet^2)',0.2274, rtet**2/(roct**2+rtet**2), 0.23122, 0.00004,'GEO')
add('sin2thW (tree x(1+9/4 a0))','tree*(1+9a0/4)',None, rtet**2/(roct**2+rtet**2)*(1+9*a0/4), 0.23122, 0.00004,'GEO')
# ---- B. Lambda=220 anchor + measured m_pi ----
mrhoLO = mpi/(2*sqrt(a0)); mrho = mrhoLO*(1-mpf(Nc)/2*a0)
add('m_rho','m_pi/(2 sqrt a0) (1-3a0/2)',775.530, mrho, 775.26, 0.23,'LAM+MEAS')
mK = mpi*(1/a0)**(mpf(1)/3)/sqrt(2)
add('m_K','m_pi (1/a0)^(1/3)/sqrt2',489.6856, mK, 493.677, 0.013,'LAM+MEAS')
mGMO2=(4*mK**2-mpi**2)/3
add('m_eta','sqrt(mGMO2 (1-2Nc a0))',547.4546, sqrt(mGMO2*(1-2*Nc*a0)), 547.862, 0.017,'LAM+MEAS')
add("m_eta'",'sqrt(mGMO2 (1+2Nc/pi))',955.338, sqrt(mGMO2*(1+2*Nc/pi)), 957.78, 0.06,'LAM+MEAS')
add('m_omega','m_rho sqrt(1+(roct^2+roct rtet-rtet^2)/pi)',782.1106, mrho*sqrt(1+(roct**2+roct*rtet-rtet**2)/pi), 782.66, 0.13,'LAM+MEAS')
add('m_K*','sqrt(m_rho m_phi)  [m_phi measured]',889.169, sqrt(mrho*mphi), 891.67, 0.26,'MEAS-INPUT')
Cp=(1+rtet-roct)  # PRL prints "/pi" but the value 0.90527 used everywhere is 1+rtet-roct (Letter misprint)
Cn=Cp+2*a0; CD=pi*Cp*(1+8*a0); CR=CD+2*Cn; C1535=CD+3*Cn; C1520=C1535-Cn/4; CD1600=2*CD+Cp/2
def mB(C): return sqrt(mrho**2+2*pi*Lam**2*C)
add('m_p','sqrt(mrho^2+2pi L^2 Cp), Cp=1+rtet-roct',936.35, mB(Cp), 938.272, 0.0001,'LAM+MEAS')
add('m_n','Cn=Cp+2a0',938.749, mB(Cn), 939.565, 0.0001,'LAM+MEAS')
add('m_Delta(1232)','CD=pi Cp(1+8a0)',1231.8985, mB(CD), 1232, 2,'LAM+MEAS')
add('m_N*(1440)','CR=CD+2Cn',1441.2421, mB(CR), 1440, 30,'LAM+MEAS')
add('m_N*(1535)','C=CD+3Cn',1535.2464, mB(C1535), 1530, 10,'LAM+MEAS')
add('m_N*(1520)','C=C1535-Cn/4',1512.2932, mB(C1520), 1515, 5,'LAM+MEAS')
add('m_Delta*(1600)','C=2CD+Cp/2',1603.5426, mB(CD1600), 1570, 70,'LAM+MEAS')
add('r_p','(hbarc/m_rho) sqrt(12 Cp)',0.838622, hbarc/mrho*sqrt(12*Cp), 0.84075, 0.00064,'LAM+MEAS')
add('r_pi (Phase48C)','sqrt6 hbarc/m_rho(LO=779.244) (1+9a0)',0.661637, sqrt(6)*hbarc/mpf('779.244')*(1+9*a0), 0.659, 0.004,'LAM+MEAS')
rp=hbarc/mrho*sqrt(12*Cp)
kappa_n=mpf('-1.91304273'); mn=mpf('939.5654')
rn2 = 3*kappa_n*hbarc**2/(2*mn**2) + (mpf(2)/3*roct**2 - 2*(mpf(1)/3)*rtet**2)  # printed '(Q_u roct^2 - 2Q_d rtet^2)'; value 0.015675 requires |Q_d|*12*hbarc**2/mrho**2 - a0*rp**2
add('r_n^2','Pauli(meas kappa_n,m_n)+Dirac(voids)-a0 r_p^2',-0.116920, rn2, -0.1155, 0.0017,'MEAS-INPUT')
add('T_c (Phase44D)','L/sqrt2 (1+3a0/8)',155.9957, Lam/sqrt(2)*(1+3*a0/8), 156.5, 1.5,'LAM')
# Koide (Phase 82D)
M02 = sqrt(2)*Lam*(1+a0); th = 2*atan(rtet)*(1-a0)
mtau=M02*(1+sqrt(2)*cos(th))**2; me=M02*(1+sqrt(2)*cos(th+2*pi/3))**2; mmu=M02*(1+sqrt(2)*cos(th+4*pi/3))**2  # 'M0^2' printed in MeV
add('m_tau (Koide)','M0^2=sqrt2 L(1+a0); th=2atan(rtet)(1-a0)',1774.5996, mtau, 1776.93, 0.09,'LAM')
add('m_e (Koide)','k=1',0.512255, me, 0.51099895, 1e-9,'LAM')
add('m_mu (Koide)','k=2',105.4791, mmu, 105.6583755, 2e-6,'LAM')
# ---- C. uses v_BCT (3-loop, not recomputable) ----
mt = v_BCT/sqrt(2)*(1+mpf(3)/8*a0)
add('m_t','v_BCT/sqrt2 (1+3a0/8), v_BCT=244.4 GeV',173296.99, mt, 172570, 290,'V_BCT')
add('m_H','v_BCT/2 (1+3a0)',124916, v_BCT/2*(1+3*a0), 125200, 110,'V_BCT')
add('m_b','roct rtet m_t (1+5a0)',4182.55, roct*rtet*mt*(1+5*a0), 4183, 7,'V_BCT')
dn_d = rtet*(1+rtet/roct); dn_u = rtet - rtet**2/roct
def mq(n): return mt*exp(-STd*n/24)
add('m_c (Phase25A)','m_t exp(-STd(8+atan(rtet/pi)-dn_d)/24)',1266.25, mq(8+atan(rtet/pi)-dn_d), 1273, 5,'V_BCT')
add('m_s (Phase25)','m_t exp(-STd(12+rtet^2/(2roct))/24)',93.33, mq(12+rtet**2/(2*roct)), 93.5, 0.8,'V_BCT')
add('m_d (Phase25)','m_t exp(-STd(17-dn_d)/24)',4.644, mq(17-dn_d), 4.70, 0.07,'V_BCT')
add('m_u (Phase25)','m_t exp(-STd(18+dn_u)/24)',2.158, mq(18+dn_u), 2.16, 0.4,'V_BCT')
# ---- D. measured-input / circular ----
add('m_P via M_R/a0^2','M_R := m_P(obs) a0^2  (CIRCULAR)',1.21995e22, (mP_obs*a0**2)/a0**2, mP_obs, 1.5e17,'CIRCULAR')
add('m_e via m_P','m_P(obs) exp(-(pi^5+pi)/6)',0.51112, mP_obs*exp(-(pi**5+pi)/6), 0.51099895, 1e-9,'MEAS-INPUT')
add('m_P via Lam exp(S_QCD)','220 exp(45.461) [S_QCD from fixed point using alpha_s input]',1.2185e22, Lam*exp(mpf('45.4608')), mP_obs, 1.5e17,'MEAS-INPUT')
add('V_us','sqrt(md/(ms-md))(1-1.5a0 ms/L) [meas md,ms]',0.224534, sqrt(mpf('4.67')/(mpf('96.4')-mpf('4.67')))*(1-mpf(3)/2*a0*mpf('96.4')/Lam), 0.22453, 0.0007,'MEAS-INPUT')
add('H_0','H0(Planck)(1+delta/2), delta=0.008',67.6696, mpf('67.4')*(1+mpf('0.008')/2), 67.4, 0.5,'MEAS-INPUT')
add('Y_p','Y_p(SM)+dYp/dtau*(-0.0138 s)',0.2470995, mpf('0.2471')+mpf('0.00004')*mpf('-0.01378'), 0.245, 0.003,'MEAS-INPUT')

print("\n%-32s %-48s %12s %14s %14s %9s %9s %s"%('quantity','formula as printed','printed','recomputed','observed','recomp%','print%','class'))
ok=fail=0
for name,f,pr,val,obs,unc,cls in rows:
    err=(val/obs-1)*100
    repro = (pr is None) or (abs(val/mpf(pr)-1)<2e-3)
    ok+=repro; fail+= (not repro)
    print("%-32s %-48s %12s %14.6g %14.6g %+9.4f %9s %s%s"%(name,f[:48],pr,float(val),float(obs),float(err),'' if pr is None else '%+.4f'%((mpf(pr)/obs-1)*100),cls,'' if repro else '  <<NO-REPRO'))
print(f"\nreproduce printed value (within 0.2%): {ok}   do not: {fail}")
