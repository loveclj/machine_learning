__author__ = 'lizhifeng'

import numpy as np
from scipy.optimize  import leastsq
import pylab as pl

def func(x, p):
    A, k, theata = p
    return A*np.sin(2*np.pi*k*x+theata)

def residuals(p, y, x):
    return y - func(x,p)

x = np.linspace(0,-2*np.pi, 100)
A,k,theta = 10,0.34,np.pi/6

y0 = func(x,[A,k,theta])
y1 = y0 + 2 *np.random.randn(len(x))

p0 = [7,0.2,0]

plsq = leastsq(residuals,p0,args=(y1,x))
print "real paramter:",[A,k,theta]
print "return parameter:",plsq[0]

pl.plot(x, y0, label="real")
pl.plot(x, y1, label="noise")
pl.plot(x, func(x,plsq[0]), label="return")
pl.legend()
pl.show()
