'''
Given two numbers represented by two linked lists of size N and M. The task is to return a sum list. The sum list is a linked list representation of the addition of two input numbers.

Input:
The first line of input contains the number of test cases T. For each test case, the first line of input contains the length of the first linked list and next line contains N elements of the linked list. Again, the next line contains M, and the following line contains M elements of the linked list.

Output:
Output the resultant linked list.

User Task:
The task is to complete the function addTwoLists() which has node reference of both the linked lists and returns the head of the new list.

Expected Time Complexity: O(N) + O(M)
Expected Auxiliary Space: O(N) + O(M)

Constraints:
1 <= T <= 100
1 <= N, M <= 5000

Example:
Input:
2
2
4 5
3
3 4 5
2
6 3
1
7
Output:
3 9 0
7 0

Explanation:
Testcase 1: For the given two linked list (4 5) and (3 4 5), after adding the two linked list resultant linked list will be (3 9 0).
Testcase 2: For the given two linked list (6 3) and (7), after adding the two linked list resultant linked list will be (7 0).
'''
''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
from _collections import deque
def addLists(first, second):
    # code here
    # return head of sum list
    ll_deque1 = deque()
    while first is not None:
        ll_deque1.append(first.data)
        first = first.next

    ll_deque2 = deque()
    while second is not None:
        ll_deque2.append(second.data)
        second = second.next

    carry_over = 0
    result_arr = []
    while len(ll_deque1) > 0 or len(ll_deque2) > 0:
        if len(ll_deque1) == 0:
            ll1_elem = 0
        else:
            ll1_elem = ll_deque1.pop()

        if len(ll_deque2) == 0:
            ll2_elem = 0
        else:
            ll2_elem = ll_deque2.pop()

        ll3_elem = ll1_elem + ll2_elem + carry_over
        if ll3_elem // 10 == 0:
            carry_over = 0
        else:
            carry_over = 1

        result_arr.append(ll3_elem%10)

    if carry_over > 0:
        result_arr.append(carry_over)

    print(result_arr)
    ll3 = LinkedList()
    for index in range(len(result_arr)-1,-1,-1):
        ll3.insert(result_arr[index])

    return ll3.head

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(n):
    while n:
        print(n.data, end = " ")
        n = n.next

    print()

if __name__ == '__main__':
    test_cases = int(input("No of test cases: "))
    for index in range(test_cases):
        n = int(input("List1 Length: "))
        arr1 = ( int(x) for x in input("List1: ").split())
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)

        n = int(input("List2 Length: "))
        arr1 = ( int(x) for x in input("List2: ").split())
        LL2 = LinkedList()
        for i in arr1:
            LL2.insert(i)

        res = addLists(LL1.head, LL2.head)
        printList(res)