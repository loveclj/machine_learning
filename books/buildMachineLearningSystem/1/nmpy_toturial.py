#!/usr/bin/env python
# coding=utf-8

import numpy

print numpy.version.full_version

arr = numpy.array(range(10, 0, -1))

print arr

print arr.shape

print arr.ndim

print arr.clip(2,5)
b = arr.reshape(5,2)

print b.shape
print b.ndim

c = arr ** 2
print c


print arr[numpy.array([2,3,4])]

print arr >4

arr[arr > 4] = 4
print arr

print "----------------------------"

d = numpy.array([1,2,3,6,8,numpy.NAN])
print d
print numpy.isnan(d)

e = numpy.array([1,2,3,6,8,numpy.NAN, 3.9])
print e.dtype
print d.dtype
