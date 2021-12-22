'''
Given a Binary Tree, print the vertical traversal of it starting from the leftmost level to the rightmost level.
If there are multiple nodes passing through a vertical line, then they should be printed as they appear in level order traversal of the tree.

Input Format:
First line of input contains the number of test cases T. For each test case, there will be only a single line of input which is a string representing the tree as described below:

The values in the string are in the order of level order traversal of the tree where, numbers denotes node values, and a character “N” denotes NULL child.

For example:

For the above tree, the string will be: 1 2 3 N N 4 6 N 5 N N 7 N

Output Format:
For each testcase, the vertical order traversal of the tree is to be printed. The nodes' data are to be separated by spaces.

Your Task:
You don't need to read input or print anything. Your task is to complete the function verticalOrder() which takes the root node as input and returns an array containing the vertical order traversal of the tree from the leftmost to the rightmost level. If 2 nodes lie in the same vertical level, they should be printed in the order they appear in the level order traversal of the tree.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= T <= 100
1 <= Number of nodes <= 5000

Example:
Input:
3
2 N 3 4 N
1 2 3 4 5 N 6
3 1 5 N 2 4 7 N N N N 6
Output:
2 4 3
4 2 1 5 3 6
1 3 2 4 5 6 7
Explanation:
Testcase1:
         2
           \
            3
            /
         4
As it is evident from the above diagram that during vertical traversal 2, 4 will come first, then 3. So output is 2 1 5 3
Testcase2:
             1
           /     \
         2       3
      /     \        \
    4       5       6
As it is evident from the above diagram that during vertical traversal 4 will come first, then 2, then 1,5, then 3 and then 6. So the output is
 4 2 1 5 3 6.

Note: The Input/Ouput format and Example given are used for system's internal purpose, and should be used by a user for Expected Output only. As it is a function problem, hence a user should not read any input from stdin/console. The task is to complete the function specified, and not to write the full code.

** For More Input/Output Examples Use 'Expected Output' option **
'''


'''
Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

from _collections import deque
from queue import Queue

def verticalOrder(root):
    #Your code here
    dict_nodes = {}
    queue_nodes = Queue()
    min = 0
    max = 0

    queue_nodes.put((root, 0))

    while queue_nodes.qsize() > 0:

        get_node = queue_nodes.get()
        curr_node = get_node[0]
        curr_node_level = get_node[1]

        if min > curr_node_level:
            min = curr_node_level

        if max < curr_node_level:
            max = curr_node_level

        if (curr_node_level in dict_nodes):
            dict_nodes.get(curr_node_level).append(curr_node.data)
        else:
            dict_nodes[curr_node_level] = [curr_node.data]

        if curr_node.left:
            queue_nodes.put((curr_node.left, curr_node_level - 1))

        if curr_node.right:
            queue_nodes.put((curr_node.right, curr_node_level + 1))

    ret_arr = []
    for index in range(min, max + 1):
        arr = dict_nodes[index]
        for index in range(len(arr)):
            ret_arr.append(arr[index])

    return ret_arr

class Node:
    def _init_(self, val):
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
    while (size > 0 and i < len(p)):
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
        res = verticalOrder(root)

        for i in res:
            print(i)  #, end=""

        print()
