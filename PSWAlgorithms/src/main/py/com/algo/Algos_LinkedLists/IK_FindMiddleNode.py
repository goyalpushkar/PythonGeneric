'''
Given a linked list, find its middle element.
If the list has even number of nodes, return the second of the two middle nodes.

Example One
{
"head": [1, 2, 3, 4, 5]
}
Output:
3
Example Two
{
"head": [1, 2, 3, 4]
}

Output:
3
Notes
Constraints:
0 <= number of nodes <= 105
-2 * 109 <= node value <= 2 * 109
Do it in one pass over the list
If given linked list is empty, return null.

'''


"""
For your reference:
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
"""
def find_middle_node(head):
    """
    Args:
     head(LinkedListNode_int32)
    Returns:
     LinkedListNode_int32
    """
    # Write your code here.
    if head is None:
        return None

    hare = head
    tortoise = head

    while hare is not None and hare.next is not None:
        hare = hare.next.next
        tortoise = tortoise.next

    return tortoise

# Second way
def find_middle_node(head):
    if head is None:
        return None

    hare = head
    tortoise = head

    while hare.next is not None and hare.next.next is not None:
        hare = hare.next.next
        tortoise = tortoise.next

    return tortoise.next if hare.next is not None else tortoise