'''
Given a binary tree, return all paths from root to leaf.

Example One
Example one

Output:

[
[1, 2, 4],
[1, 2, 5],
[1, 3, 6],
[1, 3, 7]
]
There are four leafs in the given graph, so we have four paths: from the root to every leaf. Each path is a list of
the values from the tree nodes on the path, and we have four lists. They can go in any order.

Example Two
Example two

Output:

[
[10, 20, 40],
[10, 20, 50],
[10, 30]
]
There are 3 paths in the tree.

The leftmost path contains values: 10 -> 20 -> 40

The rightmost path contains values: 10 -> 30

The other path contains values: 10 -> 20 -> 50

The order of the paths (order of the lists in the outer list) does not matter, so [[10, 30], [10, 20, 40],
[10, 20, 50]] is another correct answer.
'''

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def all_paths_of_a_binary_tree(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    if root is None:
        return []

    final_result = []

    def dfs(node, path):
        # print(f"node: {node.value}, path: {path}")

        path.append(node.value)
        if node.left is None and node.right is None:
            final_result.append(path.copy())
            # path.pop()
            # return

        if node.left:
            dfs(node.left, path)

        if node.right:
            dfs(node.right, path)

        path.pop()

        return

    dfs(root, [])
    return final_result