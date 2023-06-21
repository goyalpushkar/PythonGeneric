'''
Given a rope, cut it into parts maximizing the product of their lengths.

Example
{
"n": 4
}
Output:
4
Length of the rope is 4.
All ways it can be cut into parts: 1+3, 1+1+2, 1+1+1+1, 2+2, 2+1+1.
Among these, 2+2 cut makes for the greatest product: 2*2=4.

Notes
Return an integer which equals to the maximum possible product of the given rope’s parts.
Constraints:
2 <= length of the rope <= 94
You have to cut at least once.
Length of the rope, lengths of all parts are all positive integers.
'''

def max_product_from_cut_pieces(n):
    """
    Args:
     n(int32)
    Returns:
     int64
    """
    # Write your code here.
    memo = {}
    def maxproduct_rec(n, loop_till):
        print("n: ", n, memo)
        if n in memo:
            return memo[n]

        if n < 0:
            return 0

        if n == 0:
            return 1

        max_product = 0
        # curr_product = 1
        for i in range(1, loop_till):
            ret_value = maxproduct_rec(n - i, n + 1)
            ret_value *= i

            # print("ret_value: ", i, ret_value)
            max_product = max(max_product, ret_value)

        memo[n] = max_product

        return memo[n]

    def maxproduct_tab(n):
        if n == 0:
            return 0

        tab = [1 for rope in range(n+1)]
        for rope in range(2, n+1):
            for cut in range(1, rope):
                tab[rope] = max(tab[rope], tab[rope-cut]*cut, (rope-cut)*cut)

        return tab[-1]

    return maxproduct_rec(n, n)



