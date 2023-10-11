'''
Given a number n, generate all possible binary strings of length n.

Example
{
"n": 3
}
Output:

["000", "001", "010", "011", "100", "101", "110", "111"]
Notes
A string consisting of only 0s and 1s is called a binary string.
Return the output list in any order.
Constraints:

1 <= n <= 16
'''
class Solution:

    def get_binary_strings(n):
        """
        Args:
         n(int32)
        Returns:
         list_str
        """
        # Write your code here.
        result = []

        def helper(sol, n):
            if n == 0:
                result.append("".join(el for el in sol))
                return
            else:
                for elem in (['0', '1']):
                    sol.append(elem)
                    helper(sol, n - 1)
                    sol.pop()

        helper([], n)
        return result
