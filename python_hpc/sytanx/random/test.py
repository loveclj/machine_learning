#!/usr/bin/env python
# coding=utf-8

import random 
from random import Random

print random.random()

''' Random  is a class '''
t = Random()
print t.random()

''' id  is same  '''
print id(random.random())
print id(t.random())

list = range(10)
print random.shuffle(list)
print list

''' same seed same output?'''
random.seed(1)
print random.random()

random.seed(1)
print random.random()

print random.choice(list)

random.seed(1)
print random.gauss(0,1)
print random.gauss(0,1)
print random.gauss(0,1)



'''detail in help '''

