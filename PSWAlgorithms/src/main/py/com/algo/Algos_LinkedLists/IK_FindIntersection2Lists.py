'''
Given two linked lists, find their intersection if it exists.

Intersection is the node where the two lists merge, the first node that belongs to both lists.

Example
Example

Output:

4
The lists intersect in node 4.

Notes
Return the value of the intersection node or -1 if no intersection exists.
Constraints:

0 <= values in the list nodes <= 109
0 <= number of nodes in a list <= 105
Description of the text format of the test cases

You might need this for debugging your solution on IK UpLevel platform.

The value called merge_index in the input file represents the index in the first list where the second list is attached. Value 0 simply means that lists don't intersect.

For example,

{
"l1": [1, 2, 3, 4, 7, 8, 9],
"l2": [5, 6],
"merge_index": 3
}
is the representation of the Example given above: Example
'''

# For your reference:
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

# IK approach
# Get size of both LinkedLists
# The number of elements more in bigger list will not be common so traverse bigger list for number of more elements
# traverse bot lists and compare the values if equal that is merge point else -1

# Mine approach - creating extra space
def find_intersection(l1, l2):
    """
    Args:
    l1(LinkedListNode_int32)
    l2(LinkedListNode_int32)
    Returns:
    int32
    """
    # Write your code here.
    arr1 = []
    arr2 = []
    
    if l1 is None or l2 is None:
        return -1
        
    # traverse first list and store nodes in an array
    curr = l1
    while curr:
        arr1.append(curr)
        curr = curr.next
        
    # traverse second list and store nodes in an array
    curr = l2
    while curr:
        arr2.append(curr)
        curr = curr.next
    
    # print(arr1, arr2)
    # if last element itself is not equal that means not intersected
    if arr1[-1] != arr2[-1]:
        return -1
        
    # print(arr1, arr2)
    # compare nodes of both the arrays 1 by 1
    min_len = min(len(arr1), len(arr2))
    len_arr1 = len(arr1)-1
    len_arr2 = len(arr2)-1

    return_elem = -1
    index = 0
    # print(f"min_len: {min_len}")
    # for i in range(min_len-1, -1, -1):
    while index < min_len:
        # print(arr1[len_arr1-index].value, arr2[len_arr2-index].value)
        if arr1[len_arr1-index] != arr2[len_arr2-index]:
            return return_elem
        else:
            return_elem = arr1[len_arr1-index].value
            
        index += 1
        
    return return_elem
        