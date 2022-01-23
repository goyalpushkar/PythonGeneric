'''
Write a function that takes in an array of positive integers and returns the maximum sum of non-adjacent elements
in the array

If the input array is empty function should return 0

Sample Input -
array = [75, 105, 120, 75, 90, 135]

Output -
330 // 75 + 120 + 135

'''
# Pushkar 01/22/2022
import unittest


def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    pass


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135]), 330)


if __name__ == '__main__':
    testprogram = TestProgram()
    testprogram.test_case_1()
