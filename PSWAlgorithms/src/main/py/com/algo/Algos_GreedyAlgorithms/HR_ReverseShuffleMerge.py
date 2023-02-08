'''
Given a string s such that s E merge(reverse(A), shuffle(A)) for some string A, find the lexicographically smallest A.

For example, s=abab. We can split it into two strings of ab. The reverse is ba and we need to find a string to shuffle
 in to get abab. The middle two characters match our reverse string, leaving the a and b at the ends.
 Our shuffle string needs to be ab. Lexicographically ab < ba, so our answer is ab.

Function Description
Complete the reverseShuffleMerge function in the editor below. It must return the lexicographically smallest string
 fitting the criteria.
reverseShuffleMerge has the following parameter(s):

s: a string

Input Format
A single line containing the string s.

Constraints
 s contains only lower-case English letters, ascii[a-z]
 1 <|s| <= 10000

Output Format
Find and return the string which is the lexicographically smallest valid A.

Sample Input 0
eggegg
Sample Output 0
egg
Explanation 0
Split "eggegg" into strings of like character counts: "egg", "egg"
reverse("egg") = "gge"
shuffle("egg") can be "egg"
"eggegg" belongs to the merge of ("gge", "egg")
The merge is: e gge gg.
'egg' < 'gge'

Sample Input 1
abcdefgabcdefg
Sample Output 1
agfedcb
Explanation 1
Split the string into two strings with like characters: abcdefg and abcdefg.
Reverse abcdefg = gfedcba
Shuffle gfedcba can be bcdefga
Merge to a bcdefga abcdefg

Sample Input 2
aeiouuoiea
Sample Output 2
aeiou
Explanation 2
Split the string into groups of like characters: aeiou
Reverse aeiou = uoiea
These merge to aeiou uoiea

'''
import math
import os
import random
import re
import sys

#
# Complete the 'reverseShuffleMerge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
# https://www.youtube.com/watch?v=K4TIlM1c-w4


# All characters are duplicated in the string as reverse and shuffle are merged
# Better to use reverse engineering

from collections import deque

class Solution:
    def reverseShuffleMerge(self, s):
        # Write your code here
        unused = {}
        for elem in s:
            unused[elem] = unused.get(elem, 0) + 1

        required = {key: value//2 for key, value in unused.items()}
        used = {}
        string_deque = deque()
        # print(f"unused: {unused}\n"
        #       f"used: {used}\n"
        #       f"required: {required}")

        for index in range(len(s)-1,-1, -1):
            # if elem is not used and required enter into string deque
            # if curr element is smaller than previous element then remove all elements from the deque and insert
            # current element
            curr_elem = s[index]
            if required[curr_elem] - used.get(curr_elem, 0) > 0:
                while len(string_deque) > 0 and string_deque[len(string_deque)-1] > curr_elem and \
                        unused[string_deque[len(string_deque)-1]] > \
                        required[string_deque[len(string_deque)-1]]-used[string_deque[len(string_deque)-1]]:
                    removed_elem = string_deque.pop()
                    # unused[removed_elem] += 1
                    used[removed_elem] -= 1

                # print(f"Before Append: {string_deque}")
                string_deque.append(curr_elem)
                # print(f"After Append: {string_deque}")
                used[curr_elem] = used.get(curr_elem, 0) + 1
                # unused[curr_elem] -= 1  # = unused.get(curr_elem) - 1

            unused[curr_elem] -= 1

            # print(f"curr_elem: {curr_elem}\t left string: {s[:index]}\n"
            #       f"unused: {unused}\n"
            #       f"used: {used}\n"
            #       f"required: {required}\n"
            #       f"string_deque: {string_deque}\n\n")

        # aaaaabccigicgjihidfiejfijgidgbhhehgfhjgiibggjddjjd
        # same = "aaaaabccigicgjihidfiejfijgi"  gihd j
        # result: aaaaabccgicgihidfiejfijgibhehgfhjgiibggjddjjd	 {'a': 5, 'b': 3, 'c': 3, 'g': 7, 'i': 8, 'h': 4, 'd': 4, 'f': 3, 'e': 2, 'j': 6}
        # expect: aaaaabccigicgjihidfiejfijgidgbhhehgfhjgiibggjddjjd	 {'a': 5, 'b': 3, 'c': 3, 'i': 9, 'g': 8, 'j': 7, 'h': 5, 'd': 5, 'f': 3, 'e': 2}

        result = "".join(string_deque)
        result_res = {}
        for elem in result:
            result_res[elem] = result_res.get(elem, 0) + 1
        expect = "aaaaabccigicgjihidfiejfijgidgbhhehgfhjgiibggjddjjd"
        expect_res = {}
        for elem in expect:
            expect_res[elem] = expect_res.get(elem, 0) + 1
        print(#f"same:{same}\n"
              f"result: {result}\t {result_res}\n"
              f"expect: {expect}\t {expect_res}")
        return "".join(string_deque)
