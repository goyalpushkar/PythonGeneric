'''
Given an array A of size N having distinct elements, the task is to find the next greater element for each element of the array in order of their appearance in the array. If no such element exists, output -1

Input:
The first line of input contains a single integer T denoting the number of test cases.Then T test cases follow. Each test case consists of two lines. The first line contains an integer N denoting the size of the array. The Second line of each test case contains N space separated positive integers denoting the values/elements in the array A.

Output:
For each test case, print in a new line, the next greater element for each array element separated by space in order.

Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= Ai <= 1018
Example:
Input
2
4
1 3 2 4
4
4 3 2 1
Output
3 4 4 -1
-1 -1 -1 -1

Explanation:
Testcase1: In the array, the next larger element to 1 is 3 , 3 is 4 , 2 is 4 and for 4 ? since it doesn't exist hence -1.
'''

from collections import deque
def next_larger_elem_wrong(arr_elem):
    larger_elem = []  # Stack()
    ret_arr = []
    for index in range(len(arr_elem)):
        if index == len(arr_elem) - 1:
            larger_elem.append(-1)
            break

        if index < len(arr_elem):
            if arr_elem[index] < arr_elem[index + 1]:
                larger_elem.append(index + 1)
            else:
                larger_elem.append(-2)

    print(larger_elem)
    for index in range(len(larger_elem) - 1, -1, -1):
        #curr_elem = index
        #print("index: " + str(index) + " - " + "current_elem: " + str(curr_elem) )
        if index == len(larger_elem) - 1:
            ret_arr.append(-1)
        else:
            if larger_elem[index] == -2:
                if arr_elem[index] < arr_elem[previous_elem]:
                    ret_arr.append(arr_elem[previous_elem])
                else:
                    ret_arr.append(-1)
            else:
                ret_arr.append(arr_elem[larger_elem[index]])

        if larger_elem[index] != -2:
            previous_elem = larger_elem[index]
        #print("previous _elem: " + str(previous_elem))

    ret_arr.reverse()
    return " ".join(map(str, ret_arr))

def next_larger_elem(arr_elem):
    larger_elem = deque()
    larger_elem_map = {}
    ret_arr = []

    larger_elem.append(0)   #Append indexes
    for index in range(1, len(arr_elem)):
        next_elem = index

        last_elem = larger_elem.pop()

        while arr_elem[next_elem] > arr_elem[last_elem]:
            larger_elem_map[last_elem] = next_elem
            if len(larger_elem) <= 0:
                break
            last_elem = larger_elem.pop()

        if arr_elem[next_elem] < arr_elem[last_elem]:
            larger_elem.append(last_elem)

        larger_elem.append(next_elem)

    while len(larger_elem) > 0:
        larger_elem_map[larger_elem.pop()] = -1

    print(larger_elem_map)
    for key in sorted(larger_elem_map.keys()):
        print(key)
        if key == len(arr_elem)-1 or larger_elem_map[key] == -1:
            ret_arr.append(-1)
        else:
            ret_arr.append(arr_elem[larger_elem_map[key]])

    return " ".join(map(str, ret_arr))

'''prints element and NGE pair for all elements of 
   arr[] '''
def createStack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack) == 0

def push(stack, x):
    stack.append(x)

def pop(stack):
    if isEmpty(stack):
        print("Error : stack underflow")
    else:
        return stack.pop()

def printNGE(arr):
    s = createStack()
    element = 0
    next = 0

    # push the first element to stack
    push(s, arr[0])

    # iterate for rest of the elements
    for i in range(1, len(arr), 1):
        next = arr[i]

        if isEmpty(s) == False:

            # if stack is not empty, then pop an element from stack
            element = pop(s)

            '''If the popped element is smaller than next, then 
                a) print the pair 
                b) keep popping while elements are smaller and 
                   stack is not empty '''
            while element < next:
                print(str(element) + " -- " + str(next))
                if isEmpty(s) == True:
                    break
                element = pop(s)

            '''If element is greater than next, then push 
               the element back '''
            if element > next:
                push(s, element)

        '''push next to stack so that we can find 
           next greater for it '''
        push(s, next)

    '''After iterating over the loop, the remaining 
       elements in stack do not have the next greater 
       element, so print -1 for them '''

    while isEmpty(s) == False:
        element = pop(s)
        next = -1
        print(str(element) + " -- " + str(next))

if __name__ == '__main__':
    test_cases = int(input("No of test cases: "))
    for index in range(test_cases):
        size_arr = int(input("Array Length: "))
        arr_elem = list(map(int, input("Array: ").rstrip().split()))

        arr_return = next_larger_elem(arr_elem)
        print(arr_return)

        #printNGE(arr_elem)