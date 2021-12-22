'''
Binary Tree to DLL
Given a Binary Tree (BT), convert it to a Doubly Linked List(DLL) In-Place. The left and right pointers in nodes are to be used as previous and next pointers respectively in converted DLL. The order of nodes in DLL must be same as Inorder of the given Binary Tree. The first node of Inorder traversal (leftmost node in BT) must be the head node of the DLL.

TreeToList

Input:
The first line of input contains the number of test cases T. For each test case, there will be only a single line of input which is a string representing the tree as described below:

The values in the string are in the order of level order traversal of the tree where, numbers denote node values, and a character “N” denotes NULL child.

For example:

For the above tree, the string will be: 1 2 3 N N 4 6 N 5 N N 7 N

Output:
For each test case, in a new line, print front to end and back to end traversals of DLL.

Your Task:
You don't have to take input. Complete the function bToDLL() that takes root node of the tree as a parameter and returns the head of DLL . The driver code prints the DLL both ways.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(H).
Note: H is the height of the tree and this space is used implicitly for recursion stack.

Constraints:
1 <= T <= 100
1 <= Number of nodes <= 1000
1 <= Data of a node <= 1000

Example:
Input:
2
1 3 2
10 20 30 40 60
Output:
3 1 2
2 1 3
40 20 60 10 30
30 10 60 20 40

Explanation:
Testcase1: The tree is
        1
     /      \
   3       2
So, DLL would be 3<=>1<=>2
Testcase2: The tree is
                           10
                        /        \
                     20         30
                  /       \
               40       60
So, DLL would be 40<=>20<=>60<=>10<=>30.


Note: The Input/Output format and Examples given are used for the system's internal purpose, and should be used by a user for Expected Output only. As it is a function problem, hence a user should not read any input from stdin/console. The task is to complete the function specified, and not to write the full code.

'''
'''
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''

def insert_node(current_node, node_det):
    #new_node = Node(node_det.data)

    if current_node != None:
        print("Current Node: " + str(current_node.data))

    if current_node != None:
        current_node.right = node_det
        node_det.left = current_node
    else:
        node_det.left = None
        node_det.right = None

    current_node = node_det
    print("Node: "+ str(current_node.data))
    if current_node.left != None:
        print("Left Node: " + str(current_node.data))

    if current_node.right != None:
        print("Right Node: " + str(current_node.right.data))

    return current_node

#Your task is to complete this function
#function should return head to the DLL
from _collections import deque
def bToDLL(root):
    # do Code here
    inorder_traversal.head_node = None
    #last_node = \
    inorder_traversal(root)
    #prev = None
    while inorder_traversal.head_node.left != None:
        #root.right = prev
        inorder_traversal.head_node = inorder_traversal.head_node.left
        #prev = root

    return inorder_traversal.head_node

def inorder_traversal(root):
    if root != None:
        if root.left != None:
            inorder_traversal(root.left)

        #print(root.data)
        #head_node = insert_node(head_node, root)
        if inorder_traversal.head_node != None:
            root.left = inorder_traversal.head_node
            inorder_traversal.head_node.right = root

        inorder_traversal.head_node = root

        '''
        #Print
        print("Node: " + str(inorder_traversal.head_node.data))
        if inorder_traversal.head_node.left != None:
            print("Left Node: " + str(inorder_traversal.head_node.left.data))

        if inorder_traversal.head_node.right != None:
            print("Right Node: " + str(inorder_traversal.head_node.right.data))
        #Print
        '''

        if root.right != None:
            inorder_traversal( root.right)

    #return inorder_traversal.head_node

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def buildTree(s):
    if (len(s) == 0 or s[0] == "N"):
        return None

    ip = list(map(str, s.split()))

    # Create root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push root to queue
    q.append(root)
    size += 1

    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove front of queue
        currNode = q[0]
        q.popleft()
        size -= 1

        # Get current node's value
        currVal = ip[i]

        # if left child is not null
        if currVal != "N":
            # Create left child for currNode
            currNode.left = Node(int(currVal))

            q.append(currNode.left)
            size += 1

        # For Roght Child
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

import sys
def printDLL(head):
    prev = None
    sys.stdout.flush()
    while head != None:
        print( head.data, end=" ")
        prev = head
        head = head.right

    print(" ")
    while prev != None:
        print(prev.data, end=" ")
        prev = prev.left

    print(" ")

if __name__ == "__main__":
    t = int(input("No of test cases: "))
    for i in range(0, t):
        s = input("Nodes: ")
        root = buildTree(s)
        head = bToDLL(root)

        printDLL(head)

