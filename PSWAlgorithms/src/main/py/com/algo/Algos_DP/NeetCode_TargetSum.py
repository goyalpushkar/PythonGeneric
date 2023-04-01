'''
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums
and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build
the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.


Example 1:
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Example 2:
Input: nums = [1], target = 1
Output: 1


Constraints:
1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
'''
class Solution:
    # Beats 25.55% 391 ms
    def findTargetSumWays(self, nums, target):
        memo = {}

        def dfs(index, val):
            key = (index, val)

            if key in memo:
                return memo[key]

            if index == len(nums) - 1 and val == target:
                return 1

            if index == len(nums) - 1 and val != target:
                return 0

            # left branch +  +  # righ branch -1
            branch_sum = dfs(index + 1, val + nums[index]) + \
                         dfs(index + 1, val - nums[index])

            memo[key] = branch_sum
            return branch_sum

        return dfs(-1, 0)

    '''
    Tabulation way
    At any given point in time, you can make 2 choices:
    - '+' a certain integer
    - '-' a certain integer

    - Maybe we can have a list of numbers that can be formed so far.
        - So in ex1.
            - it1: [1, -1]
            - it2: [2, 0, 0, -2] -> [2:1, 0:2, -2:1]
            - it3: [3:1, 1:1, 1:2, -1:2, -1:1, -3:1] -> [3:1, 1:3, -1:3, -3:1]
            - it4: [4, 2, 2:2, 0:2, 0:2, -2:2, -2, -4] -> [4:1, 2:3, 0:4, -2:3, -4:1]
    
        - In each iteration, get a dictionary of numbers that can be reached 
            by all the numbers so far, and the number of ways to reach that number.
    
    '''
    def findTargetSumWays(self, nums, target):
        d = {0: 1}

        for n in nums:
            d_cur = {}
            for k, v in d.items():
                d_cur[k + n] = v + d_cur.get(k + n, 0)
                d_cur[k - n] = v + d_cur.get(k - n, 0)
            d = d_cur

        return d.get(target, 0)