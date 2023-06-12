'''
Given an array of numbers with possible duplicates, return all of its permutations in any order.

Example
{
"arr": [1, 2, 2]
}
Output:

[
[1, 2, 2],
[2, 1, 2],
[2, 2, 1]
]
Notes
Constraints:

1 <= size of the input array <= 9
0 <= any array element <= 9
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
        memo = {}
        def helper_memo(curr_arr, sol, n, key):
            # print(curr_arr, sol, n, key, memo)
            if key in memo:
                return

            if n == len(arr):
                result.append(sol.copy())
                return
            else:
                for i in range(len(curr_arr)):
                    sol.append(curr_arr[i])
                    new_key = key + str(curr_arr[i])
                    helper_memo(curr_arr[:i] + curr_arr[i + 1:], sol, n + 1, new_key)
                    memo[new_key] = 1
                    sol.pop()

        result_1 = set()
        def helper(sol, n):
            if n == len(arr):
                result_1.add(sol.copy())
                return
            else:
                for i in range(n, len(arr)):
                    sol[n], sol[i] = sol[i], sol[n]
                    helper(sol, n + 1)

        # helper_memo(arr, [], 0)
        # return result

        helper(arr, 0)
        return list(result_1)
