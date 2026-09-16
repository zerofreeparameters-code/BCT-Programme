from mpmath import mp, mpf, mpc, sqrt, sin, cos, acos, exp, arg, pi, matrix, det
mp.dps = 50

# --- Standard PDG CKM parametrisation, angles ~ observed, phase = BCT's delta = arccos(1/3)
s12, s23, s13 = mpf('0.2248'), mpf('0.0422'), mpf('0.00365')
c12, c23, c13 = sqrt(1-s12**2), sqrt(1-s23**2), sqrt(1-s13**2)

def Vckm(delta):
    d = mpc(0, delta)
    e_m, e_p = exp(-d), exp(d)
    R23 = matrix([[1,0,0],[0,c23,s23],[0,-s23,c23]])
    U13 = matrix([[c13,0,s13*e_m],[0,1,0],[-s13*e_p,0,c13]])
    R12 = matrix([[c12,s12,0],[-s12,c12,0],[0,0,1]])
    return R23*U13*R12

def jarlskog(V):
    # J = Im(V_us V_cb V_ub^* V_cs^*)  (indices: u=0,c=1,t=2 rows ; d=0,s=1,b=2 cols)
    return (V[0,1]*V[1,2]*mp.conj(V[0,2])*mp.conj(V[1,1])).imag

dBCT = acos(mpf(1)/3)
V0   = Vckm(mpf(0))       # real CKM (App EL's actual texture: real rotations only)
VB   = Vckm(dBCT)         # CKM carrying BCT's claimed phase

print("delta_BCT = arccos(1/3) =", mp.nstr(dBCT*180/pi,8), "deg")
print("J(real CKM, delta=0)      =", mp.nstr(jarlskog(V0),6), "  <- App EL real texture")
print("J(CKM, delta=arccos1/3)   =", mp.nstr(jarlskog(VB),6), "  <- corpus headline claim")
print("arg det V_CKM(real)       =", mp.nstr(arg(det(V0)),6), "rad")
print("arg det V_CKM(phased)     =", mp.nstr(arg(det(VB)),6), "rad   (det is a pure rotation -> 0)")

print("\n--- Is arg det(M_u M_d) fixed by (real masses)+(CKM,J) ? ---")
# masses real positive (MeV), irrelevant to the PHASE of det beyond being real>0
Su = matrix([mpf('2.16'), mpf('1270'), mpf('172500')])   # up-type
Sd = matrix([mpf('4.67'), mpf('93.4'), mpf('4180')])     # down-type
# Weak basis: M_u = diag(real) (V_uL=V_uR=1). M_d = V_CKM * diag(Sd) * W^dagger, W = right-handed unitary (UNOBSERVABLE)
def Md(W):
    D = matrix([[Sd[0],0,0],[0,Sd[1],0],[0,0,Sd[2]]])
    return VB * D * W
def argdet_Mq(W):
    Mu = matrix([[Su[0],0,0],[0,Su[1],0],[0,0,Su[2]]])
    return arg(det(Mu)*det(Md(W)))
I3  = matrix([[1,0,0],[0,1,0],[0,0,1]])
# choice A: W = 1
print("choice A  W=I         : arg det(M_u M_d) =", mp.nstr(argdet_Mq(I3),6), "rad")
# choice B: W = diag(e^{i phi},1,1), phi arbitrary -- same masses, same V_CKM, same J
for phi in [mpf('0.7'), mpf('1.9'), -mpf('2.4')]:
    W = matrix([[exp(mpc(0,phi)),0,0],[0,1,0],[0,0,1]])
    # confirm V_CKM and J unchanged by W (right-handed): rebuild CKM from left rotations only -> unchanged by construction
    print(f"choice B  W=diag(e^i*{mp.nstr(phi,3)},1,1): arg det(M_u M_d) =", mp.nstr(argdet_Mq(W),6),
          "rad   (masses,V_CKM,J all identical)")
