import random
#import scipy.spatial.distance.euclidean as eucl
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
#    return np.sqrt(distance)
    return distance

start = time.clock()

value = getDistance(vec1, vec2)

stop  = time.clock()

print stop - start
print value


