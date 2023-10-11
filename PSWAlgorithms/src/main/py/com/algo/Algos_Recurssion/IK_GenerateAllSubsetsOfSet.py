'''
Generate ALL possible subsets of a given set. The set is given in the form of a string s containing distinct
lowercase characters 'a' - 'z'.

Example
{
"s": "xy"
}
Output:

["", "x", "y", "xy"]
Notes
Any set is a subset of itself.
Empty set is a subset of any set.
Output contains ALL possible subsets of given string.
Order of strings in the output does not matter. E.g. s = "a", arrays ["", "a"] and ["a", ""] both will be accepted.
Order of characters in any subset must be same as in the input string. For s = "xy", array ["", "x", "y", "xy"]
will be accepted, but ["", "x", "y", "yx"] will not be accepted.
Constraints:

0 <= length of s <= 19
s only contains distinct lowercase English letters.
'''
class Solution:
    def generate_all_subsets(s):
        """
        Args:
         s(str)
        Returns:
         list_str
        """
        # Write your code here.
        result = []

        def helper(sol, i):
            if i == len(s):
                result.append("".join(elem for elem in sol))
                return
            else:

                # left
                helper(sol, i + 1)

                # right
                sol.append(s[i])
                helper(sol, i + 1)  # sol+s[i]
                sol.pop()

        helper([], 0)
        return result