'''
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either
down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the
bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Constraints:
1 <= m, n <= 100
'''
import math
class Solution:

    # Beats 29.19% 38ms
    def uniquePaths(self, m, n):
        dp_2 = [[0 for c in range(n+1)] for r in range(m+1)]

        dp_2[1][1] = 1

        for r in range(1, m+1):
            for c in range(1, n+1):
                if r == 1 and c == 1:
                    continue

                dp_2[r][c] = dp_2[r-1][c] + dp_2[r][c-1]

        return dp_2[m][n]

    # Beats 29.19% 38ms after changing key value as tuple from 10.26% 43ms
    def uniquePaths(self, m, n):

        memo = {}
        def dfs(r, c):
            key = (r, c)  # str(r) + "_" + str(c)

            if key in memo:
                return memo[key]

            if r >= m or c >= n:
                return 0

            if r == m-1 and c == n-1:
                return 1

            # right + # down
            val = dfs(r, c+1) + dfs(r+1, c)

            memo[key] = val
            return val

        return dfs(0,0)



    def uniquePaths_math(self, m, n):
        def nCr(n, r):
            return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

        return nCr(m + n - 2, n - 1)