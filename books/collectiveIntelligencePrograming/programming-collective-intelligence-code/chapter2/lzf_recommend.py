#!/usr/bin/env python
# coding=utf-8
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0, 
 'You, Me and Dupree': 3.5}, 
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0, 
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0}, 
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}


for person, movieAndScore in critics.items():
    print  person
    for movie,score in movieAndScore.items():
        print movie +" : ",
        print score
    print "--------------------"

def extractFeature(rawDictData):
    features =[]
    for person, movieAndScore in critics.items():
        oneFeature =[]
        for movie, score in  movieAndScore.items():
            oneFeature.append(score)
        features.append(oneFeature)
    return features

def printMatrix(matrix):
    for vector in matrix:
        str = ""
        for v in vector:
           str += "%f " %(v)
        print str

features = extractFeature(critics)

def getSimilarities(rawDictData):
    distanceMatrix = []
    for person, movieAndScore in rawDictData.items():
        distanceVector = []
        for comparePerson, compareMovieAndScore in rawDictData.items():
            distance = 0
            for key, value in movieAndScore.items():
                if key in compareMovieAndScore.keys():
                    diff = value - compareMovieAndScore[key]
                    distance += diff * diff
            distanceVector.append(1/(distance+1))
        distanceMatrix.append(distanceVector)
    return distanceMatrix

distanceMatrix = getSimilarities(critics)
printMatrix(distanceMatrix)



