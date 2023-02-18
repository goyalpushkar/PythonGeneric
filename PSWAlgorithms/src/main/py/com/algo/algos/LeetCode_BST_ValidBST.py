'''
Given a binary tree root node, check if the tree is a valid binary search tree.

Input: Node in a Binary Tree
Output: Boolean

Time Complexity: O(N)
Auxiliary Space Complexity: O(N)
Binary Tree Node has the following properties:

value (Integer)
right (Binary Tree Node, default null)
left (Binary Tree Node, default null)

https://leetcode.com/problems/validate-binary-search-tree/

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # Approach 1
        # create a list of inorder traversal and then check if list is sorted or not
        def inorder_traverse(curr_node):
            if curr_node is None:
                return None

            inorder_traverse(curr_node.left)
            result_list.append(curr_node.val)
            inorder_traverse(curr_node.right)

        result_list = []
        inorder_traverse(root)

        for elem in range(len(result_list)-1):
            if result_list[elem] >= result_list[elem+1]:
                return False

        return True

        # Approach 2
        # The idea could be implemented as a recursion. One compares the node value with its upper and lower limits if
        # they are available. Then one repeats the same step recursively for left and right subtrees.
        def bst_validate(curr_node, low_val, high_val):
            # base case 1 if current node is None
            if curr_node is None:
                return True

            # base case 2 is current node is less than low or greater than high
            if curr_node.val <= low_val or curr_node.val >= high_val:
                return False

            # Check for left sub tree and right subtree
            return bst_validate(curr_node.left, low_val, curr_node.val) and \
                   bst_validate(curr_node.right, curr_node.val, high_val)

        return bst_validate(root, -math.inf, math.inf)


if __name__ == '__main__':
    # rows = int(input("Enter rows: "))
    # cols = int(input("Enter cols: "))

    # matrix_board = [['' for col in range(cols)] for row in range(rows)]
    # for row in range(rows):
    #     for col in range(cols):
    #         matrix_board[row][col] = input(f"Enter Element for {row}-{col}: ")
    # word = input("Enter word: ")

    solution = Solution()
    final_Result = solution.isValidBST(root)
    print(f"final_Result: {final_Result}")