'''
Find the minimum path sum from top to bottom in a given triangular structure of numbers. For each step, movement to the adjacent cells
down from the current position is allowed i.e. from any index i in the current row, movement to index i or i + 1 in the next row is a valid movement.

Example
{
"triangle": [
[2],
[-4, -3],
[8, 3, 9],
[4, 2, 1, 6]
]
}
Output:

2
The triangle looks like:

            2
        -4      -3
    8       3       9
4       2       1       6
The minimum path sum from top to bottom is 2 + -4 + 3 + 1 = 2.

Notes
The ith row in the input list will have i + 1 elements.

Constraints:

1 <= size of the input list <= 103
-103 <= any element of the input list <= 103
'''
def get_minimum_path_sum(triangle):
    """
    Args:
    triangle(list_list_int32)
    Returns:
    int32
    """
    # Write your code here.
    rows = len(triangle)
    cols = len(triangle[rows-1])
    
    # tabulated matrix
    tab = [ [0 for i in range(cols)] for i in range(2)]
    
    curr_row = 1
    prev_row = 0
    for i in range(rows):
        # tab_row = i % 2
        
        for j in range(i+1):
            
            # if column is 0 then j-1 is negative
            if j == 0:
                tab[curr_row][j] = triangle[i][j] + tab[prev_row][j]
            # if it is the last column in the row then tab will not have value at jth position
            elif j == i:
                tab[curr_row][j] = triangle[i][j] + tab[prev_row][j-1]
            else:
                tab[curr_row][j] = triangle[i][j] + min( tab[prev_row][j], tab[prev_row][j-1] ) 
        
        # print(f"tab: {tab}")
        # copy curr_row to prev_row
        for i in range(cols):
            tab[prev_row][i] = tab[curr_row][i]
    
    # print(tab)
    return min(tab[curr_row])
