'''
Given a binary tree where every node has either 0 or 2 children and every right node is a leaf node, 
flip it upside down turning it into a binary tree where all left nodes are leafs.

Example One
Example one input

Output:

Example one output

Example Two
Example two input

Output:

Example two output

The same output tree oriented differently:

Example two alternative output

Notes
Return the root of the output tree.
Constraints:

0 <= number of nodes <= 100000
1 <= node value <= 100000
'''
"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""

def flip_upside_down(root):
    """
    Args:
    root(BinaryTreeNode_int32)
    Returns:
    BinaryTreeNode_int32
    """
    # Write your code here.
    
    if root is None:
        return None
    
    assign_left_node = None
    assign_right_node = None
    while (root):
        
        next_root = root.left
        next_assign_left_node = root.right
        next_assign_right_node = root
        
        root.left = assign_left_node
        root.right = assign_right_node
        
        if next_root:
            root = next_root.left
            
            assign_left_node = next_root.right
            assign_right_node = next_root
            
            next_root.left = next_assign_left_node
            next_root.right = next_assign_right_node
            
        else:
            return root
        
    return next_root

def flip_upside_down(root):
    """
    Args:
    root(BinaryTreeNode_int32)
    Returns:
    BinaryTreeNode_int32
    """
    # Write your code here.
    if root is None:
        return None
        
    parent_list = {}
    parent = None
    curr_node = root
    
    while curr_node.left:
        parent = curr_node
        curr_node = curr_node.left
        parent_list[curr_node] = parent
    
    return_node = curr_node
    while curr_node != root:
        parent = parent_list[curr_node]
        curr_node.left = parent.right
        curr_node.right = parent
        parent.left = None
        parent.right = None
        curr_node = parent
    
    return return_node
