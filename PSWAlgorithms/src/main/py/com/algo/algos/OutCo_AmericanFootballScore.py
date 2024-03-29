'''
In a simplified game of American football, teams score points by either achieving a touchdown (7 points) or a
field goal (3 points).

Given the score for a single team, please return how many different permutations of touchdowns and/or field goals exist
in order to arrive at that score.

Input: Integer
Output: Integer
Examples
Input:  10
Output: 2

Explanation: For a score of 10, the output would be 2. The 2 ways to arrive at
this score is to:

1) Score a field goal (3 points) and then touchdown (7 points)
2) Score a touchdown (7 points) and then field goal (3 points)


Input: 21
Output: 2

Explanation: For a score of 21, the output would be 2. The 2 ways to arrive at
this score is to:

1) Score 7 field goals (3 * 7 points)
2) Score 3 touchdowns (7 * 3 points)


Input:  16
Output: 4

Explanation: For a score of 16, the output would be 4. The 4 ways to arrive at
this score is to:

1) Score 1 touchdown (7 points) and 3 field goals (3 * 3 points)
2) Score 1 field goal (3 points), then 1 touchdown (7 points), and then 2 field goals (2 * 3 points)
3) Score 2 field goals (2 * 3 points), then 1 touchdown (7 points), and lastly 1 field goal (3 points)
4) Score 3 field goals (3 * 3 points) and then 1 touchdown (7 points)


Constraints
Time Complexity: O(2^N)
Auxiliary Space Complexity: O(N)

'''

# Tabulation
'''

Combinations
[2,5,3,6], 10
 val[i, j] = val[i-1, j] + val[i, j-col[len(col)-1]]

                 |   0   1   2   3   4   5   6   7   8   9   10
    -------------|-----------------------------------------------------
    []           |   1   0   0   0   0   0   0   0   0   0    0
    [2]          |   1   0   1   0   1   0   1   0   1   0    1
    [2,5]        |   1   0   1   0   1   1   1   1   1   1    2
    [2,5,3]      |   1   0   1   1   1   2   2   2   3   3    4
    [2,5,3,6]    |   1   0   1   1   1   2   3   2   4   4    5
    
Permutations


         |   []    [2]    [2,5]    [2,5,3]     [2,5,3,6]
    -------------------------------------------------------------------
    0    |   1      1       1          1           1   
    1    |   0      0       0          0           0   
    2    |   0      1       1          1           1   
    3    |   0      0       0          1           1   
    4    |   0      1       1          1           1   
    5    |   0      0       1          2           2   
    6    |   0      1       1          2           3   
    7    |   0      0       2          5           5   
    8    |   0      1       1          3           5   
    9    |   0      0       3          4           5   
    10   |   0      1       2          8           11   

[2,5,3,6], 10
2,5,3 | 2,2,2,2,2 | 3,3,2,2 | 6,2,2 | 5,5

2,3,5 | 2,5,3 | 3,2,5 | 3,5,2 | 5,2,3 | 5,3,2 | 2,2,6 | 6,2,2 | 2,2,2,2,2 | 3,3,2,2 | 3,2,3,2 | 3,2,2,3 | 
2,2,3,3 | 2,3,3,2 | 2,3,2,3 | 5,5
                                                                                                        10, [2,5,3,6]
                                               10,[5,3,6]                                                                                                            8,[2,5,3,6]
               10,[3,6]                                                            5,[5,3,6]                                             8,[5,3,6]                                                 6,[2,5,3,6]    
      10,[6]                     7,[3,6]                                     5,[3,6]        0,[5,3,6]                  8,[5,3,6]                        3,[5,3,6]                   6,[5,3,6]                     4,[2,5,3,6]   
  10,[]    4,[6]        7,[6]                     4,[3,6]            5,[6]          2,[5,6]    YYYY         8,[3,6]                3,[3,6]          3,[3,6]    -2,[5,3,6]    6,[3,6]          1,[3,6]    4,[5,3,6]                2,[2,5,3,6]
   X    4,[] -2,[6]  7,[]   1,[6]          4,[6]         1,[3,6]   5,[]  -1,[6]  2,[6]   -3,[5,6]      8,[6]      5,[3,6]       3,[6]    0,[3,6]  3,[6]  0,[3,6]   X   6,[6]       3,[3,6]       |    4,[3,6] -1,[5,3,6]   2,[2,5,3,6]       0,[2,5,3,6]
         X     X      X   1,[] -5,[6]  4,[6] -2,[6] 1,[6]  -2,[3,6] X      X      |          X     8,[6]  2,[6] 5,[6] 2,[3,6] 3,[] -3,[6] YYYY     |       YYYY      6,[] 0,[6]  3,[6]  0,[3,6]  X     X          X    2,[5,3,6]  0,[2,5,3,6]    YYYYY
                            X     X      X      X     X         X              X      X             |      |     |      |                         X  X                 X   YYYY   X      YYYY                              X         YYYY
                                                                                                  X   X  X   X X   X  X    X
                                                                                                                                             
YYYY - 5,5 | 2,5,3 | 6,2,2 | 3,3,2,2 | 2,2,2,2,2

16, [7,3]

                                            16
                       9(-7)                                       13(-3)
              2(-7)              6(-3)                   6(-7)                     10(-3)
         -5(-7)   -1(-3)   -1(-7)     3(-3)        -1(-7)     3(-3)           3(-7)       7(-3)
          X         X         X   -4(-7)  0(-3)      X   -4(-7)  0(-3)     -4(-7) 0(-3) 0(-7) 4(-3)
                                          YYYY              X      YYYY      X    YYYY  YYYY -3(-7) 1(-3)
                                                                                               X      XX
7,3,3,3  |  3,7,3,3  |  3,3,7,3  |   3,3,3,7                                                        
'''


def coinSum(coins, total):
    # Write your code here
    result = 0
    def helper(result, total):

        if total < 0:
            return result

        if total == 0:
            result += 1
            return result

        # # left
        # result = helper(result, total-7)
        #
        # # right
        # result = helper(result, total-3)

        for coin in coins:
            result = helper(result, total-coin)

        return result

    result = helper(result, total)

    return result


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
