#!/usr/bin/env python
# coding=utf-8
import numpy as np


a = np.array([2,3])
print a

print id(a[1])
print id(a[0])

a[1] += 2

print id(a[1])
print id(a[0])
