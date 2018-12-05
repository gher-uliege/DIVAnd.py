import numpy as np
import julia
from julia import DIVAnd as D

metric = D.DIVAnd_metric

def DIVAnd(mask, pmn, xi, x, f, corlen, epsilon2):
    va = D.DIVAndrunfi(
        np.transpose(mask),
        tuple([np.transpose(_) for _ in pmn]),
        tuple([np.transpose(_) for _ in xi]),
        x, f, corlen, epsilon2)

    return np.ma.MaskedArray(np.transpose(va), np.logical_not(mask))
