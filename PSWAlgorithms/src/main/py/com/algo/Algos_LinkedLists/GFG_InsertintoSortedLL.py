'''
Given a sorted circular linked list, the task is to insert a new node in this circular list so that it
 remains a sorted circular linked list.

Example 1:
Input:
LinkedList = 1->2->4
(the first and last node is connected,
i.e. 4 --> 1)
data = 2

Output: 1 2 2 4

Example 2:
Input:
LinkedList = 1->4->7->9
(the first and last node is connected,
i.e. 9 --> 1)
data = 5

Output: 1 4 5 7 9

Your Task:
The task is to complete the function sortedInsert() which should insert the new node into the given
 circular linked list and return the head of the linkedlist.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
0 <= N <= 105
'''
#User function Template for python3

'''
class Node: 
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  '''
class Solution:
    def sortedInsert(self, head, data):
        # Find the smalles node and insert at right place after looping starting from smallest
        # List is empty
        # list has one node
        new_node = Node(data)

        if head is None:
            new_node.next = new_node
            return new_node
        elif head.next == head:
            new_node.next = head
            head.next = new_node
            if new_node.data <= head.data:
                head = new_node
            return head

        pred = head
        curr = head.next
        while curr and pred.data <= curr.data and curr != head:
            # last condition is to handle if all values are equal
            pred = pred.next
            curr = curr.next

        # After above loop pred will be largest and curr will be smallest node
        # Optimization - If new_node is grater than largest value
        if data >= pred.data:
            pred.next = new_node
            new_node.next = curr
            return head

        while curr and curr.data < data:
            curr = curr.next
            pred = pred.next

        pred.next = new_node
        new_node.next = curr
        if new_node.data <= head.data:
            head = new_node

        return head

    # Time limit exceeded
    # This will have an issue if equal node needs to be inserted
    # e.g. 1 -> 4 -> 7 -> 9
    # insert 9
    def sortedInsert_TLE(self, head, data):
        import math
        # code here
        sentinel = Node(math.inf)
        sentinel.next = head
        new_node = Node(data)
        if head is None:
            head = new_node
            return sentinel.next

        pred = head
        curr = head.next

        while curr and not (pred.data < data and data <= curr.data):
            pred = pred.next
            curr = curr.next

        pred.next = new_node
        new_node.next = curr

        return sentinel.next