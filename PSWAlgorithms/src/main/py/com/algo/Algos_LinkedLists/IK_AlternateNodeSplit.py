'''
Given a linked list, split it into two by alternating nodes: first node goes into the first list, 
second to second, third to first, fourth to second and so on.

Example
{
"head": [1, 2, 3, 4, 5]
}
Output:

[
[1, 3, 5],
[2, 4]
]
Notes
The function has one parameter, head of the given linked list.
Return a list that contains two heads of linked lists.
Empty linked list is represented by a NULL value in both input and output.
Constraints:

0 <= number of nodes in the given list <= 100000
1 <= value of any node <= 1000000000
'''
"""
For your reference:
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
"""
def alternative_split(head):
    """
    Args:
    head(LinkedListNode_int32)
    Returns:
    list_LinkedListNode_int32
    """
    # Write your code here.
    return_list = []
    
    first_curr, first_prev = head, None
    second_sentinel = LinkedListNode(None)
    second_curr = second_sentinel
    index = 1
    while first_curr:
        
        # Even nodes need to move to second list
        if index % 2 == 0:
            # break link of current node from prev node
            first_prev.next = first_curr.next
            # Link current node to second list
            second_curr.next = first_curr
            # Move current cursor to next Node
            first_curr = first_curr.next
            # break link of next node from the second list
            second_curr = second_curr.next
            second_curr.next = None
        else:
            first_prev = first_curr
            first_curr = first_curr.next
        
        index += 1 
        
    return_list.append(head)
    return_list.append(second_sentinel.next)
    
    return return_list
