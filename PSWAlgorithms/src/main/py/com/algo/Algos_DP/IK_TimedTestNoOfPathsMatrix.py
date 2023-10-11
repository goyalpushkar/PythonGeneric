'''
Given a matrix n by m containing 0s and 1s, find the number of distinct paths from cell (0, 0) to cell (n - 1, m - 1) that

step on cells with 1s and
go only down or to the right.
Example:

Example

There are two possible paths from the cell (0, 0) to cell (1, 3) in this example.

Return the number of paths modulo (109 + 7).

Example One
{
"matrix": [
[1, 1, 1, 1],
[1, 1, 1, 1],
[1, 1, 1, 1]
}
Output:
10
Example one

There are 10 possible paths from cell (0, 0) to cell (2, 3).

Example Two
{
"matrix": [
[1, 1],
[0, 1]
]
}
Output:
1
Example two

There is 1 possible path from the cell (0, 0) to cell (1, 1).

Notes
Constraints:
1 <= n * m <= 2 * 106
Each cell of the given matrix contains either 0 or 1
'''


def number_of_paths(matrix):
    """
    Args:
     matrix(list_list_int32)
    Returns:
     int32
    """
    # Write your code here.
    row_size = len(matrix)
    col_size = len(matrix[0])

    memo = {}

    def no_paths_rec(row, col):
        key = str(row) + '_' + str(col)
        # print(key)

        if key in memo:
            return memo[key]

        if row >= row_size or col >= col_size or matrix[row][col] == 0:
            return 0

        if row == row_size - 1 and col == col_size - 1:
            return 1

        total_paths = no_paths_rec(row + 1, col) + no_paths_rec(row, col + 1)
        # print(total_paths)
        memo[key] = total_paths % (10**9+7)
        return memo[key]

    return no_paths_rec(0, 0)

def number_of_paths_tab(matrix):
    """
        Args:
         matrix(list_list_int32)
        Returns:
         int32
        """
    # Write your code here.
    # tab = [matrix[0][i] if ( i-1 >= 0 and matrix[0][i-1] != 0 or i== 0 and matrix[0][i-1] != 0) else 0 for i in range(len(matrix[0]))]
    tab = [matrix[0][i] for i in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        if i == 0:
            tab[i] = matrix[0][i]
        else:
            tab[i] *= matrix[0][i - 1]

    for row in range(1, len(matrix)):
        for col in range(len(matrix[0])):
            if col == 0:
                tab[col] = matrix[row][col]
                continue

            if tab[col] != 0:
                tab[col] += tab[col - 1]
            else:
                tab[col] = 0
    #     print(tab)

    print(tab)
    return tab[-1] % (10 ** 9 + 7)