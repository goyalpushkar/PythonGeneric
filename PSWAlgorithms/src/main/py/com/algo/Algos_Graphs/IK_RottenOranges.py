'''
Given a grid of numbers where each cell can have one of three values:

0: Represents an empty cell.
1: Represents a fresh orange.
2: Represents a rotten orange.
Every minute, any fresh orange that shares a side with a rotten orange also becomes rotten. 
Your task is to return the minimum time after which all the oranges will rot.

Example One
Example1 input grid

Output:

3
Example1 input grid

Example Two
Example1 input grid

Output:

-1
Example1 input grid

The orange at the bottom-right cell will never rot.

Notes
If there exists any orange that will never rot, return -1.

Constraints:

1 <= number of rows <= 1000
1 <= number of columns <= 1000
0 <= value of any cell <= 2
'''
def rotting_oranges(grid):
    """
    Args:
     grid(list_list_int32)
    Returns:
     int32
    """
    # Write your code here.
    
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    def bfs(fresh_oranges, total_time):
        # traverse_nodes.append((row, col))
        
        if not traverse_nodes:
            return fresh_oranges, 1
        
        while traverse_nodes:
            
            print(f"fresh_oranges: {fresh_oranges}, total_time: {total_time}, traverse_nodes: {traverse_nodes}")
            no_of_nodes = len(traverse_nodes)
            total_time += 1
            
            for i in range(no_of_nodes):
                curr_node = traverse_nodes.popleft()
                for dir in directions:
                    new_row = curr_node[0]+dir[0]
                    new_col = curr_node[1]+dir[1]
                    
                    if new_row >= 0 and new_row < len(grid) and new_col >= 0 and new_col < len(grid[0]) and grid[new_row][new_col] == 1:
                        fresh_oranges -= 1
                        grid[new_row][new_col] = 2
                        traverse_nodes.append((new_row, new_col))
        
        return fresh_oranges, total_time
    
    total_time = 0
    fresh_oranges = 0
    traverse_nodes = deque()
    for cur_row in range(len(grid)):
        for cur_col in range(len(grid[0])):
            
            if grid[cur_row][cur_col] == 1:
                fresh_oranges += 1
                
            if grid[cur_row][cur_col] == 2:
                traverse_nodes.append((cur_row, cur_col))
    
    fresh_oranges, total_time = bfs(fresh_oranges, total_time)  # cur_row, cur_col, 
                
    
    # for cur_row in range(len(grid)):
    #     for cur_col in range(len(grid[0])):
    #         if grid[cur_row][cur_col] == 1:
    #             return -1
    
    return total_time-1 if fresh_oranges == 0 and total_time > 0 else -1