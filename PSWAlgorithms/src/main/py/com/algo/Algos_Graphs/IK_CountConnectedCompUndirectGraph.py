'''
Given an undirected graph, find its total number of connected components.

Example One
Graph
{
"n": 5,
"edges": [[0 ,1], [1, 2], [0, 2], [3, 4]]
}
Output:
2

Example Two
Graph

{
"n": 4,
"edges": [[0 , 1], [0 , 3], [0 , 2], [2 , 1], [2 , 3]]
}
Output:
1

Notes

Constraints:
1 <= number of nodes <= 105
0 <= number of edges <= 105
0 <= node value < number of nodes
'''


def number_of_connected_components(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     int32
    """
    # Write your code here.
    adj_list = [[] for _ in range(n)]
    visited = [0 for _ in range(n)]
    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])

    def dfs(curr_node):

        visited[curr_node] = 1

        for nei in adj_list[curr_node]:
            if visited[nei] != 1:
                dfs(nei)

    connected_comp = 0
    for node in range(n):
        if visited[node] != 1:
            connected_comp += 1
            dfs(node)

    return connected_comp
