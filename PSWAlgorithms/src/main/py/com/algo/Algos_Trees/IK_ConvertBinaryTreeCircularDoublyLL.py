'''
Given the root node of a binary tree, convert it into a circular doubly linked list in-place. 
The left and the right pointers in nodes are to be used as previous and next pointers, respectively, 
in the structure that you return.

Returned list should follow the in-order traversal order of the given tree.

The "root" node that you return should be the first node in the in-order traversal order. 
That "root" node should be connected with the last node in the in-order traversal as if "root" node goes 
after the last node and last node goes before the "root" node.

Example
Example input

Output:

Example output

Notes
Constraints:

1 <= number of nodes <= 105
-109 <= node value <= 109
Description of the text format of the test cases

You might need this for debugging your solution on IK UpLevel platform.

Input file contains the given tree in the usual binary tree format.

Output file lists node values of the returned data structure:

starting from the returned node,
following right pointers until we reach the last node in the list,
then following left pointers until we come back to the root node.
Example output

Example output

is represented by

[1, 2, 3, 4, 5, 4, 3, 2, 1]
If the returned data structure is not circular or otherwise incorrect, the output may contain the 
correct portion of it, and you will find an error message in the ERROR field.
'''

# Save inorder traversal in an array and then join nodes from the array
def binary_tree_to_cdll(root):
    """
    Args:
    root(BinaryTreeNode_int32)
    Returns:
    BinaryTreeNode_int32
    """
    # Write your code here.

    inorder_arr = []
    def inorder_traversal(node):
        if node is None:
            return
        
        if node.left:
            inorder_traversal(node.left) 
        
        inorder_arr.append(node)

        if node.right:
            inorder_traversal(node.right) 


    inorder_traversal(root) 

    for index, elem in enumerate(inorder_arr):
        if index+1 < len(inorder_arr):
            elem.right = inorder_arr[index+1]
            inorder_arr[index+1].left = elem
        else:
            elem.right = inorder_arr[0]
            inorder_arr[0].left = elem

    return inorder_arr[0]

# Without saving inorder traversal
def binary_tree_to_cdll(root):
    """
    Args:
    root(BinaryTreeNode_int32)
    Returns:
    BinaryTreeNode_int32
    """
    # Write your code here.
    if root is None:
        return root
    
    if root.left is None and root.right is None:
        root.left = root
        root.right = root
        return root
        
    left_list = binary_tree_to_cdll(root.left)
    right_list = binary_tree_to_cdll(root.right)

    if left_list is None:
        right_tail = right_list.left

        root.right = right_list
        right_list.left = root

        right_tail.right = root
        root.left = right_tail
        
        return root
        
    if right_list is None:
        left_tail = left_list.left

        left_tail.right = root
        root.left = left_tail

        left_list.left = root
        root.right = left_list

        return left_list
        
    if left_list is not None and right_list is not None:  
        left_tail = left_list.left
        right_tail = right_list.left
        
        left_tail.right = root
        root.left = left_tail

        right_list.left = root
        root.right = right_list
        
        right_tail.right = left_list
        left_list.left = right_tail
        
        return left_list
    
# This didnt work 10/13
def binary_tree_to_cdll(root):
    """
    Args:
    root(BinaryTreeNode_int32)
    Returns:
    BinaryTreeNode_int32
    """
    # Write your code here.
    predecessor_list = []
    successor_list = []
    return_root = None
    last_node = None
    
    def inorder_traversal(node):
        nonlocal return_root, last_node
        if node is None:
            return
        
        if node.left:
            predecessor_list.append(node)
            inorder_traversal(node.left)
        else:
            # This is to set root node (leftmost node)
            if return_root is None:
                return_root = node
        
        if node.right:
            successor_list.append(node)
            inorder_traversal(node.right)
        else:
            # This is to set last node (leftmost node)
            last_node = node
        
        # print(f"node: {node.value}")
        # for val in predecessor_list:
        #     print(f"predecessor_list: {val.value}")
        # for val in successor_list:
        #     print(f"successor_list: {val.value}")
            
        # pop from predecessor list and make links
        if predecessor_list:
            prev_node = predecessor_list.pop()
            node.right = prev_node
            prev_node.left = node
            
        
        # pop from successor list and make links
        if successor_list:
            succ_node = successor_list.pop()
            node.left = succ_node
            succ_node.right = node
            
        #return node

    inorder_traversal(root) 
    # print(f"return_root: {return_root.value}, last_node: {last_node.value}")
    last_node.right = return_root
    return_root.left = last_node
    
    return return_root
