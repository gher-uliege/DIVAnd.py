import numpy as np
import julia
from divand import divand, metric


xi,yi=np.meshgrid([0.0,0.5,1.0],[0.0,0.333333,0.666667,1.0])

mask = np.full(xi.shape, True, dtype=bool)
pm = np.ones(xi.shape) / (xi[0,1]-xi[0,0])
pn = np.ones(xi.shape) / (yi[1,0]-yi[0,0])

epsilon = 1e-10;

x,y = np.meshgrid(np.linspace(epsilon,1-epsilon,3),np.linspace(epsilon,1-epsilon,3))
x = x[:]
y = y[:]
v = np.sin(x*6) * np.cos(y*6)

lenx = .15;
leny = .15;

sdn = 20;

va,s = divand(np.transpose(mask),(pm,pn),(xi,yi),(x,y),v,(lenx,leny),sdn);

print "va",va
