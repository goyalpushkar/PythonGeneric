'''
Given an array of numbers sorted in increasing order, generate another array containing the square
of all the elements in the given array, sorted in increasing order.

Example One
{
"numbers": [1, 2, 3, 4]
}
Output:

[1, 4, 9, 16]
Example Two
{
"numbers": [-9, -5, -2, 0, 3, 7]
}
Output:

[0, 4, 9, 25, 49, 81]
Notes
Constraints:

1 <= size of the input array <= 10^5
-10^4 <= any element of the input array <= 10^4
'''
def generate_sorted_array_of_squares(numbers):
    """
    Args:
     numbers(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.

    # Way 1 - Counting Sort This will work only for smaller size of array
    # misread 10^5 as 105
    # Take an array of 105 elements. Add modulo of number in the array
    # take the elements out of the count sort array and take their square
    count_sort = [0] * 104
    return_arr = []
    for num in numbers:
        count_sort[abs(num)] += 1

    for index, val in enumerate(count_sort):
        return_arr.extend(pow(count_sort[index], 2) * val)

    return return_arr

    # Way 2 -
    # Find the position in the array where -ve to +ve happens - O(N)
    # Merge left and right side of above element into a new array using abs value
    # above will be a sorted array convert the number to squares
    sign_change_pos = 0
    for index in range(len(numbers) - 1):
        # print(numbers[index], numbers[index+1])
        if numbers[index] < 0 and numbers[index + 1] >= 0:
            sign_change_pos = index + 1
            break

        # if last number is -ve
        if index == len(numbers) - 2 and numbers[index + 1] < 0:
            sign_change_pos = index + 2

    # print(sign_change_pos)
    right = sign_change_pos
    left = sign_change_pos - 1
    return_arr = []
    while right < len(numbers) and left >= 0:
        if numbers[right] <= abs(numbers[left]):
            return_arr.append(pow(numbers[right], 2))
            right += 1

        else:  # numbers[right] > abs(numbers[left]):
            return_arr.append(pow(numbers[left], 2))
            left -= 1

    while left >= 0:
        return_arr.append(pow(numbers[left], 2))
        left -= 1

    while right < len(numbers):
        return_arr.append(pow(numbers[right], 2))
        right += 1

    return return_arr