'''
Given an array of numbers, rearrange them in-place so that even numbers appear before odd ones.

Example
{
"numbers": [1, 2, 3, 4]
}
Output:

[4, 2, 3, 1]
The order within the group of even numbers does not matter; same with odd numbers. So the following are also correct outputs: [4, 2, 1, 3], [2, 4, 1, 3], [2, 4, 3, 1].

Notes
It is important to practice solving this problem by rearranging numbers in-place.
There is no need to preserve the original order within the even and within the odd numbers.
We look for a solution of the linear time complexity that uses constant auxiliary space.
Constraints:

1 <= length of the array <= 105
1 <= element of the array <= 109
'''

class Solution:

    def segregate_evens_and_odds(self, numbers):
        """
        Args:
         numbers(list_int32)
        Returns:
         list_int32
        """
        # Write your code here.
        left = 0
        right = len(numbers) - 1
        while left < right:
            # If right index is odd then move right pointer
            while right >= 0 and numbers[right] % 2 > 0:
                right -= 1

            # If left index is even then move left pointer
            while left <= len(numbers) - 1 and numbers[left] % 2 == 0:
                left += 1

                # if left is odd and right is even then swap and move pointers
            if left < right and numbers[left] % 2 > 0 and numbers[right] % 2 == 0:
                numbers[left], numbers[right] = numbers[right], numbers[left]
                right -= 1
                left += 1

        return numbers