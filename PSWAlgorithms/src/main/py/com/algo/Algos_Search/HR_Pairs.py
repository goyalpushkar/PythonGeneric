'''
You will be given an array of integers and a target value. Determine the number of pairs of array elements that have a difference equal to a target value.

For example, given an array of [1, 2, 3, 4] and a target value of 1, we have three values meeting the condition: , , and .

Function Description

Complete the pairs function below. It must return an integer representing the number of element pairs having the required difference.

pairs has the following parameter(s):

k: an integer, the target difference
arr: an array of integers
Input Format

The first line contains two space-separated integers  and , the size of  and the target value.
The second line contains  space-separated integers of the array .

Constraints

each integer  will be unique
Output Format

An integer representing the number of pairs of integers whose difference is .

Sample Input

5 2
1 5 3 4 2
Sample Output

3
Explanation

There are 3 pairs of integers in the set with a difference of 2: [5,3], [4,2] and [3,1] .
'''

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    diff_count = {}
    number_of_pairs = 0
    for index in range(len(arr)):
        diff_count[arr[index] - k] = 1

    for index in range(len(arr)):
        if arr[index] in diff_count:
            number_of_pairs += diff_count[arr[index]]

    return number_of_pairs

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input("Size of arr and Target Value: ").split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input("Array Values: ").rstrip().split()))

    result = pairs(k, arr)

    print(str(result) + '\n')
    #fptr.write(str(result) + '\n')
    #fptr.close()
