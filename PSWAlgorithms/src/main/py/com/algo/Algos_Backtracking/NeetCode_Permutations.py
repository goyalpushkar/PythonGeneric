'''
Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]


Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.

'''
from collections import deque
from itertools import permutations

class Solution:
    # Beats 99.54% 28ms
    def permute(self, nums):
        # DFS
        final_return = []
        result = []

        def helper(new_list):
            # nonlocal result
            # nonlocal final_return
            # print(f"result: {result}\tnew_list:{new_list}")
            if not new_list:  # len(new_list) == 0:
                # print("append")
                final_return.append(result.copy())  # [:]
                return

            for i in range(len(nums)):
                result.append(nums[i])
                # print(f"result_inif: {result}")
                val = nums[i]
                del nums[i]
                helper(nums)
                nums.insert(i, val)
                result.pop()

        helper(nums)
        return final_return

    # BFS
    # Beats 61.98% 42ms
    def permute_bfs(self, nums):
        queu = deque()
        queu.append(([], nums))

        final_return = []
        while queu:
            curr_elem = queu.popleft()

            if len(curr_elem[1]) == 0:
                final_return.append(curr_elem[0])

            for elem in curr_elem[1]:
                queu.append((curr_elem[0] + [elem], list(set(curr_elem[1]) - set([elem]))))

        return final_return

    def permute_oneliner(self, nums):
        return permutations(nums)