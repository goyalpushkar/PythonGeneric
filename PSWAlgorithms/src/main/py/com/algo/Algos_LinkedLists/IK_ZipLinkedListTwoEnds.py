'''
Given a linked list, zip it from its two ends in place, using constant extra space. 
The nodes in the resulting zipped linked list should go in this order: first, last, second, 
second last, and so on.

Follow up:

Implement functions to zip two linked lists and to unzip such that unzip(zip(L1, L2)) returns L1 and L2.

Example One
{
"head": [1, 2, 3, 4, 5, 6]
}
Output:

[1, 6, 2, 5, 3, 4]
Example Two
{
"head": [1, 2, 3, 4, 5]
}
Output:

[1, 5, 2, 4, 3]
Notes
The function has one parameter: head of the given linked list.
Return the head of zipped linked list.
Constraints:

0 <= number of nodes <= 100000
-2 * 109 <= node value <= 2 * 109
'''

# For your reference:
# class LinkedListNode:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

def zip_given_linked_list(head):
    """
    Args:
    head(LinkedListNode_int32)
    Returns:
    LinkedListNode_int32
    """
    # Write your code here.
    if head is None:
        return
    
    def recurse(back, front):
        # print(f"1 back: {back.value}, front: {front.value}")
        if back.next is not None:
            front = recurse(back.next, front)
            # print(f"front: {front}")
            if front == "-1":
                return "-1"
        
        # # print(f"2 back: {back.value}, front: {front.value}")
        # if even number of values then first cond and if odd number of values then second cond
        if front.next == back or front == back:
            back.next = None
            return "-1"
            
        if front.next != back:
            temp = front.next
            front.next = back
            back.next = temp
            front = temp
        # if even number of values then first cond and if odd number of values then second cond
        # elif front.next == back or back == front:
        #     back.next = None
        #     return "-1"
        # else:
        #     return front
        
        return front
    
# IK Solution 
# We provided one solution:

# Split the given list into halves so that, for example, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL becomes 1 -> 2 -> 3 -> NULL and 4 -> 5 -> 6 -> NULL.
# Reverse the second list. In this example the second list becomes 6 -> 5 -> 4 -> NULL.
# Now merge the two lists by alternating the nodes from first and second lists. Build the resulting list by updating the next pointers of the nodes.
