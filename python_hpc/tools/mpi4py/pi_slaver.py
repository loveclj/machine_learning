#!/usr/bin/env python
from mpi4py import MPI
import numpy
import time

comm = MPI.Comm.Get_parent()
size = comm.Get_size()
rank = comm.Get_rank()

'''
N = numpy.array(0, dtype='i')
comm.Bcast([N, MPI.INT], root=0)
h = 1.0 / N; s = 0.0
for i in range(rank, N, size):
    x = h * (i + 0.5)
    s += 4.0 / (1.0 + x**2)
PI = numpy.array(s * h, dtype='d')
print PI
comm.Reduce([PI, MPI.DOUBLE], None,
            op=MPI.SUM, root=0)

'''

t = time.time()
m = 1000000
arr = numpy.array(range(m),'i')
print " slaver numpy  %f" %(time.time() -t)
t = time.time()

comm.Reduce([arr, MPI.DOUBLE], None,
            op=MPI.SUM, root=0)
print " slaver %f" %(time.time() -t)
comm.Disconnect()
