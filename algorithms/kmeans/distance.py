import numpy as np
import random
import scipy.spatial.distance as dist
#import scipy.spatial.distance.euclidean as eucl
import timeit
import time

vecLen  = 500000

i = 0
vec1 = []
vec2 = []

while i < vecLen:
    vec1.append(random.random())
    vec2.append(random.random())
    i += 1

def getDistance(vec1, vec2):
    dimension =  len(vec1)
    distance = 0
    i  = 0
    while i < dimension:
        v1 = vec1[i]
        v2 = vec2[i]
        distance += (v1-v2)*(v1-v2)
        i = i + 1
    return np.sqrt(distance)

start = time.clock()

print getDistance(vec1, vec2)

stop  = time.clock()

print "time of getDistance is %f" % (stop -start)

start = time.clock()

print dist.euclidean(vec1, vec2)

stop  = time.clock()

print "time of dist.euclidean is %f" % (stop -start)

#t = timeit.Timer("getDistance(vec1, vec2)","from __main__ import getDistance, vec1, vec2")
#print t.timeit(10)

#t2 = timeit.Timer("dist.euclidean(vec1, vec2", "from __main__ import vec1, vec2, dist")




