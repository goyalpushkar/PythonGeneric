import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

'''
Create a Method which prints the value of each node until the tail
Input: node{ListNode}
Output: void

Example 1 -> 5 -> 7 -> 10
1
5
7
10

'''
def printForward(node):
    # Write your code here
    while(node is not None):
        print(node.data)
        node = node.next

'''
Create a Method which prints the value of each node backwards from the tail to the input node using recursion
Input: node{ListNode}
Output: void

Example 1 -> 5 -> 7 -> 10
10
7
5
1

'''
def printBackward(node):
    # Write your code here
    if node is None:
        return

    if node.next is not None:
        printBackward(node.next)

    print(node.data)

'''
Create a Method on the single linked list class that reverses the order of the nodes in the linked list
Input: node{ListNode}
Output: void

Example 1 -> 5 -> 7 -> 10.reverse()
        10 -> 7 -> 5 -> 1
'''
def reverseLinkedList(node):
    # Write your code here
    prev = None
    child = node
    while child is not None:
        temp = child.next
        child.next = prev
        prev = child
        child = temp

    return prev

'''
Create a Method which swaps the first occurrence of the locations of two nodes in the linked list
Input: head{ListNode}
Input: a {Integer}
Input: b {Integer}
Output: {ListNode}

Example swap(head, 5, 10)
        1 -> 5 -> 7 -> 10
        1 -> 10 -> 7 -> 5
        
'''
def swapNodes(head, a, b):
    # Write your code here
    travel = head
    prev = None
    temp_a, temp_a_prev = None, None
    temp_b, temp_b_prev = None, None
    while travel is not None:
        if travel.data == a and temp_a is None:
            temp_a, temp_a_prev = travel, prev

        if travel.data == b and temp_b is None:
            temp_b, temp_b_prev = travel, prev

        if temp_a is not None and temp_b is not None:
            if temp_a_prev is not None:
                temp_a_prev.next = temp_b
            else:
                head = temp_b

            temp_a.next, temp_b.next, temp_b_prev.next = temp_b.next, temp_a.next, temp_a
            # temp = temp_b.next
            # temp_b.next = temp_a.next
            # temp_b_prev.next = temp_a
            # temp_a.next = temp
            break

        prev = travel
        travel = travel.next

    return head


'''
Given an input of a listNode, return True if the ListNode is in a circular linked list and 
false if the linked list that terminates
Input: head{ListNode}
Output: boolean

Example 
        1 -> 2 -> 10 -> 7 -> 5 -> 3 
                  ^---------------|
        True
        1 -> 2 -> 10 -> 7 
        False
'''

def isCircular(node):
    # Write your code here
    circular = False
    hare = node
    turtle = node
    count = 0
    while (hare is not None) and (not circular):
        hare = hare.next

        if hare == turtle:
            circular = True
            break

        if (count != 0) and (count % 2 == 0):
            turtle = turtle.next

        count += 1

    return circular


if __name__ == '__main__':
    node_count = int(input("Enter Node Count: ").strip())

    node = SinglyLinkedList()

    for _ in range(node_count):
        node_item = int(input("Enter Element: ").strip())
        node.insert_node(node_item)

    print(f"{'*' * 10}printForward{'*' * 10}")
    printForward(node.head)
    print(f"{'*' * 10}printBackward{'*' * 10}")
    printBackward(node.head)
    print(f"{'*' * 10}reverseLinkedList{'*' * 10}")
    reverseReturn = reverseLinkedList(node.head)
    printForward(reverseReturn)
    a = int(input("Enter Element a: ").strip())
    b = int(input("Enter Element b: ").strip())
    print(f"{'*' * 10}swapNodes{'*' * 10}")
    reverseReturn = reverseLinkedList(reverseReturn)
    printForward(reverseReturn)
    swapReturn = swapNodes(reverseReturn, a, b)
    printForward(swapReturn)