#!/bin/python3
'''
Min Max Riddle
  Given an integer array of size The window size varies from
, find the maximum of the minimum(s) of every window size in the array. to .
For example, given
, consider window sizes of through . Windows of size are
. The maximum value of the minimum values of these windows is . Windows of
size are and their minima are . The maximum of these values is . Continue this process through window size to finally consider the entire array. All of the answers are
.
Function Description
Complete the riddle function in the editor below. It must return an array of integers representing the maximum minimum value for each window size from to .
riddle has the following parameter(s): arr: an array of integers
Input Format
The first line contains a single integer, , the size of .
The second line contains space-separated integers, each an .
Constraints
Output Format
Single line containing
Sample Input 0
4
2 6 1 12
Sample Output 0
12 2 1 1
Explanation 0
Here and
space-separated integers denoting the output for each window size from
to .
  window sizewindow1window2window3window4maximum of all windows 1 2 6 1 12 12 22112 3111 411
Sample Input 1
7
1 2 3 5 1 13 3

Sample Output 1
 13 3 2 1 1 1 1
Explanation 1
Here and
win sizew_1w_2w_3w_4w_5w_6w_7maximum of all windows
1 1235113313
2 123113 3
3 12111 2
411111 51111 6111 711
Sample Input 2
6 354762
Sample Output 2
764432
Explanation 2
Here and
win sizew_1w_2w_3w_4w_5w_6maximum of all windows 1 3547627
2 34462 6 334424 43424 5323 622
'''
import math
import os
import random
import re
import sys

# Complete the riddle function below.
def riddleTimeOut(arr):
    # complete this function
    min_max_arr = []

    for windowSize in range(1, len(arr)+1):
        min_arr = []
        for index in range(0, len(arr)-windowSize+1):
            minimum_elem = arr[index]
            for elem in range(1, windowSize):
                if minimum_elem > arr[index+elem]:
                    minimum_elem = arr[index+elem]

            #print("min - " + str(minimum_elem))
            min_arr.append(minimum_elem)

        maximum_elem = max(min_arr)
        #print("Max - " + str(maximum_elem))
        min_max_arr.append(maximum_elem)

    return min_max_arr

def riddle(arr):
    # complete this function
    elementMinWindowSize = {}
    for index in range(0, len(arr)):
        windowSize = 1
        for moveforward in range(index+1, len(arr)):
            if arr[index] <= arr[moveforward]:
                windowSize += 1
            else:
                break

        for movebackward in range(index-1, -1, -1):
            if arr[index] <= arr[movebackward]:
                windowSize += 1
            else:
                break

        if arr[index] in elementMinWindowSize:
            if elementMinWindowSize[arr[index]] < windowSize:
                elementMinWindowSize[arr[index]] = windowSize
        else:
            elementMinWindowSize[arr[index]] = windowSize

    print(elementMinWindowSize)
    windowsMaxElement = {}
    for elem in elementMinWindowSize:
        if elementMinWindowSize[elem] in windowsMaxElement:
            if windowsMaxElement[elementMinWindowSize[elem]] < elem:
                windowsMaxElement[elementMinWindowSize[elem]] = elem
        else:
            windowsMaxElement[elementMinWindowSize[elem]] = elem

    print(windowsMaxElement)
    maxArray = [i for i in range(len(arr))]
    for windows in range(len(arr), 0, -1):
        #print(len(arr)-windows)
        if windows in windowsMaxElement:
            maxArray[len(arr)-windows] = windowsMaxElement[windows]
            #maxArray.append(windowsMaxElement[windows])
        else:
            maxArray[len(arr) - windows] = maxArray[len(arr)-windows-1]
            '''
            for prevWindow in range(windows+1, len(arr) + 1):
                if len(arr)-prevWindow < len(maxArray):
                    maxArray[len(arr) - windows] = maxArray[len(arr)-prevWindow]
                    break

                if prevWindow in windowsMaxElement:
                    maxArray[len(arr)-windows] = windowsMaxElement[prevWindow]
                    break
                    #maxArray.append(windowsMaxElement[prevWindow])
            '''
    print(maxArray)
    maxArray.reverse()
    #print(maxArray)
    #reversedArr = list(reversed(maxArray))
    #print(reversedArr)
    return maxArray #list(reversed(maxArray))
        #maxArray.reverse()

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input("No of Integers: "))

    arr = list(map(int, input().rstrip().split()))

    res = riddle(arr)

    print(' '.join(map(str, res)))
    #fptr.write(' '.join(map(str, res)))
    #fptr.write('\n')
    #fptr.close()
