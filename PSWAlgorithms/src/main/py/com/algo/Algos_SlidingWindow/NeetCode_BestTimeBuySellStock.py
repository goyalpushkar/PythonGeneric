'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future
 to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104
'''
class Solution:
    # 1115 ms Beats 44.51%
    def maxProfit(self, prices):
        l = 0
        r = 1
        max_profit = 0

        while r < len(prices):
            while l < r and prices[r] < prices[l]:
                l += 1
                # r += 1

            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
            r += 1

        return max_profit

    # 1089 ms Beats 55.64%
    def maxProfit(self, prices):
        res, min_p = 0, inf
        for v in prices:
            res = max(res, v - min_p)
            min_p = min(min_p, v)

        return res



        profit = prices[r] - prices[l]
        max_profit = max(max_profit, profit)





    # Time limit exceeded
    def maxProfit_TLE(self, prices):
        max_profit = 0
        for start in range(len(prices)):
            for end in range(start, len(prices)):
                profit = prices[end] - prices[start]
                max_profit = max(max_profit, profit)

        return max_profit