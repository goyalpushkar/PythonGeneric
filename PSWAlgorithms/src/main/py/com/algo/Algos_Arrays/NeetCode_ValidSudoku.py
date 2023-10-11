'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


Example 1:
Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are
 two 8's in the top left 3x3 sub-box, it is invalid.


Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
'''
class Solution:
    def isValidSudoku_1st(self, board):
        row_dict = defaultdict(set())
        col_dict = defaultdict(set())
        sq_dict = defaultdict(set())

        for row in range(9):
            for col in range(9):
                value = board[row][col]
                square = (row // 3) * 3 + (col // 3)
                if value == ".":
                    continue

                if value in row_dict[row] or value in col_dict[col] or value in sq_dict[square]:
                    return False

                row_dict[row].add(value)
                col_dict[col].add(value)
                sq_dict[square].add(value)

        return True

    # Beats 86.99% 92 ms
    def isValidSudoku_1st(self, board):
        board_set = {i: [] for i in range(1, 10)}
        first_set = [0, 1, 2]
        second_set = [3, 4, 5]
        third_set = [6, 7, 8]

        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    # value = col + row * 9
                    board_set[int(board[row][col])].append((row, col))  # value

        # print(f"board_set: {board_set}")
        for key in board_set.keys():
            row_set = set()
            col_set = set()
            sq_set = set()

            # print(f"key: {key}")
            for pos in board_set[key]:
                # row = pos // 9
                # col = pos % 9
                row = pos[0]
                col = pos[1]

                # print(f"pos: {pos}\trow: {row}\tcol: {col}")
                # Row validation
                if row in row_set:
                    return False
                else:
                    row_set.add(row)

                # Col validation
                if col in col_set:
                    return False
                else:
                    col_set.add(col)

                # Square validation
                if row in first_set and col in first_set:
                    if 1 in sq_set:
                        return False
                    else:
                        sq_set.add(1)
                elif row in first_set and col in second_set:
                    if 2 in sq_set:
                        return False
                    else:
                        sq_set.add(2)
                elif row in first_set and col in third_set:
                    if 3 in sq_set:
                        return False
                    else:
                        sq_set.add(3)
                elif row in second_set and col in first_set:
                    if 4 in sq_set:
                        return False
                    else:
                        sq_set.add(4)
                elif row in second_set and col in second_set:
                    if 5 in sq_set:
                        return False
                    else:
                        sq_set.add(5)
                elif row in second_set and col in third_set:
                    if 6 in sq_set:
                        return False
                    else:
                        sq_set.add(6)
                elif row in third_set and col in first_set:
                    if 7 in sq_set:
                        return False
                    else:
                        sq_set.add(7)
                elif row in third_set and col in second_set:
                    if 8 in sq_set:
                        return False
                    else:
                        sq_set.add(8)
                elif row in third_set and col in third_set:
                    if 9 in sq_set:
                        return False
                    else:
                        sq_set.add(9)

        return True