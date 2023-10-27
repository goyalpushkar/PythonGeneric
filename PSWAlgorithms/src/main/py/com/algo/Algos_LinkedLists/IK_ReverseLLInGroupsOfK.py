'''
Given a linked list, reverse every group of k nodes. If there is a remainder (a group of less than k nodes) in the end, reverse that last group, too.

Example One
{
"head": [1, 2, 3, 4, 5, 6],
"k": 3
}
Output:

[3, 2, 1, 6, 5, 4]
Input list consists of two whole groups of three. In the output list the first three and last three nodes are reversed.

Example Two
{
"head": [1, 2, 3, 4, 5, 6, 7, 8],
"k": 3
}
Output:

[3, 2, 1, 6, 5, 4, 8, 7]
There are two whole groups of three and one partial group (a remainder that consists of just two nodes). Each of the three groups is reversed in the output.

Notes
The function has two parameters: head of the given linked list and k.
Return the head of the linked list after reversing the groups of nodes in it.
Constraints:

1 <= number of nodes in the list <= 100000
-2 * 109 <= node value <= 2 * 109
1 <= k <= number of nodes
Cannot use more than constant extra space
'''
"""
For your reference:
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
"""
def reverse_linked_list_in_groups_of_k(head, k):
    """
    Args:
    head(LinkedListNode_int32)
    k(int32)
    Returns:
    LinkedListNode_int32
    """
    # Write your code here.
    sentinel = LinkedListNode(None)
    prev_prev_first = sentinel
    
    prev, curr = None, head
    # first_group = False
    while curr:
        # before starting group
        first = curr
        loop_for = k
        
        # start group traversing
        while loop_for > 0 and curr:
            temp = curr
            curr = curr.next
            temp.next = prev
            prev = temp
            loop_for -= 1
        
        # Store last node in the group as first node
        # curr_first = prev
        # link prev_prev_first to current first
        prev_prev_first.next = prev
        prev_prev_first = first
    
    prev_prev_first.next = None
    
    return sentinel.next
