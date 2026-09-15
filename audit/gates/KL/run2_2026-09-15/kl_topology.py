# GATE KL — periodic topology: homotopy classes [T^3, S^2] vs pi_3(S^2).
# Pontryagin / obstruction theory for maps from a closed oriented 3-manifold X to S^2.
from math import gcd
from functools import reduce

print("=== Single hopfion (App JH's object): domain S^3 ===")
print("  [S^3, S^2] = pi_3(S^2) = Z,  generator = Hopf map, invariant H in Z.")
print("  This REQUIRES the domain to be S^3 (B^3 with constant boundary value).")
print()
print("=== Periodic knot-lattice (the KL escape): domain T^3 (3-torus) ===")
print("  [X,S^2] for closed oriented 3-manifold X (Pontryagin):")
print("   * PRIMARY class  in H^2(X;Z)  = pullback of the S^2 area generator")
print("       (a framed 1-manifold / the preimage of a regular point).")
print("   * SECONDARY 'Hopf' invariant in  H^3(X;Z) / ( 2*alpha  cup  H^1(X;Z) ).")
print()
print("  For X = T^3:  H^1=Z^3, H^2(T^3;Z)=Z^3, H^3(T^3;Z)=Z.")
print("   * PRIMARY: (m1,m2,m3) in Z^3 = the three pi_2(S^2)=Z 'sheet' (baby-skyrmion)")
print("     charges through the coordinate 2-tori T_yz, T_zx, T_xy.  <-- the protected charges")
print("   * SECONDARY Hopf part lives in  Z / (2*gcd(m1,m2,m3)) when (m1,m2,m3) != 0.")
print()

def hopf_modulus(m):
    g = reduce(gcd, [abs(x) for x in m])
    return 2*g  # residual Hopf invariant defined mod 2*gcd; 0 => full Z (only if all m=0)

for m in [(0,0,0),(1,0,0),(1,1,1),(2,0,0),(2,4,6)]:
    mod = hopf_modulus(m)
    if m==(0,0,0):
        print(f"  sheet charges {m}: Hopf invariant is a full integer in Z (S^3-like sector).")
    else:
        print(f"  sheet charges {m}: gcd={reduce(gcd,[abs(x) for x in m])}, "
              f"Hopf invariant defined only MOD {mod}  =>  NOT an independent integer per cell.")
print()
print("=== CONSEQUENCE ===")
print("  A space-filling periodic S^2 texture carrying nonzero sheet charge does NOT have")
print("  a well-defined integer 'Hopf charge per cell'. The clean protected charge is the")
print("  pi_2 SHEET charge (a baby-skyrmion crystal), not a 3D hopfion crystal.")
print("  Going periodic to escape Derrick therefore SACRIFICES the very pi_3(S^2)=Z Hopf")
print("  structure that motivated App JH's hopfion. The 'woven knot lattice' is, topologically,")
print("  a stacked baby-skyrmion crystal -- a different object from the claimed hopfion medium.")
