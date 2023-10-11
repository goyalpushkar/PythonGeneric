'''
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens
 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
'''
import math
from collections import deque
class Solution:
    # beats 74.95% 51ms
    # bfs
    def orangesRotting(self, grid):
        self.r_s = len(grid)
        self.c_s = len(grid[0])
        fresh = 0
        minutes = 0

        rotten_queue = deque()
        for row in range(self.r_s):
            for col in range(self.c_s):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    rotten_queue.append((row, col))

        possible_directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        while rotten_queue and fresh > 0:

            for index in range(len(rotten_queue)):
                elem = rotten_queue.popleft()
                r, c = elem
                for direct in possible_directions:
                    new_r = r + direct[0]
                    new_c = c + direct[1]

                    if new_r < 0 or new_c < 0 or new_r >= self.r_s or new_c >= self.c_s or grid[new_r][new_c] != 1:
                        continue

                    grid[new_r][new_c] = 2
                    rotten_queue.append((new_r, new_c))
                    fresh -= 1

            minutes += 1

        return minutes if fresh == 0 else -1

    # 244/306 passed Timit limit exceeded
    def orangesRotting_TLE(self, grid):
        self.r_s = len(grid)
        self.c_s = len(grid[0])

        time_matrix = [[math.inf if grid[row][col] == 1 else 0 for col in range(self.c_s)] for row in range(self.r_s)]

        def dfs(r, c, minutes):
            # print(f"row: {r} col: {c} minutes: {minutes} memo: {memo}")
            key = (r, c)

            # if key in memo: return
            if r < 0 or c < 0 or r >= self.r_s or c >= self.c_s or grid[r][c] in (0, 3):
                return

            curr_val = grid[r][c]

            # how quickly fresh orange is rotten
            time_matrix[r][c] = min(time_matrix[r][c], minutes)

            # mark node as visisted
            grid[r][c] = 3

            # travel further
            up = dfs(r - 1, c, minutes + 1)
            left = dfs(r, c - 1, minutes + 1)
            down = dfs(r + 1, c, minutes + 1)
            right = dfs(r, c + 1, minutes + 1)

            # reset value after visiting all paths
            grid[r][c] = curr_val

            return

        for row in range(self.r_s):
            for col in range(self.c_s):
                if grid[row][col] == 2:
                    dfs(row, col, 0)
                # print(f"row: {row} col: {col} pend_fresh_set: {pend_fresh_set} ret_val: {ret_val} grid: {grid[row]} min_so_far: {min_so_far} \n")

        max_so_far = -1
        for row in range(self.r_s):
            for col in range(self.c_s):
                max_so_far = max(max_so_far, time_matrix[row][col])

        return -1 if max_so_far == math.inf else max_so_far

    # 124/ 306
    # failed [[2,1,1],[1,1,1],[0,1,2]] - output 4 exected 2
    # wrong approach as all rotten oranges will start making other oranges rotten at the same time instead of
    # calculating time from each rotten orange
    def orangesRotting_1st(self, grid):
        self.r_s = len(grid)
        self.c_s = len(grid[0])

        def get_fresh_set():
            fresh_set = set()
            for row in range(self.r_s):
                for col in range(self.c_s):
                    if grid[row][col] == 1:
                        fresh_set.add((row, col))

            return fresh_set

        def dfs(r, c, minutes):
            # print(f"row: {r} col: {c} minutes: {minutes} memo: {memo}")
            nonlocal pend_fresh_set
            key = (r, c)

            if key in memo: return memo[key]
            if r < 0 or c < 0 or r >= self.r_s or c >= self.c_s or grid[r][c] in (0, 3):
                return minutes - 1

            curr_val = grid[r][c]
            grid[r][c] = 3
            if (r, c) in pend_fresh_set:
                pend_fresh_set.remove((r, c))
            up = dfs(r - 1, c, minutes + 1)
            left = dfs(r, c - 1, minutes + 1)
            down = dfs(r + 1, c, minutes + 1)
            right = dfs(r, c + 1, minutes + 1)
            grid[r][c] = curr_val

            final_val = max(up, left, down, right)
            memo[key] = final_val

            return final_val

        pend_fresh_set = get_fresh_set()
        if not pend_fresh_set:
            return 0

        min_so_far = math.inf
        for row in range(self.r_s):
            for col in range(self.c_s):
                memo = {}
                pend_fresh_set = get_fresh_set()  # self.fresh_set.copy()
                # print(f"pend_fresh_set: {pend_fresh_set}")
                ret_val = 0
                if grid[row][col] == 2:
                    ret_val = dfs(row, col, 0)
                    if not pend_fresh_set:
                        min_so_far = min(min_so_far, ret_val)
                # print(f"row: {row} col: {col} pend_fresh_set: {pend_fresh_set} ret_val: {ret_val} grid: {grid[row]} min_so_far: {min_so_far} \n")

        return -1 if min_so_far == math.inf else min_so_far