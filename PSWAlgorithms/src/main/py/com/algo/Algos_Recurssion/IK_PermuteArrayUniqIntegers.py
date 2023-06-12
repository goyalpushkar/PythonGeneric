'''
Given an array of unique numbers, return in any order all its permutations.

Example
{
"arr": [1, 2, 3]
}
Output:

[
[1, 2, 3],
[1, 3, 2],
[2, 1, 3],
[2, 3, 1],
[3, 2, 1],
[3, 1, 2]
]
Notes
Constraints:

1 <= size of the input array <= 9
0 <= any array element <= 99
'''

class Solution:
    def get_permutations(arr):
        """
        Args:
         arr(list_int32)
        Returns:
         list_list_int32
        """
        # Write your code here.
        result = []

        def helper(curr_arr, sol, n):
            if n == len(arr):
                result.append(sol.copy())
                return
            else:
                for i in range(len(curr_arr)):
                    sol.append(curr_arr[i])
                    helper(curr_arr[:i] + curr_arr[i + 1:], sol, n + 1)
                    sol.pop()

        helper(arr, [], 0)
        return result

    from itertools import permutations
    def get_permutations_standard(arr):
        result = []
        for i in permutations(arr):
            result.append(list(i))
        return result