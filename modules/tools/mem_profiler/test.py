#!/usr/bin/env python
# coding=utf-8


@profile
def listAppend(N):
    target =[]
    target.append(range(N))
    target.append(range(N))
    target.append(range(N))
    target.append(range(N))

if __name__ == "__main__":
    listAppend(1000)

