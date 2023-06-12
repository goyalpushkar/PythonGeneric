'''
Fibonacci sequence
'''
def find_fibonacci(n):
    """
    Args:
     n(int32)
    Returns:
     int32
    """
    # Write your code here.
    memo = {}

    def fib(n):
        if n == 0:
            return 0
        if n == 1:
            return 1

        if n in memo:
            return memo[n]

        memo[n] = fib(n - 1) + fib(n - 2)

        return memo[n]

    def fib_tab(n):
        if n == 0:
            return 0
        if n == 1:
            return 1

        tab = [0 for _ in range(n + 1)]
        tab[1] = 1
        for i in range(2, n + 1):
            tab[i] = tab[i - 1] + tab[i - 2]

        return tab[n]

    return fib_tab(n)

'''
There is a one-dimensional axis. In one turn, you can take a jump of length 1 or 2. Find the total number of distinct ways using which you can reach from 0th coordinate to n-th coordinate?

Example One
{
"n": 3
}
Output:
3

There are 3 distinct ways in which you can move from 0 to 3.
1 length jump + 1 length jump + 1 length jump.
1 length jump + 2 length jump.
2 length jump + 1 length jump.
'''
def jump_ways(n):
    """
    Args:
     n(int32)
    Returns:
     int64
    """
    # Write your code here.
    def fib_tab(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        # if n == 2:
        #     return 2

        tab = [0 for _ in range(n + 1)]
        tab[1] = 1
        tab[2] = 2
        print(tab)
        for i in range(3, n + 1):
            tab[i] = tab[i - 1] + tab[i - 2]

        print(tab)
        return tab[n]

    return fib_tab(n)

'''
Consider you have n distinct elements, find the number of ways through which you can choose 
exactly r number of elements out of those.

Example One
{
"n": 5,
"r": 3
}
Output:
10
There is a set of 5 elements {1, 2, 3, 4, 5}. You need to pick a subset of size 3. Eligible subsets are 
{1, 2, 3}, {1, 2, 4}, {1, 2, 5}, {1, 3, 4}, {1, 3, 5}, {1, 4, 5}, {2, 3, 4}, {2, 3, 5}, {2, 4, 5}, {3, 4, 5}. 
There are 10 subsets of size 3.

Example Two
{
"n": 3,
"r: 5
}
Output:
0
There is a set of 3 elements {1, 2, 3}. You need to pick a subset of size 5. Which is not possible, that's why the 
answer is 0.

Notes
Here the answer can be very big, find it modulo 109 + 7.

Constraints:
0 <= n, r <= 1000
'''
def ncr(n, r):
    """
    Args:
     n(int32)
     r(int32)
    Returns:
     int32
    """
    # Write your code here.
    if n == 0:
        return 1

    tab = [[0 for _ in range(r + 1)] for _ in range(n + 1)]

    for row in range(1, n + 1):
        tab[row][0] = 1

    # print(tab)
    for row in range(1, n + 1):
        for col in range(1, r + 1):
            if row == col:
                tab[row][col] = 1
            else:
                tab[row][col] = (tab[row - 1][col] + tab[row - 1][col - 1]) % (10 ** 9 + 7)

    # print(tab)

    return tab[n][r]

'''
Given a grid of size n x m and a robot initially staying at the top-left position, return the number of unique paths 
for the robot to reach the bottom-right corner of the grid. The robot is allowed to move either down or right 
at any point in time.

Example One
{
"n": 3,
"m": 2
}
Output:
3
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:

Right -> Down -> Down
Down -> Down -> Right
Down -> Right -> Down
Example Two
{
"n": 4,
"m": 1
}
Output:
1
From the top-left corner, there is only one way to reach bottom-right corner:

Down -> Down -> Down
Notes
Return the answer modulo 109 + 7.

Constraints:
1 <= n, m <= 103
'''


def unique_paths(n, m):
    """
    Args:
     n(int32)
     m(int32)
    Returns:
     int32
    """
    # Write your code here.
    tab = [[0 for _ in range(m)] for _ in range(n)]

    # print(tab)
    for i in range(n):
        tab[i][0] = 1

    for i in range(m):
        tab[0][i] = 1

    for row in range(1, n):
        for col in range(1, m):
            tab[row][col] = tab[row - 1][col] + tab[row][col - 1]

    # print(tab)
    return (tab[n - 1][m - 1]) % (10 ** 9 + 7)

'''
Given a two dimensional grid of numbers. Find a path from top-left corner to bottom-right corner,
 which maximizes the sum of all numbers along its path.

You can only move either down or right from your current position.

Example One
{
"grid": [
[4, 5, 8],
[3, 6, 4],
[2, 4, 7]
]
}
Output:
28
The path 4 -> 5 -> 8 -> 4 -> 7 maximizes the sum. Every other path from top left to bottom right has sum less than 28.

Example Two
{
"grid": [
[1, -4, 3],
[4, -2, 2]
]
}
Output:
5
The path 1 -> 4 -> -2 -> 2 maximizes the sum. Note that there can be negative values in the grid as well.

Notes
Constraints:
1 <= number of rows <= 300
1 <= number of columns <= 300
-104 <= numbers in the grid <= 104
'''
def maximum_path_sum(grid):
    """
    Args:
     grid(list_list_int32)
    Returns:
     int32
    """
    # Write your code here.

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if row == 0 and col == 0:
                continue

            if row == 0 and col != 0:
                grid[row][col] += grid[row][col - 1]
                continue

            if col == 0 and row != 0:
                grid[row][col] += grid[row - 1][col]
                continue

            grid[row][col] += max(grid[row - 1][col], grid[row][col - 1])

    return grid[-1][-1]

'''
There are n stairs indexed 0 to n – 1. Each stair has a cost associated with it. After paying the cost, it's
 allowed either to climb one or two steps further. It's allowed to either start from the step with index 0, or the step with index 1.
Given the cost array, find the minimum cost to reach the top of the floor.
cost[i] represents the cost of i-th stair.

Example One
{
"cost": [1, 1, 2]
}
Output:
1
There are 5 ways to reach the top floor.

step 0 → step 1 → step 2 → top floor.
step 0 → step 1 → top floor.
step 0 → step 2 → top floor.
step 1 → step 2 → top floor.
step 1 → top floor.
Here, the last way(step 1 → top floor) will provide the most optimal cost 1.

Example Two
{
"cost": [3, 4]
}
Output:
3

Notes
Constraints:
2 <= length of the input array <= 1000
0 <= cost[i] <= 999, for all i.
'''

def min_cost_climbing_stairs(cost):
    """
    Args:
     cost(list_int32)
    Returns:
     int32
    """
    # Write your code here.
    # run_cost = [0 for _ in range(len(cost)+2)]
    for i in range(1, len(cost)):
        if i - 2 < 0:
            cost[i] += min(cost[i - 1], 0)
        else:
            cost[i] += min(cost[i - 1], cost[i - 2])

    top_cost = min(cost[-2], cost[-1])

    return top_cost

'''
Given a variety of coin types defining a currency system, find the minimum number of coins required to express a
 given amount of money. Assume infinite supply of coins of every type.

Example
{
"coins": [1, 3, 5],
"value": 9
}
Output:
3
Here are all the unique ways to express 9 as a sum of coins 1, 3 and 5:

1, 1, 1, 1, 1, 1, 1, 1, 1
1, 1, 1, 1, 1, 1, 3
1, 1, 1, 1, 5
1, 1, 1, 3, 3
1, 3, 5
3, 3, 3
Last two ways use the minimal number of coins, 3.

Notes
There will be no duplicate coin types in the input.

Constraints:
1 <= number of coin types <= 102
1 <= coin value <= 102
1 <= amount of money to express <= 104
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
    def mincoin_rec(n, curr_len):  #

        # print(n, curr_len, memo)

        if n in memo:
            return memo[n]

        # base case
        if n < 0:
            return math.inf

        if n == 0:
            return 0

        min_length = math.inf
        for coin in coins:
            cur_val = mincoin_rec(n - coin, curr_len + 1)
            min_length = min(min_length, cur_val + 1)

        memo[n] = min_length

        return memo[n]

    def mincoin_tab(n):  #
        tab = [0 for i in range(n + 1)]
        for index in range(1, n + 1):
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

    return mincoin_tab(value)
    return mincoin_rec(value, 0)