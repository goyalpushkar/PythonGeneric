'''
Implement a function to check if a tree is balanced. For the purposes of this question, a balanced tree is defined to be a tree such that no
two leaf nodes differ in distance from the root by more than one
'''

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
from _collections import deque
from queue import Queue
#import math

def is_balanced(root):
    diff = max_level(root) - min_level(root)
        #is_balanced_util(root, 0)
    if diff > 1:
        return False
    else:
        return True

def is_balanced_util(root, current_level):

    if not root:
        return 0

    #return 1 + min(root.left)
    return min( is_balanced_util(root.left, current_level+1), is_balanced_util(root.right, current_level+1)) \
           - max(is_balanced_util(root.left, current_level+1), is_balanced_util(root.right, current_level+1))

'''
def min_level(root, current_level):
    if not (root.left and root.right):
        return current_level

    return min( min_level(root.left, current_level+1), min_level(root.right, current_level+1))
'''

def min_level(root):
    if not root:
        return 0

    return 1 + min(min_level(root.left), min_level(root.right))

'''def max_level(root, current_level):
    if not (root.left and root.right):
        return current_level

    return max( max_level(root.left, current_level+1), max_level(root.right, current_level+1))
'''
def max_level(root):
    if not root:
        return 0

    return 1 + max(max_level(root.left), max_level(root.right))


if __name__ == '__main__':
    #tree = BinarySearchTree()
    # arr = list(map(int, input().split()))

    t = int(input("No of test cases in the tree: "))

    for i in range(t):
        s = input("Nodes: ")
        root = buildTree(s)
        print("In order traversal")
        inorder_traversal(root)
        print("")
        print("root.data " + str(root.data))
        print("Min Level")
        print(min_level(root))
        print("Max Level")
        print(max_level(root))
        print("IS Balanced")
        print(is_balanced(root))