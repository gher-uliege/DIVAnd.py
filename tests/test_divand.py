from __future__ import print_function
import numpy as np
from divand import divand, metric


def test_divand():
    xi, yi = np.meshgrid([0.0, 0.5, 1.0], [0.0, 0.333333, 0.666667, 1.0])

    mask = np.full(xi.shape, True, dtype=bool)
    pm = np.ones(xi.shape) / (xi[0, 1] - xi[0, 0])
    pn = np.ones(xi.shape) / (yi[1, 0] - yi[0, 0])

    epsilon = 1e-10

    x, y = np.meshgrid(np.linspace(epsilon, 1-epsilon, 3),
                       np.linspace(epsilon, 1-epsilon, 3))
    x = x.flatten()
    y = y.flatten()
    v = np.sin(x*6) * np.cos(y*6)

    lenx = .15
    leny = .15

    epsilon2 = 0.05

    #va, s = divand(mask, (pm, pn), (xi, yi), (x, y), v, (lenx, leny), epsilon2)
    va = divand(mask, (pm, pn), (xi, yi), (x, y), v, (lenx, leny), epsilon2)

    print("va", va)
    assert va.shape == xi.shape
