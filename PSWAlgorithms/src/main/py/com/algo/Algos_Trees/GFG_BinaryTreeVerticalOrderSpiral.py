'''
Complete the function to print spiral order traversal of a tree. For below tree, function should print 1, 2, 3, 4, 5, 6, 7.





Input:
First line of input contains the number of test cases T. For each test case, there will be only a single line of input which is a string representing the tree as described below:

The values in the string are in the order of level order traversal of the tree where, numbers denotes node values, and a character “N” denotes NULL child.

For example:

For the above tree, the string will be: 1 2 3 N N 4 6 N 5 N N 7 N

Output:
The function should print level order traversal in spiral form.

Your Task:
The task is to complete the function printSpiral() which prints the elements in spiral form of level order traversal. The newline is automatically appended by the driver code.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= T <= 30
0 <= Number of nodes <= 105
1 <= Data of a node <= 105

Example:
Input:
2
1 3 2
10 20 30 40 60
Output:
1 3 2
10 20 30 60 40

Explanation:
Testcase1: The tree is
        1
     /      \
   3       2
So, the spiral level order would be 1 3 2
Testcase2: The tree is
                           10
                        /        \
                     20         30
                  /       \
               40       60
So, the spiral level order would be 10 20 30 60 40


Note: The Input/Ouput format and Example given are used for system's internal purpose, and should be used by a user for Expected Output only. As it is a function problem, hence a user should not read any input from stdin/console. The task is to complete the function specified, and not to write the full code.

'''

class Node:
    def _init_(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root):

        from collections import deque

        if root is None:
            return []

        # bfs_traversal_odd = deque()
        # bfs_traversal_even = deque()
        bfs_traversal = deque()
        return_array = []

        bfs_traversal.append(root)
        level = 1
        while len(bfs_traversal) > 0:  # or len(bfs_traversal_even) > 0:
            internal_array = deque()
            for index in range(len(bfs_traversal)):
                new_elem = bfs_traversal.popleft()
                internal_array.append(new_elem.data)

                if new_elem.left is not None:
                    bfs_traversal.append(new_elem.left)

                if new_elem.right is not None:
                    bfs_traversal.append(new_elem.right)

            # if level % 2 == 1 and len(bfs_traversal_odd) > 0: # odd
            #     for index in range(len(bfs_traversal_odd)):
            #         new_elem = bfs_traversal_odd.popleft()
            #         internal_array.append(new_elem.val)
            #         if new_elem.right is not None:
            #             bfs_traversal_even.append(new_elem.right)

            #         if new_elem.left is not None:
            #             bfs_traversal_even.append(new_elem.left)

            # elif level % 2 == 0 and len(bfs_traversal_even) > 0:   # even
            #     for index in range(len(bfs_traversal_even)):
            #         new_elem = bfs_traversal_even.popleft()
            #         internal_array.append(new_elem.val)
            #         if new_elem.left is not None:
            #             bfs_traversal_even.append(new_elem.left)

            #         if new_elem.right is not None:
            #             bfs_traversal_even.append(new_elem.right)

            # new_values = []
            if level % 2 == 0:  # even
                internal_array.reverse()
                # while len(internal_array) > 0:
                #     new_values.append(internal_array.pop())

            level += 1
            return_array.append(internal_array)

        return return_array

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

        # if right child is not null
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
        sol = Solution()
        res = sol.zigzagLevelOrder(root)

        for i in res:
            print(i, end=" ")

        print()
