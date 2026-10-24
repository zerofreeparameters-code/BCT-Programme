#!/usr/bin/env python3
"""Gate PLASMOID — positive and negative controls for the test machinery.

Card section 4: "This gate must be able to find a ladder."  Before any real data
are scored, the pipeline is run on synthetic data where the answer is known.

PC1  real ladder, instrument-grade data (n = 150, intrinsic width 8 % < 10 %,
     3 % measurement noise, 1 mm resolution) -> must reject at alpha = 0.01.
PC1n power of PC1 versus n (200 replicates each).
PC2  no ladder, instrument-grade (smooth log-normal) -> false-positive rate
     must be ~1 % at alpha = 0.01 (calibration of the heaping-aware null).
PC3  the PC1 ladder seen through eyewitness eyes (35 % log-scatter + human
     rounding) -> shows what eyewitness data can and cannot see.
PC4  no ladder + human rounding -> the naive uniform-phase Rayleigh test
     false-alarms; the heaping-aware null does not.  This is why 2.3 exists.
PC5  power at Letter 114's own width bound (total log-scatter 0.10), n = 30/50/100
     (added after the independent check; runs last, so PC1-PC4 are unchanged).
"""
import math
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parent))
import plasmoid_stats as ps  # noqa: E402

OUT = Path(__file__).resolve().parent
rng = np.random.default_rng(20261024)

# A generic human-rounding scheme for the synthetic eyewitness cases (PC3, PC4).
HUMAN = ps.RoundingScheme(
    p_single=0.65, p_range=0.35, p_object=0.0,
    c_values=np.array([1.0] * 8 + [0.5] * 4 + [1 / 3] * 3 + [0.2] * 3 + [0.1] * 2),
    c_units=np.array(["cm"] * 20),
    range_logwidths=np.log(np.array([4 / 3, 1.5, 1.5, 2.0, 2.5])),
)
INSTR = ps.RoundingScheme.instrument(0.1)   # 1 mm resolution


def ladder(n, D0=12.0, w=(0.4, 0.3, 0.2, 0.1), s_int=0.08, s_meas=0.03, rng=rng):
    rung = rng.choice(len(w), size=n, p=w)
    x = math.log(D0) + rung * ps.P0 + rng.normal(0, s_int, n) + rng.normal(0, s_meas, n)
    return np.exp(x)


def smooth(n, rng=rng, median=20.0, s=0.6):
    return np.exp(rng.normal(math.log(median), s, n))


lines = []
def say(s=""):
    print(s); lines.append(s)

say("Gate PLASMOID — controls.  P0 = %.10f (ratio %.10f)" % (ps.P0, ps.RATIO0))
say("Expected R for a perfect ladder with Gaussian log-scatter sigma: R = exp(-2 pi^2 sigma^2 / P0^2)")
for s in (0.03, 0.05, 0.0854, 0.10, 0.15, 0.20, 0.30, 0.405, 0.693):
    say(f"  sigma = {s:<6} -> R = {ps.expected_R_gaussian(s):.4g}")
say("  (0.0854 = sqrt(0.08^2+0.03^2), the PC1 total; 0.405 = ln 1.5; 0.693 = ln 2, Rayle's 'factor of two')")
say()

# PC1 -------------------------------------------------------------------------
D = ladder(150)
Dm = ps.apply_rounding(D, INSTR, rng)
x = np.log(Dm)
res = ps.primary_test(x, INSTR, rng)
say("PC1 (real ladder, instrument grade, n=150): " + res.summary())
ratios = ps.ratio_grid()
pg = ps.periodogram(x, ratios)
r_peak = ratios[pg.argmax()]
say(f"PC1 periodogram peak at ratio {r_peak:.4f} (R = {pg.max():.4f}); "
    f"R at phi = {ps.periodogram(x, np.array([ps.COMPETITORS['phi']]))[0]:.4f}, "
    f"R at R5 = {ps.periodogram(x, np.array([10**0.2]))[0]:.4f}; span = {res.span_periods:.2f} periods "
    f"-> resolution ~ 1/k = {1/res.span_periods:.3f} in log-period")
PC1_x, PC1_pg = x, pg
say()

# PC1n — power vs n ------------------------------------------------------------
say("PC1n power at alpha = 0.01 (200 replicates each, 2000 null draws per replicate):")
for n in (20, 30, 50, 100, 150):
    hits = 0
    for _ in range(200):
        xx = np.log(ps.apply_rounding(ladder(n), INSTR, rng))
        r = ps.primary_test(xx, INSTR, rng, n_null=2000)
        hits += r.p_heaping < ps.ALPHA
    say(f"  n = {n:<4} power = {hits/200:.3f}")
say()

# PC2 — calibration ------------------------------------------------------------
fp = 0
M = 400
for _ in range(M):
    xx = np.log(ps.apply_rounding(smooth(100), INSTR, rng))
    r = ps.primary_test(xx, INSTR, rng, n_null=2000)
    fp += r.p_heaping < ps.ALPHA
say(f"PC2 (no ladder, instrument grade, n=100): false-positive rate at alpha=0.01 = {fp/M:.4f} "
    f"({fp}/{M}; binomial 95% band for a true 1 % rate ~ 0.0-2.25 %)")
say()

# PC3 — ladder through eyewitness eyes -------------------------------------------
fails = 0
Rs = []
for _ in range(200):
    D = ladder(150) * np.exp(rng.normal(0, 0.35, 150))
    xx = np.log(ps.apply_rounding(D, HUMAN, rng))
    r = ps.primary_test(xx, HUMAN, rng, n_null=2000)
    fails += r.p_heaping >= ps.ALPHA
    Rs.append(r.R_obs)
say(f"PC3 (same ladder, + 35 % eyewitness log-scatter + human rounding, n=150): "
    f"detected in {200-fails}/200 replicates; mean R_obs = {np.mean(Rs):.4f} "
    f"(expected from scatter alone: {ps.expected_R_gaussian(math.hypot(0.0854, 0.35)):.2e})")
say()

# PC4 — heaping alone: naive vs heaping-aware ------------------------------------
naive_fp = aware_fp = 0
for _ in range(M):
    xx = np.log(ps.apply_rounding(smooth(150), HUMAN, rng))
    r = ps.primary_test(xx, HUMAN, rng, n_null=2000)
    aware_fp += r.p_heaping < ps.ALPHA
    naive_fp += r.p_uniform_rayleigh < ps.ALPHA
say(f"PC4 (no ladder, human rounding, n=150): false-positive rate at alpha=0.01 — "
    f"naive uniform-phase Rayleigh {naive_fp/M:.3f}; heaping-aware null {aware_fp/M:.3f}")
say()

# PC5 — power at Letter 114's own width bound (total log-scatter 0.10) -----------
# Added after the independent check: section 6's power statement must rest on a
# simulation at sigma = 0.10, not on PC1's 8.5 % width.  Runs after PC1-PC4, so
# their random streams (and outputs) are unchanged.
say("PC5 power at alpha = 0.01 with total log-scatter 0.10 (intrinsic 0.0954 + 3 % measurement), "
    "instrument grade (200 replicates each, 2000 null draws per replicate):")
s_int10 = math.sqrt(0.10 ** 2 - 0.03 ** 2)
for n in (30, 50, 100):
    hits = 0
    for _ in range(200):
        xx = np.log(ps.apply_rounding(ladder(n, s_int=s_int10), INSTR, rng))
        r = ps.primary_test(xx, INSTR, rng, n_null=2000)
        hits += r.p_heaping < ps.ALPHA
    say(f"  n = {n:<4} power = {hits/200:.3f}")

# Figure -----------------------------------------------------------------------
fig, ax = plt.subplots(1, 2, figsize=(11, 4))
ax[0].plot(ratios, PC1_pg, lw=1, color="#1f4e79")
for name, r in ps.COMPETITORS.items():
    ax[0].axvline(r, ls="--", lw=0.8, color="#c0392b" if "162" in name else "#7f8c8d")
    ax[0].text(r, ax[0].get_ylim()[1] if False else PC1_pg.max() * 1.02, name, rotation=90,
               fontsize=7, ha="right", va="bottom")
ax[0].set_xlabel("size ratio r (period ln r)")
ax[0].set_ylabel("Rayleigh R")
ax[0].set_title("PC1: injected ladder, n=150 — periodogram")
ax[0].set_ylim(0, PC1_pg.max() * 1.35)
sig = np.linspace(0, 0.5, 300)
ax[1].semilogy(sig, [ps.expected_R_gaussian(s) for s in sig], color="#1f4e79")
ax[1].axvline(0.10, ls="--", color="#c0392b", lw=0.8)
ax[1].text(0.102, 1e-3, "Letter 114 width bound (10 %)", rotation=90, fontsize=7, color="#c0392b")
ax[1].axvline(math.log(1.5), ls=":", color="#7f8c8d", lw=0.8)
ax[1].text(math.log(1.5) + 0.004, 1e-3, "eyewitness ~ factor 1.5", rotation=90, fontsize=7)
for n, c in ((30, "#999"), (100, "#555"), (1000, "#111")):
    ax[1].axhline(math.sqrt(math.log(100) / n), lw=0.7, color=c)
    ax[1].text(0.38, math.sqrt(math.log(100) / n) * 1.1, f"~detection floor, n={n}", fontsize=7)
ax[1].set_ylim(1e-4, 1.2)
ax[1].set_xlabel("total log-scatter sigma (intrinsic + measurement)")
ax[1].set_ylabel("expected R at P0 for a perfect ladder")
ax[1].set_title("What a real ladder can show, by data quality")
fig.tight_layout()
fig.savefig(OUT / "fig_positive_control.png", dpi=150)
(OUT / "step1_positive_control_output.txt").write_text("\n".join(lines) + "\n")
