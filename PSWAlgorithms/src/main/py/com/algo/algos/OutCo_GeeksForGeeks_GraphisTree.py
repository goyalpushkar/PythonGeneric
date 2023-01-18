'''
Given an undirected graph in an adjacency list format (a map of every vertex to a list of all its neighboring vertices), determine whether or not said graph is a tree.

Input: Undirected Graph as an Adjacency List (Map<int, int[]>)
Output: Boolean
Example
Input:
 {
   0 : [1, 2, 3],
   1 : [0],
   2 : [0],
   3 : [0, 4],
   4 : [3]
 }
Graph Is Tree
Output: True

Input:
 {
   0 : [1, 2, 3],
   1 : [0, 2],
   2 : [0, 1],
   3 : [0, 4],
   4 : [3]
 }
Graph Is Tree
Output: False // Cycle between 0, 1, 2

Input:
 {
   0 : [1, 2, 3],
   1 : [0],
   2 : [0],
   3 : [0],
   4 : []
 }
Graph Is Tree
Output: False // Island node

Constraints
Time Complexity: O(V + E)
Auxiliary Space Complexity: O(V + E)
The graph Vertex has the following properties:

value : an integer

edges : a list which contains references to other vertices in the Graph

You may assume the values of the vertices will all be unique.
'''

from typing import List

class Solution:
#Function to detect cycle in an undirected graph.
    def isCycle(self, V, adj):
        # Code here
        print(V)

        def is_Cycle_helper(start, adj, visited_multi):

            if start not in visited_nodes:
                visited_nodes.append(list(adj.keys())[0])

            if visited_multi >= 1:
                return False

            for neighbor in adj[start]:
                if neighbor in visited_nodes:
                    visited_multi += 1

                # visited_nodes[neighbor] = True
                visited_nodes.append(neighbor)

                is_Cycle_helper(neighbor, adj, visited_multi)

            return True

        visited_nodes = []
        visited_multi = 0
        # visited_nodes = {}
        # for key in adj.keys:
        #     visited_nodes[key] = False

        return_val = is_Cycle_helper(list(adj.keys())[0], adj, visited_multi)

        return return_val

#{
 # Driver Code Starts
if __name__ == '__main__':

    T = int(input("Enter Number of Test cases: ").strip())
    file = open("C:/Users/pgoyal/PyCharmWorkspace/GenericProcessing/algos/ShortestRouteEdges.txt")

    for _ in range(T):
        V, E = map(int, input("Enter number of nodes and edges as space separated values: ").split())
        adj = [[] for i in range(V)]
        for line in file:
            u, v = map(int, line.split())
            adj[u].append(v)
            adj[v].append(u)

        obj = Solution()
        ans = obj.isCycle(V, adj)
        if(ans):
            print("1")
        else:
            print("0")
# } Driver Code Ends