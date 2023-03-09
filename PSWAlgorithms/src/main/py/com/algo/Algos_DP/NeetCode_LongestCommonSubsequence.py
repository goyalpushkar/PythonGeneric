'''
Given two strings text1 and text2, return the length of their longest common subsequence.
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none)
 deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.


Constraints:
1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
'''
from functools import lru_cache
class Solution:
    # beats 23% 1017 ms
    def longestCommonSubsequence(self, text1, text2):
        row_size = len(text1)
        col_size = len(text2)

        memorization = [[0 for col in range(col_size + 1)] for row in range(row_size + 1)]

        for row in range(1, row_size + 1):
            for col in range(1, col_size + 1):
                if text1[row - 1] == text2[col - 1]:
                    memorization[row][col] = 1 + memorization[row - 1][col - 1]
                else:
                    memorization[row][col] = max(memorization[row - 1][col], memorization[row][col - 1])

        return memorization[row_size][col_size]

    # without maxsize=None 42/47 passed and TLE
    # with maxsize beats 7.47% 1763 ms
    def longestCommonSubsequence(self, text1, text2):
        @lru_cache(maxsize=None)
        def helper(text1_index, text2_index):
            if text1_index >= len(text1) or text2_index >= len(text2):
                return 0

            if text1[text1_index] == text2[text2_index]:
                return 1 + helper(text1_index+1, text2_index+1)
            else:
                return max(helper(text1_index+1, text2_index), helper(text1_index, text2_index+1))

        return helper(0, 0)

    # current_matching = 0
    # start_col = 0
    # for row in range(len(text1)):
    #     col = start_col
    #     while col < len(text2):
    #         if text1[row] == text2[col]:
    #             current_matching += 1
    #             start_col = col+1
    #             break

    #         col += 1

    # return current_matching