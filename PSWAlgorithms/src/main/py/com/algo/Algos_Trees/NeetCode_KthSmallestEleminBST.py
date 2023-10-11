'''
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of
all the values of the nodes in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Constraints:
The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Beats 86.86% 48ms
    def kthSmallest(self, root, k):
        self.node_count = 0
        self.kth_elem = -1

        def dfs_helper(curr_node):
            # print(f"start: {curr_node.val}-{self.node_count}")
            # if curr_node.left is None:  # self.node_count == 0 and
            #     self.node_count += 1

            if self.node_count >= k:
                return

            if curr_node.left is not None:
                dfs_helper(curr_node.left)
                # print(f"left: {return_val}")
                # if return_val != -1:
                #     return return_val

            self.node_count += 1
            # print(f"after left: {curr_node.val}-{self.node_count}")
            if self.node_count == k:
                self.kth_elem = curr_node.val
                return

            if curr_node.right is not None:
                dfs_helper(curr_node.right)
                # print(f"right: {return_val}")
                # if return_val != -1:
                #     return return_val

            # print(f"after right: {curr_node.val}-{self.node_count}")
            # return -1

        dfs_helper(root)
        return self.kth_elem

    # Beats 78.7% 51ms
    # In order traversal, increment count of nodes at inorder
    # verify if count is same as k then return val
    def kthSmallest_self1(self, root, k):
        self.node_count = 0

        def dfs_helper(curr_node):
            self.node_count = 0

            def dfs_helper(curr_node):
                # print(f"start: {curr_node.val}-{self.node_count}")
                # if curr_node.left is None:  # self.node_count == 0 and
                #     self.node_count += 1

                # if self.node_count == k:
                #     return curr_node.val

                if curr_node.left is not None:
                    return_val = dfs_helper(curr_node.left)
                    # print(f"left: {return_val}")
                    if return_val != -1:
                        return return_val

                self.node_count += 1
                # print(f"after left: {curr_node.val}-{self.node_count}")
                if self.node_count == k:
                    return curr_node.val

                if curr_node.right is not None:
                    return_val = dfs_helper(curr_node.right)
                    # print(f"right: {return_val}")
                    if return_val != -1:
                        return return_val

                # print(f"after right: {curr_node.val}-{self.node_count}")
                return -1

            return dfs_helper(root)

        # 51 ms
        def kthSmallest_inorder(self, root, k):
            self.node_count = 0
            self.res = None

            def inorder(root):
                if not root or self.node_count >= k:
                    return

                inorder(root.left)
                self.node_count += 1
                if self.node_count == k:
                    self.res = root.val
                    return
                inorder(root.right)

            inorder(root)
            return self.res

        # 34 ms
        def kthSmallest_dfs(self, root, k):
            res = []

            def dfs(node):
                if not node:
                    return
                dfs(node.left)
                res.append(node.val)
                dfs(node.right)

            dfs(root)
            return res[k - 1]

        # 35 ms
        def kthSmallest_bfs(self, root, k):
            n = 0
            stack = []
            curr = root
            while stack or curr:
                while curr:
                    stack.append(curr)
                    curr = curr.left
                curr = stack.pop()
                n += 1
                if n == k: return curr.val
                curr = curr.right