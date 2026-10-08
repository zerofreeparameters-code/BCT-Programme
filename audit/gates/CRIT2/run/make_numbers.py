"""Assemble crit2_numbers.txt (all D4 numbers of card section 5) from out/state.json and
the raw .jsonl run records, then print its SHA-256. Run once, before unblinding."""
import json, hashlib, os, sys

OUT = sys.argv[1] if len(sys.argv) > 1 else "/root/crit2/out"
st = json.load(open(f"{OUT}/state.json"))


def rows(tag):
    return [json.loads(l) for l in open(f"{OUT}/{tag}.jsonl")]


L = []
w = L.append
w("Gate CRIT2 -- D4 numbers (card SHA-256 b30436875a2b12ea9b38a4d5d366c1ab9fcad83bcfe0405b3af5974876df4c79)")
w("Lattice D4 (even-sum Z^4), compact U(1), Wilson action on triangles, heat bath. beta = card convention;")
w("beta_KN = 2*beta (Katz-Nogradi convention).")
w("")
w("5.1 Locate, L=4, hot+cold, 500+2000 sweeps")
w("beta    start  E          C        seed")
for r in sorted(rows("s51"), key=lambda r: (r["beta"], r["start"])):
    w(f"{r['beta']:.4f}  {r['start']:5s}  {r['E']:.6f}  {r['C']:8.4f}  {r['seed']}")
w(f"beta0 = {st['s51']['beta0']:.4f}  (C = {st['s51']['Cmax']:.4f}, {st['s51']['start']} start)")
w("")
w("5.2 Fine scan, L=8, hot+cold, 2000+4000 sweeps")
w("beta    start  E          E_err      C         C_err     seed")
for r in sorted(rows("s52"), key=lambda r: (r["beta"], r["start"])):
    w(f"{r['beta']:.4f}  {r['start']:5s}  {r['E']:.6f}  {r['E_err']:.6f}  {r['C']:8.4f}  {r['C_err']:8.4f}  {r['seed']}")
s = st["s52"]
w(f"beta8 = {s['beta8']:.4f}  (C = {s['Cmax']:.4f}, {s['start']} start; grid extensions = {s['n_ext']})")
for k in ("hot", "cold"):
    j = s[f"jump_{k}"]
    w(f"jump interval L=8 {k:4s}: [{j['lo']:.4f}, {j['hi']:.4f}]  E = {j['E_lo']:.6f} -> {j['E_hi']:.6f}  fall = {j['fall']:.6f}")
w("")
w("5.3 Cold scan, L=12, cold, 500+1500 sweeps")
w("beta    start  E          E_err      C         C_err     seed")
for r in sorted(rows("s53"), key=lambda r: r["beta"]):
    w(f"{r['beta']:.4f}  {r['start']:5s}  {r['E']:.6f}  {r['E_err']:.6f}  {r['C']:8.4f}  {r['C_err']:8.4f}  {r['seed']}")
j = st["s53"]["jump"]
w(f"jump interval L=12 cold: [{j['lo']:.4f}, {j['hi']:.4f}]  E = {j['E_lo']:.6f} -> {j['E_hi']:.6f}  fall = {j['fall']:.6f}")
w(f"E* = {st['s53']['Estar']:.6f}")
w("")
for tag, Lx in (("s54a", 12), ("s54b", 16)):
    s = st[tag]
    w(f"5.4 Mixed-phase starts, L={Lx}, 2000 sweeps, centre {s['center']:.6f}")
    w("beta       E_last500  E_final    outcome     seed")
    for r in sorted(rows(tag), key=lambda r: r["beta"]):
        w(f"{r['beta']:.6f}  {r['E_last500']:.6f}  {r['E_final']:.6f}  {r['outcome']:10s}  {r['seed']}")
    f = s["flip"]
    w(f"beta_mix({Lx}) = {f['beta_mix']:.6f}; flip interval [{f['lo']:.6f}, {f['hi']:.6f}] "
      f"(highest strong {f['highest_strong']:.6f}, lowest weak {f['lowest_weak']:.6f}, monotonic={f['monotonic']}); "
      f"grid extensions = {s['n_ext']}")
    w("")
r = st["s55"]
w("5.5 Result")
w(f"beta_inf = beta_mix(16) = {r['beta_inf']:.6f} +- {r['unc']:.6f}")
w(f"  uncertainty = max(half L=16 flip interval = {r['half_width16']:.6f}, |beta_mix(16)-beta_mix(12)| = {abs(r['beta_mix16']-r['beta_mix12']):.6f})")
w(f"beta_inf (Katz-Nogradi, beta_KN = 2 beta) = {r['beta_inf_KN']:.6f} +- {r['unc_KN']:.6f}")
w(f"Delta E (L=16) = {r['dE16']:.6f}  (mean of last-500-sweep readings; strong run beta={r['dE_runs'][0]:.6f}, weak run beta={r['dE_runs'][1]:.6f}) {r['dE_flag']}")
w(f"Delta E (L=16, final-sweep E) = {r['dE16_final']:.6f}")
w(f"Section 6 kill check: beta_inf - unc = {r['beta_inf']-r['unc']:.6f}  -> below 0.5601? {r['kill_reopened']}")

txt = "\n".join(L) + "\n"
path = f"{OUT}/crit2_numbers.txt"
if os.path.exists(path):
    raise SystemExit("crit2_numbers.txt already exists; refusing to overwrite")
with open(path, "w") as fh:
    fh.write(txt)
print(txt)
print("SHA-256(crit2_numbers.txt) =", hashlib.sha256(txt.encode()).hexdigest())
