'''
You are given an integer array height of length n. There are n vertical lines drawn
such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
n == height.length
2 <= n <= 105
0 <= height[i] <= 104
'''
import math

class Solution:
    # beats 39.53%
    def maxArea(self, height):
        # Start from left and right pointer
        # if height[left] < height[right] move left pointer else move right pointer
        left, right = 0, len(height) - 1
        max_area = -math.inf

        while left < right:
            length = right - left
            width = min(height[left], height[right])
            max_area = max(max_area, length * width)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

    # 49/61 - Time limit exceeded
    def maxArea_n2(self, height):
        # O (N^2)
        index = 0
        max_area = -math.inf
        while index < len(height) - 1:
            second_index = len(height) - 1

            while second_index > index:
                length = second_index - index
                width = min(height[index], height[second_index])
                area = length * width
                max_area = max(max_area, area)

                second_index -= 1

            index += 1

        return max_area