'''
Given a binary tree and an integer k, check whether the tree has a root to leaf path with a sum of values equal to k.
Example One
                    0
            1               2
        3       4
k = 4

Output:
1
Path 0 -> 1 -> 3 has the sum of node values equal to 4.

Example Two
                2
                        3
                                5
                            4
k = 10

Output:
0

Notes
Constraints:
1 <= number of nodes in the tree <= 105
-105 <= node value <= 105
-109 <= k <= 109
'''

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def path_sum(root, k):
    """
    Args:
     root(BinaryTreeNode_int32)
     k(int32)
    Returns:
     bool
    """
    # Write your code here.
    result = False

    if root is None:
        return result

    def helper(node, curr_sum):
        nonlocal result

        # If it is leaf node
        if node.left is None and node.right is None:
            if curr_sum - node.value == 0:
                result = True
                return

        curr_sum -= node.value
        if node.left:
            helper(node.left, curr_sum)

        if result:
            return

        if node.right:
            helper(node.right, curr_sum)

        if result:
            return

        curr_sum += node.value

    helper(root, k)

    return result

def path_sum(root, k):
    """
    Args:
     root(BinaryTreeNode_int32)
     k(int32)
    Returns:
     bool
    """
    # Write your code here.
    result = False

    if root is None:
        return result

    def helper(node, curr_sum):
        if node is None:
            return False

        # If it is leaf node
        if node.left is None and node.right is None:
            if curr_sum-node.value==0:   # - node.value == 0:
                return True

        # curr_sum -= node.value
        return helper(node.left, curr_sum-node.value) or \
                helper(node.right, curr_sum-node.value)

    # helper(root, k)

    return helper(root, k)

