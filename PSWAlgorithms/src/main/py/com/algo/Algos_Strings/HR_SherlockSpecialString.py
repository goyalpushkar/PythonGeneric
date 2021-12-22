'''
Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just  character at  index in the string, and the remaining characters will occur the same number of times. Given a string , determine if it is valid. If so, return YES, otherwise return NO.

For example, if , it is a valid string because frequencies are . So is  because we can remove one  and have  of each character in the remaining string. If  however, the string is not valid as we can only remove  occurrence of . That would leave character frequencies of .

Function Description

Complete the isValid function in the editor below. It should return either the string YES or the string NO.

isValid has the following parameter(s):

s: a string
Input Format

A single string .

Constraints

Each character
Output Format

Print YES if string  is valid, otherwise, print NO.

Sample Input 0

aabbcd
Sample Output 0

NO
Explanation 0

Given , we would need to remove two characters, both c and d  aabb or a and b  abcd, to make it valid. We are limited to removing only one character, so  is invalid.

Sample Input 1

aabbccddeefghi
Sample Output 1

NO
Explanation 1

Frequency counts for the letters are as follows:

{'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'f': 1, 'g': 1, 'h': 1, 'i': 1}

There are two ways to make the valid string:

Remove  characters with a frequency of : .
Remove  characters of frequency : .
Neither of these is an option.

Sample Input 2

abcdefghhgfedecba
Sample Output 2

YES
Explanation 2

All characters occur twice except for  which occurs  times. We can delete one instance of  to have a valid string.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    if len(s) == 0:
        return "YES"

    char_count = {}
    for chr in s:
        char_count[chr] = char_count.get(chr, 0) + 1

    print(char_count)
    distinct_length_count = {}
    for chr in char_count.keys():
        distinct_length_count[char_count[chr]] = distinct_length_count.get(char_count[chr], 0) + 1

    print(distinct_length_count)
    if len(distinct_length_count.keys()) > 2:
        return "NO"
    elif len(distinct_length_count.keys()) == 1:
        return "YES"
    else: # 2
        first_key = 0
        first_value = 0
        second_key = 0
        second_value = 0
        first_time = "Y"
        for counts in distinct_length_count.keys():
            if first_time == "Y":
                first_key = counts
                first_value = distinct_length_count[counts]
            else:
                second_key = counts
                second_value = distinct_length_count[counts]

            first_time = "N"

        #abcdefghhgfedecba
        #aaaabbbbccccddddeeeeffffggg
        #if ( first_value == 1 and ( first_key - second_key == 1 or second_key - first_key == 1 or first_key == 1 ) ) or ( second_value == 1 and ( first_key - second_key == 1 or second_key - first_key == 1 or second_key == 1 ) ):
        if (first_value == 1 and (first_key - second_key == 1 or first_key == 1)) or (second_value == 1 and (second_key - first_key == 1 or second_key == 1)):
            return "YES"
        else:
            return "NO"


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    test_cases = int(input("No of test cases: "))
    for elem in range(test_cases):
        s = input("Enter String: ")
        result = isValid(s)
        print(result + '\n')
        #fptr.write(result + '\n')
        #fptr.close()
