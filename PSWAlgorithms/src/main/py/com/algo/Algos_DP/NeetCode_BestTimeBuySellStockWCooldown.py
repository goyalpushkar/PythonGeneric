'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like
(i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).


Example 1:
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example 2:
Input: prices = [1]
Output: 0

Constraints:
1 <= prices.length <= 5000
0 <= prices[i] <= 1000
'''
class Solution:
    '''
                                                                                 0  1   2   3   4
                                                                                 1  2   3   0   2
                                                                                    (0,B)
                                                        /                                                       \
                                       -1(0,B)                                                                                                    0(0,C)
                      /                                     \                                                                /                                         \
               1(1,S)                                        -1(1,C)                                                     -2(1,B)                                                 0(1,C)
                 |                               /                            \                                   /                  \                               /                            \
               1(2,C)                       -4(2,B)                          -1(2,C)                            1(2,S)               -2(2,C)                       -3(2,B)                            0(2,C)
          /             \                 /        \                         /      \                            |              /            \                    /        \                         /      \
     1(3,B)           1(3,C)          -4(3,S)      -4 (3,C)             -1(3,S)    -1(3,C)                    1(3,C)      -2(3,B)            -2(3,C)          -3(3,S)      -3(3,C)             0(3,B)             0(3,C)
 /          \        /      \           |         /       \           |           /        \                /       \     /       \          /      \           |         /       \          /       \         /        \
3(4,S)     1(4,C)  -1(4,B)  1(4,C)   -4(4,C)    -6(4,B)  -4(4,C)   -1(4,C)     -3(4,B)    -1(4,C)        -1(4,B)   1(4,C) 0(4,S)  -2(4,C)  -4(4,B)  -2(4,C)  -3(4,C)   -5(4,B)   -3(4,C)  2(4,S)    0(4,C)  -2(4,B)     0(4,C)






    '''
    # Beats 24.64% 55 ms
    def maxProfit(self, prices):

        memo = {}

        def take_action(index, buy_y):
            if index >= len(prices):
                return 0

            if (index, buy_y) in memo:
                return memo[(index, buy_y)]

            if buy_y:
                profit = take_action(index + 1, not buy_y) - prices[index]
                cooldown = take_action(index + 1, buy_y)

            else:
                profit = take_action(index + 2, not buy_y) + prices[index]
                cooldown = take_action(index + 1, buy_y)

            memo[(index, buy_y)] = max(profit, cooldown)

            return memo[(index, buy_y)]

        return take_action(0, True)

    '''
        0   1   2   3   4   5
        6   1   3   2   4   7
        n = 6
        C = n+1 = 7    # -1+3 = n+2 = 10
        R = n-1 = 5 (Diff Gaps)

        max( prices[col+row]-prices[col] + prof[row][col+row+2],
             prof[row][col+1],
             prof[row-1][col] )

        0   1   2   3   4   5   6
    0   0   0   0   0   0   0   0
    1   5   5   3   3   3   0   0
    2   5   5   5   5   3   0   0
    3   0   0   0   0   0   0   0
    4   0   0   0   0   0   0   0
    5   0   0   0   0   0   0   0

    '''
    # 194/210 passed
    def maxProfit(self, prices):
        n = len(prices)
        prof = [[0 for col in range(n + 1)] for row in range(n)]

        for row in range(1, n):
            for col in range(n - 2, -1, -1):
                # print(f"row: {row} col: {col}")
                if col + row > n - 1:
                    sell_price = 0
                    profit = 0
                else:
                    sell_price = prices[col + row]
                    profit = prof[row][col + 1]

                if col + row + 2 > n:
                    prev_profit = 0
                else:
                    prev_profit = prof[row][col + row + 2]

                prof[row][col] = max(sell_price - prices[col] + prev_profit, profit, prof[row - 1][col])

        print(prof)
        return prof[n - 1][0]