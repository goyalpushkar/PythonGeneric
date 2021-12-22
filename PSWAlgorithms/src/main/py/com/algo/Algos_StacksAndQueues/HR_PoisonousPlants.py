'''
There are a number of plants in a garden. Each of these plants has been treated with some amount of pesticide. After each day, if any plant has more pesticide than the plant on its left, being weaker than the left one, it dies.

You are given the initial values of the pesticide in each of the plants. Print the number of days after which no plant dies, i.e. the time after which there are no plants with more pesticide content than the plant to their left.

For example, pesticide levels . Using a -indexed array, day  plants  and  die leaving . On day , plant  of the current array dies leaving . As there is no plant with a higher concentration of pesticide than the one to its left, plants stop dying after day .

Function Description
Complete the function poisonousPlants in the editor below. It must return an integer representing the number of days until plants no longer die from pesticide.

poisonousPlants has the following parameter(s):

p: an array of integers representing pesticide levels in each plant
Input Format

The first line contains an integer , the size of the array .
The next line contains  space-separated integers .

Constraints



Output Format

Output an integer equal to the number of days after which no plants die.

Sample Input

7
6 5 8 4 7 10 9
Sample Output

2
Explanation

Initially all plants are alive.

Plants = {(6,1), (5,2), (8,3), (4,4), (7,5), (10,6), (9,7)}

Plants[k] = (i,j) => jth plant has pesticide amount = i.

After the 1st day, 4 plants remain as plants 3, 5, and 6 die.

Plants = {(6,1), (5,2), (4,4), (9,7)}

After the 2nd day, 3 plants survive as plant 7 dies.

Plants = {(6,1), (5,2), (4,4)}

After the 2nd day the plants stop dying.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

from collections import deque
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_data(self):
        return self.value

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

        #return self.head

    def remove_head(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

        #return self.head

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def print_list(self):
        traverse_node = self.head
        while traverse_node is not None:
            print(traverse_node.value)
            traverse_node = traverse_node.next

    def __len__(self):
        traverse_node = self.head
        count = 0
        while traverse_node is not None:
            count +=1
            traverse_node = traverse_node.next

        return count

# Complete the poisonousPlants function below.
def poisonousPlantsTimeout(p):
    head_list = LinkedList()   #List to store heads of all deques

    first_list = LinkedList()    #Create deque for first element
    first_list.add_node(p[0])
    #new_node = first_list
    head_list.add_node(first_list) #first_list.head)
    #head_list.print_list()
    #print( head_list.head.get_data() )
    for index in range(1, len(p)):
        # if current element is less than previous element insert it into current list
        if p[index] <= p[index - 1]:
            current_list = head_list.tail
            current_list.get_data().add_node(p[index])
        # Else create a new list with the next larger element
        else:
            new_list = LinkedList()
            new_list.add_node(p[index])
            #new_node = new_list
            head_list.add_node(new_list) #new_list.head)

        #head_list.print_list()
    print(len(head_list))
    index = 0
    prev_node = head_list.head
    traverse_node = head_list.head.next
    while len(head_list) > 1:
        current_list = traverse_node.get_data()  #head_list[index]
        prev_list = prev_node.get_data()
        print("Current Head: " + str(current_list.head.get_data()) + " :previous head - " + str(prev_list.head.get_data()) )
        current_list.remove_head()
        if not current_list:
            print("Current List is empty")
            prev_node.next = traverse_node.next
        else:
            print("Current List is not empty")
            #Check if after removing head prev list and current list can be merged
            print("Current Head: " + str(current_list.head.get_data()) + " :previous tail - " + str(
                prev_list.tail.get_data()))
            if current_list.head.get_data() <= prev_list.tail.get_data():
                prev_list.tail.next = current_list.head
                prev_list.tail = current_list.tail
                prev_node.next = traverse_node.next
            else:
                if traverse_node != head_list.tail:
                    prev_node = traverse_node

        if traverse_node.next is None:   # == head_list.tail: #.next #is None:
            index += 1
            traverse_node = head_list.head.next
            prev_node = head_list.head
        else:
            traverse_node = traverse_node.next

        print("Head List Len: ", len(head_list), " ", index)

    #head_list.print_list()
    print(len(head_list))
    print(index)

    return index
    '''
    for index in range(1, len(p)):
        # if current element is less than previous element insert it into current list
        if p[index] < p[index - 1]:
            current_deque = head_list.tail
            current_deque.append(p[index])
        else:
            
    '''

    '''
    for index in range(1, len(p)):
        #if current element is less than previous element insert it into current list
        if p[index] < p[index-1]:
            current_list = head_list[len(head_list)-1]
            current_list.add_node(p[index])
        #Else create a new list with the next larger element
        else:
            new_list = LinkedList()
            new_list.add_node(p[index])
            head_list.append(new_list.head)

    index = 1
    while len(head_list) > 1:
        get_list = head_list[index]
        get_list.remove_head()
    '''

# Complete the poisonousPlants function below.
def poisonousPlants(p):
    stack = [(p[0], 0)]
    maxN = 0
    for i in range(1, len(p)):
        if (p[i] > p[i - 1]):
            stack.append((p[i], 1))
            maxN = max((maxN, 1))
        else:
            n = 0
            while (len(stack) > 0 and stack[-1][0] >= p[i]):
                n = max((n, stack[-1][1]))
                stack.pop()
            dayToDie = 0 if len(stack) == 0 else n + 1
            maxN = max((maxN, dayToDie))

            stack.append((p[i], dayToDie))
    return maxN


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input("Length of Array: "))
    p = list(map(int, input().rstrip().split()))
    result = poisonousPlants(p)
    print(str(result) + '\n')
    #fptr.write(str(result) + '\n')
    #fptr.close()