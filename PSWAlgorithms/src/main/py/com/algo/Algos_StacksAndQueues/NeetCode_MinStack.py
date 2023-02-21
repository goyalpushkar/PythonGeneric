'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.



Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2


Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.

'''

import heapq
from collections import deque
import math

class MinStack:

    def __init__(self):
        self.deque = []

        # min elem has problem with pop element if min element is removed how to find next min elem to set in min_elem
        # self.min_elem = -math.inf

        # min heap has problem with pop element like how to remove element from heap if it is not min element
        # instead of creating min heap create another array in that array
        # either push value in each push-call but save only min value till now in the array
        # or save only if pushed value is less than the current value in the array. In this case pop will hppen from min_heap
        # only if pop value from normal array is same as min value in min_heap
        self.min_heap = []
        # heapq(self.min_heap)

    def push(self, val):
        self.deque.append(val)
        new_val = min(val, self.min_heap[-1]) if self.min_heap else val
        self.min_heap.append(new_val)
        # self.min_elem = min(self.min_elem, val)
        # heapq.heappush(self.min_heap, val)

    def pop(self):
        elem = self.deque.pop()   # self.deque[-1]   #
        self.min_heap.pop()
        # heapq.heappop(self.min_heap)
        # self.deque = self.deque[:-1]
        return elem

    def top(self):
        return self.deque[-1]

    def getMin(self):
        return self.min_heap[-1] # min(self.deque)  # self.min_elem # heapq.heappop(self.min_heap)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()