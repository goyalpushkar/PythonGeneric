'''
if __name__ == '__main__':
    print({__name__}, {__file__}, {repr(__package__)})
    # print(SS.__path__)
    # print( path.dirname(path.abspath(__file__) ) )
    # print( sys.path )
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    import DS.DS_Stack.Stack
    # print( path.dirname( path.dirname(path.abspath(__file__)) ) )
'''

'''
Special String Again
A string is said to be a special string if either of two conditions is met: All of the characters are the same, e.g. aaa .
All characters except the middle one are the same, e.g. aadaa .
A special substring is any substring of a string which meets one of those criteria. Given a string, determine how many special substrings can be formed from it.
For example, given the string , we have the following special substrings: .
Function Description
Complete the substrCount function in the editor below. It should return an integer representing the number of special substrings that can be formed from the given string.
substrCount has the following parameter(s): n: an integer, the length of string s
s: a string
Input Format
The first line contains an integer, , the length of . The second line contains the string .
Constraints
Each character of the string is a lowercase alphabet, .
Output Format
Print a single line containing the count of total special substrings.
Sample Input 0
Sample Output 0
Explanation 0
 
 5 asasd
 7
The special palindromic substrings of are

Sample Input 1
Sample Output 1
Explanation 1
The special palindromic substrings of

Sample Input 2
Sample Output 2
Explanation 2
The special palindromic substrings of
are
 7 abcbaba
 10
 4 aaaa
 10
are
'''

import math
import os
import random
import re
import sys
from os import path
#from DS_Stack import Stack
from collections import deque

from src.main.py.com.algo.DS.DS_Stack import Stack

# Complete the substrCount function below.
def substrCountN2(n, s):
    count = n
    similarChars = {}
    stackSubStr = Stack()
    for index in range(len(s)):
        sstring = s[index]
        if stackSubStr.is_empty():  # .__len__() == 0: #stackSubStr.isEmpty():
            stackSubStr.push(sstring)  # append(sstring)    #
        else:
            if sstring == stackSubStr.peek():
                stackSubStr.push( sstring )
            else:
                numOfElem = stackSubStr.size()
                count += ( numOfElem * (numOfElem - 1 ) ) / 2
                stackSubStr = Stack()

    numOfElem = stackSubStr.size()
    count += (numOfElem * (numOfElem - 1)) / 2

    print(count)
    for index in range(len(s)):
        popFromStack = 0
        stackSubStr = Stack() #deque() #DS.Stack()
        for jindex in range(index, len(s)):
            #print(count)
            sstring = s[jindex]
            if stackSubStr.is_empty():   #.__len__() == 0: #stackSubStr.isEmpty():
               stackSubStr.push(sstring)  #append(sstring)    #
            else:
                if sstring == stackSubStr.peek():  #pop:   #.
                    if popFromStack == 1:
                        stackSubStr.pop()

                        if stackSubStr.is_empty():
                            count += 1
                            break
                    else:
                        stackSubStr.push(sstring)
                else:
                    if popFromStack == 1:
                        stackSubStr = Stack() #deque() #DS.Stack()
                        break
                    else:
                        popFromStack = 1

                        if stackSubStr.is_empty():   #.__len__(): #stackSubStr.isEmpty():
                            count += 1
                            break
    return int(count)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    noOfTests = int(input("No of test case - "))
    for i in range(noOfTests):
        print("Enter input - ")
        n = int(input())
        s = input()

        result = substrCountN2(n, s)

        print( 'Answer - ' + str(result))
    #fptr.write(str(result) + '\n')
    #fptr.close()
