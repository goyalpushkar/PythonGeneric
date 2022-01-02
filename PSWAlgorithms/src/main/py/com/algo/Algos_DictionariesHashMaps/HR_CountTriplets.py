'''
You are given an array and you need to find number of tripets of indices  such that the elements at those indices are in geometric progression for a given common ratio  and .
For example, . If , we have  and  at indices  and .
Function Description
Complete the countTriplets function in the editor below. It should return the number of triplets forming a geometric progression for a given  as an integer.
countTriplets has the following parameter(s):
arr: an array of integers
r: an integer, the common ratio
Input Format
The first line contains two space-separated integers  and , the size of  and the common ratio.
The next line contains  space-seperated integers .
Constraints



Output Format
Return the count of triplets that form a geometric progression.
Sample Input 0
4 2
1 2 2 4
Sample Output 0
2
Explanation 0
There are  triplets in satisfying our criteria, whose indices are  and
Sample Input 1
6 3
1 3 9 9 27 81
Sample Output 1
6
Explanation 1
The triplets satisfying are index , , , ,  and .
Sample Input 2
5 5
1 5 5 25 125
Sample Output 2
4
Explanation 2
The triplets satisfying are index , , , .
'''
import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTripletsN2(arr, r):
    elemCounts = {}
    totalCount = 0

    for elem in arr:
        #if elem / r > 0 and elem % r == 0:
        #    elemCounts[elem//r] = elemCounts.get(elem//r, 0) + 1
        elemCounts[elem] = elemCounts.get(elem, 0 ) + 1

    print(elemCounts)
    for first_index in range(len(arr)-1, -1, -1):
        #print(totalCount)
        for second_index in range(first_index-1, 0, -1):
            if arr[first_index] / arr[second_index] == r:
                if arr[second_index] // r in elemCounts:
                    totalCount += elemCounts[arr[second_index] // r]
            else:
                continue

    return totalCount

#these 2 are same

def countTripletsN2TimeOut_WrongAnswer(arr, r):

    totalCount = 0
    for elem in range(len(arr)-1,1,-1):
        for secElem in range( elem-1, 0, -1 ):
            #print( str(elem) + " " + str(secElem) )
            ratio = arr[elem] / arr[secElem]
            if ratio == r:
                secondRatio = arr[secElem] / r
                totalCount = totalCount + arr.count(secondRatio)
            else:
                continue

    return totalCount

def countTriplets2NTimeOut_WrongAnswer(arr, r):
    elemCounts = dict()
    totalCount = 0

    elemCounts[arr[0]] = arr.count(arr[0])
    for elem in arr:
        productRatio = elem * r
        countInArr = arr.count(productRatio)
        elemCounts.__setitem__(productRatio, countInArr)

    print(elemCounts)
    for elems in elemCounts:
        secondElem = elems * r
        thirdElem = secondElem * r
        firstElemCount =  int( elemCounts.get(elems, 0) )
        secondElemCount = int( elemCounts.get(secondElem,0) )
        thirdElemCount = int( elemCounts.get(thirdElem,0) )
        totalCount = totalCount + (firstElemCount * secondElemCount * thirdElemCount)

    return totalCount

def countTriplets(arr, r):
    pairs = {}   #store second and third elems pair
    elemCount = {}
    count = 0
    for elem in reversed(arr):
        secondElem = elem * r
        thirdElem = secondElem * r

        #elem is first elem in the triplet pair
        count = count + pairs.get((secondElem, thirdElem), 0)

        # elem is second elem in the triplet pair
        pairs[(elem, secondElem)] = pairs.get((elem, secondElem), 0) + elemCount.get(secondElem, 0)

        # elem is first elem in the triplet pair
        elemCount[elem] = elemCount.get(elem,0) + 1

    return count

    '''
    if elem * r in pairs:
        count += pairs[elem*r]
    if elem * r in elemCount:
        pairs[elem] = pairs[elem*r] + elemCount[i*r]
    '''


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nr = input("Array Size and GP: ").rstrip().split()
    n = int(nr[0])
    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    #ans = countTripletsN2TimeOut_WrongAnswer(arr, r)
    #ans = countTriplets2NTimeOut_WrongAnswer(arr, r)
    ans = countTripletsN2(arr, r)
    #ans = countTriplets(arr, r)
    print("Answer - " + str(ans))
    #fptr.write(str(ans) + '\n')
    # fptr.close()