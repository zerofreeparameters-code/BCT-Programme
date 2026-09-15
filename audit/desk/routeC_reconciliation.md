# DESK CHECK — ROUTE C (SAKHAROV–JACOBSON INDUCED GRAVITY): LEDGER-CONFLICT RECONCILIATION

**Not a gate.** No pre-registration, no quarantine, no fresh thread. A bookkeeping reconciliation
run against the live checkout `~/BCT-Programme`, to settle a live contradiction in the Cold Ledger
**before** any Gate RC is scheduled. Archive under `audit/desk/routeC_reconciliation.md`.

Drafted 16 September 2026. Author session had the ledger auto-loaded; the two confirmations below are
to be run/read on Michel's machine against the actual `audit/gates/T/`, `audit/gates/IG/` and
`audit/gates/BZ/` deliverables, which this session did not open.

---

## THE CONFLICT (two live, contradictory ledger entries)

1. **Open item 6** lists *"Gate IG Route C (Sakharov–Jacobson): remains **open**. The Brillouin-zone
   integral over the true FCC truncated-octahedron zone (vs. Debye sphere) is the remaining decisive
   calculation."*
2. **CN-BZ-01…06** records Route C as *already **closed** by Gate T*, and finds the Gate IG
   "one-loop momentum integral over the Brillouin zone" is a **proper-time heat-kernel with no
   momentum-space domain** (a category error), with moment index **p a free parameter spanning 4.18%**
   in G_ind, the 1.5255% square-face undershoot and −1.53% G_ind discrepancy being the *same
   dimensional identity*.

Both entries are live. This desk check decides which stands, on two independent questions.

---

## RECONCILIATION 1 — DOES GATE T ALREADY CLOSE ROUTE C?

**Logical reconciliation.** The Sakharov–Jacobson (thermodynamic / Jacobson gr-qc/9504004) route reads
Newton's constant off a **single, direction-independent** entropy-per-area coefficient η (η = 1/4G in
the standard construction). Gate T established that the area-law coefficient κ **varies ~10.7% across
cut directions** on the FCC geometry. A direction-dependent κ means no single η exists — the input the
Jacobson step requires is not available. Therefore **Gate T's finding forecloses Route C's η**, and
open item 6's "remains open" is stale. CN-BZ is correct on this point.

**Confirmation (Michel's Mac, against the live checkout):**
- Open `audit/gates/T/` and read the κ-vs-cut-direction result (or re-run its script). Confirm the
  directional spread is non-zero (~10.7%) and that Gate T's own verdict was "no single η."
- Confirm Route C / Gate IG's induced-G step assumes (explicitly or implicitly) a single η or a single
  isotropic cutoff. If it does, Gate T's variation kills it.
- **Pass condition for "closed by T":** κ is direction-dependent AND Route C needs a single η. If both
  hold → Route C closed by Gate T; update open item 6.
- **Surprise condition:** if Gate T's κ turns out *direction-independent* after all, or Route C's
  construction does not actually need a single η → this reconciliation fails and Gate RC is warranted.

---

## RECONCILIATION 2 — IS THE GATE IG "BZ INTEGRAL" A HEAT-KERNEL WITH NO MOMENTUM DOMAIN?

**Logical reconciliation.** Sakharov induced gravity via the one-loop effective action is a
**heat-kernel / proper-time** computation: W = ½ ln det Δ = −½ ∫_ε^∞ (ds/s) Tr e^{−sΔ}, and the induced
1/G is the coefficient of ∫√g R, i.e. the Seeley–DeWitt a₁ term. `routeC_heatkernel_structure.py`
(textbook machinery, attached) shows that in d=4 **1/G ∝ a₁ · (1/ε)** — set by a single proper-time
cutoff ε, with **no ∫_BZ d³k factor anywhere**. Consequently the Brillouin-zone *shape* (truncated
octahedron vs Debye sphere) **does not enter** the expression, and open item 6's "decisive calculation"
(sharpening the zone) refines the geometry of a momentum domain the method does not possess. The free
"moment index p" (CN-BZ: span 4.18%) lives exactly where the illustration predicts: in *which* SD moment
/ *which* power of ε is identified with 1/G, and in the shape factor used to map a momentum cutoff to ε —
an identification ambiguity, not a zone integral. CN-BZ is correct on this point too.

**Confirmation (Michel's Mac, against the live checkout):**
- Locate the printed Gate IG "one-loop BZ integral" (in `audit/gates/IG/` and/or the corpus App it
  audits). Classify its measure: is it ∫_zone d³k over the FCC zone, or ∫ds/s Tr e^{−sΔ} (proper time)?
- If proper-time: confirm the zone shape does not appear, and locate the definition of the moment index
  p and its 4.18% span (per CN-BZ).
- **Pass condition for "ill-posed as posed":** the integral is a heat-kernel with no momentum domain AND
  p is free. Then the truncated-octahedron calculation cannot fix G_ind.
- **Surprise condition:** if the IG expression is genuinely a convergent ∫_zone d³k with the zone shape
  entering and p fixed → this reconciliation fails and Gate RC (zone-integral audit) is warranted.

---

## VERDICT (contingent on the two confirmations)

**If both pass (expected): Route C is not a live gate.** It is closed by Gate T (no single η) and
ill-posed as posed (heat-kernel with no momentum domain; free p). Action: revise **open item 6** to
"Route C CLOSED by Gate T (no single η) + method is a heat-kernel, not a BZ integral (CN-BZ); the
truncated-octahedron calculation refines a non-existent domain — do not schedule." Gate RC stands down.
With N / F-Fb / T / IG / QP / AM / R2 and the PROMOTE shared-root closure, **gravity is closed across
every audited route**; curved-space *kinematics* (prior art — Barceló–Liberati–Visser gr-qc/0011026)
is all the phonon-on-a-flowing-background delivers.

**If either surprises: escalate to Gate RC** (the pre-registered, fresh-thread gate). Exactly one of two
triggers licenses it: (a) Gate T's κ is direction-independent, or Route C does not need a single η; or
(b) the Gate IG integral is a genuine convergent zone integral with the zone shape entering and p fixed.
Absent one of those, running Gate RC would be auditing closed ground.

---

## FILES
- `routeC_reconciliation.md` (this file)
- `routeC_heatkernel_structure.py` — textbook illustration of the induced-G heat-kernel structure
  (supports Reconciliation 2; not a verification of Gate IG's specific number)

*Desk check, not a gate. Its purpose is to remove a contradiction from the ledger, not to derive physics.
The physics conclusion it points to — Route C closed/ill-posed — becomes load-bearing only after the two
machine confirmations against the actual T/IG deliverables.*
