'''
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m
substrings
 respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.

Example 3:
Input: s1 = "", s2 = "", s3 = ""
Output: true

Constraints:
0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters.


Follow up: Could you solve it using only O(s2.length) additional memory space?
'''
class Solution:

    # Beats 70.38% 42 ms
    def interleave(self, s1, s2, s3):

        if len(s3) == 0 and len(s1) == 0 and len(s2) == 0:
            return True

        if len(s3) != len(s1) + len(s2):
            return False

            # if len(s3) == 1:
            #     if len(s1) > 0 and s3[0] == s1[0] or len(s2) > 0 and s3[0] == s2[0]:
            #         return True
            #     else:
            #         return False

        memo = {}
        def dfs(s1_index, s2_index, s3_index):
            key = (s1_index, s2_index, s3_index)

            if s3_index > len(s3) - 1:
                return True
                # if s1_index == len(s1) -1 and s2_index == len(s2) - 1:
                #     return True
                # else:
                #     return False

            if (s1_index < len(s1) and s3[s3_index] != s1[s1_index]) and (
                    s2_index < len(s2) and s3[s3_index] != s2[s2_index]):
                return False

            if key in memo:
                return memo[key]

            left = False
            if s1_index < len(s1) and s3[s3_index] == s1[s1_index]:
                left = dfs(s1_index + 1, s2_index, s3_index + 1)

            right = False
            if s2_index < len(s2) and s3[s3_index] == s2[s2_index]:
                right = dfs(s1_index, s2_index + 1, s3_index + 1)

            final = left or right
            memo[key] = final

            return final

        return dfs(0, 0, 0)


    def interleave_given(self, s1, s2, s3):
        n, m, s = len(s1), len(s2), len(s3)
        if n + m != s:
            return False
        dp = {}
        def dfs(i, j):
            if i == n and j == m:
                return True
            if (i, j) in dp:
                return dp[(i, j)]
            if i < n and s1[i] == s3[i + j] and dfs(i + 1, j):
                return True
            if j < m and s2[j] == s3[i + j] and dfs(i, j + 1):
                return True
            dp[(i, j)] = False
            return False

        return dfs(0, 0)
        