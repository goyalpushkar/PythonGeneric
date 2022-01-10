'''
Write a function that takes in Binary Tree and returns its list of branch sums ordered from leftmost branch sum to
rightmost branch sum

A branch sum is the sum of all values in a Binary Tree branch. A binary tree branch is a path of the nodes in a tree
that starts at the root node and ends at any leaf node

Each binary Tree node has an integer value, a left child node, and a right child node.
Children nodes can either be Binary Tree nodes themselves or None/ null.

Input -
                     1
                2           3
            4       5   6       7
         8     9 10

Output - [15,16,18,10,11]
15 = 1 + 2 + 4 + 8
16 = 1 + 2 + 4 + 9
18 = 1 + 2 + 5 + 10
10 = 1 + 3 + 6
11 = 1 + 3 + 7

Time - O(n) | Space - O(n) where n is number of nodes in the Binary tree

'''

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    output = []
    pre_order_traversal(root, 0, output)
    return output


def pre_order_traversal(node, running_sum, output):
    running_sum += node.value

    if node.left is not None:
        pre_order_traversal(node.left, running_sum, output)

    if node.left is None and node.right is None:
        # print(running_sum)
        output.append(running_sum)
        running_sum = 0

    if node.right is not None:
        pre_order_traversal(node.right, running_sum, output)