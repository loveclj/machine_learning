#!/usr/bin/env python
# coding=utf-8

import time

start = 1
stop  = 10000000

step  = 1

def xrange(start, stop, step):
    while start < stop:
        yield start
        start += step


def range(start, stop, step):
    list = []
    while start < stop:
        list.append(start)
        start += step
    return list

time_start = time.time()
xrange_sum  = sum(xrange(start, stop, step))
time_stop   = time.time()
print "xrange_sum time  elpased: ", time_stop - time_start, " s"


time_start = time.time()
range_sum  = sum(range(start, stop, step))
time_stop   = time.time()
print "range_sum time  elpased: ", time_stop - time_start, " s"
