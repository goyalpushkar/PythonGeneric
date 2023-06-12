'''
Given an integer array arr of size n, find all magic triplets in it.

Magic triplet is a group of three numbers whose sum is zero.

Note that magic triplets may or may not be made of consecutive numbers in arr.

Example
{
"arr": [10, 3, -4, 1, -6, 9]
}
Output:

["10,-4,-6", "3,-4,1"]
Notes
Function must return an array of strings. Each string (if any) in the array must represent a unique magic
triplet and strictly follow this format: "1,2,-3" (no whitespace, one comma between numbers).
Order of the strings in the array is insignificant. Order of the integers in any string is also insignificant.
For example, if ["1,2,-3", "1,-1,0"] is a correct answer, then ["0,1,-1", "1,-3,2"] is also a correct answer.
Triplets that only differ by order of numbers are considered duplicates, and duplicates must not be returned.
For example, if "1,2,-3" is a part of an answer, then "1,-3,2", "-3,2,1" or any permutation of the same numbers may not appear in the same answer (though any one of them may appear instead of "1,2,-3").
Constraints:

1 <= n <= 2000
-1000 <= any element of arr <= 1000
arr may contain duplicate numbers
arr is not necessarily sorted

'''
class Solution:

    def find_zero_sum(arr):
        """
        Args:
         arr(list_int32)
        Returns:
         list_str
        """
        # Write your code here.
        final_result = set()
        for num1_idx in range(len(arr)):
            target = -arr[num1_idx]
            num2_dict = set()

            for num2_idx in range(len(arr)):
                # Avoid using same number as the second number
                if num1_idx != num2_idx:
                    num3 = target - arr[num2_idx]

                    # Check if new number (3rd number) is already in dict
                    if num3 in num2_dict:
                        nums = sorted([-target, arr[num2_idx], num3])
                        nums = ",".join(str(num) for num in nums)
                        final_result.add(nums)

                    # if 3rd num is not in dict then add second number in
                    # dict to be used for 3rd num verification
                    num2_dict.add(arr[num2_idx])

        return list(final_result)
