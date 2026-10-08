"""Gate CRIT2 section 4, checks 1 (gauge invariance) and 2 (limits), both lattices."""
import json, sys
import numpy as np
import u1sim as U

OUT = sys.argv[1] if len(sys.argv) > 1 else "/root/crit2/out"
res = {"check1": {}, "check2": {}}


def endpoint_site_index(lat):
    L = lat["L"]
    end = np.mod(lat["link_origin"] + lat["link_vec"], L)
    org = lat["link_origin"]
    fi_e = U._full_index(end, L)
    fi_o = U._full_index(org, L)
    if lat["name"] == "d4":
        coords = U._coords(L)
        even = (coords.sum(axis=1) % 2) == 0
        compact = -np.ones(L ** 4, dtype=np.int64)
        compact[U._full_index(coords[even], L)] = np.arange(even.sum())
        return compact[fi_o], compact[fi_e]
    return fi_o, fi_e


print("== Check 1: gauge invariance of E ==")
rng = np.random.default_rng(2026)
ok1 = True
for name in ("d4", "hc"):
    lat = U.build(name, 4)
    so, se = endpoint_site_index(lat)
    assert (so >= 0).all() and (se >= 0).all()
    worst_E, worst_p = 0.0, 0.0
    for trial in range(5):
        U.nb_seed(1000 + trial)
        th = U.init_hot(lat["nlinks"])
        if trial >= 2:   # also on equilibrated-looking configurations
            beta = 0.6 if name == "d4" else 1.0
            U.evolve(th, lat["stp_l"], lat["stp_s"], lat["plaq_links"], lat["PS_f"], beta, 20, False)
        alpha = rng.uniform(0, 2 * np.pi, lat["Ns"])
        th2 = th + alpha[so] - alpha[se]
        E1 = U.energy(th, lat["plaq_links"], lat["PS_f"])
        E2 = U.energy(th2, lat["plaq_links"], lat["PS_f"])
        c1 = U.plaq_cos(th, lat["plaq_links"], lat["PS_f"])
        c2 = U.plaq_cos(th2, lat["plaq_links"], lat["PS_f"])
        worst_E = max(worst_E, abs(E1 - E2))
        worst_p = max(worst_p, np.abs(c1 - c2).max())
    passed = worst_E < 1e-12 and worst_p < 1e-10
    ok1 &= passed
    res["check1"][name] = dict(max_dE=worst_E, max_dcos_plaq=worst_p, passed=bool(passed))
    print(f"{name}: max|dE|={worst_E:.2e}  max|d cos_p|={worst_p:.2e}  pass={passed}")

print("== Check 2: limits, L = 4 ==")
ok2 = True
for name in ("d4", "hc"):
    lat = U.get_lat(name, 4)
    lps, pps = lat["links_per_site"], lat["plaq_per_site"]
    # strong coupling
    r, E = U.run_scan(name, 4, 0.1, "hot", 1000, 10000)
    cos_mean = 1 - r["E"]
    target = 0.1 / 2
    dev = (cos_mean - target) / target
    p1 = abs(dev) < 0.02
    print(f"{name} beta=0.1 hot: <cos>={cos_mean:.6f} +- {r['E_err']:.6f}  target beta/2={target}  "
          f"rel.dev={dev*100:+.2f}%  pass={p1}  (seed {r['seed']})")
    # weak coupling
    r2, E2 = U.run_scan(name, 4, 20.0, "cold", 1000, 10000)
    beta = 20.0
    Ewc = (lps - 1) / (2 * beta * pps)
    closed = 1 / (4 * beta) if name == "hc" else 11 / (64 * beta)
    assert abs(Ewc - closed) < 1e-15
    dev2 = (r2["E"] - Ewc) / Ewc
    p2 = abs(dev2) < 0.02
    print(f"{name} beta=20 cold: E={r2['E']:.7f} +- {r2['E_err']:.7f}  target={Ewc:.7f} "
          f"(= {'1/(4b)' if name=='hc' else '11/(64b)'})  rel.dev={dev2*100:+.2f}%  pass={p2}  (seed {r2['seed']})")
    ok2 &= p1 and p2
    res["check2"][name] = dict(beta01=dict(cos=cos_mean, err=r["E_err"], target=target, rel_dev=dev,
                                           seed=r["seed"], passed=bool(p1)),
                               beta20=dict(E=r2["E"], err=r2["E_err"], target=Ewc, rel_dev=dev2,
                                           seed=r2["seed"], passed=bool(p2)))
res["check1_pass"] = bool(ok1)
res["check2_pass"] = bool(ok2)
print("CHECK 1:", "PASS" if ok1 else "FAIL", "  CHECK 2:", "PASS" if ok2 else "FAIL")
with open(f"{OUT}/checks12.json", "w") as f:
    json.dump(res, f, indent=1)
