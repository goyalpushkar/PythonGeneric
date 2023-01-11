'''
Given a starting vertex, and a string destination, return all valid paths for a given source and destination

Input - Origin - the starting vertext
        destination - integer value of the destination vertex
    Vertices have following property
    id - the data stored in the vertex
    edges - a list of vertices connected to the vertex
Output - a sorted array of all paths fropm the origin to the destination

        C
       / \
A --- B    E --- F --- D
       \ /  \   /
        H     G

    Origin A
    Destination - D

    Output - ["ABCEFD", "ABCEGFD", "ABHEFD", "ABHEGFD"]

There are 4paths from vertext A to vertex D. These 4 paths are listed above and then sorted within their array

Contrary to breadth-first traversal to find all paths, it is advised to use depth-first traversal
implemented with recursion
There is no difference the dashed lines and forward/back slashes when it comes to defining the connections between
graph nodes
Use a set or hash map to handle redundancy

http://hr.gs/graph-traversal
'''
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'find_all_paths' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. Vertex origin
#  2. STRING destination
#

# For your reference:

# Vertex:
#   char id
#   edges[Vertex]
#

def find_all_paths(origin, destination):
    # Write your code here

    def all_paths(all_found_paths, path, current_node):
        print(f"path: {path} \n"
              f"current_node: {current_node.id}\n")
        if current_node.id == destination:
            all_found_paths.append("".join(elem for elem in path))
            print(f"all_found_paths: {all_found_paths}\n\n")
            return all_found_paths, path[:-1]

        for i in range(len(current_node.edges)):
            print(f"current_node.edges[i].id: {current_node.edges[i].id}\n"
                  f"path: {path} \n")
            if current_node.edges[i].id not in path:
                path.append(current_node.edges[i].id)
                all_found_paths, path = all_paths(all_found_paths, path, current_node.edges[i])

        return all_found_paths, path[:-1]

    all_found_paths = []
    path = [origin.id]
    all_found_paths, path = all_paths(all_found_paths, path, origin)

    return all_found_paths

# DO NOT EDIT
# Vertex class for a graph vertex
class Vertex:
    def __init__(self, id=None):
        self.id = id
        self.edges = []

# DO NOT EDIT
# generate graph from int and list of lists
def deserialize(vertices, edges):
    container = {}
    for i in range(0, len(vertices)):
        container[vertices[i]] = Vertex(vertices[i])
    for edge in edges:
        v1 = edge[0]
        v2 = edge[1]
        container[v1].edges.append(container[v2])
        container[v2].edges.append(container[v1])
    return container[vertices[0]]

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    vertices = input("Enter name of vertices: ")  # ABCDEFGH
    edges_count = int(input("Enter number of edges: ").strip())   # 9
    edges = []

    for _ in range(edges_count):
        edges_item = input("Enter Edge Links as 2 node values: ") # AB BC CE DF EF BH EG EH FG
        edges.append(edges_item)

    destination = input("Enter destination: ")   # D
    origin = deserialize(vertices, edges)

    result = find_all_paths(origin, destination)

    result.sort()
    print(result)

    # fptr.write('\n'.join(result))
    # fptr.write('\n')
    # fptr.close()