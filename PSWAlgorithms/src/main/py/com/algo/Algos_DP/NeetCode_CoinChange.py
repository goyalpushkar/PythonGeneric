'''
You are given an integer array coins representing coins of different denominations and an integer amount
representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be
made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0


Constraints:
1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
'''
class Solution(object):
    # Beats 64.9% 1478ms  - DP
    # O(amount * len(coins))
    def coinChange(self, coins, amount):
        import math

        if amount == 0: return 0
        if len(coins) == 0: return 0

        dp = [1 if i in coins else amount + 1 for i in range(amount + 1)]
        dp[0] = 1
        coins = sorted(coins)

        # print(f"dp: {dp}")
        for amt in range(amount + 1):
            for coin in coins:
                # print(f"amt: {amt}\tcoin: {coin}")
                if coin <= amt:
                    dp[amt] = min(dp[amt], 1 + dp[amt - coin])

                    # print(f"dp: {dp}")
        return -1 if dp[amount] == amount + 1 else dp[amount]

    # Beats 10.34% 2285ms  - Memo
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        import math
        memo = {}
        # self.min_len = math.inf
        def helper(target):
            # print(f"target: {target}\t coins_used: {coins_used}")
            if target < 0:
                return None

            if target == 0:
                return []

            if target in memo:
                return memo[target]

            # min_len = math.inf
            shortest_sol = None
            for num in coins:
                remaining = target - num
                pos_sol = helper(remaining)
                # print(f"target: {target}-{num} \t pos_sol: {pos_sol}\tpos_coin_used: {pos_coin_used}")

                if pos_sol is not None:
                    new_sol = pos_sol + [num]
                    if shortest_sol is None or len(new_sol) < len(shortest_sol):
                        # self.min_len = len(pos_sol)
                        # min_len = len(pos_sol)
                        shortest_sol = new_sol
                        # memo[target] = (pos_sol, pos_coins)

            # print(f"target: {target} {remaining} \t pos_coins: {pos_coins}")
            memo[target] = shortest_sol
            return shortest_sol

        if amount == 0: return 0
        if len(coins) == 0: return 0

        final = helper(amount)
        # print(f"memo: {memo}")
        return -1 if final is None else len(final)
        # return -1 if self.min_len == math.inf else self.min_len