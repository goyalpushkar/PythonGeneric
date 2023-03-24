'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the
same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
The tree tree could also be considered as a subtree of itself.

Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false

Constraints:
The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Beats 52.8% 127 ms
    def isSubtree(self, root, subRoot):

        def sameTree(tree1, tree2):

            # if both are empty
            if not tree1 and not tree2:
                return True

            if tree1 and tree2 and tree1.val == tree2.val:
                return sameTree(tree1.left, tree2.left) and sameTree(tree1.right, tree2.right)

            return False

        # if not subRoot: return True  # Code will work without this too
        if not root: return False

        if sameTree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    # Beats 99.61% 60ms
    def isSubtree(self, root, subRoot):

        def inorder_traversal(node, traversal):

            if node is None:
                traversal.append("#")
                return

            traversal.append("^")
            inorder_traversal(node.left, traversal)
            traversal.append(str(node.val))
            inorder_traversal(node.right, traversal)

        main_tree = []
        inorder_traversal(root, main_tree)
        sub_tree = []
        inorder_traversal(subRoot, sub_tree)

        m = "".join(main_tree)
        s = "".join(sub_tree)

        print(f"m: {m}\ts: {s}")
        return s in m

        # mT = 0
        # sT = 0
        # while mT < len(self.main_tree):
        #     if self.main_tree[mT] == self.sub_tree[sT]:
        #         sT += 1
        #     else:
        #         if sT != 0:
        #             return False
        #
        #     mT += 1
        #
        #     if sT == len(self.sub_tree):
        #         return True

    # 154/182 testcases passed
    def isSubtree_1st(self, root, subRoot):
        self.main_tree = []
        self.sub_tree = []

        # in_order will not work as subtree should includes node and all of its descendant of the main Tree
        # post_order will not work as subtree should includes node and all of its descendant of the main Tree
        def preorder_traversal(node, main_tree):

            if main_tree:
                self.main_tree.append(node.val)
            else:
                self.sub_tree.append(node.val)

            if node.left:
                preorder_traversal(node.left, main_tree)

            if node.right:
                preorder_traversal(node.right, main_tree)

        preorder_traversal(root, True)
        preorder_traversal(subRoot, False)

        m = "".join(self.main_tree)
        s = "".join(self.sub_tree)

        print(f"m: {m}\ts: {s}")
        # mT = 0
        # sT = 0
        # while mT < len(self.main_tree):
        #     if self.main_tree[mT] == self.sub_tree[sT]:
        #         sT += 1
        #     else:
        #         if sT != 0:
        #             return False
        #
        #     mT += 1
        #
        #     if sT == len(self.sub_tree):
        #         return True

        return s in m