'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element
in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


Constraints:
1 <= nums.length <= 104
0 <= nums[i] <= 105
'''
from collections import deque
class Solution:
    def canJump(self, nums):
        # Set goal as last index
        # start from last index and check index+value at index can reach the goal
        # if yes set goal as this new index
        # in the end if goal is 0 then return True else False

        goal = len(nums)-1
        for index in range(len(nums)-2, -1, -1):
            if index + nums[index] >= goal:
                goal = index

        return True if goal == 0 else False

        # start = 0
        # index = start
        # prev_start = -1
        # while index < len(nums):
        #     prev_start = index
        #     index += nums[index]
        #     print(prev_start, start, index)
        #     if index >= len(nums) - 1:
        #         return True
        #
        #     if index == prev_start:
        #         index = nums[start] - 1
        #         start = index
        #         if start <= 0:
        #             break
        #
        # return False

    # Time limit exceeded 71/170
    def canJump_TLE(self, nums):
        adjacent_nodes = {}
        for index in range(len(nums)):
            # adjacent_nodes[index] = [i+index for i in range(nums[index],0,-1) if i+index<=len(nums)-1]
            adjacent_nodes[index] = [i + 1 + index for i in range(nums[index]) if i + index <= len(nums) - 1]

        # perform breadth first search
        queue_list = deque()
        queue_list.append(0)

        while len(queue_list) > 0:
            elem = queue_list.popleft()
            if elem == len(nums) - 1:
                return True

            for child in adjacent_nodes[elem]:
                queue_list.append(child)

        return False


