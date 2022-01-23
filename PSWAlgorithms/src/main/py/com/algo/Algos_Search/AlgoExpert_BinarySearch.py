'''
Write a function that takes in a sorted array of integers as well as a target integer. The function should use
Binary search algorithm to determine if the target integer is contained in the array and should return its index
if it is, otherwise -1

input -
array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33

Output -
3

'''
# Pushkar 01/22/2022
import unittest

#O(N) space
def binarySearchHelper_rec(start, end, value, array):
    if end < start:
        return -1
    mid = int((end + start)/2)
    if value == array[mid]:
        return mid
    elif value > array[mid]:
        return binarySearchHelper_rec(mid+1, end, value, array)
    else:
        return binarySearchHelper_rec(start, mid-1, value, array)


#O(1) space
def binarySearchHelper_nonrec(start, end, value, array):
    while start <= end:
        mid = int((end + start)/2)
        if value == array[mid]:
            return mid
        elif value > array[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1


def binarySearch(array, target):
    # Write your code here.
    return binarySearchHelper_rec(0, len(array)-1, target, array)
    # return binarySearchHelper_nonrec(0, len(array)-1, target, array)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33), 3)

    def test_case_2(self):
        self.assertEqual(binarySearch([1, 5, 23, 111], 111), 3)


if __name__ == '__main__':
    testprogram = TestProgram()
    testprogram.test_case_1()

