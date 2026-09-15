#!/usr/bin/env python3
# GATE PROMOTE - Step 0, built COLD.
from fractions import Fraction as F
sizes=[1,8,6,6,3,1,8,6,6,3]; order=sum(sizes); assert order==48
chars={
 "A1g":[1,1,1,1,1,1,1,1,1,1],"A2g":[1,1,-1,-1,1,1,1,-1,-1,1],
 "Eg":[2,-1,0,0,2,2,-1,0,0,2],"T1g":[3,0,-1,1,-1,3,0,-1,1,-1],
 "T2g":[3,0,1,-1,-1,3,0,1,-1,-1],"A1u":[1,1,1,1,1,-1,-1,-1,-1,-1],
 "A2u":[1,1,-1,-1,1,-1,-1,1,1,-1],"Eu":[2,-1,0,0,2,-2,1,0,0,-2],
 "T1u":[3,0,-1,1,-1,-3,0,1,-1,1],"T2u":[3,0,1,-1,-1,-3,0,-1,1,1],
}
irreps=list(chars); dim={g:chars[g][0] for g in irreps}; sq=[0,1,0,4,0,0,1,0,4,0]
def inner(a,b): return F(sum(sizes[k]*a[k]*b[k] for k in range(10)),order)
def dec(ch): return {g:int(inner(ch,chars[g])) for g in irreps if inner(ch,chars[g])!=0}
def ss(g):
    x=chars[g]; return [(x[k]*x[k]+x[sq[k]])//2 if (x[k]*x[k]+x[sq[k]])%2==0 else F(x[k]*x[k]+x[sq[k]],2) for k in range(10)]
for a in irreps:
    for b in irreps: assert inner(chars[a],chars[b])==(1 if a==b else 0)
print("O_h orthonormal; |O_h|=",order,"; sum d^2=",sum(d*d for d in dim.values()))
strain=dec(ss("T1u")); print("\nStrain [T1u x T1u]_sym =",strain); assert strain=={"A1g":1,"Eg":1,"T2g":1}
aniso={"Eg","T2g"}
print("\nSTEP 0 ISOTROPY MAP")
for g in irreps:
    d=dim[g]; M="DISCRETE(Z2)" if d==1 else f"cont d={d}"
    s=dec(ss(g)); v="ISOTROPIC(bulk)" if g=="A1g" else ("ANISOTROPIC" if any(k in s for k in aniso) else "iso-safe*")
    print(f"  {g:4} dim={d} {M:12} sym^2={s} -> {v}")
print("\nPincer: multi-D spatial condensed -> anisotropy; 1-D -> discrete;")
print("only continuous iso-safe route = richer local DOF, quantum-disordered (Step 2).")
