'''
There is a fence with n posts and there are k different colors. Find the number of ways the fence can be painted, where:

Every post must be painted with exactly one color.
Three or more consecutive posts are not painted with the same color.
The answer can be very large. So, return answer modulo 109 + 7.

Example One
{
"n": 3,
"k": 2
}
Output:

6
{Color1-Color1-Color2, Color1-Color2-Color1, Color1-Color2-Color2, Color2-Color1-Color1, Color2-Color1-Color2, Color2-Color2-Color1}. These are the possible ways of coloring the fence.

Example Two
{
"n": 3,
"k": 7
}
Output:

336
Notes
Constraints:

1 <= n <= 105
1 <= k <= 109

{
"n": 3,
"k": 7
} -- 336
'''
def number_of_ways(n, k):
    """
    Args:
    n(int32)
    k(int32)
    Returns:
    int32
    """
    # Write your code here.
    if n == 0:
        return 0
    
    # if there is only one pole then it can be painted k ways
    if n == 1:
        return k
    
    # DP for 3 rows - same, different and total
    # columns as number of poles
    dp = [ [0 for _ in range(n)] for _ in range(3)]
    modulo = pow(10, 9) + 7
    
    for c in range(1, n):
        # print(f"c: {c}, dp: {dp}")
        if c == 1: # 2 poles
            # 0 index is same color
            dp[0][c] = k
            # 1 index is different color
            dp[1][c] = k * (k-1)
        
        else: # all other poles
            # if both has to be same color then take different ways for last pole
            dp[0][c] = dp[1][c-1]
            # if both has to be different color then take total ways for last pole * k-1 for this pole
            dp[1][c] = dp[2][c-1] * (k-1)
            
        # 2 index is total colors
        dp[2][c] = (dp[0][c] + dp[1][c]) % modulo
        
    return dp[2][n-1]