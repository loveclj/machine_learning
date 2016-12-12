#encoding=utf-8
import time
import math
import numpy as np


x = [ i*0.001 for i in xrange(1000000)]

start = time.clock()
for i,t in enumerate(x):
    x[i] = math.sin(t)

print "math.sin: ", time.clock() - start

x = [ i * 0.001 for i in xrange(1000000)]
x = np.array(x)
start = time.clock()
np.sin(x,x)
print "numpy.sin: ",time.clock() - start


x = [ i * 0.001 for i in xrange(1000000)]
x = np.array(x)
start = time.clock()
for i,t in enumerate(x):
    x[i] = np.sin(t)

print "single numpy.sin: ", time.clock() - start  #numpy.sin比math.sin快10倍多。这得利于numpy.sin在C语言级
#别的循环计算。numpy.sin同样也支持对单个数值求正弦,例如:numpy.sin(0.5)。不过值得注意的
#是,对单个数的计算math.sin则比numpy.sin快得多了

print type(math.sin(0.5))
print type(np.sin(0.5))