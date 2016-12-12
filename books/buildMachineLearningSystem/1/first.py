#!/usr/bin/env python
# coding=utf-8
import scipy as sp
import matplotlib.pyplot as plt

from func import *

data    =   sp.genfromtxt("web_traffic.tsv", delimiter="\t")

print "data shape is ",
print data.shape

x       =   data[:,0]
y       =   data[:,1]

print "number of NAN in y",
print sp.sum(sp.isnan(y))

x       =   x[~sp.isnan(y)]
y       =   y[~sp.isnan(y)]

plt.scatter(x,y)
plt.title("web traffic")
plt.xlabel("time")
plt.ylabel("hits/hour")
plt.xticks([w*7*24 for w in range(10)], ['week %i' %w for w in range(10)])
plt.autoscale(tight = True)
plt.grid()

fp1, res,  = sp.polyfit(x, y, 1, True)
#fp1, res, rank, sv, rcond = sp.polyfit(x, y, 1, True)

print("module parameter %s" %fp1)
print("res is %s" %res)

f1  = sp.poly1d(fp1)

print error(f1, x, y)
fx  = sp.linspace(0, x[-1], 1000)
plt.plot(fx, f1(fx), linewidth=4)
plt.legend(["d=%i" % f1.order], loc="upper left")
plt.show()
