'''
You are given a linked list with the continuous sequence of the natural numbers, i.e., 1, 2, ..., n. 
Apart from the standard pointer to the next node, each node also has another one pointing to a random node
in the list. Any of these two pointers may be empty (null, nil). The random pointer may point to the node
itself or any other node in the list.

Clone the list in an efficient manner, both in terms of time and memory usage.

Example
Example

Output:

Return the head of a new list that is identical to the given list, but includes (reuses) none of the nodes from the original list: you must create all nodes of the new list.

Notes
Constraints:

1 <= n <= 105
Description of the text format of the test cases

You might need this for debugging your solution on IK UpLevel platform.

The linked list is represented by a two-dimensional JSON array in both input and output.

Each inner list has three values that mean
[node.value, node.next.value, node.random.value]

Number -1 represents null pointers in the second and third columns: for the next and random pointers, respectively.
'''


"""
For your reference:
"""
class LinkedListNode:
    def __init__(self, node_data):
        self.value = node_data
        self.next = None
        self.random = None

# IK Approach
def clone_linked_list(head):
    """
    Args:
    head(LinkedListNode)
    Returns:
    LinkedListNode
    """
    # Write your code here.
    # 1. add new nodes in between existing list
    # 2. Go through list and add random pointers for next nodes
    # 3. Get the cloned list from original list by breaking links
    
    curr = head
    while curr:
        new_node = LinkedListNode(curr.value)
        
        new_node.next, curr.next = curr.next, new_node
        
        curr = new_node.next
        
    curr = head
    while curr:
        print(f"random curr {curr.value}")
        if curr.random:
            curr.next.random = curr.random.next
        
        if curr.next:
            curr = curr.next.next
    
    sentinel = LinkedListNode(-1)
    traverse_node = sentinel
    curr = head
    while curr:
        # print(f"curr {curr.value}")
        traverse_node.next = curr.next
        
        # print(f"curr.next {curr.next.value}")
        if curr.next:
            curr = curr.next.next 
        
        traverse_node = traverse_node.next
    
    return sentinel.next


# Approach 2
# this handles approach 1 issues but Time and Space complexity is increased
def clone_linked_list(head):
    """
    Args:
    head(LinkedListNode)
    Returns:
    LinkedListNode
    """
    # Write your code here.
    from collections import defaultdict, deque
    sentinel = LinkedListNode(-1)
    traverse_node = sentinel
    curr = head
    random_links = defaultdict(deque)
    node_links = {}
    # print(head.value)
    while curr:
    # for curr in head:
        # print(f"{curr.value}, random_links:{random_links}")
        new_node = LinkedListNode(curr.value)
        node_links[new_node.value] = new_node
        
        # if random link exists for the current node then 
        # save randome link's value in the hash map with new node as value
        if curr.random:
            random_links[curr.random.value].append(new_node)
        
        # if new node had a random link then get its linked node
        # assign current node as random node for the linked node
        # if new_node.value in random_links:
        #     old_node_list = random_links[new_node.value]
        #     # print(f"old_node: {old_node.value}")
        #     for old_node in old_node_list:
        #         if old_node.value <= new_node.value:
        #             old_node_ran = old_node_list.popleft()
        #             old_node_ran.random = new_node
            # del random_links[new_node.value]
        
        traverse_node.next = new_node
        traverse_node = traverse_node.next
        curr = curr.next

    # print(random_links)
    for key, val in random_links.items():
        for old_node in val:
            # print(old_node.value)
            # old_node_ran = val.popleft()
            # old_node.random = new_node
            old_node.random = node_links[key]
    
    # print(sentinel.next.value) 
    return sentinel.next

# Approach 1
# 14/25 - 
# 1. This approach will not work for random backlinks e..g 1 -> 2
# random link between 1 and 2, 2 and 1
# to make it work we may need to save node value and its node to link random backlinks in another iteration
# 2. It will not work if multiple nodes have random link to one node as random node is taken as the key
# T - O(N) but space will become O(N) for the new hashmap
def clone_linked_list(head):
    """
    Args:
    head(LinkedListNode)
    Returns:
    LinkedListNode
    """
    # Write your code here.
    sentinel = LinkedListNode(-1)
    traverse_node = sentinel
    curr = head
    random_links = {}
    # print(head.value)
    while curr:
    # for curr in head:
        # print(f"{curr.value}, random_links:{random_links}")
        new_node = LinkedListNode(curr.value)
        
        # if prev_node:
        #     prev_node.next = new_node
        
        # if random link exists for the current node then 
        # save randome link's value in the hash map with new node as value
        if curr.random:
            random_links[curr.random.value] = new_node
        
        # if new node had a random link then get its linked node
        # assign current node as random node for the linked node
        if new_node.value in random_links:
            old_node = random_links[new_node.value]
            # print(f"old_node: {old_node.value}")
            old_node.random = new_node
        
        # prev = new_node
        traverse_node.next = new_node
        traverse_node = traverse_node.next
        curr = curr.next

    # print(sentinel.next.value) 
    return sentinel.next