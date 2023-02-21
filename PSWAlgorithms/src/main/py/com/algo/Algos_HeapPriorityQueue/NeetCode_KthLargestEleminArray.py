'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.



Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4


Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
'''


class Solution:
    import heapq

    # Custom heap beats 19.52%
    def findKthLargest(self, nums, k):
        self.heapify(nums)

        elem = None
        index = 1
        while index <= k:
            elem = self.extract_max(nums, len(nums)-index+1)
            index += 1

        return elem

    # standard heap beats 52.52%
    def findKthLargest_standard(self, nums, k):
        # heap sort takes O(NLogN) while heapify takes O(N)
        nums = [-1 * x for x in nums]
        heapq.heapify(nums)

        elem = None
        index = 1
        while index <= k:
            elem = -1 * (heapq.heappop(nums))
            index += 1

        return elem

    '''
        left (2n+1) right (2n+2)
        limit_end exclusive
    '''
    def sortify(self, arr):
        index = len(arr) - 1
        while index >= 0:
            arr[index], arr[0] = arr[0], arr[index]
            self.bubble_down(0, arr, index)
            index -= 1

    def extract_max(self, arr, limit_end=None):
        if limit_end is None:
            limit_end = len(arr)

        last_elem = limit_end-1
        arr[last_elem], arr[0] = arr[0], arr[last_elem]
        self.bubble_down(0, arr, last_elem-1)

        # return_elem = arr[last_elem]
        # arr = arr[:-1]

        return arr[last_elem]   # return_elem

    def heapify(self, arr):
        index = len(arr)-1

        while index >= 0:
            self.bubble_down(index, arr)
            index -= 1

    def get_child(self, index, arr, limit_end=None):
        if limit_end is None:
            limit_end = len(arr)

        left = 2 * index + 1
        right = 2 * index + 2

        if left >= limit_end:
            return left
        elif right >= limit_end:
            return left
        elif arr[left] >= arr[right]:
            return left
        else:
            return right

    def bubble_down(self, index, arr, limit_end=None):
        if limit_end is None:
            limit_end = len(arr)

        while index < limit_end:
            eligible_child = self.get_child(index, arr, limit_end)
            if eligible_child < limit_end and arr[eligible_child] > arr[index]:
                arr[eligible_child], arr[index] = arr[index], arr[eligible_child]
            else:
                break

            index = eligible_child
