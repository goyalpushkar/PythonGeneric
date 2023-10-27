'''
Given a binary tree, check whether it is a mirror of itself i.e. symmetric around its centre.

Example One
Tree

Output:

1
Example Two
Tree

Output:

0
Example Three
Tree

Output:

0
Notes
Constraints:

0 <= number of nodes in the tree <= 5 * 104
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
from collections import deque


def check_if_symmetric(root):
    """
    Args:
    root(BinaryTreeNode_int32)
    Returns:
    bool
    """
    # Write your code here.
    def rec_helper(node1, node2):
        if node1 is None and node2 is None:
            return True
        
        if node1 is None or node2 is None:
            return False
        
        return node1.value == node2.value and rec_helper(node1.left, node2.right) and rec_helper(node1.right, node2.left)

    return rec_helper(root, root)


def check_if_symmetric(root):
    """
    Args:
    root(BinaryTreeNode_int32)
    Returns:
    bool
    """
    # Write your code here.
    
    if root is None:
        return True
        
    node_deque = deque()
    node_deque.append((root, 0))
    level = 0
    
    while node_deque:
        n = len(node_deque)
        
        # print(f"n:{n}")
        # No need to perform check for root node
        # else check if all nodes in the deque are symmetric from start and end
        if node_deque[-1][0] != root:
            if n % 2 != 0:
                return False
            else:
                for i in range(n//2):
                    # print(f"i:{i}, node_deque: {node_deque[i][0].value}, {node_deque[n-1-i][0].value}")
                    if (node_deque[i][0].value != node_deque[n-1-i][0].value) or \
                        ( node_deque[i][1] + node_deque[n-1-i][1] != pow(2, level)-1 ):
                        return False
        
        for i in range(n):
            curr_node, curr_level = node_deque.popleft()
            # print(f"curr_node:{curr_node.value}, curr_level: {curr_level}")
            if curr_node.left:
                node_deque.append((curr_node.left, 2*curr_level))
            if curr_node.right:
                node_deque.append((curr_node.right, 2*curr_level+1))
        level += 1
    
    return True
