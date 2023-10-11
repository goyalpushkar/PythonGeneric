'''
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.



Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]


Constraints:
The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000

Follow-up: Can you solve the problem in O(1) extra memory space?
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if k == 1 or k == 0:
            return head

        def reverse_list(head, k):
            curr = head
            pred = None
            nodes_handled = 0
            while curr and nodes_handled < k:
                succ = curr.next
                curr.next = pred

                pred = curr
                curr = succ
                nodes_handled += 1
            # pred will be having head of reverselist
            # curr will be having next node

            # if there are less than k elements then reverse the list
            if curr is None and nodes_handled < k:
                # reverse_list(pred, nodes_handled)
                curr = pred
                pred = None
                while curr:
                    succ = curr.next
                    curr.next = pred

                    pred = curr
                    curr = succ

            return pred, curr  # reversehead, reverseHead.next

        # if we call validate_kelements everytime it will unnecessary traverse list
        # for each k set, so its better to do reversing 2 times for the last elements < k
        sentinel = ListNode(0, head)
        prev = sentinel
        curr = head
        while curr:
            startpoint = curr
            revrseHead, revrseHeadNext = reverse_list(curr, k)

            prev.next = revrseHead

            curr = revrseHeadNext
            prev = startpoint

        return sentinel.next

        # def validate_kelements(k):
        #     # if tortoise-1 (if len starts from 1) >= k/2 then there are k elements
        #     # validate if there are k elements in the list starting from head
        #     hare = head
        #     tortoise = head
        #     tor_length = 0
        #     while hare and hare.next and hare.next.next:
        #         hare = hare.next.next
        #         tortoise = tortoise.next
        #         tor_length += 1
        #
        #     if tor_length >= k//2:
        #         return True
        #     else:
        #         return False

    def reverseNodesKGroups_IK(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        sentinel = ListNode(0, head)
        prev = sentinel
        curr = head
        while curr:
            # go to head of next k nodes
            m = curr
            for i in range(k):
                if m is None:
                    return sentinel.next
                m = m.next

            # reverse current k nodes
            localpred = None
            localcurr = curr
            while localcurr:
                succ = localcurr.next
                localcurr.next = localpred

                localpred = localcurr
                localcurr = succ

            # localpred is head of reverselist
            prev.next = localpred
            curr.next = m # need to check why is it required

            prev = curr
            curr = m

        return sentinel.next