'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]


Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz


Follow up: Could you do this in one pass?
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Beats 85.6% 31ms
    def removeNthFromEnd(self, head, n):
        # dummy = ListNode(next=head)
        fast = head
        slow = head

        while n > 0:
            n -= 1
            fast = fast.next

        # if fast is at the end of list that means we need to remove first node
        # 1 -> 2 -> 3 -> 4 -> 5 n=5
        if fast is None:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head


    # Beats 55.95% 36 ms
    def removeNthFromEnd_2Pass(self, head, n):
        size = 0
        curr_node = head

        while curr_node:
            size += 1
            curr_node = curr_node.next

        remove_node = size - n + 1

        start = 1
        curr_node = head
        prev = None
        while start <= remove_node:
            if start == remove_node:
                if remove_node == 1:
                    head = curr_node.next
                else:
                    prev.next = curr_node.next
                break

            start += 1
            prev = curr_node
            curr_node = curr_node.next

        return head
