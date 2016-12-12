#!/usr/bin/env python
# coding=utf-8

import time

start  = time.time()

suma = 0

arr = range(1000000)
for i in arr: 
    tmp = arr[i]
    suma += tmp * tmp


print time.time() - start

start  = time.time()

sumb = sum(arr * arr)
print time.time() - start



