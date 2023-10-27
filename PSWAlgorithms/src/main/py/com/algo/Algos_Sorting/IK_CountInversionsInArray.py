'''
Count the number of inversions in a given array of numbers. A pair (nums[i], nums[j]) is said to form an inversion if nums[i] > nums[j] and i < j.

Example One
{
"nums": [3, 6, 1, 7, 2]
}
Output:

5
The given array has five inversions: (3, 1), (3, 2), (6, 1), (6, 2), and (7, 2).

Example Two
{
"nums": [5, 10, 15, 18]
}
Output:

0
Notes
Constraints:

1 <= size of the input array <= 10^5
0 <= any element of the input array <= 10^5
'''


def count_inversions(nums):
    """
    Args:
     nums(list_int32)
    Returns:
     int64
    """

    # Write your code here.
    # Merge Sort and count inversions while merging
    # number_of_inversions = 0
    # def merge(arr1, arr2):
    #     print(arr1, arr2)
    #     nonlocal number_of_inversions
    #     i = 0
    #     j = 0
    #     k = 0
    #     actual_arr = []
    #
    #     while i < len(arr1) and j < len(arr2):
    #         if arr1[i] <= arr2[j]:
    #             actual_arr[k] = arr1[i]
    #             i += 1
    #         else:
    #             actual_arr[k] = arr2[j]
    #             j += 1
    #             number_of_inversions += 1
    #
    #         k += 1
    #
    #     while i < len(arr1):
    #         actual_arr[k] = arr1[i]
    #         i += 1
    #         k += 1
    #         number_of_inversions += 1
    #
    #     while j < len(arr2):
    #         actual_arr[k] = arr2[j]
    #         j += 1
    #         k += 1
    #
    #     # nums[start:end] = actual_arr
    #     # return number_of_inversions

    def merge(start, middle, end):
        print(start, middle, end)
        # nonlocal number_of_inversions
        i = start
        j = middle+1
        k = 0
        number_of_inversions = 0
        actual_arr = [0 for i in range(end-start+1)]

        while i <= middle and j <= end:
            if nums[i] <= nums[j]:
                actual_arr[k] = nums[i]
                i += 1
            else:
                actual_arr[k] = nums[j]
                j += 1
                number_of_inversions += (middle+1-i)

            k += 1

        while i <= middle:
            actual_arr[k] = nums[i]
            i += 1
            k += 1
            # number_of_inversions += 1

        while j <= end:
            actual_arr[k] = nums[j]
            j += 1
            k += 1

        nums[start:end] = actual_arr[start:end]
        return number_of_inversions

    def mer_sort(start, end):
        number_of_inversions = 0
        if start < end:
            middle = start + (end-start)//2

            number_of_inversions = mer_sort(start, middle)
            number_of_inversions += mer_sort(middle+1, end)

            number_of_inversions += merge(start, middle, end)
            # number_of_inversions += merge(nums[start:middle+1], nums[middle+1:end+1], nums)
            print(f"start: {start}, end: {end}, number_of_inversions: {number_of_inversions}, nums: {nums}")

            # return left + right + merged

        return number_of_inversions

    # def merge_sort(arr_pass):
    #
    #     if len(arr_pass) > 1:
    #         middle = len(arr_pass) // 2
    #
    #         left_half = arr_pass[:middle]
    #         right_half = arr_pass[middle:]
    #
    #         left = mer_sort(left_half)
    #         right = mer_sort(right_half)
    #         merged = merge(left_half, right_half, arr_pass)
    #         print(f"left: {left}, right: {right}, merged: {merged}")
    #         # return mer_sort(left_half) + mer_sort(right_half) + merge(left_half, right_half, arr_pass)
    #
    #         return left + right + merged
    #
    #     return 0

    start = 0
    end = len(nums) - 1
    return mer_sort(start, end)