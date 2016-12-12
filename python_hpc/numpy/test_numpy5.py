__author__ = 'lizhifeng'

import numpy as np

a = np.arange(10).reshape(2,-1)
print a
print a.dtype

a.tofile("a.bin")
b = np.fromfile("a.bin", dtype=np.float)
print b
print b.dtype

c =np.fromfile("a.bin", dtype=np.int32)
print c
print c.dtype

d = np.fromfile("a.bin", dtype=np.int64)
print d
print d.dtype

np.save("a.npy", a)
c = np.load("a.npy")
print c



################savez
a = np.array([[1,2,3],[4,5,6]])
b = np.arange(0, 1.0, 0.1)
c = np.sin(b)
np.savez("result.npz", a, b, sin_array =c)
r = np.load("result.npz")
print r["arr_0"]
print r["arr_1"]
print r["sin_array"]

a =np.arange(0,12,0.5).reshape(4,-1)
np.savetxt("a.txt",a)
b = np.loadtxt("a.txt")
print a
print b

f = file("r.npy", "wb")
np.save(f, a)
np.save(f, c)
f.close()
f =file("r.npy","rb")
print np.load(f)
print np.load(f)