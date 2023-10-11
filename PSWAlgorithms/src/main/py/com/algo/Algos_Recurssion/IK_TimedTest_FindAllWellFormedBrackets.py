'''
Given a positive integer n, return ALL strings of length 2 * n with well-formed round brackets.

Example
{
"n": 3
}
Output:

[
"((()))",
"(()())",
"(())()",
"()(())",
"()()()"
]
Any array containing these five strings in any order is a correct output.

Notes
Order of strings in the returned array is insignificant, e.g. for n = 2 both ["(())", "()()"] and ["()()", "(())"]
 will be accepted.
Constraints:

1 <= n <= 12
Only use round brackets. '(' and ')'
'''


class Solution:
    def find_all_well_formed_brackets(n):
        """
        Args:
         n(int32)
        Returns:
         list_str
        """
        # Write your code here.
        result = []

        def helper(sol, open, closed):
            if open == n and closed == n:
                result.append("".join(elem for elem in sol.copy()))
                return
            else:

                if open < n:
                    sol.append("(")
                    helper(sol, open + 1, closed)
                    sol.pop()

                if open > closed:
                    sol.append(")")
                    helper(sol, open, closed + 1)
                    sol.pop()

        helper(["("], 1, 0)
        return result

    def find_all_well_formed_brackets_2(n):
        """
        Args:
         n(int32)
        Returns:
         list_str
        """
        # Write your code here.
        result = []

        def helper(temp, open, closed):
            nonlocal result

            if open == n and closed == n:
                result.append("".join(elem for elem in temp))
                return

            if open < n:
                temp.append("(")
                helper(temp, open + 1, closed)
                temp.pop()

            if open > closed:
                temp.append(")")
                helper(temp, open, closed + 1)
                temp.pop()

        helper(["("], 1, 0)

        return result