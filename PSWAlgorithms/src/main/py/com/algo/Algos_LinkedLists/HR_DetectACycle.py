'''
A linked list is said to contain a cycle if any node is visited more than once while traversing the list. For example, in the following graph there is a cycle formed when node  points back to node .

image

Function Description

Complete the function has_cycle in the editor below. It must return a boolean true if the graph contains a cycle, or false.

has_cycle has the following parameter(s):

: a pointer to a Node object that points to the head of a linked list.
Note: If the list is empty,  will be null.

Input Format

There is no input for this challenge. A random linked list is generated at runtime and passed to your function.

Constraints

Output Format

If the list contains a cycle, your function must return true. If the list does not contain a cycle, it must return false. The binary integer corresponding to the boolean value returned by your function is printed to stdout by our hidden code checker.

Sample Input

The following linked lists are passed as arguments to your function:

image

image

Sample Output

0
1
Explanation

The first list has no cycle, so we return false and the hidden code checker prints  to stdout.
The second list has a cycle, so we return true and the hidden code checker prints  to stdout.
'''
"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

from collections import Set
def has_cycle(head):
    visited_nodes = set()
    if head is None:
        return False
    else:
        traverse_node = head
        found_cycle = False
        while not found_cycle:
            visited_nodes.add(traverse_node)
            traverse_node = traverse_node.next
            if traverse_node is None:
                break

            if traverse_node in visited_nodes:
                found_cycle = True

        return found_cycle
