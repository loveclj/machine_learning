#!/usr/bin/env python
from mpi4py import MPI
import numpy
import sys
import time

comm = MPI.COMM_SELF.Spawn(sys.executable,
                           args=['pi_slaver.py'],
                           maxprocs=2)

'''
N = numpy.array(100, 'i')
comm.Bcast([N, MPI.INT], root=MPI.ROOT)
PI = numpy.array(0.0, 'd')
comm.Reduce(None, [PI, MPI.DOUBLE],
            op=MPI.SUM, root=MPI.ROOT)
print(PI)
            '''

m = 1000000
t = time.time()
arr = numpy.array(range(m),'i')
print "master %f" %(time.time() - t)

now = time.time()
comm.Reduce(None, [arr,MPI.DOUBLE],
            op=MPI.SUM, root=MPI.ROOT)
print "master reduce %f " %(time.time() -now)
print t



