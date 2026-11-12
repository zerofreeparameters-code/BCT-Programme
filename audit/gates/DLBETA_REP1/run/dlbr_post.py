"""
Gate DL-BETA REP1 -- after the section 4.7 hash: Q7 arithmetic, Q4/Q5 records, and post-unblinding
observations (not verdict inputs). Usage: python -I dlbr_post.py OUTDIR ORIGINAL_RESULT.md ORIGINAL_NUMBERS.txt
"""
import os, sys, json, re, math
import numpy as np

OUT, ORES, ONUM = sys.argv[1], sys.argv[2], sys.argv[3]
U = 1e7
st = json.load(open(os.path.join(OUT, "state.json")))
P = []
w = P.append


def rec(stage, L, bn, start):
    return json.load(open(os.path.join(OUT, "records", f"{stage}_void_L{L}_b{bn:09d}_{start}.json")))


def ser(stage, L, bn, start):
    return np.load(os.path.join(OUT, "series", f"{stage}_void_L{L}_b{bn:09d}_{start}.npz"))["series"]


# ---------------- Q7 ----------------
txt = open(ONUM).read()
m_b = re.search(r"^beta_inf = .*?\[([0-9.]+)\]", txt, re.M)
m_u = re.search(r"^uncertainty = .*= ([0-9.]+)\s*$", txt, re.M)
binf_O, u_O = float(m_b.group(1)), float(m_u.group(1))
IO = (binf_O - u_O, binf_O + u_O)
fi = st["final"]
betaR = fi["betaR"] / U
d = 0.0 if IO[0] - 1e-12 <= betaR <= IO[1] + 1e-12 else min(abs(betaR - IO[0]), abs(betaR - IO[1]))
resolved = fi["resolved"]
if not (st["K4"]["pass_"] and st["K5"]["pass_"]):
    code = "SC-DLBR-0"
elif not (st["S1"]["interior"] and st["S3"]["located"]):
    code = "SC-DLBR-5"
elif resolved and d <= 0.005 + 1e-12:
    code = "SC-DLBR-1"
elif d > 0.010:
    code = "SC-DLBR-2"
else:
    code = "SC-DLBR-3"
w("Q7")
w(f"  original beta_inf = {binf_O}, uncertainty = {u_O} -> I_O = [{IO[0]:.5f}, {IO[1]:.5f}]")
w(f"  beta^R = {betaR:.5f}; d = {d:.5f}; Resolved = {resolved}; sealed material seen early: no")
w(f"  verdict = {code}")
w(f"  beta_inf(REP1) - beta_inf(original) = {fi['beta_inf']/U - binf_O:+.5f}")
oj6 = re.search(r"jump interval L = 6 cold = \[([0-9.]+), ([0-9.]+)\]", txt)
w(f"  L = 6 cold jump: REP1 [{st['S3']['cold_jump'][0]/U:.4f}, {st['S3']['cold_jump'][1]/U:.4f}] vs original [{oj6.group(1)}, {oj6.group(2)}]")
w("")

# ---------------- sensitivity of the mixed-run classification ----------------
def line_err(line, stage_pts, start, bn):
    """1-sigma error of a 4-point LSQ line evaluated at bn, from the 20-block errors of its points."""
    xs = np.array([p[0] / U for p in line["points"]])
    sig = np.array([rec("S3", 6, p[0], start)["E_err"] for p in line["points"]])
    A = np.vstack([np.ones_like(xs), xs - xs.mean()]).T
    Ainv = np.linalg.pinv(A)                 # unweighted LSQ (as used), errors propagated
    cov = Ainv @ np.diag(sig ** 2) @ Ainv.T
    g = np.array([1.0, bn / U - xs.mean()])
    return float(np.sqrt(g @ cov @ g))


w("Sensitivity of the C1 outcomes (observation; not a verdict input)")
w("  sigma(E_end): sd of the 10 readings / sqrt(10); sigma(S), sigma(W): 20-block errors propagated through the lines")
w("  | L | beta | f | sigma_f (MC) | margin to nearest cut in units of sigma_f | P(other side) |")
rng = np.random.default_rng(20261113)
sens = {}
for stage, L in (("S4a", 6), ("S4b", 8)):
    for r in st[stage]["runs"]:
        s = ser(stage, L, r["bn"], "mixed")
        rd = s[1550:2001:50, 0]
        sE = rd.std(ddof=1) / np.sqrt(len(rd))
        sS = line_err(st["S3"]["S_line"], None, "hot", r["bn"])
        sW = line_err(st["S3"]["W_line"], None, "cold", r["bn"])
        n = 200000
        Ed = r["E_end"] + sE * rng.standard_normal(n)
        Sd = r["S"] + sS * rng.standard_normal(n)
        Wd = r["W"] + sW * rng.standard_normal(n)
        fd = (Sd - Ed) / (Sd - Wd)
        sf = float(np.std(fd))
        cut = 1 / 3 if abs(r["f"] - 1 / 3) < abs(r["f"] - 2 / 3) else 2 / 3
        lab = np.where(fd < 1 / 3, "strong", np.where(fd > 2 / 3, "weak", "unresolved"))
        p_other = float(np.mean(lab != r["primary"]))
        sens[(L, r["bn"])] = dict(sf=sf, p_other=p_other, sE=sE, sS=sS, sW=sW)
        w(f"  | {L} | {r['bn']/U:.5f} | {r['f']:.6f} | {sf:.4f} (sE {sE:.5f}, sS {sS:.5f}, sW {sW:.5f}) | {abs(r['f']-cut)/sf:.3f} | {p_other:.3f} |")
w("")
# what-if: the 1.26125 weak win (f just above 2/3) read as unresolved
runs8 = st["S4b"]["runs"]
alt = [("unresolved" if (abs(r["f"] - 2 / 3) < 1e-3) else r["primary"]) for r in runs8]
grid8 = [r["bn"] for r in runs8]
st_ = [b for b, o in zip(grid8, alt) if o == "strong"]
wk = [b for b, o in zip(grid8, alt) if o == "weak"]
S8, W8 = max(st_), min(wk)
mid = (S8 + W8) / 2 / U
u_alt = max((W8 - S8) / 2 / U, abs(mid - st["S4a"]["flip"]["mid"] / U))
n_un = sum(1 for o in alt if o == "unresolved")
res_alt = n_un <= 1 and u_alt <= 0.010
d_alt = 0.0 if IO[0] <= mid <= IO[1] else min(abs(mid - IO[0]), abs(mid - IO[1]))
w(f"  What-if (observation): with 1.26125 unresolved instead of weak -> L = 8 flip [{S8/U:.5f}, {W8/U:.5f}], beta_mix(8) = {mid:.5f}, "
  f"u = {u_alt:.5f}, unresolved = {n_un}, Resolved = {res_alt}, d = {d_alt:.5f} -> {'SC-DLBR-1' if (res_alt and d_alt <= 0.005) else ('SC-DLBR-2' if d_alt > 0.010 else 'SC-DLBR-3')}")
w("")

# ---------------- cross-code comparison of E at shared grid points ----------------
ores = open(ORES).read()


def parse_table(start_marker, ncols_pm):
    sec = ores.split(start_marker, 1)[1]
    rows = {}
    for line in sec.splitlines()[1:]:
        if line.startswith("|") and re.match(r"\|\s*\**[0-9]", line):
            cells = [c.strip().strip("*") for c in line.strip("|").split("|")]
            rows[float(cells[0])] = cells[1:]
        elif rows and not line.startswith("|"):
            break
    return rows


w("Cross-code comparison (after unblinding; observation): z = (E_REP1 - E_orig)/sqrt(s_REP1^2 + s_orig^2)")
t4 = parse_table("### 4.2 Fine scan", 2)
zs = []
lines = []
for b, cells in sorted(t4.items()):
    bn = int(round(b * U))
    for k, s in ((0, "hot"), (1, "cold")):
        Eo, so = [float(x) for x in cells[k].split("±")]
        r = rec("S2", 4, bn, s)
        z = (r["E"] - Eo) / math.hypot(r["E_err"], so)
        zs.append((b, s, z))
        lines.append(f"    L=4 {s:4s} {b:.4f}: REP1 {r['E']:.5f} +- {r['E_err']:.5f}  orig {Eo:.5f} +- {so:.5f}  z = {z:+.2f}")
away = [z for (b, s, z) in zs if not (1.2449 < b < 1.2601)]
w(f"  L = 4, both starts, {len(away)} comparisons away from 1.245-1.260: rms z = {np.sqrt(np.mean(np.square(away))):.2f}, max |z| = {np.max(np.abs(away)):.2f}")
near = [(b, s, z) for (b, s, z) in zs if 1.2449 < b < 1.2601]
w("  L = 4 at 1.245-1.260 (part-mixed runs): " + "; ".join(f"{b:.3f} {s} {z:+.1f}" for b, s, z in near))
t6 = parse_table("### 4.3 Cold scan", 1)
z6 = []
for b, cells in sorted(t6.items()):
    bn = int(round(b * U))
    Eo, so = [float(x) for x in cells[0].split("±")]
    r = rec("S3", 6, bn, "cold")
    z = (r["E"] - Eo) / math.hypot(r["E_err"], so)
    z6.append((b, z))
away6 = [z for b, z in z6 if not (1.2499 < b < 1.2551)]
w(f"  L = 6 cold, {len(away6)} comparisons away from 1.250-1.255: rms z = {np.sqrt(np.mean(np.square(away6))):.2f}, max |z| = {np.max(np.abs(away6)):.2f}; "
  + "at 1.250/1.255: " + ", ".join(f"{z:+.1f}" for b, z in z6 if 1.2499 < b < 1.2551))
w("")
for l in lines:
    w(l)
w("")


def parse_mixed(marker):
    sec = ores.split(marker, 1)[1]
    rows = {}
    for line in sec.splitlines()[1:]:
        if re.match(r"\|\s*1\.2[0-9]{4}\s*\|", line):
            c = [x.strip() for x in line.strip("|").split("|")]
            if len(c) >= 6:
                rows[float(c[0])] = float(c[2])
        if line.startswith("**beta") or line.startswith("**β_mix"):
            break
    return rows


w("Mixed-phase E_end at the same beta, both codes (observation)")
om6 = parse_mixed("### 4.4 Mixed-phase starts")
om8 = parse_mixed("### 4.5 Mixed-phase starts")
for stage, L, om in (("S4a", 6, om6), ("S4b", 8, om8)):
    mine = {r["bn"] / U: r for r in st[stage]["runs"]}
    for b in sorted(set(round(x, 5) for x in list(om.keys()) + list(mine.keys()))):
        a = mine.get(b); o = om.get(b)
        Sb = st["S3"]["S_line"]["a"] + st["S3"]["S_line"]["slope"] * (b - st["S3"]["S_line"]["xc"])
        Wb = st["S3"]["W_line"]["a"] + st["S3"]["W_line"]["slope"] * (b - st["S3"]["W_line"]["xc"])
        fo = (Sb - o) / (Sb - Wb) if o is not None else None
        oc = None if fo is None else ("strong" if fo < 1 / 3 else ("weak" if fo > 2 / 3 else "unresolved"))
        w(f"  L={L} {b:.5f}: REP1 E_end {a['E_end']:.5f} f {a['f']:.3f} {a['primary']:10s} | " if a else f"  L={L} {b:.5f}: REP1 —                                 | ",)
        P[-1] += (f"original E_end {o:.5f}; REP1's C1 lines applied: f {fo:.3f} -> {oc}" if o is not None else "original —")
w("")

# ---------------- Q5 ----------------
w("Q5 anisotropy record (recorded, not interpreted)")
binf = fi["beta_inf"]
g6 = st["S3"]["grid"]
below = max(b for b in g6 if b < binf); above = min(b for b in g6 if b > binf)
for b in (below, above):
    for s in ("hot", "cold"):
        r = rec("S3", 6, b, s)
        w(f"  L = 6 {s:4s} scan, beta = {b/U:.3f} ({'below' if b < binf else 'above'} beta_inf): E_s = {r['Es']:.5f} +- {r['Es_err']:.5f}, "
          f"E_t = {r['Et']:.5f} +- {r['Et_err']:.5f}, E_t/E_s = {r['Et']/r['Es']:.4f}")
for bn in (fi["dE8_below"], fi["dE8_above"]):
    r = [x for x in st["S4b"]["runs"] if x["bn"] == bn][0]
    w(f"  L = 8 mixed, beta = {bn/U:.5f} ({r['primary']} win, {'below' if bn < binf else 'above'} beta_inf): E_s = {r['Es_end']:.5f}, E_t = {r['Et_end']:.5f}, E_t/E_s = {r['Et_end']/r['Es_end']:.4f}")
k23 = json.load(open(os.path.join(OUT, "k23.json")))["K3_void"]["b20"]
w(f"  beta = 20 (K3, void L = 2, L_t = 6, cold): E_s = {k23['Es']:.6f} +- {k23['Es_err']:.6f}, E_t = {k23['Et']:.6f} +- {k23['Et_err']:.6f}, E_t/E_s = {k23['ratio']:.4f}")
ratios = []
for b in g6:
    for s in ("hot", "cold"):
        r = rec("S3", 6, b, s); ratios.append((b, s, r["Et"] / r["Es"]))
w("  L = 6 scan E_t/E_s, every point: " + "; ".join(f"{b/U:.3f}{s[0]} {x:.4f}" for b, s, x in ratios))
w("")
json.dump(dict(code=code, d=d, IO=IO, betaR=betaR, binf_O=binf_O, u_O=u_O,
               sens={f"{k[0]}_{k[1]}": v for k, v in sens.items()}), open(os.path.join(OUT, "post.json"), "w"), indent=1)
open(os.path.join(OUT, "post_obs.txt"), "w").write("\n".join(P) + "\n")
print("\n".join(P))
