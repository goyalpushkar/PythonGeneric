
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

def tree_height(root):
    if not root:
        return 0

    return 1 + max( tree_height(root.left), tree_height(root.right) )

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
       // this is a node of the tree , which contains info as data, left , right
'''

import sys
sys.setrecursionlimit(100000)

def createMinimalBST(arr):
    return createTree_util(arr, 0, len(arr)-1)

def createTree_util(arr, start, end):

    #print( start, end)
    if end < start:
        return None

    mid =  (start + end)//2   #( (end+1) - start ) // 2
    root = Node(arr[mid])

    root.left = createTree_util(arr, start, mid-1) #[:mid]
    root.right = createTree_util(arr, mid+1, end) #[mid+1:]

    return root

if __name__ == '__main__':
    #tree = BinarySearchTree()
    # arr = list(map(int, input().split()))

    t = int(input("No of test cases in the tree: "))

    for i in range(t):
        s = list(map(int,input("Sorted Array: ").rstrip().split() ) )

        root = createMinimalBST(s)

        print("In order traversal")
        inorder_traversal(root)
        print("")
        print("root.data " + str(root.data))

        print("Tree height: ", tree_height(root))