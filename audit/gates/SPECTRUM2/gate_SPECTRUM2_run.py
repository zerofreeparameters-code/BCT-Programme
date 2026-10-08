#!/usr/bin/env python3
"""Gate SPECTRUM2 run script (8 Oct 2026).
Card: audit/gates/gate_SPECTRUM2_prompt.md @ commit d3eee7766d42bc0d93a81846cbd1523d1762e3ba
Card SHA-256: d5d052c9483579ac8dcf9189d21687d5d75a201008f87c2b080841cdf1ed285c
One loop, step thresholds. mpmath, 60 dps working, 40 dps reported.
All inputs are the card's values (section 4.1) and Gate LOG section 3.3 (T5 only), unchanged.

Reading of MARGINAL (fixed and sent to Michel before this script was written):
  centre: any mass below threshold -> EXCLUDED; else any mass < 3*threshold -> MARGINAL; else PASS
  corners (A_Y +-3, A_2 +-3): plain threshold test. Centre PASS but excluded at a corner -> MARGINAL.
  Centre EXCLUDED but not excluded at some corner -> MARGINAL. Corner with x<0 -> MARGINAL.
  MARGINAL counts neither as pass (SC-SPEC2-1) nor as fail (SC-SPEC2-2).
"""
from mpmath import mp, mpf, log, pi, exp, nstr
from itertools import product
mp.dps = 60
R = lambda x: nstr(x, 40)
S = lambda x, n=6: nstr(x, n)
TWO_PI = 2*pi

# ---- 4.1 inputs -------------------------------------------------------------
MP, MZ, MT = mpf('1.220890e19'), mpf('91.1876'), mpf('172.57')
INV_A_MZ, S2W, ALPHA_S = mpf('127.951'), mpf('0.23122'), mpf('0.1180')
BY_SM, B2_SM = mpf(41)/6, mpf(-19)/6
B3_LO, B3_HI = mpf(-23)/3, mpf(-7)
INV2_MZ, INVY_MZ, INV3_MZ = S2W*INV_A_MZ, (1-S2W)*INV_A_MZ, 1/ALPHA_S
LZ = log(MP/MZ)

A_Y = INVY_MZ - BY_SM*LZ/TWO_PI
A_2 = INV2_MZ - B2_SM*LZ/TWO_PI
A_3 = INV3_MZ - B3_LO*log(MT/MZ)/TWO_PI - B3_HI*log(MP/MT)/TWO_PI

# ---- 4.2 coefficients rebuilt from field content -----------------------------
# Dirac multiplet = (colour dim, SU(2) dim, Y).  Q = T3 + Y.
h, third = mpf(1)/2, mpf(1)/3
T2 = {1: mpf(0), 2: h, 3: mpf(2)}          # Dynkin index of SU(2) rep by dimension
T3c = {1: mpf(0), 3: h}                    # Dynkin index of SU(3) rep by dimension
def coeffs(mults):
    bY = b2 = b3 = bem = mpf(0)
    for (dc, dw, Y) in mults:
        bY += mpf(4)/3 * dc*dw * Y**2
        b2 += mpf(4)/3 * T2[dw] * dc
        b3 += mpf(4)/3 * T3c[dc] * dw
        j = mpf(dw-1)/2
        t3s = [j - k for k in range(dw)]
        bem += mpf(4)/3 * dc * sum((t3 + Y)**2 for t3 in t3s)
    return bY, b2, b3, bem

CONTENT = {
 'G': [(3,2,mpf(1)/6), (3,1,mpf(2)/3), (3,1,-third), (1,2,-h), (1,1,mpf(-1)), (1,1,mpf(0))],
 'T': [(1,3,mpf(0))],
 'L': [(1,2,h)],
 'Q': [(3,2,mpf(1)/6)],
}
CARD = {'G': (mpf(40)/9, mpf(8)/3, mpf(8)/3, mpf(64)/9),
        'T': (mpf(0),    mpf(8)/3, mpf(0),   mpf(8)/3),
        'L': (mpf(2)/3,  mpf(2)/3, mpf(0),   mpf(4)/3),
        'Q': (mpf(2)/9,  mpf(2),   mpf(4)/3, mpf(20)/9)}
B = {}
print("== 4.2 coefficient rebuild ==")
for k, m in CONTENT.items():
    c = coeffs(m)
    for got, want in zip(c, CARD[k]):
        assert abs(got - want) < mpf(10)**-50, (k, got, want)
    assert abs(c[0] + c[1] - c[3]) < mpf(10)**-50      # b_em = b_Y + b_2 = (4/3) sum Nc Q^2
    B[k] = c
    print(k, "b_Y, b_2, b_3, b_em =", [S(v, 12) for v in c], "asserted")

THRESH = {'G': mpf(2000), 'Q': mpf(2000), 'T': mpf(1000), 'L': mpf(1000)}
FAMILIES = ('T', 'L', 'Q')
NS = range(1, 7)

def solve(X, aY, a2):
    """Exact 2x2 solve of section 4.4 for (x_G, x_X)."""
    gY, g2 = B['G'][0], B['G'][1]
    xY, x2 = B[X][0], B[X][1]
    det = gY*x2 - xY*g2
    return (aY*x2 - xY*a2)/det, (gY*a2 - aY*g2)/det

mass = lambda x, N: MP*exp(-TWO_PI*x/N)

def run_profile(X, NG, NX, MG, MX):
    """Values of 1/alpha_Y and 1/alpha_2 at every node MZ, thresholds, MP (piecewise linear in ln mu)."""
    th = sorted([(MG, NG*B['G'][0], NG*B['G'][1]), (MX, NX*B[X][0], NX*B[X][1])])
    nodes = [MZ] + [t[0] for t in th] + [MP]
    y, w = INVY_MZ, INV2_MZ
    bY, b2 = BY_SM, B2_SM
    out = [(MZ, y, w)]
    for i in range(1, len(nodes)):
        seg = log(nodes[i]/nodes[i-1])
        y -= bY*seg/TWO_PI; w -= b2*seg/TWO_PI
        out.append((nodes[i], y, w))
        if i-1 < len(th):
            bY += th[i-1][1]; b2 += th[i-1][2]
    return out, (bY, b2)     # final-segment coefficients returned for the approach-to-zero sign

print("\n== T0 ==")
print("ln(M_P/M_Z) =", R(LZ))
print("A_Y =", R(A_Y)); print("A_2 =", R(A_2)); print("A_3 =", R(A_3))

# ---- T5 baseline (Gate LOG V1) ----------------------------------------------
F = lambda Qc, Nc: mpf(4)/3*Nc*Qc**2
q23, q13 = mpf(2)/3, mpf(1)/3
LOGBASE = {'e': (F(mpf(1),1), mpf('0.00051099895')), 'mu': (F(mpf(1),1), mpf('0.1056583755')),
 'tau': (F(mpf(1),1), mpf('1.77686')), 'u': (F(q23,3), mpf('0.00216')), 'd': (F(q13,3), mpf('0.00470')),
 's': (F(q13,3), mpf('0.0935')), 'c': (F(q23,3), mpf('1.273')), 'b': (F(q13,3), mpf('4.183')),
 't': (F(q23,3), mpf('172.57')), 'W': (mpf(-7), mpf('80.3692'))}
MEAS = mpf('137.035999')
B_V1 = sum(b*log(MP/m) for b, m in LOGBASE.values())/TWO_PI

results = {}
fam_summary = {}
for X in FAMILIES:
    fam = 'G+' + X
    xG, xX = solve(X, A_Y, A_2)
    # residual check of the solve
    assert abs(B['G'][0]*xG + B[X][0]*xX - A_Y) < mpf(10)**-50
    assert abs(B['G'][1]*xG + B[X][1]*xX - A_2) < mpf(10)**-50
    c0 = 'PASS' if (xG >= 0 and xX >= 0) else 'FAIL'
    inv3 = A_3 - B['G'][2]*xG - B[X][2]*xX
    c2 = 'FAIL' if inv3 < -3 else ('INCONCLUSIVE' if inv3 <= 3 else 'PASS')
    print(f"\n==================== family {fam} ====================")
    print("T1 x_G =", R(xG)); print("T1 x_X =", R(xX)); print("T1 C0  =", c0)
    print("T1 1/alpha_s(M_P) =", R(inv3), "| C2 =", c2)
    t5 = B_V1 + B['G'][3]*xG + B[X][3]*xX
    print("T5 1/alpha(0), Gate LOG V1 + solved content =", R(t5))
    print("T5 difference from 137.035999               =", R(t5 - MEAS),
          "| NOTICE" if abs(t5 - MEAS) > 3 else "| within 3")
    corners = [solve(X, A_Y + dY, A_2 + d2) for dY, d2 in product((3, -3), repeat=2)]
    print("corner x (dY,d2 = ++,+-,-+,--):", [(S(a, 8), S(b, 8)) for a, b in corners])
    fam_summary[fam] = dict(xG=xG, xX=xX, c0=c0, inv3=inv3, c2=c2, t5=t5)

    print("\nT2 rows: N_G N_X | M_G (GeV) | M_X (GeV) | C1 | band M_G | band M_X | flags")
    for NG in NS:
        for NX in NS:
            MG, MX = mass(xG, NG), mass(xX, NX)
            excl = MG < THRESH['G'] or MX < THRESH[X]
            near = MG < 3*THRESH['G'] or MX < 3*THRESH[X]
            centre = 'EXCLUDED' if excl else ('MARGINAL' if near else 'PASS')
            cm, cst = [], []
            for (cg, cx) in corners:
                if cg < 0 or cx < 0:
                    cst.append('NOSOL')
                else:
                    cst.append('EXCLUDED' if (mass(cg, NG) < THRESH['G'] or mass(cx, NX) < THRESH[X]) else 'OK')
                cm.append((mass(cg, NG), mass(cx, NX)))
            status = centre
            if centre == 'PASS' and any(s != 'OK' for s in cst): status = 'MARGINAL'
            if centre == 'EXCLUDED' and any(s != 'EXCLUDED' for s in cst): status = 'MARGINAL'
            flags = []
            if MG < MZ or MX < MZ: flags.append('SUB-MZ: figures not meaningful')
            if 'NOSOL' in cst: flags.append('corner without solution')
            if status != centre: flags.append(f'centre {centre}, corners {cst}')
            bandG = (min(c[0] for c in cm), max(c[0] for c in cm))
            bandX = (min(c[1] for c in cm), max(c[1] for c in cm))
            prof, last = run_profile(X, NG, NX, MG, MX)
            interior = prof[:-1]
            minY, min2 = min(p[1] for p in interior), min(p[2] for p in interior)
            endY, end2 = prof[-1][1], prof[-1][2]
            c3 = 'FAIL' if (minY < -3 or min2 < -3) else 'PASS'
            results[(fam, NG, NX)] = dict(MG=MG, MX=MX, centre=centre, status=status, flags=flags,
                bandG=bandG, bandX=bandX, minY=minY, min2=min2, endY=endY, end2=end2, c3=c3, last=last)
            print(f"{NG} {NX} | {R(MG)} | {R(MX)} | {status} | "
                  f"[{S(bandG[0])}, {S(bandG[1])}] | [{S(bandX[0])}, {S(bandX[1])}] | {'; '.join(flags)}")

    passing = [(NG, NX) for NG in NS for NX in NS if results[(fam, NG, NX)]['status'] == 'PASS']
    nonexcl = [(NG, NX) for NG in NS for NX in NS if results[(fam, NG, NX)]['status'] != 'EXCLUDED']
    fam_summary[fam].update(passing=passing, nonexcl=nonexcl)
    print("\nT3 clean-PASS rows:", passing)
    print("T3 MARGINAL rows  :", [r for r in nonexcl if r not in passing])
    if passing:
        mg, mx = min(r[0] for r in passing), min(r[1] for r in passing)
        print("T3 smallest N_G passing =", mg, "| smallest N_X passing =", mx,
              "| both together pass:", (mg, mx) in passing)
        for row in sorted({(mg, min(r[1] for r in passing if r[0] == mg)),
                           (min(r[0] for r in passing if r[1] == mx), mx)}):
            r = results[(fam,) + row]
            print(f"   row {row}: M_G = {R(r['MG'])}")
            print(f"            M_X = {R(r['MX'])}")
            print(f"            band M_G = [{R(r['bandG'][0])}, {R(r['bandG'][1])}]")
            print(f"            band M_X = [{R(r['bandX'][0])}, {R(r['bandX'][1])}]")
    print("\nT4 C3 for rows passing C1 (min over nodes below M_P; value at M_P; final-segment b_Y, b_2):")
    for row in passing:
        r = results[(fam,) + row]
        print(f"   {row}: min 1/aY = {R(r['minY'])}")
        print(f"          min 1/a2 = {R(r['min2'])}")
        print(f"          at M_P: 1/aY = {S(r['endY'], 5)}, 1/a2 = {S(r['end2'], 5)}; "
              f"final b_Y = {S(r['last'][0], 8)}, b_2 = {S(r['last'][1], 8)}; C3 = {r['c3']}")
    c3_all = sorted({results[(fam, a, b)]['c3'] for a in NS for b in NS
                     if results[(fam, a, b)]['MG'] >= MZ and results[(fam, a, b)]['MX'] >= MZ})
    print("C3 over all rows with both masses above M_Z (diagnostic):", c3_all)

# ---- verdict ------------------------------------------------------------------
print("\n==================== verdict ====================")
c0_fams = [f for f, s in fam_summary.items() if s['c0'] == 'PASS']
survivors = {f: [r for r in fam_summary[f]['passing']
                 if fam_summary[f]['c2'] == 'PASS' and results[(f,) + r]['c3'] == 'PASS'] for f in c0_fams}
any_marginal = any(len(fam_summary[f]['nonexcl']) > len(fam_summary[f]['passing']) for f in c0_fams)
any_pass_c1 = any(fam_summary[f]['passing'] for f in c0_fams)
if any(survivors.values()): code = 'SC-SPEC2-1'
elif not c0_fams: code = 'SC-SPEC2-3'
elif not any_pass_c1 and not any_marginal: code = 'SC-SPEC2-2'
elif not any_pass_c1 and any_marginal: code = 'UNDECIDED BY TOLERANCE (MARGINAL rows only)'
else:
    inconc = any(fam_summary[f]['c2'] == 'INCONCLUSIVE' and fam_summary[f]['passing'] for f in c0_fams)
    code = 'UNDECIDED (C2 INCONCLUSIVE)' if inconc else 'SC-SPEC2-3'
print("verdict:", code)
for f in fam_summary:
    s = fam_summary[f]
    print(f, "| C0", s['c0'], "| C2", s['c2'], "| clean-PASS rows:", len(s['passing']),
          "| MARGINAL rows:", len(s['nonexcl']) - len(s['passing']),
          "| surviving C0-C3:", len(survivors.get(f, [])))
