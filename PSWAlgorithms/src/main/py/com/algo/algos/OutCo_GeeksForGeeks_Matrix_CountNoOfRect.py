'''
Given a rectangular matrix containing only the values “0” and “1”, where the values of “1” always appear in the form of a rectangular island and the islands are always separated row-wise and column-wise by at least one line of “0”s, count the number of islands in the given matrix. Note that the islands can diagonally adjacent.

Input: Matrix of elements with values either 0 or 1
Output: An integer which is the count of all rectangular islands
Example
Input: [[1, 1, 0, 1],
        [1, 1, 0, 1],
        [0, 0, 1, 0],
        [0, 0, 1, 0]]

Output: 3

Input: [[1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 1],
        [0, 0, 0, 1]]

Output: 3

Constraints
Time Complexity: O(MN)
Auxiliary Space Complexity: O(1)
The islands are all rectangular and the islands are always separated row-wise and column-wise by at least one line of 0s.

'''

class Solution:
    def numOfrectangle(self, matrix):
        # Check if X/1 value is the top left corner then it is a rectangle to be counted
        # else it is an adjacent X/1 to another already counted rectangle
        no_of_islands = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 'X':
                    if ((row-1 >= 0 and matrix[row-1][col] == '0') or (row-1 < 0 and True)) and \
                            ((col-1 >= 0 and matrix[row][col-1] == '0') or (col-1 <0 and True)):
                        no_of_islands += 1
                # print(f"row: {row}\tcol:{col}\tno_of_islands:{no_of_islands}")
        return no_of_islands


if __name__ == '__main__':

    mat = [['X','0','0','0','0','0'], ['X','0','X','X','X','X'], ['0','0','0','0','0','0'],
           ['X','X','X','0','X','X'], ['X','X','X','0','X','X'], ['0','0','0','0','X','X']]
    # [['0', '0', '0'],
    #  ['X', 'X', '0'],
    #  ['X', 'X', '0'],
    #  ['0', '0', 'X'],
    #  ['0', '0', 'X'],
    #  ['X', 'X', '0']] = 3
    solution = Solution()
    result = solution.numOfrectangle(mat)

    print(f"result: {result}")