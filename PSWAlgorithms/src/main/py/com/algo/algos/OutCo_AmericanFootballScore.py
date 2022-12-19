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
def footballScore(coins, total):
    # Write your code here


    return 0

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    coins_count = int(input("Enter Coin Type Count: ").strip())
    coins = []

    for _ in range(coins_count):
        coins_item = int(input("Enter Coin Types: ").strip())
        coins.append(coins_item)

    total = int(input("Enter Total to be achieved: ").strip())

    result = footballScore(coins, total)
    print(f"Final Result: {result}")
    # fptr.write(str(result) + '\n')
    # fptr.close()
