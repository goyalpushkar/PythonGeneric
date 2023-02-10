'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
'''

class Solution:
    def maxDepth(self, root):

        def maxDepth_helper(root, depth):
            # if root itself is none
            if root is None:
                return depth-1

            # if no left and right child - Not required
            # if root.left is None and root.right is None:
            #     return depth

            return max(maxDepth_helper(root.left, depth+1), maxDepth_helper(root.right, depth+1))

        return maxDepth_helper(root, 1)




