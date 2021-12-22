
'''
Maximum Xor
You are given an array of elements. A list of integers, maximum value of \text{each} arr[i] 0 \le i < n elements.
Note that there are multiple test cases in one input file. For example:

For example:

Function Description
Complete the maxXor function in the editor below. It must return an array of integers, each representing
the maximum xor value for each element against all elements of maxXor has the following parameter(s):
arr: an array of integers
q: an array of integers to query

Input Format
The first line contains an integer n, the size of the array arr.
The second line contains n space-separated integers, arr[i] from 0 ≤ i < n
The third line contain m, the size of the array queries.
Each of the next m lines contains an integer queries[j] where 0 ≤ j < m

Constraints
1 ≤ n, m ≤ 10^5
0 ≤ arr[i], q[i] ≤ 10^9

Output Format
The output should contain m lines with each line representing output for the corresponding input of the testcase.


Input 0
3
012
3
3
7
2

Sample Output 0
3
7
3

Sample Input 1
5
51743
2
2
0
Sample Output 1
7
7

Sample Input 2
4
1357
2
17
6

Sample Output 2
22
7

'''
import math
import os
import random
import re
import sys

def convertToBinary( number ):
    quotient = number
    binaryString = ""

    if number == 0:
        binaryString = "0"

    while quotient > 0:
        binaryString = str( quotient % 2 ) + binaryString
        quotient //= 2

    return binaryString

def convertToDecimal( binaryString ):
    value = 0
    index = 0
    for elem in range(len(binaryString)-1, -1, -1):
        value += int(binaryString[index]) * pow(2, elem)
        index += 1

    return value

def doXor( binaryString1, binaryString2 ):
    newbinaryString1 = ""
    newbinaryString2 = ""
    xorBinaryString = ""
    #Append Zeroes to shorter binary string
    if len(binaryString1) >= len(binaryString2):
       for index in range( len(binaryString1) - len(binaryString2) ):
           newbinaryString2 += "0"
       newbinaryString2 += binaryString2
       newbinaryString1 = binaryString1
    else:
        for index in range(len(binaryString2) - len(binaryString1)):
            newbinaryString1 += "0"
        newbinaryString1 += binaryString1
        newbinaryString2 = binaryString2

    #print( newbinaryString1 + " XOR " + newbinaryString2)
    #Generate XOR binary String
    for index in range(len(newbinaryString1)):
        if newbinaryString1[index] == newbinaryString2[index]:
            xorBinaryString += "0"
        else:
            xorBinaryString += "1"

    return xorBinaryString

# Complete the maxXor function below.
def maxXorTimeOuts(arr, queries):
    returnArray = []

    # solve here
    for queryIndex in range(len(queries)):
        maxValue = 0
        #print("\n")
        #print("Query Value - " + str(queries[queryIndex]))
        queryBinary = convertToBinary(queries[queryIndex])
        #print("Binary Conversion Query - " + queryBinary)
        for arrIndex in range(len(arr)):
            #print("\n")
            #print("Array Value - " + str(arr[arrIndex]))
            arrBinary = convertToBinary(arr[arrIndex])
            #print("Binary Conversion Array - " + arrBinary)
            xorBinary = doXor(queryBinary, arrBinary)
            #print("Binary XOR - " + xorBinary)
            xorDecimal = convertToDecimal(xorBinary)
            #print("Decimal - " + str(xorDecimal) )
            if maxValue < xorDecimal:
                maxValue = xorDecimal

        #print("Max Value - " + str(maxValue))
        returnArray.append(maxValue)

    return returnArray

def convertToBinaryBuiltIn( number, maxlength ):
    return '{:b}'.format(number).zfill(maxlength)

def convertToDecimalBuiltIn( binaryString ):
    return int(binaryString, 2)

def binaryTree():  #value
    return {}  #[[],[]]  # Value and Children

def insertChild(root, value):
    newRoot = root
    #print(newRoot)
    '''
    #If passed value is 0 and exists in index 0 then set newRoot as index 0
    if len(newRoot) > 0:
        if value == newRoot[0]:
            newRoot = newRoot[0]
        # If passed value is 1 and exists in index 1 then set newRoot as index 1
        elif value == newRoot[1]:
            newRoot = newRoot[1]
        # if passed value does not exists in the index 1 or 2 means no child exists
    else:
    '''
    newNode = [] #[int(value), []]
    # If passed value is 0 then insert new node into index 0
    if value == '0':
        #newNode = [int(value), []]
        newRoot[[]]
    # If passed value is 1 then insert new node into index 1
    else:
        newNode = [[], int(value)]

    newRoot.append(newNode)
    newRoot = newNode

    # Return current node
    return newRoot

# Complete the maxXor function below.
def maxXor(arr, queries):
    returnArray = []
    root = binaryTree()

    #Find Binary length of maximum integer in the 2 arrays
    #this will be used to fill shorter lengths with number of zeroes
    maxLength = len('{:b}'.format(max(arr+queries)))

    for arrIndex in range(len(arr)):
        binaryValue = convertToBinaryBuiltIn(arr[arrIndex], maxLength)
        print("Binary Value for " + str(arr[arrIndex]) + " - " + binaryValue )
        startNode = root
        #Start loop for each bit in the binaryValue to insert into Tree
        for char in binaryValue:
            if char not in startNode:
                startNode[char] = {}

            startNode = startNode[char]

            #startNode = insertChild(startNode, char)

    print(root)
    for queryIndex in range(len(queries)):
        binaryValue = convertToBinaryBuiltIn(queries[queryIndex], maxLength)
        print("Binary Value for " + str(queries[queryIndex]) + " - " + binaryValue)
        startNode = root
        xoredAvailableValue = ''
        for char in binaryValue:
            xoredValue = str(int(char) ^ 1)
            if xoredValue in startNode:
               xoredAvailableValue += str(int(xoredValue) ^ int(char))#+ xoredAvailableValue
               startNode = startNode[xoredValue]
            else:  #if xoredValue == startNode[1]:
               xoredAvailableValue += str(int(char) ^ int(char)) #+ xoredAvailableValue
               startNode = startNode[char]

        print(xoredAvailableValue)
        maxDecimalValue = convertToDecimalBuiltIn(xoredAvailableValue)
        print(maxDecimalValue)
        returnArray.append(maxDecimalValue)

    return returnArray

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input("No of Array Elements: "))
    arr = list(map(int, input().rstrip().split()))

    m = int(input("No of Query Elements: "))
    queries = []

    for _ in range(m):
        queries_item = int(input())
        queries.append(queries_item)

    result = maxXor(arr, queries)
    print(('\n'.join(map(str, result))))
    print("\n")

    '''
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
    '''