from mpmath import mp, mpf, atan, pi, sqrt
mp.dps = 30
r_oct_over_r_tet = mpf('1.8430')          # ledger close-packing constant
r_tet_over_r_oct = 1/r_oct_over_r_tet
a0 = mpf('0.007408')
gt = pi/2 - atan(r_tet_over_r_oct) + atan(sqrt(a0))
obs = mpf('1.1960')
print("r_tet/r_oct        =", mp.nstr(r_tet_over_r_oct,6), "(doc 0.5426)")
print("arctan(r_tet/r_oct)=", mp.nstr(atan(r_tet_over_r_oct),6), "(doc 0.4971)")
print("arctan(sqrt a0)    =", mp.nstr(atan(sqrt(a0)),6), "(doc 0.08591)")
print("delta_GT           =", mp.nstr(gt,6), "rad  (doc 1.1596)")
print("error vs obs       =", mp.nstr((gt-obs)/obs*100,4), "%  (doc -3.0%)")
