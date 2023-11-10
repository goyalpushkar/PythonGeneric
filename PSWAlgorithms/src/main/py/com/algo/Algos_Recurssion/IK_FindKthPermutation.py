'''
Given two numbers n and k, find the k-th lexicographically smallest permutation of the sequence [1, 2, 3, ..., n].

Example One
{
"n": 3,
"k": 5
}
Output:

"312"
Explanation: There are a total of 3! = 6 permutations of the sequence 123 as: 123, 132, 213, 231, 312, 321

The fifth permutation is 312.

Example Two
{
"n": 4,
"k": 2
}
Output:

"1243"
Notes
In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of 
all positive integers less than or equal to n. Read more about factorials from here.

Constraints:

1 <= n <= 9
1 <= k <= n!
'''
def get_kth_permutation(n, k):
    """
    Args:
    n(int32)
    k(int32)
    Returns:
    str
    """
    # Write your code here.
    final_comb = []
    
    def rec(slate, arr):
        nonlocal final_comb
        
        if len(slate) == n:
            final_comb.append("".join(str(elm) for elm in slate))
            return
        
        for idx, elem in enumerate(arr):
            slate.append(elem)
            rec(slate, arr[:idx]+arr[idx+1:])
            slate.pop()
            
    
    arr = [i+1 for i in range(n)]
    rec([], arr)
    
    
    return final_comb[k-1]


# IK 
def get_kth_permutation(n, k):
    """
    Args:
    n(int32)
    k(int32)
    Returns:
    str
    """
    # Write your code here.
    res = ""
    arr = list(range(1, n+1))
    from math import factorial
    k -= 1
    
    for i in range(1, n+1) :
        
        idx = k//factorial(n-i)
        res += str(arr[idx])
        k -= factorial(n-i)*idx
        arr.pop(idx)

    return res