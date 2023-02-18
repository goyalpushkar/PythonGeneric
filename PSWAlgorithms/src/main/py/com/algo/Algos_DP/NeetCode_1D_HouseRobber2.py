'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two
adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can
rob tonight without alerting the police.

Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [1,2,3]
Output: 3

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000

'''
class Solution:
    def rob(self, nums):

        def helper(numbers):
            rob1, rob2 = 0, 0
            # index1, index2 = [], []
            for i in range(len(numbers)):
                max_value = max(numbers[i] + rob1, rob2)
                rob1 = rob2
                rob2 = max_value

                # if nums[i] + rob1 > rob2:
                #     index1.append(i)
                #
                # index2, index1 = index1, index2

            return rob2

        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))

    def rob_wrong(self, nums):
        if len(nums) == 0:
            return 0

        # last_val = (nums[0], 0)
        max_sum = (nums[0], 0)
        max_indexes = [[0]]
        reduce_zero = False

        if len(nums) > 1:
            max_sum = (nums[0], max(nums[0], nums[1]))
            if nums[0] > nums[1]:
                max_indexes.append([0])
            else:
                max_indexes.append(([1]))
            # last_val = (nums[0], nums[1])

        for i in range(2, len(nums)):

            if i % 2 == 0:
                new_val = nums[i] + max_sum[0]
            else:
                new_val = nums[i] + max_sum[1]

            # if it is the last house then subtract the value for first one
            if i == len(nums) - 1:
                if i % 2 == 0:
                    if 0 in max_indexes[0]:
                        new_val = new_val - nums[0]
                        reduce_zero = True
                else:
                    if 0 in max_indexes[1]:
                        new_val = new_val - nums[0]
                        reduce_zero = True

            if i % 2 == 0:
                max_sum = (max(max_sum[1], new_val), max_sum[1])
                if max_sum[1] > new_val:
                    max_indexes = (max_indexes[1], max_indexes[1])
                else:
                    max_indexes = (max_indexes[0] + [i], max_indexes[1]) # - [0] if reduce_zero else [], max_indexes[1])
            else:
                max_sum = (max_sum[0], max(max_sum[0], new_val))
                if max_sum[0] > new_val:
                    max_indexes = (max_indexes[0], max_indexes[0])
                else:
                    max_indexes = (max_indexes[0], max_indexes[1] + [i]) # - [0] if reduce_zero else [])

            print(f"i: {i} max_sum: {max_sum} \tnew_val: {new_val}\n"
                  f"max_sum: {max_sum} \tmax_indexes: {max_indexes}")

        return max(max_sum)