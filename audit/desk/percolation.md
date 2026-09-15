# Desk check — the FCC interstitial network percolates

**Non-gate verification (15 Sep 2026).** Confirms a claim on the *surviving* geometric layer:
that the BCT (= FCC at c/a=√2) interstitial void space is a single connected network the
superfluid can flow through, and identifies its flow bottleneck. Textbook FCC geometry;
stacking-blind; independent of the contested S¹/S² field-content questions.

**Script.** `percolation_deskcheck.py` — builds a 4×4×4 conventional-cell FCC supercell,
enumerates octahedral and tetrahedral void sites, links oct↔tet pairs that share a triangular
face (separation √3·a/4), and tests connectivity + percolation with `networkx`. Deterministic;
needs `numpy`, `scipy`, `networkx`. Re-run: `python3 percolation_deskcheck.py`.

**Result (reproduced on M. Cabrié's machine, Python 3.9.6).**
- Void radii, ratios to the sphere radius (convention-free): r_oct/r_s = √2−1 = 0.414214,
  r_tet/r_s = √(3/2)−1 = 0.224745, r_window/r_s = 2/√3−1 = 0.154701.
- In corpus units (r_s = 1/2): r_oct = 0.207107, r_tet = 0.112372, r_window = 0.077350.
- Ordering: window (0.1547) < tet (0.2247) < oct (0.4142) — the shared triangular window
  (three mutually touching spheres) is the true bottleneck, narrower than either chamber.
- Network: a single connected component (768/768 nodes); bulk octahedral chambers each share
  8 triangular windows with tetrahedral chambers; the component percolates in all three axes.

**Reading.** The sphere surfaces are the walls, the octahedral/tetrahedral voids are the
chambers, and the chambers connect through triangular windows into one percolating flow network
(the oct→tet→oct diffusion pathway of real FCC metals). This is an ordinary S¹-superfluid
property — it does **not** require hopfions or an S² order parameter, and it is essentially an
independent re-derivation of the exterior void-condensate the appendices posit. It stands
whatever Gate KL concludes about the knot-lattice.
