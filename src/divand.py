import numpy as np
import julia

j = julia.Julia()
j.using("divand")


def divand(mask, pmn, xi, x, f, corlen, epsilon2):
    va, s = j.divandrun(
        np.transpose(mask),
        tuple([np.transpose(_) for _ in pmn]),
        tuple([np.transpose(_) for _ in xi]),
        x, f, corlen, epsilon2)

    return np.ma.MaskedArray(np.transpose(va), np.logical_not(mask)), s


def metric(lon, lat):
    return j.divand_metric(lon, lat)
