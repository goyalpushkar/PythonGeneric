'''
Given the head of a singly linked list, return true if it is a
palindrome
 or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false


Constraints:
The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9


Follow up: Could you do it in O(n) time and O(1) space?
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse_list(head):
            pred = None
            curr = head
            while curr:
                succ = curr.next
                curr.next = pred

                pred = curr
                curr = succ

            return pred

        # Get middle Node
        hare = head
        tortoise = head
        while hare and hare.next and hare.next.next:
            hare = hare.next.next
            tortoise = tortoise.next

        reverse_node = tortoise.next
        tortoise.next = None

        # Reverse List after middle Node
        reverse_head = reverse_list(reverse_node)

        # Compare Lists
        first_list = head
        second_list = reverse_head
        return_val = True

        while first_list and second_list:
            if first_list.val != second_list.val:
                return False

            first_list = first_list.next
            second_list = second_list.next

        return return_val