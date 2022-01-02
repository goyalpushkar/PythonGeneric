'''
Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. Given a string, find the number of pairs of substrings of the string that are anagrams of each other.

For example , the list of all anagrammatic pairs is  at positions  respectively.

Function Description

Complete the function sherlockAndAnagrams in the editor below. It must return an integer that represents the number of anagrammatic pairs of substrings in .

sherlockAndAnagrams has the following parameter(s):

s: a string .
Input Format

The first line contains an integer , the number of queries.
Each of the next  lines contains a string  to analyze.

Constraints



String  contains only lowercase letters  ascii[a-z].

Output Format

For each query, return the number of unordered anagrammatic pairs.

Sample Input 0

2
abba
abcd
Sample Output 0

4
0
Explanation 0

The list of all anagrammatic pairs is  and  at positions  and  respectively.

No anagrammatic pairs exist in the second query as no character repeats.

Sample Input 1

2
ifailuhkqq
kkkk
Sample Output 1

3
10
Explanation 1

For the first query, we have anagram pairs  and  at positions  and  respectively.

For the second query:
There are 6 anagrams of the form  at positions  and .
There are 3 anagrams of the form  at positions  and .
There is 1 anagram of the form  at position .

Sample Input 2

1
cdcd
Sample Output 2

5
Explanation 2

There are two anagrammatic pairs of length :  and .
There are three anagrammatic pairs of length :  at positions  respectively.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    elem_dict = {}
    for window in range(1, len(s)):
        for elem_index in range(0, len(s) - window+1):
            store_substr = ''.join(sorted(s[elem_index:elem_index+window]))
            elem_dict[store_substr] = elem_dict.get(store_substr, 0) + 1

    total_count = 0
    #print(elem_dict)
    for elem in elem_dict.keys():
        #print("Elem: ", elem_dict[elem])
        total_count += ( elem_dict[elem] * (elem_dict[elem]-1) ) // 2
        #print("total_count: ", total_count)

    return total_count

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input("No of test cases: "))

    for q_itr in range(q):
        s = input("String: ")

        result = sherlockAndAnagrams(s)
        print(str(result) + '\n')
        #fptr.write(str(result) + '\n')

    #fptr.close()
