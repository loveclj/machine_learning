#!/usr/bin/env python
# coding=utf-8

import time
import thread

def add(N):
    sum = 0
    for i in xrange(N):
        sum = sum + i
    print sum

def testMultiThread(mThreads, N):
    for i in range(mThreads):
        thread.start_new_thread(add,(N/mThreads,))

if __name__ == "__main__":
    t = time.time()
    testMultiThread(2,100000)
    time.sleep(2)
    print time.time() - t




