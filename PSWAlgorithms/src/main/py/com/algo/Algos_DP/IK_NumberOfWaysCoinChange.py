'''
Given a variety of coin denominations existing in a currency system, find the total number of ways a given amount of money can be expressed using coins in that currency system.

Assume infinite supply of coins of every denomination. Return answer modulo 1000000007.

Example
{
"coins ": [1, 2, 3],
"amount": 3
}
Output:
3
The three ways are:

Use the coin with denomination 1 three times.
Use the coin with denomination 3 once.
Use the coin with denomination 2 once and coin with denomination 1 once.
Notes
Two ways are considered different if they use a different number of coins of any particular denomination.
Constraints:
1 <= total number of denominations <= 102
1 <= denomination of a coin <= 104
1 <= amount to be expressed <= 104
'''
def number_of_ways_iterDP(coins, amount):
    """
    Args:
     coins(list_int32)
     amount(int32)
    Returns:
     int32
    """
    # Write your code here.
    n = len(coins)
    tab = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]
    # tab[0] = 1

    for coin_index in range(1, n + 1):
        for amt_index in range(amount + 1):
            if amt_index == 0:
                tab[coin_index][amt_index] = 1
                continue

            if amt_index - coins[coin_index - 1] >= 0:
                tab[coin_index][amt_index] = tab[coin_index - 1][amt_index] + tab[coin_index][
                    amt_index - coins[coin_index - 1]]
            else:
                tab[coin_index][amt_index] = tab[coin_index - 1][amt_index]

        # print(tab)

    return tab[n][amount]

def number_of_ways_iterDPSpaceOpt(coins, amount):
    n = len(coins)
    prev_row = [0 for _ in range(amount + 1)]
    curr_row = [0 for _ in range(amount + 1)]
    curr_row[0] = 1

    for coin_index in range(1, n + 1):
        for amt_index in range(1, amount + 1):
            if amt_index - coins[coin_index - 1] >= 0:
                curr_row[amt_index] = prev_row[amt_index] + curr_row[amt_index - coins[coin_index - 1]]
            else:
                curr_row[amt_index] = prev_row[amt_index]

        # print(prev_row, curr_row)
        for index in range(amount + 1):
            prev_row[index] = curr_row[index]

    return curr_row[amount]