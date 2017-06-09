from __future__ import print_function
import numpy as np
from divand import divand, metric

xi, yi = np.meshgrid([0.0, 0.5, 1.0], [0.0, 0.333333, 0.666667, 1.0])

pm,pn = metric(xi,yi)

print('pm',pm)
