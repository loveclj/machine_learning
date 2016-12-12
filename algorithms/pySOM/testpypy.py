#!/usr/bin/env python
# coding=utf-8

arr = [2,3]
print id(arr[0])
print id(arr[1])

arr[1] += 2
print id(arr[0])
print id(arr[1])
