'''
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean.
The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right
and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where
heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south,
east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow
from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from
cell (ri, ci) to both the Pacific and Atlantic oceans.



Example 1:
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

Example 2:
Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.


Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105
'''
import math
class Solution:
    # efficient way
    # check from pacific ocean sides which all boxes pacific ocean water can reach to
    # check from atlantic ocean sides which all boxes atlantic ocean water can reach to
    # Beats 69.79% 279ms
    def pacificAtlantic(self, heights):
        self.r_s = len(heights)
        self.c_s = len(heights[0])

        pacific, atlantic = set(), set()

        def dfs(r, c, visited, prev_val):
            if (r, c) in visited or r < 0 or c < 0 or r > self.r_s - 1 or c > self.c_s - 1 or heights[r][c]<prev_val:
                return

            visited.add((r, c))
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
            dfs(r+1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])


        for col in range(self.c_s):
            dfs(0, col, pacific, heights[0][col])
            dfs(self.r_s-1, col, atlantic, heights[self.r_s-1][col])

        for row in range(self.r_s):
            dfs(row, 0, pacific, heights[row][0])
            dfs(row, self.c_s-1, atlantic, heights[row][self.c_s-1])

        return_arr = []
        for val in pacific:
            if val in atlantic:
                return_arr.append(val)

        return return_arr

    # Beats 5.1% 6775 ms
    def pacificAtlantic_1stAttempt(self, heights):
        self.r_s = len(heights)
        self.c_s = len(heights[0])

        def dfs(r, c, val, curr_val):

            key = (r, c)
            # print(f"call: {key}")

            if key in memo: return memo[key]

            # base case
            if r == 0 or c == 0:
                val[0] = 1

            if r == self.r_s - 1 or c == self.c_s - 1:
                val[1] = 1

            if (r == 0 and c == self.c_s - 1) or (c == 0 and r == self.r_s - 1):
                val[0] = 1
                val[1] = 1
                memo[key] = val
                return val

            heights[r][c] = math.inf
            # north
            n_v = [0, 0]
            if r - 1 >= 0 and curr_val >= heights[r - 1][c]:
                n_v = dfs(r - 1, c, [0, 0], heights[r - 1][c])

            # west
            w_v = [0, 0]
            if c - 1 >= 0 and curr_val >= heights[r][c - 1]:
                w_v = dfs(r, c - 1, [0, 0], heights[r][c - 1])

            # south
            s_v = [0, 0]
            if r + 1 < self.r_s and curr_val >= heights[r + 1][c]:
                s_v = dfs(r + 1, c, [0, 0], heights[r + 1][c])

            # east
            e_v = [0, 0]
            if c + 1 < self.c_s and curr_val >= heights[r][c + 1]:
                e_v = dfs(r, c + 1, [0, 0], heights[r][c + 1])

            if n_v[0] == 1 or w_v[0] == 1 or s_v[0] == 1 or e_v[0] == 1:
                val[0] = 1

            if n_v[1] == 1 or w_v[1] == 1 or s_v[1] == 1 or e_v[1] == 1:
                val[1] = 1

            # print(f"key: {key} val: {val}")
            heights[r][c] = curr_val
            memo[key] = val
            return val

        return_arr = []
        for row in range(self.r_s):
            for col in range(self.c_s):
                memo = {}
                fin = dfs(row, col, [0, 0], heights[row][col])
                if fin[0] == 1 and fin[1] == 1:
                    return_arr.append([row, col])

                # print(f"row: {row} col: {col} memo: {memo}")
                # print(heights[row], "\n")

        return return_arr

