#!/usr/bin/env python
# coding=utf-8

def fibonacci_naive():
    i, j = 0, 1
    count = 0
    while j < 5000:
        if j%2:
            count += 1
        i , j = j, i + j
    return count

def fibonacci_transform():
    count = 0
    for f in fibonacci():
        if f > 5000:
            break
        if f % 2:
            count += 1
    return count

from itertools import islice

def fibonacci_succinct():
    is_odd = lambda x:x%2
    first_5000 = islice(fibonacci(), 0, 5000)
    return sum(1 for x in first_5000 if is_odd(x))
