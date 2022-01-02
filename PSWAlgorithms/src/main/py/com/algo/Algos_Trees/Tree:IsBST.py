'''
For the purposes of this challenge, we define a binary search tree to be a binary tree with the following properties:
The  value of every node in a node's left subtree is less than the data value of that node.
The  value of every node in a node's right subtree is greater than the data value of that node.
The  value of every node is distinct.
For example, the image on the left below is a valid BST. The one on the right fails on several counts:
- All of the numbers on the right branch from the root are not larger than the root.
- All of the numbers on the right branch from node 5 are not larger than 5.
- All of the numbers on the left branch from node 5 are not smaller than 5.
- The data value 1 is repeated.

Given the root node of a binary tree, determine if it is a binary search tree.
Function Description
Complete the function checkBST in the editor below. It must return a boolean denoting whether or not the binary tree is a binary search tree.
checkBST has the following parameter(s):
root: a reference to the root node of a tree to test
Input Format
You are not responsible for reading any input from stdin. Hidden code stubs will assemble a binary tree and pass its root node to your function as an argument.
Constraints

Output Format
Your function must return a boolean true if the tree is a binary search tree. Otherwise, it must return false.
Sample Input
image
Sample Output
Yes
Explanation
The tree in the diagram satisfies the ordering property for a Binary Search Tree, so we print Yes.
'''

#Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def put(self, value):
        if self.root is not None:
            self._put(self, value, self.root)
        else:
            self.root = node(value)

    def _put(self, value, currentNode):
        if value >= currentNode.data:
            if currentNode.right is not None:
                self._put(self, value, currentNode.right)
            else:
                currentNode.right = node(value)

        if value < currentNode.data:
            if currentNode.left is not None:
                self._put(self, value, currentNode.left)
            else:
                currentNode.left = node(value)


from collections import deque
#from DS import DS_BinarySearchTree


def checkBSTFailedGrandchilOutofOrder(root):
    rightStack = deque()
    leftStack = deque()
    node_values = set()

    rightStack.append(root)
    node_values.add(root.data)
    level = 0

    while (len(rightStack) != 0) or (len(leftStack) != 0):
        if level % 2 == 0:
            current_node = rightStack.pop()
            if current_node.left is not None:
                if current_node.left.data < current_node.data:
                    leftStack.append(current_node.left)
                else:
                    return "No"

                if current_node.left.data in node_values:
                    return "No"
                else:
                    node_values.add(current_node.left.data)

            if current_node.right is not None:
                if current_node.right.data > current_node.data:
                    leftStack.append(current_node.right)
                else:
                    return "No"

                if current_node.right.data in node_values:
                    return "No"
                else:
                    node_values.add(current_node.right.data)

        else:
            current_node = leftStack.pop()
            if current_node.right is not None:
                if current_node.right.data > current_node.data:
                    leftStack.append(current_node.right)
                else:
                    return "No"

                if current_node.right.data in node_values:
                    return "No"
                else:
                    node_values.add(current_node.right.data)

            if current_node.left is not None:
                if current_node.left.data < current_node.data:
                    leftStack.append(current_node.left)
                else:
                    return "No"

                if current_node.left.data in node_values:
                    return "No"
                else:
                    node_values.add(current_node.left.data)

        if (level % 2 == 0 and len(rightStack) == 0) or (level % 2 != 0 and len(leftStack) == 0):
            level += 1

    return "Yes"

def checkBSTDidntWork(root):
    #checkBSTRoot(root, -1, 10000)
    checkBSTRoot(root, -float('inf'), float('inf'))

def checkBSTRoot(root, min_value, max_value):
    if root is None:
        return "Yes"

    return min_value <= root.data <= max_value and checkBSTRoot(root.left, min_value, root.data) and checkBSTRoot(root.right, root.data, max_value)

value_set = []  #set()
max_value = -1
duplicate_value = 0
def checkBST(root):
    inOrderTraverse(root)
    # print(duplicate_value)
    #if 'Duplicated' in value_set:
    #    return "No"
    #else:
        #return list(sorted(value_set)) == value_set  # and duplicate_value == 0
    return sorted(set(value_set)) == value_set

def inOrderTraverse(root):
    if root:
        return

    inOrderTraverse(root.left)
    # print(value_set)
    value_set.append(root.data)
    '''
    if root.data in value_set:
        value_set.append("Duplicated")
        duplicate_value = 1
    else:
        value_set.append(root.data)
        if max_value < root.data:
            value_set.append(root.data)
            max_value  = root.data
        else:
            return "No"
    '''
    inOrderTraverse(root.right)

a=[]
def checkBST(root):
    if root:
        checkBST(root.left)
        a.append(root.data)
        checkBST(root.right)
    if sorted(set(a)) == a:
        return True
    else:
        return False

def in_order_traversal(root):
    if root.left:
        in_order_traversal(root.left)

    print(root.info, end=" ")

    if root.right:
        in_order_traversal(root.right)

tree = BinarySearchTree()
t = int(input("No of nodes in the tree: "))
arr = list(map(int, input().split()))
print(arr)
for i in range(t):
    tree.put(arr[i])

in_order_traversal(tree.root)
print(checkBST(tree.root))