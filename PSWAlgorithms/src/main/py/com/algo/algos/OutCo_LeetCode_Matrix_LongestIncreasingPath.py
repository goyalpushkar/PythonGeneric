'''
Given an integer matrix, find the length of the longest increasing path.

Given each cell, you can either move to four directions, left, right, up or down. You may NOT move diagonally or
move outside of the boundary (i.e. wrap-around is not allowed).

Input: Matrix of Integers
Output: Integer (length of the longest increasing path)

Example
Example 1:
Input:

nums = [
[9, 9, 4],
[6, 6, 8],
[2, 1, 1]
]

Output: 4
1 -> 2 -> 6 -> 9

Example 2:
Input:
nums = [
[3, 4, 5],
[3, 2, 6],
[2, 2, 1]
]

Output: 4
3 -> 4 -> 5 -> 6


Constraints
Time Complexity: O(M * N)
Auxiliary Space Complexity: O(M*N)

https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

'''

class Solution:
    def longestIncreasingPath(self, matrix):
        max_rows = len(matrix)
        max_cols = len(matrix[0])
        directions = ((1,0),(-1,0),(0,1),(0,-1))

        def helper_cache(row, col):
            print(f"-----\n"
                  f"row:{row}\tcol:{col}\n"
                  f"already_visited:{already_visited}"
                  f"-----\n")

            nonlocal cache
            key = str(row)+'_'+str(col)

            if key in cache:
                return cache[key]

            cache[key] = 0
            for r in directions:
                next_row = row+r[0]
                next_col = col+r[1]

                if next_row >= 0 and next_row < max_rows and next_col >= 0 and next_col < max_cols:
                    if matrix[next_row][next_col] > matrix[row][col]:
                        cache[key] = max(cache[key], helper_cache(next_row, next_col))

            cache[key] += 1

            return cache[key]

        def dfs(row, col, prev):
            if row < 0 or row >= max_rows or col < 0 or col >= max_cols or matrix[row][col] <= prev:
                return 0

            if already_visited[row][col] > 0:
                return already_visited[row][col]

            curr_value = matrix[row][col]
            already_visited[row][col] = 1 + max(dfs(row-1, col, curr_value), dfs(row+1, col, curr_value),
                                                dfs(row, col-1, curr_value), dfs(row, col+1, curr_value))

            return already_visited[row][col]

        # 135 / 138 testcases passed
        def helper(row, col, curr_val, curr_path, max_path):
            print(f"-----\n"
                  f"row:{row}\tcol:{col}\tcurr_Val:{curr_val}\tcurr_path:{curr_path}\tmax_path:{max_path}\n"
                  f"already_visited:{already_visited}"
                  f"-----\n")
            if row < 0 or row >= max_rows or col < 0 or col >= max_cols:
                return max_path

            if already_visited[row][col] == 1:
                return max_path

            if matrix[row][col] <= curr_val:
                return max_path

            if matrix[row][col] > curr_val:
                curr_path += 1
                max_path = max(max_path, curr_path)
                # return max_path

            already_visited[row][col] = 1
            up = helper(row-1, col, matrix[row][col], curr_path, max_path) # up
            down = helper(row+1, col, matrix[row][col], curr_path, up) # down
            left = helper(row, col-1, matrix[row][col], curr_path, down) # left
            right = helper(row, col+1, matrix[row][col], curr_path, left) # right
            already_visited[row][col] = 0

            return max(up, down, left, right)

        already_visited = [[0 for _ in range(max_cols)] for _ in range(max_rows)]
        cache = {}
        max_return = -1
        for row in range(max_rows):
            for col in range(max_cols):
                print(f"****************\n"
                      f"row: {row}\tcol:{col}\n"
                      f"****************\n")
                max_value = helper(row, col, -1, 0, 0)
                # max_value = helper_cache(row, col)
                print(f"max_value: {max_value}\n"
                      )
                max_return = max(max_return, max_value)

        return max_return

if __name__ == '__main__':
    mat = [[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],
           [20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],
           [40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],
           [60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],
           [80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],
           [100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],
           [120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],
           [0,0,0,0,0,0,0,0,0,0]]

    # [[9,9,4],[6,6,8],[2,1,1]] - 4
    # [[3,4,5],[3,2,6],[2,2,1]] - 4
    '''


    '''
    solution = Solution()
    result = solution.longestIncreasingPath(mat)

    print(f"result: {result}")