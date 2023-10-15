'''
Each of the cells in a given square grid is assigned a value of either "0" or "1".

A grid cell is connected to another cell only if they share a common side. A connected component is a set of directly or 
indirectly connected cells, each with the value "1".

Find the largest possible size of a connected component achievable by changing the value of at most one cell from "0" to "1" in the grid.

Example One
{
"grid": [
[1, 0],
[0, 0]
]
}
Output:

2
Changing any of the two "0"s adjacent to the "1" forms a component of size 2.

Example Two
{
"grid": [
[1, 1],
[1, 1]
],
}
Output:

4
There are no cells with the value "0", so no operations can be performed. But the whole grid is already connected with size 4.

Notes
Constraints:

1 <= dimensions of the input grid <= 500
0 <= value of a cell in the grid <= 1

{
"grid": [
[1, 1],
[1, 1]
]
}

{
"grid": [
[1, 1, 1, 1, 1],
[1, 1, 1, 1, 1],
[1, 1, 0, 1, 1],
[1, 1, 1, 1, 1],
[1, 1, 1, 1, 1]
]
}

'''

# main idea is 
# Generate a group_id at the each start of the traversal for value 1
#   Mark all visited nodes with same group_id with which traversal is started
#   Prepare group size value map for group id and count of connected nodes
#   also collect zero values - row, col in a seperate array
# Once all 1 values are traversed, loop over zero value array
#   Check all adjacent group ids for current 0 value and take count for each distinct adjacent group id and add them + 1
#   keep track of max value in this loop
def largest_connected_component(grid):
    """
    Args:
    grid(list_list_int32)
    Returns:
    int32
    """
    # Write your code here.
    import math

    no_rows = len(grid)
    no_cols = len(grid[0])
    directions = [(-1,0,), (1,0), (0,-1), (0,1)]
    
    def dfs(row, col, group_id):
        # print(f"row: {row}, col: {col}")
        
        # visited
        grid[row][col] = group_id
        
        count = 1
        for dir in directions:
            new_row = row + dir[0]
            new_col = col + dir[1]
            
            if new_row >= 0 and new_row < no_rows and new_col >= 0 and new_col < no_cols and grid[new_row][new_col] == 1:
                count += dfs(new_row, new_col, group_id)
                # print(f"row: {row}, col: {col}, new_row: {new_row}, new_col: {new_col}, count: {count}")
            
        return count

    group_count = {}
    zero_values = []
    group_id = 100
    for row in range(no_rows):
        for col in range(no_cols):
            if grid[row][col] == 0:
                zero_values.append((row, col))
                continue
            
            if grid[row][col] == 1:
                curr_count = dfs(row, col, group_id)
                group_count[group_id] = curr_count
                
                group_id += 1
            
            # print(f"row: {row}, col: {col}, curr_count: {curr_count}, grid: {grid}, new_grid: {new_grid}")

    # print(f"group_count: {group_count}, zero_values: {zero_values}, grid: {grid}")
    
    # if there are no zero values i.e. all graph is connected then get the value from group_count for first group id
    if not zero_values:
        return group_count[100]
        
    max_connected = -math.inf
    for val in zero_values:
        curr_count = 1
        adj_group_ids = set()
        for dir in directions:
            new_row = val[0] + dir[0]
            new_col = val[1] + dir[1]
        
            # get group Id for adjacent cols
            # we need to get distinct adjacent group_ids because if all adjacent nodes are traversed using 
            # same group_id then it will duplciate the counts
            if new_row >= 0 and new_row < no_rows and new_col >= 0 and new_col < no_cols and grid[new_row][new_col] > 0:
                # curr_group_id = grid[new_row][new_col]
                adj_group_ids.add(grid[new_row][new_col])
        
        for group_id in adj_group_ids:
            curr_count += group_count[group_id]
        
        max_connected = max(max_connected, curr_count)
        
        
    return max_connected


# 4 Timeout 
def largest_connected_component(grid):
    """
    Args:
    grid(list_list_int32)
    Returns:
    int32
    """
    # Write your code here.
    import math
    
    no_rows = len(grid)
    no_cols = len(grid[0])
    directions = [(-1,0,), (1,0), (0,-1), (0,1)]
    visited= {}

    def dfs(row, col):
        # print(f"row: {row}, col: {col}")
        key = str(row) + "_" + str(col)
        
        # visited
        # grid[row][col] = 2
        visited[key] = True
        
        # dfs is called only when value is 1
        # if grid[row][col] == 0:
        #     return 0
            
        count = 1
        for dir in directions:
            new_row = row + dir[0]
            new_col = col + dir[1]
            new_key = str(new_row) + "_" + str(new_col)
            
            if new_row >= 0 and new_row < no_rows and new_col >= 0 and new_col < no_cols and grid[new_row][new_col] == 1 and new_key not in visited:
                count += dfs(new_row, new_col)
                # print(f"row: {row}, col: {col}, new_row: {new_row}, new_col: {new_col}, count: {count}")
            
        return count
    
    max_connected = -math.inf
    for row in range(no_rows):
        for col in range(no_cols):
            # new_grid = [[grid[i][j] for j in range(no_cols)] for i in range(no_rows)]
            visited = {}
            
            old_value = grid[row][col]
            if grid[row][col] == 0:
                grid[row][col] = 1
            
            curr_count = dfs(row, col)
            grid[row][col] = old_value
            
            # print(f"row: {row}, col: {col}, curr_count: {curr_count}, grid: {grid}, new_grid: {new_grid}")
            max_connected = max(max_connected, curr_count)
            
    return max_connected
    
