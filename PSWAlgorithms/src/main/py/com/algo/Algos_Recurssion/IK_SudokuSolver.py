'''
Given a partially filled two-dimensional array, fill all the unfilled cells such that each row, 
each column and each 3 x 3 subgrid (as highlighted below by bolder lines) has every digit from 1 to 9
 exactly once.

Unfilled cells have a value of 0 on the given board.

Example
Example one

{
"board": [
[8, 4, 9, 0, 0, 3, 5, 7, 0],
[0, 1, 0, 0, 0, 0, 0, 0, 0],
[7, 0, 0, 0, 9, 0, 0, 8, 3],
[0, 0, 0, 9, 4, 6, 7, 0, 0],
[0, 8, 0, 0, 5, 0, 0, 4, 0],
[0, 0, 6, 8, 7, 2, 0, 0, 0],
[5, 7, 0, 0, 1, 0, 0, 0, 4],
[0, 0, 0, 0, 0, 0, 0, 1, 0],
[0, 2, 1, 7, 0, 0, 8, 6, 5]
]
}
Output:

[
[8, 4, 9, 1, 6, 3, 5, 7, 2],
[3, 1, 5, 2, 8, 7, 4, 9, 6],
[7, 6, 2, 4, 9, 5, 1, 8, 3],
[1, 5, 3, 9, 4, 6, 7, 2, 8],
[2, 8, 7, 3, 5, 1, 6, 4, 9],
[4, 9, 6, 8, 7, 2, 3, 5, 1],
[5, 7, 8, 6, 1, 9, 2, 3, 4],
[6, 3, 4, 5, 2, 8, 9, 1, 7],
[9, 2, 1, 7, 3, 4, 8, 6, 5]
]
Notes
You can assume that any given puzzle will have exactly one solution.

Constraints:

Size of the input array is exactly 9 x 9
0 <= value in the input array <= 9
'''

def solve_sudoku_puzzle(board):
    """
    Args:
    board(list_list_int32)
    Returns:
    list_list_int32
    """
    # Write your code here.
    len_rows = len(board)
    len_cols = len(board[0])
    # def check_everything_filled(row, col):
    #     for r in range(row, len_rows):
    #         for c in range(col, len_cols):
    #             if board[r][c] == 0:
    #                 return False
                    
    #     return True
        
    # def print_board(row, col):
    #     for r in range(row, len_rows):
    #         for c in range(col, len_cols):
    #             print(board[r][c])
    
    def check_safe(row, col, val):
        # validate row values
        for c in range(len_cols):
            if c != col and board[row][c] == val:
                return False
    
        # validate col values
        for r in range(len_rows):
            if r != row and board[r][col] == val:
                return False     
            
        # validate square values
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for r in range(row_start, row_start+3):
            for c in range(col_start, col_start+3):
                if r != row and c != col and board[r][c] == val:
                    return False  
                
        return True
        
    def get_next_empty(row, col):
        # if all cols are filled for this row then move to next row
        # while True:
        #     while row < len_rows and col < len_cols and board[row][col] != 0:
        #         col += 1
                
        #         # if all cols are filled for this row then move to next row
        #         if col == len_cols:
        #             row += 1
        #             col = 0
                    
        #     return row, col
        for r in range(row, len_rows):
            for c in range(0, len_cols):
                if board[r][c] == 0:
                    return r, c

        return len_rows, len_cols
    
    def rec(row, col):
        # print(f"row: {row}, col: {col}, board: {board}")
        
        e_row, e_col = get_next_empty(row, col)
        # if next empty is outside the box return True
        if e_row >= len_rows or e_col >= len_cols:
            return True
        
        for i in range(1, 10):
            # if value is safe to fill
            # print(f"e_row: {e_row}, e_col: {e_col},i: {i}")
            if check_safe(e_row, e_col, i):   # board[row][col] == 0 and 
                # print(f"e_row: {e_row}, e_col: {e_col}, i: {i}")
                board[e_row][e_col] = i
                
                if rec(e_row, e_col):
                    return True
                else:
                    board[e_row][e_col] = 0
            
                
        return False

    rec(0, 0)
    return board
