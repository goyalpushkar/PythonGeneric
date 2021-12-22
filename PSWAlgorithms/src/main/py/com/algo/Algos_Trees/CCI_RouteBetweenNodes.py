'''
Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
'''

from _collections import deque
from queue import Queue
#import math

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def buildTree(s):
    if (len(s) == 0 or s[0] == "N"):
        return None

    ip = list(map(str, s.split()))
    print(ip)
    #Create root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    #Push root to queue
    q.append(root)
    size += 1

    i = 1
    while (size > 0 and i < len(ip)):
        #Get and remove front of queue
        currNode = q[0]
        q.popleft()
        size -= 1

        #Get current node's value
        currVal = ip[i]

        #if left child is not null
        if currVal != "N":
            #Create left child for currNode
            currNode.left = Node(int(currVal))

            q.append(currNode.left)
            size += 1

        #For Right Child
        i += 1
        if i > len(ip):
            break
        currVal = ip[i]

        # if left child is not null
        if currVal != "N":
            # Create left child for currNode
            currNode.right = Node(int(currVal))

            q.append(currNode.right)
            size += 1

        i += 1

    return root

def inorder_traversal(root):
    if root:
        if root.left:
            inorder_traversal(root.left)

        print(root.data, end=" ")

        if root.right:
            inorder_traversal(root.right)

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
       // this is a node of the tree , which contains info as data, left , right
'''

from collections import deque
def is_path(graph, node1, node2):

    visited_nodes = {}
    for node in graph.allnodes:
        visited_nodes[node] = 0

    traverse_nodes = deque()
    traverse_nodes.append(node1)

    found = false
    while len(traverse_nodes) > 0 and not found:
        process_node = traverse_nodes.pop()

        for node in process_node.get_adjacent_nodes():
            if visited_nodes[node] == 0:  #If already visited dont insert again
                traverse_nodes.append(node)
                visited_nodes[node] = 1
                if node == node2:
                    return True

        visited_nodes[process_node] = 1

    return False
if __name__ == '__main__':
    t = int(input("No of test cases in the tree: "))

    for i in range(t):
        s = input("Nodes: ")
        root = buildTree(s)

        print("In order traversal")
        inorder_traversal(root)
        print("")
        print("root.data " + str(root.data))

        print("IS Path")
        print(is_path(graph, node1, node2))