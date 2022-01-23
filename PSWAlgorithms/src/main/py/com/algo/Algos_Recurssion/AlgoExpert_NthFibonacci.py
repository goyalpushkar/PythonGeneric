'''
The fibonacci sequence is defined as follow: first number is 0, second is 1, nth number is sum of (n-1)th and
(n-2)th numbers. Write a function that takes in an integer n and returns the nth Fibonacci number

Important note: The fibonacci sequence is often defined with its First 2 numbers as F0 = 0 and F1 = 1, for the purpose
of this question, the first number is F0; therefore getNthFib(1) is equal to F0, getNthFib(2) is equal to F1, etc.

Input #1
n=2

Output #1
1

Input #2
n=6

Output #2
5 // 0, 1, 1, 2, 3, 5
'''
# Pushkar 01/22/2022

import unittest

def getFib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return getFib(n-1) + getFib(n-2)


def getNthFib(n):
    # Write your code here.
    return getFib(n-1)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(getNthFib(6), 5)
        self.assertEqual(getNthFib(3), 1)
        self.assertEqual(getNthFib(5), 3)

if __name__ == '__main__':
    test_program = TestProgram()
    test_program.test_case_1()