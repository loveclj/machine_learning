#!/usr/bin/env python
# coding=utf-8


from mpi4py import MPI 
import numpy
import time

comm = MPI.COMM_WORLD

rank =  comm.Get_rank()

#list = range(10)
list = 1

arr = numpy.array(list, dtype='i')
comm.Reduce([arr,MPI.INT],None, op=MPI.SUM, root=0)
#comm.Disconnect()
time.sleep(2) 
if rank == 0:
    print arr
else:
    print arr
