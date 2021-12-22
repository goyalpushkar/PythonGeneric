'''

'''
class Node:
    def __init__(self, val, parent):
        self.info = val
        self.parent = parent
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val, None)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val, current)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val, current)
                        break
                else:
                    break

def inorder_traversal(root):
    if root:
        if root.left:
            inorder_traversal(root.left)

        print(root.info, end = " ")
        if root.parent:
            print(" :Parent - ", root.parent.info, end = " ")
        if in_order_successor(root):
            print(" :In order successor - ", in_order_successor(root).info, end = " ")
        print()

        if root.right:
            inorder_traversal(root.right)

from collections import deque

def in_order_successor(root):
    if root:
        if root.parent is None or root.right is not None:
            succesor = find_leftmost(root.right)
        else:
            traverse_node = root.parent
            while traverse_node is not None:
                if traverse_node.left == root:
                    break
                else:
                    if traverse_node.parent is not None:
                        traverse_node = traverse_node.parent
                    else:
                        break

            succesor = traverse_node

        return succesor

def find_leftmost(node):
    traverse_node = node
    while traverse_node.left is not None:
        traverse_node = traverse_node.left

    return traverse_node

if __name__ == '__main__':
    #tree = BinarySearchTree()
    # arr = list(map(int, input().split()))

    t = int(input("No of test cases in the tree: "))

    for i in range(t):
        tree = BinarySearchTree()
        t = int(input("No of nodes in the tree: "))
        arr = list(map(int, input().split()))

        for i in range(t):
            tree.create(arr[i])

        print("In order traversal")
        inorder_traversal(tree.root)
        print("")
        print("root.info " + str(tree.root.info))

        print("In Order Succesor")
        succesor = in_order_successor(tree.root)
        print(succesor.info)