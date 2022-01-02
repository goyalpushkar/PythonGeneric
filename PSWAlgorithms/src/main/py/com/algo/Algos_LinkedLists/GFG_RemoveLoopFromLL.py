'''
You are given a linked list of N nodes. The task is to remove the loop from the linked list, if present.

Input:
First line of input contains number of testcases T. T testcases follow. For each testcase, first line of input contains length N of the linked list and next line contains N data of the linked list. The third line contains the position of the node(from head) to which the last node will get connected. If it is 0 then there is no loop.

Output:
For each testcase, in a new line, 1 will be printed if loop is removed and the list still has all N nodes connected to it, else 0 will be printed.

User Task:
Your task is to complete the function removeLoop(). The only argument of the function is head pointer of the linked list. Do not print anything. Simply remove the loop in the list (if present) without disconnecting any nodes from the list.

Expected time complexity : O(n)

Expected auxiliary space : O(1)

Constraints:
1 <= T <= 102
1 <= N <= 104

Example:
Input:
2
3
1 3 4
2
4
1 8 3 4
0
Output:
1
1

Explanation:
Testcase 1: In the first test case N = 3.The linked list with nodes N = 3 is given. Here, x = 2 which means last node is connected with xth node of linked list. Therefore, there exists a loop.
Testcase 2: N = 4 and x = 0, which means lastNode->next = NULL, thus the Linked list does not contains any loop.
'''
'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''


def removeLoop(head):
    # code here
    # remove the loop without losing any nodes
    visited_dict = {}
    temp = head

    while temp is not None:
        print(temp.data)
        visited_dict[temp] = 'Visited'

        if temp.next in visited_dict:
            # print("Already Visited. Loop is here")
            temp.next = None
            break
        # else:
        # print("Not Visited")
        temp = temp.next

class Node:
    def __init__(self, val):
        self.next = None
        self.data = val

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

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

    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next

    def loopHere(self, pos):
        if pos == 0:
            return

        temp = self.head
        for index in range(1,pos):
            temp = temp.next

        self.tail.next = temp

    def length(self):
        walk = self.head
        ret = 0
        while walk:
            ret += 1
            walk = walk.next

        return ret

if __name__ == '__main__':
    t = int(input("No of test cases: "))
    for te in range(t):
        n = int(input("Length of List: "))
        arr = tuple(int(x) for x in input().split())
        pos = int(input("Position to be looped: "))

        ll = LinkedList()
        for i in arr:
            ll.add(i)

        ll.printlist()
        print()
        ll.loopHere(pos)

        removeLoop(ll.head)

        if ll.is_loop() or ll.length() != n:
            print(0)
            continue
        else:
            print(1)
