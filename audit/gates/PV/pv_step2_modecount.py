"""
GATE PV - Step 2. Physical propagating-mode count by Hamiltonian (Dirac) counting.

Phase-space DOF per point = 2 * (config components).
Each first-class constraint removes 2 phase-space DOF (constraint + gauge orbit).
Physical modes = (physical phase-space DOF)/2.

Compare:
  Maxwell (rank-1)         : A_i (3), Gauss d_i E^i = rho (1 constraint)
  scalar-charge (Gate P)   : A_ij sym (6), Gauss d_i d_j E^ij = rho (1 constraint)
  vector-charge (Gate PV)  : A_ij sym (6), Gauss d_i E^ij = rho^j (3 constraints)
  vector-charge traceless  : A_ij sym-traceless (5), Gauss d_i E^ij = rho^j (3 constraints)
"""
def modes(config, first_class):
    ps = 2*config
    ps_phys = ps - 2*first_class
    return ps_phys//2, ps_phys

for name, cfg, fc in [
    ("Maxwell rank-1            ", 3, 1),
    ("scalar-charge (P)  full   ", 6, 1),
    ("scalar-charge (P)  tracel.", 5, 1),
    ("vector-charge (PV) full   ", 6, 3),
    ("vector-charge (PV) tracel.", 5, 3),
]:
    m, ps = modes(cfg, fc)
    print(f"{name}: config={cfg}  first-class={fc}  -> physical modes = {m}")

print()
print("Maxwell photon target: 2 transverse polarisations, NO physical longitudinal.")
print("vector-charge full    : 3 physical modes  -> 2 transverse + 1 PHYSICAL longitudinal")
print("                        (the extra compressional mode Maxwell does not have).")
print("vector-charge traceless: 2 physical modes, but they live in Eg(+)T2g tensor")
print("                        sector, NOT the T1u transverse-vector doublet.")
