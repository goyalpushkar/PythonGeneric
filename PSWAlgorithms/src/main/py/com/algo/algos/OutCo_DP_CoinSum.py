'''
Given an array of coins and a target toal, return how many unique ways there are to use the coins to make up that total

Input [1,2,3], 4
Output 4
Possible combinations
1 + 1 + 1 + 1
1 + 3
1 + 1 + 2
2 + 2

Input [2,5,3,6], 10
Output 5
Possible combinations
2 + 3 + 5
5 + 5
2 + 3 + 2 + 3
2 + 2 + 6
2 + 2 + 2 + 2 + 2

  left -> subtract the total, keep coin types same
  right -> keep total same, remove one of the coins
                                                                                                                                    10, [2,3,5,6]
                                                                                 8,[2,3,5,6]                                                                                                        10, [3,5,6]
                                            6, [2,3,5,6]                                                                   8, [3,5,6]                                          7, [3,5,6]                                   10, [5,6]
                     4, [2,3,5,6]                                       6, [3,5,6]                         5, [3,5,6]                     8, [5,6]                  4, [3,5,6]          7, [5,6]                 5, [5, 6]               10, [6]
        2, [2,3,5,6]                4, [3,5,6]                3, [3,5,6]           6, [5,6]         2, [3,5,6]        5, [5,6]      3, [5,6]    8, [6]       1, [3,5,6]    4, [5,6]  2, [6]   7, [6]       0, [5, 6]    5, [6]    4, [6]      10, [0]
0, [2,3,5,6]   2, [3,5,6]    1, [3,5,6]     4, [5,6]    0, [3,5,6]   3, [5,6]   1, [5,6]  6, [6]    X          X   0, [6]   5, [6]  X       X    X     X    X          X    X      X  X    X   X     X
          -1, [3,5,6] 2, [5,6]                                                          0,[6]  6,[]
'''

# Memoization - Cache
def coinSum(coins, total):
    # Write your code here
    cache = {}

    def helper_coinSum(coins, total, cache):
        coin_elem = ",".join(str(e) for e in coins)
        key = str(total)+'_'+coin_elem
        # print(f"coins: {coins}\n"
        #       f"total: {total}\n"
        #       f"cache: {cache}\n"
        #       f"key: {key}\n"
        #       f"\n")

        if key in cache:
            return cache[key]

        if total == 0:
            return 1

        if (total < 0) | (len(coins) == 0):
            return 0

        # left
        # removing first element result in moving all the elements of the list so we will remove last element
        left = helper_coinSum(coins, total-coins[len(coins)-1], cache)
        # print(f"Left: {left}")
        # right
        right = helper_coinSum(coins[0:len(coins)-1], total, cache)
        # print(f"Right: {right}")

        cache[key] = left + right

        return left + right

    final_result = helper_coinSum(coins, total, cache)
    return final_result


# Tabulation
'''
[2,5,3,6], 10
 val[i, j] = val[i-1, j] + val[i, j-col[len(col)-1]]
 
                 |   0   1   2   3   4   5   6   7   8   9   10
    -------------|-----------------------------------------------------
    []           |   1   0   0   0   0   0   0   0   0   0    0
    [2]          |   1   0   1   0   1   0   1   0   1   0    1
    [2,5]        |   1   0   1   0   1   1   1   1   1   1    2
    [2,5,3]      |   1   0   1   1   1   2   2   2   3   3    4
    [2,5,3,6]    |   1   0   1   1   1   2   3   2   4   4    5

'''
def coinSum(coins, total):
    # Write your code here

    coin_table = [[0 for i in range(0, total+1)] for j in range(len(coins)+1)]
                  # [0] * total
    for row in range(0, len(coins)+1):
        coin_table[row][0] = 1

    for row in range(1, len(coins)+1):
        for col in range(1, total+1):
            # print(f"Before: row: {row}, col: {col}, value: {coin_table[row][col]}")
            if col-coins[row-1] < 0:
                coin_table[row][col] = coin_table[row-1][col] + 0
            else:
                coin_table[row][col] = coin_table[row-1][col] + coin_table[row][col-coins[row-1]]

            # print(f"After: row: {row}, col: {col}, value: {coin_table[row][col]}")

    return coin_table[len(coins)][total]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    coins_count = int(input("Enter Coin Type Count: ").strip())
    coins = []

    for _ in range(coins_count):
        coins_item = int(input("Enter Coin Types: ").strip())
        coins.append(coins_item)

    total = int(input("Enter Total to be achieved: ").strip())

    result = coinSum(coins, total)
    print(f"Final Result: {result}")
    # fptr.write(str(result) + '\n')
    # fptr.close()
