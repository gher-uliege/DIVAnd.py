import os
import shutil
import unittest
import netCDF4
import numpy as np
from divand import divand, metric

print("Running Divand tests")
print(" ")


class TestDivand(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.outputdir = "./outputs"
        if not os.path.exists(cls.outputdir):
            os.makedirs(cls.outputdir)

        cls.xi, cls.yi = np.meshgrid([0.0, 0.5, 1.0], [0.0, 0.333333, 0.666667, 1.0])
        cls.mask = np.full(cls.xi.shape, True, dtype=bool)


    def test_metrics(self):
        """
        Test the metric computation
        """
        pm, pn = metric(self.xi, self.yi)

        self.assertEqual(pm.shape, (4, 3))
        self.assertEqual(pn.shape, (4, 3))
        """
        self.assertAlmostEqual(self.pm[0, 0], 2.69795966e-05)
        self.assertEqual(self.pm[1, 1], self.pm[3, 1])
        self.assertAlmostEqual(self.pn[0, 1], 1.79864067e-05)
        self.assertAlmostEqual(self.pn[2, 2], 1.79876244e-05)
        self.assertEqual(self.pn[-1, 0], self.pn[-1, 1])
        """

    def test_divandcalc(self):
        """
        Test the interpolation on a simple case
        """
        pm, pn = metric(self.xi, self.yi)
        epsilon = 1e-10

        x, y = np.meshgrid(np.linspace(epsilon, 1 - epsilon, 3),
                           np.linspace(epsilon, 1 - epsilon, 3))
        x = x.flatten()
        y = y.flatten()
        v = np.sin(x * 6) * np.cos(y * 6)

        lenx = .15
        leny = .15
        epsilon2 = 0.05

        va = divand(self.mask, (pm, pn), (self.xi, self.yi), (x, y), v, (lenx, leny), epsilon2)

        self.assertEqual(va.shape, (4, 3))
        self.assertAlmostEqual(va[2, 1], -1.91700011637e-10)
        self.assertAlmostEqual(va.mean(), -3.0683031149438756e-11)
        self.assertAlmostEqual(va.max(),3.87256023191e-10)
        self.assertAlmostEqual(va.min(), -7.66761116239e-10)

        with netCDF4.Dataset(os.path.join(self.outputdir, "test.nc"), "w") as nc:
            lat = nc.createDimension("lat", self.xi.shape[0])
            lon = nc.createDimension("lon", self.xi.shape[1])
            latitudes = nc.createVariable("lat", "f4", ("lat", "lon",))
            longitudes = nc.createVariable("lon", "f4", ("lat", "lon",))
            field = nc.createVariable("field", "f4", ("lat", "lon",))
            latitudes[:] = self.yi
            longitudes[:] = self.xi
            field[:] = va

        self.assertTrue(os.path.exists(os.path.join(self.outputdir, "test.nc")))


    @classmethod
    def tearDown(cls):
        pass
        shutil.rmtree(cls.outputdir)
