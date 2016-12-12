#!/usr/bin/env python
# coding=utf-8
import profile

def arrayAdd(N):
    i = 0
    sum = 0
    while i < N:
        sum += i
        i=i+1


def profileTest():
    total = 1
    for i in range(100000):
        total = total * (i + 1)
    arrayAdd(1000000)
    arrayAdd(100000)
    arrayAdd(100000)
    return total


if __name__ == "__main__":
    profile.run("profileTest()")
