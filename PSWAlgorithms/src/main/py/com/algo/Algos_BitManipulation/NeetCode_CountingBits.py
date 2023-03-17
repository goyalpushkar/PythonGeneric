'''
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the
number of 1's in the binary representation of i.

Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

Constraints:
0 <= n <= 105

Follow up:
It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly
 in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
'''
class Solution:

    '''
            0 - 0 0 0 0 =     dp[0]   = 0
            1 - 0 0 0 1 = 1 + dp[n-1] = 1
            2 - 0 0 1 0 = 1 + dp[n-2] = 1
            3 - 0 0 1 1 = 1 + dp[n-2] = 2
            4 - 0 1 0 0 = 1 + dp[n-4] = 1
            5 - 0 1 0 1 = 1 + dp[n-4] = 2
            6 - 0 1 1 0 = 1 + dp[n-4] = 2
            7 - 0 1 1 1 = 1 + dp[n-4] = 3
            8 - 1 0 0 0 = 1 + dp[n-8]
    '''

    # Beats 85.8% 80 ms
    def countBits(self, n):
        dp = [0] * n+1
        offset = 1
        for i in range(1, n+1):
            if offset*2 == i:
                offset = i
            dp[i] = 1 + dp[i-offset]

        return dp


    # Beats 32.56% 125 ms
    def countBits_1st(self, n):

        def helper(n):
            sum = 0
            while n != 0:
                sum += 1
                n = n & (n - 1)

            return sum

        return_array = []
        for i in range(n + 1):
            return_array.append(helper(i))

        return return_array

    def countBits_short(self, n):
        return [i.bit_count() for i in range(n + 1)]
        # return [bin(i).count('1') for i in range(n+1)]