'''
Given a linked list and an integer k, swap k-th (1-indexed) node from the beginning, with k-th node from the end.

Note that you have to swap the actual nodes, not just their values.

Example
{
"head": [1, 2, 3, 4, 7, 0],
"k": 2
}
Output:

[1, 7, 3, 4, 2, 0]
Notes
The function has two parameters: head of the given linked list and k.
Return the head of the linked list after swapping k-th nodes of given linked list.
Constraints:

1 <= number of nodes in the given list <= 100000
-2 * 109 <= node value <= 2 * 109
1 <= k <= number of nodes
Try to access nodes of the given list as little as possible
'''

# """
# For your reference:
# class LinkedListNode:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
# """

def swap_nodes(head, k):
    """
    Args:
    head(LinkedListNode_int32)
    k(int32)
    Returns:
    LinkedListNode_int32
    """
    # Write your code here.
    def get_first_node(k):
        first_prev, first = LinkedListNode(None), head
        while k > 1:
            first_prev = first
            first = first.next
            k -= 1
            
        return first_prev, first
            
    # if we set temp as kth node from front and last node at the head 
    # when temp reaches the last node then last_node pointer will be kthe distance from last
    # Because diff between temp and last_node is k and when temp reaches last node then last_node
    # will be kth distance from last node
    def get_last_node(temp):
        last_prev, last = LinkedListNode(None), head
        while temp.next:
            last_prev = last
            last = last.next
            temp = temp.next
            
        return last_prev, last
    
    def replace_front_last(first_prev, first, last_prev, last, head):
        
        if first_prev.value is not None:
            first_prev.next = last
        else:
            head = last
            
        if last_prev.value is not None:
            last_prev.next = first
        else:
            head = first
        
        temp = first.next
        first.next = last.next
        last.next = temp
        
        return head
        
    
    # This will give kth node from front
    first_prev, first = get_first_node(k)
    
    # This will give kth node from last
    temp = first
    last_prev, last = get_last_node(temp)
    
    return replace_front_last(first_prev, first, last_prev, last, head)


def swap_nodes(head, k):
    """
    Args:
    head(LinkedListNode_int32)
    k(int32)
    Returns:
    LinkedListNode_int32
    """
    # Write your code here.

    # Write your code here.
    # Get length, front node and its prev in one loop
    # get last node by traversing again
    # replace the nodes
    def get_length(head):
        slow = head
        # fast = head
        length = 1
        slow_prev, front_prev, front = LinkedListNode(None), LinkedListNode(None), head
        while slow.next: #fast.next and fast.next.next:
            slow_prev = slow
            slow = slow.next
            # fast = fast.next.next
            length += 1
            
            if length == k:
                front_prev = slow_prev
                front = slow
            
        # if fast.next is None:
        #     return 2*length - 1, front_prev, front
        # else:
        #     return 2*length, front_prev, front
        return length, front_prev, front
            
    def get_last_node(loop_last_node):
        # print(f"loop_last_node: {loop_last_node}")
        slow = head
        slow_prev = LinkedListNode(None)
        # fast_prev, fast = None, head
        while loop_last_node > 0:
            slow_prev = slow
            slow = slow.next
            # fast_prev = fast.next
            # fast = fast.next.next
            loop_last_node -= 1
            # print(f"loop_last_node: {loop_last_node}, fast_prev: {fast_prev.value}, fast: {fast.value}")
            
        return slow_prev, slow
            
    def replace_front_last(front_prev, front, last_prev, last, head):
        if front_prev.value is not None:
            front_prev.next = last
        else:
            head = last
        
        if last_prev.value is not None:
            last_prev.next = front
        else:
            head = front

        temp = front.next
        front.next = last.next
        last.next = temp

        return head
        
    length, front_prev, front = get_length(head)
    print(f"length: {length}, front_prev: {front_prev.value}, front: {front.value}")
    
    # loop_last_node = ( (length - k) + 1 ) // 2
    # if ( (length - k) + 1 ) % 2 > 0:
    #     loop_last_node += 1
    loop_last_node = (length - k) + 1
    
    last_prev, last = get_last_node(loop_last_node-1)
    print(f"loop_last_node: {loop_last_node}, last_prev: {last_prev.value}, last: {last.value}")
    
    # if ( (length - k) + 1 ) % 2 == 0:
    #     last_prev = last_prev.next
    #     last = last.next
    
    return replace_front_last(front_prev, front, last_prev, last, head)