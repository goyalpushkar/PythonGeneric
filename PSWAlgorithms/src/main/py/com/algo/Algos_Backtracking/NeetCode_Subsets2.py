'''
Given an integer array nums that may contain duplicates, return all possible
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10

'''
from collections import deque


class Solution:
    from collections import deque

    # Consider test case if there are duplicate elements and are not sorted, so better to sort new_array
    # e.g. 4,4,4,1,4
    # While checking new_array existence make sure to insert curr_array to deque

    def subsetsWithDup_bfs(self, nums):
        final_array = []

        final_array.append([])
        if len(nums) == 0:
            return final_array

        level_queue = deque()
        level_queue.append([])
        level_queue.append([nums[0]])

        final_array.append([nums[0]])
        level = 1
        while level != len(nums):
            for _ in range(len(level_queue)):
                curr_array = level_queue.popleft()
                new_array = sorted(curr_array + [nums[level]])
                if new_array in level_queue:
                    level_queue.append(curr_array)
                    continue

                final_array.append(new_array)

                level_queue.append(curr_array)
                level_queue.append(new_array)

            print(f"{level} final_array: {final_array}\n"
                  f"level_queue: {level_queue}")
            level += 1

        return final_array

    def subsetsWithDup(self, nums):

        final_array = set()
        def subset_helper(curr_array, level, side):
            nonlocal final_array
            # print(f"{' ' * level * 2} {curr_array}\t{level}\t{side}\n"
            #       f"{' ' * level * 2} final_array: {final_array}")
            if level == len(nums):
                # if len(curr_array) == 1:
                #     final_array.add("("+str(curr_array[0])+")")
                # else:
                final_array.add(tuple(curr_array))
                # if len(curr_array) > 0:
                #     curr_array.pop()
                # curr_array = curr_array[:-1]
                return

            # left call
            subset_helper(curr_array, level + 1, 'L')  # curr_array =
            # print(f"{('-') * level} {level} Left result:  {final_array}")

            # right call
            subset_helper(curr_array + [nums[level]], level + 1, 'R')  # + [nums[level]]
            # print(f"{('-') * level} {level} Left result:  {final_array}")

            return

        subset_helper([], 0, 'L')
        return final_array
