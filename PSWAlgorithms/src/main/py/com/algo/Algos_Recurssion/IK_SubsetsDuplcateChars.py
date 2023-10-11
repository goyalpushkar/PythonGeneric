'''
Given a string that might contain duplicate characters, find all the possible distinct subsets of that string.

Example One
{
"s": "aab"
}
Output:

["", "a", "aa", "aab", "ab", "b"]
Example Two
{
"s": "dc"
}
Output:

["", "c", "cd", "d"]
Notes
All the subset strings should be individually sorted.
The order of the output strings does not matter.

Constraints:
1 <= length of the string <= 15
String consists of lowercase English letters
'''


class Solution:
    def get_distinct_subsets(s):
        """
        Args:
         s(str)
        Returns:
         list_str
        """
        # Write your code here.
        result = []
        memo = {}

        def helper(sol, i):
            # print(sol, "-", i, "-", memo)
            if sol + '_' + str(i - 1) in memo:
                return

            if i == len(s):
                result.append(sol)
                return
            else:
                # left
                helper(sol, i + 1)
                memo[sol + '_' + str(i)] = 1

                # right
                helper(sol + s[i], i + 1)
                # if sol != "":
                memo[sol + s[i] + '_' + str(i)] = 1

        s = sorted(s)
        helper("", 0)
        return result
