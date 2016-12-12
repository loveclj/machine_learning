__author__ = 'lizhifeng'

import numpy as np

a = np.arange(1,10).reshape(3,3)
print a

print a*a
print np.dot(a,a)

a = np.arange(12).reshape(2,3,2)
b = np.arange(12,24).reshape(2,2,3)

c =np.dot(a,b)

print np.alltrue(c[0,:,0,:] == np.dot(a[0],b[0]))

a = np.random.rand(5,5)
b =np.random.rand(5)
print a
print b

x = np.linalg.solve(a,b)
print x