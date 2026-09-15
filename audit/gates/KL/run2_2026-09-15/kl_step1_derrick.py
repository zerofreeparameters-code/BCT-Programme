# GATE KL — Step 1: Derrick scaling, below-uniform, and c4/c2 ~ xi^2.
# Deterministic. Demonstrates the load-bearing stability facts.
from mpmath import mp, mpf, sqrt, nstr
mp.dps = 40
xi = mpf('2.317543794911664963039020806144813022013')  # xi/a from step0

print("=== FACT A: below-uniform is impossible for a positive-definite energy ===")
print("E[n] = INT( c2|dn|^2 + c4 F^2 ),  c2,c4 >= 0, no odd-derivative (DMI/chiral) term.")
print("Both integrands are pointwise >= 0.  Uniform n=const has E=0.")
print("=> uniform is the GLOBAL minimum over ALL configs and ALL topological sectors.")
print("=> NO modulated texture can be below uniform.  SC-KL-3 (needs below-uniform) is UNREACHABLE.")
print()

print("=== FACT B: 3D Derrick scaling  n_lambda(x)=n(x/lambda) ===")
# In d dims, term with 2k derivatives scales as lambda^(d-2k).
for d,label in [(3,'3D (single knot / infinite space)')]:
    e2 = d-2   # two-derivative term exponent
    e4 = d-4   # four-derivative term exponent
    print(f"{label}: E2 ~ lambda^{e2}, E4 ~ lambda^{e4}")
    print(f"  c4=0 (as WRITTEN in App JH): E(lambda)=c2 I2 lambda^{e2} -> minimized at lambda->0 => COLLAPSE.")
    print(f"  c4>0: E=c2 I2 lambda + c4 I4/lambda -> lambda* = sqrt(c4 I4/(c2 I2)).")
print()

print("=== FACT C: c4/c2 ~ xi^2  (gradient expansion) ===")
print("[c2]=E/L, [c4]=E*L  => c4/c2 has dimension L^2. The only massive scale is the")
print("amplitude (Higgs) mode, gap ~ 1/xi. So c4/c2 = O(xi^2), lambda* = O(xi).")
print(f"  => lambda* ~ xi = {nstr(xi,20)} a  (natural knot size).")
print()

print("=== FACT D: 2D baby-skyrmion (the periodic sheet charge) scaling ===")
d=2; e2=d-2; e4=d-4
print(f"2D: E2 ~ lambda^{e2} (scale-invariant, Belavin-Polyakov), E4 ~ lambda^{e4}.")
print("  E(lambda)=c2 I2 + c4 I4/lambda^2 -> monotonically DECREASING => texture wants to GROW.")
print("  No n-hat POTENTIAL exists (GP quartic at |Psi|=const is n-independent) => no geometry-set")
print("  finite size. In a crystal, size is capped by the PERIOD => period is an IMPOSED length.")
print()

print("=== FACT E: self-consistency of period ===")
period = mpf(1)   # one charge per primitive cell, period = a
print(f"  natural size lambda* ~ xi = {nstr(xi,20)} a ;  cell period = {nstr(period,3)} a")
print(f"  lambda*/period = {nstr(xi/period,20)}  != 1")
print("  => the geometry-fixed size does NOT equal the FCC period.")
print("  => the period must be imposed as a SECOND, independent length (SC-KL-2 trigger).")
