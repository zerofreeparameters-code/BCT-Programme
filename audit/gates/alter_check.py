from fractions import Fraction as F
import itertools
def mod1(v): return tuple(F(x)%1 for x in v)
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)
fcc = [(0,0,0),(0,F(1,2),F(1,2)),(F(1,2),0,F(1,2)),(F(1,2),F(1,2),0)]
fcc=[mod1(v) for v in fcc]
def in_fcc(v): return mod1(v) in fcc
print("FCC Bravais: corner->centre of BCT cell (=(1/2,1/2,0) fcc) is lattice vec:", in_fcc((F(1,2),F(1,2),0)))
print("(1/2,1/2,1/2) is FCC lattice vector:", in_fcc((F(1,2),F(1,2),F(1,2))))
t1=(F(1,4),)*3; t2=(F(3,4),)*3
print("T2 = -T1 mod 1 (inversion through atom):", mod1(neg(t1))==t2)
print("T2 = T1 + FCC vector:", any(mod1(add(t1,v))==t2 for v in fcc))
oct_=(F(1,2),)*3
print("oct voids form FCC translate of atoms:", all(in_fcc(add(o, neg(oct_))) for o in [mod1(add(oct_,v)) for v in fcc]))
# rutile: Ti (0,0,0),(1/2,1/2,1/2); O at ±(u,u,0), (1/2±u,1/2∓u,1/2)
u=F(3,10)
O=[mod1((u,u,0)),mod1((-u,-u,0)),mod1((F(1,2)+u,F(1,2)-u,F(1,2))),mod1((F(1,2)-u,F(1,2)+u,F(1,2)))]
shift=lambda v: mod1(add(v,(F(1,2),)*3))
print("rutile: body-centring translation maps O->O:", set(map(shift,O))==set(O))
c4=lambda v:(-v[1],v[0],v[2])
print("rutile: 4_2 screw {C4z|1/2,1/2,1/2} maps O->O:", set(mod1(add(c4(v),(F(1,2),)*3)) for v in O)==set(O))
inv=lambda v: mod1(neg(v))
print("rutile: inversion maps Ti sublattice A->A (not A->B):", inv((0,0,0))==(0,0,0))
