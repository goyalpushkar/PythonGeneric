'''
Given a grid with several walls, gates, and empty rooms, find the distance from each room to its nearest gate.

One cannot make a move to a cell containing a wall. A movement can be made in any of the four directions within the grid (UP, DOWN, LEFT, RIGHT).

Representations:

-1 : A wall.
0 : A gate.
INF : An empty room. The value 231-1 = 2147483647 has been used to represent INF.
Example One
{
"grid": [
[2147483647, 2147483647, 0, 2147483647],
[2147483647, 2147483647, 2147483647, -1],
[0, -1, -1, -1],
[2147483647, 2147483647, 2147483647, 0]
]
}
Output:

[
[2, 1, 0, 1],
[1, 2, 1, -1],
[0, -1, -1, -1],
[1, 2, 1, 0]
]
Example Two
{
"grid": [
[0, -1],
[-1, 2147483647]
]
}
Output:

[
[0, -1],
[-1, 2147483647]
]
Notes
Gates that are not reachable from any room should be filled with INF.

Constraints:

1 <= number of rows and columns in grid <= 500
'''
def find_closest_gates(grid):
    """
    Args:
    grid(list_list_int32)
    Returns:
    list_list_int32
    """
    # Write your code here.
    from collections import deque
    neighbors = [(-1,0),(1,0),(0,-1),(0,1)]

    def valid(row, col):
        if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]):
            return True
        else:
            return False
        
    traverse_queue = deque()

    # add all 0 value cols into the queue
    for row, row_val in enumerate(grid):
        for col, col_val in enumerate(grid[row]):
            if col_val == 0:
                traverse_queue.append((row, col))
        
    # Traverse from all 0 columns to mark their neighbors
    while traverse_queue:
        curr = traverse_queue.popleft()

        for neighbor in neighbors:
            new_row = curr[0] + neighbor[0]
            new_col = curr[1] + neighbor[1]
            if valid(new_row, new_col):
                if grid[curr[0]][curr[1]] + 1 < grid[new_row][new_col]:
                    grid[new_row][new_col] = grid[curr[0]][curr[1]] + 1
                    traverse_queue.append((new_row, new_col))

    return grid

# Loop over all the empty rooms
# call bfs/dfs for each room until 0 is found. 
    # increase the level by 1 for each neighbor traverse
    # check the min_so_far and set the min for parent
# 2 failed with wrong values Shortest path problem - BFS should be used
def find_closest_gates(grid):
    """
    Args:
    grid(list_list_int32)
    Returns:
    list_list_int32
    """
    # Write your code here.
    import math
    
    neighbors = [(-1,0),(1,0),(0,-1),(0,1)]
    mem = {}
    visited = {}
    def dfs(row, col):
        print(f"visit row: {row}, col: {col}, mem: {mem}")
        visited[(row, col)] = 1
        
        if (row, col) in mem:
            visited[(row, col)] = 0
            return mem[(row, col)]
            
        if grid[row][col] == 0:
            mem[(row, col)] = 0
            visited[(row, col)] = 0
            return 0
        
        min_value = math.inf
        child_level = 1
        for neighbor in neighbors:
            new_row = row + neighbor[0]
            new_col = col + neighbor[1]
            # print(f"\t\tnew_row: {new_row}, new_col: {new_col}, min_value: {min_value}")
            if valid(new_row, new_col) and ( (new_row, new_col) not in visited or visited[(new_row, new_col)] == 0):
                child_level += dfs(new_row, new_col)    
                # print(f"\t\t\tnew_row: {new_row}, new_col: {new_col}, child_level1: {child_level1}")
                # child_level += child_level1 
                min_value = min(min_value, child_level)
            # elif (new_row, new_col) in mem:
            #     child_level += mem[(new_row, new_col)]
            #     min_value = min(min_value, child_level)
        
        visited[(row, col)] = 0
        print(f"\nvisit row: {row}, col: {col}, min_value: {min_value}")
        mem[(row, col)] = min_value
        return min_value
        
    def valid(row, col):
        if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and grid[row][col] != -1:
            return True
        else:
            return False
        
        
    for row, row_val in enumerate(grid):
        for col, col_val in enumerate(grid[row]):
            # if (row, col) in mem:
            #     grid[row][col] = mem[(row, col)]
            if col_val == 0 or col_val == -1:
                continue
            elif valid(row, col):
                value = dfs(row, col)
                # print(f"row: {row}, col: {col}, value: {value}")
                if value == math.inf:
                    grid[row][col] = 2147483647
                else:
                    grid[row][col] = value
    
    return grid