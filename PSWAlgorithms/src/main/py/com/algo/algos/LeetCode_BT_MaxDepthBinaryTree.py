'''
Given a binary tree node, return the number of nodes in the longest path between the root and a leaf node

Input: Node in a Binary Tree
Output: Integer
Example
Input: <BSTNode 1> =>   Output: 3 (from path 1--> 3--> 4)
LongestPathBinaryTree

Constraints
Time Complexity: O(N)
Auxiliary Space Complexity: O(N)
Binary Tree Node has the following properties:

value (Integer)
left (Binary Tree Node, default null)
right (Binary Tree Node, default null)

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def root_height(node, height):

            if node is None:
                return height

            return max(root_height(node.left, height+1), root_height(node.right, height+1))

        max_depth = root_height(root, 0)

        return max_depth


# DO NOT EDIT
# Node class for a binary tree node
class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


# DO NOT EDIT
# generate tree from list
def deserialize(lst):
    if len(lst) == 0:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while i < len(lst):
        current = queue.pop(0)
        if lst[i] is not None:
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        if i + 1 < len(lst) and lst[i + 1] is not None:
            current.right = TreeNode(lst[i + 1])
            queue.append(current.right)
        i += 2
    return root


if __name__ == '__main__':
    # rows = int(input("Enter rows: "))
    # cols = int(input("Enter cols: "))

    # matrix_board = [['' for col in range(cols)] for row in range(rows)]
    # for row in range(rows):
    #     for col in range(cols):
    #         matrix_board[row][col] = input(f"Enter Element for {row}-{col}: ")
    # word = input("Enter word: ")
    lst = [1, 2, 3, None, None, 4, 5]
    sample_tree = deserialize(lst)

    solution = Solution()
    final_Result = solution.maxDepth(sample_tree)
    print(f"final_Result: {final_Result}")
