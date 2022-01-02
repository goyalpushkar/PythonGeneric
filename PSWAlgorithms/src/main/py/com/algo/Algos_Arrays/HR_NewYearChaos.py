'''
It's New Year's Day and everyone's in line for the Wonderland rollercoaster ride! There are a number of people queued up, and each person wears a sticker indicating their initial position in the queue. Initial positions increment by  from  at the front of the line to  at the back.

Any person in the queue can bribe the person directly in front of them to swap positions. If two people swap positions, they still wear the same sticker denoting their original places in line. One person can bribe at most two others. For example, if  and  bribes , the queue will look like this: .

Fascinated by this chaotic queue, you decide you must know the minimum number of bribes that took place to get the queue into its current state!

Function Description

Complete the function minimumBribes in the editor below. It must print an integer representing the minimum number of bribes necessary, or Too chaotic if the line configuration is not possible.

minimumBribes has the following parameter(s):

q: an array of integers
Input Format

The first line contains an integer , the number of test cases.

Each of the next  pairs of lines are as follows:
- The first line contains an integer , the number of people in the queue
- The second line has  space-separated integers describing the final state of the queue.

Constraints

Subtasks

For  score
For  score

Output Format

Print an integer denoting the minimum number of bribes needed to get the queue into its final state. Print Too chaotic if the state is invalid, i.e. it requires a person to have bribed more than  people.

Sample Input

2
5
2 1 5 3 4
5
2 5 1 3 4
Sample Output

3
Too chaotic
Explanation

Test Case 1

The initial state:

pic1(1).png

After person  moves one position ahead by bribing person :

pic2.png

Now person  moves another position ahead by bribing person :

pic3.png

And person  moves one position ahead by bribing person :

pic5.png

So the final state is  after three bribing operations.
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes_wrongAnswer(g):
    number_of_bribes = 0
    for index in range(len(g)):
        bribes = g[index] - (index + 1)
        if bribes > 0:
            if bribes >= 3:
                number_of_bribes = -1
                print("Too chaotic")
                return
            else:
                number_of_bribes += bribes

    print(number_of_bribes)

#Bubble Sort - O(N2) Time Out
def minimumBribes_bs(q):

    number_of_bribes = 0
    for first in range(len(q)-1, -1, -1):
        consecutive_bribes = 0
        for second in range(0, first):
            if q[second] > q[second+1]:
                q[second], q[second+1] = q[second+1], q[second]
                number_of_bribes += 1
                consecutive_bribes += 1
            else:
                consecutive_bribes = 0

            if consecutive_bribes >= 3:
                print("Too chaotic")
                return

    print(number_of_bribes)

def minimumBribes(q):
    number_of_bribes = 0
    for index in range(len(q)):

        #Check if an element is ahead more than 2 positions then he has given more bribes
        if (q[index] - ( index + 1 )) > 2:
            print("Too chaotic")
            return

        for elem in range( max(0, q[index]-2), index):
            if q[elem] > q[index]:
                number_of_bribes += 1

    print(number_of_bribes)

if __name__ == '__main__':
    t = int(input("No of test cases: "))
    for t_itr in range(t):
        n = int(input("Number of people: "))
        q = list(map(int, input().rstrip().split()))
        minimumBribes(q)