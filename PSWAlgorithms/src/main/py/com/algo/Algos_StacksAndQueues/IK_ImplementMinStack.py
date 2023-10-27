'''
You have to build a min stack. Min stack should support push, pop methods (as usual stack) as well as one 
method that returns the minimum element in the entire stack.

You are given an integer array named operations of size n, containing values >= -1.

operations[i] = -1 means you have to perform a pop operation. The pop operation does not return the 
removed/popped element.
operations[i] = 0 means you need to find the minimum element in the entire stack and add it at the end 
of the array to be returned.
operations[i] >= 1 means you need to push operations[i] on the stack.

Example
{
"operations": [10, 5, 0, -1, 0, -1, 0]
}
Output:

[5, 10, -1]
Initially stack = [], ans = [].
operations[0] = 10 -> push -> stack = [10], ans = []
operations[1] = 5 -> push -> stack = [10, 5], ans = []
operations[2] = 0 -> get minimum element -> stack = [10, 5], ans = [5]
operations[3] = -1 -> pop -> stack = [10], ans = [5]
operations[4] = 0 -> get minimum element -> stack = [10], ans = [5, 10]
operations[5] = -1 -> pop -> stack = [], ans = [5, 10]
operations[6] = 0 -> get minimum element -> stack = [], ans = [5, 10, -1] (As stack is empty we have
 to consider -1 as the minimum element.)

Notes
Return an integer array res, containing answer for each operations[i] = 0.
If stack is empty, then do nothing for pop operation.
If stack is empty, then consider -1 as the minimum element.
Constraints:

1 <= n <= 100000
-1 <= operations[i] <= 2 * 109, for all i.
'''
def min_stack(operations):
    """
    Args:
    operations(list_int32)
    Returns:
    list_int32
    """
    # Write your code here.
    def append(value, min_stack, normal_stack):
        if min_stack and value > min_stack[-1]:
            min_stack.append(min_stack[-1])
        else:
            min_stack.append(value)
        
        normal_stack.append(value)
        
    def pop(min_stack, normal_stack):
        min_stack.pop()
        normal_stack.pop()
        
    def min_pop(min_stack, normal_stack):
        # popped = min_stack[-1]
        # new_stack = []
        # while popped == min_stack[-1]:
        #     popped = min_stack.pop()
        #     new_stack.append(normal_stack.pop())
        
        # min_value = new_stack.pop()
        # while new_stack:
        #     normal_stack.append(new_stack.pop())
        #     min_stack.append(min_stack[-1])
        
        return min_stack[-1]
        
    def main(operations):
        return_array = []
        normal_stack = []
        min_stack = []
    
        for val in operations:
            if val == -1:
                if normal_stack:
                    pop(min_stack, normal_stack)
            elif val == 0:
                if not min_stack:
                    min_val = -1
                else:
                    min_val = min_pop(min_stack, normal_stack)
                return_array.append(min_val)
            elif val >= 1:
                append(val, min_stack, normal_stack)
                
            # print(f"val: {val}, min_stack: {min_stack}, normal_stack: {normal_stack}, return_array: {return_array}")
                
        return return_array
    
    return main(operations)