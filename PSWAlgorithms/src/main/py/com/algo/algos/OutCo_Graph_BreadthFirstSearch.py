'''
Implement Breadth First Search using a queue and while loop

Input - the starting vertext (will always start at Vertext A)
    Vertices have following property
    id - the data stored in the vertex
    edges - a list of vertices connected to the vertex
Output - a string with the Ids arranged in a breadth first manner
        C
       / \
A --- B    E --- F --- D
       \ /  \   /
        H     G

    Output - ABCHEFGD

This order is one of the possible breadth-first paths. ABHCEFGD is also a valid breadth first traversa,
but be aware this will not match with test expectation
To handle for this, make sure you work with the edges for a node in the order they appear in the node's edge list

http://hr.gs/graph-traversal

'''
# !/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bfs' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. Vertex origin
#


# For your reference:

# Vertex:
#   char id
#   edges[Vertex]
#
from collections import deque

def bfs(origin):
    # Write your code here

    # Queue can be replaced with an array but if number of nodes are too many then length of this array will keep
    # on increasing
    # if array is used instead of queue then visited_nodes array is not required
    node_queue = deque()
    visited_nodes = []
    result = []

    # If empty graph is passed
    if origin.id != None:
        node_queue.append(origin)
        visited_nodes.append(origin)

        # If an array is used then while loop can be replaced with for loop for elements in the array
        # Until all nodes are checked
        while len(node_queue) > 0:

            # deque from the node_queue
            dequeued = node_queue.popleft()

            # check if it has edges and loop through all edges below steps
            for i in range(len(dequeued.edges)):
                edge_of_dequeued = dequeued.edges[i]
                # if not visited add to the queue and append to the visited set
                if edge_of_dequeued not in visited_nodes:
                    visited_nodes.append(edge_of_dequeued)
                    node_queue.append(edge_of_dequeued)

            # add dequeued node to the result
            result.append(dequeued.id)

    return "".join(a for a in result)

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
    vertices = input("Enter name of Vertices: ")
    edges_count = int(input("Enter number of edges: ").strip())
    edges = []

    for _ in range(edges_count):
        edges_item = input("Enter Edge Links as 2 node values: ")
        edges.append(edges_item)

    origin = deserialize(vertices, edges)
    result = bfs(origin)
    print(result)

    # fptr.write(result + '\n')
    # fptr.close()