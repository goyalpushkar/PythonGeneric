''''
Given an array of integers arr of size n and an integer w, find maximum number in all subarrays of arr of length w.

Imagine that n is very large and a sliding window of a smaller size w is moving through arr from left to right. We need to find the maximum in every position of the sliding window.

Example
{
"arr": [1, 3, -1, -3, 5, 3, 6, 7],
"w": 3
}
Output:

[3, 3, 5, 5, 6, 7]
Size of arr is 8 and so the size of the output array is n - w + 1 = 8 - 3 + 1 = 6.

Here are all the 6 positions of the sliding window and the corresponding maximum values:

[1 3 -1] -3 5 3 6 7. Maximum is 3.
1 [3 -1 -3] 5 3 6 7. Maximum is 3.
1 3 [-1 -3 5] 3 6 7. Maximum is 5.
1 3 -1 [-3 5 3] 6 7. Maximum is 5.
1 3 -1 -3 [5 3 6] 7. Maximum is 6.
1 3 -1 -3 5 [3 6 7]. Maximum is 7.
Notes
Function must return an array of integers of length n - w + 1. i-th value in the returned array must be the maximum among arr[i], arr[i + 1], ..., arr[i + w - 1].
Constraints:

1 <= n <= 105
-2 * 109 <= arr[i] <= 2 * 109
1 <= w <= n
'''
def max_in_sliding_window(arr, w):
    """
    Args:
    arr(list_int32)
    w(int32)
    Returns:
    list_int32
    """
    # Write your code here.
    return_arr = []
    max_elem = deque()
    for i, val in enumerate(arr):
        
        # remove any indices that are smaller than current element 
        # as they will never be max after current element
        while max_elem and arr[max_elem[-1]] < val:
            max_elem.pop()
        
        max_elem.append(i)
        
        # print(f"i: {i}, val: {val}, max_elem:{max_elem}")
        # if window is reached
        if i >= w-1:
            
            # remove any element that is out of window
            if max_elem[0] < i-w+1:
                max_elem.popleft()
            
            return_arr.append(arr[max_elem[0]])
        
    return return_arr


# wrong 33/35
def max_in_sliding_window(arr, w):
    """
    Args:
    arr(list_int32)
    w(int32)
    Returns:
    list_int32
    """
    # Write your code here.
    return_arr = []

    max_elem = []
    for i, val in enumerate(arr):
        if i == 0:
            max_elem.append(i)
            if w == 1:
                return_arr.append(arr[max_elem[-1]])
            continue
        
        # if current value is greater than max value
        if val > arr[max_elem[-1]]:
            max_elem.append(i)
            
        # max value is outside of window range
        # check if previous value or current value is max
        elif max_elem[-1] + w - 1 < i:
            if w > 1:
                if val > arr[i-1]:
                    max_elem.append(i) 
                else: 
                    max_elem.append(i-1) 
            else:
                max_elem.append(i) 
        else:
            max_elem.append(max_elem[-1])
        
        if w-1 <= i:
            return_arr.append(arr[max_elem[i]])
        
    return return_arr

# wrong many failed
def max_in_sliding_window(arr, w):
    """
    Args:
    arr(list_int32)
    w(int32)
    Returns:
    list_int32
    """
    # Write your code here.
    return_arr = []

    k = 0 
    max_elem = []
    for i, val in enumerate(arr):
        max_elem = max(max_elem, val)
        k += 1
        
        if k == w:
            return_arr.append(max_elem)
            k -= 1
        
    
    return return_arr
        