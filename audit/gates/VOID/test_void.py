#!/usr/bin/env python3
"""Unit tests for Gate VOID scripts.  Run:  python3 -m pytest -q test_void.py   (or python3 test_void.py)

Fast variants of every check in the gate (small Monte Carlo, coarse grids);
the full-size runs are reproduced by the scripts' main() entry points.
"""
import math
import unittest

import numpy as np
import mpmath as mp
import sympy as sp

import void_geometry as vg
import void_eigen as ve
import void_x as vx


class TestGeometry(unittest.TestCase):
    def test_solid_angle_identity_exact(self):
        self.assertTrue(vg.solid_angle_identity_exact())

    def test_solid_angles_numeric(self):
        # 8 tet vertices + 6 oct vertices around each sphere cover 4 pi
        tot = vg.N(8 * vg.OMEGA_T + 6 * vg.OMEGA_O)
        self.assertLess(abs(tot - 4 * mp.pi), mp.mpf(10) ** -50)

    def test_volume_sum_exact(self):
        ok, lhs, rhs = vg.volume_sum_check()
        self.assertTrue(ok)
        self.assertLess(abs(lhs - rhs), mp.mpf(10) ** -50)

    def test_warm_thread_forecast_values(self):
        # gate card §0: 0.02597 / 0.13157 / 0.18351 / ball 0.00594 / 0.03721
        self.assertAlmostEqual(float(vg.N(vg.V_TET)), 0.02597, places=5)
        self.assertAlmostEqual(float(vg.N(vg.V_OCT)), 0.13157, places=5)
        self.assertAlmostEqual(float(vg.N(vg.V_OCT + 2 * vg.V_TET)), 0.18351, places=5)
        self.assertAlmostEqual(float(vg.N(vg.V_BALL_TET)), 0.00594, places=5)
        self.assertAlmostEqual(float(vg.N(vg.V_BALL_OCT)), 0.03721, places=5)

    def test_inscribed_radii_match_corpus(self):
        self.assertEqual(sp.simplify(vg.R_OCT - (sp.sqrt(2) - 1) / 2), 0)
        self.assertEqual(sp.simplify(vg.R_TET - (sp.sqrt(6) - 2) / 4), 0)

    def test_window_positive_and_small(self):
        w = float(vg.N(vg.A_WINDOW))
        self.assertGreater(w, 0)
        self.assertLess(w, float(vg.N(vg.A_FACE)))

    def test_wall_area_sums_to_sphere(self):
        # per sphere: 8 tet sectors + 6 oct sectors = full sphere area pi
        tot = vg.N(2 * vg.WALL_TET + vg.WALL_OCT)   # 2 tet + 1 oct chambers per sphere
        self.assertLess(abs(tot - mp.pi), mp.mpf(10) ** -50)

    def test_monte_carlo_small(self):
        mc = vg.monte_carlo_check(n=400_000, seed=17)
        for k, d in mc.items():
            self.assertLess(abs(d["z"]), 4.0, k)


class TestEigen(unittest.TestCase):
    def test_masks_partition(self):
        for dom in ("ball", "network", "oct", "tet"):
            h, d, dr, nm = ve.masks(32, dom)
            self.assertFalse(np.any(d & dr))
            self.assertFalse(np.any(d & nm))
            self.assertFalse(np.any(dr & nm))
            self.assertGreater(d.sum(), 0)

    def test_network_unknown_fraction(self):
        # free points / all points -> geometric void fraction 0.2595 as N grows
        h, d, dr, nm = ve.masks(64, "network")
        frac = d.sum() / d.size
        self.assertAlmostEqual(frac, 0.25952, delta=0.01)

    def test_laplacian_symmetric_spd(self):
        L, h, n = ve.laplacian(24, "oct")
        self.assertLess(abs(L - L.T).max(), 1e-12)
        self.assertGreater(ve.lowest_eigenvalue(24, "oct", verbose=False)[0], 0)

    def test_ball_coarse(self):
        lam, h, n = ve.lowest_eigenvalue(32, "ball", verbose=False)
        self.assertAlmostEqual(lam, 4 * math.pi ** 2, delta=0.1 * 4 * math.pi ** 2)

    def test_richardson_recovers_exact(self):
        hs = [1 / 48, 1 / 64, 1 / 96]
        lam0, C = 100.0, 50.0
        for p in (1.0, 2.0):
            lams = [lam0 + C * h ** p for h in hs]
            ex = ve.richardson(hs, lams)
            self.assertAlmostEqual(float(ex["primary"]), lam0, places=6)

    def test_chamber_below_network_bound(self):
        # min over chambers of the Neumann-window eigenvalue must not exceed the network value
        lo = ve.lowest_eigenvalue(32, "oct", verbose=False)[0]
        net = ve.lowest_eigenvalue(32, "network", verbose=False)[0]
        self.assertLessEqual(lo, net * 1.02)


class TestX(unittest.TestCase):
    def test_corpus_reproduction(self):
        rows = vx.evaluate(mp.mpf(146), mp.mpf(435))
        c = rows["(i) corpus"]
        self.assertAlmostEqual(float(c["x_EW"]), 0.33917, places=5)
        self.assertAlmostEqual(float(c["x_SU3_NLO"]), 0.72127, places=5)
        self.assertAlmostEqual(float(c["x_SU3_NNLO"]), 0.71954, places=5)
        self.assertAlmostEqual(float(rows["L127 boxed (not GP)"]["x_EW"]), 0.33666, places=5)

    def test_corpus_intermediate_table(self):
        # Letter 127 App AZ10.4 table
        self.assertAlmostEqual(float(vx.N(vx.ALPHA0)), 0.00740806, places=8)
        self.assertAlmostEqual(float(vx.N(vx.NLO)), 0.01018282, places=8)
        self.assertAlmostEqual(float(vx.N(2 * vx.MU_TET_BALL * vx.V_TET_BALL / vx.S_QCD)), 0.72868532, places=7)

    def test_shift_factors(self):
        rows = vx.evaluate(mp.mpf(146), mp.mpf(435))
        r = float(rows["(ii) true V, ball mu"]["x_EW"] / rows["(i) corpus"]["x_EW"])
        self.assertAlmostEqual(r, float(vg.N(vg.V_OCT / vg.V_BALL_OCT)), places=10)

    def test_p_void(self):
        p, pf, dp, vgeo = vx.p_void_40()
        self.assertTrue(p.startswith("0.370974707015939"))
        self.assertTrue(pf.startswith("0.370709726"))
        self.assertTrue(vgeo.startswith("0.2595195103"))

    def test_hierarchy_undefined_above_one(self):
        self.assertIsNone(vx.hierarchy_scale(vx.N(vx.S_QCD), mp.mpf("1.75")))
        self.assertIsNotNone(vx.hierarchy_scale(vx.N(vx.S_QCD), mp.mpf("0.72")))


if __name__ == "__main__":
    unittest.main(verbosity=2)
