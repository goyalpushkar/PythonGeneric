'''
Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not necessarily a binary search tree.
'''
class Node:
    def __init__(self, val):
        self.info = val
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

#Problem with this approach nodes are geting traversed multiple times once in checkExistence and then in FCA
def first_common_ancestor(root, node1, node2):
    if checkExistence(root.left, node1) and checkExistence(root.left, node2):
        return first_common_ancestor(root.left, node1, node2 )

    if checkExistence(root.right, node1) and checkExistence(root.right, node2):
        return first_common_ancestor(root.right, node1, node2 )

    return root

def checkExistence(root, p):
    if root is None:
        return False

    if root == p:
        return True

    return checkExistence(root.left, p) or checkExistence(root.right, p)

#New Faster Way
def lowestCommonAncestor(self, root, p, q):
    if root in (None, p, q): return root
        left, right = (self.lowestCommonAncestor(kid, p, q)
                   for kid in (root.left, root.right))
        return root if left and right else left or right


def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root:
        return

    if root == p or root == q:
        return root

    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root

    if left:
        return left

    if right:
        return right

if __name__ == '__main__':
    t = int(input("No of test cases in the tree: "))

    for i in range(t):
        s = input("Nodes: ")
        root = buildTree(s)

        print("In order traversal")
        inorder_traversal(root)
        print("")
        print("root.data " + str(root.data))

        node1 = input("Node1: ")
        node2 = input("Node2: ")

        first_common_ancestor(root, node1, node2)

