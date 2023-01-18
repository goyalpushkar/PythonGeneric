'''
Given an unweighted, undirected graph which represents a metro map as follows

vertices are stations
edges are the path between two stations
Given a start station and ending station, determine the minimum number of stops that must be made to get to the destination.

Input: A Graph (unweighted/undirected), a starting Vertex, and an ending Vertex
Output: Integer

Input: The graph represented below, Vertex A, Vertex F
Shortest Route
                A ---- B
             /  |      |
            /   |      |
           C    D      E
           |    |     /
           |    |    /
           F -- G --/

Output: 2 Stops (From A stop at C, and then stop at F)

Constraints
Time Complexity: O(V + E) where V is the number of Vertices and E is the number of Edges
Auxiliary Space Complexity: O(V)
A graph Vertex instance has the following properties:

value : a string
edges : a list which contains references to other vertices in the Graph
The graph has a list of all the vertices: Graph.vertices

The Vertex values are all unique

'''

import math
import os
import random
import re
import sys
from collections import deque, defaultdict
#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n - Num of nodes
#  2. INTEGER m - Num of edges
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s - Starting node
#

# efficient - Not sure if it is working, took from Discussions from other
# def bfs(n, m, edges, s):
#     graph = defaultdict(list)
#     for u, v in edges:
#         graph[u] += [v]
#         graph[v] += [u]
#
#     res = [-1] * (n + 1)
#     res[s] = 0
#     q = deque([(s, 0)])
#     cost = 6
#
#     while q:
#         node, total = q.popleft()
#         total += cost
#         for i in graph[node]:
#             if res[i] == -1:
#                 q.append((i, total))
#                 res[i] = total
#
#     return res[1:s] + res[s + 1:]


# 7/8 passed 1/8 - Timeout
# Taking distance_node as an array, preparing edge list at node level reduces the run time and passed all test cases 8/8
def bfs(n, m, edges, s):
    # Write your code here
    # for node in range(s, n+1):
    #     node = int(node)
    #     distance_node[node] = math.inf
    #     visited_node[node] = False
    #
    # for node in range(1, s):
    #     node = int(node)
    #     distance_node[node] = math.inf
    #     visited_node[node] = False

    distance_node = [math.inf for i in range(n)]
    # distance_node = {}
    # visited_node = {}
    # for node in range(1, n + 1):
    #     node = int(node)
    #     distance_node[node] = math.inf
    #     visited_node[node] = False

    traverse_queue = deque()
    traverse_queue.append(s)
    # visited_node[s] = True
    distance_node[s-1] = 0
    node_path = {}
    node_path[s] = []

    # Instead of going through edges in each step of while loop, keep a list of neighbors at node level
    neighbor_list = defaultdict(list)
    for edge in edges:
        edge0 = int(edge[0])
        edge1 = int(edge[1])
        neighbor_list[edge0] = neighbor_list.get(edge0, []) + [edge1]
        neighbor_list[edge1] = neighbor_list.get(edge1, []) + [edge0]

    # print(neighbor_list)

    while len(traverse_queue) > 0:
        curr_node = traverse_queue.popleft()
        # print(f"curr_node: {curr_node}")
        # for edge in edges:
        for neighbor_node in neighbor_list[curr_node]:
            # neighbor_node = None
            # if int(edge[0]) == curr_node:
            #     neighbor_node = int(edge[1])
            # elif int(edge[1]) == curr_node:
            #     neighbor_node = int(edge[0])
            # print(f"curr_node: {curr_node}, neighbor_node: {neighbor_node}")
            # if neighbor_node:
            # print(f"curr_node: {curr_node}, neighbor_node: {neighbor_node}\n"
            #       f"distance_node: {distance_node}")
                # if not visited_node[neighbor_node]:
            if distance_node[neighbor_node-1] == math.inf:
                # print("append")
                traverse_queue.append(neighbor_node)
                node_path[neighbor_node] = node_path[curr_node] + [curr_node]
                # visited_node[neighbor_node] = True
                distance_node[neighbor_node-1] = min(distance_node[neighbor_node-1], 6+distance_node[curr_node-1])

    # return_array = []
    for node in range(1, n + 1):
        node = int(node)
        if distance_node[node-1] == math.inf:
            distance_node[node-1] = -1
    #     return_array.append(distance_node[node])

    print(f"distance_node: {distance_node}")
    print(f"node_path: {node_path}")
    # print(return_array)
    # return return_array[0:s - 1] + return_array[s:]
    return distance_node[0:s-1] + distance_node[s:]

    # for node in range(1, s):
    #     node = int(node)
    #     if distance_node[node] == math.inf:
    #         distance_node[node] = -1
    #
    #     return_array.append(distance_node[node])
    #
    # for node in range(s+1, n+1):
    #     node = int(node)
    #     if distance_node[node] == math.inf:
    #         distance_node[node] = -1
    #
    #     return_array.append(distance_node[node])


# 4/8 passed - 3/8 - Time limit exceeded, 1/8 - Wrong Answer
def bfs_rec(n, m, edges, s):
    # Write your code here
    def distance_helper(node, s):
        print(f" Current node {node} value: {distance_node[node]}, s: {s}")
        if node == s:
            print(f"Return 0")
            return 0

        for edge in edges:
            neighbor_node = None
            if int(edge[0]) == node:
                neighbor_node = int(edge[1])
            elif int(edge[1]) == node:
                neighbor_node = int(edge[0])

            if neighbor_node:
                print(f"Neighbor node: {neighbor_node}")
                if visited_node[neighbor_node] == False:
                    visited_node[neighbor_node] = True
                    distance_node[node] = min(distance_node[node], 6+distance_helper(neighbor_node, s))

        print(f"Final return distance_node[node]: {distance_node[node]}")
        return distance_node[node]

    distance_node = {}
    visited_node = {}

    def initialize():
        for node in range(s, n+1):
            node = int(node)
            distance_node[node] = math.inf
            visited_node[node] = False

        for node in range(1, s):
            node = int(node)
            distance_node[node] = math.inf
            visited_node[node] = False

    return_array = {}
    return_val = []
    for node in range(1, s):
        initialize()
        node = int(node)
        # distance_node[node] = 0
        visited_node[node] = True
        print(distance_node)
        # print("\n\n")
        distance = distance_helper(node, s)
        if distance == math.inf:
            distance = -1
        print(f"distance: {distance}\n\n")
        return_array[node] = distance
        return_val.append(distance)

    for node in range(s+1, n+1):
        initialize()
        node = int(node)
        # distance_node[node] = 0
        visited_node[node] = True
        print(distance_node)
        # print("\n\n")
        distance = distance_helper(node, s)
        if distance == math.inf:
            distance = -1
        print(f"distance: {distance}\n\n")
        return_array[node] = distance
        return_val.append(distance)

    print(return_val)
    return return_val


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input("Enter Number of Test cases: ").strip())
    file = open("C:/Users/pgoyal/PyCharmWorkspace/GenericProcessing/algos/ShortestRouteEdges.txt")
    for q_itr in range(q):
        # 70 1988
        first_multiple_input = input("Enter number of nodes and edges as space separated values: ").rstrip().split()

        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])

        edges = []
        for _ in range(m):
            for line in file:
                edges.append(line.split())
            # edges.append(list(map(int, input("Enter nodes as space separated values for edge: ").rstrip().split())))

        # 16
        s = int(input("Enter starting node: ").strip())

        print(f"edges: {edges}")
        result = bfs(n, m, edges, s)
        print(' '.join(map(str, result)))
        print("\n")
        # fptr.write(' '.join(map(str, result)))
        # fptr.write('\n')

    # fptr.close()

