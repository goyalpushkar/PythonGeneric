'''
You have two very large binary trees: T1, with millions of nodes, and T2, with hundreds of nodes.
Create an algorithm to decide if T2 is a subtree of T1
'''


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

    # Beats 52.8% 127 ms
    def isSubtree(self, root, subRoot):

        def sameTree(tree1, tree2):

            # if both are empty
            if not tree1 and not tree2:
                return True

            if tree1 and tree2 and tree1.val == tree2.val:
                return sameTree(tree1.left, tree2.left) and sameTree(tree1.right, tree2.right)

            return False

        if not subRoot: return True
        if not root: return False

        if sameTree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
