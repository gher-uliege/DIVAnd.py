import numpy as np
import julia

j = julia.Julia()
#j = julia.Julia(debug=True)
#j.eval('push!(LOAD_PATH, joinpath(ENV["HOME"],"projects/Julia/DIVAnd.jl/src"))')
j.using("DIVAnd")

def DIVAnd(mask, pmn, xi, x, f, corlen, epsilon2):
    va = j.DIVAndrunfi(
        np.transpose(mask),
        tuple([np.transpose(_) for _ in pmn]),
        tuple([np.transpose(_) for _ in xi]),
        x, f, corlen, epsilon2)

    return np.ma.MaskedArray(np.transpose(va), np.logical_not(mask))


def metric(lon, lat):
    return j.DIVAnd_metric(lon, lat)
