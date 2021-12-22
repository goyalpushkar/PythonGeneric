import math
import os
import random
import re
import sys

'''
A prime is a natural number greater than that has no positive divisors other than and itself. Given
integers, determine the primality of each integer and print whether it is Prime or Not prime on a new
line.
Note: If possible, try to come up with an primality algorithm, or see what sort of optimizations
you can come up with for an algorithm. Be sure to check out the Editorial after submitting your
code!
Function Description
Complete the primality function in the editor below. It should return Prime if is prime, or Not prime.
primality has the following parameter(s):
n: an integer to test for primality
Input Format
The first line contains an integer, , denoting the number of integers to check for primality.
Each of the subsequent lines contains an integer, , the number you must test for primality.
Constraints
Output Format
For each integer, print whether is Prime or Not prime on a new line.
Sample Input
3
12
5
7
Sample Output
Not prime
Prime
Prime
Explanation
We check the following integers for primality:
1. is divisible by numbers other than and itself (i.e.: , , ), so we print Not prime on a new
line.
2. is only divisible and itself, so we print Prime on a new line.
3. is only divisible and itself, so we print Prime on a new line
'''

# Complete the primality function below.
def primality(n):
    if n == 1:
       return "Not prime"
    elif n == 2 or n == 3:
       return "Prime"
    elif n % 2 == 0:
       return "Not prime"
    else:
       for elem in range(3,int(math.sqrt(n)) + 1,2):
           if n % elem == 0:
               return "Not prime"

    return "Prime"

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    p = int(input("No of test cases - "))
    #p = int(input())

    for p_itr in range(p):
        n = int(input())

        result = primality(n)

        print(result + '\n')
        #fptr.write(result + '\n')

    #fptr.close()
