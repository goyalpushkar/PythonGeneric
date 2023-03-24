'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.


Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]


Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # Beats 96.78%  30ms
    def mergeTwoLists(self, list1, list2):
        listHead = ListNode()
        listCurr = listHead

        while list1 or list2:
            if list1.val <= list2.val:
                listCurr.next = list1
                list1 = list1.next
            else:
                listCurr.next = list2
                list2 = list2.next

            listCurr = listCurr.next

        if list1:
            listCurr.next = list1

        if list2:
            listCurr.next = list2

        return listHead.next

    # Beats 54.27%  40ms
    def mergeTwoLists(self, list1, list2):
        curr1 = list1
        curr2 = list2

        newList = None
        newListHead = None

        while curr1 is not None or curr2 is not None:
            # if newList is not None:
            #     print(f"newList: {newList.val}")
            # else:
            #     print(f"newList: None")
            # if curr1 is not None:
            #     print(f"curr1: {curr1.val}")
            # if curr2 is not None:
            #     print(f"curr2: {curr2.val}")

            print(f"\n\n")

            # First list is finished
            if curr1 is None:
                while curr2 is not None:

                    if newListHead is None:
                        newList = curr2
                        newListHead = newList
                    else:
                        newList.next = curr2
                        newList = newList.next
                    curr2 = curr2.next

            # Second list is finished
            if curr2 is None:
                while curr1 is not None:

                    if newListHead is None:
                        newList = curr1
                        newListHead = newList
                    else:
                        newList.next = curr1
                        newList = newList.next
                    curr1 = curr1.next

            # None of them is finshed
            if curr1 is not None and curr2 is not None:
                if curr1.val <= curr2.val:

                    if newListHead is None:
                        newList = curr1
                        newListHead = newList
                    else:
                        newList.next = curr1
                        newList = newList.next
                    curr1 = curr1.next
                else:

                    if newListHead is None:
                        newList = curr2
                        newListHead = newList
                    else:
                        newList.next = curr2
                        newList = newList.next
                    curr2 = curr2.next

                # newList = newList.next

        return newListHead