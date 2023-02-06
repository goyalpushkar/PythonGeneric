'''
Alice is taking a cryptography class and finding anagrams to be very useful. We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

Alice decides on an encryption scheme involving two large strings where encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. Can you help her find this number?

Given two strings,  and , that may or may not be of the same length, determine the minimum number of character deletions required to make  and  anagrams. Any characters can be deleted from either of the strings.

For example, if  and , we can delete  from string  and  from string  so that both remaining strings are  and  which are anagrams.

Function Description

Complete the makeAnagram function in the editor below. It must return an integer representing the minimum total characters that must be deleted to make the strings anagrams.

makeAnagram has the following parameter(s):

a: a string
b: a string
Input Format

The first line contains a single string, .
The second line contains a single string, .

Constraints

The strings  and  consist of lowercase English alphabetic letters ascii[a-z].
Output Format

Print a single integer denoting the number of characters you must delete to make the two strings anagrams of each other.

Sample Input

cde
abc
Sample Output

4
Explanation

We delete the following characters from our two strings to turn them into anagrams of each other:

Remove d and e from cde to get c.
Remove a and b from abc to get c.
We must delete  characters to make both strings anagrams, so we print  on a new line.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram_old(a, b):
    elem_dict = {}
    for elem in a:
        elem_dict[elem] = (elem_dict.get(elem, (0,0))[0] + 1, 1)

    print(elem_dict)
    for elem in b:
        if elem_dict.get(elem, (0,0))[0] > 0 and elem_dict.get(elem, (0,0))[1] == 1:
            elem_dict[elem] = (elem_dict.get(elem, (0,0))[0] - 1, 1)
        else:
            elem_dict[elem] = (elem_dict.get(elem, (0,0))[0] + 1, 2)

    print(elem_dict)
    total_deletions = 0
    for value in elem_dict.values():
        total_deletions += value[0]

    return total_deletions

# 02/05/2023
def makeAnagram(a, b):
    # Write your code here
    a_chars = {}
    for index in range(len(a)):
        a_chars[a[index]] = a_chars.get(a[index], 0) + 1

    for index in range(len(b)):
        a_chars[b[index]] = a_chars.get(b[index], 0) - 1

    # print(a_chars)
    required_deletions = 0
    for elem in a_chars.keys():
        if a_chars[elem] != 0:
            required_deletions += abs(a_chars[elem])

    return required_deletions

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input("String1: ")
    b = input("String2: ")

    res = makeAnagram(a, b)
    print(str(res) + '\n')
    #fptr.write(str(res) + '\n')
    #fptr.close()
