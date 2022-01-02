'''
Queues: A Tale of
Two Stacks
A queue is an abstract data type that maintains the order in which elements were added to it, allowing the oldest elements to be removed from the front and new elements to be added to the rear. This is called a Firs t -I n -Firs t -Out (FIFO) data structure because the first element added to the queue (i.e., the one that has been waiting the longest) is always the first one to be removed.
A basic queue has the following operations:
Enqueue: add a new element to the end of the queue.
Dequeue: remove the element from the front of the queue and return it.
In this challenge, you must first implement a queue using two stacks. Then process query is one of the following types:
1. 1 x : Enqueue element into the end of the queue.
2. 2 : Dequeue the element at the front of the queue.
3. 3 : Print the element at the front of the queue.
For example, a series of queries might be as follows:
Function Description
queries, where each
Complete the put, pop, and peek methods in the editor below. They must perform the actions as described above.
Input Format
The first line contains a single integer, , the number of queries.
Each of the next lines contains a single query in the form described in the problem statement above. All queries start with an integer denoting the query , but only query is followed by an additional space- separated value, , denoting the value to be enqueued.
Constraints
It is guaranteed that a valid answer always exists for each query of types and .
Output Format
For each query of type , return the value of the element at the front of the fifo queue on a new line.
Sample Input


10
1 42 2
1 14 3
1 28 3
1 60 1 78 2
2
Sample Output
14 14
Explanation
'''


class MyQueuePerformanceBad(object):
    def __init__(self):
        self.actuallist = []
        self.templist = []

    def insert_elem(self, value):
        """

        :param value:
        """
        for elem in range(len(self.templist)):
            self.actuallist.append(self.templist.pop())

        self.templist.append(value)

        for elem in range(len(self.actuallist)):
            self.templist.append(self.actuallist.pop())


    def peek(self):
        """

        :return:
        """
        return self.templist[len(self.templist)-1]

    def pop(self):
        """

        :return:
        """
        return self.templist.pop()

    def put(self, value):
        """

        :param value:
        """
        self.insert_elem(value)

class MyQueue(object):
    def __init__(self):
        self.actuallist = []
        self.templist = []

    def move_elements(self):
        """

        :param value:
        """
        for elem in range(len(self.actuallist)):
            self.templist.append(self.actuallist.pop())

    def peek(self):
        """

        :return:
        """
        #if len(self.templist) == 0:
        if not self.templist:
            self.move_elements()

        return self.templist[len(self.templist)-1]

    def pop(self):
        """

        :return:
        """
        #if len(self.templist) == 0:
        if not self.templist:
            self.move_elements()

        return self.templist.pop()

    def put(self, value):
        """

        :param value:
        """
        self.actuallist.append(value)

queue = MyQueue()
t = int(input("No of queries: "))
for line in range(t):
    values = map(int, input().split())
    values = list(values)

    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())

    print(queue.actuallist)
    print(queue.templist)