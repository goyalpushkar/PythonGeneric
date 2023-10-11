'''
Find the maximum width of a given binary tree. The width of a particular level is the number of nodes
 (including null nodes) between the end nodes (the leftmost and rightmost non-null nodes) of that level.
 The maximum width of the tree is the maximum width among all levels.

Example
Graph

Output:

3
The maximum width exists at the third level with length 3 (4, null, 5).

Notes
It is guaranteed that the answer will lie within the range of 32-bit signed integer.
Constraints:

1 <= number of nodes in the tree <= 3000
1 <= node value <= 104
'''


def find_maximum_width(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """
    # Write your code here.
    if root is None:
        return 0

    level_queue = deque()
    level_queue.append((root, 0))
    max_width = 0

    while len(level_queue) > 0:

        no_of_nodes = len(level_queue)
        start = 0
        end = 0

        for i in range(no_of_nodes):
            curr, index = level_queue.popleft()

            if i == 0:
                start = index

            if i == no_of_nodes - 1:
                end = index

            if curr.left:
                level_queue.append((curr.left, 2 * index))

            if curr.right:
                level_queue.append((curr.right, (2 * index) + 1))

        level_width = end - start + 1
        max_width = max(max_width, level_width)

    return max_width


# Not working
def find_maximum_width(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """
    # Write your code here.
    if root is None:
        return 0

    level_queue = deque()
    level_queue.append(root)
    max_width = 0
    all_consumed = 0

    while len(level_queue) > 0:

        no_of_nodes = len(level_queue)
        level_width = 0
        null_count = 0
        non_null_found = 0
        print("First", no_of_nodes, all_consumed, max_width)
        if all_consumed == 1:
            max_width = max(max_width, level_width)
            return max_width

        for i in range(no_of_nodes):
            curr = level_queue.popleft()
            print("Second: ", level_width, null_count)
            # Parent is null then add 2 child nodes
            if curr is None:
                null_count += 2
                level_queue.append(None)
                level_queue.append(None)
                all_consumed = 1
            else:
                all_consumed = 0
                if curr.left:
                    print(f"curr.left: {curr.left.value}-{level_width}")
                    level_width += 1
                    if level_width == 1:
                        null_count = 0
                    else:
                        level_width += null_count
                        null_count = 0

                    non_null_found = 1
                    level_queue.append(curr.left)
                else:
                    null_count += 1
                    level_queue.append(None)

                if curr.right:
                    level_width += 1
                    print(f"curr.right: {curr.right.value}-{level_width}")
                    if level_width == 1:
                        null_count = 0
                    else:
                        level_width += null_count
                        null_count = 0

                    non_null_found = 1
                    level_queue.append(curr.right)
                else:
                    null_count += 1
                    level_queue.append(None)

        if all_consumed == 0:
            if non_null_found == 1:
                level_width += null_count

            max_width = max(max_width, level_width)

    return max_width
