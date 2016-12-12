__author__ = 'lizhifeng'

import numpy as np

a = np.arange(0,4)
print a
b = np.arange(2,6)

print b

print np.add(a,b)

def triangle_wave(x, c, c0, hc):
    x =  x -int(x)
    if x >= c:
        r = 0.0
    elif x < c0:
        r= x/c0*hc
    else:
        r = (c-x)/(c-c0)*hc
    return r

x = np.linspace(0, 2, 10000)
y =np.array([triangle_wave(t,0.6,0.4,1.0) for t in x])

a = np.arange(0,60,10).reshape(-1,2)
print a