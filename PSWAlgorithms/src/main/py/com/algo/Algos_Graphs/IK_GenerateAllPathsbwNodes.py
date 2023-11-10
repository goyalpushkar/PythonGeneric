'''
Given a directed acyclic graph with n nodes, find all the possible paths starting from the node with the
 value 1 and ending at the node with the value n.

Example
{
"n": 4,
"edges": [
[1, 2],
[1, 3],
[2, 3],
[2, 4],
[3, 4]
]
}
Graph

Output:

[
[1, 2, 3, 4],
[1, 2, 4],
[1, 3, 4]
]
Notes
Return all the possible paths in any order.
For a graph with n nodes, the value of all the nodes are distinct and lie in the range [1, n].
Edges are given as a list of pairs: a list of lists where each inner list has exactly two elements. 
Each pair [X, Y] represents a directed edge from X to Y.
The list won't contain duplicate edges. That is, no more than one instance of any pair [X, Y] will be
present in the input list.
Constraints:

1 <= n <= 15
1 <= node value <= n
There will be no cycle or self-loop in the graph.
0 <= number of edges <= (n * (n - 1)) / 2
1 <= any number in the input list of edges <= n
'''

def get_all_paths(n, edges):
    """
    Args:
    n(int32)
    edges(list_list_int32)
    Returns:
    list_list_int32
    """
    # Write your code here.
    
    # adj_list =defaultdict(list)
    adj_list = {i+1:[] for i in range(n)}
    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        
    final_paths = []
    
    def dfs(path, node):
        if node == n:
            # final_paths.append(",".join(str(elem) for elem in path))
            final_paths.append(path.copy())
            # return
    
        for neighbor in adj_list[node]:
            path.append(neighbor)
            dfs(path, neighbor)
            path.pop()
        
        return 
    
    dfs([1], 1)
    return final_paths