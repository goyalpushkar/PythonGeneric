'''
Given a binary tree, find the number of unival subtrees. An unival (single value) tree is a tree that has the same
value in every node.

Example One
Output:
6

The input tree has a total of 6 nodes. Each node is a root of a subtree. All those 6 subtrees are unival trees.

Example Two
Output:
5

The input tree has a total of 7 nodes, so there are 7 subtrees. Of those 7, all but two subtrees are unival.
The two non-unival subtrees are:

The one rooted in the root node and
The one rooted in the root's right child.
Notes
Constraints:

0 <= number of nodes in the tree <= 10^5
-10^9 <= node value <= 10^9
'''
"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""


def find_single_value_trees(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """
    # Write your code here.
    if root is None:
        return 0

    def helper(curr):

        # print(curr.value)
        if curr.left is None and curr.right is None:
            return 1, True

        uvCount, leftC, rightC = 0, 0, 0
        left, right = True, True
        leftV, rightV = True, True

        if curr.left:
            if curr.value == curr.left.value:
                left = True
            else:
                left = False
            leftC, leftV = helper(curr.left)

        if curr.right:
            if curr.value == curr.right.value:
                right = True
            else:
                right = False
            rightC, rightV = helper(curr.right)

        # print(left, right, leftV, rightV)
        if left & right & leftV & rightV:
            uvCount = 1
        else:
            uvCount = 0

        # print(uvCount, leftC, rightC)
        uvCount += (leftC + rightC)

        return uvCount, (left & right & leftV & rightV)

    treeCount, treeVal = helper(root)

    return treeCount

