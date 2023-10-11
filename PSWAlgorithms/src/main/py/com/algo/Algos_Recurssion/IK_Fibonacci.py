'''
Given a number n, find the n-th Fibonacci Number.

Example
{
"n": 2
}
Output:
1
2nd Fibonacci Number is the sum of the 0th and 1st Fibonacci Number = 0 + 1 = 1.

Notes
In mathematics, the Fibonacci numbers, commonly denoted Fn, form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
F(0) = 0, F(1) = 1 and F(n) = F(n − 1) + F(n − 2) for n > 1.

Constraints:
0 <= n <= 46
'''
def find_fibonacci(n):
    """
    Args:
     n(int32)
    Returns:
     int32
    """
    # Write your code here.
    memo = {}

    def fibo_help(n):
        if n in memo:
            return memo[n]

        if n == 0:
            return 0
        if n == 1:
            return 1

        val = fibo_help(n - 1) + fibo_help(n - 2)
        memo[n] = val

        return memo[n]

    return fibo_help(n)