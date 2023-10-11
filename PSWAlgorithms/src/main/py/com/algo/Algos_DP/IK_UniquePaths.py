'''
Given a grid of size n x m and a robot initially staying at the top-left position, return the number of unique paths for the robot to reach the bottom-right corner of the grid. The robot is allowed to move either down or right at any point in time.

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
    curr_row = [1 for _ in range(m)]
    # curr_row[0] = 0

    for row in range(1, n):
        for col in range(m):
            if col == 0:
                curr_row[col] = 1
            else:
                curr_row[col] += curr_row[col - 1]

        # print(curr_row)

    # print(curr_row)
    return curr_row[m - 1] % (10 ** 9 + 7)