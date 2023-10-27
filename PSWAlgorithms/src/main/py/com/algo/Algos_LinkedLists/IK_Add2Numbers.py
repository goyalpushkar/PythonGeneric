'''
Write a function which adds two numbers a and b, represented as linked lists of size lenA and 
lenB respectively, and returns the sum of a and b in the form of a new linked list.

Ignoring the allocation of a new linked list, try to use constant memory when solving it.

A number is represented by a linked list, with the head of the linked list being the least significant digit. 
For example 125 is represented as 5->2->1, and 371 is represented as 1->7->3. Adding 5->2->1(125) and 
1->7->3(371) should produce 6->9->4(496).

Example One
{
"l_a": [7, 5, 2],
"l_b": [2, 0, 3]
}
Output:

[9, 5, 5]
As l_a = 7->5->2 means number 257 and l_b = 2->0->3 means number 302. Sum of 257 and 302 is 559 so, 
result will represent 9->5->5.

Example Two
{
"l_a": [5, 8, 3],
"l_b": [9, 4, 1]
}
Output:

[4, 3, 5]
As l_a = 5->8->3 means number 385 and l_b = 9->4->1 means number 149. Sum of 385 and 149 is 534 so, 
result will represent 4->3->5.

Notes
There are two input parameters l_a and l_b, denoting linked lists representing numbers a and b respectively.
Output is the head node of resultant linked list representing the sum of two numbers a and b.
Constraints

1 <= length of the input linked lists <= 100000
0 <= linked list node value <= 9
Leading zeros will not appear in the input and will not be accepted in the output.
No negative numbers.

{
"expression": "((1+2)*3*)"
}

{
"expression": "()()[]{}"
}


{
"expression": "1+*2"
}
{
"expression": "3(2)+"
}
'''
# """
# For your reference:
# class LinkedListNode:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
# """
def add_two_numbers(l_a, l_b):
    """
    Args:
    l_a(LinkedListNode_int32)
    l_b(LinkedListNode_int32)
    Returns:
    LinkedListNode_int32
    """
    # Write your code here.
    carry_over = 0
    curr_a = l_a
    curr_b = l_b
    prev_a, prev_b = LinkedListNode(None), LinkedListNode(None)
    
    ret_list = None
    while curr_a or curr_b:
        if curr_a:
            a_val = curr_a.value
        else:
            a_val = 0
        
        if curr_b:
            b_val = curr_b.value
        else:
            b_val = 0      
        
        temp = a_val + b_val + carry_over
        
        carry_over = temp // 10
        temp = temp % 10 
        
        if curr_a:
            curr_a.value = temp
            prev_a = curr_a
            curr_a = curr_a.next
            ret_list = "A"
        
        if curr_b:
            curr_b.value = temp
            prev_b = curr_b
            curr_b = curr_b.next
            ret_list = "B"
        
    if carry_over > 0:
        new_node = LinkedListNode(carry_over)
        if ret_list == "A":
            prev_a.next = new_node
            # return l_a
        else:
            prev_b.next = new_node
            # return l_b
    # else:
    return l_a if ret_list == "A" else l_b
    
    # return curr_a