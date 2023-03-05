'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers
such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2]
where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array
[index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

Constraints:
2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
'''
class Solution:
    # beats 45.78%
    def twoSum(self, numbers, target):
        # take 2 pointers start and end and get their sum if sum is greater than target
        # then reduce right pointer else increase left pointer
        left, right = 0, len(numbers)-1
        while left <= right:
            act_target = numbers[left] + numbers[right]
            if act_target > target:
                right -= 1
            elif act_target < target:
                left += 1
            else:
                return [left+1, right+1]

        return [-1, -1]

    # beats 9.15%
    def twoSum_binarySearch(self, numbers, target):
        # loop through all elements and second_elem = target - elem[index]
        # Perform binary search for the second_elem in rest of the array
        def binary_search(target_elem, low, high):
            while low <= high:
                mid = int(high - (high - low) / 2)

                if numbers[mid] == target_elem:
                    return mid
                elif numbers[mid] > target_elem:
                    high = mid - 1
                else:
                    low = mid + 1

            return -1

        for index in range(len(numbers)):
            second_elem = target - numbers[index]
            second_index = binary_search(second_elem, index + 1, len(numbers) - 1)

            if second_index != -1:
                return [index + 1, second_index + 1]