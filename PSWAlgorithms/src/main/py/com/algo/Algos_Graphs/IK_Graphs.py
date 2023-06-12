'''
Check if Eulerian Cycle Exists
Check if there exists any eulerian cycle in a given undirected connected graph.
The Euler cycle is a path in the graph that visits every edge exactly once and
 starts and finishes at the same vertex.
'''
def check_if_eulerian_cycle_exists(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     bool
    """
    # Write your code here.
    edge_map = {}
    for edge in edges:
        if edge[0] in edge_map:
            edge_map[edge[0]] += 1
        else:
            edge_map[edge[0]] = 1
        if edge[1] in edge_map:
            edge_map[edge[1]] += 1
        else:
            edge_map[edge[1]] = 1

        # edge_map.get(edge[0], 0) += 1
        # edge_map.get(edge[1], 0) += 1

    for key, val in edge_map.items():
        if val % 2 > 0:
            return False

    return True

'''
Check if Eulerian Path Exists
Given an undirected connected graph, check if there exists any eulerian path in it. 
The Eulerian Path is a path in the graph that visits every edge exactly once 
(allowing for revisiting vertices).
'''


def check_if_eulerian_path_exists(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     bool
    """
    # Write your code here.
    if len(edges) == 0:
        return True

    edge_map = {}
    for edge in edges:
        if edge[0] in edge_map:
            edge_map[edge[0]] += 1
        else:
            edge_map[edge[0]] = 1
        if edge[1] in edge_map:
            edge_map[edge[1]] += 1
        else:
            edge_map[edge[1]] = 1

    print(edge_map)
    num_of_odd_edge_nodes = 0
    for key, val in edge_map.items():
        if val % 2 > 0:
            num_of_odd_edge_nodes += 1

    return True if num_of_odd_edge_nodes in (0, 2) else False

'''
Convert the given edge list to the adjacency list of an undirected connected graph.
An adjacency list represents a graph as a list of lists. The list index represents a vertex, and each element 
in its inner list represents the other vertices that form an edge with the vertex.
'''
def convert_edge_list_to_adjacency_list(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    adj_list = [[] for _ in range(n)]
    # adj_list = {}
    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])

        # if edge[0] in adj_list:
        #     adj_list[edge[0]].add(edge[1])

        # if edge[1] in adj_list:
        #     adj_list[edge[1]].add(edge[0])

    for index in range(n):
        adj_list[index] = sorted(adj_list[index])

    return adj_list


'''
Convert the given edge list to the adjacency matrix of an undirected connected graph.
The adjacency matrix is a matrix with rows and columns labeled by graph vertices, with a 1 or 0 
in position (u, v) according to whether vertices u and v are adjacent or not.
'''
def convert_edge_list_to_adjacency_matrix(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     list_list_bool
    """
    # Write your code here.
    adj_matrix = [[False for _ in range(n)] for _ in range(n)]

    for edge in edges:
        row = edge[0]
        col = edge[1]
        adj_matrix[row][col] = True
        adj_matrix[col][row] = True

    return adj_matrix

'''
'''
from collections import deque


def bfs_traversal(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    # Convert edge list to adjacency list
    adj_list = {}
    for edge in edges:
        if edge[0] in adj_list:
            adj_list[edge[0]].append(edge[1])
        else:
            adj_list[edge[0]] = [edge[1]]

        if edge[1] in adj_list:
            adj_list[edge[1]].append(edge[0])
        else:
            adj_list[edge[1]] = [edge[0]]

    # print(adj_list)

    # BFS
    def bfs(start_node):
        # nonlocal captured
        nonlocal final_result
        nonlocal visited

        node_queue = deque()
        node_queue.append(start_node)

        # captured[start_node] = 1
        while node_queue:
            # print(node_queue)
            curr_elem = node_queue.popleft()
            visited[curr_elem] = 1
            final_result.append(curr_elem)

            # temp = []
            # temp.append(curr_elem)
            if curr_elem in adj_list:
                for elem in adj_list[curr_elem]:
                    if visited[elem] == 0:  # captured
                        node_queue.append(elem)
                        visited[elem] = 1

            # result.append(elem for elem in temp)

    visited = [0 for _ in range(n)]
    # captured = [0 for _ in range(n)]
    final_result = []
    for node in range(n):
        # print("node: ", node, visited)
        if visited[node] == 0:
            bfs(node)

    # print(final_result)
    return final_result


def dfs_traversal(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    final_result = []

    adj_list = [[] for _ in range(n)]
    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])

    def dfs(start_node):
        nonlocal final_result
        final_result.append(start_node)
        visited[start_node] = 1

        for conn_nodes in adj_list[start_node]:
            if visited[conn_nodes] == 0:
                dfs(conn_nodes)

        return

    visited = [0 for _ in range(n)]
    for node in range(n):
        if visited[node] == 0:
            dfs(node)

    return final_result


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
    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])

    # print(adj_list)
    def dfs(node):
        nonlocal visited
        visited[node] = 1

        for neighbor in adj_list[node]:
            if visited[neighbor] == -1:
                dfs(neighbor)

    visited = [-1 for _ in range(n)]
    connected_components = 0
    for node in range(n):
        if visited[node] == -1:
            connected_components += 1
            dfs(node)
            # print(node, visited)

    return connected_components

'''
Given an undirected graph, find out whether it is a tree.

The undirected edges are given by two arrays edge_start and edge_end of equal size. Edges of the given graph 
connect nodes edge_start[i] and edge_end[i] for all valid i.

1st property: The graph has to be connected
2nd property: The graph cannot have a cycle


The above two properties are necessary and sufficient for a graph to be a tree. We can make a few more 
observations which are derived from this definition.

Observation 1: The graph cannot have a multi-edge. Otherwise the graph will lack the 2nd property. If the given graph 
has a multi-edge(more than one edge between a pair of nodes) then we can conclude that the graph is not a tree as a 
multi-edge will create a cycle in the graph.
Observation 2: The graph cannot have self-loops. Otherwise the graph will lack the 2nd property. Self loops(An edge
 connecting a node with itself) also creates a cycle.
Observation 3: The graph must have node_count - 1 edges. Otherwise the graph will lack 1st and/or 2nd property. 
Although mentioned in the problem statement, it can be proven that a tree having n nodes must have exactly n - 1 edges.\
Observation 4: If the graph is connected and has node_count - 1 edges, then it cannot have a cycle. In this case, 
the graph has both of the properties. So the graph must be a tree. It can be proven that an undirected connected 
graph having n nodes and n - 1 edges must be a tree.\

'''


def is_it_a_tree(node_count, edge_start, edge_end):
    """
    Args:
     node_count(int32)
     edge_start(list_int32)
     edge_end(list_int32)
    Returns:
     bool
    """
    # Write your code here.
    adj_list = [[] for _ in range(node_count)]
    for index in range(len(edge_start)):
        adj_list[edge_start[index]].append(edge_end[index])
        adj_list[edge_end[index]].append(edge_start[index])

    # print(adj_list)
    def dfs(node):
        nonlocal visited
        visited[node] = 1

        for neighbor in adj_list[node]:
            if visited[neighbor] == -1:
                parent[neighbor] = node
                if dfs(neighbor):
                    return True
            else:
                # if neighbor is already visited and its parent is not current node
                # that means it is a back edge
                # Visited neighbor could have been parent of the node itself in case of DFS,
                # so we are making sure it is not the parent of node
                if parent[node] != neighbor:
                    return True

        return False

    visited = [-1 for _ in range(node_count)]
    parent = [-1 for _ in range(node_count)]
    connected_components = 0
    for node in range(node_count):
        if visited[node] == -1:
            connected_components += 1

            # print(connected_components, visited, parent)
            # If there are more than 1 connected components means graph is disconnected and not a tree
            if connected_components > 1:
                return False

            # if any back edge for DFS or cross edge for BFS found then there is a cycle and it is not a Tree
            if dfs(node):
                return False
            # print(node, visited)

    return True


from collections import deque


def is_it_a_tree_bfs(node_count, edge_start, edge_end):
    """
    Args:
     node_count(int32)
     edge_start(list_int32)
     edge_end(list_int32)
    Returns:
     bool
    """
    # Write your code here.
    adj_list = [[] for _ in range(node_count)]
    for index in range(len(edge_start)):
        adj_list[edge_start[index]].append(edge_end[index])
        adj_list[edge_end[index]].append(edge_start[index])

    print(adj_list)

    def bfs(node):
        nonlocal visited
        nonlocal que

        que.append(node)
        visited[node] = 1

        while que:
            cur_node = que.popleft()
            # print(cur_node, que, parent)

            for neighbor in adj_list[cur_node]:
                if visited[neighbor] == -1:
                    parent[neighbor] = cur_node

                    visited[neighbor] = 1
                    que.append(neighbor)


                else:
                    # if neighbor is already visited and its parent is not current node
                    # that means it is a back edge
                    if parent[cur_node] != neighbor:
                        return True

        return False

    visited = [-1 for _ in range(node_count)]
    parent = [-1 for _ in range(node_count)]
    que = deque()
    connected_components = 0
    for node in range(node_count):
        if visited[node] == -1:
            connected_components += 1

            # print(connected_components, visited, parent)
            # If there are more than 1 connected components means graph is disconnected and not a tree
            if connected_components > 1:
                return False

            # print("before bfs")
            # if any back edge for DFS or cross edge for BFS found then there is a cycle and it is not a Tree
            if bfs(node):
                return False
            # print(node, visited)

    return True

'''
# Perform a breadth-first search (BFS) on the graph
def bfs(graph, start):
    queue = []
    visited = set()

    queue.append((start, 0))  # (cell, distance from start)
    visited.add(start)

    while queue:
        cell, distance = queue.pop(0)

        if cell == 100:
            return distance  # Found the shortest path to the last cell

        for neighbor in graph[cell]:
            if neighbor not in visited:
                queue.append((neighbor, distance + 1))
                visited.add(neighbor)

    return -1  # No path to the last cell found

# Call the BFS function to find the shortest path
shortest_path = bfs(graph, 1)
print("Shortest path to reach the last cell:", shortest_path)
'''