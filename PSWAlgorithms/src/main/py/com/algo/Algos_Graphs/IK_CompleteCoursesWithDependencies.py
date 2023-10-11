'''
A university has n courses to offer. To graduate from that university, a student must complete all those courses. Some courses have prerequisite courses. One can take a course only after completing all of its prerequisites. Dependencies between the courses are described by two arrays a and b of the same size: course a[i] must be taken before course b[i] for all valid indices. Is it possible to complete all the courses without violating constraints?

Example One
{
"n": 4,
"a": [1, 1, 3],
"b": [0, 2, 1]
}
Output:
1
One possible ordering is 3, 1, 0, 2.

Example Two
{
"n": 4,
"a": [1, 1, 3, 0],
"b": [0, 2, 1, 3]
}
Output:
0
Every possible ordering of the courses violates at least one of the constraints.

Notes
The courses are labeled from 0 to n - 1.

Constraints:
2 <= n <= 100000
1 <= size of a = size of b <= 100000
0 <= a[i], b[i] < n holds for any valid index i
a[i] != b[i] holds for any valid index i
No duplicate dependencies are present.
'''
from collections import deque

def can_be_completed(n, a, b):
    """
    Args:
     n(int32)
     a(list_int32)
     b(list_int32)
    Returns:
     bool
    """
    # Write your code here.
    # if there is a cycle then it cannot be completed

    adj_list = [[] for _ in range(n)]
    for i in range(len(a)):
        adj_list[a[i]].append(b[i])
        # print(adj_list)

    print(adj_list)

    def dfs(node, curr_path):
        # print(curr_path)
        visited[node] = 1
        curr_path.append(node)

        for nei in adj_list[node]:
            if visited[nei] == -1:
                # visited[nei] = 1
                # curr_path.append(nei)
                if dfs(nei, curr_path):
                    return True

            else:
                if nei in curr_path:
                    return True

        curr_path.pop()

        return False

    que = deque()
    # parent = [-1 for _ in range(n)]
    visited = [-1 for _ in range(n)]
    for index in range(n):
        if visited[index] == -1:
            # print("before dfs: ", visited)
            if dfs(index, []):
                # print("after dfs: ", visited)
                return False

    return True
