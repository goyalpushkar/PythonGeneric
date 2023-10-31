'''
Given a non-empty binary search tree (BST) and a target value, find k values in the BST that are the closest to the target.

Example
example1

"target": 2
"k": 2
Output:

[1, 2]
As we can see the target value is 2 and [1, 2] are the nearest values (in terms of the absolute difference between target value and node values). Besides this, the answer [2, 3] is also correct, because abs(2 - 1) = abs(2 - 3). You can return any of them. You can also return your answer in any order, that is [1, 2] or [2, 1], both are correct.

Notes
The function accepts the root of the BST.
Return the k nearest values to the given target value.
The values in the BST are NOT necessarily distinct.
If there are multiple correct answers, return any one.
Constraints:

1 <= number of nodes in the tree <= 100000
1 <= values stored in the nodes <= 109
0 <= target value <= 109
1 <= k <= n
number of edges = n - 1
'''

# For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_k_closest_values(root, target, k):
    """
    Args:
    root(BinaryTreeNode_int32)
    target(int32)
    k(int32)
    Returns:
    list_int32
    """
    # Write your code here.
    # approach 1 - 
    # Create a min priority heap for nodes with difference from target
    # Traverse the tree and check the difference and insert into heap
    # if heap size greater than allowed limit remove from heap
    import heapq, math
    
    min_heap = []
    heapq.heapify(min_heap)
    
    def traversal(curr, min_heap):
        # print(f"min_heap 1:{min_heap}")
        if curr.left:
            traversal(curr.left, min_heap)
        
        if curr.right:
            traversal(curr.right, min_heap)    
            
        diff = abs(curr.value - target)
        diff = diff if diff > 0 else -math.inf
        heapq.heappush(min_heap, (-diff, curr.value))
        # print(f"min_heap 2:{min_heap}")
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    if root is None:
        return []
    
    traversal(root, min_heap)
    # print(min_heap)
    final_res = []
    for elem in min_heap:
        final_res.append(elem[1])
    
    return final_res