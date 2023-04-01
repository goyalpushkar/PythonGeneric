'''
A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse
of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.


Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").

Constraints:
1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
'''
class Solution:
    '''
                2236

                                     ""
                            /               \
                            2               22
                        /       \        /       \
                    2           23      3         36  (X)
                /       \        |      |
            3           36 (X)   6      6
          /
        6

                2206
                                    "
                              /               \
                            2               22
                        /       \        /       \
                    2           20      0 (X)    06  (X)
                /       \        |
              0(X)      06 (X)   6
    '''
    # DP
    # Beats 14.98% 42ms
    def numDecodings(self, s):

        dp = {len(s): 1}
        def dfs(index):
            if index in dp:
                return dp[index]

            if s[index] == "0":
                return 0

            res = dfs(index+1)

            # next 2 digits are either 1 or 20-26
            if index+1 < len(s) and (s[index] == "1" or (s[index] == "2" and s[index+1] in "0123456")):
                res += dfs(index+2)

            dp[index] = res

            return res

        return dfs(0)


    '''
                        2206
             6  /                   \ 06
            220                     X
    0/               \20
    X                2
                     |2
                    ""
            1 way 0 2 20 6
    '''
    # Memo
    # Beats 6.2% 49ms
    def numDecodings(self, s):
        self.memo = {}

        def helper(passed_value):
            # print(f"Passed_value: {passed_value}")
            if passed_value in self.memo:
                return self.memo[passed_value]

            if passed_value == "":
                # print("Empty String")
                return 1

            # This should not be the base case as it is failing with "10" value
            # it will fail with check of 0 only and return. It will never check for the branch of "10"
            # if passed_value[-1:] != str(int(passed_value[-1:])) \
            #         or int(passed_value[-1:]) < ord('A') - 64 \
            #         or int(passed_value[-1:]) > ord('Z') - 64:
            #     # print(f"One char failed\t {int(passed_value[-1:])}, {ord('A') - 64}, {ord('Z') - 64}")
            #     return 0
            #
            # if len(passed_value) > 1 and (passed_value[-2:] != str(int(passed_value[-2:]))
            #                               or (int(passed_value[-2:]) < ord('A') - 64
            #                                   or int(passed_value[-2:]) > ord('Z') - 64)):
            #     # print(f"Two char failed\t {int(passed_value[-2:])}, {ord('A') - 64}, {ord('Z') - 64}")
            #     return 0

            # If left side is valid call left branch
            ret_val_left = 0
            if passed_value[-1:] == str(int(passed_value[-1:])) \
                    and ord('A') - 64 <= int(passed_value[-1:]) <= ord('Z') - 64:
                # print(f"One char passed\t {int(passed_value[-1:])}, {ord('A') - 64}, {ord('Z') - 64}")
                ret_val_left = helper(passed_value[:-1])

                # If right side is valid call right branch
            ret_val_right = 0
            if len(passed_value) > 1 and passed_value[-2:] == str(int(passed_value[-2:])) \
                    and ord('A') - 64 <= int(passed_value[-2:]) <= ord('Z') - 64:
                # print(f"Two char passed\t {int(passed_value[-2:])}, {ord('A') - 64}, {ord('Z') - 64}")
                ret_val_right = helper(passed_value[:-2])

            # ret_val = helper(passed_value[:-1]) + helper(passed_value[:-2]) if len(passed_value) > 1 else 0

            # print(f"passed_value: {passed_value} - {ret_val_left}+{ret_val_right} ")
            ret_val = ret_val_left + ret_val_right
            self.memo[passed_value] = ret_val
            # print(f"passed_value: {passed_value}-{self.memo}")

            return ret_val

        # print(f"self.memo: {self.memo}")
        return helper(s)