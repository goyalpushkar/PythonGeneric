'''
Given a binary search tree (BST) and an integer k, find k-th smallest element.

Example
Example one

k = 3

Output:

3
The 3rd smallest element is 3.

Notes
There are two arguments in the input. First one is the root of the BST and second one is an integer k.
Return an integer, the k-th smallest element of the BST.
Constraints:

1 <= number of nodes in the BST <= 6000
1 <= k <= number of nodes
-2 * 109 <= value stored in any node <= 2 * 109
You are not allowed to alter the given BST in any way.

https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
'''

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def kth_smallest_element(root, k):
    """
    Args:
     root(BinaryTreeNode_int32)
     k(int32)
    Returns:
     int32
    """
    # Write your code here.
    arr = []
    if not root:
        return None

    def inorder_traversal(node):
        if node is None:
            return

        inorder_traversal(node.left)
        arr.append(node.value)
        if len(arr) >= k:
            return
        inorder_traversal(node.right)

    inorder_traversal(root)

    # if k > len(arr):
    #     return None

    return arr[k - 1]

def kth_smallest_element(root, k):
    """
    Args:
     root(BinaryTreeNode_int32)
     k(int32)
    Returns:
     int32
    """
    # Write your code here.
    if not root:
        return None

    def inorder_traversal(node, counter):
        if node is None:
            return

        inorder_traversal(node.left)

        counter += 1
        if counter == k:
            return node.value

        inorder_traversal(node.right)

    inorder_traversal(root, 0)

    # if k > len(arr):
    #     return None

    return arr[k - 1]

