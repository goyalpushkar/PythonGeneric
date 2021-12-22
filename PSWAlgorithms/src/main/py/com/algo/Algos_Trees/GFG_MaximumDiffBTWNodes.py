'''
Given a Binary Tree, you need to find the maximum value which you can get by subtracting the value of node B from the value of node A, where A and B are two nodes of the binary tree and A is an ancestor of B.

Input:
The first line of input contains the number of test cases T. For each test case, there will be only a single line of input which is a string representing the tree as described below:

The values in the string are in the order of level order traversal of the tree where, numbers denote node values, and a character “N” denotes NULL child.

For example:

For the above tree, the string will be: 1 2 3 N N 4 6 N 5 N N 7 N

Output:
The function should return an integer denoting the maximum difference.

User Task:
The task is to complete the function maxDiff() which finds the maximum difference between the node and its ancestor.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(H).
Note: H is the height of the tree.

Constraints:
1 <= T <= 30
1 <= Number of edges <= 104
0 <= Data of a node <= 105

Example:
Input:
2
5 2 1
1 2 3 N N N 7
Output:
4
-1

Explanation:
Testcase 1:

             5
           /    \
         2      1
The maximum difference we can get is 4, which is bewteen 5 and 1.

Testcase 2:

             1
           /    \
         2      3
                   \
                    7
The maximum difference we can get is -1, which is between 1 and 2.
'''

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

import sys
from _collections import deque

def maxDiff(root):
    '''
    :param root: Root of given tree
    :return: Integer
    '''
    # code here
    min_node, result = min_value(root, -sys.maxsize)
    return result

def min_value(node, result):

    if node is None:
        return sys.maxsize, result

    if node.left is None and node.right is None:
        return node.data, result

    left_node, result = min_value(node.left, result)
    right_node, result = min_value(node.right, result)

    minimum_value = min(left_node, right_node)

    result = max(result, node.data - minimum_value)

    return min(minimum_value, node.data), result

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def buildTree(s):
    if (len(s) == 0 or s[0] == "N"):
        return None

    ip = list(map(str, s.split()))

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

        #For Roght Child
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

if __name__ == "__main__":
    t = int(input("No of test cases: "))
    for i in range(0, t):
        s = input("Nodes: ")
        root = buildTree(s)

        print(maxDiff(root))
