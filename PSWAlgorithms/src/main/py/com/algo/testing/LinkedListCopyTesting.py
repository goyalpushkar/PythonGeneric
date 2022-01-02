
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def push(self, data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
            self.last = temp
        else:
            temp.next = self.head
            self.head = temp

    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next

    def make_loop(self, pos):
        temp = self.head
        for index in range(1,pos):
            temp = temp.next

        self.last.next = temp

    def is_loop(self):

        if self.head is None:
            return False

        temp = self.head.next
        prev = self.head

        while temp != prev:
            if temp is None or temp.next is None:
                return False
            temp = temp.next.next
            prev = prev.next

        return True

if __name__ == '__main__':
    newLinkedList = LinkedList()
    newLinkedList.push(4)
    newLinkedList.push(3)
    newLinkedList.push(2)
    newLinkedList.push(1)
    newLinkedList.printlist()
    print()

    newLinkedList.make_loop(2)

    #newLinkedList.printlist()
    #print()
    dict = {}

    temp = newLinkedList.head
    while temp:
        print(temp.data)
        dict[temp] = 'Visited'

        if temp.next in dict:
            print("Already Visited. Loop is here")
            temp.next = None
            break
        else:
            print("Not Visited")
        temp = temp.next

    newLinkedList.printlist()