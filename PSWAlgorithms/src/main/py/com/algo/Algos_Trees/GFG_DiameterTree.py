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
    import math
    # Beats 51.4% 49ms
    def diameterOfBinaryTree(self, root):
        
        def height(node):
            if node is None:
                return 0

            lh = height(node.left)
            rh = height(node.right)

            self.max_len = max(self.max_len, lh+rh)

            return max(lh, rh) + 1

        self.max_len = 0
        height(root)
        return self.max_len

    # Beats 68.91% 46ms
    def diameterOfBinaryTree(self, root):
        import math
        def height(node, max_dia):
            if node is None:
                return (0, max_dia)

            lh = height(node.left, max_dia)
            rh = height(node.right, max_dia)

            ht = max(lh[0], rh[0]) + 1
            max_dia = max(lh[0] + rh[0], lh[1], rh[1])

            return (ht, max_dia)

        return height(root, -math.inf)[1]

    def diameterOfBinaryTree(self, root):
        import math

        def diameter_helper(root, max_height, height):
            if root is None:
                return (max_height, 0)

            left_height = diameter_helper(root.left, max_height, height + 1)
            right_height = diameter_helper(root.right, max_height, height + 1)
            # print(f"{' '*height} {root.value} left_height: {left_height}")
            # print(f"{' '*height} {root.value} right_height: {right_height}")
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

# IK - Interview Kickstart
def binary_tree_diameter(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """
    # Write your code here.
    max_dia = 0

    if root is None:
        return max_dia

    def helper(node):
        nonlocal max_dia
        if node.left is None and node.right is None:
            return 1

        left_height = 0
        if node.left:
            left_height = helper(node.left)

        right_height = 0
        if node.right:
            right_height = helper(node.right)

        # diameter for current node
        dia = left_height + right_height
        # max(left_height, right_height) + min(left_height, right_height)
        max_dia = max(max_dia, dia)

        return max(left_height, right_height) + 1

    helper(root)
    return max_dia

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
