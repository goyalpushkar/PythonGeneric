'''
Given a binary tree root node, invert the binary tree (mirror) and return back the root node.

Input: Node in a Binary Tree
Output: Node in a Binary Tree

Example
Input: InvertBinaryTree1
               1
        2               3
                    4        5

Output: InvertbinaryTree2
                1
        3               2
    5       4
    
Constraints
Time Complexity: O(N)
Auxiliary Space Complexity: O(N)
Binary Tree Node has the following properties:

value (Integer)
left (Binary Tree Node, default null)
right (Binary Tree Node, default null)
Must swap the entire node instances, not just their values
'''
# Python

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


def inorder(root_node, distance):
    if root_node is not None:
        distance += 5
        inorder(root_node.left, distance)
        print(f"{' '*distance}{root_node.value}")
        inorder(root_node.right, distance)


class Solution:
    def invert(self, root):
      # TODO

        def invert_helper(curr_node):
            if curr_node is not None:
                curr_node.left, curr_node.right = invert_helper(curr_node.right), invert_helper(curr_node.left)

            return curr_node

        return invert_helper(root)


if __name__ == '__main__':
    # rows = int(input("Enter rows: "))
    # cols = int(input("Enter cols: "))

    # matrix_board = [['' for col in range(cols)] for row in range(rows)]
    # for row in range(rows):
    #     for col in range(cols):
    #         matrix_board[row][col] = input(f"Enter Element for {row}-{col}: ")
    # word = input("Enter word: ")
    # DO NOT EDIT
    lst = [4,2,7,1,3,6,9]
    sample_tree = deserialize(lst)
    inorder(sample_tree, 1)

    solution = Solution()
    final_Result = solution.invert(sample_tree)
    print(f"final_Result: {final_Result}")
    inorder(final_Result, 1)