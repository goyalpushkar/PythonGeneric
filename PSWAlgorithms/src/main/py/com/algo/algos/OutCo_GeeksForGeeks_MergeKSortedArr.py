'''
Given an array of sorted arrays of numbers, return the result of merging all those sorted arrays into a single sorted array

Input: arrays , Array of Arrays of Ints, [[Int]]
Output: [Int]

Example
Input:
[
[1, 10, 11, 15],
[2, 4,  9,  14],
[5, 6,  8,  16],
[3, 7,  12, 13]
]

Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

Constraints
Basic:

Time Complexity: O(N K log NK)
Auxiliary Space Complexity: O(NK)

Advanced:

Time Complexity: O(N K log K)
Auxiliary Space Complexity: O(NK)

K = # of Arrays
N = Avg. Length of Arrays

Arrays do not necessarily need to be the same length.

Inputs will always be integers, and sorted.

https://www.geeksforgeeks.org/merge-k-sorted-arrays/

'''
import heapq
import math

class Solution:
    #Function to merge k sorted arrays.
    # (nk log nk)
    def mergeKArrays(self, arr, K):
        # code here
        # return merged list
        final_arr = []
        for row in arr:
            for val in row:
                final_arr.append(val)

        final_arr = sorted(final_arr)

        return final_arr

    def mergeKArrays_advanced(self, arr, K):
        # code here
        final_arr = []

        # Prepare Heap with first element from each of the k arrays
        user_heap = MinHeap()
        for index in range(K):
            user_heap.insert_elem(arr[index][0], index, 0)

        user_heap.print_values()
        user_heap.print_complete()

        while len(user_heap) > 0:
            min_elem = user_heap.pop()
            outer = min_elem.out_position
            inner = min_elem.inner_position

            print(f"min_elem: {min_elem.val}")
            final_arr.append(min_elem.val)
            user_heap.print_values()

            if inner < len(arr[outer])-1:
                inner += 1
                new_elem = arr[outer][inner]
                print(f"new_elem: {new_elem}")
                user_heap.insert_elem(new_elem, outer, inner)

            print(f"final_arr: {final_arr}")
            user_heap.print_values()

        return final_arr

class HeapNode:
    def __init__(self, value, out_pos, in_pos):
        self.val = value
        self.out_position = out_pos
        self.inner_position = in_pos

class MinHeap:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def get_child(self, index):
        child1 = 2 * index + 1
        child2 = 2 * index + 2

        if child1 >= len(self.heap) or child2 >= len(self.heap):
            return child1
        elif self.heap[child1].val <= self.heap[child2].val:
            return child1
        else:
            return child2

    def bubble_down(self, index, limit=None):
        if limit is None:
            limit = len(self.heap)

        child = self.get_child(index)
        while child < len(self.heap) and self.heap[child].val < self.heap[index].val:
            self.heap[child], self.heap[index] = self.heap[index], self.heap[child]
            index = child
            child = self.get_child(index)

    def bubble_up(self, index, limit=None):
        if limit is None:
            limit = len(self.heap)

        parent = math.floor((index-1)/2)
        while parent >= 0 and self.heap[parent].val > self.heap[index].val:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
            parent = math.floor((index-1)/2)

    def insert_elem(self, value, out_pos, in_pos):
        node = HeapNode(value, out_pos, in_pos)
        self.heap.append(node)
        # self.heapify()
        self.bubble_up(len(self.heap)-1)
        self.print_values()

    def heapify(self):
        index = len(self.heap)
        while index >=0:
            self.bubble_down(index)
            index -= 1

    def pop(self):
        elem = self.heap[0]
        self.heap[0], self.heap[len(self.heap)-1] = self.heap[len(self.heap)-1], self.heap[0]
        self.heap = self.heap[:-1]
        self.bubble_down(0)
        return elem

    def print_values(self):
        for elem in self.heap:
            print(elem.val,end=' ')
        print("\n")

    def print_complete(self):
        for elem in self.heap:
            print(f"Value:{elem.val} - Outer:{elem.out_position} - Inner:{elem.inner_position}")
        print("\n")

#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t=int(input("Enter number of test cases: "))
    for _ in range(t):
        n=int(input("Enter k as number of arrays: "))
        numbers=[[ 0 for _ in range(n) ] for _ in range(n) ]
        line=input("Enter elements as space separated values: ").strip().split()
        for i in range(n):
            for j in range(n):
                numbers[i][j]=int(line[i*n+j])
        # numbers = [[27, 41, 51, 100], [120, 307, 690, 3000], [30, 31, 83, 100], [3, 24, 36, 68]]
        # 27 41 51 100 120 307 690 3000 30 31 83 100 3 24 36 68
        #     # [[1,2,3], [4,5,6], [7,8,9]] # 1,2,3, 4,5,6,7,8,9
            # [[57, 81],[63, 71]]
        ob = Solution();
        merged_list=ob.mergeKArrays(numbers, n)
        for i in merged_list:
            print(i,end=' ')
        print()

        merged_list = ob.mergeKArrays_advanced(numbers, n)
        for i in merged_list:
            print(i,end=' ')
        print()
# } Driver Code Ends

