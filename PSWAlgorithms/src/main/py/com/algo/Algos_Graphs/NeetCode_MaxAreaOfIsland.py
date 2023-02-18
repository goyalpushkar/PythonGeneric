'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected
 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
               [0,0,0,0,0,0,0,1,1,1,0,0,0],
               [0,1,1,0,1,0,0,0,0,0,0,0,0],
               [0,1,0,0,1,1,0,0,1,0,1,0,0],
               [0,1,0,0,1,1,0,0,1,1,1,0,0],
               [0,0,0,0,0,0,0,0,0,0,1,0,0],
               [0,0,0,0,0,0,0,1,1,1,0,0,0],
               [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.

'''
class Solution(object):
    # beats 72.15% 139ms after commenting part_of_island  (61.51% 145 ms )
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]

        # def part_of_island(row, col):
        #     # top or left is 1 then it is part of island
        #     if (grid[row - 1][col] == 1 and visited[row][col] != 1) or (
        #             grid[row][col - 1] == 1 and visited[row][col] != 1) \
        #             or (grid[row][col] == 1):
        #         return 1
        #     else:
        #         return 0

        max_count = 0
        def check_neighbors(row, col):
            count = 0
            # if already visited
            # print(f"check_neighbors: {row} {col} count: {count}")
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or visited[row][col] == 1:
                return 0  # count

            # print(f"already visited: {visited[row][col]}")
            # if visited[row][col] == 1:
            #     return 0
            visited[row][col] = 1
            if grid[row][col] == 1:   # part_of_island(row, col):
                count += 1
                count += check_neighbors(row - 1, col) + check_neighbors(row + 1, col) + \
                         check_neighbors(row, col - 1) + check_neighbors(row, col + 1)

            return count

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                count = 0
                if visited[row][col] == 1 or grid[row][col] == 0:
                    continue
                count = check_neighbors(row, col)
                # print(f"count: {count}")
                max_count = max(max_count, count)
                print(f"row: {row} col: {col} max_count: {max_count}\n\n")

        return max_count