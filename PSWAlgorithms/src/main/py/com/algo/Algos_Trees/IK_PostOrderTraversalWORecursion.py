'''
Given a binary tree, find its post-order traversal without using recursion.

Example
Example one

Output:

[400, 500, 200, 300, 100]
Notes
Constraints:

1 <= number of nodes <= 105
-109 <= value in a node <= 109
'''
"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""


def postorder_traversal(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    if root is None:
        return None

    result_array = []
    stack_node = []
    stack_node.append(root)

    while stack_node:
        curr_node = stack_node[-1]
        if curr_node.left:
            stack_node.append(curr_node.left)
            curr_node.left = None
        elif curr_node.right:
            stack_node.append(curr_node.right)
            curr_node.right = None
        else:
            result_array.append(stack_node.pop().value)

    return result_array
