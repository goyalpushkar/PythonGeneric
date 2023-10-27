'''
Given a list of characters, sort it in the non-decreasing order based on ASCII values of characters.

Example
{
"arr": ["a", "s", "d", "f", "g", "*", "&", "!", "z", "y"]
}
Output:

["!", "&", "*", "a", "d", "f", "g", "s", "y", "z"]
Notes
Constraints:

1 <= length of the list <= 100000
Input list consists of alphanumeric characters and these ones: !, @, #, $, %, ^, &, *, (, ).
'''
def sort_array(arr):
    """
    Args:
     arr(list_char)
    Returns:
     list_char
    """
    # Write your code here.
    # Way 1 - O(NlogN)
    # Loop over list and get their ascii chars - N
    # Sort the ascii char list - N Log N
    # Loop over list and revert the ascii to char
    for index in range(len(arr)):
        arr[index] = ord(arr[index])

    arr = sorted(arr)

    for index in range(len(arr)):
        arr[index] = chr(arr[index])

    return arr

    # Way 2 -
    # Count Sort - O(N)
    # Take empty array of 128 chars - Ascii values
    # Get ascii value of each character and update count for the ascii value in new array
    # Loop over ascii array to get values
    ascii_arr = [0] * 128
    return_arr = []
    for index in range(len(arr)):
        ascii_arr[ord(arr[index])] += 1

    for index in range(len(count_sort)):
        # print(pow(index, 2), count_sort[index], [pow(index, 2)] * count_sort[index])
        return_arr.extend([pow(index, 2)] * count_sort[index])

    return return_arr

