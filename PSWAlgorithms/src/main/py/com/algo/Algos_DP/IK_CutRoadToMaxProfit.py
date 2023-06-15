'''
Given the prices for rod pieces of every size between 1 inch and n inches, find the maximum total profit
 that can be made by cutting an n inches long rod inch into pieces.

Example
{
"price ": [1, 5, 8, 9]
}
Output:
10
The rod can be cut in the ways given below:
1 + 1 + 1 + 1 inches will cost price[0] + price[0] + price[0] + price[0] = 4
1 + 1 + 2 inches will cost price[0] + price[0] + price[1] = 7
1 + 3 inches will cost price[0] + price[2] = 9
2 + 2 inches will cost price[1] + price[1] = 10
One piece of 4 inches will cost price[3] = 9
The maximum profit is obtained by cutting it into two pieces 2 inches each.

Notes
Constraints:
1 <= n <= 103
1 <= price of any sized piece of the rod <= 105
'''
import math


def get_maximum_profit(price):
    """
    Args:
     price(list_int32)
    Returns:
     int32
    """
    # Write your code here.
    rod_length = len(price)

    memo = {}
    def profit_rec(n):
        # print(n, memo)
        if n in memo:
            return memo[n]

        if n == 0:
            return 0

        max_profit = -math.inf
        for index in range(rod_length):
            if n - (index + 1) >= 0:
                return_profit = profit_rec(n - (index + 1))
                return_profit += price[index]
            else:
                return_profit = 0
            max_profit = max(max_profit, return_profit)

        memo[n] = max_profit
        return memo[n]

    def profit_tab(price):
        tab = [0 for i in range(rod_length + 1)]

        for i in range(rod_length + 1):
            for cost_index in range(rod_length):
                if i - (cost_index + 1) >= 0:
                    tab[i] = max(tab[i], tab[i - (cost_index + 1)] + price[cost_index])

        return tab[rod_length]

    return profit_tab(price)
    return profit_rec(rod_length)