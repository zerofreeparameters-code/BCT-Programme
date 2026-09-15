#!/usr/bin/env python3
# GATE PROMOTE - manifolds + p-form polarization guards. Built COLD.
from math import comb
print("A) MANIFOLDS (dim, pi3, ordered Goldstones)")
for name,dM,pi3 in [("S^1 corpus",1,"0"),("S^2=O(3)/O(2)",2,"Z(hopfions)"),
                    ("RP^2 nematic",2,"Z"),("S^3=SU(2)",3,"Z"),("CP^1~S^2",2,"Z")]:
    print(f"  {name:16} dimM={dM} pi3={pi3:12} Goldstones(ordered)={dM}")
print("  ordered S^2 -> magnons NOT photon; CP^1 photon needs the DISORDERED phase.")
print("\nB) MASSLESS p-FORM POLARIZATIONS D=4 = C(D-2,p)")
D=4
for p,lab in [(0,"phonon"),(1,"PHOTON"),(2,"Kalb-Ramond"),(3,"")]:
    print(f"  {p}-form {lab:12}: {comb(D-2,p)}")
print("  guards: scalar phonon=0-form(1); KR 2-form(1)!=photon(2); transverse phonons=no Gauss law.")
print("\nC) HARD-CONSTRAINT LEDGER (Step 2 crux)")
print("  neutral scalar: no separable local charge, soft double layer -> NO hard Gauss law")
print("  spin ice/link rotors: hard law POSSIBLE (pyrochlore) but DOF+coupling not in corpus")
print("  BCT/FCC voids: not corner-sharing; ice/ring coupling=SELECTED FIT; deconf=analogy")
print("  => hard constraint NOT geometry-supplied")
