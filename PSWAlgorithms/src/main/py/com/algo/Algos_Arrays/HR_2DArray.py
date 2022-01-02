'''
Given a  2D Array, :
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
We define an hourglass in  to be a subset of values with indices falling in this pattern in 's graphical representation:
a b c
  d
e f g
There are  hourglasses in , and an hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.
For example, given the 2D array:
-9 -9 -9  1 1 1
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0
We calculate the following  hourglass values:
-63, -34, -9, 12,
-10, 0, 28, 23,
-27, -11, -2, 10,
9, 17, 25, 18
Our highest hourglass value is  from the hourglass:
0 4 3
  1
8 6 6
Note: If you have already solved the Java domain's Java 2D Array challenge, you may wish to skip this challenge.
Function Description
Complete the function hourglassSum in the editor below. It should return an integer, the maximum hourglass sum in the array.
hourglassSum has the following parameter(s):
arr: an array of integers
Input Format
Each of the  lines of inputs  contains  space-separated integers .
Constraints


Output Format
Print the largest (maximum) hourglass sum found in .
Sample Input
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
Sample Output
19
Explanation
 contains the following hourglasses:
image
The hourglass with the maximum sum () is:
2 4 4
  2
1 2 4
'''


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_sum = -64
    for row in range(1, len(arr)-1):
        #print(len(arr[row]))
        for col in range(1, len(arr[row])-1):
            running_sum = 0
            print("Row-Col: " + str(row) + " " + str(col))
            running_sum = arr[row-1][col-1] + arr[row-1][col] + arr[row-1][col+1]
            running_sum += arr[row][col] #arr[row][col-1] + + arr[row][col+1]
            running_sum += arr[row+1][col-1] + arr[row+1][col] + arr[row+1][col+1]
            print("running_sum - " + str(running_sum))
            if max_sum < running_sum:
                max_sum = running_sum

    return max_sum

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input("Enter Array Rows: ").rstrip().split())))

    print(arr)
    result = hourglassSum(arr)
    print(str(result) + '\n')
    #fptr.write(str(result) + '\n')
    #fptr.close()

