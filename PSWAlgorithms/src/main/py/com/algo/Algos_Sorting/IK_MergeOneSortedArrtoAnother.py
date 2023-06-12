'''
First array has n positive numbers, and they are sorted in the non-descending order.

Second array has 2n numbers: first n are also positive and sorted in the same way but
the last n are all zeroes.

Merge the first array into the second and return the latter. You should get 2n positive
integers sorted in the non-descending order.

Example
{
"first": [1, 3, 5],
"second": [2, 4, 6, 0, 0, 0]
}
Output:

[1, 2, 3, 4, 5, 6]
Notes
Constraints:

1 <= n <= 105
1 <= array elements (except those zeroes) <= 2 * 109
You can use only constant auxiliary space

https://uplevel.interviewkickstart.com/resource/rc-codingproblem-470031-900132-1127-6898
'''

class Solution:
    def merge_one_into_another(self, first, second):
        """
        Args:
         first(list_int32)
         second(list_int32)
        Returns:
         list_int32
        """
        # Write your code here.
        s1_idx = len(first) - 1
        s2_idx = len(second) - 1
        k_idx = len(second) - 1

        # Bring s2_idx to non-zero value index
        while second[s2_idx] == 0:
            s2_idx -= 1

        while s1_idx >= 0 or s2_idx >= 0:
            # if s1 is consumed but s2 is yet to be consumed
            while s1_idx < 0 and s2_idx >= 0:
                second[k_idx] = second[s2_idx]
                k_idx -= 1
                s2_idx -= 1

            # if s2 is consumed but s1 is yet to be consumed
            while s2_idx < 0 and s1_idx >= 0:
                second[k_idx] = first[s1_idx]
                k_idx -= 1
                s1_idx -= 1

            if second[s2_idx] < first[s1_idx]:
                second[k_idx] = first[s1_idx]
                k_idx -= 1
                s1_idx -= 1
            else:
                second[k_idx] = second[s2_idx]
                k_idx -= 1
                s2_idx -= 1

        return second