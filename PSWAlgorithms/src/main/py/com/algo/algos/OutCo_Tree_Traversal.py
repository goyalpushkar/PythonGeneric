'''


'''
#
# Complete the 'treeBFS' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts TreeNode root as parameter.
#
import math
import os
import random
import re
import sys
from collections import deque

# Node class for a binary tree node
class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

'''
Using a queue and while loop write a function that takes the root of a binary node and outputs an array of values 
ordered by BREADTH FIRST

Input/Output
Input: node {TreeNode}
Output: {Array}
'''
def treeBFS(root):
    # Write your code here
    result = []
    if root is None:
        return result

    elem_queue = deque()
    elem_queue.append(root)
    while len(elem_queue) > 0:
        curr_element = elem_queue.popleft()
        result.append(curr_element.value)

        if curr_element.left is not None:
            elem_queue.append(curr_element.left)

        if curr_element.right is not None:
            elem_queue.append(curr_element.right)

    return result

'''
Using RECURSION or ITERATION with a while loop, write a function that takes the root of a binary tree node and outputs 
an array of values ordered by DEPTH-FIRST (Pre-Order) 

Input/Output
Input: node {TreeNode}
Output: {Array}
'''
def preDFS(root):
    # Write your code here
    result = []
    def helper(root, result):
        if root is None:
            return result

        result.append(root.value)
        result = helper(root.left, result)
        result = helper(root.right, result)

        return result

    result = helper(root, result)
    return result

'''
Using RECURSION or ITERATION with a while loop, write a function that takes the root of a binary tree node and outputs 
an array of values ordered by DEPTH-FIRST (In-Order) 

Input/Output
Input: node {TreeNode}
Output: {Array}
'''
def inDFS(root):
    # Write your code here

    result = []
    def helper(root):
        if root is None:
            return result

        helper(root.left)
        result.append(root.value)
        helper(root.right)

        return result

    result = helper(root)
    return result


'''
Using RECURSION or ITERATION with a while loop, write a function that takes the root of a binary tree node and outputs
an array of values ordered by DEPTH-FIRST (Post-Order)

Input/Output
Input: node {TreeNode}
Output: {Array}

Example Tree:
               4
             /   \
           2       5
         /   \       \
       1       3       7
                     /   \
                   6      8
'''
def postDFS(root):
    # Write your code here
    result = []

    # def helper(root):
    #     if root is None:
    #         return result
    #
    #     helper(root.left)
    #     helper(root.right)
    #     result.append(root.value)
    #
    #     return result
    #
    # result = helper(root)
    # return result

    if root is None:
       return result
    node_stack = deque()
    pre_node = None
    # Continue until stack is empty and root is None
    while root is not None or len(node_stack) > 0:
        # if root is not None, traverse left elements and put them on a stack
        if root is not None:
            node_stack.append(root)
            root = root.left
        else:
            # If root is none, peek the element from stack and if it does not have right element or right element is
            # already visited then push the element in output, pop it out from the stack and set root as None
            # else traverse towards right
            last_elem = node_stack[-1]
            if last_elem.right is None or last_elem.right == pre_node:
                result.append(last_elem.value)
                node_stack.pop()
                root = None
                pre_node = last_elem
            else:
                root = last_elem.right

    return result

# generate tree from list
def deserialize(lst):
    if len(lst) == 0:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while i < len(lst):
        current = queue.pop(0)
        if lst[i] != -1:
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        if i + 1 < len(lst) and lst[i + 1] != -1:
            current.right = TreeNode(lst[i + 1])
            queue.append(current.right)
        i += 2
    return root

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    compressed_tree_count = int(input().strip())
    compressed_tree = []

    for _ in range(compressed_tree_count):
        compressed_tree_item = int(input().strip())
        compressed_tree.append(compressed_tree_item)

    root = deserialize(compressed_tree)
    result = treeBFS(root)
    print('\n'.join(map(str, result)))
    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    # fptr.close()
