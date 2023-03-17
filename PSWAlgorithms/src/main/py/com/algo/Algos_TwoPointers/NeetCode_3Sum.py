'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k,
and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


Constraints:
3 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''
class Solution:
    '''
        -1,0,1,2,-1,-4
        -4,-1,-1,0,1,2

    '''
    # Beats 77.79% 1278 ms
    def threeSum(self, nums):
        result_set = []
        nums = sorted(nums)

        for i, a in enumerate(nums):

            # if combinations are found for the same num
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, len(nums)-1
            while left < right:
                target_sum = a + nums[left] + nums[right]
                if target_sum > 0:
                    right -= 1
                elif target_sum < 0:
                    left += 1
                else:
                    result_set.append([a, nums[left], nums[right]])
                    left += 1

                    # to skip duplicate values in result set move left
                    while nums[left] == nums[left-1] and left < right:
                        left += 1

        return result_set

    # 39.24% 1905 ms
    def threeSum(self, nums):
        dict_3rd_num = {}
        for i in range(len(nums)):
            dict_3rd_num[nums[i]] = dict_3rd_num.get(nums[i], []) + [i]

        nums = list(set(nums))
        result_set = {}
        if len(dict_3rd_num.get(0, [])) > 2:
            result_set["0,0,0"] = [0,0,0]

        for first in range(len(nums)):
            for second in range(first + 1, len(nums)):
                target = 0 - (nums[first] + nums[second])
                # print(f"target: {target} for {first} {second} existence: {dict_3rd_num.get(target, -1)}")

                if target != nums[first] and target != nums[second]:
                    if target in dict_3rd_num:
                        final_data = sorted([nums[first], nums[second], target])
                        key = ",".join(str(i) for i in final_data)
                        # result_set.add(final_data)
                        result_set[key] = final_data
                else:
                    if target in dict_3rd_num and len(dict_3rd_num[target]) > 1:
                        final_data = sorted([nums[first], nums[second], target])
                        key = ",".join(str(i) for i in final_data)
                        # result_set.add(final_data)
                        result_set[key] = final_data

        return list(result_set.values())  # list(result_set)

    # 310/312 passed
    def threeSum(self, nums):
        dict_3rd_num = {nums[i]:nums[i].append(i) for i in range(len(nums))}
        # print(dict_3rd_num)

        result_set = {} # set()
        for first in range(len(nums)):
            for second in range(first+1, len(nums)):
                target = 0 - (nums[first] + nums[second])
                # print(f"target: {target} for {first} {second} existence: {dict_3rd_num.get(target, -1)}")
                if target in dict_3rd_num and dict_3rd_num[target] != first and dict_3rd_num[target] != second:
                    final_data = sorted([nums[first], nums[second], target])
                    key = ",".join(str(i) for i in final_data)
                    # result_set.add(final_data)
                    result_set[key] = final_data

        return list(result_set.values()) # list(result_set)