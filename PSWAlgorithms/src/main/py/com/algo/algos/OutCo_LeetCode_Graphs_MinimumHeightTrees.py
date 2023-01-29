'''
Given an undirected graph with N vertices and is a tree-like (meaning there are no cycles,
no disconnected vertices or disjoined sets).

If a vertex in the given graph is selected as a root node of a tree, there is an associated height.
 (The height of a tree is defined as the largest number of nodes in the path from the root to a leaf)

Find the values of vertices, where the associated tree’s height would be a minimum height.
If there are ties for minimum, height, return all the values.

There are N vertices, and vertices have values ranging from 0 to N-1
Input:   Integer N denoting number of vertices
	     Array of Two-Item Integers representing edges
Output: Array of Integers representing vertices with minimum height

Example
Input: N = 4, edges = [[0, 3], [1, 3], [2,3]]
Output: [3] (because vertex 3 at the root has a minimum height of 2)

        0
    3
1       2
Height = 3

        1
    3
2       0
Height = 3

        2
    3
0       1
Height = 3

        3
    0   1   2
Height = 3


Input: N = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
Output: [3, 4]

        5
        4
        3
    0   1   2
Height = 4

        3
    0   1   2   4
                    5
Height = 3

            4
        3           5
    0   1   2
Height = 3

        0
        3
    1   2   4
            5
Height = 4

Constraints
Time Complexity: O(V+E)
Auxiliary Space Complexity: O(V+E)

V is the number of vertices
E is the number of edges

'''
import math

class Solution:
    # [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
    # create adjacency matrix  {'0': [3], '1': [3], '2': [3], '3': [0,1,2,4], '4': [3, 5], '5': [4]}
    # create a list for degrees of each node [1, 1, 1, 4, 2, 1]
    # in loop until adjacency is empty
        # get all leave node [0, 1, 2, 5] (1), [3, 4] (2)
        # reduce degree for all neighbors [0, 0, 0, 1, 1, 0]  {'3': [4], '4': [3]} (1), [0, 0, 0, 0, 0, 0] {} (2)
    # return leave nodes

    # Time Limit exceeded 70/71 passed - if I take while loop with len(adjacency_list) > 0
    # Passed all if new_leaves are updated in the current loop itself and using n > 2 as while
    def findMinHeightTrees(self, n, edges):
        # Create an adjacency list for each node
        adjacency_list = {}
        print(f"edges: {edges}")

        if n == 1:
            return [0]

        for edge in edges:
            if edge[0] in adjacency_list:
                new_value = adjacency_list[edge[0]]
                new_value.append(edge[1])
                adjacency_list[edge[0]] = new_value
            else:
                adjacency_list[edge[0]] = [edge[1]]

            if edge[1] in adjacency_list:
                new_value = adjacency_list[edge[1]]
                new_value.append(edge[0])
                adjacency_list[edge[1]] = new_value
            else:
                adjacency_list[edge[1]] = [edge[0]]
        print(f"adjacency_list: {adjacency_list}")

        degree = [0 for _ in range(n)]
        for key in adjacency_list.keys():
            degree[key] = len(adjacency_list[key])
        print(f"degree: {degree}")

        leaves = []
        # Get all leave nodes
        for index in range(n):
            if degree[index] == 1 or (degree[index] == 0 and index in adjacency_list.keys()):
                leaves.append(index)
        print(f"leaves: {leaves}")

        # index = 1
        while n > 2:  # and index < 4  len(adjacency_list) > 0
            # leaves = []
            # Get all leave nodes Moved out of loop
            n -= len(leaves)
            new_leaves = []

            # reduce degree of neighbors
            for leave in leaves:
                degree[leave] -= 1
                neighbors = adjacency_list[leave]
                for neighbor in neighbors:
                    # get neighbor
                    # neighbor = adjacency_list[leave][0]
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        new_leaves.append(neighbor)

                adjacency_list.pop(leave)

            print(f"adjacency_list: {adjacency_list}\n"
                  f"degree: {degree}")
            # index += 1
            leaves = new_leaves

        return leaves

    # Time Limit Exceeded
    def findMinHeightTrees_TE(self, n, edges):

        if n == 1:
            return [0]

        # Create an adjacency list for each node
        adjacency_list = {}
        print(f"edges: {edges}")
        for edge in edges:
            print(edge[0], edge[1])
            if edge[0] in adjacency_list:
                new_value = adjacency_list[edge[0]]
                new_value.append(edge[1])
                adjacency_list[edge[0]] = new_value
            else:
                adjacency_list[edge[0]] = [edge[1]]
            # adjacency_list.get(edge[0], []).append(edge[1])

            if edge[1] in adjacency_list:
                new_value = adjacency_list[edge[1]]
                new_value.append(edge[0])
                adjacency_list[edge[1]] = new_value
            else:
                adjacency_list[edge[1]] = [edge[0]]
            # adjacency_list[edge[1]] = adjacency_list[edge[1]].append(edge[0]) if edge[1] in adjacency_list else [edge[0]]
            # adjacency_list.get(edge[1], []).append(edge[0])
            print(f"adjacency_list: {adjacency_list}")


        def helper(node, curr_height):
            # print(f"node: {node} \t curr_height: {curr_height}\n"
            #       f"visited_node: {visited_node}")
            # if current node already visited return its height
            if node in visited_node:
                return visited_node[node]

            # if current node does not have any child return 1
            if len(adjacency_list[node]) == 0:
                visited_node[node] = curr_height
                return curr_height

            # mark node as visited
            visited_node[node] = curr_height

            # Loop for all its children and get max height out of them
            for child in adjacency_list[node]:
                # print(f"child: {child}")
                visited_node[node] = max(visited_node[node], helper(child, curr_height+1))

            return visited_node[node]

        min_height_nodes = []
        curr_min = math.inf
        # Check height from each node as a root and add it to dictionary
        for each_node in adjacency_list:
            visited_node = {}
            # print(f"Get value for {each_node}")
            result = helper(each_node, 1)
            if result <= curr_min:
                # if top most element height is greater than current then remove it
                if len(min_height_nodes) > 0 and min_height_nodes[0][1] > result:
                    min_height_nodes = []
                    min_height_nodes.append((each_node,result))
                else:
                    min_height_nodes.append((each_node, result))

            curr_min = min(curr_min, result)

        print(f"min_height_nodes: {min_height_nodes}")
        final_list = []
        for elem in min_height_nodes:
            final_list.append(elem[0])

        return final_list

if __name__ == '__main__':
    test_cases = int(input("Enter no of test cases: "))
    for i in range(test_cases):
        n = int(input("Enter no of nodes: "))
        edges = []
        for edge in range(n-1):
            edge = list(map(int, input("Enter vertices for edge: ").split()))
            edges.append([edge[0], edge[1]])

        sol = Solution()
        # result = sol.findMinHeightTrees_TE(n, edges)
        result = sol.findMinHeightTrees(n, edges)
        print(f"result: {result}")