#!/usr/bin/env python
# coding=utf-8

a = [ [ 0 for x in range(3) ] for y in range(2) ]
print a
b = [ [0] * 3 ] *2
print b


a[0][0] =1
b[0][0] = 1
print a
print b
