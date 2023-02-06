'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k
(1 <= k < nums.length) such that the resulting array is
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
 For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of
target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
'''
class Solution:

    def search(self, nums, target):
        import math

        def search_helper(low, high):

            # Added Part to remove duplicates, In case duplicates are allowed
            # shif to remove duplicate elements
            while low < high - 1 and nums[low] == nums[low + 1]:
                low += 1

            while low < high - 1 and nums[high - 1] == nums[high - 2]:
                high -= 1
            # Ended Part to remove duplicates, In case duplicates are allowed

            mid = math.floor(high - ((high - low)/2))
            print(f"low: {low}    high: {high}    mid:{mid}")
            if low >= high:
                return -1

            if target == nums[mid]:
                return mid
            else:
                # if target < nums[low] or target > nums[mid]:
                # Logic 2 - Didnt work
                # mid > low and target > mid -> has to be searched in upper half
                # mid > low and target < mid and target > low ->  has to be searched in lower half
                # mid > low and target < mid and target < low ->  has to be searched in upper half

                # mid < low and target > mid and target > low -> has to be searched in lower half
                # mid < low and target > mid and target < low -> has to be searched in upper half
                # mid < low and target < mid -> has to be searched in upper half
                # if (nums[mid] > nums[low] and target > nums[mid]) \
                #         or (nums[mid] < nums[low] and target < nums[mid]) \
                #         or (nums[mid] > nums[low] and target < nums[low])\
                #         or (nums[mid] < nums[low] and target < nums[low]):
                #     return search_helper(mid + 1, high)
                # else:
                #     return search_helper(low, mid)

                # Logic 3
                # if mid > low lower half is sorted
                # else upper half is sorted

                # check if key is between lower and upper boundary of sorted array if yes then key should be in that
                # part else in other half
                if nums[mid] > nums[low]:
                    # Lower half is sorted - low, mid
                    if target >= nums[low] and target < nums[mid]:
                        return search_helper(low, mid)
                    else:
                        return search_helper(mid + 1, high)
                else:
                    # upper half is sorted - mid+1, high
                    if target > nums[mid] and target <= nums[high-1]:
                        return search_helper(mid+1, high)
                    else:
                        return search_helper(low, mid)


        return search_helper(0, len(nums))

    def findMin_2nd(self, nums):
        import math
        low = 0
        high = len(nums)-1
        min_elem = nums[low]

        while (low <= high):  # and (mid <= high and mid >= low)

            # Added Part to remove duplicates, In case duplicates are allowed
            # shif to remove duplicate elements
            while low < high and nums[low] == nums[low + 1]:
                low += 1

            while low < high and nums[high] == nums[high - 1]:
                high -= 1

            mid = math.floor(high - ((high - low) / 2))
            # print(f"low: {low}    high: {high}    mid:{mid}    min_elem: {min_elem}")
            # If firts element is same as mid element
            # if min_elem == nums[mid]:
            min_elem = min(nums[mid], min_elem)
            # else:
            if nums[mid] > nums[high]:
                # lower half is sorted
                # min_elem = min(nums[low], min_elem)
                # search for lower element in upper half
                low = mid+1
            else:
                # upper half is sorted
                # if mid+1 <= high:
                #     min_elem = min(nums[mid+1], min_elem)
                # search for lower element in lower half
                high = mid-1
            # mid = math.floor(high - ((high - low) / 2))

        return min_elem

    def find_min_1st(self, nums):
        import math
        low = 0
        high = len(nums) - 1
        min_elem = nums[low]

        while (low <= high):  # and (mid <= high and mid >= low)

            # Added Part to remove duplicates, In case duplicates are allowed
            # shif to remove duplicate elements
            while low < high and nums[low] == nums[low + 1]:
                low += 1

            while low < high and nums[high] == nums[high - 1]:
                high -= 1

            mid = math.floor(high - ((high - low) / 2))

            print(f"low: {low}    high: {high}    mid:{mid}    min_elem: {min_elem}")
            # If firts element is same as mid element
            # if min_elem == nums[mid]:
            min_elem = min(nums[mid], min_elem)
            # else:
            if nums[mid] > nums[low]:
                # lower half is sorted
                min_elem = min(nums[low], min_elem)
                # search for lower element in upper half
                low = mid + 1
            else:
                # upper half is sorted
                if mid + 1 <= high:
                    min_elem = min(nums[mid + 1], min_elem)
                # search for lower element in lower half
                high = mid - 1
            mid = math.floor(high - ((high - low) / 2))

        return min_elem
'''
0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 
1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1]



'''