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

                             18
                      11                   26
                7           14         23          32
            4       9   12      15  22    25   29       35
        1        8         13     21         27    30


removal -
Single Node -
    nothing
Root or Middle of the tree -
    if has right
        get the left leaf on right or parent of that left leaf
    else

Leaf -
    No change

Has 2 child -
Has 1 child -


'''
import unittest

# Child type and Parent_node will be None only if traverse_node is root
def traversal(root, value):
    traverse_node = root
    parent_node = None
    child_type = None
    while traverse_node is not None:
        if value == traverse_node.value:
            break
        elif value >= traverse_node.value:
            if traverse_node.right is None:
                break
            else:
                parent_node = traverse_node
                traverse_node = traverse_node.right
                child_type = "RIGHT"

        elif value < traverse_node.value:
            if traverse_node.left is None:
                break
            else:
                parent_node = traverse_node
                traverse_node = traverse_node.left
                child_type = "LEFT"

    return traverse_node, parent_node, child_type


def print_intraversal_tree(root):
    if root.left:
        print_intraversal_tree(root.left)
    print(root.value, "\t")
    if root.right:
        print_intraversal_tree(root.right)


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

        def get_minimum_node(self, node, parent_node=None):
            current_node = node
            while current_node.left is not None:
                parent_node = current_node
                current_node = current_node.left

            return current_node, parent_node

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        current_node = self
        parent_node = None
        # print("insert", value)
        while True:
            # print(current_node.value)
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            else:
                # elif value < current_node.value:
                parent_node = current_node
                current_node = current_node.right

            if value == parent_node.value:
                if current_node is None:
                    parent_node.right = BST(value)
                    break
                else:
                    min_node, min_node_parent = self.get_minimum_node(current_node, parent_node)
                    min_node.left = BST(value)
                    break
            elif current_node is None:
                if value < parent_node.value:
                    parent_node.left = BST(value)
                else:
                    parent_node.right = BST(value)

                break

        return self

    def contains(self, value):
        # Write your code here.
        current_node = self
        parent_node = None
        while True:
            if current_node is None:
                return False
            elif value == current_node.value:
                return True
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            elif value < current_node.value:
                parent_node = current_node
                current_node = current_node.left

    def remove(self, value, parent_node=None):
        # Write your code here.
        # Do not edit the return statement of this method.
        current_node = self
        # print("remove", value, parent_node)
        while True:
            print(current_node.value)
            if value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            elif value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            else:
                # if value == current_node.value:

                # Provided Code
                # if has both child
                # 				if current_node.left is not None and current_node.right is not None:
                # 					replace_node, replace_node_parent = self.get_minimum_node(current_node.right, current_node)
                # 					# print(replace_node.value)
                # 					if replace_node_parent.right == replace_node:
                # 						replace_node_parent.right = replace_node.right
                # 					else:
                # 						replace_node_parent.left = replace_node.right

                # 					current_node.value = replace_node.value
                # # 				# if parent node is None means it is root node
                # 				elif parent_node is None:
                # 					if current_node.left is not None:
                # 						current_node.value = current_node.left.value
                # 						current_node.right = current_node.left.right
                # 						current_node.left = current_node.left.left
                # 					elif current_node.right is not None:
                # 						current_node.value = current_node.right.value
                # 						current_node.left = current_node.right.left
                # 						current_node.right = current_node.right.right
                # 					else:
                # 						# this is single node tree do nothing
                # 						pass
                # 				elif parent_node.right == current_node:
                # 					parent_node.right = current_node.left if current_node.left is not None else current_node.right
                # 				elif parent_node.left == current_node:
                # 					parent_node.left = current_node.left if current_node.left is not None else current_node.right
                # #
                # 				break
                # Provided Code Ended

                # Self code
                # print(current_node.value)
                if parent_node is None:
                    # if no other node then just return
                    if current_node.left is None and current_node.right is None:
                        return self

                # leaf node
                if current_node.left is None and current_node.right is None:
                    if current_node.value < parent_node.value:
                        parent_node.left = None
                    else:
                        parent_node.right = None

                    # if has both child
                elif current_node.left is not None and current_node.right is not None:
                    replace_node, replace_node_parent = self.get_minimum_node(current_node.right, current_node)
                    # print(replace_node.value)
                    if replace_node_parent.right == replace_node:
                        replace_node_parent.right = replace_node.right
                    else:
                        replace_node_parent.left = replace_node.right

                    current_node.value = replace_node.value

                # has only one child
                else:
                    # print("has one child", parent_node, current_node.value)
                    if parent_node is not None:
                        # if parent_node.right is not None:
                        if current_node.value < parent_node.value:
                            # parent_node.right.value == current_node.value:
                            parent_node.left = current_node.left if current_node.left is not None else current_node.right
                        else:
                            parent_node.right = current_node.left if current_node.left is not None else current_node.right
                    else:
                        if current_node.left is not None:
                            current_node.value = current_node.left.value
                            current_node.right = current_node.left.right
                            current_node.left = current_node.left.left
                        elif current_node.right is not None:
                            current_node.value = current_node.right.value
                            current_node.left = current_node.right.left
                            current_node.right = current_node.right.right
                    # else:
                    # current_node.value = current_node.left.value if current_node.left is not None else current_node.right.value
                    # remove_node = current_node.left if current_node.left is not None else current_node.right
                    # remove_node.remove(remove_node.value, current_node)
                    # self.remove(current_node.left.value if current_node.left is not None else current_node.right.value, current_node)
                    # current_node = current_node.left.value if current_node.left is not None else current_node.right.value
                # Self code  Ended
                return self

        return self


# Didnt work for all scenarios
# class BST:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
#     def get_left_node(self, start_node, parent_node):
#         traverse_node = start_node
#         traverse_parent_node = parent_node
#         while traverse_node.left is not None:
#             traverse_parent_node = traverse_node
#             traverse_node = traverse_node.left
#
#         return traverse_node, traverse_parent_node
#
#     def get_right_node(self, start_node, parent_node):
#         traverse_node = start_node
#         traverse_parent_node = parent_node
#         while traverse_node.right is not None:
#             traverse_parent_node = traverse_node
#             traverse_node = traverse_node.right
#
#         return traverse_node, traverse_parent_node
#
#     def insert(self, value):
#         # Write your code here.
#         # Do not edit the return statement of this method.
#         new_node = BST(value)
#         return_node, parent_removal_node, child_type = traversal(self, value)
#         if value == return_node.value:
#             if return_node.right is not None:
#                 insert_node, insert_node_parent = self.get_left_node(return_node.right, return_node)
#                 insert_node.left = new_node
#             else:
#                 return_node.right = new_node
#             # new_node.right = return_node.right
#             # return_node.right = new_node
#         elif value > return_node.value:
#             return_node.right = new_node
#         else:
#             return_node.left = new_node
#         return self
#
#     def contains(self, value):
#         # Write your code here.
#         return_node, parent_removal_node, child_type = traversal(self, value)
#         if return_node is not None:
#             return return_node.value == value
#         else:
#             return False
#
#     def remove(self, value):
#         # Write your code here.
#         # Do not edit the return statement of this method.
#         traverse_node = self
#
#         # If only node then don't do anything
#         if traverse_node.left is None and traverse_node.right is None:
#             return self
#         # else do the whole logic
#         else:
#             removal_node, removal_node_parent, child_type = traversal(traverse_node, value)
#             print(removal_node.value, removal_node_parent, child_type)
#             # Value not found
#             if removal_node.value != value:
#                 return self
#             else:
#                 # if removal_node is leaf then just remove and dont do anything
#                 if removal_node.left is None and removal_node.right is None:
#                     # remove this node
#                     if child_type == "LEFT":
#                         removal_node_parent.left = None
#                     else:
#                         removal_node_parent.right = None
#                 else:
#                     if removal_node.right is not None:
#                         replace_side = "RIGHT"
#                         replace_node, replace_node_parent = self.get_left_node(removal_node.right, removal_node)
#                     else:
#                         replace_side = "LEFT"
#                         replace_node, replace_node_parent = self.get_right_node(removal_node.left, removal_node)
#
#                     print(replace_node.value, replace_node_parent.value)
#
#                     # if replace node is child node replace it with removal node
#                     # else replace the removal node with replace node and replace the replace node
#                     # with its right child
#                     if replace_side == "RIGHT":
#                         if replace_node_parent != removal_node:
#                             if replace_node.right is not None:
#                                 replace_node_parent.left = replace_node.right
#                             else:
#                                 replace_node_parent.left = None
#                                 # if replace_node_parent != removal_node:
#                                 #     replace_node_parent.left = None
#                                 # else:
#                                 #     replace_node_parent.right = None
#                     else:
#                         if replace_node_parent != removal_node:
#                             if replace_node.left is not None:
#                                 replace_node_parent.right = replace_node.left
#                             else:
#                                 replace_node_parent.right = None
#                                 # if replace_node_parent != removal_node:
#                                 #     replace_node_parent.right = None
#                                 # else:
#                                 #     replace_node_parent.left = None
#
#                     if child_type == "LEFT":
#                         removal_node_parent.left = replace_node
#                     elif child_type == "RIGHT":
#                         removal_node_parent.right = replace_node
#                     else:
#                         print("inside else")
#                         removal_node.value = replace_node.value
#
#         return self

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        print("inside test_case_1")
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.left.right = BST(14)
        root.right.right = BST(22)

        root.insert(12)
        print(root.right.left.left.value == 12)
        self.assertTrue(root.right.left.left.value == 12)

        root.remove(10)
        self.assertTrue(not root.contains(10))
        print(not root.contains(10))
        self.assertTrue(root.value == 12)
        print(root.value == 12)

        self.assertTrue(root.contains(15))
        print(root.contains(15))

    def test_case_2(self):
        print("inside test_case_2")
        root = BST(10)
        root.left = BST(5)
        root.right = BST(15)

        root.remove(10)
        self.assertTrue(not root.contains(10))
        print(not root.contains(10))
        self.assertTrue(root.value == 15)
        print(root.value == 15)

        self.assertTrue(root.contains(15))
        print(root.contains(15))

    def test_case_3(self):
        print("inside test_case_3")
        root = BST(1)
        root.insert(2)
        root.insert(3)
        root.insert(4)
        root.insert(5)
        root.insert(6)
        root.insert(7)
        root.insert(8)
        root.insert(9)
        root.insert(10)
        root.insert(11)
        root.insert(12)
        root.insert(13)
        root.insert(14)
        root.insert(15)
        root.insert(16)
        root.insert(17)
        root.insert(18)
        root.insert(19)
        root.insert(20)


        root.remove(2)
        root.remove(4)
        root.remove(6)
        root.remove(8)
        root.remove(11)
        root.remove(13)
        root.remove(15)
        root.remove(17)
        root.remove(19)

        print("print tree")
        print_intraversal_tree(root)
        root.insert(1)

        print("print tree")
        print_intraversal_tree(root)
        root.insert(2)
        root.insert(3)
        root.insert(4)
        root.insert(5)
        root.insert(6)
        root.insert(7)
        root.insert(8)
        root.insert(9)
        root.insert(10)


        self.assertTrue(root.contains(9000))
        print(root.contains(9000))

    def test_case_4(self):
        print("inside test_case_4")
        root = BST(1)
        root.insert(2)
        root.insert(3)
        root.insert(4)
        print("print tree")
        print_intraversal_tree(root)
        root.remove(1)
        print("print tree")
        print_intraversal_tree(root)


if __name__ == '__main__':
    test_program = TestProgram()
    # test_program.test_case_1()
    # print("*******")
    # test_program.test_case_2()
    # print("*******")
    # test_program.test_case_3()
    print("*******")
    test_program.test_case_4()
