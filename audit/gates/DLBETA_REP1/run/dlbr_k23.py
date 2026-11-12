"""
Gate DL-BETA REP1 -- K2 (local correctness), K3 (limits), sampler unit test.
Usage: python -I dlbr_k23.py OUTDIR
"""
import sys, os, json
import numpy as np
from scipy import stats
from scipy.special import i0e, i1e

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dlbr_sim as S
import dlbr_stats as ST

OUT = []
NUM = {}
FAILS = []


def say(s=""):
    print(s, flush=True)
    OUT.append(s)


def check(cond, msg):
    say(("  ok    " if cond else "  FAIL  ") + msg)
    if not cond:
        FAILS.append(msg)


def endpoints(kind, L):
    """origin/target node of every stored link."""
    if kind == "void":
        Lt = 3 * L
        loops, signs, ltype, Nl, meta, sp = S.build_void_spacetime(L, Lt)
        V, E, B = sp["V"], sp["E"], meta["B"]
        org = np.zeros(Nl, dtype=np.int64); tgt = np.zeros(Nl, dtype=np.int64)
        for t in range(Lt):
            t1 = (t + 1) % Lt
            org[t * B:t * B + E] = t * V + sp["link_ends"][:, 0]
            tgt[t * B:t * B + E] = t * V + sp["link_ends"][:, 1]
            org[t * B + E:(t + 1) * B] = t * V + np.arange(V)
            tgt[t * B + E:(t + 1) * B] = t1 * V + np.arange(V)
        return org, tgt, V * Lt
    else:
        loops, signs, ltype, Nl, meta, x = S.build_z4(L)
        Ns = L ** 4
        org = np.repeat(np.arange(Ns), 4)
        mu = np.tile(np.arange(4), Ns)
        xx = x[org].copy()
        xx[np.arange(Nl), mu] += 1
        xx %= L
        tgt = ((xx[:, 0] * L + xx[:, 1]) * L + xx[:, 2]) * L + xx[:, 3]
        return org, tgt, Ns


def k2(kind, L, seed):
    lat = S.get_lattice(kind, L)
    rng = np.random.default_rng(seed)
    th = rng.uniform(0, 2 * np.pi, lat["Nl"])
    org, tgt, Nv = endpoints(kind, L)
    # consistency: every loop is a closed path of its links (sum of signed boundaries = 0)
    chain = np.zeros((lat["loops"].shape[0], Nv), dtype=np.int64)
    P = lat["loops"].astype(np.int64); Sg = lat["signs"].astype(np.int64)
    for k in range(4):
        np.add.at(chain, (np.arange(P.shape[0]), org[P[:, k]]), -Sg[:, k])
        np.add.at(chain, (np.arange(P.shape[0]), tgt[P[:, k]]), Sg[:, k])
    check(not np.any(chain), f"K2 {kind} L={L}: every loop is a closed oriented path (boundary of boundary = 0)")
    lam = rng.uniform(0, 2 * np.pi, Nv)
    th2 = th + lam[org] - lam[tgt]
    c1 = S.loop_cos(th, lat["loops"], lat["signs"])
    c2 = S.loop_cos(th2, lat["loops"], lat["signs"])
    d = np.max(np.abs(c1 - c2))
    check(d < 1e-12, f"K2 {kind} L={L}: gauge invariance, max |change in cos theta_loop| = {d:.1e}")
    beta = 1.0
    maxdiff = 0.0
    for trial in range(200):
        l = int(rng.integers(lat["Nl"]))
        new = rng.uniform(0, 2 * np.pi)
        re, im = S.staple(th, lat["ptr"], lat["oth"], lat["osg"], l)
        R = np.hypot(re, im); phi = np.arctan2(im, re)
        dS_loc = -beta * (R * np.cos(new + phi) - R * np.cos(th[l] + phi))
        S0 = beta * np.sum(1 - S.loop_cos(th, lat["loops"], lat["signs"]))
        th3 = th.copy(); th3[l] = new
        S1 = beta * np.sum(1 - S.loop_cos(th3, lat["loops"], lat["signs"]))
        maxdiff = max(maxdiff, abs((S1 - S0) - dS_loc))
    check(maxdiff < 1e-9, f"K2 {kind} L={L}: local staple dS equals global recompute (200 links, max diff {maxdiff:.1e})")
    NUM[f"K2_{kind}"] = dict(gauge=float(d), dS=float(maxdiff), links_per_loop_in=int(lat["counts"].max()))


def k3(kind, L, rank_target):
    lat = S.get_lattice(kind, L)
    Np = lat["meta"]["Np"]
    res = {}
    rec, ser = S.do_run(kind, L, 0.1, "hot", 11000)
    m = ser[1001:, 0]
    cos_mean = 1 - m.mean()
    cos_err = ST.block_err(1 - m)
    u = i1e(0.1) / i0e(0.1)
    dev = cos_mean / u - 1
    check(abs(dev) < 0.02, f"K3 {kind} L={L}: beta=0.1 hot (seed {rec['seed']}), <cos> = {cos_mean:.6f} +- {cos_err:.6f} vs I1/I0 = {u:.6f} ({100*dev:+.2f}%, {(cos_mean-u)/cos_err:+.1f} sigma)")
    res["b01"] = dict(seed=rec["seed"], cos=cos_mean, err=cos_err, target=u, dev=dev, ms=rec["ms_per_sweep"])
    np.savez(os.path.join(sys.argv[1], "series", f"k3_{kind}_L{L}_b0.1_hot.npz"), series=ser, seed=rec["seed"])
    rec, ser = S.do_run(kind, L, 20.0, "cold", 11000)
    m = ser[1001:]
    E = m[:, 0].mean(); Ee = ST.block_err(m[:, 0])
    tgt = rank_target / (2 * 20.0 * Np)
    dev = E / tgt - 1
    check(abs(dev) < 0.02, f"K3 {kind} L={L}: beta=20 cold (seed {rec['seed']}), E = {E:.6f} +- {Ee:.6f} vs rank/(2 beta N_loops) = {tgt:.6f} ({100*dev:+.2f}%)")
    res["b20"] = dict(seed=rec["seed"], E=E, err=Ee, target=tgt, dev=dev, ms=rec["ms_per_sweep"])
    if kind == "void":
        Es = m[:, 1].mean(); Et = m[:, 2].mean()
        say(f"        beta = 20: rhombi E_s = {Es:.6f} +- {ST.block_err(m[:,1]):.6f}; temporal squares E_t = {Et:.6f} +- {ST.block_err(m[:,2]):.6f}; E_t/E_s = {Et/Es:.4f}")
        res["b20"].update(Es=Es, Et=Et, Es_err=ST.block_err(m[:, 1]), Et_err=ST.block_err(m[:, 2]), ratio=Et / Es)
    np.savez(os.path.join(sys.argv[1], "series", f"k3_{kind}_L{L}_b20_cold.npz"), series=ser, seed=rec["seed"])
    NUM[f"K3_{kind}"] = res


def sampler_test():
    say("Sampler unit test: von Mises(0, kappa), Best-Fisher, 1,000,000 draws per (kappa, seed)")
    rows = []
    for kappa in (0.05, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0, 40.0):
        for seed in (11, 12):
            x = S.vm_draws(seed, kappa, 1000000)
            ks = stats.kstest(x, stats.vonmises(kappa).cdf)
            u = i1e(kappa) / i0e(kappa)
            c = np.cos(x)
            z = (c.mean() - u) / (c.std() / np.sqrt(len(c)))
            rows.append((kappa, seed, ks.pvalue, z))
            say(f"    kappa = {kappa:6.2f} seed {seed}: KS p = {ks.pvalue:.3f}; <cos> - I1/I0 = {z:+.2f} sigma")
    ps = [r[2] for r in rows]; zs = [abs(r[3]) for r in rows]
    # 16 tests: expect min p ~ 1/16; fail only on gross error
    check(min(ps) > 1e-4 and max(zs) < 4.5, f"sampler: 16 KS p-values {min(ps):.3f}..{max(ps):.3f}; max |z(<cos>)| = {max(zs):.2f}")
    NUM["sampler"] = [dict(kappa=r[0], seed=r[1], ks_p=r[2], z_cos=r[3]) for r in rows]


def main(outdir):
    os.makedirs(os.path.join(outdir, "series"), exist_ok=True)
    say("=" * 96)
    say("Gate DL-BETA REP1 -- K2, K3, sampler")
    say("=" * 96)
    sampler_test()
    say()
    # K2: void L=2 (L_t=6), Z4 L=4; seeds for the random configurations/gauge transformations
    k2("void", 2, 7919 * 2 + 700000)
    k2("z4", 4, 7919 * 4 + 300000)
    say()
    # K3: 1000 + 10,000 sweeps; seeds by the card rule (s = 0 hot, 1 cold)
    k3("void", 2, 1533)
    k3("z4", 4, 765)
    say()
    say(f"K2/K3/sampler FAILS: {len(FAILS)}" + ("" if not FAILS else " -> " + "; ".join(FAILS)))
    NUM["fails"] = FAILS
    with open(os.path.join(outdir, "k23.txt"), "w") as f:
        f.write("\n".join(OUT) + "\n")
    with open(os.path.join(outdir, "k23.json"), "w") as f:
        json.dump(NUM, f, indent=1, default=float)


if __name__ == "__main__":
    main(sys.argv[1])
