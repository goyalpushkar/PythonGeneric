'''
Write an efficient algorithm that searches for a value in an M x N matrix. This matrix has the following properties:

Integers in each row are sorted from left to right
The first integer of each row is greater than the last integer of the previous row.
Input: Matrix of Integers, Target Integer
Output: Boolean
Example
Example 1:
Input:

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

target = 3
Output: True

Example 2:
Input:

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

target = 13
Output: False

Constraints
Time Complexity: O(log (N*M)) with M being the number of rows and N being the number of columns.
Auxiliary Space Complexity: O(1)

https://leetcode.com/problems/search-a-2d-matrix/

'''
import math

class Solution:
    # beats 82.91% - old-beats 57.7%
    def searchMatrix(self, matrix, target):
        import math
        row_len = len(matrix)
        col_len = len(matrix[0])

        # get row
        def get_row(low, high):
            while low <= high:
                mid = math.floor(high - (high - low) / 2)

                # Performance improvement adding other or and and conditions
                if (target == matrix[mid][0] or matrix[mid][-1] == target) or (target >= matrix[mid][0] and target <= matrix[mid][-1]):
                    return mid

                if target <= matrix[mid][0]:
                    low = min(low, mid)
                    high = mid - 1
                else:
                    low = mid + 1

            return low - 1

        # search in the row
        row = get_row(0, len(matrix) - 1)

        def search_row(low, high):
            while low <= high:
                mid = math.floor(high - (high - low) / 2)

                if target == matrix[row][mid]:
                    return True

                if target <= matrix[row][mid]:
                    low = min(low, mid)
                    high = mid - 1
                else:
                    low = mid + 1

            return False  # low-1

        return search_row(0, len(matrix[0]) - 1)

    # beats 12.16 %
    def searchMatrix_old(self, matrix, target):
        import math
        row_len = len(matrix)
        col_len = len(matrix[0])
        min_row, max_row = 0, row_len

        def check_value(min_row, max_row):
            while min_row < max_row:
                min_col, max_col = 0, col_len

                # Get mid_row
                mid_row = math.floor( min_row + ( max_row - min_row ) / 2 )

                if check_row(mid_row, min_col, max_col):
                    return True

                # Check if we need to search on upper half or lower half of the matrix
                if target > matrix[mid_row][0]:
                    min_row, max_row = mid_row+1, max_row
                else:
                    min_row, max_row = min_row, mid_row

        def check_row(row, min_col, max_col):
            while min_col < max_col:
                # Get mid_col
                mid_col = math.floor(min_col + (max_col - min_col)/2)

                if target == matrix[row][mid_col]:
                    return True

                # Check if we need to search on left half or right half of the matrix
                if target > matrix[row][mid_col]:
                    min_col, max_col = mid_col+1, max_col
                else:
                    min_col, max_col = min_col, mid_col

            return False

        if check_value(min_row, max_row):
            return True

        return False


if __name__ == '__main__':
    mat = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        # [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = int(input("Enter value to be searched: "))
    solution = Solution()
    result = solution.searchMatrix(mat, target)

    print(f"result: {result}")