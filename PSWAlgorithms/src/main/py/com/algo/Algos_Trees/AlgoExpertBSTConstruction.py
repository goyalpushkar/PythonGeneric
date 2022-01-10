'''
Write a BST for Binary Search Tree. The class should support:
Inserting values with the insert method
Removing values with the remove method; this method should remove only the first instance of a given value
Searching the values with the contains method

Note that you cant remove values from a single-node tree. In other words, calling the remove method on a single-node
tree should simply not do anything.

Eash BST node has an integer value, a left node and a right node. A node is said to be a valid BST node if and only if
it satisfies the BST property; its value is strictly greater than the values of every node to its left; its value is
strictly less than the values of every node to its right; and its children nodes are either valid BST nodes themselves
or None / null

Usage -
                        10
                    5           15
                2       5 13        22
            1                 14

insert(12) -
                        10
                    5           15
                2       5  13        22
            1            12   14

remove(10) -
                        12
                    5           15
                2       5  13        22
            1                 14

contains(15) - true

'''
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        return self

    def contains(self, value):
        # Write your code here.
        pass

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        return self
