'''
Write a function that takes in an array of positive integers and returns the maximum sum of non-adjacent elements
in the array

If the input array is empty function should return 0

Sample Input -
array = [75, 105, 120, 75, 90, 135]

Output -
330 // 75 + 120 + 135

'''
# Pushkar 02/01/2022
import unittest


def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    last_max = 0
    last_to_last_max = 0
    for index in range(len(array)):
        # print("index: "+str(index), last_max, last_to_last_max)
        if index == 0:
            last_max = array[index]
        else:
            new_last_max = max(last_max, last_to_last_max + array[index])
            last_to_last_max = last_max
            last_max = new_last_max

    return max(last_max, last_to_last_max)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135]), 330)


if __name__ == '__main__':
    testprogram = TestProgram()
    testprogram.test_case_1()
