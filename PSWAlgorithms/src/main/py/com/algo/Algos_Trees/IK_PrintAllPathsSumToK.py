'''
Given a binary tree and an integer k, find all the root to leaf paths that sum to k.
Example One

                    10
        25                      30
45                          40         50

k = 80
Output:
[
[10, 25, 45]
[10, 30, 40]
]
Example Two
                    5
            5               5
k = 10
Output:
[
[5, 5],
[5, 5]
]
Notes
In case there is no root to leaf path with a sum equal to k, return [[-1]].
The order of the paths (order of the lists in the outer list) does not matter.

Constraints:
1 <= number of nodes <= 104
-105 <= value in a node <= 105
-109 <= k <= 109
'''
"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""


def all_paths_sum_k(root, k):
    result = []

    if root is None:
        return [[-1]]

    def helper(curr_node, curr_sum, curr_path):

        # leaf node
        if curr_node.left is None and curr_node.right is None:
            if curr_sum - curr_node.value == 0:
                curr_path.append(curr_node.value)
                result.append(curr_path)
                curr_path.pop()

        curr_path.append(curr_node.value)
        if curr_node.left:
            helper(curr_node.left, curr_sum- curr_node.value, curr_path)

        if curr_node.right:
            helper(curr_node.right, curr_sum- curr_node.value, curr_path)

        curr_path.pop()

    helper(root, k, [])

    if len(result) == 0:
        result = [[-1]]

    return result

def all_paths_sum_k_notworking(root, k):
    """
    Args:
     root(BinaryTreeNode_int32)
     k(int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    result = []

    if root is None:
        return [[-1]]

    memo = {}
    def dfs(curr_node, curr_sum, curr_path):
        key = "".join(str(elem) for elem in side)[:-1]
        # print(curr_sum, curr_path, memo, key)
        if curr_sum == k and curr_node is None:
            if memo.get(key, 0) == 0:
                memo[key] = 1
                result.append(curr_path.copy())

        if curr_node is None:
            return

        # print(curr_node.value)

        curr_sum += curr_node.value
        curr_path.append(curr_node.value)
        side.append(str(curr_node.value) + 'L')
        dfs(curr_node.left, curr_sum, curr_path, side)
        curr_sum -= curr_node.value
        curr_path.pop()
        side.pop()
        memo[key] = 0

        curr_sum += curr_node.value
        curr_path.append(curr_node.value)
        side.append(str(curr_node.value) + 'R')
        dfs(curr_node.right, curr_sum, curr_path, side)
        curr_sum -= curr_node.value
        curr_path.pop()
        side.pop()
        memo[key] = 0


    dfs(root, 0, [])

    if len(result) == 0:
        result = [[-1]]

    return result
