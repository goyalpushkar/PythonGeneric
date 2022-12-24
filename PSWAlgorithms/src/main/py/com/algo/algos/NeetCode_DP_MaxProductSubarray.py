'''
Given an integer array nums, find a
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.



Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
'''

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        run_sum = None
        max_sum = nums[0]
        run_sum_2 = None

        run_sum_negative = 0

        for index in range(0, len(nums)):

            if run_sum is None:
                run_sum = nums[index]
            else:
                run_sum *= nums[index]

            if run_sum_negative == 1:
                if run_sum_2 is None:
                    run_sum_2 = nums[index]
                else:
                    run_sum_2 *= nums[index]
                # run_sum_negative = 0

            print(f"run_sum_negative: {run_sum_negative}\n"
                  f"run_sum: {run_sum}\trun_sum_2: {run_sum_2}\tmax_sum: {max_sum}")
            if run_sum_2 is None:
                max_sum = max(max_sum, run_sum)
            else:
                max_sum = max(max_sum, run_sum, run_sum_2)

            if run_sum < 0:
                run_sum_negative = 1
            # else:
            #     run_sum_negative = 0

            if run_sum == 0:
                run_sum = None
                run_sum_negative = 0

            if run_sum_2 == 0:
                run_sum_2 = None

        return max_sum


if __name__ == '__main__':
    nums = [1,0,-1,2,3,-5,-2]
        # [-1,0,-2,2]  # Changed code to reset run_sum_negative = 0 at run_sum = 0 and add run_sum_2 == 0
        # [1,0,-1,2,3,-5,-2] # Changed check max_sum ==0 to run_sum == 0
        # [2,-5,-2,-4,3]  # Removed else part of run_sum < 0
        # [0,2]   # Changed logic to start fro m index 0
        # [2,-3,4,5,6,7]
        # [2,3,-1,4]
    solution = Solution()
    result = solution.maxProduct(nums)
    print(f"result: {result}")
