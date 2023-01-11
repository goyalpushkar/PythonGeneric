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
        self.color = 'Red'   # Black
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


    def get_parent_grandparent(self, node):
        parent_node = node.parent
        cur_side = None
        parent_side = None
        if parent_node is not None:
            grandparent_node = parent_node.parent
        else:
            grandparent_node = None

        # Get the current node's side relative to parent
        if parent_node is not None:
            if node == parent_node.left:
                cur_side = 'left'
            else:
                cur_side = 'right'

        # Get the parent node's side relative to grand-parent
        if grandparent_node is not None:
            if parent_node == grandparent_node.left:
                parent_side = 'left'
            else:
                parent_side = 'right'
        else:
            parent_side = None

        return grandparent_node, parent_node, parent_side, cur_side

    # Perform Recoloring
    def change_parent_grandparent_color(self, node):
        while node is not None:   # node.parent is not None:
            gp_p = self.get_parent_grandparent(node)
            grandparent_node = gp_p[0]
            parent_node = gp_p[1]
            parent_side = gp_p[2]
            curr_side = gp_p[3]

            if parent_node is not None:
                parent_node.color = 'Black'

            if grandparent_node is not None:
                grandparent_node.color = 'Red'

                # Check if uncle is Red
                if parent_side == 'left':
                    if grandparent_node.right is not None:
                        if grandparent_node.right.color == 'Red':
                            # change color of parent and grand-parent and subsequently all the nodes above them
                            grandparent_node.right.color = 'Black'
                else:
                    if grandparent_node.left is not None:
                        if grandparent_node.left.color == 'Red':
                            # change color of parent and grand-parent and subsequently all the nodes above them
                            grandparent_node.left.color = 'Black'

            node = grandparent_node

    def search(self, value):

        def search_helper(value, curr_node):
            if curr_node is None:
                return None

            if value == curr_node.val:
                return curr_node

            if value < curr_node:
                return search_helper(value, curr_node.left)
            else:
                return search_helper(value, curr_node.right)

        return search_helper(value, self.root)

    '''
                                                15
                                8                               20
                     5                  11               18                  24
                3        7           9               16
    
    '''
    def insert_node(self, value):

        # If this is the first node
        if self.root is None:
            self.root = Node(value)
            self.root.color = 'Black'

            return self.root

        # helper method to insert at the right place
        def insert_helper(value, current_node):   # value
            nonlocal new_node
            if current_node is None:
                new_node = Node(value)
                return new_node   # None  # Node(value)

            # print(f"current_node: {current_node.val} \t new_node: {value}\n"
            #       f"current_node.left: {current_node.left.val if current_node.left is not None else current_node.left} \t "
            #       f"current_node.right: {current_node.right.val if current_node.right is not None else current_node.right}")

            # If tree is already populated insert node at the right place
            if value < current_node.val:
                new_node_1 = insert_helper(value, current_node.left)
                # if insert_helper(new_node, current_node.left) is None:
                current_node.left = new_node_1
                new_node_1.parent = current_node
                # else:
                #     insert_helper(new_node, current_node.left)
            else:
                new_node_1 = insert_helper(value, current_node.right)
                # insert_helper(new_node, current_node.right) is None:
                current_node.right = new_node_1
                new_node_1.parent = current_node
                # else:
                #     insert_helper(new_node, current_node.right)

            return current_node

        # If new node is not root node then insert it at its proper place and perform balancing
        new_node = None   # Node(value)
        return_node = insert_helper(value, self.root)
        # new_node = return_node
        print(f"Show Tree Just after inserting the new node - {new_node.val}")
        # self.printtree()
        print("node inserted, proceeding with balancing")

        gp_p = self.get_parent_grandparent(new_node)
        grandparent_node = gp_p[0]
        parent_node = gp_p[1]
        parent_side = gp_p[2]
        curr_side = gp_p[3]

        print(f"new_node: {new_node.val}, curr_side: {curr_side}, "
              f"parent_node: {parent_node.val}, parent_side: {parent_side}, "
              f"grandparent_node: {grandparent_node.val if grandparent_node is not None else grandparent_node }")

        # Do Balancing of the tree
        # if new node is not root and its parent is not black (that means both parent and child are red
        # that contradicts the definition of red-black tree)
        if new_node != self.root and parent_node.color == 'Red':

            # Check if uncle is Red
            uncle_color = "Black"
            if parent_side == 'left':
                if grandparent_node is not None and grandparent_node.right is not None:
                    if grandparent_node.right.color == 'Red':
                        # change color of parent and grand-parent and subsequently all the nodes above them
                        uncle_color = "Red"
            else:
                if grandparent_node is not None and grandparent_node.left is not None:
                    if grandparent_node.left.color == 'Red':
                        # change color of parent and grand-parent and subsequently all the nodes above them
                        uncle_color = "Red"

            # if uncle is Red, do recoloring
            if uncle_color == "Red":
                self.change_parent_grandparent_color(new_node)

            # if uncle is black, do rotation and recoloring
            else:
                if parent_side == "left" and curr_side == "left":
                    self.rotate_right(grandparent_node)
                    parent_node.color, grandparent_node.color = grandparent_node.color, parent_node.color
                elif parent_side == "left" and curr_side == "right":
                    self.rotate_left(parent_node)
                    self.rotate_right(new_node)
                    new_node.color, grandparent_node.color = grandparent_node.color, new_node.color
                elif parent_side == "right" and curr_side == "left":
                    self.rotate_right(parent_node)
                    self.rotate_left(grandparent_node)
                    new_node.color, grandparent_node.color = grandparent_node.color, new_node.color
                elif parent_side == "right" and curr_side == "right":
                    self.rotate_left(grandparent_node)
                    parent_node.color, grandparent_node.color = grandparent_node.color, parent_node.color

        return new_node


    def delete_node(self, value):
        return self.root


    def inordertraversal(self):

        def inordertraversal_helper(space, curr_node):
            if curr_node is not None:
                space += 5
                inordertraversal_helper(space, curr_node.left)
                print(f"{' '*space} {curr_node.val} {curr_node.color}")
                inordertraversal_helper(space, curr_node.right)

        inordertraversal_helper(0, self.root)

    def printtree(self):

        def printtree_helper(space, curr_node):
            if curr_node is not None:
                space += 10
                printtree_helper(space, curr_node.right)
                append_length = space - 10
                print(f"\n{'  '*space} {curr_node.val} {curr_node.color}")
                printtree_helper(space, curr_node.left)

        printtree_helper(0, self.root)


if __name__ == '__main__':
    no_of_nodes = int(input("Enter number of nodes: "))

    red_black_tree = RedBlackTree()
    for i in range(no_of_nodes):
        node_data = int(input("Enter node value: "))
        red_black_tree.insert_node(node_data)
        red_black_tree.inordertraversal()

    print(red_black_tree.root.val)
    red_black_tree.printtree()