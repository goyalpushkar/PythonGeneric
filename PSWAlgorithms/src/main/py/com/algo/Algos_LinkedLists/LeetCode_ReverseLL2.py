'''
https://leetcode.com/problems/reverse-linked-list-ii/description/

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.



Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]


Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n


Follow up: Could you do it in one pass?
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head, left, right):
        curr_node = head
        prev_node = None

        prev_reversal_start = None
        reversal_start_first = None

        start_reverse = False
        left_count = 1

        while curr_node:
            # if curr_node is not equal to left keep proceeding
            if left_count != left and not start_reverse:
                prev_node = curr_node
                curr_node = curr_node.next

                prev_reversal_start = prev_node
            else:
                start_reverse = True

                if reversal_start_first is None:
                    reversal_start_first = curr_node

                temp = curr_node.next
                curr_node.next = prev_node
                prev_node, curr_node = curr_node, temp

                # Stop reversal and
                if left_count == right:  # prev_node.val
                    if prev_reversal_start:
                        prev_reversal_start.next = prev_node
                    if reversal_start_first:
                        reversal_start_first.next = curr_node

                    # In case reversal started from first node we should make head point to
                    # current reversal stop node i.e. prev_node
                    if left == 1:
                        head = prev_node

                    start_reverse = False

            left_count += 1

        return head