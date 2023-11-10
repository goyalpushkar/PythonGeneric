'''
Count the number of nodes in a complete binary tree. A complete binary tree is a binary tree 
in which every level, except possibly the last, is completely filled, and all nodes in the 
last level are as far left as possible.

Example
Tree

Output:

10
Notes
Constraints:

0 <= number of nodes in the tree <= 2 * 104
0 <= value in a tree node <= 105
The given tree will always be a complete binary tree.
'''
"""
For your reference:
"""
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# IK - O(Log N) - Binary Search
def count_nodes(root):
    """
    Args:
    root(BinaryTreeNode_int32)
    Returns:
    int32
    """
    # Write your code here.
    # get depth of the tree
    # Check at the last level where last node will lie by taking mid point at the last level.
    # Verify if mid exists in the tree else move left or right

# Self - O(N)
def count_nodes(root):
    """
    Args:
    root(BinaryTreeNode_int32)
    Returns:
    int32
    """
    # Write your code here.
    from collections import deque
    
    if root is None:
        return 0
        
    def bfs(node):
        traverse_node = deque()
        traverse_node.append(node)
        
        total_nodes = 0
        while traverse_node:
            n = len(traverse_node)
            total_nodes += n
            
            for i in range(n):
                curr = traverse_node.popleft()
                if curr.left:
                    traverse_node.append(curr.left)
                if curr.right:
                    traverse_node.append(curr.right)
        
        return total_nodes

    return bfs(root)