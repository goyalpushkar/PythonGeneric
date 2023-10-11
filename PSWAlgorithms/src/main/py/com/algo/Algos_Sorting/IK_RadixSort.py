'''
Given a list of numbers, sort it using the Radix Sort algorithm.

Example
{
"arr": [5, 8, 3, 9, 4, 1, 7]
}
Output:

[1, 3, 4, 5, 7, 8, 9]
Notes
Constraints:

1 <= length of the given list <= 4 * 105
0 <= number in the list <= 109
'''

# In Each digit loop (max_digits), elements can be moved from buckets array
# to original array then for index in range(20): can be removed
def radix_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    count_arr_odd = [deque() for _ in range(20)]
    count_arr_even = [deque() for _ in range(20)]
    return_arr = []

    max_num = max(arr, key=abs)
    max_digits = len(str(max_num))
    # print(max_num, max_digits)

    def derive_value(val, divide_by, empty_arr):
        # current_digit in the number
        num = (val // divide_by) % 10
        # print(num, divide_by)
        if val >= 0:
            empty_arr[num + 10].append(val)
        else:
            empty_arr[abs(num)].append(val)  # 10-abs(num)

    def insert_vals(index, i, filled_arr, empty_arr):
        divide_by = pow(10, i)

        if i == 0:
            # if there are elements at the current index
            for val in filled_arr:
                derive_value(val, divide_by, empty_arr)

        else:
            # if there are elements at the current index
            for j_index in range(len(filled_arr[index])):
                val = filled_arr[index].popleft()

                # current_digit in the number
                derive_value(val, divide_by, empty_arr)

    def fill_array(count_arr):
        nonlocal return_arr

        # loop over values in the array:
        for index in range(20):
            # get elements from count_array and insert into return array
            for j_index in range(len(count_arr[index])):
                # print(j_index, count_arr[index])
                val = count_arr[index].popleft()
                return_arr.append(val)

    # print(return_arr, max_num, len(str(max_num)))
    # Loop for number of digits
    for i in range(max_digits):

        if i == 0:
            insert_vals(0, i, arr, count_arr_odd)
        else:
            # loop over values in the array:
            for index in range(20):

                if i % 2 == 0:
                    insert_vals(index, i, count_arr_even, count_arr_odd)
                else:
                    insert_vals(index, i, count_arr_odd, count_arr_even)

        # print(i, count_arr_odd)
        # print(i, count_arr_even)

    if max_digits % 2 == 0:
        fill_array(count_arr_even)
    else:
        fill_array(count_arr_odd)

    return return_arr