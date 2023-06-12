'''
Construct a Binary Search Tree whose preorder traversal matches the given list.

Example One
{
"preorder": [1, 0, 2]
}
Output:
          1
    0           2

Example Two
{
"preorder": [2, 0, 1, 3, 5, 4]
}
Output:
                    2
        0                       3
            1                           5
                                    4

inorder = [0,1,2,3,4,5]
Notes
Constraints:
1 <= size of the given list <= 105
-109 <= number in the list <= 109
Numbers in the given list are unique
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
"preorder": [2, 0, 1, 3, 5, 4]
"inorder":  [0, 1, 2, 3, 4, 5]
            {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
            left = curr_index - start
            right = len(arr)-1 - curr_index
                    2
         (2 nodes)           (3 Nodes)
            0                    3
   (0 nodes)  (1 Node)  (0 Nodes)  (2 nodes)
                                       5
                                (1 node)
                                    4
'''
# T - O(n^2)
# S = O(n)
# Failed 1 test case 15/16
def build_binary_search_tree_bruteforce(preorder):
    """
    Args:
     preorder(list_int32)
    Returns:
     BinaryTreeNode_int32
    """
    # Write your code here.
    def get_next_max(arr, index):
        next_max = -1
        for i in range(index+1, len(arr)):
            if arr[i] > arr[index]:
                next_max = i
                break

        return next_max

    def createBST(arr, start, end):
        if start > end:
            return

        node = BinaryTreeNode(arr[start])
        right_start = get_next_max(arr, start)

        print(start, end, right_start)

        if right_start == -1:
            node.left = createBST(arr, start + 1, high)
            return node

        # if left > 0:
        node.left = createBST(arr, start + 1, right_start - 1)
        # if right > 0:
        node.right = createBST(arr, right_start, end)

        return node

    return createBST(preorder, 0, len(preorder) - 1)

# T - O(n logn)
# S = O(n)
def build_binary_search_tree_inorder(preorder):
        """
        Args:
         preorder(list_int32)
        Returns:
         BinaryTreeNode_int32
        """
        # Write your code here.
        inorder = sorted(preorder)

        def get_index_inorder(inorder_arr, low, high, value):
            if low > high:
                return

            mid = (high - (high - low) // 2)
            if inorder_arr[mid] == value:
                return mid

            if inorder_arr[mid] > value:
                return get_index_inorder(inorder_arr, low, mid - 1, value)
            else:
                return get_index_inorder(inorder_arr, mid + 1, high, value)

        def createBST(arr, inorder_arr, start, end):
            nonlocal preorder_index

            if start > end:
                return

            node = BinaryTreeNode(arr[preorder_index])
            preorder_index += 1

            if start == end:
                return node

            left_end = get_index_inorder(inorder_arr, start, end, node.value)
            # print(preorder_index, 'nodevalue: ', node.value, 'start: ', start, 'end: ', end, 'left_end: ', left_end)

            node.left = createBST(arr, inorder_arr, start, left_end - 1)
            node.right = createBST(arr, inorder_arr, left_end + 1, end)

            return node

        preorder_index = 0
        return createBST(preorder, inorder, 0, len(preorder) - 1)

# T - O(n)
# S = O(n)
def build_binary_search_tree_inorder(preorder):


    # inorder = sorted(preorder)
    # inorder_map = {}
    # for index in range(len(inorder)):
    #     inorder_map[inorder[index]] = index
    #
    # print(inorder, inorder_map)
    #
    # def createBST(arr, start, end):
    #     if start > end:
    #         return
    #
    #     # mid = int(start - (start-end)//2)
    #     mid = start
    #     node = BinaryTreeNode(arr[mid])
    #     print(start, end, mid)
    #
    #     # Get left and right from inorder_map
    #     mid_index = inorder_map[arr[mid]]
    #     # left = mid_index - start
    #     # right = end - mid_index
    #
    #     node.left = createBST(arr, start+1, start+mid_index)
    #     node.right = createBST(arr, start+mid_index + 1, end)
    #
    #     return node
    #
    # return createBST(preorder, 0, len(preorder) - 1)



    # def createBST(arr, start, end):
    #     if start > end:
    #         return
    #
    #     # mid = int(start - (start-end)//2)
    #     mid = start
    #     node = BinaryTreeNode(arr[mid])
    #     print(start, end, mid)
    #
    #     # Get left and right from inorder_map
    #     mid_index = inorder_map[mid]
    #     left = mid_index - start
    #     right = end - mid_index
    #
    #     if left > 0:
    #         node.left = createBST(arr[mid + 1:mid + left + 1], start, mid - 1)
    #     if right > 0:
    #         node.right = createBST(arr[mid + left + 1: mid + left + 1 + right], mid + 1, end)
    #
    #     return node