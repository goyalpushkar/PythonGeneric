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
        5         17

    2       5 13        22

1                   14

target = 12

Output = 13

Avergae Time - O(log N) | Space - O(1)   Worst Time - O(N) | Space - O(1)


initialize traverse_node as tree.root
min_diff = abs(target - tree.root)
min_diff_value = tree.root
loop while traverse_node != None:
    diff_1 = abs(target - traverse_node)
    if diff_1 < min_diff:
        min_diff = diff_1
        min_diff_value = traverse_node.value
    if target == traverse_node:
        return traverse_node.value
    elif target > traverse_node:
        traverse_node = traverse_node.right
    else:
        traverse_node = traverse_node.left

return min_diff_value

Test Cases -
Normal - Target is present in the Tree. Target = 22
         Target is not present in the Tree. Target = 12
         Target node is the leave node. Target = 15
         Target node is the root node. Target = 11
'''

def findClosestValueInBst(tree, target):
    # Write your code here.
    traverse_node = tree
    min_diff = abs(target - tree.value)
    min_diff_value = tree.value
    while traverse_node is not None:
        diff_1 = abs(target - traverse_node.value)
        if diff_1 < min_diff:
            min_diff = diff_1
            min_diff_value = traverse_node.value
        if target == traverse_node:
            return traverse_node.value
        elif target > traverse_node.value:
            traverse_node = traverse_node.right
        else:
            traverse_node = traverse_node.left

    return min_diff_value


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
