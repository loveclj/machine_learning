#!/usr/bin/env python
# coding=utf-8

def fibonacii(n):
    a = 1
    b = 1
    while a < n:
        yield a
        a, b = b, a + b


for i in fibonacii(20):
    print i


constructor = fibonacii(20)

while True:
    try:
        print constructor.next()
    except:
        print "catch error"
        break
    
