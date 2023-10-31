''''
Given a binary search tree and two numbers low and high, find the sum of values of all the nodes
 that lie in the inclusive range [low, high].

Example
Tree

{
"low": 5,
"high": 15
}
Output:

45
Nodes 5, 6, 8, 12 and 14 are in the range [5, 15]. 5 + 6 + 8 + 12 + 14 = 45.

Notes
Constraints:

1 <= number of nodes in the tree <= 2 * 104
1 <= value in a tree node <= 105
1 <= low <= high <= 105
'''
"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def get_range_sum(root, low, high):
    """
    Args:
    root(BinaryTreeNode_int32)
    low(int32)
    high(int32)
    Returns:
    int32
    """
    # Write your code here.
    # Write your code here.
    # Approach 1
    # 1. In Order traversal and store result in an array - T O(N) and S - O(N)
    # 2. Take sum of the elements in the sorted array between range. T - O(N)
    # 3. Total T - 2 O(N) and S - O(N)
    
    arr = []
    def in_order(curr):

        if curr.left:
            in_order(curr.left)
            
        arr.append(curr.value)
        
        if curr.right:
            in_order(curr.right)
    
    if root is None:
        return 0
    
    in_order(root)
    sum = 0
    for i, val in enumerate(arr):
        if val >= low and val <= high:
            sum += val
    
    return sum
    
    # Approach 2
    # 1. search for low value, 
    # 1.1 Low not found, then start from the last value greater than low
    # 1.2 Once low found go only to right to find high value
    #  a. High value is on the right subtree of low value
    #  b. High is on the right/left of the any ancestor of low value
    #  c. High is not found then take till the last value less than high
    # return 0
    # Total O(N) and S - O(1), Aux for Recursion - O(N)
    def in_order_traversal(curr, sum):
        # if curr.value > high:
        #     return sum
        # print(f"curr.value: {curr.value}, sum: {sum}")
        if curr.left:
            sum += in_order_traversal(curr.left, 0)
        
        if curr.right:
            sum += in_order_traversal(curr.right, 0)
            
        if curr.value >= low and curr.value <= high:
            sum += curr.value
        
        # print(f"curr.value: {curr.value}, sum: {sum}")
        
        return sum
            
    if root is None:
        return 0
        
    final_sum = in_order_traversal(root, 0)
    
    return final_sum