'''
Given the head of a singly linked list, reverse the list, and return the reversed list.



Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []


Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000


Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        traverse_node = head
        prev = None
        while traverse_node:
            temp = traverse_node.next
            traverse_node.next = prev
            prev = traverse_node
            traverse_node = temp

        return prev

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel_node = ListNode()

        def recursive_call(curr_node):
            if curr_node is None:
                return sentinel_node

            my_node = curr_node
            send_node = my_node.next
            my_node.next = None
            return_node = recursive_call(send_node)
            return_node.next = my_node

            return return_node.next

        recursive_call(head)
        return sentinel_node.next