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
class Solution:
    def subsets(self, nums):

        final_array = []
        def subset_helper(curr_array, level, side):

            nonlocal final_array
            print(f"{' '*level*2} {curr_array}\t{level}\t{side}\n"
                  f"{' '*level*2} final_array: {final_array}")
            if level == len(nums):
                final_array.append(curr_array)
                return # final_array # curr_array[:-1]  #[:-1]   # if side == 'L' else curr_array[:-1]

            # left call
            build_left = curr_array
            subset_helper(build_left, level+1, 'L')  # curr_array =
            # print(f"{('-') * level} {level} Left result:  {final_array}")

            # right call
            build_right = curr_array
            build_right.append(nums[level])
            subset_helper(build_right, level+1, 'R')  # curr_array =
            # print(f"{('-') * level} {level} Left result:  {final_array}")

            return # final_array # curr_array[:-1]

        subset_helper([], 0, 'L')
        return final_array