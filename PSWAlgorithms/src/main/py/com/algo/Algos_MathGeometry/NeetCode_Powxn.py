'''
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).


Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Constraints:
-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
-104 <= xn <= 104
'''
class Solution:
    '''
            x = 2, n  = 10
            = 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2
            = 2^5 * 2^5
            = 2 * 2^2 * 2^2 * 2 * 2^2 * 2^2
            =


    '''
    # Beats 22.25% 38 ms
    def myPow(self, x, n):

        if n == 0: return 1
        if x == 0: return 0
        def helper(n):

            if n == 0:
                return 1

            res = helper(n//2)
            print(f"n: {n} res: {res}")

            if n % 2 == 0:
                return res * res
            else:
                return res * res * x

            # res = res * res
            # return x * res if n % 2 else res

        final_val = helper(abs(n))

        return final_val if n > 0 else 1/final_val

    def myPow_1liner(self, x: float, n: int) -> float:
        return x ** n

    # 291/305 passed Time Limit exceeded
    def myPow_TLE(self, x, n):
        if n == 0:
            return 1

        if n > 0:
            ret_val = x
            for i in range(n - 1):
                ret_val *= x
        else:
            n = -n
            ret_val = 1 / x
            for i in range(n - 1):
                ret_val *= 1 / x

        return ret_val

        # fails for negative values of x
        y = n * math.log2(x)
        return math.pow(2, y)