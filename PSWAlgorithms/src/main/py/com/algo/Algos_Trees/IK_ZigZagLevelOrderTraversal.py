'''
Given a binary tree, return the zigzag level order traversal of the node values listing
the odd levels from left to right and the even levels from right to left.

Example One
Example one

Output:

[
[0],
[2, 1],
[3, 4]
]
Example Two
Example two

Output:

[
[0],
[1],
[2],
[3]
]
Notes
Root node is considered to be at the level 1.

Constraints:
1 <= number of nodes in the given tree <= 20000
0 <= node value < number of nodes
Node values are unique
'''
def zigzag_level_order_traversal(root):
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
    level = 0

    while len(traverse_queue) > 0:

        number_of_nodes = len(traverse_queue)
        child_nodes = []
        for i in range(number_of_nodes):
            curr_node = traverse_queue.popleft()

            child_nodes.append(curr_node.value)

            if curr_node.left is not None:
                traverse_queue.append(curr_node.left)

            if curr_node.right is not None:
                traverse_queue.append(curr_node.right)

        if level % 2 > 0:
            child_nodes.reverse()

        result.append(child_nodes)
        level += 1

    return result


# Another approach is to use 2 Stacks and push left to right and right to left alternatively
'''
static ArrayList<ArrayList<Integer>> zigzag_level_order_traversal(BinaryTreeNode root) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<>();

        if (root == null) {
            return result;
        }

        Stack<BinaryTreeNode> current_level = new Stack<>(), next_level = new Stack<>();

        boolean left_to_right = true; // First level is traversed from left to right.
        current_level.push(root);

        while (!current_level.isEmpty()) {
            int current_level_node_count = current_level.size();
            ArrayList<Integer> level_labels = new ArrayList<>();

            // Traversing all the nodes of the current level.
            for (int i = 0; i < current_level_node_count; ++i) {
                BinaryTreeNode node = current_level.pop();

                level_labels.add(node.value);

                // If the current level is traversed from left to right,
                // the next level will be traversed from right to left.
                // But since a stack follows the last-in-first-out property,
                // we will push the left child before the right child
                // so that the right child gets popped out first from the next level.
                if (left_to_right) {
                    if (node.left != null) {
                        next_level.push(node.left);
                    }
                    if (node.right != null) {
                        next_level.push(node.right);
                    }
                }

                // If the current level is traversed from right to left,
                // the next level will be traversed from left to right.
                else {
                    if (node.right != null) {
                        next_level.push(node.right);
                    }
                    if (node.left != null) {
                        next_level.push(node.left);
                    }
                }
            }

            result.add(level_labels);
            left_to_right = !left_to_right;

            // The current "next_level" will be the "current_level" of the next iteration.
            Stack<BinaryTreeNode> temp1 = new Stack<>(), temp2 = new Stack<>();

            // Swapping current_level and next_level
            while (!next_level.isEmpty()) {
                temp1.push(next_level.pop());
            }
            while (!current_level.isEmpty()) {
                temp2.push(current_level.pop());
            }
            while (!temp1.isEmpty()) {
                current_level.push(temp1.pop());
            }
            while (!temp2.isEmpty()) {
                next_level.push(temp2.pop());
            }
        }

        return result;
    }
    '''