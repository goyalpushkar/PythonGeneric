'''
Given an integer n, find all possible ways to position n queens on an n×n chessboard so that no two queens attack each other. A queen in chess can move horizontally, vertically, or diagonally.

Do solve the problem using recursion first even if you see some non-recursive approaches.

Example One
{
"n": 4
}
Output:

[
["--q-",
 "q---",
 "---q",
 "-q--"],

["-q--",
 "---q",
 "q---",
 "--q-"]
]
There are two distinct ways four queens can be positioned on a 4×4 chessboard without attacking each other. The positions may appear in the output in any order. So the same two positions in different order would be another correct output.

Example Two
{
"n": 2
}
Output:

[
]
No way to position two queens on a 2×2 chessboard without them attacking each other - so empty array.

Notes
The function must return a two-dimensional array of strings representing the arrangements. Size of the array must be m×n where m is the number of distinct arrangements.

Each string must be n characters long, and the strings' characters may be either q (for a queen) or - (for an empty position on the chessboard). Valid arrangements may appear in the output in any order.

Constraints:

1 <= n <= 12
'''

class Solution:
    def find_all_arrangements(n):
        """
        Args:
        n(int32)
        Returns:
        list_list_str
        """
        # Write your code here.
        # for n * n matrix there will 2n-1 diagonals e.g. 5 * 5 has 9 diagonals, 4 * 4 has 7 diagonals
        occupied_cols = [False for _ in range(n)]

        # diagonals are always number as row-col+n-1
        occupied_diagonals = [False for _ in range(2 * n - 1)]

        # back diagonals are always number as row+col
        occupied_back_diagonals = [False for _ in range(2 * n - 1)]

        final_sol = []

        def is_safe(p_row, p_col):
            if (occupied_cols[p_col] or occupied_diagonals[p_row + p_col]
                    or occupied_back_diagonals[p_row - p_col + n - 1]):
                return False
            else:
                return True

        def find_arrangements(sol, row):

            if len(sol) == n:
                final_sol.append(sol.copy())
                return
            else:

                for col in range(n):
                    if is_safe(row, col):
                        # add col to solution
                        sol.append(col)

                        # place q on board
                        occupied_cols[col] = True
                        occupied_diagonals[row + col] = True
                        occupied_back_diagonals[row - col + n - 1] = True

                        find_arrangements(sol, row + 1)

                        sol.pop()

                        # un place q on board
                        occupied_cols[col] = False
                        occupied_diagonals[row + col] = False
                        occupied_back_diagonals[row - col + n - 1] = False

        return_sol = []

        def create_return_sol():
            for arr in final_sol:
                # print(arr)
                create_arr = [['-' for _ in range(n)] for _ in range(n)]
                for row, col in enumerate(arr):
                    create_arr[row][col] = 'q'

                # print(create_arr)
                create_arr = ["".join(elem for elem in create_arr[row]) for row in range(len(create_arr))]
                # print(create_arr)
                return_sol.append(create_arr)

        find_arrangements([], 0)
        # print(final_sol)
        create_return_sol()

        return return_sol
