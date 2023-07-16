'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]


Constraints:
The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reOrderList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Get mid point
        hare = head
        tortoise = head
        while hare and hare.next and hare.next.next:
            hare = hare.next.next
            tortoise = tortoise.next

        reverse_list = tortoise.next
        tortoise.next = None

        # Reverse list
        pred = None
        curr = reverse_list
        while curr:
            succ = curr.next
            curr.next = pred

            pred = curr
            curr = succ
        # pred is the head of reversed list

        # merge 2 lists
        sentinel = ListNode(0, head)
        curr = sentinel
        leftList = head
        rightList = pred
        while leftList and rightList:
            leftNext = leftList.next
            rightNext = rightList.next

            curr.next = leftList
            leftList.next = rightList
            rightList.next = None

            # # last_elem = rightList
            # rightList.next = None
            # leftList.next = rightList

            leftList = leftNext
            rightList = rightNext
            curr = curr.next.next

        curr.next = leftNext

        return sentinel.next

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        '''
        1. reverse the pointers of the last half
            Can be done using fast and slow pointers
        2. Merge the two halfs

            1 -> 2 -> 3 -> 4
                1)    1 -> 2
                      4 -> 3
                2)   1-> 4 -> 2 -> 3

            1 -> 2 -> 3 -> 4 -> 5
                1) 1 -> 2 -> 3
                   5 -> 4
                2) 1 -> 5 -> 2 -> 4 -> 3
        '''
        # get slow and fast cursor positions
        slow = head
        fast = head

        while fast and fast.next:  # is not None
            slow = slow.next
            fast = fast.next.next

        # reverse second half pointers
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # merge two halfs of the list
        first, second = head, prev
        while second:
            temp1, temp2 = second.next, first.next
            first.next, second.next = second, temp2
            first, second = temp2, temp1

        # list_nodes = []
        # traverse_node = head
        # while traverse_node is not None:
        #     list_nodes.append(traverse_node)
        #     traverse_node = traverse_node.next

        # # print(list_nodes)

        # if len(list_nodes) == 1:
        #     return

        # def helper(next, prev):
        #     if next.next == prev:
        #         prev.next = None
        #         return
        #     else:
        #         temp = next.next
        #         next.next = prev
        #         prev.next = temp

        #         prev = list_nodes.pop()
        #         if temp == prev:
        #             prev.next = None
        #             return
        #         helper(temp, prev)

        # prev = list_nodes.pop()
        # helper(head, prev)