'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

The LCA of nodes a and b in a tree is defined as the shared ancestor node of a and b that is located farthest
 from the root of the tree.

Example
Example one

a = 8, b = 9

Output:

5
There are three shared parents of 8 and 9 in this tree: 5, 2, 1. Of those three, the farthest from the root is 5.

Other examples:
LCA(2, 5) = 2
LCA(2, 3) = 1

Notes
A node is considered its own ancestor and its own descendant.
Return the value of the LCA node of the two given nodes.
Constraints:

1 <= number of nodes <= 100000
1 <= node value <= number of nodes
Node values are unique
'''

def lca(root, a, b):
    """
    Args:
     root(BinaryTreeNode_int32)
     a(BinaryTreeNode_int32)
     b(BinaryTreeNode_int32)
    Returns:
     int32
    """
    # Write your code here.
    lca = [None]
    def helper_dfs(node):
        nonlocal lca
        aFound, bFound = False, False
        if node.value == a.value:
            aFound = True

        if node.value == b.value:
            bFound = True

        # if leaf node
        if not node.left and not node.right:
            if aFound and bFound and lca[0] is None:
                lca[0] = node.value
            return aFound, bFound

        if node.left:
            (retaFound, retbFound) = helper_dfs(node.left)
            aFound = aFound or retaFound
            bFound = bFound or retbFound

        if node.right:
            (retaFound, retbFound) = helper_dfs(node.right)
            aFound = aFound or retaFound
            bFound = bFound or retbFound

        if aFound and bFound and lca[0] is None:
            lca[0] = node.value

        return aFound, bFound

    afind, bfind = helper_dfs(root)
    return lca[0] if afind and bfind else None

def lca(root, a, b):

    if root is None:
        return

    def helper_dfs(node):
        left, right = None, None
        if node.value in (a.value, b.value):
            return node.value

        if node.left:
            left = helper_dfs(node.left)

        if node.right:
            right = helper_dfs(node.right)

        if left and right:
            return node.value

        return left or right

    return helper_dfs(root)

#Not working
def lca(root, a, b):
    """
    Args:
     root(BinaryTreeNode_int32)
     a(BinaryTreeNode_int32)
     b(BinaryTreeNode_int32)
    Returns:
     int32
    """
    # Write your code here.
    # Naive approach
    # Perform DFs for both a and b and collect their path in an array
    # compare arrays from back until common node is found.
    # common node is LCA if not found then no LCA

    # Another approach
    # Perform DFS, search for either a or b
    lca = None
    aFound, bFound = False, False

    def helper_dfs(node):
        nonlocal lca, aFound, bFound

        if aFound and bFound:
            return lca

        print(f"node1: {node.value}, lca: {lca}, aFound: {aFound}, bFound: {bFound}, a:{a.value}, b:{b.value}")
        if node.value == a.value or node.value == b.value:
            if not aFound and not bFound:
                lca = a.value if node == a else b.value

            if node.value == a.value:
                aFound = True
            if node.value == b.value:
                bFound = True

            if aFound and bFound:
                return lca

        if node.left:
            helper_dfs(node.left)
            print(f"node after left: {node.value}, lca: {lca}, aFound: {aFound}, bFound: {bFound}")

            # If it is parent node of one of the found nodes and one node is yet to be searched
            # print(f"node.left: {node.left.value}, a.value: {a.value}, b.value: {b.value}, not aFound: {not aFound}, not bFound: {not bFound}")
            # if (node.left.value == a.value or node.left.value == b.value) & (not aFound or not bFound):
            #     lca = node.value

        if not aFound or not bFound:
            lca = node.value
        print(f"node after left reset: {node.value}, lca: {lca}, aFound: {aFound}, bFound: {bFound}")

        if node.right:
            helper_dfs(node.right)
            print(f"node after right return: {node.value}, lca: {lca}, aFound: {aFound}, bFound: {bFound}")

            # if (node.right.value == a.value or node.right.value == b.value) & (not aFound or not bFound):
            #     lca = node.value

        if not aFound or not bFound:
            lca = node.value

        return

    helper_dfs(root)

    return lca if aFound and bFound else None
