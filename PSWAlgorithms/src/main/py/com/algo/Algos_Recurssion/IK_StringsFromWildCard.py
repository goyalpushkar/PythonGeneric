'''
You are given string s of length n, having m wildcard characters '?', where each wildcard character represents a
single character. Write a program which returns a list of all possible distinct strings that can be generated
by replacing each wildcard character in s with either '0' or '1'.

Any string returned must not contain '?' characters, all must be replaced with either '0' or '1'.

Example One
{
"s": "1?10"
}
Output:

["1010", "1110"]
Example Two
{
"s": "1?0?"
}
Output:

["1000", "1001", "1100", "1101"]
Input string has two '?' characters. Each one can be replaced with either '0' or '1' making the total number of
distinct strings 22 = 4.

Notes
Order of strings in the output does not matter.

Constraints:

1 <= n <= 50
0 <= m <= 17
'''


def find_all_possibilities(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    # Write your code here.
    result = []

    def helper(slate, index):
        if index == len(s):
            result.append(slate)
            return

        if s[index] == "?":
            helper(slate + "0", index + 1)
            helper(slate + "1", index + 1)
        else:
            helper(slate + s[index], index + 1)

    helper("", 0)

    return result