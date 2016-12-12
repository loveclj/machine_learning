#!/usr/bin/env python
# coding=utf-8


def listAppend(element, list = []):
    list.append(element)
    print list
    return list

def listAppendFix(element, list = None): 
    if list is None:
        list = []

    list.append(element)
    print list
    return list




if "__main__" == __name__:
    print " listAppend  use default Parameter empty list :"
    listAppend(1)
    listAppend(2)
    listAppend(3)
    print "--------------------"
    print " listAppend use default Parameter None:"
    listAppendFix(1)
    listAppendFix(2)
    listAppendFix(3)


