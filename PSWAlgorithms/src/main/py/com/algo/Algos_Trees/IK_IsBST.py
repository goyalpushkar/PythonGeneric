'''
Given a binary tree, check if it is a binary search tree (BST). A valid BST does not have to be complete or balanced.

Consider this definition of a BST:

All nodes values of left subtree are less than or equal to parent node value.
All nodes values of right subtree are greater than or equal to parent node value.
Both left subtree and right subtree must be BSTs.
NULL tree is a BST.
Single node trees (including leaf nodes of any tree) are BSTs.
Example One
Example one

Output:

0
Left child value 200 is greater than the parent node value 100; violates the definition of BST.

Example Two
Example two

Output:

1
Notes
Return true if the input tree is a BST or false otherwise.
Constraints:

0 <= number of nodes <= 100000
-109 <= values stored in the nodes <= 109
'''


"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""

# Efficient way - Instead of sorting the array and comparing, check with previous value after left
def is_bst(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     bool
    """
    # Write your code here.
    import math
    if root is None:
        return True

    def helper(node, prev):
        # print(f"prev: {prev}, node.value: {node.value}")
        leftBST, rightBST = True, True

        if node is None:
            return True, prev

        if node.left:
            leftBST, prev = helper(node.left, prev)
        # print(f"leftBST: {leftBST}, prev: {prev}, node.value: {node.value}")

        if node.value < prev:
            return False, prev

        prev = node.value
        if node.right:
            rightBST, prev = helper(node.right, prev)
        # print(f"rightBST: {rightBST}, prev: {prev}, node.value: {node.value}")

        return leftBST & rightBST, prev

    return helper(root, -math.inf)[0]

def is_bst(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     bool
    """
    # Write your code here.
    # inorder traversal and verify if array is sorted
    if root is None:
        return True

    all_nodes = []

    def inorder_traversal(node):

        if node.left:
            inorder_traversal(node.left)

        all_nodes.append(node.value)

        if node.right:
            inorder_traversal(node.right)

        return

    inorder_traversal(root)

    return True if all_nodes == sorted(all_nodes) else False

    # first approach is wrong as it does not check if root's sub tree is valid BST or not
    # def helper(node):

    #     result = True

    #     if node is None:
    #         return True

    #     if ( node.left and node.left.value > node.value ) or (node.right and node.right.value < node.value):
    #         return False

    #     if node.left:
    #         retResult = helper(node.left)
    #         result = result & retResult

    #     if node.right:
    #         retResult = helper(node.right)
    #         result = result & retResult

    #     return result

    # return helper(root)
