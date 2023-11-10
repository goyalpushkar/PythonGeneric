'''
Given a binary tree, find the largest subtree that's a binary search tree (BST).

Here the largest subtree means a subtree with maximum number of nodes.

Example
Example one

Output:

3
There are seven distinct subtrees. Five of them are BSTs (rooted in 300, 200, 400, 600, 700). Sizes if those five are 3, 1, 1, 1 and 1 respectively. The largest BST subtree has 3 nodes.

Notes
There is only one argument named root denoting the root of the input tree.
Return an integer denoting the size of the largest BST.
Constraints:

0 <= number of nodes <= 100000
-109 <= values stored in the nodes <= 109
'''
"""
For your reference:
"""
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_largest_bst(root):
    """
    Args:
    root(BinaryTreeNode_int32)
    Returns:
    int32
    """
    # Write your code here.
    

# 21/22
def find_largest_bst(root):
    """
    Args:
    root(BinaryTreeNode_int32)
    Returns:
    int32
    """
    # Write your code here.
    
    max_size = 0
    def bst(node):
        nonlocal max_size
        
        if node is None:
            return 0
        
        # print(f"max_size:{max_size},node: {node.value}")
        
        if node.left is None and node.right is None:
            value = 1
            max_size = max(max_size, value)
            return value

        elif node.left is None:
            right = bst(node.right)
            if right == 0:
                return 0
            elif node.value <= node.right.value:
                value = 1 + right
            else:
                value = right
            max_size = max(max_size, value)
            return value
        
        elif node.right is None:
            left = bst(node.left)
            if left == 0:
                return 0
            elif node.value >= node.left.value :
                value = 1 + left
            else:
                value = left
            max_size = max(max_size, value)
            return value
        
        else:
            left = bst(node.left)
            right = bst(node.right)
            if left == 0 or right == 0:
                return 0
            elif node.value >= node.left.value and node.value <= node.right.value:
                value = 1 + left + right
            else:
                value = max(left, right)
            max_size = max(max_size, value)
            return value
        return 0
    
    bst(root)
    return max_size