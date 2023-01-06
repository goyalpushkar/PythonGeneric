'''
Implement a Linked List data structure with addToTail and removeFromHead methods.
Then use that Linked List data structure to implement a Queue data structure with enqueue and dequeue methods.
'''

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertNode(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node

    def removeNode(self, value):
        traverse_node = self.head

        # if list is empty
        if traverse_node is None:
            return None

        # if node to be removed is head
        if traverse_node.value == value:
            self.head = None
            self.tail = None

        # Loop through nodes and check if next value is the node to be deleted then remove the node
        while traverse_node.next is not None:
            if traverse_node.next.value == value:
                if traverse_node.next == self.tail:
                    self.tail = traverse_node

                traverse_node.next = traverse_node.next.next
                break

            traverse_node = traverse_node.next

    def printList(self):
        traverse_node = self.head

        # Loop through nodes and check if next value is the node to be deleted then remove the node
        while traverse_node is not None:
            print(traverse_node.value)
            traverse_node = traverse_node.next

    def addToTail(self, value):
        # if list is empty
        if self.tail is None:
            self.insertNode(value)
        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node

    def removeFromHead(self):
        traverse_node = self.head

        # if list is empty
        if traverse_node is None:
            return None

        # self.head, self.head.next = self.head.next, None
        temp = self.head.next
        return_val = self.head
        self.head.next = None
        self.head = temp

        # in case head is None, set tail to None
        if self.head is None:
            self.tail = None

        return return_val.value

class Queue:
    def __init__(self):
        self.ll = Linked_List()
        # self.head = self.ll.head

    def enqueue(self, value):
        self.ll.addToTail(value)

    def dequeue(self):
        return self.ll.removeFromHead()

    def printQueue(self):
        self.ll.printList()


if __name__ == '__main__':
    data_type = input("Enter Q for Queue and LL for Linked List: ")

    que = None
    ll = None
    if data_type.upper() == 'Q':
        que = Queue()
    elif data_type.upper() == 'LL':
        ll = Linked_List()
    else:
        print("Please enter valid data type")
        exit()

    no_of_op = int(input("Enter number of operations: "))
    for index in range(no_of_op):
        op = input("Enter Operation Name I for Insert, R for Remove, and P for Print: ")
        if op.upper() == 'I':
            val = int(input("Enter value to add: "))
            if que is not None:
                que.enqueue(val)
            elif ll is not None:
                ll.addToTail(val)
        elif op.upper() == 'R':
            if que is not None:
                print(que.dequeue())
            elif ll is not None:
                print(ll.removeFromHead())
        elif op.upper() == 'P':
            if que is not None:
                que.printQueue()
            elif ll is not None:
                ll.printList()
        else:
            print("Please enter valid operation")
