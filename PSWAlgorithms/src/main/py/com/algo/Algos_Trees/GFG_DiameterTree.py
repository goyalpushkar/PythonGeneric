# Python3 program to find the diameter of a binary tree
# A binary tree Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Height:
    def __init__(self):
        self.height = 0

class Solution:
    def diameterOfBinaryTree(self, root):
        import math

        def diameter_helper(root, max_height, height):
            if root is None:
                return (max_height, 0)

            left_height = diameter_helper(root.left, max_height, height + 1)
            right_height = diameter_helper(root.right, max_height, height + 1)
            print(f"{' '*height} {root.value} left_height: {left_height}")
            print(f"{' '*height} {root.value} right_height: {right_height}")
            max_height = max(left_height[0], right_height[0], left_height[1] + right_height[1])

            return (max_height, max(left_height[1], right_height[1])+1)

        return diameter_helper(root, -math.inf, 1)[0]


def diameterOpt(root, height):
    # to store height of left and right subtree
    lh = Height()
    rh = Height()

    if root is None:
        height.h = 0
        return 0

    # height of left subtree and right subtree is obtained from lh and rh
    # and returned value of function is stored in ldiameter and rdiameter
    ldiameter = diameterOpt(root.left, lh)
    rdiameter = diameterOpt(root.right, rh)

    # height of tree will be max of left subtree
    # height and right subtree height plus1
    height.height = max(lh.height, rh.height) + 1

    # return maximum of the following
    # 1)left diameter
    # 2)right diameter
    # 3)left height + right height + 1
    return max(lh.height + rh.height + 1, max(ldiameter, rdiameter))

def diameter(root):
    height = Height()
    return diameterOpt(root, height)

if __name__ == "__main__":
    print("Build Tree")
    # Driver Code
    Iroot = Node(1)
    Iroot.left = Node(2)
    Iroot.right = Node(3)
    Iroot.left.left = Node(4)
    Iroot.left.right = Node(5)

    print("Get Diameter")
    print(diameter(Iroot))
