'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that
is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in
 the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in
the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in
the range since it does not appear in nums.

Constraints:
n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.


Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
'''
class Solution:

    # beats 91.61% 128 ms
    #     # Time - O(N) Space - O(1)
    def missingNumber_math(self, nums):
        n = len(nums)
        sum_elem = sum(nums)
        req_sum = (n * (n + 1)) / 2
        missing_elem = req_sum - sum_elem

        return missing_elem

    # beats 63.31%% 138 ms
    # Time - O(N) Space - O(1)
    def missingNumber(self, nums):
        res = len(nums)
        for i in range(len(nums)):
            res += (i - nums[i])

        return res

    # beats 76.57% 134 ms
    # Time - O(2N) Space - O(N)
    def missingNumber_1st(self, nums):
        n = len(nums)
        arr = [0] * (n+1)
        for elem in nums:
            arr[elem] = 1

        missing_elem = None
        for i in range(n+1):
            if arr[i] == 0:
                missing_elem = i
                break

        return missing_elem
