'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product
of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.


Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra
space for space complexity analysis.)

'''
class Solution:
    # 86.12% 229 ms
    def productExceptSelf(self, nums):
        # O(1) Space
        result = []

        prefix_val = 1
        result.append(prefix_val)
        for index in range(1, len(nums)):
            prefix_val *= nums[index - 1]
            result.append(prefix_val)

        prev_num = 1
        for index in range(len(nums) - 2, -1, -1):
            prev_num *= nums[index + 1]
            result[index] *= prev_num

        return result

    # 21.89% 268 ms
    def productExceptSelf_ONSpace(self, nums):
        # O(N)
        prefix = []
        postfix = []
        result = []

        prefix_val = 1
        prefix.append(prefix_val)
        for index in range(1, len(nums)):
            prefix_val *= nums[index-1]
            prefix.append(prefix_val)

        postfix_val = 1
        postfix.append(postfix_val)
        for index in range(len(nums)-2, -1, -1):
            postfix_val *= nums[index+1]
            postfix.append(postfix_val)

        # print(f"prefix: {prefix}\npostfix:{postfix}")
        n = len(nums)-1
        for index in range(len(nums)):
            result.append(prefix[index] * postfix[n-index])

        return result
