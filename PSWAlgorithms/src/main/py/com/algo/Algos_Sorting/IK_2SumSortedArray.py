'''
Given an array sorted in non-decreasing order and a target number, find the indices of the two values from the array
 that sum up to the given target number.

Example
{
"numbers": [1, 2, 3, 5, 10],
"target": 7
}
Output:

[1, 3]
Sum of the elements at index 1 and 3 is 7.

Notes
In case when no answer exists, return an array of size two with both values equal to -1, i.e., [-1, -1].
In case when multiple answers exist, you may return any of them.
The order of the indices returned does not matter.
A single index cannot be used twice.
Constraints:

2 <= array size <= 105
-105 <= array elements <= 105
'''
class Solution:
    def pair_sum_sorted_array(numbers, target):
        """
        Args:
         numbers(list_int32)
         target(int32)
        Returns:
         list_int32
        """
        # Write your code here.

        start = 0
        end = len(numbers) - 1
        while start < end:
            if target - numbers[start] == numbers[end]:
                return [start, end]
            elif target - numbers[start] > numbers[end]:
                start += 1
            else:
                end -= 1

        return [-1, -1]