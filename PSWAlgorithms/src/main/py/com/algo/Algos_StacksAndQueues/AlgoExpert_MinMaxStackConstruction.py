'''
Write a Min MAx Class for Min Max Stack. The class should support
    Pushing and Poping values on and off the stack
    Peeking at the value at the top of the stack
    Getting both minimum and maximum values in the stack at any given point in time

All class methods when considered independently should run in constant time and with constant space

Sample Usage
MinMaxStack()
push(5)
getMin() = 5
getMax() = 5
peek() = 5
push(7)
getMin() = 5
getMax() = 7
peek() = 7
push(2)
getMin() = 2
getMax() = 7
peek() = 2
pop() = 2
pop() = 7
getMin() = 5
getMax() = 5
peek() = 5
'''
# Pushkar 01/22/2022
import unittest

class MinMaxStack:
    def __init__(self):
        self.stack_array = []
        self.min_max_array = [{"min": float("inf"), "max": float("-inf")}]
        # self.min_value = float("inf")
        # self.max_value = float("-inf")

    def peek(self):
        # Write your code here.
        return self.stack_array[-1]

    def pop(self):
        # Write your code here.
        self.min_max_array.pop(-1)
        return self.stack_array.pop(-1)

    def push(self, number):
        # Write your code here.
        self.stack_array.append(number)
        # if number < self.min_value:
        #     self.min_value = number
        #
        # if number > self.max_value:
        #     self.max_value = number
        new_min_max = {}
        new_min_max["min"] = min(self.min_max_array[-1]["min"], number)
        new_min_max["max"] = max(self.min_max_array[-1]["max"], number)
        self.min_max_array.append(new_min_max)

    def getMin(self):
        # Write your code here.
        # return self.min_value
        return self.min_max_array[-1]["min"]

    def getMax(self):
        # Write your code here.
        # return self.max_value
        return self.min_max_array[-1]["max"]


def testMinMaxPeek(self, min, max, peek, stack):
    self.assertEqual(stack.getMin(), min)
    self.assertEqual(stack.getMax(), max)
    self.assertEqual(stack.peek(), peek)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        stack = MinMaxStack()
        stack.push(5)
        testMinMaxPeek(self, 5, 5, 5, stack)
        stack.push(7)
        testMinMaxPeek(self, 5, 7, 7, stack)
        stack.push(2)
        testMinMaxPeek(self, 2, 7, 2, stack)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 7)
        testMinMaxPeek(self, 5, 5, 5, stack)

if __name__ == '__main__':
    test_program = TestProgram()
    test_program.test_case_1()
