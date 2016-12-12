#!/usr/bin/env python
# coding=utf-8

class Test():
    i = 2
    def add(self):
        Test.i = Test.i + 1
    


t = Test()
t.add()
print t.i

t2 = Test()
t3 = Test()

print t2.i

t2.add()

print t2.i

print t3.i
