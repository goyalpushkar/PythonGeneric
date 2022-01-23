'''
Write a functon that takes potentially invalid BST and returns a boolean representing whether BST is valid or not

Eash BST node has an integer value, a left node and a right node. A node is said to be a valid BST node if and only if
it satisfies the BST property; its value is strictly greater than the values of every node to its left; its value is
strictly less than the values of every node to its right; and its children nodes are either valid BST nodes themselves
or None / null

Usage -
                        10
                    5           15
                2       5 13        22
            1                 14

output - True
'''
import unittest

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def print_intraversal_tree(root):
    if root.left:
        print_intraversal_tree(root.left)
    print(root.value, "\t")
    if root.right:
        print_intraversal_tree(root.right)


def intraversal(root, rooted_array):
    if root.left:
        intraversal(root.left, rooted_array)

    rooted_array.append(root.value)

    if root.right:
        intraversal(root.right, rooted_array)


def checkminmax(minvalue, node, maxvalue):
    if node is not None:
        print(minvalue, node.value, maxvalue)
    else:
        print(minvalue, None, maxvalue)
    if node is None:
        return True
    elif minvalue > node.value or node.value >= maxvalue:
        return False
    else:
        return checkminmax(minvalue, node.left, node.value) and checkminmax(node.value, node.right, maxvalue)

    return True

def validateBst(tree):
    # Write your code here.
    return checkminmax(float("-inf"), tree, float("inf"))


# this does not work for test case 3 where equal node should be on the right side not on the left side
def validateBst_2NPerformance(tree):
    # Write your code here.
    rooted_values = []
    intraversal(tree, rooted_values)
    for index in range(len(rooted_values)-1):
        if rooted_values[index+1] < rooted_values[index]:
            return False

    return True


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        print("********1********")
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.left.right = BST(14)
        root.right.right = BST(22)
        print_intraversal_tree(root)
        print(validateBst(root))
        self.assertEqual(validateBst(root), True)

    def test_case_2(self):
        print("********2********")
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(11)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.left.right = BST(14)
        root.right.right = BST(22)
        print_intraversal_tree(root)
        print(validateBst(root))
        # self.assertEqual(validateBst(root), True)

    def test_case_3(self):
        print("********3********")
        root = BST(10)
        root.left = BST(5)
        root.left.right = BST(10)
        root.right = BST(15)
        print(validateBst(root))
        self.assertEqual(validateBst(root), True)


if __name__ == '__main__':
    testprogram = TestProgram()
    testprogram.test_case_1()
    # testprogram.test_case_2()
    # testprogram.test_case_3()
