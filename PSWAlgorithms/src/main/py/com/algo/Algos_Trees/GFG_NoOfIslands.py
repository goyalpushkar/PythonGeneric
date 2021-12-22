'''
Given a Matrix consisting of 0s and 1s. Find the number of islands of connected 1s present in the matrix.
Note: A 1 is said to be connected if it has another 1 around it (either of the 8 directions).

Input:
The first line of input will be the number of testcases T, then T test cases follow. The first line of each testcase contains two space separated integers N and M. Then in the next line are the NxM inputs of the matrix A separated by space .

Output:
For each testcase in a new line, print the number of islands present.

Your Task:
You don't need to read input or print anything. Your task is to complete the function findIslands() which takes the matrix A and its dimensions N and M as inputs and returns the number of islands of connected 1s present in the matrix. A 1 is said to be connected if it has another 1 around it (either of the 8 directions).

Expected Time Complexity: O(N*M).
Expected Auxiliary Space: O(N*M).

Constraints:
1 <= T <= 100
1 <= N, M <= 100
0 <= A[i][j] <= 1

Example(To be used only for expected output) :
Input
2
3 3
1 1 0 0 0 1 1 0 1
4 4
1 1 0 0 0 0 1 0 0 0 0 1 0 1 0 0

Output
2
2

Explanation:
Testcase 1: The graph will look like
1 1 0
0 0 1
1 0 1
Here, two islands will be formed
First island will be formed by elements {A[0][0] ,  A[0][1], A[1][2], A[2][2]}
Second island will be formed by {A[2][0]}.
Testcase 2: The graph will look like
1 1 0 0
0 0 1 0
0 0 0 1
0 1 0 0
Here, two islands will be formed
First island will be formed by elements {A[0][0] ,  A[0][1], A[1][2], A[2][3]}
Second island will be formed by {A[3][1]}.
'''

# User function Template for python3
'''
	Your task is to return the count of number
	of islands in the given boolean grid.

	Function Arguments: A (boolean grid), N -> no of rows, M -> no of columns. 
	Return Type: Integer denoting the number of islands

	Contributed By: Nagendra Jha
'''

import sys
sys.setrecursionlimit(100000)

def findIslands(A, N, M):
    # code here

    '''
    for row in range(N):
        for col in range(M):
            all_nodes[row][col] = -1
    '''
    findIslands.rows = N
    findIslands.columns = M

    all_nodes = [[False for col in range(M)] for row in range(N)]
    count = 0
    # print(all_nodes)
    for row in range(N):
        for col in range(M):
            if all_nodes[row][col] == False and A[row][col] == 1:
                dfs_util(A, all_nodes, row, col)
                count += 1

    return count


def safe(A, all_nodes, row, col):
    return (0 <= row < findIslands.rows
            and 0 <= col < findIslands.columns
            and A[row][col] == 1 and not all_nodes[row][col]
            )


def dfs_util(A, all_nodes, row, col):
    # print("Row - " + str(row) + " :Col - " + str(col))
    all_nodes[row][col] = True
    rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
    colNbr = [-1, 0, 1, -1, 1, -1, 0, 1]

    for i in range(8):
        if safe(A, all_nodes, row + rowNbr[i], col + colNbr[i]):
            dfs_util(A, all_nodes, row + rowNbr[i], col + colNbr[i])
    '''
    for adj_values in get_adjacent_nodes(A, row, col):
        #print(adj_values)
        if A[adj_values[0]][adj_values[1]] and not all_nodes[adj_values[0]][adj_values[1]]:
            dfs_util(A, all_nodes, adj_values[0], adj_values[1])
    '''


def get_adjacent_nodes(A, row, col):
    adj_nodes = []

    if row - 1 >= 0:
        if col - 1 >= 0:
            adj_nodes.append((row - 1, col - 1))  # (A[row - 1][col - 1])
        adj_nodes.append((row - 1, col))  # (A[row - 1][col])
        if col + 1 < findIslands.columns:
            adj_nodes.append((row - 1, col + 1))  # (A[row - 1][col + 1])

    if col - 1 >= 0:
        adj_nodes.append((row, col - 1))  # (A[row][col - 1])
    if col + 1 < findIslands.columns:
        adj_nodes.append((row, col + 1))  # (A[row][col + 1])

    if row + 1 < findIslands.rows:
        if col - 1 >= 0:
            adj_nodes.append((row + 1, col - 1))  # (A[row + 1][col - 1])
        adj_nodes.append((row + 1, col))  # (A[row + 1][col])
        if col + 1 < findIslands.columns:
            adj_nodes.append((row + 1, col + 1))  # (A[row + 1][col + 1])

    # print(adj_nodes)
    return adj_nodes

if __name__ == '__main__':
    t = int(input("No of test cases: "))
    for index in range(t):
        n, m = map(int, input("Rows and Columns: ").strip().split())
        cell_info = list(map(int, input("Values of Array: ").strip().split()))
        a = []
        k = 0
        for i in range(n):
            row_i = []
            for j in range(m):
                row_i.append(cell_info[k])
                k += 1

            a.append(row_i)

        print(findIslands(a, n, m))
