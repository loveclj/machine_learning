#!/usr/bin/env python
# coding=utf-8
import sys
import time
import random
import profile
import math

def  initCodeBook(SOM_X, SOM_Y, dimension):
    codeBook = []
    len = SOM_X * SOM_Y *dimension
    i = 0
    while i < len:
        codeBook.append(random.random())
        i += 1
    return codeBook

def  generateFeature(dimension, nSamples):
    feature = []
    len = dimension * nSamples
    i = 0
    while i < len:
        feature.append(random.random())
        i += 1
#    feature  = np.random.random(dimension * nSamples).reshape(nSamples, dimension)
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
        self.den = [0.0]*(self.SOM_X * self.SOM_Y)
        self.num = [0.0]*(self.SOM_X * self.SOM_Y * dimension)
        

    def setFeature(self, feature, numSampes):
        self.feature = feature
        self.numSamples = numSampes

    def train(self):
        for epoch in xrange(self.totalEpoch):
            epoch += 1
            self.R  = (self.SOM_X/2.0)*math.exp(-10.0*(epoch - 1)*(epoch - 1)/(epoch*epoch))
            self.trainOneEpoch()
            self.updateCodeBook()


    def getBMU(self, n):
        bmu = [0, 0]
        min = sys.float_info.max
        offset_feature = n * self.dimension
        for somx in xrange(self.SOM_X):
            for somy in xrange(self.SOM_Y):
                dist = 0.0
                offset_codebook =  (somx * self.SOM_Y + somy)*self.dimension
                for d in xrange(self.dimension):
                    tmp =  self.feature[offset_feature + d] - self.codeBook[offset_codebook + d]
                    dist += tmp *tmp
                    if(tmp < min):
                        min =  tmp
                        bmu[0] = somx
                        bmu[0] = somy
        return bmu


    def updateCodeBook(self):
        for somx in xrange(self.SOM_X):
            for somy in xrange(self.SOM_Y):
                offset =  (somx * self.SOM_Y + somy)*self.dimension
                offset_den =  somx * self.SOM_Y + somy#*self.dimension
                for d in xrange(self.dimension):
                    self.codeBook[offset + d] = self.num[offset + d]/self.den[offset_den]


    def trainOneEpoch(self):
        for n in xrange(self.numSamples):
            bmu = self.getBMU(n)
            offset_feature = n * self.dimension
            for  somx in xrange(self.SOM_X):
                for somy in xrange(self.SOM_Y):
                     deltax = somx - bmu[0]
                     deltay = somx - bmu[1]
                     dist   = 1.0* (deltax * deltax + deltay * deltay)
                     neigorFactor = math.exp(-1.0 * dist/(self.R * self.R));
#                     neigorFactor = 1.0 #np.exp(-1.0 * dist/(self.R * self.R));

                     #offset = (somx * self.SOM_Y +somy)* dimension
                     offset_codebook =  (somx * self.SOM_Y + somy)*self.dimension
                     offset_den=  (somx * self.SOM_Y + somy)#*self.dimension
                     for d in xrange(self.dimension):
                         self.num[offset_codebook + d] +=  neigorFactor * self.feature[offset_feature + d]
                     self.den[offset_den]  += neigorFactor
                    







if  "__main__" == __name__:
    print "som train"
    SOM_X = 10
    SOM_Y = 10
    dimension = 1000
    totalEpoch = 10

    train = Train(SOM_X,SOM_Y,dimension, 0.1, totalEpoch)

    codeBook =  initCodeBook(SOM_X,SOM_Y,dimension)

#    print train.codeBook
    nSamples  = 100
    feature   =  generateFeature(dimension, nSamples)
    train.setFeature(feature, nSamples)
    #print train.feature 
    t =  time.time()
#    profile.run("train.train()")
    train.train()
    print time.time() - t

