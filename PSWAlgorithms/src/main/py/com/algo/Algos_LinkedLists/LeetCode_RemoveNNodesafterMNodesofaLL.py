'''
Given a linked list, delete N nodes after skipping M nodes of a linked list until the last of the linked list.

Example:
Input:
2
8
2 1
9 1 3 5 9 4 10 1
6
6 1
1 2 3 4 5 6

Output:
9 1 5 9 10 1
1 2 3 4 5 6

Explanation:
Deleting one node after skipping the M nodes each time, we have list as 9-> 1-> 5-> 9-> 10-> 1.
Input:
The first line of input contains the number of test cases T. For each test case, the first line of input
contains a number of elements in the linked list, and the next M and N respectively space-separated. The last line contains the elements of the linked list.

Output:
The function should not print any output to the stdin/console.

Your Task:
The task is to complete the function linkdelete() which should modify the linked list as required.

Constraints:

size of linked list <= 1000
'''
# your task is to complete this Function
# Function shouldn't return anything

'''
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
'''


class Solution:
    def skipMdeleteN(self, head, M, N):
        # Code here
        slow = head
        fast = head
        while fast is not None:

            mf = M - 1
            while mf > 0 and fast is not None:
                fast = fast.next
                mf -= 1

            if fast is None:
                break

            nf = N
            rem = fast
            while nf > 0 and rem is not None and rem.next is not None:
                rem = rem.next
                nf -= 1

            fast.next = rem.next

            fast = rem.next
            slow = fast