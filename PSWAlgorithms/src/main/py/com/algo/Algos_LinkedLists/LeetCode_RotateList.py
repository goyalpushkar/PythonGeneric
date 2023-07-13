'''
Given the head of a linked list, rotate the list to the right by k places.



Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]


Constraints:
The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        if length == 0:
            return head

        k = k % length
        if k == length:
            return head

        right_part = length - k - 1
        left_part = k

        sentinel = ListNode()
        tail = sentinel

        curr = head
        while right_part > 0:
            curr = curr.next
            right_part -= 1

        tail.next = curr.next
        curr.next = None

        while left_part > 0:
            tail = tail.next
            left_part -= 1

        tail.next = head

        return sentinel.next

    def rotateRight_2nd(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        sentinel = ListNode(0, head)
        length = 0
        pred = sentinel
        curr = head
        while curr:
            pred = curr
            curr = curr.next
            length += 1

        if length == 0:
            return head

        k = k % length
        if k == 0 or k == length:
            return head

        right_part = length - k
        left_part = k

        tail = pred

        curr = head
        pred = sentinel
        while right_part > 0:
            pred = curr
            curr = curr.next
            right_part -= 1

        tail.next = sentinel.next
        sentinel.next = curr
        pred.next = None

        # while left_part > 0:
        #     tail = tail.next
        #     left_part -= 1
        # tail.next = head

        return sentinel.next