'''
Given a binary search tree, design an algorithm which creates a linked list of all the nodes at each depth
(i.e., if you have a tree with depth D, you’ll have D linked lists).
'''
class Node:
    def __init__(self, val):
        self.info = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def inorder_traversal(root):
    if root:
        if root.left:
            inorder_traversal(root.left)

        print(root.info, end=" ")

        if root.right:
            inorder_traversal(root.right)

from collections import deque

class LinkedListNode():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        if self.head is None:
            self.head = LinkedListNode(data)
            self.tail = self.head
        else:
            self.tail.next = LinkedListNode(data)
            self.tail = self.tail.next

    def print_list(self):
        traverse_list = self.head
        while traverse_list is not None:
            print( traverse_list.data, end = " " )
            traverse_list = traverse_list.next

def depth_linked_list(root):

    level = 0
    even_queue = deque()
    odd_queue = deque()
    array_linked_list = []

    even_queue.append(root)
    level_linked_list = LinkedList()

    while len(even_queue) > 0 or len(odd_queue) > 0:
        if level % 2 == 0:
            new_node = even_queue.popleft()
            level_linked_list.add_node(new_node.info)

            if new_node.left:
                odd_queue.append(new_node.left)

            if new_node.right:
                odd_queue.append(new_node.right)

            if len(even_queue) == 0:
                print("level: ", level)
                array_linked_list.append(level_linked_list)
                level += 1
                level_linked_list = LinkedList()

        else:
            new_node = odd_queue.popleft()
            level_linked_list.add_node(new_node.info)

            if new_node.left:
                even_queue.append(new_node.left)

            if new_node.right:
                even_queue.append(new_node.right)

            if len(odd_queue) == 0:
                print("level: ", level)
                array_linked_list.append(level_linked_list)
                level += 1
                level_linked_list = LinkedList()

    return array_linked_list

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

        print("Linked List for  each depth")
        returned_lists = depth_linked_list(tree.root)
        for level in range(len(returned_lists)):
            link_list = returned_lists[level]
            print("list at level: ", level)
            link_list.print_list()
            print(" ")