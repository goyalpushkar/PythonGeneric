'''
Given the total number of rows and columns of a two-dimensional grid with a list of location points for update operations, count the total number of islands after each update operation.

The grid represents a map where 0 represents water and 1 represents land. Initially, all of the cells of the grid are assumed to be water cells.

An update operation on a point turns the water at that specific location into land.

Return an array of integers where the ith element is the number of islands after applying the ith operation.

Example One
{
"row_count": 2,
"column_count": 2,
"update_positions": [
[0, 0],
[1, 1],
[0, 1],
[1, 0]
]
}
Output:

[1, 2, 1, 1]
Explanation: Initially the grid looks as following:

0 0
0 0
After the 1st update operation at location (0, 0), it becomes:

1 0
0 0
Total number of islands is 1 now. After the 2nd update, it looks like following:

1 0
0 1
Now, the total number of islands becomes 2.

Example Two
{
"row_count": 3,
"column_count": 3,
"update_positions": [
[0, 0],
[0, 2],
[0, 1],
[2, 1],
[1, 1]
]
}
Output:

[1, 2, 1, 2, 1]
Notes
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. It can be assumed that all four edges of the grid are all surrounded by water.

Constraints:

1 <= number of rows, columns <= 104
1 <= number of rows * number of columns <= 106
1 <= update operations <= 106
All update locations will be distinct, valid, and inside the grid.
.
.
.
.
.

Autocomplete

I/O
    #     count_of_islands = 0
    #     for row in range(1, row_count+1):

'''

def number_of_islands_after_each_operation(row_count, column_count, update_positions):
    """
    Args:
    row_count(int32)
    column_count(int32)
    update_positions(list_list_int32)
    Returns:
    list_int32
    """
    # Write your code here.

    
# 5/7
def number_of_islands_after_each_operation(row_count, column_count, update_positions):
    """
    Args:
    row_count(int32)
    column_count(int32)
    update_positions(list_list_int32)
    Returns:
    list_int32
    """
    # Write your code here.
    # add an extra row and col to handle fist row and col conditions
    grid = [ [0 for i in range(column_count+1)] for i in range(row_count+1)]
    neighbors = [(-1,0), (1,0), (0,-1), (0,1)]
    # if top and left position is water then its an island
    # otherwise it is connected to land and not an island
    # this didnt work
    # def count_islands(grid):
    #     count_of_islands = 0
    #     for row in range(1, row_count+1):
    #         for col in range(1, column_count+1):
    #             if grid[row][col] == 1:
                    
    #                 if row-1 >= 0 and grid[row-1][col] == 0 and col-1 >= 0 and grid[row][col-1] == 0: 
    #                   count_of_islands += 1    
        
    #     return count_of_islands
    
    def safe(row, col, visited):
        # print(visited)
        if row >= 0 and row < row_count+1 and col >= 0 and col < column_count+1 \
            and grid[row][col] == 1 and (row, col) not in visited:
            return True
        else:
            return False
    
    def dfs(row, col, visited):
        visited[(row, col)] = 1
        
        for neigh in neighbors:
            new_row = row + neigh[0]
            new_col = col + neigh[1]
            # print(row, col, new_row, new_col, visited)
            if safe(new_row, new_col, visited):
                dfs(new_row, new_col, visited)
        
        # return visited
        
    def count_islands(grid):
        count_of_islands = 0
        visited = {}
        for row in range(1, row_count+1):
            for col in range(1, column_count+1):
                if grid[row][col] == 1 and (row, col) not in visited:
                    dfs(row, col, visited)
                    count_of_islands += 1
        
        return count_of_islands
        
    def print_grid():
        for row in range(1, row_count+1):
            print(grid[row])

    final_output = []
    for oper in update_positions:
        # print(oper)
        grid[oper[0]+1][oper[1]+1] = 1
        # print_grid()
        ret_value = count_islands(grid)
        # print(ret_value)
        final_output.append(ret_value)
        
    return final_output