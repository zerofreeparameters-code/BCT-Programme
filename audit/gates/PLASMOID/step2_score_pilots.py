#!/usr/bin/env python3
"""Gate PLASMOID — score the obtainable datasets (all eyewitness => pilot only).

Coding rules (fixed before any R was computed; see data/*.csv for provenance):

Dataset A — Keul 2021, Hist. Geo Space Sci. 12, 43-56 (CC BY 4.0).
  Table 1 of the paper is a binned contingency table, so per-case sizes were taken
  from the case abstracts.  Primary set = the 41 core cases (Sections 3-4) that state
  an explicit number with a length unit for the luminous object.  Ranges -> geometric
  mean of the endpoints.  Imperial values converted exactly (2.54 cm/in) from the
  printed inches.  Where an object has a core and an outer envelope, the OUTER size
  is primary.  Lower bounds ("more than a meter"), burn marks, fragments, angular
  sizes and comparison objects are not used.
  Sensitivities (exploratory): core instead of outer; drop the two sizes derived from
  angular size; add the two Section-6 notable cases; KDE density instead of log-normal.

Dataset A2 — Beatty collection, NMT ball-lightning report site (eyewitness).
  Size field used; narrative used only if the size field is empty or a bare shape
  word.  Explicit numbers with units are scored as for A.  Comparison objects are
  scored only for regulation sports balls, at their regulation diameters (below);
  non-standard objects (fruit, fist, balloon, "football" — ambiguous between codes)
  are excluded.  "A little bigger than ..." and angular statements are excluded.
  Sensitivities (exploratory): numeric-only subset; KDE density.

One primary test per dataset: Rayleigh R at P0 against the heaping-aware null
(log-normal density + the dataset's own rounding scheme), 10 000 draws, alpha 0.01.
"""
import csv
import hashlib
import json
import math
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import plasmoid_stats as ps  # noqa: E402

# Regulation diameters (cm).  Circumference rules converted with d = C/pi.
OBJECT_CM = {
    "ping-pong ball": 4.0,              # ITTF: 40 mm
    "golf ball": 4.267,                 # R&A/USGA: >= 1.680 in
    "cue ball": 2.25 * 2.54,            # pool: 2.25 in
    "tennis ball": 6.70,                # ITF: 6.54-6.86 cm
    "softball": 12 * 2.54 / math.pi,    # 12 in circumference
    "volleyball": 66.0 / math.pi,       # FIVB: 65-67 cm circumference
    "soccer ball": 69.0 / math.pi,      # FIFA size 5: 68-70 cm circumference
    "basketball": 29.5 * 2.54 / math.pi,  # size 7: 29.5 in circumference
}

SEED = 20261024
lines = []


def say(s=""):
    print(s)
    lines.append(s)


def parse_vals(s):
    return tuple(float(v) for v in s.split(";")) if s else ()


def keul_reports(variant="primary"):
    reps, labels = [], []
    with open(HERE / "data" / "keul2021_cases.csv") as f:
        for row in csv.DictReader(f):
            if row["section"] == "notable" and variant != "plus_notable":
                continue
            if variant == "no_angular" and row["angular_derived"] == "1":
                continue
            vals = parse_vals(row["values_native"])
            if variant == "core" and row["core_values_native"]:
                vals = parse_vals(row["core_values_native"])
            kind = "range" if len(vals) == 2 else "single"
            reps.append(ps.Report(kind, vals, row["unit"]))
            labels.append(row["id"])
    return reps, labels


def beatty_reports(variant="primary"):
    reps, labels = [], []
    with open(HERE / "data" / "beatty_nmt_reports.csv") as f:
        for row in csv.DictReader(f):
            if row["kind"] == "object":
                if variant == "numeric_only":
                    continue
                reps.append(ps.Report("object", object_cm=OBJECT_CM[row["object"]]))
            else:
                vals = parse_vals(row["values_native"])
                reps.append(ps.Report(row["kind"], vals, row["unit"]))
            labels.append(row["report"])
    return reps, labels


def score(name, reps, rng, density="lognormal", make_figs=False, tag=None):
    x = np.log(np.array([r.value_cm() for r in reps]))
    scheme = ps.RoundingScheme.from_reports(reps)
    res = ps.primary_test(x, scheme, rng, density=density)
    say(f"[{name}] " + res.summary())
    out = {"name": name, "n": res.n, "R_obs": res.R_obs, "p": res.p_heaping,
           "p_plus1": res.p_heaping_plus1, "null_median": float(np.median(res.null_R)),
           "null_p99": float(np.percentile(res.null_R, 99)), "span_periods": res.span_periods,
           "p_uniform": res.p_uniform_rayleigh}
    if make_figs:
        audit = scheme.terminal_digit_audit(reps)
        say(f"[{name}] rounding-scheme audit: " + json.dumps({k: (round(v, 3) if isinstance(v, float) else v) for k, v in audit.items()}))
        say(f"[{name}] sizes (cm, sorted): " + ", ".join(f"{v:.3g}" for v in sorted(np.exp(x))))
        ratios = ps.ratio_grid()
        pg = ps.periodogram(x, ratios)
        X0 = ps.heaping_null(x, scheme, np.random.default_rng(SEED + 1), ps.N_NULL, density)
        PG0 = ps.periodogram_batch(X0, ratios, chunk=200)
        env99 = np.percentile(PG0, 99, axis=0)
        gmax_null = PG0.max(axis=1)
        p_global = float((gmax_null >= pg.max()).mean())
        say(f"[{name}] periodogram (exploratory): peak at ratio {ratios[pg.argmax()]:.4f}, R = {pg.max():.4f}; "
            f"look-elsewhere p of that peak over 1.2-2.5 under the heaping-aware null = {p_global:.4f}")
        comp = {k: float(ps.periodogram(x, np.array([v]))[0]) for k, v in ps.COMPETITORS.items()}
        say(f"[{name}] R at competitor ratios: " + "; ".join(f"{k} {v:.4f}" for k, v in comp.items()))
        say(f"[{name}] resolution: span {res.span_periods:.2f} periods of P0 -> ~{100/res.span_periods:.0f} % in log-period; "
            f"phi is +3.3 %, R5 is -1.1 % from P0: neither can be excluded.")
        out.update({"pg_peak_ratio": float(ratios[pg.argmax()]), "pg_peak_R": float(pg.max()),
                    "p_global": p_global, "R_competitors": comp, "rounding_audit": audit})
        fig, axs = plt.subplots(1, 2, figsize=(11, 4))
        a = axs[0]
        a.plot(ratios, pg, lw=1.1, color="#1f4e79", label="observed R(P)")
        a.plot(ratios, env99, lw=0.9, color="#e67e22", ls="-", label="heaping-aware null, 99th pct (pointwise)")
        top = max(pg.max(), env99.max()) * 1.12
        for k, v in ps.COMPETITORS.items():
            a.axvline(v, ls="--", lw=0.8, color="#c0392b" if "162" in k else "#95a5a6")
            a.text(v, top * 0.99, k, rotation=90, fontsize=7, ha="right", va="top")
        a.set_ylim(0, top * 1.25)
        a.set_xlabel("size ratio r (period ln r)")
        a.set_ylabel("Rayleigh R")
        a.set_title(f"{tag}: periodogram (n = {res.n})")
        a.legend(fontsize=7, loc="lower right")
        b = axs[1]
        b.hist(res.null_R, bins=60, color="#bdc3c7", edgecolor="#7f8c8d")
        b.axvline(res.R_obs, color="#c0392b", lw=1.5, label=f"observed R = {res.R_obs:.3f}")
        b.axvline(np.percentile(res.null_R, 99), color="#e67e22", ls="--", lw=1, label="null 99th pct (alpha = 0.01)")
        b.set_xlabel("R at P0 under the heaping-aware null (10 000 draws)")
        b.set_ylabel("count")
        b.set_title(f"{tag}: primary test, p = {res.p_heaping:.3f}")
        b.legend(fontsize=7)
        fig.tight_layout()
        fig.savefig(HERE / f"fig_{tag}.png", dpi=150)
        plt.close(fig)
    return out


def main():
    freeze = json.loads((HERE / "FREEZE.json").read_text())
    for fn, h in freeze["sha256"].items():
        got = hashlib.sha256((HERE / fn).read_bytes()).hexdigest()
        assert got == h, f"frozen file changed: {fn}"
    say(f"Freeze check passed ({len(freeze['sha256'])} files, frozen {freeze['frozen_at']}).")
    say(f"P0 = {ps.P0:.10f}; alpha = {ps.ALPHA}; N_null = {ps.N_NULL}")
    say()
    results = {}
    rng = np.random.default_rng(SEED)

    say("=== Dataset A: Keul 2021 (eyewitness, professional observers) — PILOT ===")
    reps, _ = keul_reports("primary")
    results["A_primary"] = score("A primary", reps, rng, make_figs=True, tag="A_keul2021")
    say("--- A sensitivities (exploratory) ---")
    for v in ("core", "no_angular", "plus_notable"):
        r, _ = keul_reports(v)
        results[f"A_{v}"] = score(f"A {v}", r, rng)
    results["A_kde"] = score("A KDE density (bw >= P0)", reps, rng, density="kde")
    say()

    say("=== Dataset A2: Beatty collection, NMT site (eyewitness, public) — PILOT ===")
    reps, _ = beatty_reports("primary")
    results["A2_primary"] = score("A2 primary", reps, rng, make_figs=True, tag="A2_beatty")
    say("--- A2 sensitivities (exploratory) ---")
    r, _ = beatty_reports("numeric_only")
    results["A2_numeric_only"] = score("A2 numeric only", r, rng)
    results["A2_kde"] = score("A2 KDE density (bw >= P0)", reps, rng, density="kde")
    say()

    say("Regulation object diameters used (cm): " + ", ".join(f"{k} {v:.3f}" for k, v in OBJECT_CM.items()))
    (HERE / "step2_output.txt").write_text("\n".join(lines) + "\n")
    (HERE / "step2_results.json").write_text(json.dumps(results, indent=2, default=float))


if __name__ == "__main__":
    main()
