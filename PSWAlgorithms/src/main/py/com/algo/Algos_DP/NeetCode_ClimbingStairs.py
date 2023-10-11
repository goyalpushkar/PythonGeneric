'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:
1 <= n <= 45
'''
class Solution:
    # Beats 80.87% 28ms
    def climbStairs(self, n):
        # backtracking
        memo = {}
        self.sum = 0

        def track(n):
            if n < 0:
                return 0

            if n == 0:
                return 1

            if n in memo:
                return memo[n]

            total = track(n - 1) + track(n - 2)
            memo[n] = total

            return total

        return track(n)

    def climbStairs(self, n):
        mem = [0 for _ in range(n + 1)]

        mem[0] = 1
        mem[1] = 1

        for i in range(2, n + 1):
            mem[i] = mem[i - 1] + mem[i - 2]

        return mem[n]
