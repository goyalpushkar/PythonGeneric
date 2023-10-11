'''
Given a list of numbers, sort it using the Counting Sort algorithm.

Example
{
"arr": [5, 8, 3, 9, 4, 1, 7]
}
Output:

[1, 3, 4, 5, 7, 8, 9]
Notes
Constraints:

1 <= length of the given list <= 4 * 105
-4 * 105 <= number in the list <= 4 * 105
'''

'''

{
"arr": [-5, -3, -1, 0, 1, 3, 5]
}

{
"arr": [5, 3, 1, -10, -11, -100]
}


'''


def counting_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    # internal_deque = deque()
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

# n - number of elements, m - range of elements
# O (n + m)
def counting_sort_2(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    elem_map = {}
    min_elem = arr[0]
    max_elem = arr[0]
    for elem in arr:
        if elem in elem_map:
            elem_map[elem] += 1
        else:
            elem_map[elem] = 1

        min_elem = min(min_elem, elem)
        max_elem = max(max_elem, elem)

    # print(elem_map, min_elem, max_elem)
    arr_index = 0
    for i in range(min_elem, max_elem + 1):

        while i in elem_map and elem_map[i] > 0:
            arr[arr_index] = i
            arr_index += 1
            elem_map[i] -= 1

    return arr