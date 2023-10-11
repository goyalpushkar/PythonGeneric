'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false


Constraints:
The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Beats 11.5% 41ms
    def isSameTree(self, p, q):
        def tree_traversal(node, traversal):
            if not node:
                traversal.append("E")
                return

            traversal.append("S")
            tree_traversal(node.left, traversal)
            traversal.append(str(node.val))
            tree_traversal(node.right, traversal)

        tree1 = []
        tree_traversal(p, tree1)
        tree2 = []
        tree_traversal(q, tree2)

        tree1 = "".join(tree1)
        tree2 = "".join(tree2)
        # print(f"tree1: {tree1}\ntree2: {tree2}")

        return tree1 == tree2

    # Beats 36.4% 36ms
    def isSameTree(self, p, q):
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
