'''
The distance between a node in a Binary Tree and the tree's root is called the node's depth
Write a function that takes n a Binary Tree and returns the sum of its node's depths

Each BinaryTree node has an integer value, left, right child nodes
Children node can either be Binary Tree themselves or None/null

tree =                  1
                 2             3
            4         5   6          7
      8          9

Sample Output
16

'''
# Pushkar 01/18/2022

def nodeDepths(root):
    # Write your code here.
    q1 = []
    q2 = []
    l = -1
    s = 0
    first = 0
    q1.append(root)
    while len(q1) != 0 or len(q2) != 0:
        first = 1
        while len(q1) != 0:
            # if it is the first element
            if first == 1:
                l += 1
                s += l * len(q1)
                first = 0
            # print("q1", l, s, first)

            elem = q1.pop()
            if elem.right:
                q2.append(elem.right)
            if elem.left:
                q2.append(elem.left)

        first = 1
    while len(q2) != 0:
        # if it is the first element
        if first == 1:
            l += 1
            s += l * len(q2)
            first = 0
        # print("q2", l, s, first)

        elem = q2.pop()
        if elem.right:
            q1.append(elem.right)
        if elem.left:
            q1.append(elem.left)

    return s


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def test_case_1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.left.left = BinaryTree(4)
        root.left.left.left = BinaryTree(8)
        root.left.left.right = BinaryTree(9)
        root.left.right = BinaryTree(5)
        root.right = BinaryTree(3)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)
        actual = nodeDepths(root)
        self.assertEqual(actual, 16)
