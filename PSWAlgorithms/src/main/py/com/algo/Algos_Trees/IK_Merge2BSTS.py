'''
Given two Binary Search Trees (BSTs), merge them into a single height-balanced BST.

Example One
Example1 input

Output:

Example1 output

Example Two
Example2 input

Output:

Example2 output

Notes
A node with value equal to the value of the root node can be inserted either in the left or right subtree.
A binary tree is called height-balanced if for each node the following property is satisfied:
The difference in the heights of its left and right subtrees differ by at most 1.
Constraints:

1 <= number of nodes in the given BSTs <= 104
-10^9 <= node value <= 10^9
'''
"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def merge_two_binary_search_trees(root1, root2):
    """
    Args:
    root1(BinaryTreeNode_int32)
    root2(BinaryTreeNode_int32)
    Returns:
    BinaryTreeNode_int32
    """
    # Write your code here.
    
    def inorder_traverse(node, inorder_list):
        if node.left:
            inorder_traverse(node.left, inorder_list)
            
        inorder_list.append(node.value)
        
        if node.right:
            inorder_traverse(node.right, inorder_list)
        
        return inorder_list
    
    # Get In-Order list of the trees
    in_order_1 = []
    in_order_2 = []
    if root1:
        in_order_1 = inorder_traverse(root1, [])
        
    if root2:
        in_order_2 = inorder_traverse(root2, [])
    
    # print(f"in_order_1: {in_order_1}, in_order_2: {in_order_2}")
    def merge_2_lists(list1, list2):
        
        idx1, idx2, idx3 = 0,0,0
        final_list = []
        while idx1 < len(list1) and idx2 < len(list2):
            if list1[idx1] <= list2[idx2]:
                final_list.append(list1[idx1])
                idx1 += 1
                
            else:  # list1[idx1] > list2[idx2]:
                final_list.append(list2[idx2])
                idx2 += 1
                
            # idx3 += 1
            
        while idx1 < len(list1):
            final_list.append(list1[idx1])
            idx1 += 1
            # idx3 += 1
            
        while idx2 < len(list2):
            final_list.append(list2[idx2])
            idx2 += 1
            # idx3 += 1
        
        return final_list
    
    # Merge both lists
    final_tree_list = merge_2_lists(in_order_1, in_order_2)
    # print(f"final_tree_list: {final_tree_list}")

    def build_balanced_tree(final_list, start, end):
        # print(f"final_list: {final_list}, start: {start}, end: {end}")
        if start >= end:
            return
        
        mid = (start+end)//2   # ( start - (start-end)//2 )
        # print(f"mid: {mid}")
        node = BinaryTreeNode(final_list[mid])
        
        node.left = build_balanced_tree(final_list, start, mid)
        node.right = build_balanced_tree(final_list, mid+1, end)
        
        return node
    
    final_node = build_balanced_tree(final_tree_list, 0, len(final_tree_list))
    return final_node