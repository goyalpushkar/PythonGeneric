'''
Given a linked list with elements sorted in ascending order, convert it into a height-balanced binary search tree.

Example One
Input
-1, 2, 3, 5, 6, 7, 10
Output:
                5
        2               7
    -1      3        6      10

Example Two
Input
-1, 2

Output:
            -1
        2

Notes
A binary tree is called height-balanced if for any node, the difference in the heights of its left and
right subtree does not exceed one.
Input list does not contain duplicates.
Return the root node of the created hight-balanced BST.

Constraints:
1 <= length of the linked list <= 20000
-109 <= node value <= 109

https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
'''

"""
For your reference:
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""

def sorted_list_to_bst(head):
    """
    Args:
     head(LinkedListNode_int32)
    Returns:
     BinaryTreeNode_int32
    """
    # Write your code here.
    aux_arr = []
    if head is None:
        return None

    # Store elements of a linked list into an array
    traverse_node = head
    while traverse_node is not None:
        aux_arr.append(traverse_node)
        traverse_node = traverse_node.next

        # print(aux_arr)

    def create_bst(start, end):
        # print(start,'-', end)
        if start > end:
            return

        mid = int(start - (start - end) // 2)
        node = BinaryTreeNode(aux_arr[mid].value)

        node.left = create_bst(start, mid - 1)
        node.right = create_bst(mid + 1, end)

        # print(node.value)
        return node

    root_tree = create_bst(0, len(aux_arr) - 1)

    return root_tree

# without additional array
def sorted_list_to_bst(head):

    def get_middle(head):
        if head is None or head.next is None:
            return head

        slow = head
        fast = head
        slow_prev = None
        while fast is not None and fast.next is not None:
            slow_prev = slow
            slow = slow.next
            fast = fast.next.next

        slow_prev.next = null

        return slow

    if head is None:
        return None
    elif head.next is None:
        return BinaryTreeNode(head.value)
    else:
        middle_node = get_middle(head)
        root = BinaryTreeNode(middle_node.value)

        # Left side
        head_left = head
        # Right Side
        head_right = middle_node.next
        middle_node.next = null

        root.left = sorted_list_to_bst(head_left)
        root.right = sorted_list_to_bst(head_right)

        return root
