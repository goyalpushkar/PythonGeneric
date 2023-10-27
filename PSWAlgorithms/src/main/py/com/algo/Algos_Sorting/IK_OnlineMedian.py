'''
Given a list of numbers, the task is to insert these numbers into a stream and find the median of the stream after each insertion. 
If the median is a non-integer, consider it’s floor value.

The median of a sorted array is defined as the middle element when the number of elements is odd and the mean of the middle two elements when the number of 
elements is even.

Example
{
"stream": [3, 8, 5, 2]
}
Output:

[3, 5, 5, 4]
Iteration	Stream	Sorted Stream	Median
1	[3]	[3]	3
2	[3, 8]	[3, 8]	(3 + 8) / 2 => 5
3	[3, 8, 5]	[3, 5, 8]	5
4	[3, 8, 5, 2]	[2, 3, 5, 8]	(3 + 5) / 2 => 4
Notes
Constraints:

1 <= length of stream <= 105
1 <= any value in the stream <= 105
The stream can contain duplicates.
'''
def online_median(stream):
    """
    Args:
    stream(list_int32)
    Returns:
    list_int32
    """
    # Write your code here.
    import heapq
    
    max_heap = []   # will have all smaller elements
    min_heap = []   # will have all larger elements
    return_means = []
    
    for idx, elem in enumerate(stream):
        
        # Insert elements into min and max heaps
        if len(max_heap) <= len(min_heap):
            # print(f"min heap top: {min_heap[0] if min_heap else None}")
            if min_heap and elem > min_heap[0]:
                popped_elem = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -1*popped_elem)
                heapq.heappush(min_heap, elem)
            else:
                heapq.heappush(max_heap, -1*elem)
        else:
            # print(f"max heap top: {max_heap[0]}")
            if max_heap and elem < -1*max_heap[0]:
                popped_elem = -1*heapq.heappop(max_heap)
                heapq.heappush(min_heap, popped_elem)
                heapq.heappush(max_heap, -1*elem)
            else:
                heapq.heappush(min_heap, elem)
            
        # print(f"max_heap: {max_heap}, min_heap: {min_heap}")
        # Calculate means
        if len(max_heap) == len(min_heap):
            curr_mean = (-1*max_heap[0] + min_heap[0]) // 2
        else:
            curr_mean = -1*max_heap[0]
        
        return_means.append(curr_mean)
    
    
    return return_means
