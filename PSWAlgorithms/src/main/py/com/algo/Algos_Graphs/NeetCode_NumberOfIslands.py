'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
 return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or
vertically. You may assume all four edges of the grid are all surrounded by water.


Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''
class Solution:
    def numIslands(self, grid):
        self.m = len(grid)
        self.n = len(grid[0])

        def dfs(r, c):
            # print(r, c)

            if r < 0 or r >= self.m or c < 0 or c >= self.n:
                return

                # if it is water
            if grid[r][c] == "0":
                return

            # down
            if r + 1 < self.m:
                if grid[r + 1][c] == "1":
                    grid[r + 1][c] = "V"
                    dfs(r + 1, c)

            # left
            if c + 1 < self.n:
                if grid[r][c + 1] == "1":
                    grid[r][c + 1] = "V"
                    dfs(r, c + 1)

            # up
            if r - 1 >= 0:
                if grid[r - 1][c] == "1":
                    grid[r - 1][c] = "V"
                    dfs(r - 1, c)

            # right
            if c - 1 >= 0:
                if grid[r][c - 1] == "1":
                    grid[r][c - 1] = "V"
                    dfs(r, c - 1)

            return

        total_count = 0
        for r in range(self.m):
            for c in range(self.n):
                if grid[r][c] == "1":
                    grid[r][c] = "V"
                    dfs(r, c)
                    total_count += 1
                    # print(r, c, total_count, "\n")

        return total_count
