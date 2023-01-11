'''
Given the head node of a singly linked list, return the value of one of the nodes at random from the linked list.

The node value that is returned must be fairly random. How can we test this out?

(1) -> (5) -> (7) -> (10)
        ^
        |
Input: (1)
Output: 5

// If we were to call the function on the above linked list 100 times, we would
// expect the frequency of each node value to return approximately 25 times.
// Should resemble:

{
  1: 25
  5: 25
  7: 25
  10: 25
}

'''

import random
import math

class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = ListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

    def printForward(self):
        # Write your code here
        node = self.head
        array_print = []
        while (node is not None):
            # print(node.val)
            array_print.append(node.val)
            node = node.next

        print( " ".join(str(elem) for elem in array_print) )

# O(N) Auxilliary spoce
def random_value_On(head):

    # If list is empty
    if head is None:
        return None

    # It will have additional space but this can be avoided by taking 2 loops
    ll_array = []
    ll_len = 0

    # Loop through all elements and store them in an array
    travers_node = head
    while travers_node is not None:
        ll_len += 1
        ll_array.append(travers_node.val)
        travers_node = travers_node.next

    # Get Random value
    random_val = random.random()
    index = math.floor(random_val * ll_len)

    # -1 added if random_val is 1
    # if array is not used then do another loop start=1, increment start by 1 after each elem
    # and return value at start=index-1
    return_val = ll_array[index-1]

    return return_val

# O(1) Auxilliary spoce
'''
p(i) = p1 . p2

Where: 
- p1= probability of Math.random < 1/i upon iterating item i
- p2= probability of Math.random > 1/j upon iterating item j for all i < j <= n.

Assuming Math.random has normal distrubution, p1 = `1/i`

Therefore: 

p(i) = 1/i * [ i/(i+1) * (i+1)/(i+2) * ... (n-1)/(n) ] = 1/n

Therefore p(i) = 1/n.
'''
def random_value_O1(head):

    # If list is empty
    if head is None:
        return None

    ll_len = 0
    return_val = None

    # Loop through all elements
    travers_node = head
    while travers_node is not None:
        ll_len += 1
        if random.random() < 1/ll_len:
            return_val = travers_node.val

        travers_node = travers_node.next

    return return_val


def return_random_node_value(head):
    # TODO
    val = random_value_On(head)
    print(f"Space ON val: {val}")
    val = random_value_O1(head)
    print(f"Space O1 val: {val}")

    return "Done"


if __name__ == '__main__':
    # head = ListNode(1)
    # head.next = ListNode(5)
    # head.next.next = ListNode(7)
    # head.next.next.next = ListNode(10)

    node_count = int(input("Enter Node Count: ").strip())
    node = SinglyLinkedList()

    for _ in range(node_count):
        node_item = int(input("Enter Element: ").strip())
        node.insert_node(node_item)

    print("Print Linked List")
    node.printForward()

    call_random = int(input("Enter no of times to call Random: "))
    freq_O1 = {}
    freq_ON = {}
    for index in range(call_random):
        val = random_value_On(node.head)
        freq_ON[val] = freq_ON.get(val, 0) + 1

        val = random_value_O1(node.head)
        freq_O1[val] = freq_O1.get(val, 0) + 1

        # random_val = return_random_node_value(node.head)
        # print(f"Random val: {random_val}")

    print(f"freq_ON: {freq_ON}")
    print(f"freq_O1: {freq_O1}")
