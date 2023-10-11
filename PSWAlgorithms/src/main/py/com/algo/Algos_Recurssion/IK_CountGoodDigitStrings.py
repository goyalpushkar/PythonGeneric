'''
A digit string is a string consisting of digits 0 through 9 which may contain leading zeros.
A digit string is called good if the digits at even indices are even and the digits at odd indices are prime
 (2, 3, 5, or 7).

Calculate the total number of good digit strings of a given length n.

Example
{
"n": 1
}
Output:

5
The good digit strings of length 1 are "0", "2", "4", "6" and "8".

Notes
Consider the examples: 0762 is a good digit string because the digits (0 and 6) at even indices are even and
the digits (7 and 2) at odd indices are prime. However, "67298" is not good because 9 is at an odd index but is
not prime.
Return the answer modulo 10^9 + 7.
The modulo operation returns the remainder or signed remainder of a division after one number is divided by another.
Constraints:

1 <= given length <= 10^12
'''


def count_good_digit_strings(n):
    """
    Args:
     n(int64)
    Returns:
     int32
    """
    # Write your code here.
    # Way 1 - Timeout in 4 out of 9
    if n <= 0:
        return 0

    result = 1
    for index in range(n):
        if index % 2 == 0:
            # even indices should be 0,2,4,6,8
            result *= 5
        else:
            # odd indices should be prime 2,3,5,7
            result *= 4

    return (result % (pow(10, 9) + 7))

    # Way 2 recursive using mem cache
    mem_cache = {}

    def helper(n):
        # print(n)
        if n in mem_cache:
            return mem_cache[n]

        if n == 1:
            mem_cache[n] = 5

        elif n == 2:
            mem_cache[n] = 5 * 4

        else:
            # if last num of digits are even
            if (n - 1) % 2 == 0:
                # print(f"even n: {n}")
                mem_cache[n] = (helper(n - 1) * 5 % (pow(10, 9) + 7))

            else:
                # print(f"odd n: {n}")
                mem_cache[n] = (helper(n - 1) * 4 % (pow(10, 9) + 7))

    # print(n, mem_cache)
    return mem_cache[n]
