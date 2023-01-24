'''
Given a matrix with N rows and M columns where elements in the matrix can be either 1 or 0 and each row and column
are sorted in ascending order, find the number of 1s.

Input: Matrix of elements with values either 0 or 1
Output: An integer which is the count of all 1’s in the matrix

Example
Input:  [[0, 0, 0, 1],
		[0, 0, 1, 1],
		[0, 1, 1, 1],
		[0, 1, 1, 1]]

Output: 9
Constraints
Time Complexity: O(N + M)
Auxiliary Space Complexity: O(1)
Each row and column of the matrix is sorted in ascending order.

Values of the matrix will be either 0 or 1.
'''
class Solution:
    def countOnes(self, matrix):
        result = 0

        row_len = len(matrix)
        col_len = len(matrix[0])

        row = 0
        while row >= 0 and row < row_len:
            col = 0
            while col >= 0 and col < col_len:
                if matrix[row][col] == 1:
                    # Add 1 for all rows from the current row to row_len and for all subsequent columns
                    result += 1 * (row_len-row) * (col_len-col)
                    col_len = col

                col += 1

            row += 1

        return result

if __name__ == '__main__':
    mat = [[0,0,1],[0,0,1],[0,0,1]]


    '''
    [[0,0,1],[0,1,1],[1,1,1]] - 6 
    [[1,1,1],[1,1,1],[1,1,1]] - 9
    [[0,0,1],[0,0,1],[0,0,1]] - 3
    
    [[0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 1, 1, 1],
    [0, 1, 1, 1]]
    11
    
    [[0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 1, 1, 1]]
       9 
    '''

    solution = Solution()
    result = solution.countOnes(mat)

    print(f"result: {result}")