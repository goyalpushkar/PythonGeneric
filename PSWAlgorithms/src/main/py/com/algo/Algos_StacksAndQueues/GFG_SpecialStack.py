'''

Design a data-structure SpecialStack that supports all the stack operations like push(), pop(), isEmpty(), isFull() and an additional operation getMin() which should return minimum element from the SpecialStack. Your task is to complete all the functions, using stack data-Structure.

Input Format:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains two lines. The first line of input contains an integer n denoting the number of integers in a sequence. In the second line are n space separated integers of the stack.

Output Format:
For each testcase, in a new line, print the minimum integer from the stack.

Your Task:
Since this is a function problem, you don't need to take inputs. You just have to complete 5 functions, push() which takes an integer x as input and pushes it into the stack; pop() which pops out the topmost element from the stack; isEmpty() which returns true/false depending upon whether the stack is empty or not; isFull() which takes the size of the stack as input and returns true/false depending upon whether the stack is full or not (depending upon the given size); getMin() which returns the minimum element of the stack.

Expected Time Complexity: O(1) for all the 5 functions.
Expected Auxiliary Space: O(1) for all the 5 functions.

Constraints:
1 <= T <= 100
1 <= N <= 100

Example:
Input:
1
5
18 19 29 15 16
Output:
15
'''

# Your task is to complete all these function's
# function should append an element on to the stack
import heapq
def push(arr, ele):
    # Code here
    arr.append(ele)

# Function should pop an element from stack
def pop(arr):
    # Code here
    arr.pop()

# function should return 1/0 or True/False
def isFull(n, arr):
    # Code here
    return len(arr) == n

# function should return 1/0 or True/False
def isEmpty(arr):
    #Code here
    return len(arr) == 0

# function should return minimum element from the stack
def getMin(n, arr):
    # Code here
    arr_copy = arr
    heapq.heapify(arr_copy)
    return heapq.heappop(arr_copy)

if __name__ == '__main__':
    t = int(input("No of test cases: "))
    for index in range(t):
        n = int(input("No of elements: "))
        arr = list(map(int,input().strip().split()))
        stack = []
        for i in range(n):
            push(stack, arr[i])

        print(getMin(n, stack))

