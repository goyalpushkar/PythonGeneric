'''
Given a two-dimensional binary matrix of size n * m, find the largest square submatrix with all 1s.

Example
{
"n": 3,
"m": 3,
"mat": [
[1, 0, 0],
[0, 1, 1],
[0, 1, 1]
]
}
Output:

2
2x2 submatrix at right-bottom has all 1s. That’s the largest one. Length of its side is 2.

Notes
Output is an integer, the length of the side of the largest square submatrix with all 1s.
Constraints:

1 <= n, m <= 1000
'''

def largest_sub_square_matrix(n, m, mat):
    """
    Args:
    n(int32)
    m(int32)
    mat(list_list_int32)
    Returns:
    int32
    """
    # Write your code here.
    max_size = 0
    
    # check if any has 1 in last row or last col
    for c in range(m):
        max_size = max(max_size, mat[n-1][c])
    
    for r in range(n):
        max_size = max(max_size, mat[r][m-1])
        
    for r in range(n-2, -1, -1):
        for c in range(m-2, -1, -1):
            if mat[r][c] == 1:
                mat[r][c] += min(mat[r+1][c+1], mat[r+1][c], mat[r][c+1]) 
                max_size = max(max_size, mat[r][c] )
                
    return max_size

# 20/23 - 2 Timeouts 1 wrong
def largest_sub_square_matrix(n, m, mat):
    """
    Args:
    n(int32)
    m(int32)
    mat(list_list_int32)
    Returns:
    int32
    """
    # Write your code here.
    
    visited = set()
    neighbors = [(0, 1), (1, 0)]
    def dfs(row, col):
        
        visited.add(str(row)+'_'+str(col))
        
        # for neighbor in neighbors:
        # left
        left = (row, col)
        new_row = row + 0
        new_col = col + 1
        if new_row < n and new_col < m and mat[new_row][new_col] == 1 and str(new_row)+'_'+str(new_col) not in visited:
            left = dfs(new_row, new_col)
            
        # down
        down = (row, col)
        new_row = row + 1
        new_col = col + 0
        if new_row < n and new_col < m and mat[new_row][new_col] == 1 and str(new_row)+'_'+str(new_col) not in visited:
            down = dfs(new_row, new_col)
            
        if left[0] == down[0]:
            return (left[0], max(left[1], down[1]))
        elif left[1] == down[1]:
            return (max(left[0], down[0]), left[1])
        else:
            return (min(left[0], down[0]), min(left[1], down[1]))
    
    max_size = 0
    for r in range(n):
        for c in range(m):
            visited = set()
            if mat[r][c] == 1:
                ret = dfs(r, c)
                l = ret[0] - r + 1
                b = ret[1] - c + 1
                if l == b:
                    max_size = max(max_size, l)
                
    return max_size
