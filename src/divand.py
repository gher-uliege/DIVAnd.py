import numpy as np
import julia
j = julia.Julia();
j.using("divand")

def divand(mask,pmn,xi,x,f,len,epsilon2):
    va,s = j.divandrun(
        np.transpose(mask),
        tuple([np.transpose(_) for _ in pmn]),
        tuple([np.transpose(_) for _ in xi]),
        x,f,len,epsilon2)

    return np.ma.MaskedArray(np.transpose(va),np.logical_not(mask)),s

def metric(Lon,Lat):
    return j.divand_metric(Lon,Lat)
