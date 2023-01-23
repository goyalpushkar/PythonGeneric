'''
Given a maze, represented by a matrix of bits (values 0 and 1), a rat must find a path from index [0][0] to [n-1][m-1]. The rat can only travel to the right or down, and can only travel on 0 values. 1 values represent walls.
Input:   maze (Matrix of elements with values either 0 or 1)
Output:  Array of two-item arrays indicating the path.
Example
Input:   [[0, 0, 0, 1],
          [0, 1, 0, 1],
          [0, 1, 0, 0],
          [0, 0, 1, 0]]
Output:  [[0, 0],
          [0, 1],
          [0, 2],
          [1, 2],
          [2, 2],
          [2, 3],
          [3, 3]]
Constraints
For M x N matrix.
Time Complexity: 0(MN)
Auxiliary Space Complexity: O(MN)
If not path found, return the following path: [[-1, -1]]
Remember, the rat can only move RIGHT or DOWN
'''

'''
      0    1    2    3 
0   ['0', '0', '0', '1'] 
1   ['0', '1', '0', '1']
2   ['0', '1', '0', '0']
3   ['0', '0', '1', '0']
                                          0,0
                                     /               \
                             1,0                         0,1
                      /              \             /            \
                   2,0               1,1        1,1             0,2
               /         \            X          X           /       \
            3,0             2,1                            1,2      0,3
            /  \             X                            /   \       X
           X    3,1                                    2,2    1,3
        (row>      \                                  /   \     X
        len(row)    3,2                             3,2   2,3             
        )            X                               X    / \     
                    (==1)                                3,3 X
                                                        Good (col>
                                                             len(col))
'''


class Solution:

    def rat_path(self, matrix):

        def helper(row, col, curr_path):

            curr_path.append([row, col])

            # Base case outside of range
            if row >= len(matrix) or col >= len(matrix[0]):
                return curr_path[:-1]

            # Base case Wall found
            if matrix[row][col] == '1':
                return curr_path[:-1]

            # Base case found
            if row == len(matrix) - 1 and col == len(matrix[0]) - 1:
                final_path.append(curr_path)
                return curr_path[:-1]

            # right
            right = helper(row, col + 1, curr_path)

            # down
            down = helper(row + 1, col, right)

            return down[:-1]

        final_path = []
        last_call = helper(0, 0, [])

        print(f"final_path: {final_path}\n"
              f"last_call: {last_call}")

        return final_path[0]

    '''
    Rat can move in all direction. Return all paths in lexographic order

    '''

    def findPath_alldirec(self, m, n):
        # code here
        def helper(row, col, curr_path):
            # print(f"row: {row}\tcol: {col}\tcurr_path:{curr_path}\n"
            #       f"final_path: {final_path}")

            # Base case outside of range
            if row < 0 or row >= len(m) or col < 0 or col >= len(m[0]):
                return curr_path[:-1]

            # # Base case already visited
            if final_path[row][col] == 1:
                return curr_path[:-1]

            final_path[row][col] = 1

            # Base case Wall found
            if m[row][col] == '1':
                return curr_path[:-1]

            # Base case found
            if row == len(m) - 1 and col == len(m[0]) - 1:
                all_paths.append("".join(elem for elem in curr_path))
                # print(f"final_path: {final_path}\n"
                #       f"all_paths: {all_paths}\n\n")
                final_path[row][col] = 0
                return curr_path[:-1]

            # Only proceed on the path if not already visited
            # right
            # if final_path[row][col+1] == 0:
            curr_path.append("R")
            right = helper(row, col + 1, curr_path)

            # down
            # if final_path[row+1][col] == 0:
            right.append("D")
            down = helper(row + 1, col, right)

            # left
            # if final_path[row][col-1] == 0:
            down.append("L")
            left = helper(row, col - 1, down)

            # up
            # if final_path[row-1][col] == 0:
            left.append("U")
            up = helper(row - 1, col, left)

            final_path[row][col] = 0

            return up[:-1]

        # Track the path and visited nodes to avoid stuck in recursive loop
        # n - columns and len(m) - rows
        final_path = [[0 for i in range(n)] for _ in range(len(m))]
        all_paths = []
        last_call = helper(0, 0, [])

        # print(f"final_path: {final_path}\n"
        #       f"last_call: {last_call}")

        return sorted(all_paths)


if __name__ == '__main__':
    mat = [['0', '1', '1', '1'],
           ['0', '0', '1', '0'],
           ['0', '0', '1', '1'],
           ['1', '0', '0', '0']]
    '''
        [['0', '0', '0', '1'],
           ['0', '1', '0', '1'],
           ['0', '1', '0', '0'],
           ['0', '0', '1', '0']]
           
        [[0,0], [0,1]]
    '''
    solution = Solution()
    result = solution.rat_path(mat)
    print(f"result: {result}\n")
    result_all = solution.findPath_alldirec(mat, len(mat[0]))

    print(f"result_all: {result_all}")