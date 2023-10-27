'''
Given a sequence of enqueue and dequeue operations, return a result of their execution without using a queue implementation from a library. Use two stacks to implement queue.

Operations are given in the form of a linked list, and you need to return the result as a linked list, too. Operations:

A non-negative integer means "enqueue me".
-1 means
If the queue is not empty, dequeue current head and append it to the result.
If the queue is empty, append -1 to the result.
Example One
{
"operations": [1, -1, 2, -1, -1, 3, -1]
}
Output:

[1, 2, -1, 3]
Here is how we would execute the operations and build the result list:

Operation	Queue contents after the operation	Result list after the operation
1	[1]	[]
-1	[]	[1]
2	[2]	[1]
-1	[]	[1, 2]
-1	[]	[1, 2, -1]
3	[3]	[1, 2, -1]
-1	[]	[1, 2, -1, 3]
Example Two
{
"operations": [0, 1, 2, -1, 3]
}
Output:

[0]
The only dequeue operation results in the first enqueued element, 0, to be appended to the result list.

Notes
Constraints:

-1 <= value in the list of operations <= 2 * 109
1 <= number of operations <= 105
There will be at least one dequeue (-1) operation
'''

# For your reference:
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def implement_queue(operations):
    """
    Args:
    operations(LinkedListNode_int32)
    Returns:
    LinkedListNode_int32
    """
    # Write your code here.
    insert_stack = []
    append_stack = []
    sentinel = LinkedListNode(None)
    result = sentinel
    
    def delete_elem():
        
        if append_stack:
            return append_stack.pop()
            
        # pop everything from insert stack and insert into append stack
        while insert_stack:
            append_stack.append(insert_stack.pop())
        
        # return last element from append_stack
        return append_stack.pop()
    
        
    curr = operations
    # for oper in operations:
    while curr:
        # print(f"insert_stack: {insert_stack}")
        if curr.value >= 0:
            insert_stack.append(curr.value)
        else:
            if insert_stack or append_stack:
                new_val = delete_elem()
            else: 
                new_val = -1
                
            new_node = LinkedListNode(new_val)
            result.next = new_node
            result = result.next
        
        curr = curr.next
        
    return sentinel.next
                

# 27/30 - 3 Timeout Error
def implement_queue(operations):
    """
    Args:
    operations(LinkedListNode_int32)
    Returns:
    LinkedListNode_int32
    """
    # Write your code here.
    insert_stack = []
    append_stack = []
    sentinel = LinkedListNode(None)
    result = sentinel
    
    def insert_elem(elem):
        
        # pop everything from insert stack and insert into append stack
        while insert_stack:
            append_stack.append(insert_stack.pop())
        
        # insert element to insert_stack 
        insert_stack.append(elem)
        
        # pop everything from append_stack and insert back into insert_stack
        while append_stack:
            insert_stack.append(append_stack.pop())
        
    curr = operations
    # for oper in operations:
    while curr:
        # print(f"insert_stack: {insert_stack}")
        if curr.value >= 0:
            insert_elem(curr.value)
        else:
            if insert_stack:
                new_val = insert_stack.pop()
            else: 
                new_val = -1
                
            new_node = LinkedListNode(new_val)
            result.next = new_node
            result = result.next
        
        curr = curr.next
        
    return sentinel.next
                