'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []


Constraints:
k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import math

        if len(lists) == 0:
            return ListNode('')

        def merge_lists(head1, head2):
            newList = ListNode(math.inf, None)
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

        while len(lists) > 1:
            mid = len(lists) // 2
            start = 0
            end = len(lists) - 1
            while start < mid:
                if start != end:
                    new_list = merge_lists(lists[start], lists[end])
                    lists.pop()
                else:
                    new_list = lists[start]
                lists[start] = new_list
                start += 1
                end -= 1

        return lists[0]

    # Type 2
    def mergeKLists_pq(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import math, heapq
        newList = ListNode(math.inf, None)
        tail = newList
        pq = []

        for l in lists:
            if l:
                heapq.heappush(pq, (l.val, l))
                # TypeError: '<' not supported between instances of 'ListNode' and 'ListNode'
                # heapq.heappush(pq, (l.val, l))
                
        # Until pq becomes empty, extract top element from priority queue
        # pick first element from the top element's list and add to the new list
        while pq:
            (priority, lst) = heapq.heappop(pq)
            tail.next = lst
            tail = lst
            succ = tail.next
            lst.next = None
            if succ:
                heapq.heappush(pq, (succ.val, succ))

        return newList.next