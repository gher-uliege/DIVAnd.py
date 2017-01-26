import numpy as np
import netCDF4
import matplotlib.pyplot as plt
from divand import divand, metric

# bathymetry
fname = "diva_bath.nc"

nc = netCDF4.Dataset(fname)

b = nc.variables["bat"][:,:]
lon = nc.variables["lon"][:]
lat = nc.variables["lat"][:]

Lon,Lat = np.meshgrid(lon,lat)
mask = b < 0

pm,pn = metric(Lon,Lat)

# data file
A = np.loadtxt("temperature_argo.txt")

xobs = A[:,0];
yobs = A[:,1];
vobs = A[:,2];
lenx = 800e3; # in meters
leny = 800e3; # in meters
sdn = 1.

# compute anomalies
vmean = np.mean(vobs[:])
vanom = vobs - vmean

# make the analysis
va,s = divand(mask,(pm,pn),(Lon,Lat),(xobs,yobs),vobs,(lenx,leny),sdn);

v = va + vmean
plt.pcolor(Lon,Lat,v); plt.colorbar()
plt.savefig("divand_argo.png")
