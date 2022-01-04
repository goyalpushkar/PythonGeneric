'''
Write a function that take Binary Search Tree (BST) and a target integer value and returns the closest value to that
target value contained in the BST

You can assume that there will only be one closest value

Each BST node has an integer value, a left child node and a right child node. A node is said to be the valid BST node if
and only if it satisfies the BST property; its value is strictly greater than the values of every node to its left;
its value is less than or equal to every node to its right; and its children nodes are either valid BST nodes themselves
or None/ null
Sample input -
tree =      10
        5         15

    2       5 13        22

1                   14

target = 12

Output = 13

Avergae Time - O(log N) | Space - O(1)   Worst Time - O(N) | Space - O(1)
'''

def findClosestValueInBst(tree, target):
    # Write your code here.
    pass


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

        