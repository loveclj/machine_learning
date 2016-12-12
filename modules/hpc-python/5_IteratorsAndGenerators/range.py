#!/usr/bin/env python
# coding=utf-8

def range(start, stop, step = 1):
    list =[]
    if step < 0:
        start, stop = stop, start
        step = -step

    while start < stop:
        list.append(start)
        start += step
    return list


l = range(1,10,1)
print l
