'''
Given an array of integers, find the k-th largest number in it.

Example One
{
"numbers": [5, 1, 10, 3, 2],
"k": 2
}
Output:

5
Example Two
{
"numbers": [4, 1, 2, 2, 3],
"k": 4
}
Output:

2
Notes
Constraints:

1 <= array size <= 3 * 105
-109 <= array elements <= 109
1 <= k <= array size
'''
def kth_largest_in_an_array(numbers, k):
    """
    Args:
    numbers(list_int32)
    k(int32)
    Returns:
    int32
    """
    import heapq
    # Write your code here.
    # Simple approach - Sort and then get the kth element from sorted list - O(N log N)
    sorted_list = sorted(numbers)
    # print(sorted_list)
    n = len(sorted_list)
    for idx in range(n, -1, -1):
        if n-1-idx == k-1:
            return sorted_list[idx]
    
    # Heap approach - Create a heap 
    # 1
    max_heap = []
    for num in numbers:
        heapq.heappush(max_heap, -1*num)
    
    while k != 0:
        # print(max_heap, k-1)
        elem = heapq.heappop(max_heap)
        k -= 1
    
    return -1*elem

    # enumerate will not work on heap as elements are getting popped enumerate will finish as initial last element is popped
    # for idx, _ in enumerate(max_heap):
    #     print(max_heap,idx, k-1)
    #     elem = heapq.heappop(max_heap)
    #     print(elem)
    #     if idx == k-1:
    #       return -1*elem

    # 2 maintain only k elements in the heap O(k + (n-k) log k)
    # k element min heap of larger elements and return the top element from the heap. if k is small then use min heap
    # n-k+1 elements max heap of smaller elements and return the top element from the heap. if k is large then use max heap
    import heapq
    min_heap = []
    idx = 0
    while idx < k:
        heapq.heappush(min_heap, numbers[idx])
        idx += 1
    
    # print(min_heap)
    while idx < len(numbers):
        if numbers[idx] >= min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, numbers[idx])
        idx += 1
    
    # print(min_heap)
    
    return heapq.heappop(min_heap)

    # 3
    # heapq.heapify(numbers) # This will not sort the numbers. it will just place the numbers with minimum on top
    # print(numbers)
    # for idx in range(len(numbers), -1, -1):
    #     if idx == k-1:
    #         return numbers[idx]

    # return None