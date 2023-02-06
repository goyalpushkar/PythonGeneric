'''

Davis has a number of staircases in his house and he likes to climb each staircase , , or  steps at a time. Being a very precocious child, he wonders how many ways there are to reach the top of the staircase.

Given the respective heights for each of the  staircases in his house, find and print the number of ways he can climb each staircase, module  on a new line.

For example, there is  staircase in the house that is  steps high. Davis can step on the following sequences of steps:

1 1 1 1 1
1 1 1 2
1 1 2 1
1 2 1 1
2 1 1 1
1 2 2
2 2 1
2 1 2
1 1 3
1 3 1
3 1 1
2 3
3 2
There are  possible ways he can take these  steps.

Function Description

Complete the stepPerms function in the editor below. It should recursively calculate and return the integer number of ways Davis can climb the staircase, modulo 10000000007.

stepPerms has the following parameter(s):

n: an integer, the number of stairs in the staircase
Input Format

The first line contains a single integer, , the number of staircases in his house.
Each of the following  lines contains a single integer, , the height of staircase .

Constraints

Subtasks

 for  of the maximum score.
Output Format

For each staircase, return the number of ways Davis can climb it as an integer.

Sample Input

3
1
3
7
Sample Output

1
4
44
Explanation

Let's calculate the number of ways of climbing the first two of the Davis'  staircases:

The first staircase only has  step, so there is only one way for him to climb it (i.e., by jumping  step). Thus, we print  on a new line.
The second staircase has  steps and he can climb it in any of the four following ways:
Thus, we print  on a new line.

'''


import math
import os
import random
import re
import sys

#n to 0
def getWays2(n, oneStep):
    '''
    ways = {}
    ways[2] = n // 2
    ways[n % 2] = 1
    '''
    if n % 2 == 1:
        oneStep += 1

    return int(math.factorial((n // 2)+oneStep) / (math.factorial(oneStep) * math.factorial(n // 3)))
    # (n // 2) + 1

#n to 0
def getWays3(n, oneStep):
    '''
    ways = {}
    ways[3] = n // 3
    ways[n % 2] = 1
    '''
    twoStep = 0
    if n % 3 == 1:
        oneStep += 1
    elif n % 3 == 2:
        twoStep += 1

    return int(math.factorial((n // 3)+oneStep+twoStep) / (math.factorial(oneStep) * math.factorial(n // 3)))

def getWays(n, number, oneStep):
    '''
    ways = {}
    ways[2] = n // 2
    ways[n % 2] = 1
    '''
    twoStep = 0
    if n % number == 1:
        oneStep += 1
    elif n % number == 2:
        twoStep += 1

    if number == 2:
        subsets = {number: n//number, 1: oneStep, 3: 0}
    else:
        subsets = {number: n//number, 1: oneStep, 2: twoStep}

    return subsets

    '''
    return int(math.factorial((n // number) + oneStep + twoStep) /
               (math.factorial(n // number) * math.factorial(oneStep) * math.factorial(twoStep))
             )
    '''

def twoThreeWays(n, finalset):
    for index in range(0, n//3):
        if (n - (3*index)) % 2 == 0:
            subset = {3: index, 1: 0, 2: (n - (3*index)) // 2}
            if subset not in finalset.values():
                finalset[2*n+index+1] = subset
            #return subsets
        #else:
         #   return {3: 0, 2: 0, 1: 0}

    return finalset

def totalSteps(n, index, finalSet):  #, sum
    #print("Steps - " + str(n))
    #print("Sum - " + str(sum))
    #print(finalSet)
    #print("Index - " + str(index))
    if n == 0 or n == 1:
        return finalSet #sum
    else:
        # sum +=
        subset = getWays(n, 2, index)
        #print(subset)
        if subset not in finalSet.values():
            finalSet[2*(index)+1] = subset

        subset = getWays(n, 3, index)
        #print(subset)
        if subset not in finalSet.values():
            finalSet[2*(index)+2] = subset

        return totalSteps(n-1, index+1, finalSet)  # , sum

# Complete the stepPerms function below.
def stepPermsWrong(n):
    #totalSum = 1
    finalSet = {}
    index = 0

    subsets = {1: n, 2: 0, 3: 0}
    finalSet[index] = subsets

    #if n != 1:
    totalSteps(n, index, finalSet)  #, totalSum
        #totalSum +=

    # This is kind of special case when 1: 0
    # e.g. if number is 7 then one combination 4 + 3 is not covered
    finalSet = twoThreeWays(n, finalSet)
    '''
    emptyKeys = [k for k, v in finalSet.items() if v == 0]
    for key in emptyKeys:
        del finalSet[key]
    '''

    print(finalSet)
    finalSum = 0
    for values in finalSet.values():
        totalSum = 0
        denominator = 1
        for index in values.values():
            totalSum += index
            denominator *= int(math.factorial(index))

        #print(totalSum)
        if totalSum != 0:
            finalSum += int(math.factorial(totalSum) / denominator)
        #print(finalSum)

    return finalSum

# Complete the stepPerms function below.
def stepPerms(n):
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else:
        return stepPerms(n - 1) + stepPerms(n - 2) + stepPerms(n - 3)

# After OutCo
# time limit failure for 5,6,7,8
# after adding dictionary all test cases passed
def stepPerms_new(n):
    # Write your code here

    def stepPerms_helper(left):

        if left in calc:
            return calc[left]

        if left < 0:
            return 0

        if left == 0:
            calc[left] = 1
            return 1

        final = stepPerms_helper(left - 1) + stepPerms_helper(left - 2) + stepPerms_helper(left - 3)
        calc[left] = final

        return final

    calc = {}
    return stepPerms_helper(n)


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = int(input("No of staircases - "))

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        print(str(res) + '\n')
        #fptr.write(str(res) + '\n')

    #fptr.close()