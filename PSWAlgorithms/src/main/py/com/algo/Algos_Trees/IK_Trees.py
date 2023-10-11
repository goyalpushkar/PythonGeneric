"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
from collections import deque


def build_a_bst_longer(values):
    """
    Args:
     values(list_int32)
    Returns:
     BinaryTreeNode_int32
    """
    # Write your code here.
    if len(values) == 0:
        return None

    # root = values[0]

    def helper_search(node, value, parent):
        if node is None:
            return parent

        if value == node.value:
            return parent
        elif value < node.value:
            return helper_search(node.left, value, node)
        elif value > node.value:
            return helper_search(node.right, value, node)

    def helper_insert(root, value):

        new_node = BinaryTreeNode(value)

        if root is None:
            return new_node

        target_node = helper_search(root, value, None)

        if value < target_node.value:
            target_node.left = new_node
        else:
            target_node.right = new_node

        return root
        # if 2*index+1 < len(values) and values[2*index+1] < values[index]:
        #     new_node.left = helper(2*index+1)
        # else:
        #     new_node.left = None

        # if 2*index+2 < len(values) and  values[2*index+2] >= values[index]:
        #     new_node.right = helper(2*index+2)
        # else:
        #     new_node.right = None

        # return root

    # root = BinaryTreeNode(values[0])
    root = None
    for val in values:
        root = helper_insert(root, val)

    return root


def build_a_bst(values):
    """
    Args:
     values(list_int32)
    Returns:
     BinaryTreeNode_int32
    """
    # Write your code here.
    def helper_insert(node, user_value):
        if node is None:
            return BinaryTreeNode(user_value)

        if user_value < node.value:
            node.left = helper_insert(node.left, user_value)
        else:
            node.right = helper_insert(node.right, user_value)

        return node

    root = None
    for val in values:
        root = helper_insert(root, val)

    return root

def get_maximum_value(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """
    # Write your code here.

    curr = root
    while curr.right is not None:
        # print(curr.value)
        curr = curr.right

    return curr.value

def search_node_in_bst(root, value):
    """
    Args:
     root(BinaryTreeNode_int32)
     value(int32)
    Returns:
     bool
    """
    # Write your code here.
    result = False

    if root is None:
        return result

    def helper(passed_root):
        if passed_root is None:
            return False

        if passed_root.value == value:
            return True

        if helper(passed_root.left) or helper(passed_root.right):
            return True

        return False

    return helper(root)

def delete_from_bst(root, values_to_be_deleted):
    """
    Args:
     root(BinaryTreeNode_int32)
     values_to_be_deleted(list_int32)
    Returns:
     BinaryTreeNode_int32
    """

    '''
        {
        "root": [4,
        2, 7,
        1, 3],
        "values_to_be_deleted": [-1, 0, 8, 9]
        } 
        [4,
        2, 7,
        1, 3]


        {
        "root": [10,
        3, 11,
        -1, 5],
        "values_to_be_deleted": [3, 6, 9]
        }

        [10,
        5, 11,
        -1]

        {
        "root": [5,
        null, 6,
        null, 7,
        null, 8,
        null, 10],
        "values_to_be_deleted": [5, 6, 7, 8]
        } 
        [10]

        {
        "root": [5],
        "values_to_be_deleted": [5]
        }

        [null]


    '''
    def helper_delete(node, val):

        curr_node = node
        prev = None
        while curr_node is not None and val != curr_node.value:

            if val < curr_node.value:
                prev = curr_node
                curr_node = curr_node.left
            else:
                prev = curr_node
                curr_node = curr_node.right

        # in case node not found
        if curr_node is None:
            return node

        # # in case there is only one root node and need to be deleted
        # if prev is None and curr_node.left is None and curr_node.right is None:
        #     # root = None
        #     return -1
        #     # return None

        # Case 1: deleted node does not have any child
        if curr_node.left is None and curr_node.right is None:
            if prev is None:
                node = None
            elif val < prev.value:
                prev.left = None
            else:
                prev.right = None

            return node

        # Case 2: deleted node has one child
        if curr_node.left is None or curr_node.right is None:
            if prev is None:
                node = curr_node.left if curr_node.left is not None else curr_node.right
            elif val < prev.value:
                prev.left = curr_node.left if curr_node.left is not None else curr_node.right
            else:
                prev.right = curr_node.left if curr_node.left is not None else curr_node.right

            return node

        # Case 3: deleted node has two children
        if curr_node.left is not None and curr_node.right is not None:
            # get successor for the current_node
            succ_parent = curr_node
            succ_node = curr_node.right
            while succ_node.left is not None:
                succ_parent = succ_node
                succ_node = succ_node.left

            # if prev is None:
            #     root = succ_node

            curr_node.value = succ_node.value
            # if succ_node is right child
            if succ_parent.right == succ_node:  # curr_node:
                # curr_node.value = succ_node.value
                succ_parent.right = succ_node.right

            # if succ_node is somewhere from left side of right child
            else:
                # curr_node.value = succ_node.value
                succ_parent.left = succ_node.right

            return node

    root_node = root
    for val in values_to_be_deleted:
        root_node = helper_delete(root_node, val)
        # return_val =
        # if return_val == -1:
        #     return None

    return root_node

def level_order_binarytraversal(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    result = []

    if root is None:
        return result

    traverse_queue = deque()
    traverse_queue.append(root)

    while len(traverse_queue) > 0:

        number_of_nodes = len(traverse_queue)
        child_nodes = []
        for i in range(number_of_nodes):
            curr_node = traverse_queue.popleft()

            # if curr_node is not None:
            child_nodes.append(curr_node.value)

            if curr_node.left is not None:
                traverse_queue.append(curr_node.left)

            if curr_node.right is not None:
                traverse_queue.append(curr_node.right)

        result.append(child_nodes)

    return result


def level_order_traversal(root):
    """
    Args:
     root(TreeNode_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    result = []

    if root is None:
        return result

    traverse_queue = deque()
    traverse_queue.append(root)

    while traverse_queue:

        queue_len = len(traverse_queue)
        temp = []

        for index in range(queue_len):

            elem = traverse_queue.popleft()
            temp.append(elem.value)

            for child in elem.children:
                traverse_queue.append(child)

        result.append(temp)

    return result

def preorder(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    result = []

    def preorder_helper(passed_root):
        if passed_root is None:
            return

        result.append(passed_root.value)
        preorder_helper(passed_root.left)
        preorder_helper(passed_root.right)

    preorder_helper(root)

    return result


def inorder(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    result = []

    def inorder_helper(passed_root):
        if passed_root is None:
            return

        inorder_helper(passed_root.left)
        result.append(passed_root.value)
        inorder_helper(passed_root.right)

    inorder_helper(root)

    return result


def postorder(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    result = []

    def postorder_helper(passed_root):
        if passed_root is None:
            return

        postorder_helper(passed_root.left)
        postorder_helper(passed_root.right)
        result.append(passed_root.value)

    postorder_helper(root)

    return result