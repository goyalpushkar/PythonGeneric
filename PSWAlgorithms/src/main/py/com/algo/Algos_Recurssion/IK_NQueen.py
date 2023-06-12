'''

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
