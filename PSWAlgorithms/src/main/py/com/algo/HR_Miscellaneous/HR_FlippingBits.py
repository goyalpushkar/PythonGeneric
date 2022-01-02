import math
import os
import random
import re
import sys


'''
You will be given a list of 32 bit unsigned integers. Flip all the bits (1->0 and 0->1) and print the result as
an unsigned integer.
Input Format
The first line of the input contains , the number of test cases.
The next lines each contain an integer to process.
Constraints

Output Format
Output one line per element from the list with the decimal value of the resulting unsigned integer.

Sample Input 0

3
2147483647
1
0
Sample Output 0

2147483648
4294967294
4294967295


9/2 = Q 4 r1
4/2 = Q 2 r0
2/2 = Q 1 r0
1/2 = Q 0 r1
'''



# Complete the flippingBits function below.
def flippingBits(n):
    passedstring = ""
    returnstring = ""
    returnValue = 0
    quotient = n
    while quotient > 0:
        passedstring += str(quotient % 2)
        if quotient % 2 == 1:
            returnstring += str(0)
        else:
            returnstring += str(1)
        quotient //= 2

    print(passedstring)
    print(returnstring)

    if len(returnstring) < 32:
        for index in range(1, 32-len(returnstring)+1):
            returnstring += str(1)
    print(returnstring)

    for elem in reversed(range(32)):
        returnValue += int(returnstring[elem]) * int( pow(2,elem) )

    return returnValue

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input("No of test cases - "))
    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        print( str(result) + '\n')
        #fptr.write(str(result) + '\n')

    #fptr.close()
