
#!/bin/python3
'''
Largest Rectangle
Skyline Real Estate Developers is planning to demolish a number of old, unoccupied buildings and construct a shopping mall in their place. Your task is to find the largest solid area in which the mall can be constructed.
There are a number of buildings in a certain two-dimensional landscape. Each building has a height, given by . If you join adjacent buildings, they will form a solid rectangle of area
.
  . A rectangle of height and length can be
Complete the function largestRectangle int the editor below. It should return an integer representing the largest rectangle that can be formed within the bounds of consecutive buildings.
largestRectangle has the following parameter(s):
h: an array of integers representing building heights
Input Format
The first line contains , the number of buildings.
The second line contains space-separated integers, each representing the height of a building.
Constraints

Output Format
Print a long integer representing the maximum area of rectangle formed.
Sample Input
5 12345
Sample Output
9
Explanation
An illustration of the test case follows.
For example, the heights array
constructed within the boundaries. The area formed is .
Function Description

                                           12345
'''
import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(h):
    max_area = 0
    for element in range(len(h)):
        number_of_buildings = 1

        for element2 in range(element-1, -1, -1):
            if h[element] <= h[element2]:
                number_of_buildings += 1
            else:
                break

        for element2 in range(element+1, len(h), 1):
            if h[element] <= h[element2]:
                number_of_buildings += 1
            else:
                break

        area = h[element] * number_of_buildings
        print( str(h[element]) + "*" + str(number_of_buildings) + "=" + str(area) )
        if max_area < area:
            max_area = area

    return max_area

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input("Number of buildings: "))

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    print(str(result) + '\n')
    #fptr.write(str(result) + '\n')
    #fptr.close()
