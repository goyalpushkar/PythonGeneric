'''
Created on Feb 18, 2020

@author: goyalpushkar
'''

class quickFind:

    def __init__(self, lastelement):
        self.arrayOfObjects = {key for key in range(lastelement)}
        self.count = lastelement

    def insertValue(self, value):
        self.arrayOfObjects[value] = value

    def isLinked(self, object1, object2):
        return findObject[object1] == findObject[object2]

    def checkCount(self):
        return count

    def findObject(self,object):
        return self.arrayOfObjects[object]

    def unionObjects(self, object1, object2):
        objectValue1 = findObject[object1]
        objectValue2 = findObject[object2]

        if objectValue1 == objectValue2:
            return

        for objects in arrayOfObjects:
            if self.arrayOfObjects[objects] == objectValue1:
                self.arrayOfObjects[objects] == objectValue2

        count -= 1

class quickUnion:

    def __init__(self, lastelement):
        self.arrayOfObjects = {key for key in range(lastelement)}
        self.count = lastelement

    def insertValue(self, value):
        self.arrayOfObjects[value] = value

    def isLinked(self, object1, object2):
        return findObject[object1] == findObject[object2]

    def checkCount(self):
        return count

    def findObject(self, object):
        while self.arrayOfObjects[object] != object:
            object = arrayOfObjects[object]

        return object

    def unionObjects(self, object1, object2):
        objectValue1 = findObject[object1]
        objectValue2 = findObject[object2]

        if objectValue1 == objectValue2:
            return

        self.arrayOfObjects[objectValue1] = objectValue2
        count -= 1

class weightedQuickUnion:

    def __init__(self, lastelement):
        arrayOfObjects = {key for key in range(lastelement)}
        sizeOfObjects = {1 for key in range(lastelement)}
        count = lastelement

    def insertValue(self, value):
        arrayOfObjects[value] = value

    def isLinked(self, object1, object2):
        return findObject[object1] == findObject[object2]

    def checkCount(self):
        return count

    def findObject(self, object):
        while arrayOfObjects[object] != object:
            object = arrayOfObjects[object]

        return object

    def unionObjects(self, object1, object2):
        objectValue1 = findObject[object1]
        objectValue2 = findObject[object2]

        if objectValue1 == objectValue2:
            return

        if sizeOfObjects[objectValue1] < sizeOfObjects[objectValue2]:
           arrayOfObjects[objectValue1] = objectValue2
           sizeOfObjects[objectValue2] += sizeOfObjects[objectValue1]
        else:
            arrayOfObjects[objectValue2] = objectValue1
            sizeOfObjects[objectValue1] += sizeOfObjects[objectValue2]

        count -= 1


class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''