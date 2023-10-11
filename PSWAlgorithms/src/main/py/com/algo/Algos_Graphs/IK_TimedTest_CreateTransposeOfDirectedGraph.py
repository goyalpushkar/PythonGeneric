'''
Given a strongly connected directed graph, return its transpose. The graph will be given as a reference to one of its nodes; the rest of the graph can be discovered by walking its edges.

Example
Input: a node of a graph like this:

Input

Output: a node of a graph like this:

Output

Notes
Constraints:

1 <= number of nodes <= 315
Node values are unique integers, and 1 <= node value <= number of nodes
No multiple edges (connecting any pair of nodes in one direction) or self loops (edges connecting a node with itself) in the input graph
Description of the text format of the test cases

You might need this for debugging your solution on IK UpLevel platform.

Input and output file each contain a list or directed edges representing a directed graph.

The input example

Example

is represented by

{
"edges": [
[1, 2],
[2, 3],
[3, 1]
]
}
and the output

Output

is represented by

[
[2, 1],
[3, 2],
[1, 3]
]
'''
"""
For your reference:
class GraphNode:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
"""
from collections import deque


def create_transpose(node):
    """
    Args:
     node(GraphNode_int32)
    Returns:
     GraphNode_int32
    """
    # Write your code here.

    curr_pathstack = deque()
    visited_set = set()
    existing_node = {}
    return_node = GraphNode(-1)

    def dfs(node):
        nonlocal visited_set
        nonlocal curr_pathstack
        nonlocal return_node

        visited_set.add(node)
        curr_pathstack.append(node)
        print("nodevalue: ", node.value)

        # print(visited_set, curr_pathstack)
        for nei in node.neighbors:
            if nei not in visited_set:
                dfs(nei)

            else:
                print("nei.value: ", nei.value)

                if nei.value not in existing_node:
                    prev_node = GraphNode(nei.value)
                    existing_node[nei.value] = prev_node
                else:
                    prev_node = existing_node[nei.value]

                for i in range(len(curr_pathstack)):

                    curr_node = curr_pathstack.pop()
                    print("curr_node.value: ", curr_node.value)

                    if curr_node.value in existing_node:
                        new_node = existing_node[curr_node.value]
                    else:
                        new_node = GraphNode(curr_node.value)
                        existing_node[curr_node.value] = new_node

                    if i == 0:
                        return_node = new_node

                    prev_node.neighbors.append(new_node)

                    prev_node = new_node

                curr_pathstack = deque()
                curr_pathstack.append(node)

        if curr_pathstack:
            curr_pathstack.pop()

    dfs(node)
    return return_node

