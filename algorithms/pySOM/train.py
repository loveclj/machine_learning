#!/usr/bin/env python
# coding=utf-8
import numpy as np
import sys
import time
#import profile

def  initCodeBook(SOM_X, SOM_Y, dimension):
    codeBook = np.random.random(SOM_X * SOM_Y * dimension).reshape(SOM_X, SOM_Y, dimension)
    return codeBook

def  generateFeature(dimension, nSamples):
    feature  = np.random.random(dimension * nSamples).reshape(nSamples, dimension)
    return feature
    

class Train():
    def __init__(self, SOM_X, SOM_Y, dimension, learnRate, totalEpoch):
        self.SOM_X = SOM_X
        self.SOM_Y = SOM_Y
        self.dimension = dimension
        self.learnRate = learnRate
        self.totalEpoch = totalEpoch
        self.R          = 0
        self.codeBook   = initCodeBook(self.SOM_X, self.SOM_Y, self.dimension)
        self.den = np.array(np.zeros([self.SOM_X, self.SOM_Y]))
        self.num = np.array(np.zeros([self.SOM_X, self.SOM_Y, self.dimension]))
        

    def setFeature(self, feature, numSampes):
        self.feature = feature
        self.numSamples = numSampes

    def train(self):
        for epoch in xrange(self.totalEpoch):
            epoch += 1
            self.R  = (self.SOM_X/2.0)*np.exp(-10.0*(epoch - 1)*(epoch - 1)/(epoch*epoch))
            self.trainOneEpoch()
            self.updateCodeBook()
            print epoch


    def getBMU(self, n):
        bmu = [0, 0]
        min = sys.float_info.max
        for somx in xrange(self.SOM_X):
            for somy in xrange(self.SOM_Y):
                tmp =  np.linalg.norm(self.feature[n] - self.codeBook[somx][somy])
                if(tmp < min):
                   min =  tmp
                   bmu[0] = somx
                   bmu[0] = somy
        return bmu


    def updateCodeBook(self):
        for somx in xrange(self.SOM_X):
            for somy in xrange(self.SOM_Y):
                for d in xrange(self.dimension):
                    self.codeBook[somx][somy][d] = self.num[somx][somy][d]/self.den[somx][somy]


    def trainOneEpoch(self):
        for n in xrange(self.numSamples):
            bmu = self.getBMU(n)
            for  somx in xrange(self.SOM_X):
                for somy in xrange(self.SOM_Y):
                     deltax = somx - bmu[0]
                     deltay = somx - bmu[1]
                     dist   = 1.0* (deltax * deltax + deltay * deltay)
                     neigorFactor = np.exp(-1.0 * dist/(self.R * self.R));
#                     neigorFactor = 1.0 #np.exp(-1.0 * dist/(self.R * self.R));

                     #offset = (somx * self.SOM_Y +somy)* dimension
                     for d in xrange(self.dimension):
                         self.num[somx][somy][d] +=  neigorFactor * self.feature[n][d]
                     self.den[somx][somy]  += neigorFactor
                    







if  "__main__" == __name__:
    print "som train"
    SOM_X = 10
    SOM_Y = 10
    dimension = 1000
    totalEpoch = 10

    train = Train(SOM_X,SOM_Y,dimension, 0.1, totalEpoch)
    codeBook =  initCodeBook(SOM_X,SOM_Y,dimension)

#    print train.codeBook
    nSamples  = 10
    feature   =  generateFeature(dimension, nSamples)
    train.setFeature(feature, nSamples)
    #print train.feature 
    t =  time.time()
    train.train()
    #profile.run("train.train()")
    print time.time() - t

