'''
Given n ropes of different lengths represented by an array of integers, connect them all into a single rope in a way
that minimizes the cost of connecting them.
The cost of connecting two ropes is equal to the sum of their lengths. We want to minimize the cost of connecting
all the ropes.

Input: ropes, [Integer]
Output: Integer

Example
In: [4, 3, 2, 6]
Out: 29

Explanation:

First we connect 3 + 2 = 5, giving the following ropes: [4,5,6]
Then we connect 5 + 4 = 9, giving the following ropes: [9,6]
Then we connect 9 + 6 = 15, giving the final combination of all ropes: [15]

So in total the cost for the most efficient approach is: 5 + 9 + 15 = 29

A less efficient way would be:

First we connect 4 + 6 = 10, giving the following ropes: [10,3,2]
Then we connect 10 + 3 = 13, giving the following ropes: [13,2]
Then we connect 13 + 2 = 15, giving the final combination of all ropes: [15]

So in total the cost for the less efficient approach is: 10 + 13 + 15 = 38

Although in both cases we need to make the same number of connections, the costs are different

Constraints
Intermediate:
Time Complexity: O(N log N)
Auxiliary Space Complexity: O(N)

Advanced:
Time Complexity: O(N log N)
Auxiliary Space Complexity: O(1)

N = # of Ropes

Input will always contain positive integers.

'''
import atexit
import io
import sys
import heapq
from collections import defaultdict

import math

class Solution:
    # Function to return the minimum cost of connecting the ropes.
    def minCost_predefined(self, arr, n):
        heapq.heapify(arr)
        print(f"minCost_predefined-heapify arr: {arr}")
        running_sum = 0
        while len(arr) != 1:
            elem1 = heapq.heappop(arr)
            elem2 = heapq.heappop(arr)
            new_elem = elem1 + elem2
            running_sum += new_elem
            heapq.heappush(arr, new_elem)

        return running_sum


    def minCost(self, arr, n):
        self.heapify(arr)
        print(f"minCost-heapify arr: {arr}")
        final_val = self.sortify(arr)
        print(f"minCost-Sortify arr: {arr}")

        return final_val

        # aggregate_sum = 0
        # index = len(arr)-1
        # # for index in range(len(arr), -1, -1):
        # while index > 0:
        #     new_sum = arr[index] + arr[index-1]
        #     arr[index-1] = new_sum
        #     aggregate_sum += new_sum
        #     print(f"{index}:: aggregate_sum:{aggregate_sum}\n"
        #           f"arr: {arr}")
        #     index -= 1
        #
        # return aggregate_sum

    # 251/281 - Time Limit Exceeded -
    # In both ways
    def sortify(self, arr):

        index = len(arr)-1
        curr_index = 1
        old_elem = None
        aggregate_sum = 0
        new_elem = 0
        while index > 0:
            # Get the min value from top and add to the last, move last value to 0 position
            old_elem = arr[0]
            arr[index], arr[0] = arr[0], arr[index]
            self.bubble_down(arr,0,index)
            index -= 1

            new_elem = old_elem + arr[0]
            aggregate_sum += new_elem

            arr[0] = new_elem
            self.bubble_down(arr, 0, index)

            # if curr_index != 0 and curr_index % 2 == 0:
            #     new_elem = arr[index] + arr[index+1]
            #     aggregate_sum += new_elem
            #     arr[index] = new_elem
            #     self.bubble_up(arr, index)
            # else:
            #     index -= 1
            #
            print(f"minCost-sortify {index}-{curr_index}: arr: {arr}\n"
                  f"new_elem: {new_elem} \taggregate_sum: {aggregate_sum}")
            #
            # curr_index += 1

        return aggregate_sum

    def heapify(self, arr):
        index = len(arr)
        while index >= 0:
            self.bubble_down(arr, index)
            index -= 1

    def bubble_down(self, arr, index, limit_end=None):
        if limit_end is None:
            limit_end = len(arr)

        while index < limit_end:
            child = self.get_child(arr, index, limit_end)
            if child < limit_end and arr[child] < arr[index]:
                arr[child], arr[index] = arr[index], arr[child]
            else:
                break

            index = child

    def bubble_up(self, arr, index):
        while index > 0:
            parent = math.floor((index-1)/2)
            if parent >= 0 and arr[parent] > arr[index]:
                arr[parent], arr[index] = arr[index], arr[parent]
            else:
                break

            index = parent

    def get_child(self, arr, index, limit_end=None):
        if limit_end is None:
            limit_end = len(arr)

        child1 = 2 * index + 1
        child2 = 2 * index + 2

        if child1 >= limit_end:
            return child1
        elif child2 >= limit_end:
            return child1
        elif arr[child1] <= arr[child2]:
            return child1
        else:
            return child2

# code here

# {
# Driver Code Starts
# Initial Template for Python 3


# _INPUT_LINES = sys.stdin.read().splitlines()
# input = iter(_INPUT_LINES).__next__
# _OUTPUT_BUFFER = io.StringIO()
# sys.stdout = _OUTPUT_BUFFER

# @atexit.register
# def write():
#     sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input("Enter number of test cases: "))
    for cases in range(test_cases):
        n = int(input("Enter number of elements in Array: "))
        a = list(map(int, input("Enter array elements as space-separated values: ").strip().split()))
        ob = Solution()
        a_copy = a.copy()
        print(f"Predefined Value: {ob.minCost_predefined(a, n)}")
        print(f"Newly Defined Value: {ob.minCost(a_copy, n)}")
# } Driver Code Ends