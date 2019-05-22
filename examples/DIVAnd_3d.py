from __future__ import print_function
from julia import DIVAnd as julia_DIVAnd
import DIVAnd
import numpy as np
import matplotlib.pyplot as plt


x = np.random.rand(75);
y = np.random.rand(75);
z = np.random.rand(75);
f = np.sin(x*6) * np.cos(y*6)+np.sin(z*6) * np.cos(x*6) ;

testsize=300
testsizez=3
xi,yi,zi = np.meshgrid(np.arange(0,1,1/testsize),
                       np.arange(0,1,1/testsize),
                       np.arange(0,1,1/testsizez),
                       indexing="ij");

fref = np.sin(xi*6) * np.cos(yi*6)+np.sin(zi*6) * np.cos(xi*6) ;

mask = np.ones(xi.shape)==1;

pm = np.ones(xi.shape) / (xi[1,0,0]-xi[0,0,0])
pn = np.ones(xi.shape) / (yi[0,1,0]-yi[0,0,0])
po = np.ones(xi.shape) / (zi[0,0,1]-zi[0,0,0])

lenx = 0.5;

epsilon2 = 1.;

va = julia_DIVAnd.DIVAndrunfi(mask,(pm,pn,po),(xi,yi,zi),(x,y,z),f,lenx,epsilon2)
print("va range", va.max(),va.min())
print("va.shape", va.shape)


va2 = DIVAnd.DIVAnd(mask,(po,pn,pm),(zi,yi,xi),(z,y,x),f,lenx,epsilon2)
print("va2 range", va2.max(),va2.min())
print("va2.shape", va2.shape)

plt.pcolor(va[:,:,1])
plt.show()

plt.pcolor(va2[:,:,1])
plt.show()
