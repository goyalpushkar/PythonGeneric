'''
Given an integer array and a number k, find the k most frequent elements in the array.

Example One
{
"arr": [1, 2, 3, 2, 4, 3, 1],
"k": 2
}
Output:
[3, 1]

Example Two
{
"arr": [1, 2, 1, 2, 3, 1],
"k": 1
}
Output:
[1]

Notes
If multiple answers exist, return any.
The order of numbers in the output array does not matter.
Constraints:
1 <= length of the given array <= 3 * 105
0 <= array element <= 3 * 105
1 <= k <= number of unique elements in the array
'''
from collections import Counter
import heapq

# T - O(n log n), S - O(n)
def find_top_k_frequent_elements(arr, k):
    """
    Args:
     arr(list_int32)
     k(int32)
    Returns:
     list_int32
    """
    # Write your code here.
    key_val = {}
    for elem in arr:
        if elem in key_val:
            key_val[elem] += 1
        else:
            key_val[elem] = 1

    sorted_val = sorted(key_val.items(), key=lambda x: x[1], reverse=True)
    return_arr = []
    for key, value in sorted_val:
        return_arr.append(key)
        if len(return_arr) == k:
            return return_arr

# T - O(n log k), S - O(n+k)
def find_top_k_frequent_elements_heap(arr, k):
    key_val = Counter(arr)
    elem_heap = []
    return_arr = []

    def add_heap(elem):
        heapq.heappush(elem_heap, elem)

        if len(elem_heap) > k:
            heapq.heappop(elem_heap)

        # print(elem_heap)

    def final_elems():
        while len(elem_heap) > 0:
            return_arr.append(heapq.heappop(elem_heap)[1])

    # print(key_val)
    for key, value in key_val.items():
        # print(key, value)
        add_heap([value, key])

    # print(elem_heap)
    final_elems()
    return return_arr

# T - O(n), S - O(n+k)
def find_top_k_frequent_elements_countSort(arr, k):
    key_val = Counter(arr)
    return_arr = []

    count_sort = [[] for _ in range(len(arr)+1)]
    for key, val in key_val.items():
        count_sort[val].append(key)

    for index in range(len(arr), -1, -1):
        if len(count_sort[index]) > 0:
            for elem in count_sort[index]:
                if k > 0:
                    return_arr.append(elem )
                    k -= 1

    return return_arr