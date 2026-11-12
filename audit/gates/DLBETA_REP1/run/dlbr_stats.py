"""
Gate DL-BETA REP1 -- estimators and the card's rules (REP1 section 4.4-4.5), fixed before the first run.

Readings of the card wording beyond R1-R9 (RD = run decision, fixed here before any simulation):
 RD1  "sigma of block means / sqrt(20)": sample standard deviation (ddof = 1) of the 20 block means.
 RD2  C jackknife: C_i = N_loops * population variance with block i removed; err = sqrt((n-1)/n sum (C_i - mean)^2).
 RD3  Locate extension: grid points at step 0.01; an extension adds 0.25 on the side whose edge is within 0.05
      of beta_0, clipped to [0.20, 4.00]. If beta_0 is within 0.05 of an edge that already sits at 0.20 or 4.00,
      there is no interior C maximum (-> SC-DLBR-5).
 RD4  L = 4 "at an edge" = the lowest or highest grid point; one 0.005 point is added on that side (both starts),
      and beta_4 is recomputed; repeated until interior.
 RD5  Hysteresis "differ by more than 3 sigma": |E_hot - E_cold| > 3 sqrt(s_hot^2 + s_cold^2), 20-block errors.
 RD6  Mixed-run readings are E measured right after sweeps 50, 100, ..., 2000; E_end = mean of the 10 readings
      after sweeps 1550, 1600, ..., 2000.
 RD7  Mixed-grid extensions per round: if there is no weak win (and fewer than 8 extensions so far) add one
      0.0025 step above the current highest point; then, if there is no strong win (and fewer than 8 so far), add
      one step below the current lowest point. Each added point counts as one extension. Max 8 per size.
 RD8  "At most one unresolved L = 8 point" counts every L = 8 mixed run made (grid and extensions).
 RD9  If no L = 6 primary flip exists, the L = 8 grid (centred on beta_mix(6)) is undefined and L = 8 is not run.
 RD10 Q5 "either side of beta_inf": the L = 6 scan points (hot and cold) nearest below and above beta_inf, and
      the two L = 8 runs that define Delta E; "at beta = 20": the K3 void run (L = 2, L_t = 6, cold).
 RD11 K5 flip interval: under the fixed-band rule with E*_hc; S = highest strong win, W = lowest weak win,
      interval [min(S,W), max(S,W)]; K5 passes iff it meets [1.0051, 1.0171] (R4).
 RD12 beta grid values are held as integers in units of 1e-7 and converted by n / 1e7 for simulation and seeds.
"""
import numpy as np

NB = 20


def block_means(x, nb=NB):
    x = np.asarray(x, dtype=float)
    assert len(x) % nb == 0, "measurement count not divisible into 20 equal blocks"
    return x.reshape(nb, -1).mean(axis=1)


def block_err(x, nb=NB):
    bm = block_means(x, nb)
    return float(np.std(bm, ddof=1) / np.sqrt(nb))


def spec_heat(x, Np):
    x = np.asarray(x, dtype=float)
    return float(Np * np.var(x))          # population variance (ddof = 0)


def spec_heat_jk(x, Np, nb=NB):
    x = np.asarray(x, dtype=float)
    blocks = x.reshape(nb, -1)
    Ci = []
    for i in range(nb):
        rest = np.concatenate([blocks[j] for j in range(nb) if j != i])
        Ci.append(Np * np.var(rest))
    Ci = np.array(Ci)
    return float(np.sqrt((nb - 1) / nb * np.sum((Ci - Ci.mean()) ** 2)))


def argmax_low(vals):
    """index of the maximum; ties -> lowest index (lowest beta), R2/R3."""
    vals = np.asarray(vals, dtype=float)
    return int(np.flatnonzero(vals == vals.max())[0])


def largest_fall(betas_n, E):
    """R3: fall over (b_i, b_{i+1}) = E_i - E_{i+1}; ties to the lower beta. betas_n sorted, uniform step."""
    E = np.asarray(E, dtype=float)
    falls = E[:-1] - E[1:]
    i = argmax_low(falls)
    return i, float(falls[i])


def two_peaks(x, nbins=50):
    """R7. Returns (two_peaks: bool, counts, edges, peaks)."""
    x = np.asarray(x, dtype=float)
    counts, edges = np.histogram(x, bins=nbins, range=(x.min(), x.max()))
    cmax = counts.max()
    peaks = []
    for i in range(nbins):
        lo, hi = max(0, i - 5), min(nbins, i + 6)
        if counts[i] != counts[lo:hi].max():
            continue
        if i > 0 and counts[i - 1] == counts[i]:
            continue                      # not the first bin of a plateau
        if counts[i] < 0.10 * cmax:
            continue
        peaks.append(i)
    two = False
    pair = None
    for a in range(len(peaks)):
        for b in range(a + 1, len(peaks)):
            i, j = peaks[a], peaks[b]
            m = 0.5 * min(counts[i], counts[j])
            if j - i >= 2 and np.any(counts[i + 1:j] < m):
                two = True
                pair = (i, j, int(counts[i + 1:j].min()))
                break
        if two:
            break
    return two, counts, edges, peaks, pair


def binder(x):
    x = np.asarray(x, dtype=float)
    return float(1.0 - np.mean(x ** 4) / (3.0 * np.mean(x ** 2) ** 2))


def outcome_primary(E_end, Sb, Wb):
    """C1: f = (S - E_end)/(S - W). Returns (outcome, f, flagged)."""
    gap = Sb - Wb
    if gap <= 0:
        return "unresolved", float("nan"), True
    f = (Sb - E_end) / gap
    if f < 1.0 / 3.0:
        return "strong", float(f), False
    if f > 2.0 / 3.0:
        return "weak", float(f), False
    return "unresolved", float(f), False


def outcome_band(E_end, Estar):
    """original rule: weak if E_end < E* - 0.01, strong if E_end > E* + 0.01."""
    if E_end < Estar - 0.01:
        return "weak"
    if E_end > Estar + 0.01:
        return "strong"
    return "unresolved"


def flip(betas_n, outcomes):
    """S = highest beta with a strong win, W = lowest with a weak win.
    Returns dict(exists, S, W, lo, hi, mid, nonmono, n_unres_inside, n_unres_total)."""
    b = np.asarray(betas_n)
    st = [bb for bb, o in zip(b, outcomes) if o == "strong"]
    wk = [bb for bb, o in zip(b, outcomes) if o == "weak"]
    un = [bb for bb, o in zip(b, outcomes) if o == "unresolved"]
    d = dict(exists=False, S=None, W=None, lo=None, hi=None, mid=None, nonmono=False,
             n_unres_total=len(un), has_strong=len(st) > 0, has_weak=len(wk) > 0)
    if st and wk:
        S = int(max(st)); W = int(min(wk))
        lo, hi = min(S, W), max(S, W)
        d.update(exists=True, S=S, W=W, lo=lo, hi=hi, mid=(S + W) / 2.0, nonmono=S > W,
                 n_unres_inside=sum(1 for u in un if lo < u < hi))
    return d
