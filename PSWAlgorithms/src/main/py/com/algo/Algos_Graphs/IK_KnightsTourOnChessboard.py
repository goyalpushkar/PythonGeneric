'''
You are given a chessboard with rows rows and cols columns and a knight - that moves like in normal chess - located at the start_row-th row 
and start_col-th column. The knight needs to reach the position at the end_row-th row and end_col-th column.

Find minimum number of moves that knight needs to make to get from starting position to ending position.

start_row, start_col, end_row and end_col are all zero-indexed.

Example
{
"rows": 5,
"cols": 5,
"start_row": 0,
"start_col": 0,
"end_row": 4,
"end_col": 1
}
Output:

3
3 moves to reach from (0, 0) to (4, 1):
(0, 0) → (1, 2) → (3, 3) → (4, 1).

Notes
If it is not possible to reach from starting position to ending position, then return -1.
Constraints:

1 <= rows * cols <= 105
0 <= start_row, end_row < rows
0 <= start_col, end_col < cols
'''
def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):
    """
    Args:
     rows(int32)
     cols(int32)
     start_row(int32)
     start_col(int32)
     end_row(int32)
     end_col(int32)
    Returns:
     int32
    """
    # Write your code here.
    directions = [(-2,-1), (-2,1), (2,-1), (2,1), (1,2), (1,-2), (-1,2), (-1,-2)]
    visited = {}
    parent = {}
    node_traversal = deque()
    
    if start_row == end_row and start_col == end_col:
        return 0
    
    def bfs(row, col):
        # parent[(row, row)] = -1
        visited[(row, col)] = True
        node_traversal.append((row, col, 0))
        found = False
        
        level = 0
        while node_traversal:
            # no_of_nodes = len(node_traversal)
            curr_node = node_traversal.popleft()
            # print(f"curr_node: {curr_node}, node_traversal: {node_traversal}")
            for dir in directions:
                new_row = curr_node[0] + dir[0]
                new_col = curr_node[1] + dir[1]
                
                if new_row == end_row and new_col == end_col:
                    # parent[(new_row, new_col)] = (row, col)
                    visited[(new_row, new_col)] = True
                    found = True
                    level = curr_node[2] + 1
                    break
                
                if new_row >= 0 and new_row < rows and new_col >= 0 and new_col < cols and (new_row, new_col) not in visited:
                    # parent[(new_row, new_col)] = (row, col)
                    visited[(new_row, new_col)] = True
                    node_traversal.append((new_row, new_col, curr_node[2]+1))
    
            if found:
                return level
                
        return -1
    
    return bfs(start_row, start_col)
    
    # def get_path():
    #     result = []
    #     no_of_steps = 0
    #     if (end_row, end_col) in parent:
            
            
            
    #     else:
    #         return -1
    
    return 0

