'''
Given an unsorted array of integers, return the array sorted using heapsort. The heapsort Algorithm must be performed in
place without using extra space (outside of the call stack)

Input/Output
Input - Arra of integers
Output - Array of integers

heapsort([4,15,16,50,8,23,42,108])
 -> [4,8,15,16,23,42,50,108]

 Heapsort can be performed by transforming your array into a max heap and thn using the properties of a max heap to
 transform your max heap into a sorted array. How can we do this in-place? Consider implementing and using any of the
 following functions:
    bubbledown (Swapping parents with their children in order o maintain heap conditions)
    getChild (calculate and return a relevant child index based on a given parent index in an array-based heap)
    bubbleUp (Swapping children with their parents in order to maintain the heap conditions)

Parent child relationhips -
    child1 - 2*Parent + 1
    child2 - 2*Parent + 2
    parent - floor(child-1/2)


                                   4 (0)
                            /                \
                          15 (1)             16 (2)
                       /       \           /       \
                    50 (3)     8 (4)      23 (5)   42 (6)
                   /
                108 (7)
'''
import math

def heapsort(arr):
    # Write your code here

    # first hepify the array - i.e. make it max heap
    heapify(arr)
    print(f"Heapify arr; {arr}")

    # sort the max heap
    sortify(arr)
    print(f"Sortify arr; {arr}")

    return arr


# Option 1 - Bubble Down from Top - Does not work as logic does not make sense once top element settles down
# Option 2 - Bubble Up from last element - keep doing from same index until element at that index does not move up anymore
#            Need multiple bubble up calls at the same index
# option 3 - Bubble down from last element - easiest and simple logic to ensure all previous elements are max heap
#           It is O(N) and takes advantage of the fact that a compact array = complete binary tree and all leaves
#           i.e., half of the vertices are Binary Max Heap by default
#           Need one call of bubble down at each index
def heapify(arr):
    index = len(arr) - 1
    # Start from last index and bubble down elements till 0th index
    # it uses the fact that leaves are already max heap as they don't have any child
    while index >= 0:
        bubble_down(arr, index)
        print(f"index: {index}\tarr: {arr}")
        index -= 1

    # return arr

# 108 50 42 15 8 23 16 4
#      4 50 42 15 8 23 16 108 -> 50 4 42 15 8 23 16 108 -> 50 15 42 4 8 23 16 108
#      16 15 42 4 8 23 50 108 -> 42 15 16 4 8 23 50 108 -> 42 15 23 4 8 16 50 108
#      16 15 23 4 8 42 50 108 -> 23 15 16 4 8 42 50 108
#      8 15 16 4 23 42 50 108 -> 16 15 8 4 23 42 50 108
#      4 15 8 16 23 42 50 108 -> 15 4 8 16 23 42 50 108
#      8 4 15 16 23 42 50 108
#      4 8 15 16 23 42 50 108
def sortify(arr):
    index = len(arr) - 1
    while index >= 0:
        arr[index], arr[0] = arr[0], arr[index]
        bubble_down(arr, 0, index)  # Pass end limit which is excluded for consideration
        print(f"index: {index}\tarr: {arr}")
        index -= 1

    # return arr

'''
  index         Child index
    0           1, 2
    1           3, 4
    2           5, 6
    3           7, 8
    4           9, 10
    child - 2*p+1, 2*p+2
'''
def get_child(arr, index, limit_end=None):
    if limit_end is None:
        limit_end = len(arr)

    # Get Child indexes
    child1 = (2 * index) + 1
    child2 = (2 * index) + 2

    # If first child itself is out of bound then return it and handle out of bound in calling place
    if child1 >= limit_end:
        return child1

    # if second child is out of bound then return first child (as it is not out of bound based on first if)
    # and it will be handled accordingly
    elif child2 >= limit_end:
        return child1

    # If it is max heap then check if first child value is greater than second child value then return first child
    # else return second child
    elif arr[child1] >= arr[child2]:
        return child1
    else:
        return child2

# O(Log N)
def bubble_down(arr, index, limit_end=None):
    if limit_end is None:
        limit_end = len(arr)

    # Keep running loop until index is in bounds - index will increase only
    while index < limit_end:
        child = get_child(arr, index, limit_end)

        # verify child is in bound and child is greater than parent then swap child with parent if not then return as it is
        if child < limit_end and arr[child] > arr[index]:
            arr[index], arr[child] = arr[child], arr[index]
        else:
            break
        index = child

    # return arr

# O(Log N)
def bubble_up(arr, index):

    # Keep running loop until index is in bounds - index will decrease
    while index > 0 and index < len(arr):
        parent = math.floor((index-1)/2)

        # Check if parent is less than current value than swap
        if index > 0 and arr[parent] < arr[index]:
            arr[parent], arr[index] = arr[index], arr[parent]
        else:
            break

        index = parent

    # return arr

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # arr_count = int(input("Enter Array Count: ").strip())
    # arr = []
    # for _ in range(arr_count):
    #     arr_item = int(input("Enter Array element: ").strip())
    #     arr.appendpend(arr_item)
    # arr = [4, 15, 16, 50, 8, 23, 42, 108] -[108, 50, 42, 15, 8, 23, 16, 4] - [4, 8, 15, 16, 23, 42, 50, 108]
    arr = [9,5,2,3,7,23,5,8,111,-4,-20] # - [111,9,23,5,7,2,5,8,-4,-20] - [-4, -20]
    result = heapsort(arr)
    print(f"result: {result}\n")
    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()