'''
You are given head of a Singly Linked List whose nodes are in sorted order with respect to their values.
Write a function that returns a modified version of the linked list that doesnt contain any nodes with duplicate
values. The linked list should be modified in place (i.e.you shouldnt create a brand new list0 and the modified
Linked list should still have its nodes sorted with respect to their values.
Each linked list node has an integer value as well as a next node pointing to the next node in the list or
to None/ null if its the tail of the list

Input -
linkedlist = 1 -> 1 -> 3 -> 4 -> 4 -> 4 -> 5 -> 6 -> 6

Output -
1 -> 3 -> 4 -> 5 -> 6


'''
# Pushkar 01/22/2022
import unittest

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(1)
def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    traverse_node = linkedList
    prev_node = None

    while traverse_node != None:
        current_value = traverse_node.value
        if prev_node is not None and current_value == prev_node.value:
            prev_node.next = traverse_node.next
        else:
            prev_node = traverse_node

        traverse_node = traverse_node.next

    return linkedList


# O(d) space where d is distinct values in the list
def removeDuplicatesFromLinkedList_d(linkedList):
    # Write your code here.
    list_dict = {}
    traverse_node = linkedList
    prev_node = None

    while traverse_node != None:
        current_value = traverse_node.value
        # print(current_value)
        if current_value in list_dict:
            prev_node.next = traverse_node.next
        else:
            list_dict[current_value] = 1
            prev_node = traverse_node

        traverse_node = traverse_node.next

    return linkedList


class LinkedList(LinkedList):
    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = LinkedList(1).addMany([1, 3, 4, 4, 4, 5, 6, 6])
        expected = LinkedList(1).addMany([3, 4, 5, 6])
        actual = removeDuplicatesFromLinkedList(test)
        self.assertEqual(actual.getNodesInArray(), expected.getNodesInArray())


if __name__ == '__main__':
    test_program = TestProgram()
    test_program.test_case_1()
