'''
Given a two-dimensional matrix of 0s and 1s, find the number of islands.

An island is a group of connected 1s or a standalone 1. A cell in the matrix can be connected to
up to 8 neighbors: 2 vertical, 2 horizontal and 4 diagonal.

Example
{
"matrix": [
[1, 1, 0, 0, 0],
[0, 1, 0, 0, 1],
[1, 0, 0, 1, 1],
[0, 0, 0, 0, 0],
[1, 0, 1, 0, 1]
]
}
Output:

5
Notes
Use as little extra memory as possible.
Solve the problem without allocating a visited matrix.
Constraints:

1 <= number of rows <= 450
1 <= number of columns <= 450
'''
from collections import deque


def count_islands(matrix):
    """
    Args:
     matrix(list_list_int32)
    Returns:
     int32
    """
    # Write your code here.

    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    def bfs(r, c):
        nonlocal node_queue

        matrix[r][c] = -1
        node_queue.append([r, c])

        while node_queue:
            curr_node = node_queue.popleft()
            for nei in neighbors:
                cur_row = curr_node[0] + nei[0]
                cur_col = curr_node[1] + nei[1]

                if cur_row >= 0 and cur_col >= 0 \
                        and cur_row < len(matrix) and cur_col < len(matrix[0]) \
                        and matrix[cur_row][cur_col] not in (0, -1):
                    matrix[cur_row][cur_col] = -1
                    node_queue.append([cur_row, cur_col])

    island_count = 0
    node_queue = deque()
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] not in (0, -1):
                island_count += 1
                bfs(row, col)

    return island_count