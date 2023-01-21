'''
Given an (MxN) matrix of integers, return an array in spiral order.

Input: Array of integers
Output: Array of integers
Example
Input: [[1,2,3],
        [4,5,6],
        [7,8,9]]

Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

Input: [[]]
Output: []


Constraints
Time Complexity: O(MN)
Auxiliary Space Complexity: O(MN)
Values of the array will be digits 0-9.


Must account long or tall matrices:
Input: [[1,2,3,4]]
Output: [1, 2, 3, 4]

TripleByte has asked this problem on their final round.

'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        return_array = []
        row_len = len(matrix)
        col_len = len(matrix[0])

        start_row = 0
        end_row = row_len

        start_col = 0
        end_col = col_len

        col_track = 0

        while start_row < end_row and start_col < end_col:
            print(f"start_row: {start_row} end_row: {end_row}\n"
                  f"start_col: {start_col} end_col: {end_col}")
            # Traverse straight col
            for col in range(start_col, end_col):
                return_array.append(matrix[start_row][col])
            print(f"After Straight col-return_array: {return_array}")
            start_row += 1

            print(f"start_row: {start_row} end_row: {end_row}\n"
                  f"start_col: {start_col} end_col: {end_col}")
            # Traverse down row
            for row in range(start_row, end_row):
                return_array.append(matrix[row][end_col-1])
            print(f"After Down row-return_array: {return_array}")
            end_col -= 1

            print(f"start_row: {start_row} end_row: {end_row}\n"
                  f"start_col: {start_col} end_col: {end_col}")
            # Traverse back col
            if start_row < end_row:
                for col in range(end_col-1, start_col-1, -1):
                    return_array.append(matrix[end_row-1][col])
                print(f"After Back col-return_array: {return_array}")
                end_row -= 1

            print(f"start_row: {start_row} end_row: {end_row}\n"
                  f"start_col: {start_col} end_col: {end_col}")
            # Traverse up row
            if start_col < end_col:
                for row in range(end_row-1, start_row-1, -1):
                    return_array.append(matrix[row][start_col])
                print(f"After Up row-return_array: {return_array}")
                start_col += 1


        # while start_row >= 0 and start_row < row_len:
        #     print(f"start_row: {start_row} end_row: {end_row}\n"
        #           f"start_col: {start_col} end_col: {end_col}\n"
        #           f"col_track: {col_track}")
        #
        #     temp = start_col
        #     while start_col >= 0 and start_col < col_len:
        #         return_array.append(matrix[start_row][start_col])
        #         if col_track % 2 == 0:
        #             start_col += 1
        #         elif col_track % 2 != 0:
        #             start_col -= 1
        #
        #     if start_col >= col_len:
        #         start_col -= 1
        #     elif start_col < 0:
        #         start_col + 1
        #
        #     print(f"After col traverse:\n"
        #           f"start_row: {start_row} end_row: {end_row}\n"
        #           f"start_col: {start_col} end_col: {end_col}\n"
        #           f"col_track: {col_track}")
        #     while start_row < end_row and start_row >= 0:
        #         if col_track % 2 == 0:
        #             start_row += 1
        #         else:
        #             start_row -= 1
        #
        #         return_array.append(matrix[start_row][start_col])
        #
        #     print(f"After row traverse:\n"
        #           f"start_row: {start_row} end_row: {end_row}\n"
        #           f"start_col: {start_col} end_col: {end_col}\n"
        #           f"col_track: {col_track}")
        #     print(f"return_array: {return_array}")
        #     col_track += 1
        #     # change col
        #     if col_track % 2 == 0:
        #         start_col += 1
        #     else:
        #         start_col -= 1

            # start_col = end_col
            # print(f"col_track: {col_track}\ttemp:{temp}")
            # if col_track == 1:
            #     end_col = temp
            # elif col_track % 2 == 0:
            #     end_col = temp - 1
            # else:
            #     end_col = temp + 1
            #
            # start_row, end_row = end_row, start_row + 1

        return return_array


if __name__ == '__main__':
    matr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution = Solution()
    result = solution.spiralOrder(matr)
    print(f"result: {result}\n")