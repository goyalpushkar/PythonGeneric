'''
Using pure recursion, count the number of unique paths to travel from the top left corner to the bottom right corner of
a lattice of M X N square via vertices. When moving through lattice one can only move to right or down

Input - m - rows of square, n - column of squares
Output - # of unique paths
'''
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'latticePaths' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER n
#

def latticePaths(m, n):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    m = int(input().strip())
    n = int(input().strip())
    result = latticePaths(m, n)
    print(f"result: {result}")
    fptr.write(str(result) + '\n')
    fptr.close()
