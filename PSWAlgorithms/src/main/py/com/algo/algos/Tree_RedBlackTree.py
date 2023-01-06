'''
Red Black Tree
Rules That Every Red-Black Tree Follows:
	1. Every node has a color either red or black.
	2. The root of the tree is always black.
	3. There are no two adjacent red nodes (A red node cannot have a red parent or red child).
	4. Every path from a node (including root) to any of its descendants NULL nodes has the same number of black nodes.
	5. All leaf nodes are black nodes.

'''
class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.color = 'Red'
        self.parent = None

class RedBlackTree:

    def __init__(self):
        self.root = None

    '''
                                     P
                         q                    r
                    s         t           u        v
    '''
    def rotate_left(self, node):
        # consider if node to be rotated is parent node i.e. P then
        # you have to think to rotate using node.right (r) and node.right.left (u)
        r = node.right
        u = r.left

        node.right = u
        if u is not None:
            u.parent = node

        r.left = node
        node.parent = r

        return r


    def rotate_right(self, node):
        q = node.left
        t = q.right

        node.left = t
        if t is not None:
            t.parent = node

        q.right = node
        node.parent = q

        return q


    def insert_node(self, node):
        return node

    def delete_node(self, value):
        return self.root

