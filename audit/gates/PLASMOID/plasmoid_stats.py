#!/usr/bin/env python3
"""Gate PLASMOID — test machinery (card sections 2.1-2.4).

Fixed before any real dataset is scored. Everything here follows the card:

  2.1  x = ln D ; period P0 = ln(j11/j01) ; phase free.
  2.2  Primary statistic: Rayleigh R at P0,  theta_i = 2 pi (x_i mod P0)/P0,
       R = |mean(exp(i theta_i))|.  One primary test per dataset.
  2.3  Heaping-aware null: (1) smooth density for x (log-normal = primary;
       Gaussian KDE with bandwidth >= P0 = sensitivity); (2) the dataset's own
       rounding scheme, estimated from its reported numbers; (3) 10 000 synthetic
       datasets of the same size, rounded the same way; p = share of null R >=
       observed R.  alpha = 0.01.
  2.4  Periodogram R(P) for ratios 1.2-2.5, with competitor ratios marked.

Rounding model ("report generator").  A report is either a single number or a
range [a, b] (scored as the geometric mean), or — for datasets that use them —
a comparison object ("basketball").  Each reported number v is assigned the
coarsest step s from the dataset's unit grid that divides it exactly
(metric grid 1,2,5,10,20,50,100,200,500,1000 cm; imperial grid 1,2,3,6,12,24,36 in);
its relative coarseness is c = s/v.  The null draws a true size from the smooth
density, picks a report type with the observed frequencies, draws c (and unit
system) from the observed values, rounds to the grid step nearest c*v in log,
and for ranges draws the observed log-width.  Comparison-object reports snap to
the nearest object size (in log) among the objects the dataset actually uses.
This reproduces multiples of 5 and 10, "half"/"double" values (the 1-2-5 grid),
feet and inches, and object heaping — the card's 2.3(2) list.

Instrument data use the same code with a single fixed step (the resolution).
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field

import numpy as np
from scipy.special import jn_zeros

J01 = float(jn_zeros(0, 1)[0])
J11 = float(jn_zeros(1, 1)[0])
RATIO0 = J11 / J01
P0 = math.log(RATIO0)
ALPHA = 0.01
N_NULL = 10_000

COMPETITORS = {
    "j11/j01 (#162)": RATIO0,
    "phi": (1 + 5 ** 0.5) / 2,
    "R5 = 10^(1/5)": 10 ** 0.2,
    "sqrt(e)": math.e ** 0.5,
    "1.5": 1.5,
    "2": 2.0,
}

METRIC_STEPS_CM = np.array([1, 2, 5, 10, 20, 50, 100, 200, 500, 1000], float)
IMPERIAL_STEPS_IN = np.array([1, 2, 3, 6, 12, 24, 36], float)
CM_PER_IN = 2.54


# ----------------------------------------------------------------------------
# Statistics
# ----------------------------------------------------------------------------
def rayleigh_R(x: np.ndarray, P: float = P0) -> float:
    th = 2 * np.pi * np.mod(x, P) / P
    return float(np.abs(np.exp(1j * th).mean()))


def rayleigh_R_batch(X: np.ndarray, P: float = P0) -> np.ndarray:
    """X shape (m, n) -> R for each row."""
    th = 2 * np.pi * np.mod(X, P) / P
    return np.abs(np.exp(1j * th).mean(axis=1))


def ratio_grid(lo: float = 1.2, hi: float = 2.5, step: float = 0.0005) -> np.ndarray:
    return np.round(np.arange(lo, hi + step / 2, step), 6)


def periodogram(x: np.ndarray, ratios: np.ndarray) -> np.ndarray:
    P = np.log(ratios)[:, None]
    th = 2 * np.pi * x[None, :] / P          # mod is unnecessary inside exp
    return np.abs(np.exp(1j * th).mean(axis=1))


def periodogram_batch(X: np.ndarray, ratios: np.ndarray, chunk: int = 500) -> np.ndarray:
    """X (m, n) -> (m, len(ratios))."""
    out = np.empty((X.shape[0], len(ratios)))
    w = 2 * np.pi / np.log(ratios)           # angular frequency in x
    for i in range(0, X.shape[0], chunk):
        Xc = X[i:i + chunk]
        ph = Xc[:, None, :] * w[None, :, None]
        out[i:i + chunk] = np.abs(np.exp(1j * ph).mean(axis=2))
    return out


def expected_R_gaussian(sigma_log: float, P: float = P0) -> float:
    """Expected Rayleigh R for a perfect ladder with Gaussian log-scatter sigma."""
    return math.exp(-2 * math.pi ** 2 * sigma_log ** 2 / P ** 2)


def periods_spanned(x: np.ndarray, P: float = P0) -> float:
    return float((x.max() - x.min()) / P)


# ----------------------------------------------------------------------------
# Rounding scheme estimation
# ----------------------------------------------------------------------------
def coarsest_step(v: float, unit: str) -> float:
    """Coarsest grid step (in the value's own unit) dividing v exactly."""
    steps = METRIC_STEPS_CM if unit == "cm" else IMPERIAL_STEPS_IN
    best = None
    for s in steps:
        q = v / s
        if abs(q - round(q)) < 1e-9 and round(q) >= 1:
            best = s
    return best if best is not None else 0.0   # 0 => finer than grid


@dataclass
class Report:
    kind: str                 # "single" | "range" | "object"
    values_native: tuple = () # reported numbers in native unit
    unit: str = "cm"          # "cm" or "in"
    object_cm: float | None = None

    def value_cm(self) -> float:
        if self.kind == "object":
            return float(self.object_cm)
        f = CM_PER_IN if self.unit == "in" else 1.0
        vs = [v * f for v in self.values_native]
        return float(math.exp(np.mean(np.log(vs))))


@dataclass
class RoundingScheme:
    p_single: float
    p_range: float
    p_object: float
    c_values: np.ndarray            # relative coarseness of reported numbers
    c_units: np.ndarray             # unit of each c value ("cm"/"in")
    range_logwidths: np.ndarray
    object_sizes_cm: np.ndarray = field(default_factory=lambda: np.array([]))
    fixed_step_cm: float | None = None   # instrument resolution, if any

    @staticmethod
    def from_reports(reports: list[Report]) -> "RoundingScheme":
        n = len(reports)
        ks = [r.kind for r in reports]
        cs, us, lw, objs = [], [], [], []
        for r in reports:
            if r.kind == "object":
                objs.append(r.object_cm)
                continue
            for v in r.values_native:
                s = coarsest_step(v, r.unit)
                cs.append(s / v if s > 0 else 0.0)
                us.append(r.unit)
            if r.kind == "range":
                a, b = r.values_native
                lw.append(math.log(b / a))
        return RoundingScheme(
            p_single=ks.count("single") / n,
            p_range=ks.count("range") / n,
            p_object=ks.count("object") / n,
            c_values=np.array(cs, float),
            c_units=np.array(us),
            range_logwidths=np.array(lw, float),
            object_sizes_cm=np.array(sorted(set(objs)), float),
        )

    @staticmethod
    def instrument(step_cm: float) -> "RoundingScheme":
        return RoundingScheme(1.0, 0.0, 0.0, np.array([]), np.array([]),
                              np.array([]), np.array([]), fixed_step_cm=step_cm)

    def terminal_digit_audit(self, reports: list[Report]) -> dict:
        nums_cm, nat = [], []
        for r in reports:
            if r.kind == "object":
                continue
            for v in r.values_native:
                nat.append((v, r.unit))
                nums_cm.append(v * (CM_PER_IN if r.unit == "in" else 1.0))
        cm_only = [v for v, u in nat if u == "cm"]
        in_only = [v for v, u in nat if u == "in"]
        def share(pred, xs):
            return (sum(1 for x in xs if pred(x)) / len(xs)) if xs else float("nan")
        return {
            "n_reports": len(reports),
            "n_numbers": len(nat),
            "share_range_reports": self.p_range,
            "share_object_reports": self.p_object,
            "cm: share multiple of 10 cm": share(lambda v: abs(v / 10 - round(v / 10)) < 1e-9, cm_only),
            "cm: share multiple of 5 (not 10) cm": share(lambda v: abs(v / 5 - round(v / 5)) < 1e-9 and abs(v / 10 - round(v / 10)) > 1e-9, cm_only),
            "cm: share on 1-2-5 sequence (x10^k)": share(_on_125, cm_only),
            "in: share multiple of 12 in (whole feet)": share(lambda v: abs(v / 12 - round(v / 12)) < 1e-9, in_only),
            "in: share multiple of 3 in": share(lambda v: abs(v / 3 - round(v / 3)) < 1e-9, in_only),
            "share of numbers with c = 1 (value is itself a grid step)": share(lambda c: abs(c - 1) < 1e-9, list(self.c_values)),
            "ranges: share whose endpoints are half/double (b/a = 2)": share(lambda w: abs(w - math.log(2)) < 1e-9, list(self.range_logwidths)),
        }


def _on_125(v: float) -> bool:
    if v <= 0:
        return False
    k = math.floor(math.log10(v) + 1e-12)
    m = v / 10 ** k
    return any(abs(m - t) < 1e-9 for t in (1, 2, 5, 10))


def _round_to_grid(v: np.ndarray, c: np.ndarray, units: np.ndarray) -> np.ndarray:
    """Round true sizes v (cm) to the grid step nearest c*v (in log)."""
    out = np.empty_like(v)
    for unit, steps, f in (("cm", METRIC_STEPS_CM, 1.0), ("in", IMPERIAL_STEPS_IN, CM_PER_IN)):
        m = units == unit
        if not m.any():
            continue
        vn = v[m] / f
        cm = c[m]
        fine = cm <= 0
        target = np.where(fine, 1.0, cm * vn)
        idx = np.abs(np.log(steps)[None, :] - np.log(np.maximum(target, 1e-12))[:, None]).argmin(axis=1)
        s = steps[idx]
        s = np.where(fine, steps[0], s)
        r = np.maximum(np.round(vn / s), 1) * s
        out[m] = r * f
    return out


def apply_rounding(v_true: np.ndarray, scheme: RoundingScheme, rng: np.random.Generator) -> np.ndarray:
    """Turn true sizes (cm) into reported sizes (cm) under the scheme."""
    if scheme.fixed_step_cm is not None:
        s = scheme.fixed_step_cm
        return np.maximum(np.round(v_true / s), 1) * s
    n = v_true.size
    u = rng.random(n)
    kind = np.where(u < scheme.p_single, 0, np.where(u < scheme.p_single + scheme.p_range, 1, 2))
    out = np.empty(n)
    nc = len(scheme.c_values)

    m0 = kind == 0
    if m0.any():
        j = rng.integers(0, nc, m0.sum())
        out[m0] = _round_to_grid(v_true[m0], scheme.c_values[j], scheme.c_units[j])
    m1 = kind == 1
    if m1.any():
        k = m1.sum()
        w = scheme.range_logwidths[rng.integers(0, len(scheme.range_logwidths), k)]
        a = v_true[m1] * np.exp(-w / 2)
        b = v_true[m1] * np.exp(w / 2)
        ja = rng.integers(0, nc, k)
        jb = rng.integers(0, nc, k)
        # a range is stated in one unit system: use the unit of the first draw
        ua = scheme.c_units[ja]
        ar = _round_to_grid(a, scheme.c_values[ja], ua)
        br = _round_to_grid(b, scheme.c_values[jb], ua)
        br = np.maximum(br, ar)  # a range cannot invert
        out[m1] = np.sqrt(ar * br)
    m2 = kind == 2
    if m2.any():
        objs = scheme.object_sizes_cm
        idx = np.abs(np.log(objs)[None, :] - np.log(v_true[m2])[:, None]).argmin(axis=1)
        out[m2] = objs[idx]
    return out


# ----------------------------------------------------------------------------
# Smooth densities and the null
# ----------------------------------------------------------------------------
def sample_lognormal(x: np.ndarray, size: tuple, rng) -> np.ndarray:
    mu, sd = float(np.mean(x)), float(np.std(x, ddof=1))
    return np.exp(rng.normal(mu, sd, size))


def sample_kde(x: np.ndarray, size: tuple, rng, bw: float | None = None) -> np.ndarray:
    """Gaussian KDE in x with bandwidth max(P0, Silverman) unless given."""
    n = x.size
    silver = 1.06 * np.std(x, ddof=1) * n ** (-1 / 5)
    h = bw if bw is not None else max(P0, silver)
    centres = rng.choice(x, size=size, replace=True)
    return np.exp(centres + rng.normal(0, h, size))


def heaping_null(x_obs: np.ndarray, scheme: RoundingScheme, rng, n_null: int = N_NULL,
                 density: str = "lognormal") -> np.ndarray:
    """Return an (n_null, n) array of null log-sizes."""
    n = x_obs.size
    if density == "lognormal":
        V = sample_lognormal(x_obs, (n_null, n), rng)
    elif density == "kde":
        V = sample_kde(x_obs, (n_null, n), rng)
    else:
        raise ValueError(density)
    flat = apply_rounding(V.ravel(), scheme, rng)
    return np.log(flat.reshape(n_null, n))


@dataclass
class TestResult:
    n: int
    R_obs: float
    p_heaping: float
    p_heaping_plus1: float
    null_R: np.ndarray
    p_uniform_rayleigh: float
    span_periods: float

    def summary(self) -> str:
        return (f"n = {self.n}; span = {self.span_periods:.2f} periods of P0; "
                f"R_obs(P0) = {self.R_obs:.4f}; heaping-aware null: median R = "
                f"{np.median(self.null_R):.4f}, 99th pct = {np.percentile(self.null_R, 99):.4f}; "
                f"p = {self.p_heaping:.4f} [(k+1)/(N+1) = {self.p_heaping_plus1:.4f}]; "
                f"uniform-phase Rayleigh p (for contrast only) = {self.p_uniform_rayleigh:.4g}")


def rayleigh_uniform_p(R: float, n: int) -> float:
    """Standard Rayleigh p-value vs uniform phase (Zar 1999 approximation)."""
    Z = n * R ** 2
    p = math.exp(math.sqrt(1 + 4 * n + 4 * (n ** 2 - (n * R) ** 2)) - (1 + 2 * n))
    return min(1.0, max(p, 0.0)) if n > 1 else float("nan")


def primary_test(x_obs: np.ndarray, scheme: RoundingScheme, rng, n_null: int = N_NULL,
                 density: str = "lognormal") -> TestResult:
    R_obs = rayleigh_R(x_obs)
    X0 = heaping_null(x_obs, scheme, rng, n_null, density)
    nullR = rayleigh_R_batch(X0)
    k = int((nullR >= R_obs).sum())
    return TestResult(
        n=x_obs.size, R_obs=R_obs, p_heaping=k / n_null, p_heaping_plus1=(k + 1) / (n_null + 1),
        null_R=nullR, p_uniform_rayleigh=rayleigh_uniform_p(R_obs, x_obs.size),
        span_periods=periods_spanned(x_obs),
    )
