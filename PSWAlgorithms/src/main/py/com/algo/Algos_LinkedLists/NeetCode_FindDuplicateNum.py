'''
Given an array of integers nums containing n + 1 integers where each integer is in the
range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Constraints:
1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.

Follow up:
How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
https://leetcode.com/problems/find-the-duplicate-number/description/

'''
class Solution:
    def findDuplicate(self, nums):
        # hare and tortiose approach
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break

        return slow

        # Sort approach - This is modifying the array and also not constant extra space
        # beats 21.72%
        nums = sorted(nums)
        for i in range(0, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]

        # Dict approach - This is not constant extra space
        # beats 67.12%
        num_dict = {}
        for i in range(0, len(nums)):
            if nums[i] in num_dict:
                return nums[i]
            else:
                num_dict[nums[i]] = 1

        # failed with test case - [2,2,2,2,2]
        n = len(nums) - 1
        act_sum = int((n * (n + 1)) / 2)
        num_sum = sum(nums)
        diff = num_sum - act_sum

        return diff