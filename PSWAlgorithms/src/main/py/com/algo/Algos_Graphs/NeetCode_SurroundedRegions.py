'''
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example 1:
Input: board = [["X","X","X","X"],
                ["X","O","O","X"],
                ["X","X","O","X"],
                ["X","O","X","X"]]
Output: [["X","X","X","X"],
         ["X","X","X","X"],
         ["X","X","X","X"],
         ["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.

Example 2:
Input: board = [["X"]]
Output: [["X"]]

Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
    0   1   2   3   4   5
[["O","O","O","O","X","X"],
 ["O","O","O","O","O","O"],
 ["O","X","O","X","O","O"],
 ["O","X","O","O","X","O"],
 ["O","X","O","X","O","O"],
 ["O","X","O","O","O","O"]]

Expected:
[["O","O","O","O","X","X"],
["O","O","O","O","O","O"],
["O","X","O","X","O","O"],
["O","X","O","O","X","O"],
["O","X","O","X","O","O"],
["O","X","O","O","O","O"]]

Output:
[["O","O","O","O","X","X"],
["O","O","O","O","O","O"],
["O","X","O","X","O","O"],
["O","X","O","X","X","O"],
["O","X","O","X","O","O"],
["O","X","O","O","O","O"]]


'''
class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        def verify(row, col):
            # print(f"{row} {col}")
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != 'O':
                return

            # print("Set value to T")
            board[row][col] = 'T'
            verify(row - 1, col)
            verify(row + 1, col)
            verify(row, col - 1)
            verify(row, col + 1)

        # 1. Capture unsurrounded regions (O -> T)
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O' and (row in [0, rows - 1] or col in [0, cols - 1]):
                    verify(row, col)

        # print(f"board 1: {board}")
        # 2. Capture surrounded regions (O -> X)
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    # print("Set X")
                    board[row][col] = 'X'

        # print(f"board 2: {board}")
        # 3. Uncapture unsurrounded regions (T -> 0)
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'T':
                    # print("Set O")
                    board[row][col] = 'O'

        # print(f"board 3: {board}")

        return board

    def solve_better(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        def verify(row, col):
            # print(f"{row} {col}")
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != 'O':
                return

            # print("Set value to T")
            board[row][col] = 'T'
            verify(row - 1, col)
            verify(row + 1, col)
            verify(row, col - 1)
            verify(row, col + 1)

        for i in range(rows):
            verify(i, 0)
            verify(i, cols - 1)
        for i in range(cols):
            verify(0, i)
            verify(rows - 1, i)
        for i in range(rows):
            for j in range(cols):
                board[i][j] = 'X' if board[i][j] != 'T' else 'O'

        # visited = [[0 for col in range(cols)] for row in range(rows)]

        # def verify(row, col):
        #     print(f"{row} {col}")
        #     if row < 0 or row >= rows or col < 0 or col >= cols:  # or board[row][col] == '0' or visited[row][col] == 1
        #         return False
        #
        #     print(f" visited: {visited[row][col]} - board: {board[row][col]}")
        #     if board[row][col] == 'X' or visited[row][col] == 1:  # or visited[row][col] == 1  or visited[row][col] == 1
        #         return True
        #     else:
        #         visited[row][col] = 1
        #         # board[row][col] = 'X'
        #         if verify(row - 1, col) and verify(row + 1, col) and verify(row, col - 1) and verify(row, col + 1):
        #             board[row][col] = 'X'
        #             return True
        #         # else:
        #         #     board[row][col] = 'O'
        #         #     return False
        #
        #     return False

        # for row in range(rows):
        #     for col in range(cols):
        #         if board[row][col] == 'O':
        #             # verify
        #             verify(row, col)
        #             # if verify(row-1, col) and verify(row+1, col) and verify(row, col-1) and verify(row, col+1):
        #             #     board[row][col] = 'X'
        #             print(f"board: {board} \n\n")