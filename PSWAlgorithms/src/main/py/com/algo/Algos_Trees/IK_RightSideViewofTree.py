'''
Given a binary tree, imagine yourself standing on the right side of it and return a list of the node values that you
can see from the top to the bottom.

Example One
                    0
            1               2
    3           4


Output:
[0, 2, 4]
From the right side, the tree will look like below:

Example one output

Example Two
                     0
            1
                 2
            3

Output:
[0, 1, 2, 3]
Notes
Constraints:
1 <= number of nodes in the tree <= 20000
0 <= node value < number of nodes in the tree
Node values are unique
'''
"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def right_view(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    result = []

    if root is None:
        return result

    traverse_queue = deque()
    traverse_queue.append(root)

    while traverse_queue:

        queue_count = len(traverse_queue)
        # temp = []
        last_element = None
        for _ in range(queue_count):

            curr_node = traverse_queue.popleft()
            # temp.append(curr_node.value)
            last_element = curr_node.value

            if curr_node.left:
                traverse_queue.append(curr_node.left)

            if curr_node.right:
                traverse_queue.append(curr_node.right)

        # result.append(temp[-1])
        result.append(last_element)

    return result

