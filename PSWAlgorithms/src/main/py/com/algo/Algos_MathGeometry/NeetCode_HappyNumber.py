'''
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does
not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:
Input: n = 2
Output: false

Constraints:
1 <= n <= 231 - 1
'''
class Solution:

    # Beats 85.12%  32ms
    def isHappy(self, n):
        while n != 1:
            n = sum(int(i)**2 for i in str(n))

            if n == 4:
                return False

        return True

    # Beats 40.42%  40ms
    # Same algorithm without a function finishes in 26 ms
    def isHappy_1st(self, n):
        sq_num = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
        track_sums = set()

        def get_sum(n_cop):
            sum = 0
            while n_cop > 0:
                bit = n_cop % 10
                n_cop = n_cop // 10
                sum += sq_num[bit]

            return sum

        next_val = n
        while (True):
            next_val = get_sum(next_val)
            print(f"next_val: {next_val}")
            if (next_val in track_sums):  # or (len(str(next_val)) == 1 and next_val != 1)
                return False

            if len(str(next_val)) == 1 and next_val == 1:
                return True

            track_sums.add(next_val)
