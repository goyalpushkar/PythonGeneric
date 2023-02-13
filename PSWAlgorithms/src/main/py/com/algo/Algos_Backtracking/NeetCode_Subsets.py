'''
Given an integer array nums of unique elements, return all possible
subsets  (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.

                                               []
                                []                               [1]
                    []                  [2]             [1]               [1,2]
                []     [3]          [2]   [2,3]     [1]     [1,3]    [1,2]      [1,2,3]
'''
from itertools import chain, combinations

class Solution:
    def subsets(self, nums):

        final_array = []
        # def subset_helper_string(curr_array, level, side):
        #
        #     nonlocal final_array
        #     # print(f"{' '*level*2} {curr_array}\t{level}\t{side}\n"
        #     #       f"{' '*level*2} final_array: {final_array}")
        #     if level == len(nums):
        #         new_array = list(map(int, curr_array.split()))
        #         final_array.append(new_array)
        #         return
        #
        #     # left call
        #     subset_helper_string(curr_array, level+1, 'L')  # curr_array =
        #
        #     # right call
        #     # build_right = curr_array
        #     curr_array = curr_array + ' ' + str(nums[level])
        #     subset_helper_string(curr_array, level+1, 'R')  # curr_array =
        #
        #     return

        def subset_helper(curr_array, level, side):

            nonlocal final_array
            print(f"{' '*level*2} {curr_array}\t{level}\t{side}\n"
                  f"{' '*level*2} final_array: {final_array}")
            if level == len(nums):
                final_array.append(curr_array)
                # if len(curr_array) > 0:
                #     curr_array.pop()
                # curr_array = curr_array[:-1]
                return  # final_array # curr_array[:-1]  #[:-1]   # if side == 'L' else curr_array[:-1]

            # left call
            subset_helper(curr_array, level+1, 'L')  # curr_array =
            # print(f"{('-') * level} {level} Left result:  {final_array}")

            # right call
            # curr_array.append(nums[level])
            subset_helper(curr_array + [nums[level]], level+1, 'R') # + [nums[level]]
            # curr_array.pop()
            # curr_array = curr_array[:-1]
            # print(f"{('-') * level} {level} Left result:  {final_array}")

            return   # final_array # curr_array[:-1]

        # subset_helper_string("", 0, 'L')
        subset_helper([], 0, 'L')
        return final_array

    def subsets_short(self, nums):
        s = list(nums)
        return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))