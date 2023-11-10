'''
Given a two-dimensional board, count the number of battleships.

The following properties describe a board:

Any cell of the board is either a part of a battleship ('X') or empty ('.').
The shape of a battleship is either 1 x length or length x 1.
All the battleships are axis-aligned.
There are no two adjacent battleships, which means at least one horizontal or vertical cell separates between two battleships.
Example
{
"board": [
['X', '.', 'X', 'X', '.'],
['.', 'X', '.', '.', 'X'],
['.', '.', '.', '.', 'X'],
['.', '.', '.', '.', 'X'],
['.', '.', '.', '.', 'X']
]
}
Output:

4
Following are the locations of the four battleships on the board.

Battleship1 of shape 1 x 1 located at cell (0, 0).
Battleship2 of shape 1 x 2 located at cell (0, 2).
Battleship3 of shape 1 x 1 located at cell (1, 1).
Battleship4 of shape 4 x 1 located at cell (1, 4).
All the locations represent the top or left corner of a battleship.

Notes
Constraints:

1 <= number of rows and columns in the board <= 1000
Each cell of the board is either 'X' or '.'.
The length of a battleship will always be less than the size of any dimension of the board.
'''
def count_battleships(board):
    """
    Args:
    board(list_list_char)
    Returns:
    int32
    """
    # Write your code here.
    
    # It is to count number of connected components
    # Perform DFS over all of the unvisited elements 
    # In DFS mark the element and its neighbors as visited
    
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows = len(board)
    cols = len(board[0])
    
    visited = set()
    def dfs(row, col):
        
        # visited.add((row, col))
        # if board update is allowed mark some value on the board for visited
        board[row][col] = 'V'
        
        # visit neighbors 
        for neighbor in neighbors:
            new_row = row + neighbor[0]
            new_col = col + neighbor[1]
            
            if new_row >=0 and new_row < rows and new_col >= 0 and new_col < cols \
                and board[new_row][new_col] == 'X':
                dfs(new_row, new_col)
        
        return
    
    no_of_components = 0
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == 'X':
                dfs(row, col)
                no_of_components += 1
        
    return no_of_components


# IK Solution
def count_battleships(board):
    """
    Args:
    board(list_list_char)
    Returns:
    int32
    """
    # Write your code here.
    # each starting battleships top and left shouldnot be X i.e.
    # it should be empty (for top row and first col) or .
    counter = 0
    for row, row_val in enumerate(board):
        for col, col_val in enumerate(board[row]):
            if col_val == 'X':
                if (row == 0 or board[row-1][col] == ".") and (col == 0 or board[row][col-1] == "."):
                    counter += 1
        
    return counter