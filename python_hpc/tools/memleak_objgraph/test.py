#!/usr/bin/env python
# coding=utf-8

import objgraph



list = []

for i in range(10):
    list.append(i)

tupple =(list)

for i in tupple:
    print i
objgraph.show_most_common_types()

