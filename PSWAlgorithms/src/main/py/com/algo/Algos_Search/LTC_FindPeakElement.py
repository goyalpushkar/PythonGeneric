'''
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5
Explanation: Your function can return either index number 1 where the peak element is 2,
             or index number 5 where the peak element is 6.
Follow up: Your solution should be in logarithmic complexity.
'''


class Solution:
    #Linear O(N)
    def findPeakElement(self, nums: List[int]) -> int:
        for elem in range(1, len(nums)):
            # print(elem, nums[elem], nums[elem-1], nums[elem+1])
            if elem == len(nums) - 1:
                if nums[elem] > nums[elem - 1]:
                    return elem
            else:
                if nums[elem] > nums[elem - 1] and nums[elem] > nums[elem + 1]:
                    # print("before return")
                    return elem

        return 0

    #Logarithmic O(logN)
    def findPeakElementLog(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l