"""Gate SONO - Q4 fit scoring of Letter 110's #154 and #155 under Gate PRED2's grammar and charges.

Grammar: the code below is PRED2's pred2_step2_grammar.py / pred2_step3_score.py logic reproduced line for line
(atoms, 22 unary + 4 binary operations, node-count complexity, exhaustive enumeration, density per unit ln x in the
narrowest log-window with >= 60 hits, P = rho * 2 eps, raw bits = -log2 P). The ONLY change is that the atom list is a
parameter, because PRED2's rule 'add any atom the census shows the corpus using' obliges this run to add the three
Bessel zeros Letter 110 names (j_{1,1}, j_{1,2}, j_{2,1}) for #155, whose expression j_{1,2}/j_{1,1} does not exist
in PRED2's 20-atom grammar. #154 is scored under both atom sets.

Scoring rule (card 6): delta_154 = (r_tet/r_oct)/(lambda_UV/lambda_peak)_obs - 1, delta_155 = (j12/j11)/(lambda1/lambda2)_obs - 1,
'obs' = the letter's printed ratios 200/370 and 700/380. eps = |delta|. Thresholds >= 10 / 3-10 / < 3 bits.
Charges (PRED2 lines, floors, fixed before any number below was seen - see gate_SONO_RESULT.md Q4 preamble):
  LE_targets   = log2(92)                          PRED2's census floor, charged to every prediction
  LE_constants = log2(12)                          the card's enumerated palette {r_tet/r_oct, r_oct/r_tet, j12/j11, j21/j11} + inverses + squares
  LE_pairs     = log2(C(n_feat, 2))                wavelength pairs a reader could form from features named in the traced sources
  drift        = log2( ln(R_hi/R_lo) / (2 eps) )   comparison-value charge: tolerance windows inside the documented drift of the chosen 'observed' value
  corr/date    = 0                                 no post-hoc factor in either expression
"""
import math, sys, itertools
from mpmath import mp, besseljzero, sqrt as msqrt
mp.dps = 30

# ---------------- PRED2 grammar, atoms parameterised ----------------
a0 = ((math.sqrt(2) - 1) / 2) * ((math.sqrt(6) - 2) / 4) / math.pi
PRED2_ATOMS = {
    '1': 1.0, '2': 2.0, '3': 3.0, '4': 4.0, '6': 6.0, '8': 8.0, '12': 12.0, '24': 24.0, '48': 48.0,
    'pi': math.pi, 'sqrt2': math.sqrt(2), 'sqrt3': math.sqrt(3), 'sqrt6': math.sqrt(6), 'e': math.e,
    'a0': a0, 'r_tet': (math.sqrt(6) - 2) / 4, 'r_oct': (math.sqrt(2) - 1) / 2, 'R': 0.5,
    'S_D4': math.pi ** 5 / 6, 'x_lep': 4 * a0 / math.pi,
}
BESSEL_ATOMS = {'j11': float(besseljzero(1, 1)), 'j12': float(besseljzero(1, 2)), 'j21': float(besseljzero(2, 1))}
LIM = 1e60

def _p(x, n):
    try:
        v = x ** n
        return v if abs(v) < LIM else None
    except (OverflowError, ZeroDivisionError, ValueError):
        return None

UN = []
UN.append(('sqrt', lambda x: math.sqrt(x) if x >= 0 else None))
for n in (2, 3, 4, 5): UN.append((f'^{n}', (lambda n: lambda x: _p(x, n))(n)))
for n in (1, 2, 3, 4, 5): UN.append((f'^-{n}', (lambda n: lambda x: _p(x, -n) if x != 0 else None)(n)))
UN.append(('exp', lambda x: math.exp(x) if -700 < x < 130 else None))
UN.append(('ln', lambda x: math.log(x) if x > 0 else None))
UN.append(('1/(1-x)', lambda x: 1.0 / (1 - x) if abs(1 - x) > 1e-12 else None))
UN.append(('cos', lambda x: math.cos(x) if abs(x) < 1e6 else None))
UN.append(('tan', lambda x: (lambda t: t if abs(t) < 1e12 else None)(math.tan(x)) if abs(x) < 1e6 else None))
UN.append(('acos', lambda x: math.acos(x) if -1 <= x <= 1 else None))
UN.append(('atan', lambda x: math.atan(x)))
BIN = [('+', lambda a, b: a + b), ('-', lambda a, b: a - b), ('*', lambda a, b: a * b if abs(a * b) < LIM else None),
       ('/', lambda a, b: a / b if b != 0 and abs(a / b) < LIM else None)]
NU, NB = len(UN), len(BIN)

def enumerate_levels(atoms, CEX):
    """levels[C] = list of (value, expr_string) of complexity exactly C, as PRED2 generates them (duplicates kept)."""
    names = list(atoms.keys()); vals = list(atoms.values())
    levels = [None, [(v, n) for v, n in zip(vals, names)]]
    for C in range(2, CEX + 1):
        out = []
        for un, f in UN:
            for v, s in levels[C - 1]:
                r = f(v)
                if r is not None and abs(r) < LIM and not math.isnan(r):
                    out.append((r, f'{un}({s})'))
        for i in range(1, C - 1):
            for bn, g in BIN:
                for a, sa in levels[i]:
                    for b, sb in levels[C - 1 - i]:
                        r = g(a, b)
                        if r is not None and not math.isnan(r):
                            out.append((r, f'({sa}{bn}{sb})'))
        levels.append(out)
    return levels

def logdensity(pool, T):
    """PRED2's rule: values per unit ln(x) near T, narrowest window with >= 60 hits."""
    n = len(pool); lt = math.log(abs(T))
    for w in (0.002, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.4, 0.8):
        hits = [v for v in pool if v > 0 and abs(math.log(v) - lt) <= w]
        if len(hits) >= 60:
            return len(hits) / (n * 2 * w), w, len(hits), n
    hits = [v for v in pool if v > 0 and abs(math.log(v) - lt) <= 0.8]
    return (len(hits) + 1) / (n * 1.6), 0.8, len(hits), n

def raw_bits(pool, T, eps):
    d, w, nh, n = logdensity(pool, T)
    p = min(1.0, d * 2 * abs(eps))
    return (-math.log2(p) if p > 0 else float('inf')), p, d, w, nh, n

# ---------------- targets (card 6; values from sono_q2_reproduce.py) ----------------
r_tet = PRED2_ATOMS['r_tet']; r_oct = PRED2_ATOMS['r_oct']
j11, j12, j21 = BESSEL_ATOMS['j11'], BESSEL_ATOMS['j12'], BESSEL_ATOMS['j21']
T154 = 200 / 370; eps154 = abs((r_tet / r_oct) / T154 - 1)
T155 = 700 / 380; eps155 = abs((j12 / j11) / T155 - 1)
C_EXPR = 3   # atom / atom

CEX = int(sys.argv[1]) if len(sys.argv) > 1 else 4
print(f"eps_154 = {eps154:.6e}  T_154 = {T154:.10f}   eps_155 = {eps155:.6e}  T_155 = {T155:.10f}   C_expr = {C_EXPR}")
print()

results = {}
for label, atoms in (('PRED2 20 atoms', PRED2_ATOMS), ('PRED2 + 3 Bessel zeros (23 atoms)', {**PRED2_ATOMS, **BESSEL_ATOMS})):
    levels = enumerate_levels(atoms, CEX)
    print(f"=== grammar: {label} ===")
    for C in range(1, CEX + 1):
        vals = [v for v, s in levels[C]]
        print(f"  C={C}: generated {len(vals):,}, distinct (12 s.f.) {len(set(float(f'{v:.12e}') for v in vals)):,}")
    for tag, T, eps in (('#154 r_tet/r_oct vs 200/370', T154, eps154), ('#155 j12/j11 vs 700/380', T155, eps155)):
        if tag.startswith('#155') and 'j11' not in atoms:
            print(f"  {tag}: expression j12/j11 NOT expressible in this grammar - not scored here")
            continue
        for C in range(2, CEX + 1):
            pool = [v for v, s in levels[C] if v and math.isfinite(v) and v != 0]
            b, p, d, w, nh, n = raw_bits(pool, T, eps)
            mark = '  <-- scored level (C_expr)' if C == C_EXPR else ''
            print(f"  {tag}  C={C}: p_raw={p:.3e} raw bits={b:6.2f} (window {w}, hits {nh}/{n}){mark}")
            if C == C_EXPR:
                results[(label, tag)] = b
        # exhaustive cross-check at C <= C_expr: distinct values within eps of T, and the best (inverse-symbolic control)
        allv = [(v, s) for C in range(1, C_EXPR + 1) for v, s in levels[C] if v and math.isfinite(v)]
        within = {}
        for v, s in allv:
            if abs(v / T - 1) <= eps:
                within.setdefault(float(f'{v:.12e}'), s)
        ndist = len(set(float(f'{v:.12e}') for v, s in allv))
        best = min(allv, key=lambda t: abs(t[0] / T - 1))
        print(f"     exhaustive C<={C_EXPR}: {len(within)} distinct values within eps of T out of {ndist:,} distinct values "
              f"(fraction {len(within)/ndist:.3e} -> {-math.log2(len(within)/ndist) if within else float('inf'):.2f} bits)")
        print(f"     control (best C<={C_EXPR} expression for T): {best[1]} = {best[0]:.8f}, |eps| = {abs(best[0]/T-1):.3e}")
        ex = sorted(within.items(), key=lambda kv: abs(kv[0] / T - 1))[:6]
        print("     nearest in-window expressions:", '; '.join(f'{s}={v:.6f}' for v, s in ex))
    print()

# ---------------- charges (floors, fixed in the Q4 preamble) ----------------
LE_targets = math.log2(92)
LE_constants = math.log2(12)
LE_pairs = {'#154': math.log2(math.comb(4, 2)), '#155': math.log2(math.comb(6, 2))}
drift = {'#154': max(0.0, math.log2(math.log(370 / 336) / (2 * eps154))),
         '#155': max(0.0, math.log2(math.log(550 / 350) / (2 * eps155)))}
print("=== charge sheet (bits) ===")
print(f"LE_targets = log2(92) = {LE_targets:.2f};  LE_constants = log2(12) = {LE_constants:.2f}")
print(f"LE_pairs: #154 log2(C(4,2)=6) = {LE_pairs['#154']:.2f}; #155 log2(C(6,2)=15) = {LE_pairs['#155']:.2f}")
print(f"drift: #154 log2(ln(370/336)/(2 eps)) = {drift['#154']:.2f} [N = {math.log(370/336)/(2*eps154):.1f} windows];"
      f" #155 log2(ln(550/350)/(2 eps)) = {drift['#155']:.2f} [N = {math.log(550/350)/(2*eps155):.1f} windows]")
print()
print(f"{'prediction':46s} {'grammar':36s} {'raw':>6s} {'LE_t':>6s} {'LE_c':>6s} {'pairs':>6s} {'drift':>6s} {'net':>7s}  bin")
for (label, tag), b in results.items():
    key = tag[:4]
    net = b - LE_targets - LE_constants - LE_pairs[key] - drift[key]
    net_nodrift = b - LE_targets - LE_constants - LE_pairs[key]
    bin_ = 'SURPRISING' if net >= 10 else ('suggestive' if net >= 3 else 'unsurprising')
    print(f"{tag:46s} {label:36s} {b:6.2f} {LE_targets:6.2f} {LE_constants:6.2f} {LE_pairs[key]:6.2f} {drift[key]:6.2f} {net:7.2f}  {bin_}"
          f"   (net without drift charge: {net_nodrift:.2f}; raw minus LE_targets only: {b-LE_targets:.2f})")
