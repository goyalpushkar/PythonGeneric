'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]


Constraints:

-10^9 <= nums1[i], nums2[i] <= 10^9
nums1.length == m + n
nums2.length == n
'''


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        '''
        retArray = []
        array1Index = 0
        array2Index = 0
        # for index in range(min(len(nums1), len(nums2))):
        while array1Index < m and array2Index < n:
            # print(nums1[array1Index], nums2[array2Index])
            if nums1[array1Index] < nums2[array2Index]:
                retArray.append(nums1[array1Index])
                array1Index += 1
            else:
                retArray.append(nums2[array2Index])
                array2Index += 1

            # print(retArray, "\n")

        # print(array1Index, array2Index, m, n)
        while array1Index <= m - 1:
            # print("FirstArray")
            retArray.append(nums1[array1Index])
            array1Index += 1

        # print("1", retArray, "\n")
        # print(array1Index, array2Index, m, n)
        while array2Index <= n - 1:
            # print("SecondArray")
            retArray.append(nums2[array2Index])
            array2Index += 1

        # print("2", retArray, "\n")
        nums1[:] = retArray[:]  # [elem for elem in range(len(retArray))]
        '''

        #2
        '''
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1

        if n > 0:
            nums1[:n] = nums2[:n]
        '''

        #3
        for i in range(len(nums2)):
            nums1[m] = nums2[i]
            m += 1
        nums1.sort()