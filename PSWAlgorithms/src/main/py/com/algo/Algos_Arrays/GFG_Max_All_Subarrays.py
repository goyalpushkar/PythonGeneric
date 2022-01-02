'''
Given an array A and an integer K. Find the maximum for each and every contiguous subarray of size K.

Input:
The first line of input contains an integer T denoting the number of test cases. The first line of each test case contains a single integer N denoting the size of array and the size of subarray K. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output:
Print the maximum for every subarray of size k.

Constraints:
1 ≤ T ≤ 200
1 ≤ N ≤ 107
1 ≤ K ≤ N
0 ≤ A[i] <= 107

Example:
Input:
2
9 3
1 2 3 1 4 5 2 3 6
10 4
8 5 10 7 9 4 15 12 90 13

Output:
3 3 4 5 5 5 6
10 10 10 15 15 90 90

Explanation:
Testcase 1: Starting from first subarray of size k = 3, we have 3 as maximum. Moving the window forward, maximum element are as 3, 4, 5, 5, 5 and 6.
'''

import queue
from collections import deque


def max_all_subarrays_wrongoutput(arr, sub_array_size):
    max_elems_arr = ""
    queue_elem = queue.Queue(0)

    max_elem = 0
    for elem in range(len(arr)):
        queue_elem.put(arr[elem])
        if max_elem < arr[elem]:
            max_elem = arr[elem]

        if queue_elem.qsize() == sub_array_size:
            max_elems_arr += str(max_elem) + " "
            queue_elem.get()

    return max_elems_arr

def max_all_subarrays(arr, sub_array_size):
    queue_elem = deque()
    max_elems_arr = ""

    for elem in range(len(arr)):

        index = 0
        while index < len(queue_elem):
            if arr[queue_elem[index]] < arr[elem]:
                queue_elem.pop()
            else:
                index += 1

        queue_elem.append(elem)

        if elem - sub_array_size == queue_elem[0]:
            queue_elem.popleft()

        if elem + 1 >= sub_array_size:
            max_elems_arr += str(arr[queue_elem[0]]) + " "

    return max_elems_arr

if __name__ == '__main__':
    test_cases = int(input())

    for tests in range(test_cases):
        arr_size, sub_array_size = map(int, input().rstrip().split())
        arr = list(map(int, input().rstrip().split()))

        max_elems = max_all_subarrays(arr, sub_array_size)

        print(max_elems)