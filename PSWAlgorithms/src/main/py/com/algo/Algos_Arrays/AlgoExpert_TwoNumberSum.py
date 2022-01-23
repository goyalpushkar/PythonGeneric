'''
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
If any two numbers in the array sum to the target number the function should return them in an array, in any order.
If no two numbers sum up to the target sum, function should return an empty array.

Not that the target sum has to be obtained by summing 2 different integers in the array; you cant add same integer to
itself to get the target sum

You can assume that there will be at most one pair of numbers summing up to the target sum

Input -
Array = [3, 5, -4, 8, 11, 1, -1, 6]
Target Sum = 10

Sample output = [-1, 11]

'''
# 01/22/2022

import unittest

def twoNumberSum(array, targetSum):
    # Write your code here.
    return_array = []

    diff_dict = {}
    for index in range(len(array)):
        diff_dict[array[index]] = index

    for index in range(len(array)):
        required_num = targetSum-array[index]
        if required_num in diff_dict and required_num != array[index]:
            return (array[index], required_num)
            # req_index = diff_dict[required_num]
            # if req_index != index:
            #     return_array.append(array[index])
            #     return_array.append(array[req_index])
            #     return return_array

    # print(return_array)
    return return_array



class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = twoNumberSum([14], 15)
        self.assertTrue(len(output) == 2)
        self.assertTrue(11 in output)
        self.assertTrue(-1 in output)

    def test_case_2(self):
        output = twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10)
        self.assertTrue(len(output) == 2)
        self.assertTrue(11 in output)
        self.assertTrue(-1 in output)


if __name__ == '__main__':
    testing = TestProgram()
    testing.test_case_2()