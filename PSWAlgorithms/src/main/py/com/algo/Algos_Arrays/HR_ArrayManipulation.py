'''
Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in your array.
For example, the length of your array of zeros . Your list of queries is as follows:
    a b k
    1 5 3
    4 8 7
    6 9 1
Add the values of  between the indices  and  inclusive:
index->	 1 2 3  4  5 6 7 8 9 10
	[0,0,0, 0, 0,0,0,0,0, 0]
	[3,3,3, 3, 3,0,0,0,0, 0]
	[3,3,3,10,10,7,7,7,0, 0]
	[3,3,3,10,10,8,8,8,1, 0]
The largest value is  after all operations are performed.
Function Description
Complete the function arrayManipulation in the editor below. It must return an integer, the maximum value in the resulting array.
arrayManipulation has the following parameters:
n - the number of elements in your array
queries - a two dimensional array of queries where each queries[i] contains three integers, a, b, and k.
Input Format
The first line contains two space-separated integers  and , the size of the array and the number of operations.
Each of the next  lines contains three space-separated integers ,  and , the left index, right index and summand.
Constraints




Output Format
Return the integer maximum value in the finished array.
Sample Input
5 3
1 2 100
2 5 100
3 4 100
Sample Output
200
Explanation
After the first update list will be 100 100 0 0 0.
After the second update list will be 100 200 100 100 100.
After the third update list will be 100 200 200 200 100.
The required answer will be .
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):

    values_array = [0 for i in range(n)]
    for index in range(len(queries)):
        start_index = queries[index][0]
        end_index = queries[index][1]
        value = queries[index][2]

        values_array[start_index-1] += value
        if end_index < n:
            values_array[end_index] += -value

    #print(values_array)
    max_value = 0
    sum = 0
    for value in values_array:
        sum += value

        if max_value < sum:
            max_value = sum

    return max_value

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input("Size of Array and number of operations: ").split()
    n = int(nm[0])
    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    print(str(result) + '\n')
    #fptr.write(str(result) + '\n')
    #fptr.close()
