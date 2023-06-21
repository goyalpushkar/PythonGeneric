'''

'''
import math
def minimum_coins(coins, value):
    """
    Args:
     coins(list_int32)
     value(int32)
    Returns:
     int32
    """
    # Write your code here.
    memo = {}

    def mincoin_rec(curr_val):
        # print(curr_val, memo)
        if curr_val in memo:
            return memo[curr_val]

        if curr_val < 0:
            return math.inf

        if curr_val == 0:
            return 0

        min_val = math.inf
        for index in range(len(coins)):
            min_val = min(min_val, mincoin_rec(curr_val - coins[index]) + 1)

        memo[curr_val] = min_val

        return memo[curr_val]

    return mincoin_rec(value)

def minimum_coins(coins, value):
    """
    Args:
     coins(list_int32)
     value(int32)
    Returns:
     int32
    """
    # Write your code here.
    tab = [0 for i in range(value + 1)]

    for index in range(1, value + 1):
        min_value = math.inf
        for coin in coins:
            # print('Before', index, coin, min_value)
            if index - coin < 0:
                cur_val = math.inf
            else:
                cur_val = tab[index - coin] + 1

            min_value = min(min_value, cur_val)
            # print('After', index, coin, min_value, cur_val)

        tab[index] = min_value

    # print(tab)
    return tab[value]