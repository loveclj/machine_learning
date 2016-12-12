#!/usr/bin/env python
# coding=utf-8
import time
import threading

class MultiThreadTest1(threading.Thread):
    def __init__(self, N):
        threading.Thread.__init__(self)
        self.N = N
    def run(self):
        self.sum = 0
        for i in xrange(self.N):
            self.sum = self.sum + i


class MultiThreadTest2(threading.Thread):
    def __init__(self, N):
        threading.Thread.__init__(self)
        self.N = N
    def run(self):
        self.sum = 0
        for i in xrange(self.N):
            self.sum = self.sum + i

def test(mThread, N):
    
    timeElapsed = time.time()

    threads = []
    for i in xrange(mThread):
        threads.append(MultiThreadTest1(N/mThread))
    
    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print "%d threads cost time %f " %(mThread, time.time()-timeElapsed)


def test2(mThread, N):

    timeElapsed = time.time()

    threads = []
    threads.append(MultiThreadTest1(N/mThread))
    threads.append(MultiThreadTest2(N/mThread))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print "%d threads cost time %f " %(mThread, time.time()-timeElapsed)

if __name__ == "__main__":

    mThreadList = [1, 2, 3, 4, 6, 8] 
    N = 10000000

    for mThread in mThreadList:
        test(mThread, N)


    test2(2, N)



