#!/usr/bin/env python
# coding=utf-8

m = 2
n = 3

matrix = [None]*m

for i in xrange(m):
    matrix[i] = [None]*n

for i in xrange(m):
    for j in xrange(n):
        matrix[i][j] = j

print matrix

