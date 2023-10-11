'''
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.


Example 1:
Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false

Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.
Example 2:
Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.


Constraints:
graph.length == n
1 <= n <= 100
0 <= graph[u].length < n
0 <= graph[u][i] <= n - 1
graph[u] does not contain u.
All the values of graph[u] are unique.
If graph[u] contains v, then graph[v] contains u.
'''

# https://www.geeksforgeeks.org/bipartite-graph/
# DFS can also be used on this
class Solution:
    # Approach with putting alternate layer nodes in different set
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # edge_list = []
        # duplicate_check = set()
        # for index in range(len(graph)):
        #     for edges in graph[index]:
        #         key = "".join(str(elem) for elem in sorted([index, edges]))
        #         if key not in duplicate_check:
        #             edge_list.append(sorted([index, edges]))
        #             duplicate_check.add(key)

        # print(edge_list)

        # adj_list = [[] for i in range(num_of_people)]
        # for i in range(len(dislike1)):
        #     adj_list[dislike1[i]].append(dislike2[i])

        print(graph)

        def bfs(node):
            set_node[node] = -1
            que.append(node)

            while que:
                curr_node = que.popleft()
                print(curr_node, set_node, que)
                for nei in graph[curr_node]:
                    # check if neighbor is already visited and in the same set then return true
                    # else call bfs on neighbor with alternate set_num
                    if set_node[nei] == 0:
                        set_node[nei] = -1 * set_node[curr_node]
                        que.append(nei)
                    else:
                        if set_node[curr_node] == set_node[nei]:
                            return True

            return False

        que = deque()
        set_node = [0 for _ in range(len(graph))]
        for index in range(len(graph)):
            if set_node[index] == 0:
                if bfs(index):
                    return False

        return True

        # 79/81 passed
        # [[0, 3], [1, 2], [1, 4], [3, 4]] - failed
        # Problem using edge list or adjacency list we dont know what other edges will be there on the node and
        # which all vertices will be present so we may end up placing 2 vertices in corresponding to node 1 into another set
        # but there could be an edge between those 2 nodes
        # One approach is to do BFS and put nodes and its neighbors in alternate sets. Verify if node is visited then does it
        # exists in alternate set
        # Second approach is to check if there are cycles (using cross edges for BFS). If there is a cycle with odd number of
        # nodes then it will not be bipartite but if cycle is with even number of nodes then it will be bipartite
        # because if there are 5 nodes and 5 edges connect them all then it will not be bipartite but if there are 6 nodes and 6 edges
        # then they will be bipartite
        '''
                    R                           R
                G       G                  G        G
                
                R       R                  R        R
                                            
                                                G
            Not bipartite as 2 Red      Bipartite as no 2 nodes have same color
        '''
        # e.g.
        '''
                        s 
                n1      n2      n3
                |        |      |


                   w1   w2  w3 .... w6
            u1  u2  u3  u4........u5   - k level
            If cross edge is between u1 and u2 len of paths from s 
            s - u1 (k) - u2 (1) - s (k) = 2k + 1 - cannot be bipartited
            If cross edge is between u1 and w1 len of paths from s 
            s - u1 (k) - w1 (1) - s (k-1) = 2k - can be bipartited

        '''
        # set1 = set()
        # set2 = set()
        # def check_xistense_in_sets(edge1, edge2, set):
        #     if edge1 in set and edge2 in set:
        #         return True

        # def add_edge_in_set(edge1, edge2, set1, set2):
        #     if edge1 in set1:
        #         if edge2 not in set2:
        #             set2.add(edge2)
        #             return

        #     if edge1 in set2:
        #         if edge2 not in set1:
        #             set1.add(edge2)
        #             return

        #     if edge2 not in set1:
        #         set1.add(edge1)
        #         return

        #     if edge2 not in set2:
        #         set2.add(edge1)

        # for edge in edge_list:
        #     print(edge[0], edge[1], set1, set2)
        #     if check_xistense_in_sets(edge[0], edge[1], set1):
        #         return False
        #     if check_xistense_in_sets(edge[0], edge[1], set2):
        #         return False

        #     add_edge_in_set(edge[0], edge[1], set1, set2)
        #     print('first iteration ', set1, set2)
        #     add_edge_in_set(edge[1], edge[0], set1, set2)
        #     print('second iteration ', set1, set2)

        # return True