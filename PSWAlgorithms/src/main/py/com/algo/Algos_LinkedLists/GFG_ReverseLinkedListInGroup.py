'''
Given a linked list of size N. The task is to reverse every k nodes (where k is an input to the function) in the linked list.

Input:
First line of input contains number of testcases T. For each testcase, first line contains length of linked list and next line contains the linked list elements.

Output:
For each testcase, there will be a single line of output which contains the linked list with every k group elements reversed.

User Task:
The task is to complete the function reverse() which should reverse the linked list in group of size k.

Expected Time Complexity : O(n)
Expected Auxilliary Space : O(1)

Example:
Input:
2
8
1 2 2 4 5 6 7 8
4
5
1 2 3 4 5
3

Output:
4 2 2 1 8 7 6 5
3 2 1 5 4

Explanation:
Testcase 1: Since, k = 4. So, we have to reverse everty group of two elements. Modified linked list is as 4, 2, 2, 1, 8, 7, 6, 5.


** For More Input/Output Examples Use 'Expected Output' option **
'''
"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""


from collections import deque  # if Linked List adds in the end
from queue import Queue  # if Linked List adds in the front
def reverse(head, k):
    # Code here
    iterator_node = head
    count = 1

    traversed_stack = Queue(0)  # deque()
    returned_list = LinkedList()
    last_node = None
    # iterator_node_retlist = returned_list.head
    print("Iterator Node Head Data: "+ str(iterator_node.data))
    while iterator_node:
        print("Iterator Node Data: "+ str(iterator_node.data))
        traversed_stack.put(iterator_node)
        iterator_return = LinkedList()
        next_last_node = None
        #curr = None
        # last_node = Node()

        print("count - " + str(count))
        print("queue Size - " + str(traversed_stack.qsize()))
        if count % k == 0 or iterator_node.next is None:  #
            while traversed_stack.qsize() > 0:  # is not empty:
                temp = traversed_stack.get()

                if not iterator_return.head:  #curr:   #iterator_return.head:
                    next_last_node = temp  # Node(temp)
                    if not returned_list.head:
                        last_node = temp #Node(temp)

                #temp.next = curr
                #curr = temp
                iterator_return.push(temp.data)

                #print("queue Size 1 - " + str(traversed_stack.qsize()))

            print("Last Node - " + str(last_node.data))
            print("Next Last Node - " + str(next_last_node.data))
            #print("curr Node - " + str(curr.data))
            print("Iterator Return")
            iterator_return.printList()
            #print("Iterator Return head Data - " + str(iterator_return.head.data))
            if returned_list.head:
                last_node.next = iterator_return.head  #curr  #iterator_return.head
                last_node = next_last_node
            else:
                returned_list.head = iterator_return.head  #curr  #iterator_return.head

            print("Returned List")
            returned_list.printList()
            #print("Return List Head - " + str(returned_list.head.data))

        count += 1
        iterator_node = iterator_node.next

    return returned_list.head

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next

        print()

if __name__ == '__main__':
    t = int(input("No of test cases: "))
    while t > 0:
        llist = LinkedList()
        n = input("Size of Linked List: ")
        values = list(map(int, input("Values: ").split()))
        for i in reversed(values):
            llist.push(i)

        k = int(input("Sub group Size: "))

        llist.printList()
        new_head = LinkedList()
        new_head = reverse(llist.head, k)
        print("Returned Node - " + str(new_head.data))
        llist.head = new_head
        llist.printList()
        t -= 1