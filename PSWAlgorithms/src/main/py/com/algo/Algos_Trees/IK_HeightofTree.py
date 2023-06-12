'''
Given a tree, find its height: number of edges in the longest path from the root to any node.

Example
                  1
        3           2           5
                                4
Output:
2
The longest path from the root is 1 -> 5 -> 4. It has two edges.

Notes
Return the number of edges in the longest path from the root to any node.
Constraints:
1 <= number of nodes <= 105

https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
'''

"""
For your reference:
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
"""


def find_height(root):
    """
    Args:
     root(TreeNode_int32)
    Returns:
     int32
    """
    # Write your code here.
    result = 0
    if root is None:
        return result

    def helper(node):

        # Leaf Node
        if len(node.children) == 0:
            return 1

        max_child_height = 0
        for child in node.children:
            max_child_height = max(max_child_height, helper(child))

        return max_child_height + 1

    return helper(root) - 1


"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""


def height_of_binary_tree(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """
    # Write your code here.
    result = 0
    if root is None:
        return result

    def helper(node):

        # Leaf Node
        if node.left is None and node.right is None:
            return 1

        max_child_height = 0
        lh = 0
        if node.left:
            lh = helper(node.left)

        rh = 0
        if node.right:
            rh = helper(node.right)

        max_child_height = max(max_child_height, max(lh, rh))

        return max_child_height + 1

    return helper(root)