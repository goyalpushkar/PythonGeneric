'''
Given a base a and an exponent b. Your task is to find ab. The value could be large enough. So, calculate ab % 1000000007.

Example
{
"a": 2,
"b": 10
}
Output:

1024
Notes
Constraints:

0 <= a <= 104
0 <= b <= 109
a and b together won't be 0
'''

class Solution():
    def calculate_power(a, b):
        """
        Args:
         a(int64)
         b(int64)
        Returns:
         int32
        """
        # Write your code here.
        if a == 0:
            return 0

        if a == 1:
            return 1

        if b == 0:
            return 1

            # return ( a * calculate_power(a, b-1) ) % 1000000007
            # RecursionError: maximum recursion depth exceeded in comparison
        '''
        {
            "a": 10000,
            "b": 10000000
            }
            '''
        temp = calculate_power(a, b // 2)
        # print(a, b, temp)
        if b % 2 == 0:
            return (temp % 1000000007 * temp % 1000000007)
        else:
            return (a % 1000000007 * temp % 1000000007 * temp % 1000000007)