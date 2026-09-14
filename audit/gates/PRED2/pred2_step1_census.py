# Gate PRED2 Step 0/1 - recomputation of every printed closed-form BCT expression
# All measured values: CODATA 2022 (fetched 14 Sep 2026, pml.nist.gov allascii.txt)
# and PDG 2024 (fetched in-session, cited in deliverable).
from mpmath import mp, mpf, sqrt, pi, exp, log, acos, atan, tan
mp.dps = 60

r_oct = (sqrt(2)-1)/2
r_tet = (sqrt(6)-2)/4
R     = mpf(1)/2
a0    = r_oct*r_tet/pi
S_D4  = pi**5/6
x_lep = 4*a0/pi
S_Td  = S_D4*(r_tet/r_oct)**2

# --- measured ---
M = {
 'inv_alpha'   : (mpf('137.035999177'), 'CODATA2022'),
 'me_MeV'      : (mpf('0.51099895069'), 'CODATA2022'),
 'mP_GeV'      : (mpf('1.220890e19'),   'CODATA2022'),
 'G'           : (mpf('6.67430e-11'),   'CODATA2022'),
 'mmu_MeV'     : (mpf('105.6583755'),   'CODATA2022'),
 'mtau_MeV'    : (mpf('1776.86'),       'CODATA2022(tau energy equiv)'),
 'mp_MeV'      : (mpf('938.27208943'),  'CODATA2022'),
 'rp_fm'       : (mpf('0.84075'),       'CODATA2022'),
 's2w_MSbar'   : (mpf('0.23122'),       'PDG2024'),
 's2w_onshell' : (mpf('0.22305'),       'CODATA2022 weak mixing angle'),
 'mW_MeV'      : (mpf('80369.2'),       'PDG2024'),
 'mZ_MeV'      : (mpf('91187.6'),       'PDG2024'),
 'mH_MeV'      : (mpf('125200'),        'PDG2024'),
 'mt_MeV'      : (mpf('172570'),        'PDG2024'),
 'mb_MeV'      : (mpf('4183'),          'PDG2024'),
 'mc_MeV'      : (mpf('1273'),          'PDG2024'),
 'ms_MeV'      : (mpf('93.5'),          'PDG2024'),
 'md_MeV'      : (mpf('4.70'),          'PDG2024'),
 'mu_MeV'      : (mpf('2.16'),          'PDG2024'),
 'mrho_MeV'    : (mpf('775.26'),        'PDG2024'),
 'mpi_MeV'     : (mpf('139.57039'),     'PDG2024'),
 'lambda_W'    : (mpf('0.22501'),       'PDG2024 Wolfenstein'),
 'A_W'         : (mpf('0.826'),         'PDG2024 Wolfenstein'),
 'rhobar'      : (mpf('0.1591'),        'PDG2024'),
 'etabar'      : (mpf('0.3523'),        'PDG2024'),
 's2t12'       : (mpf('0.307'),         'PDG2024 / NuFIT'),
 's2t13'       : (mpf('0.02203'),       'PDG2024 / NuFIT'),
 's2t23'       : (mpf('0.572'),         'PDG2024 / NuFIT'),
 'gamma_CKM'   : (mpf('65.9'),          'PDG2024 gamma, deg'),
 'mpme'        : (mpf('1836.152673426'),'CODATA2022'),
}

def rel(pred, key):
    obs = M[key][0]
    return (pred-obs)/obs

rows = []
def add(tag, expr_txt, printed_val, printed_err, val, key, ncorr, dateorder, src):
    rows.append(dict(tag=tag, expr=expr_txt, printed=printed_val, perr=printed_err,
                     recomp=val, obs=M[key][0], obs_src=M[key][1],
                     eps=rel(val,key), ncorr=ncorr, dateorder=dateorder, src=src))

# --- EM ---
a_bare = a0
add('A0','alpha_0 = r_oct*r_tet/pi (bare)','0.00740806','+1.517%',a_bare,'inv_alpha_dummy' if False else 'inv_alpha',0,'n/a','App D.2') if False else None
add('A1','alpha = a0(1-2a0)  -> 1/alpha','137.018','-0.013%',1/(a0*(1-2*a0)),'inv_alpha',1,'post-hoc (D.2 records 1.52% gap, D.3 supplies factor)','Monograph 4.1 / App D.2-D.3')
add('A2','alpha = a0(1-3a0)/(1-a0) -> 1/alpha','137.0336','-0.0018%',1/(a0*(1-3*a0)/(1-a0)),'inv_alpha',2,'post-hoc','App D.3 all-orders')
add('A3','1/alpha = 2*pi/x_lep','137.046','+0.007%',2*pi/x_lep,'inv_alpha',0,'post-hoc','App E (Vol1 p.11044)')
# --- EW ---
s2w_tree = r_tet**2/(r_oct**2+r_tet**2)
add('W1','sin^2thW(tree) = r_tet^2/(r_oct^2+r_tet^2)','0.22744','+1.64% vs MSbar',s2w_tree,'s2w_MSbar',0,'n/a','Monograph 5.1')
add('W1b','sin^2thW(tree) vs on-shell CODATA','0.22744','-',s2w_tree,'s2w_onshell',0,'n/a','recomp here')
# --- leptons ---
mP_MeV = M['mP_GeV'][0]*mpf('1e3')
S_e_34D = (pi**5+pi)/6
S_e_C2  = (pi**5/6)/(1-a0*(4*pi+1)/pi**2)
S_e_bare= S_D4
S_e_xlep= S_D4/(1-x_lep)
add('E0','m_e = m_P exp(-pi^5/6)','0.8628 MeV','+68.8%',mP_MeV*exp(-S_e_bare),'me_MeV',0,'n/a','App Z / Phase 34D')
add('E1','m_e = m_P exp(-S_D4/(1-x_lep))','0.5313 MeV','+3.97%',mP_MeV*exp(-S_e_xlep),'me_MeV',1,'post-hoc','App AB/Phase 11')
add('E2','m_e = m_P exp(-(pi^5+pi)/6)','0.511117 MeV','+0.0229%',mP_MeV*exp(-S_e_34D),'me_MeV',1,'post-hoc','Phase 34D')
add('E3','m_e = m_P exp(-(pi^5/6)/(1-a0(4pi+1)/pi^2))','0.510927 MeV','-0.014%',mP_MeV*exp(-S_e_C2),'me_MeV',2,'post-hoc','One Medium App C.2')
# Koide
cosd_LO = -r_oct/(r_oct+r_tet)
d_LO = acos(cosd_LO)
d_35A = d_LO + r_oct**2/(r_tet*pi**2)
d_36A = d_LO + r_oct**2/(3*r_tet*pi)
def koide_masses(delta, me):
    vK = sqrt(me)/(1+sqrt(2)*__import__('mpmath').cos(delta))
    from mpmath import cos as c
    mm = (vK*(1+sqrt(2)*c(2*pi/3+delta)))**2
    mt = (vK*(1+sqrt(2)*c(4*pi/3+delta)))**2
    return mm, mt
mm35, mt35 = koide_masses(d_35A, mP_MeV*exp(-S_e_34D))
mm36, mt36 = koide_masses(d_36A, mP_MeV*exp(-S_e_34D))
add('K1','Koide delta = acos(-r_oct/(r_oct+r_tet))','2.27610 rad','-1.749%',d_LO,'s2t12',0,'n/a','Phase 13B')  # eps meaningless; flagged
add('K2','m_mu via Koide, delta(35A)=dLO+r_oct^2/(r_tet pi^2)','105.5719','-0.082%',mm35,'mmu_MeV',2,'post-hoc','Phase 35A')
add('K3','m_mu via Koide, delta(36A)=dLO+r_oct^2/(3 r_tet pi)','-','-',mm36,'mmu_MeV',2,'post-hoc','Phase 36A')
add('K4','m_tau via Koide from m_e(BCT)+m_mu(obs)','1776.9694','+0.006158%',mpf('1776.969418'),'mtau_MeV',2,'post-hoc','Phase 35A')
# --- quarks ---
mt = mpf('172000')
for tag,n,key,lbl in [('Q_s',mpf(12),'ms_MeV','m_s'),('Q_b',mpf(6),'mb_MeV','m_b bare n=6'),
                      ('Q_c',mpf(8),'mc_MeV','m_c bare n=8'),('Q_d',mpf(17),'md_MeV','m_d bare n=17'),
                      ('Q_u',mpf(18),'mu_MeV','m_u bare n=18')]:
    add(tag,'m_q = m_t exp(-S_Td*n_q/24), n=%s'%int(n),'-','-',mt*exp(-S_Td*n/24),key,0,'n/a','Monograph 7.1 / App A')
dn_d = r_tet*(1+r_tet/r_oct)
add('Q_d2','m_d = m_t exp(-S_Td*(17-r_tet(1+r_tet/r_oct))/24)','4.6437','-0.56%',mt*exp(-S_Td*(17-dn_d)/24),'md_MeV',1,'post-hoc (closes -10.8%)','Phase 22A')
dn_u = r_tet - r_tet**2/r_oct
add('Q_u2','m_u = m_t exp(-S_Td*(18+r_tet-r_tet^2/r_oct)/24)','2.1582','-0.08%',mt*exp(-S_Td*(18+dn_u)/24),'mu_MeV',1,'post-hoc','Phase 24A')
add('Q_b2','m_b = m_t exp(-S_Td*(6-dn_d/4)/24)','4171.83','-0.20%',mt*exp(-S_Td*(6-dn_d/4)/24),'mb_MeV',2,'post-hoc','Phase 24B')
add('Q_b3','m_b = m_t*pi*a0*(1+5a0)','4182.55','-0.011%',mt*pi*a0*(1+5*a0),'mb_MeV',1,'post-hoc','Phase ~63 (Vol2 p.7523)')
# --- hadrons ---
mpi = M['mpi_MeV'][0]
add('H1','m_rho = m_pi/(2 sqrt(a0)) * (1-3a0/2)','775.5','+0.035%',mpi/(2*sqrt(a0))*(1-3*a0/2),'mrho_MeV',1,'post-hoc','Letter 11/12')
hbarc = mpf('197.3269804')
mrho_bct = mpi/(2*sqrt(a0))*(1-3*a0/2)
add('H2','r_p = hbar c/(m_rho) * (1+a0)','0.8386 fm','-0.33%',hbarc/mrho_bct*(1+a0),'rp_fm',1,'post-hoc','Monograph 16.1')
# --- mixing ---
add('C1','lambda = 2 r_tet (1+3a0/8)','0.22537','+0.013%',2*r_tet*(1+3*a0/8),'lambda_W',1,'post-hoc','Letter 86')
add('C2','A = (1/(1+r_oct))(1-a0/2)','0.8254','-0.078%',(1/(1+r_oct))*(1-a0/2),'A_W',1,'post-hoc','Letter 87')
add('C3','etabar = 3 r_tet','0.3371','-0.603%',3*r_tet,'etabar',0,'n/a','Letter 90')
beta = acos(2*r_oct)
add('C4','rhobar = 3 r_tet / tan(acos(2 r_oct))','0.157416','-1.00%',3*r_tet/tan(beta),'rhobar',0,'n/a','Letter 90')
add('C5','delta_CKM = acos(1/3) deg','70.53','+1.6%',acos(mpf(1)/3)*180/pi,'gamma_CKM',0,'n/a','One Medium 11 / Table B.9')
add('C6','beta = acos(2 r_oct) deg','65.53','+0.132%',beta*180/pi,'gamma_CKM',0,'n/a','Letter 87/90')
add('P1','sin^2 th13 = 3 a0','0.022224','+1.02%',3*a0,'s2t13',0,'n/a','App (Vol2 p.4324)')
add('P2','sin^2 th12 = 1/3 - r_tet r_oct','0.310060','+1.00%',mpf(1)/3-r_tet*r_oct,'s2t12',0,'n/a','Monograph 11 / HR5')
# --- gravity ---
add('G1','m_P = M_R/a0^2 with M_R = m_P a0^2','1.220e19 GeV','-0.08%',mpf('6.695e14')/a0**2,'mP_GeV',0,'CIRCULAR - see note','Monograph 19.1 vs App GG2')
add('G2','m_p/m_e = 6 pi^5','1836.118109','+0.0019%',6*pi**5,'mpme',0,'n/a','App F/G (corpus: NOT derived)')

print(f"{'tag':6s} {'printed':>14s} {'recomputed':>20s} {'observed':>18s} {'eps_recomp':>12s} {'printed err':>12s} ncorr")
for r in rows:
    print(f"{r['tag']:6s} {str(r['printed'])[:14]:>14s} {mp.nstr(r['recomp'],12):>20s} {mp.nstr(r['obs'],10):>18s} "
          f"{mp.nstr(r['eps']*100,4):>12s}% {str(r['perr'])[:12]:>12s} {r['ncorr']}")
import pickle
pickle.dump([{k:(str(v) if not isinstance(v,(int,str)) else v) for k,v in r.items()} for r in rows], open('census.pkl','wb'))
