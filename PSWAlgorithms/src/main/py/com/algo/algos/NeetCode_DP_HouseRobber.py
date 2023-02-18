'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
 the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and
  it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money
you can rob tonight without alerting the police.


Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

index -         0   1   2   3   4
values -        2   7   9   3   1
Running Sum -   2   7   11  11  12
Run indexes -   0   1   0,2 0,2 0,2,4


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400+
'''

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob1, rob2 = 0,0
        for num in nums:
            max_value = max(num+rob1, rob2)
            rob1 = rob2
            rob2 = max_value

        return rob2


    def rob_lengthy(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        running_sum = [nums[0]]
        running_indexes = [[0]]
        # running_sum.append(nums[0])
        # running_indexes.append([0])
        for index in range(1, len(nums)):
            # print(f"index: {index} - {running_sum[index-2]}+{nums[index]}\t"
            #       f"{running_sum[index-1]}\n"
            #       f"{running_indexes[index-2]}\t{running_indexes[index-1]}\n"
            #       )
            if index == 1:
                second_last_val = 0
            else:
                second_last_val = running_sum[index - 2]
            running_sum.append(max((second_last_val + nums[index]), running_sum[index-1]))
            if second_last_val + nums[index] > running_sum[index - 1]:
                if index - 2 < 0:
                    new_value = []
                else:
                    new_value = running_indexes[index - 2]
                new_value.append(index)
            else:
                new_value = running_indexes[index-1]
            running_indexes.append(new_value)

        print(f"Max Sum: {running_sum[len(nums)-1]} \n"
              f"Max Indexes: {running_indexes[len(nums)-1]}")
        return running_sum[len(nums)-1]

if __name__ == '__main__':

    nums = [1,2,3,1]
    solution = Solution()
    result = solution.rob(nums)
    print(f"result: {result}")

