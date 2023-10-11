'''
Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
class Node {
    public int val;
    public List<Node> neighbors;
}


Test case format:
For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with
val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of
 neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference
to the cloned graph.


Example 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1
 and it does not have any neighbors.

Example 3:
Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.

Constraints:
The number of nodes in the graph is in the range [0, 100].
1 <= Node.val <= 100
Node.val is unique for each node.
There are no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.

'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:

    # beats 95.11% 32 ms
    def cloneGraph(self, node):

        new_old_node = {}
        def helper_dfs(node):

            if node in new_old_node:
                return new_old_node[node]

            copy = Node(node.val)
            new_old_node[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(helper_dfs(neighbor))

            return copy

        return helper_dfs(node) if node else None

    # 7.2% 53 ms
    def cloneGraph_bfs(self, node):
        # print("Node: ", node)
        if node is None:
            return None

        main_queue = deque()
        main_queue.append(node)

        # adjacency_list = {}
        visited_nodes = set()
        new_visited_nodes = {}

        while len(main_queue) > 0:
            elem = main_queue.popleft()
            visited_nodes.add(elem.val)

            # Create a new adjacency list for new graph
            # if adjacency_list.get(elem.val, []) == []:
            if elem.val not in new_visited_nodes:
                new_elem = Node(elem.val)
                new_visited_nodes[elem.val] = new_elem
                # adjacency_list[new_elem.val] = []
            else:
                new_elem = new_visited_nodes[elem.val]

            neighbor_list = []
            # Visit all neighbors of the current node
            for neighbor in elem.neighbors:
                # Check if neighbor is already visited
                if neighbor.val not in new_visited_nodes:
                    new_neighbor = Node(neighbor.val)
                    new_visited_nodes[neighbor.val] = new_neighbor

                    # adjacency_list.get(new_elem.val, []).append(new_neighbor)
                    neighbor_list.append(new_neighbor)
                else:
                    # adjacency_list.get(new_elem.val, []).append(new_visited_nodes[neighbor.val])
                    neighbor_list.append(new_visited_nodes[neighbor.val])

                if neighbor.val not in visited_nodes:
                    main_queue.append(neighbor)

            new_elem.neighbors = neighbor_list

        # adjacency_list = sorted(adjacency_list, key=adjacency_list.keys())
        # adjacency_list = dict(sorted(adjacency_list.items(), key=lambda kv: (kv[0])))
        # first_key = list(adjacency_list.keys())[0]
        # return_val = new_visited_nodes[first_key]
        # print("adjacency_list: ", adjacency_list)
        # print("new_visited_nodes: ", new_visited_nodes)
        #
        # print("first key: ", first_key)
        #
        # print("return val: ", return_val, "\n\n")
        return new_visited_nodes[1]
