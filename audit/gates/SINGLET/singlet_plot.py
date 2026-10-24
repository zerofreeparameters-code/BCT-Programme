#!/usr/bin/env python3
"""
Gate SINGLET -- figure: E(theta) of the signed-measure construction under three readouts,
against the singlet curve -cos(theta). All curves are the t -> inf closed forms, which the
scripts singlet_step0.py / singlet_priorart.py reproduce numerically (m = 24 sites shown as markers).
Palette: categorical slots 1-3 of the dataviz reference palette (validated all-pairs, light mode);
aqua is below 3:1 on the surface, so every series is direct-labelled and the RESULT carries the table.
Run: python3 -I singlet_plot.py [out.png]
"""
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

SURF, INK, INK2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df"
BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"

th = np.linspace(0, np.pi, 400)
s, c = np.abs(np.sin(th / 2)), np.abs(np.cos(th / 2))
Eq = lambda q: (s ** q - c ** q) / (s ** q + c ** q)
ths = np.arange(0, 13) * np.pi / 12
ss, cs = np.abs(np.sin(ths / 2)), np.abs(np.cos(ths / 2))
Eqs = lambda q: (ss ** q - cs ** q) / (ss ** q + cs ** q)
V = 4 / np.pi ** 2

fig, ax = plt.subplots(figsize=(7.2, 4.4), dpi=160)
fig.patch.set_facecolor(SURF); ax.set_facecolor(SURF)
ax.axhline(0, color=GRID, lw=1, zorder=0)
for y in (-1, -0.5, 0.5, 1):
    ax.axhline(y, color=GRID, lw=0.6, zorder=0)
ax.plot(np.degrees(th), -np.cos(th), color=INK2, lw=1.2, ls=(0, (4, 3)), zorder=1, label="singlet  −cos θ")
ax.plot(np.degrees(th), Eq(2), color=BLUE, lw=2, zorder=3, label="squared readout |M|² (Born)")
ax.plot(np.degrees(ths), Eqs(2), "o", ms=6, color=BLUE, mec=SURF, mew=1.5, zorder=4)
ax.plot(np.degrees(th), Eq(4), color=ORANGE, lw=2, zorder=2, label="readout |M|⁴ (per-pair normalised)")
ax.plot(np.degrees(ths), Eqs(4), "s", ms=6, color=ORANGE, mec=SURF, mew=1.5, zorder=4)
ax.plot(np.degrees(th), -V * np.cos(th), color=AQUA, lw=2, zorder=2, label="site-complete hemisphere readout")
ax.plot(np.degrees(ths), -V * np.cos(ths), "^", ms=6, color=AQUA, mec=SURF, mew=1.5, zorder=4)
# direct labels (text in ink, mark carries identity)
ax.annotate("|M|²: −cos θ, |S| = 2√2", xy=(60, -0.5), xytext=(70, -0.86), color=INK, fontsize=8.5,
            arrowprops=dict(arrowstyle="-", color=INK2, lw=0.6))
ax.annotate("|M|⁴: |S| = 3.77, flat marginals,\nnormalisation needs both settings", xy=(117, 0.78),
            xytext=(4, 0.74), color=INK, fontsize=8.5, arrowprops=dict(arrowstyle="-", color=INK2, lw=0.6))
ax.annotate("site-complete: −(4/π²) cos θ, |S| = 1.15", xy=(135, V * 0.7071), xytext=(96, 0.62), color=INK,
            fontsize=8.5, arrowprops=dict(arrowstyle="-", color=INK2, lw=0.6))
ax.set_xlim(0, 180); ax.set_ylim(-1.08, 1.08)
ax.set_xticks(range(0, 181, 30)); ax.set_yticks([-1, -0.5, 0, 0.5, 1])
ax.set_xlabel("setting difference θ = b − a (degrees)", color=INK2, fontsize=9)
ax.set_ylabel("correlation E(θ)", color=INK2, fontsize=9)
ax.tick_params(colors=INK2, labelsize=8, length=0)
for sp in ax.spines.values():
    sp.set_visible(False)
ax.set_title("Signed-measure construction: the readout exponent picks the curve", color=INK, fontsize=10.5,
             loc="left", pad=10)
leg = ax.legend(loc="lower right", fontsize=7.8, frameon=False, labelcolor=INK)
fig.text(0.01, 0.005, "t → ∞ closed forms; markers = m = 24 lattice settings. The |M|² curve lies exactly on −cos θ. Periodic sector (Z₂ sign dropped): E ≡ 0.",
         color=INK2, fontsize=7)
fig.tight_layout(rect=(0, 0.03, 1, 1))
fig.savefig(sys.argv[1] if len(sys.argv) > 1 else "singlet_E_theta.png", facecolor=SURF)
