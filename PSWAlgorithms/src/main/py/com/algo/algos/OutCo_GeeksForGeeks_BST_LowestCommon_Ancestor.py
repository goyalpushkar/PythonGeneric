'''
Given the root node of a binary tree and two distinct values, find the lowest common ancestor.

Input: Root Node, Two Integer Values
Output: Integer Value of Lowest Common Ancestor

                            5
                    2                   7
                                    4       8
                                                9
Input: root, 4, 9 => Output: 7 LowestCommonAncestor

Time Complexity: O(N)
Auxiliary Space Complexity: O(N)
Integer values of nodes are all distinct.

Binary Tree Node has the following properties:

value (Integer)
right (Binary Tree Node, default null)
left (Binary Tree Node, default null)

The lowest common ancestor is the lowest node in the tree that has both n1 and n2 as descendants, where n1 and n2
are the nodes for which we wish to find the LCA. Hence, the LCA of a binary tree with nodes n1 and n2 is the shared
ancestor of n1 and n2 that is located farthest from the root.

'''
from collections import deque

class Solution:
    # Function to return the lowest common ancestor in a Binary Tree.
    # O(N) - Time and Space
    def lca(self, root, n1, n2):
        # Code here
        node1_path = deque()
        self.find_node(root, n1, node1_path)

        node2_path = deque()
        self.find_node(root, n2, node2_path)

        # print("\n\nfinal path 1")
        # print(node1_path)
        #
        # print("final path 2")
        # print(node2_path)

        # max_length = max(len(node1_path), len(node2_path))
        # Compare values from the paths when mismatched nodes are found that means last node was common ancestor
        return_elem = None
        while len(node2_path) > 0 or len(node1_path) > 0:
            if len(node1_path) > 0:
                elem1 = node1_path.pop()

            if len(node2_path) > 0:
                elem2 = node2_path.pop()

            if elem1.data == elem2.data:
                return_elem = elem1
            else:
                return return_elem

    # Find path for a node -
    # Check in the left sub tree and then right subtree if node is find then save all
    # returning nodes in the path list
    def find_node(self, root, n1, node_path):

        if root is None:
            return False

        # print(root.data)
        # print(elem for elem in node_path)
        if root.data == n1:
            node_path.append(root)
            # print("root")
            # print(node_path)
            return True

        if self.find_node(root.left, n1, node_path):
            node_path.append(root)
            # print("left")
            # print(node_path)
            return True

        if self.find_node(root.right, n1, node_path):
            node_path.append(root)
            # print("right")
            # print(node_path)
            return True

        return False

    # Function to return the lowest common ancestor in a Binary Tree.
    # O(N) - Time and O(H) - Space - Single Traversal
    '''
    The idea is to traverse the tree starting from the root. If any of the given keys (n1 and n2) matches with the root,
     then the root is LCA (assuming that both keys are present). If the root doesn’t match with any of the keys, 
     we recur for the left and right subtree. 

    The node which has one key present in its left subtree and the other key present in the right subtree is the LCA. 
    If both keys lie in the left subtree, then the left subtree has LCA also, 
    Otherwise, LCA lies in the right subtree.  
    '''
    def lca_h(self, root, n1, n2):
        # Code here
        v = [False, False]
        lca = self.lca_helper(root, n1, n2, v)

        # Returns LCA only if both n1 and n2 are present in tree
        if v[0] and v[1] or v[0] and self.find_node(lca, n2) or v[1] and self.find_node(lca, n1):
            return lca

        return None


    def lca_helper(self, root, n1, n2, v):
        if root is None:
            return None

        if root.data == n1:
            v[0] = True
            return root

        if root.data == n2:
            v[1] = True
            return root

        left_lca = self.lca_helper(root.left, n1, n2)
        right_lca = self.lca_helper(root.right, n1, n2)

        if left_lca and right_lca:
            return root

        return left_lca if left_lca is not None else right_lca

    def find_node(self, root, k):
        if root is None:
            return False

        # if k is root or on the left or right subtree
        if root.data == k or self.find(root.left, k) or self.find(root.right, k):
            return True

        return False

# {
# Driver Code Starts
# Initial Template for Python 3

# Contributed by Sudarshan Sharma
from collections import deque


# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


if __name__ == "__main__":
    t = int(input("Enter number of test cases: "))
    for _ in range(0, t):
        a, b = list(map(int, input("Enter Elements to Search for: ").split()))
        s = input("Enter Tree Elements: ")
        root = buildTree(s)
        k = Solution().lca(root, a, b)
        print(k)  # .data

# } Driver Code Ends