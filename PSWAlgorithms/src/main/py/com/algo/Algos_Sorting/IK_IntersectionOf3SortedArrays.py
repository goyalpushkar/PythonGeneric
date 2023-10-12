'''
Given three arrays sorted in the ascending order, return their intersection sorted array in the ascending order.

Example One
{
"arr1": [2, 5, 10],
"arr2": [2, 3, 4, 10],
"arr3": [2, 4, 10]
}
Output:

[2, 10]
Example Two
{
"arr1": [1, 2, 3],
"arr2": [],
"arr3": [2, 2]
}
Output:

[-1]
Example Three
{
"arr1": [1, 2, 2, 2, 9],
"arr2": [1, 1, 2, 2],
"arr3": [1, 1, 1, 2, 2, 2]
}
Output:

[1, 2, 2]
Notes
If the intersection is empty, return an array with one element -1.
Constraints:

0 <= length of each given array <= 105
0 <= any value in a given array <= 2 * 106
'''
def find_intersection(arr1, arr2, arr3):
    """
    Args:
    arr1(list_int32)
    arr2(list_int32)
    arr3(list_int32)
    Returns:
    list_int32
    """
    # Write your code here.
    if len(arr1) == 0 or len(arr2) == 0 or len(arr3) == 0:
        return [-1]
    
    return_arr = []
    
    # n = min(len(arr1), len(arr2), len(arr3))
    l, m, n = len(arr1), len(arr2), len(arr3)
    p1, p2, p3 = 0, 0, 0
    
    # while p1 < n or p2 < n or p3 < n:
    while p1 < l and p2 < m and p3 < n:
        if arr1[p1] != arr2[p2] or arr2[p2] != arr3[p3] or arr1[p1] != arr3[p3]:
            
            # get max value for the current arr
            max_element = max(arr1[p1], arr2[p2], arr3[p3])
            
            while p1 < len(arr1) and arr1[p1] < max_element:
                p1 += 1
            while p2 < len(arr2) and arr2[p2] < max_element:
                p2 += 1
            while p3 < len(arr3) and arr3[p3] < max_element:
                p3 += 1
        
        # print(f"p1: {p1}, p2: {p2}, p3: {p3}, return_arr: {return_arr}")
        
        if p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3) and arr1[p1] == arr2[p2] and arr2[p2] == arr3[p3]:
            return_arr.append(arr1[p1])
            p1 += 1
            p2 += 1
            p3 += 1
        
        # print(f"p1: {p1}, p2: {p2}, p3: {p3}, return_arr: {return_arr}")
        # if p1 >= len(arr1) or p2 >= len(arr2) or p3 >= len(arr3):
        #     return return_arr if return_arr else [-1]
        
    return return_arr if return_arr else [-1]
