'''
In an array, , the elements at indices  and  (where ) form an inversion if . In other words, inverted elements  and  are considered to be "out of order". To correct an inversion, we can swap adjacent elements.
For example, consider the dataset . It has two inversions:  and . To sort the array, we must perform the following two swaps to correct the inversions:

Given  datasets, print the number of inversions that must be swapped to sort each dataset on a new line.
Function Description
Complete the function countInversions in the editor below. It must return an integer representing the number of inversions required to sort the array.
countInversions has the following parameter(s):
arr: an array of integers to sort .
Input Format
The first line contains an integer, , the number of datasets.
Each of the next  pairs of lines is as follows:
The first line contains an integer, , the number of elements in .
The second line contains  space-separated integers, .
Constraints



Output Format
For each of the  datasets, return the number of inversions that must be swapped to sort the dataset.
Sample Input
2
5
1 1 1 2 2
5
2 1 3 1 2
Sample Output
0
4
Explanation
We sort the following  datasets:
 is already sorted, so there are no inversions for us to correct. Thus, we print  on a new line.

We performed a total of  swaps to correct inversions.
'''

import math
import os
import random
import re
import sys

# Complete the countInversions function below.

#number_of_inversions = 0
def countInversions(arr):
    number_of_inversions_returned = 0
    number_of_inversions_returned = merge_sort(arr)

    return number_of_inversions_returned

def merge(arr_passed, first_half, second_half):
    i = 0
    j = 0
    k = 0
    number_of_inversions = 0

    while i < len(first_half) and j < len(second_half):
        if first_half[i] <= second_half[j]:
            arr_passed[k] = first_half[i]
            i += 1
        else:
            arr_passed[k] = second_half[j]
            j += 1
            number_of_inversions += 1

        k += 1

    while i < len(first_half):
        arr_passed[k] = first_half[i]
        i += 1
        k += 1
        number_of_inversions += 1

    while j < len(second_half):
        arr_passed[k] = second_half[j]
        j += 1
        k += 1

    return number_of_inversions

def merge_sort(arr_passed):

    #number_of_inversions = 0
    if len(arr_passed) > 1:
        mid = len(arr_passed) // 2
        first_half = arr_passed[:mid]
        second_half = arr_passed[mid:]

        #merge_sort(first_half)
        #merge_sort(second_half)
        #number_of_inversions += merge(arr_passed, first_half, second_half)

        number_of_inversions = merge_sort(first_half) + merge_sort(second_half) + merge(arr_passed, first_half, second_half)

        print(arr_passed)
        print(number_of_inversions)
        return number_of_inversions

    return 0

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input("No of test cases: "))
    for t_itr in range(t):
        n = int(input("No of elements in the array: "))
        arr = list(map(int, input().rstrip().split()))
        result = countInversions(arr)
        print(str(result) + '\n')
        #fptr.write(str(result) + '\n')

    #fptr.close()
