import numpy as np
import julia
from julia import DIVAnd as D

metric = D.DIVAnd_metric

def DIVAnd(mask, pmn, xi, x, f, corlen, epsilon2):
    va = D.DIVAndrunfi(
        np.swapaxes(mask,1,0),
        tuple([np.swapaxes(_,1,0) for _ in pmn]),
        tuple([np.swapaxes(_,1,0) for _ in xi]),
        x, f, corlen, epsilon2)

    return np.ma.MaskedArray(np.swapaxes(va,1,0), np.logical_not(mask))
