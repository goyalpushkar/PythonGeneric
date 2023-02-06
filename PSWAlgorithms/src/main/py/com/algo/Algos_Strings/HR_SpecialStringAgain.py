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

# from src.main.py.com.algo.DS.DS_Stack import Stack

# Complete the substrCount function below.
class Solution:
    def substrCountN2(self, n, s):
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

    # 3/16 rest failing with - RecursionError: maximum recursion depth exceeded while calling a Python object
    def substrCount_rec(self, n, s):
        # All possible substrings are
        #   1. length of the string
        #   2. Find substring that satisfy the requirement

        # Need to write a method that takes start and end and return true if it is special

        def is_special(start, end):
            #  and start+1 != end-1 and start+1<end and s[start]==s[start+1] and end-1>start and s[end]==s[end-1]
            prev = s[start]
            while start < end:
                if s[start] == s[end] and s[start] == prev:
                    prev = s[start]
                    start += 1
                    end -= 1
                else:
                    return False

            return True

        def substr_helper(start, end, indent):
            key = str(start) + '_' + str(end)
            print(f"{' '*indent}key: {key} word: {s[start:end+1]}\t"
                  f"{check_dict}")

            if key in check_dict:
                return 0 #check_dict[key]

            if start >= end:
                check_dict[key] = 0
                return 0

            result = substr_helper(start + 1, end, indent+5) + substr_helper(start, end - 1, indent+5) + \
                     substr_helper(start+1, end - 1, indent+5)
            # 1 if is_special(start, end) else 0
            # 0 if str(start + 1) + '_' + str(end) in check_dict.keys() else substr_helper(start + 1, end) + \
            # 0 if str(start) + '_' + str(end-1) in check_dict.keys() else substr_helper(start, end - 1) + \
            # 0 if str(start + 1) + '_' + str(end-1) in check_dict.keys() else substr_helper(start + 1, end - 1)

            if is_special(start, end):
                print(f"{' '*indent}key: {key} word: {s[start:end+1]}")
                result += 1

            check_dict[key] = result
            print(f"{' '*indent} f result: {check_dict[key]}")

            return check_dict[key]

        check_dict = {}
        sys.setrecursionlimit(10 ** 6)
        all_subs = substr_helper(0, len(s)-1, 0)
        final_subs = all_subs + len(s)

        return final_subs

    # def substrCount_nonrec(self, n, s):
    #     # All possible substrings are
    #     #   1. length of the string
    #     #   2. Find substring that satisfy the requirement
    #
    #     # Need to write a method that takes start and end and return true if it is special
    #
    #     def is_special(start, end):
    #         #  and start+1 != end-1 and start+1<end and s[start]==s[start+1] and end-1>start and s[end]==s[end-1]
    #         key = str(start) + '_' + str(end)
    #         if key in check_dict:
    #             return check_dict[key]
    #
    #         prev = s[start]
    #         while start < end:
    #             if s[start] == s[end] and s[start] == prev:
    #                 prev = s[start]
    #                 start += 1
    #                 end -= 1
    #             else:
    #                 check_dict[key] = False
    #                 return False
    #
    #         check_dict[key] = True
    #         return True
    #
    #     start = 0
    #     end = len(s)-1
    #     check_dict = {}
    #     result = 0
    #     while start<end:
    #         key = str(start) + '_' + str(end)
    #         print(f"key: {key} word: {s[start:end+1]}\t"
    #               f"{check_dict}")
    #
    #         curr = 1 if is_special(start, end) else 0
    #         next = 1 if is_special(start+1, end) else 0
    #         prev = 1 if is_special(start, end-1) else 0
    #
    #         result += curr + next + prev
    #
    #         start += 1
    #         end -= 1
    #
    #
    #     final_subs = result + len(s)
    #
    #     return final_subs

    # Passed all test cases
    def substrCount(self, n, s):
        i = 0
        same_char_count = [0 for _ in range(n)]
        return_val = 0
        while i < n:
            j = i + 1
            c = 1
            while j < n and s[j] == s[i]:
                j += 1
                c += 1

            return_val += (c * (c+1))//2
            same_char_count[i] = c
            i = j

        # print(same_char_count, return_val)
        for j in range(1, n-1):
            # print(f"j: {j} {s[j]}")
            if s[j] == s[j-1]:
                same_char_count[j] = same_char_count[j-1]

            # odd length substr(s) which has middle element diiferent
            if s[j-1] == s[j+1] and s[j] != s[j-1]:
                # print(f"matched")
                return_val += min(same_char_count[j-1], same_char_count[j+1])

            # print(f"final val: {return_val}")

        # print(f"final val: {return_val}")
        return return_val



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    noOfTests = int(input("No of test case - "))
    for i in range(noOfTests):
        print("Enter input - ")
        n = int(input())
        s = input()
        sol = Solution()
        result = sol.substrCount(n, s)
        # substrCountN2

        print( 'Answer - ' + str(result))
    #fptr.write(str(result) + '\n')
    #fptr.close()
