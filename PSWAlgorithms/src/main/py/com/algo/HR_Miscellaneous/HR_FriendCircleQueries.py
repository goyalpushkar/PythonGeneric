import math
import os
import random
import re
import sys
from collections import Set

'''
The population of HackerWorld is . Initially, none of the people are friends with each other. In order to
start a friendship, two persons a and b have to shake hands, where . The friendship
relation is transitive, that is if a and b shake hands with each other, a and friends of a become friends with
b and friends of b.
You will be given queries. After every query, you need to report the size of the largest friend circle (the
largest group of friends) formed after considering that query.
For example, your list of queries is:
1 2
3 4
2 3
First, and shake hands, forming a circle of . Next, and do the same. Now there are two groups of
friends. When and become friends in the next query, both groups of friends are added together to
make a circle of friends. We would print
2
2
4
Function Description
Complete the function maxCircle in the editor below. It must return an array of integers representing the
size of the maximum circle of friends after each query.
maxCircle has the following parameter(s):
queries: an array of integer arrays, each with two elements indicating a new friendship
Input Format
You need to complete the function, which takes 2-D integer array of size . After each
query, person and become friends.
Codestub input format:
First line consist of an integer which denotes the number of queries to process.
Each of the next lines consists of two integers denoting the 2-D array .
Constraints
for
Output Format
Return an integer array of size , whose value at index is the size of largest group present after
processing till query.

'''


# Complete the maxCircle function below.
def maxCircleTimeOutsOneWrong(queries):
    mainarray = []
    allofFriendsarray = []  # Just for verification
    maxSize = 2

    for index in range(len(queries)):
        setofelements = {queries[index][0], queries[index][1]}

        # print(setofelements)
        for checkIndex in range(index - 1, -1, -1):
            if setofelements.__contains__(queries[checkIndex][0]) or setofelements.__contains__(queries[checkIndex][1]):
                setofelements.add(queries[checkIndex][0])
                setofelements.add(queries[checkIndex][1])
                for newsearchindex in range(checkIndex + 1, index, 1):
                    if setofelements.__contains__(queries[newsearchindex][0]) or setofelements.__contains__(
                            queries[newsearchindex][1]):
                        setofelements.add(queries[newsearchindex][0])
                        setofelements.add(queries[newsearchindex][1])

        allofFriendsarray.append(setofelements)
        if len(setofelements) > maxSize:
            maxSize = len(setofelements)
            mainarray.append(len(setofelements))
        else:
            mainarray.append(maxSize)

    print('\n'.join(map(str, allofFriendsarray)))
    return mainarray


# Complete the maxCircle function below.
def maxCircleTimeOuts(queries):
    mainarray = []
    allofFriendsarray = []  # Just for verification
    maxFriends = 2
    for index in range(len(queries)):
        setofelements = {queries[index][0], queries[index][1]}

        allofFriendsarray.append(setofelements)
        # print("start")
        # print('\n'.join(map(str, allofFriendsarray)))
        # print(setofelements)
        # n = len(allofFriendsarray)
        start = len(allofFriendsarray) - 1
        mergedIndex = -1

        # while (n>=0):
        #   start = n
        # print(start)
        for internalindex in range(start - 1, -1, -1):
            '''
            if allofFriendsarray[index].__contains__(setofelements[0]) and not allofFriendsarray[index].__contains__(setofelements[1]):
                allofFriendsarray[index].add(setofelements[0])
                allofFriendsarray[index].add(setofelements[1])
                #del setofelements[0]
            elif allofFriendsarray[index].__contains__(setofelements[1]) and not allofFriendsarray[index].__contains__(setofelements[0]):
                allofFriendsarray[index].add(setofelements[0])
                allofFriendsarray[index].add(setofelements[1])
                #del setofelements[1]
            el'''

            if len(allofFriendsarray[internalindex]) > 0:
                if allofFriendsarray[internalindex].__contains__(queries[index][0]) or allofFriendsarray[
                    internalindex].__contains__(queries[index][1]):
                    # print(internalindex)
                    allofFriendsarray[internalindex].add(queries[index][0])
                    allofFriendsarray[internalindex].add(queries[index][1])
                    # print(allofFriendsarray[internalindex])
                    # print(mergedIndex)
                    if mergedIndex != -1:
                        allofFriendsarray[internalindex] = allofFriendsarray[internalindex].union(
                            allofFriendsarray[mergedIndex])
                        # print(allofFriendsarray[internalindex])
                        del allofFriendsarray[mergedIndex]

                    mergedIndex = internalindex
                    # del setofelements[0]
                    # del setofelements[1]
                    # return

                    # print("internalindex")
                    # print('\n'.join(map(str, allofFriendsarray)))
                    if maxFriends < len(allofFriendsarray[internalindex]):
                        maxFriends = len(allofFriendsarray[internalindex])

        if mergedIndex != -1:
            del allofFriendsarray[len(allofFriendsarray) - 1]

        # print("end")
        # print("\n")
        # print('\n'.join(map(str, allofFriendsarray)))
        mainarray.append(maxFriends)

    return mainarray


class classUnionFind(object):

    def __init__(self):
        self.arrayOfObjects = {0: 0}
        self.sizeOfObjects = {0: 0}
        self.count = 0
        self.maxSize = 0

    def insertElement(self, value):
        # print(value)
        '''
        if self.arrayOfObjects[value]:
            print("Value not found")
            self.count += 1
        else:
            print("Value found")
'       '''
        self.arrayOfObjects[value] = self.arrayOfObjects.get(value, value)
        self.sizeOfObjects[value] = self.sizeOfObjects.get(value, 1)
        self.count += 1

    def isLinked(self, object1, object2):
        return self.findObject(object1) == self.findObject(object2)

    def checkCount(self):
        return self.count

    def findObject(self, object):
        while self.arrayOfObjects[object] != object:
            object = self.arrayOfObjects[object]

        return object

    def unionObjects(self, object1, object2):
        objectValue1 = self.findObject(object1)
        objectValue2 = self.findObject(object2)

        #print("Objects - " + str(object1) + "-" + str(object2))
        #print("Object Values - " + str(objectValue1) + "-" + str(objectValue2))
        if objectValue1 == objectValue2:
            return

        if self.sizeOfObjects[objectValue1] < self.sizeOfObjects[objectValue2]:
            #print("if")
            #print(str(self.sizeOfObjects[objectValue2]) + "-" + str(self.sizeOfObjects[objectValue1]))
            self.arrayOfObjects[objectValue1] = objectValue2
            self.sizeOfObjects[objectValue2] += self.sizeOfObjects[objectValue1]
            if self.maxSize < self.sizeOfObjects[objectValue2]:
                self.maxSize = self.sizeOfObjects[objectValue2]
        else:
            #print("else")
            #print(str(self.sizeOfObjects[objectValue1]) + "-" + str(self.sizeOfObjects[objectValue2]))
            self.arrayOfObjects[objectValue2] = objectValue1
            self.sizeOfObjects[objectValue1] += self.sizeOfObjects[objectValue2]
            if self.maxSize < self.sizeOfObjects[objectValue1]:
                self.maxSize = self.sizeOfObjects[objectValue1]

        self.count -= 1


def maxCircle(queriesp):
    mainarray = []
    unionFindObject = classUnionFind()
    for index in range(len(queriesp)):
        unionFindObject.insertElement(queriesp[index][0])
        unionFindObject.insertElement(queriesp[index][1])

        '''
        print("\n")
        print("ArrayOfObjects Array - " + str(index))
        print('\n'.join(map(str, unionFindObject.arrayOfObjects.items())))
        print("SizeOfObjects Array - " + str(index))
        print('\n'.join(map(str, unionFindObject.sizeOfObjects.items())))
        print("Max Size - " + str(unionFindObject.maxSize))
        '''
        unionFindObject.unionObjects(queriesp[index][0], queriesp[index][1])

        mainarray.append(unionFindObject.maxSize)

        print("ArrayOfObjects Array")
        print('\n'.join(map(str, unionFindObject.arrayOfObjects.items())))
        print("SizeOfObjects Array")
        print('\n'.join(map(str, unionFindObject.sizeOfObjects.items())))
        print("Counts - " + str(unionFindObject.count))
        print("\n")

    return mainarray


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input("No of queries: "))
    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = maxCircle(queries)

    print('\n'.join(map(str, ans)))
    print('\n')
    # fptr.write('\n'.join(map(str, ans)))
    # fptr.write('\n')

    # fptr.close()
