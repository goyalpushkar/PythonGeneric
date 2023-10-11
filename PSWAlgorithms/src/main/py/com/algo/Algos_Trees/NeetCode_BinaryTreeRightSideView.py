'''
Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    # Beats 96.68%
    def rightSideView(self, root):
        main_queue = deque()
        if root is None:
            return []

        main_queue.append(root)
        final_list = []
        level = 0
        while len(main_queue) > 0:
            internal_queue = deque()
            for index in range(len(main_queue)):
                elem = main_queue.popleft()
                if index == 0:
                    final_list.append(elem.val)

                if elem.right is not None:
                     internal_queue.append(elem.right)

                if elem.left is not None:
                     internal_queue.append(elem.left)

            main_queue += internal_queue

            level += 1

        return final_list

    def rightSideView_dfs(self, root):
        if not root:
            return None
        res = []

        def dfs(node, lvl):
            if node:
                if len(res) == lvl:
                    res.append(node.val)
                dfs(node.right, lvl + 1)
                dfs(node.left, lvl + 1)

        dfs(root, 0)
        return res