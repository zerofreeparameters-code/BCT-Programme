#!/usr/bin/env python3
"""
dls_q3_q5.py — Gate DL-STIFF, Q3 and Q5.

Q3: the comparison table against beta_c. No route survived Q1, so there is NO derived
    beta to compare; the candidate beta_geom is tabulated and LABELLED as not derived,
    which is what the card's §5 SC-DLS-2 verdict requires to be reported.
Q5: the DL theory's free-input count after this gate, in TWIST's cost-table form.

Also re-verifies the card §7 identity cold (independent of dls_deskcheck.py).
"""
from mpmath import mp, mpf, sqrt, pi, nstr

mp.dps = 30
R_DIG = 10
p = lambda label, v: print(f"{label:<52s} {nstr(v, R_DIG)}")

r_oct = (sqrt(2) - 1) / 2
r_tet = (sqrt(6) - 2) / 4
alpha0 = r_oct * r_tet / pi
xi = 1 / sqrt(8 * r_oct * r_tet)
alpha_codata = mpf("0.0072973525643")

print("=" * 78)
print("CARD §7 IDENTITY, RE-VERIFIED COLD (30 digits working, 10 reported)")
print("=" * 78)
f1 = 1 / (4 * pi * alpha0)
f2 = 1 / (4 * r_oct * r_tet)
f3 = 2 * xi ** 2
p("r_oct = (sqrt2 - 1)/2", r_oct)
p("r_tet = (sqrt6 - 2)/4", r_tet)
p("alpha_0 = r_oct r_tet / pi", alpha0)
p("1/alpha_0", 1 / alpha0)
p("xi/a = 1/sqrt(8 r_oct r_tet)", xi)
p("form 1: 1/(4 pi alpha_0)", f1)
p("form 2: 1/(4 r_oct r_tet)", f2)
p("form 3: 2 xi^2/a^2", f3)
p("max pairwise difference", max(abs(f1 - f2), abs(f2 - f3), abs(f1 - f3)))
p("1/(4 pi alpha_CODATA) for comparison", 1 / (4 * pi * alpha_codata))
p("fractional gap alpha_0 vs alpha_CODATA", abs(alpha0 - alpha_codata) / alpha_codata)
print("The three forms agree because they are the same expression; this is an identity by")
print("the MINIMAL_BCT §1.3 definitions and carries no information about beta (see R6a).")

print()
print("=" * 78)
print("Q3 — COMPARISON AGAINST beta_c")
print("=" * 78)
beta_geom = f3
rows = [
    ("hypercubic Z4 (Wilson, standard)", mpf("1.0111"), "standard 4D lattice result"),
    ("D4, CRIT2 card convention", mpf("0.6150"), "Gate CRIT2"),
    ("D4, Katz-Nogradi convention", mpf("1.2300"), "Gate CRIT2"),
]
print(f"{'lattice / convention':<36s} {'beta_c':>9s} {'beta_geom/beta_c':>18s}")
print("-" * 78)
for name, bc, src in rows:
    print(f"{name:<36s} {nstr(bc, 6):>9s} {nstr(beta_geom / bc, 6):>18s}")
print(f"{'void network (FCC voids x time)':<36s} {'PENDING':>9s} {'DL-BETA pending':>18s}")
print("-" * 78)
print("SURVIVING beta FROM THIS GATE: none. Every route R1-R5 and every R6 route found was")
print("closed by its pre-registered kill test (Q1). The row below is therefore the CANDIDATE")
print("number, not a result of this gate:")
p("  candidate beta_geom = 2 xi^2/a^2 (NOT DERIVED)", beta_geom)
print("  Tier: this number is an identity of the pinned definitions. Its status after this")
print("  gate is 'the value beta would have IF some route fixed it', and no route does.")

print()
print("=" * 78)
print("Q5 — COST TABLE: free inputs of the DL theory after this gate (TWIST form)")
print("=" * 78)
cost = [
    ("the added compact U(1) link field on the void network", 1,
     "not in the corpus; MINIMAL_BCT §1.1 is one complex scalar (PROVEN, Gate RANK)"),
    ("beta, the plaquette coupling", 1,
     "THIS GATE: SC-DLS-2. Every route closed; beta is an input of S_gauge"),
    ("the charge carrier", 1,
     "Gate DL-MATTER, not run. Vortex strings are neutral under a field the medium is neutral under"),
    ("the alpha identification", 0,
     "subsumed: with beta free, beta IS fixed by fitting the observed alpha. Not a second input"),
]
print(f"{'input':<54s} {'cost':>5s}")
print("-" * 78)
tot = 0
for name, c, note in cost:
    tot += c
    print(f"{name:<54s} {c:>5d}")
print("-" * 78)
print(f"{'TOTAL free inputs of the DL theory':<54s} {tot:>5d}")
print()
for name, c, note in cost:
    print(f"  [{c}] {name}")
    print(f"      {note}")
print()
print("Notes on the counting, stated so it can be checked:")
print("  * The alpha identification is scored 0 BECAUSE beta is free: one free coupling and")
print("    one coupling observable are the same parameter. Scoring both 1 would double-count.")
print("  * Counterfactually, had this gate returned SC-DLS-1, the table would read")
print("    field 1 + beta 0 + carrier 1 + alpha-identification 0 = 2, and the theory would")
print("    predict alpha = alpha_0 = 1/134.99 against the measured 1/137.036 - a 1.5 % miss")
print("    that FWD/STAT already closed as a selected correction map. A derived beta would")
print("    therefore have been a FALSIFIABLE and prima facie FALSE prediction, not a free win.")
p("    alpha_0 as 1/alpha_0", 1 / alpha0)
p("    CODATA as 1/alpha", 1 / alpha_codata)
print("  * The theory as it stands is therefore at minimum THREE-INPUT, and its only")
print("    geometric content is the lattice itself (isotropy + two polarisations, PROVEN by")
print("    Gate DL CN-DL-01/04), exactly as the scoping note §6 forecast.")
