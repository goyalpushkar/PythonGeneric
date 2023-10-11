'''
Given a binary tree, find its vertical order traversal starting from the leftmost level to the rightmost level.

Example
Tree

Output:

[
[4],
[2],
[1, 5, 6],
[3, 8],
[7]
]
Tree

Notes
If two or more nodes lie in the same vertical level, then the one with earlier occurrence in the level-order
 traversal of the tree should come first in the output.
If two or more nodes share the same horizontal and vertical level, then the order should be from left to right.
Constraints:

0 <= number of nodes in the tree <= 2 * 104
0 <= value in a tree node <= 105
'''
"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""

'''
BFS
'''


def vertical_order_traversal(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    if root is None:
        return []

    traverse_queue = deque()
    traverse_queue.append((root, 0))
    negative = []
    positive = []
    zero = []

    while len(traverse_queue) > 0:
        curr, level = traverse_queue.popleft()
        # print(curr.value, level)
        # print(f"negative: {negative}")
        # print(f"zero: {zero}")
        # print(f"positive: {positive}")

        if level == 0:
            zero.append(curr.value)

        if level < 0:
            if len(negative) < abs(level):
                negative.append([curr.value])
            else:
                negative[abs(level) - 1].append(curr.value)

        if level > 0:
            if len(positive) < abs(level):
                positive.append([curr.value])
            else:
                positive[abs(level) - 1].append(curr.value)

        if curr.left:
            traverse_queue.append((curr.left, level - 1))

        if curr.right:
            traverse_queue.append((curr.right, level + 1))

    # print(f"negative: {negative}")
    # print(f"zero: {zero}")
    # print(f"positive: {positive}")
    negative.reverse()
    negative.append(zero)

    return negative + positive


'''
DFS
{
"root": [1,
2, 3,
null, 4, 5, 6,
7, null, null, 8, 9, 10,
null, null, null, null, null, 11, null, null,
null, 12]
}
It is failing for above case 
Reason being in DFS we willnot be able to maintain the order of nodes so we need to use BFS
'''
def vertical_order_traversal(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    if root is None:
        return []

    result = []
    level_map = {}

    def helper(node, level):
        print(node.value, level)
        if level in level_map:
            level_map[level].append(node.value)
        else:
            level_map[level] = [node.value]

        if node.left is None and node.right is None:
            # print(level_map[level])
            # result.append(level_map[level])
            return

        # print(f"level_map: {level_map}")
        if node.left:
            helper(node.left, level - 1)

        if node.right:
            helper(node.right, level + 1)

    helper(root, 0)
    sorted_keys = list(level_map.keys())
    sorted_keys.sort()

    return [level_map[val] for val in sorted_keys]

