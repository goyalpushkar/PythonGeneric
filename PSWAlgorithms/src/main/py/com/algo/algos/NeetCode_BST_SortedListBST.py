# Definition for singly-linked list.
from pyparsing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
                                    -10
                                            -3
                                                    0   
                                                            5
                                                                    9   
-------------------------------------------------------------------------------------------------
                                    -10                                         -3                           0
                                            -3              =>           -10            0       =>      -3        5
                                                    0                                               -10                                 
                1 -----------------------------------------------------
                                    -3                                                  -3
                        -10                     0                           -10                       5
                                                        5          =>                          0              9
                                                        
                                                                9
                2 -----------------------------------------------------
                                    0                                                       5
                            -3              5                                       0               9
                    -10                             9                        -3                             11
                                                         11           -10                                           13
                                                                                                                          15
                                                                                                                            
                                    9                                                                                        
                                5        11                                                                                     
                             0               13
                         -3                       15             
                    -10                       
                    
Need method to find left height and right height as the difference is more than 1 do rotation
Need method to do left rotation and right rotation

1. keep adding child to the right of current node
2. At every odd number perform left rotation on root's right child


-10 -3 0 5 9 11 13 15

root_node = 9
curr_node = 15
index = 7
						-10               -3             -3                 0                          5                            9
							 -3      -10       0      -10    0          -3      5                   0     9                       5    11
							                                    5   -10           9            -3           11                 0         13
							                                                          11    -10                  13          -3              15
																					                                 15   -10 
																					                                                                                     
'''
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        new_list = []
        traverse_node = head
        while (traverse_node != None):
            new_list.append(traverse_node.val)
            traverse_node = traverse_node.next

        if len(new_list) == 0:
            return None
        else:
            return self.build_tree(new_list)

    def build_tree(self, sorted_list):

        if len(sorted_list) == 0:
            return

        mid = len(sorted_list) // 2
        root_node = TreeNode(val=sorted_list[mid], left=None, right=None)

        root_node.left = self.build_tree(sorted_list[0:mid])
        root_node.right = self.build_tree(sorted_list[mid+1:])

        return root_node


    # This approach is not making tree as balanced.
    # e.g. [0,1,2,3,4,5]
    # def sortedListToBST_rotation(self, head: Optional[ListNode]) -> Optional[TreeNode]:
    #
    #     traverse_node = head
    #
    #     root_node = TreeNode(val=None, left=None, right=None)
    #     # we need to do left rotation at every odd element as linked list is already sorted
    #     index = 0
    #     # need to add new element on the node
    #     curr_node = TreeNode(val=None, left=None, right=None)
    #
    #     # Loop through all elements of the linked list
    #     while (traverse_node != None):
    #
    #         new_node = TreeNode(val=traverse_node.val, left=None, right=None)
    #
    #         # Assign first node as root node
    #         if index == 0:
    #             root_node = new_node
    #         else:
    #             curr_node.right = new_node
    #
    #         # if index is odd then perform left rotation
    #         if (index != 0) and (index % 2 == 0):
    #             root_node = self.left_rotation(root_node, curr_node)
    #
    #         curr_node = new_node
    #         traverse_node = traverse_node.next
    #         index += 1
    #
    #     if root_node.val is None:
    #         return None
    #     else:
    #         return root_node
    #
    # '''
    #         -10                        -10                     -10                   -10
    #                 -3                        -3                    -3          -11         -3
    #             -2        0               -2                            0                -1       0
    #                                                                                         -2        5
    #
    #
    # '''
    # def left_rotation(self, root, curr):
    #     root.right = None
    #     curr.left = root
    #
    #     return curr
    #
    # def inorder_traversal(self, root):
    #     if root.left:
    #         self.inorder_traversal(root.left)
    #     print(root.val)
    #     if root.right:
    #         self.inorder_traversal(root.right)

    # This approach is not making tree as balanced.
    # e.g. [0,1,2,3,4,5]
    # def sortedListToBST_rotation(self, head: Optional[ListNode]) -> Optional[TreeNode]:
    #
    #     traverse_node = head
    #
    #     root_node = TreeNode(val=None, left=None, right=None)
    #     # we need to do left rotation at every odd element as linked list is already sorted
    #     index = 0
    #     # need to add new element on the node
    #     curr_node = TreeNode(val=None, left=None, right=None)
    #
    #     # Loop through all elements of the linked list
    #     while (traverse_node != None):
    #
    #         new_node = TreeNode(val=traverse_node.val, left=None, right=None)
    #
    #         # Assign first node as root node
    #         if index == 0:
    #             root_node = new_node
    #         else:
    #             curr_node.right = new_node
    #
    #         # if index is odd then perform left rotation
    #         if (index != 0) and (index % 2 > 0):
    #             root_node = self.left_rotation(root_node.right, root_node)
    #
    #         curr_node = new_node
    #         traverse_node = traverse_node.next
    #         index += 1
    #
    #     if root_node.val is None:
    #         return None
    #     else:
    #         return root_node
    #
    # '''
    #         -10                        -10                     -10                   -10
    #                 -3                        -3                    -3          -11         -3
    #             -2        0               -2                            0                -1       0
    #                                                                                         -2        5
    #
    #
    # '''
    #
    # def left_rotation(self, root, parent):
    #     if root.left:
    #         parent.right = root.left
    #     else:
    #         parent.right = None
    #
    #     root.left = parent
    #
    #     return root
    #
    # def inorder_traversal(self, root):
    #     if root.left:
    #         self.inorder_traversal(root.left)
    #     print(root.val)
    #     if root.right:
    #         self.inorder_traversal(root.right)
    #
    # def get_height(self, root, depth):
    #     if root.left is None and root.right is None:
    #         return depth
    #
    #     if root.left:
    #         left_height = self.get_height(root.left, depth+1)
    #     else:
    #         left_height = 0
    #
    #     if root.right:
    #         right_height = self.get_height(root.right, depth + 1)
    #     else:
    #         right_height = 0
    #
    #     if left_height > right_height:
    #         return left_height - right_height
    #     else:
    #         return right_height - left_height