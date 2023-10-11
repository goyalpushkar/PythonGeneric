'''
Given the head of a linked list, return the list after sorting it in
ascending order.

Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:
Input: head = []
Output: []


Constraints:
The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

'''


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        import math

        return self.sortL(head)

    def getMidPoint(self, head):
        hare = head
        tortoise = head

        while hare.next and hare.next.next:
            hare = hare.next.next
            tortoise = tortoise.next

        return tortoise

    def merge(self, head1, head2):
        newList = ListNode(-math.inf, None)
        tail = newList
        while head1 and head2:
            if head1.val <= head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next

            tail = tail.next

        if head1:
            tail.next = head1

        if head2:
            tail.next = head2

        return newList.next

    def sortL(self, head):
        if head is None or head.next is None:
            return head

        mid = self.getMidPoint(head)
        # print("mid", mid.val)

        left = head
        right = mid.next
        mid.next = None
        # if left:
        #     print("left", left.val)
        # if right:
        #     print("right", right.val)

        return self.merge(self.sortL(left), self.sortL(right))