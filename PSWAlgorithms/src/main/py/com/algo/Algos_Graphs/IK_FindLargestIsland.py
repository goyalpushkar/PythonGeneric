'''
Given a two-dimensional grid of 0s and 1s, find the size of the largest island. If there is no island return 0.

An island is a group of 1s connected vertically or horizontally.

Example One
{
"grid": [
[1, 1, 0],
[1, 1, 0],
[0, 0, 1]
]
}
Output:
4

There are two islands:

[(0, 0), (0, 1), (1, 0), (1, 1)]
[(2, 2)]
Size of the largest (first) island is 4.

Example Two
{
"grid": [
[0, 0, 0],
[0, 0, 0],
[0, 0, 0]
]
}
Output:
0

Notes

Constraints:
1 <= number of rows <= 200
1 <= number of columns <= 200
'''
from collections import deque


def max_island_size(grid):
    """
    Args:
     grid(list_list_int32)
    Returns:
     int32
    """
    # Write your code here.

    neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    #  [-1, -1], [1, 1], [-1, 1], [1, -1]
    que = deque()

    def bfs(row, col):
        nonlocal que

        curr_size = 0
        que.append([row, col])
        grid[row][col] = 0
        while que:
            # print(que, curr_size)
            popped_node = que.popleft()
            curr_size += 1

            for nei in neighbors:
                cur_row = popped_node[0] + nei[0]
                cur_col = popped_node[1] + nei[1]

                if cur_row >= 0 and cur_row < len(grid) \
                        and cur_col >= 0 and cur_col < len(grid[0]) \
                        and grid[cur_row][cur_col] != 0:
                    grid[cur_row][cur_col] = 0
                    que.append([cur_row, cur_col])

        return curr_size

    largest_island = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != 0:
                island_size = bfs(row, col)
                # print(island_size)
                largest_island = max(largest_island, island_size)

    return largest_island 