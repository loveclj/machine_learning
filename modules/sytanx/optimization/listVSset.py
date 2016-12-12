#!/usr/bin/env python
# coding=utf-8
from time import time
lista=[1,2,3,4,5,6,7,8,9,13,34,53,43,44]
listb=[2,4,6,9,23]

interserction=[]

t = time()
for i in xrange(100000):
    for  a in lista:
        for b in listb:
            if a == b:
                interserction.append(a)

print "list intersection is: %f " %(time() -t)


interserction=[]

t = time()
for i in xrange(100000):
    list(set(lista)&set(listb))

print "set  intersection is: %f " %(time() -t)

