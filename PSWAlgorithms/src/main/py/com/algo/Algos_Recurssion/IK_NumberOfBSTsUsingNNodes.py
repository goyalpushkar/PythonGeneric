'''
Write a function that returns the number of distinct binary search trees that can be constructed with n nodes. For the purpose of this exercise, do solve the problem using recursion first even if you see some non-recursive approaches.

Example One
{
"n": 1
}
Output:

1
Example Two
{
"n": 2
}
Output:

2
Suppose the values are 1 and 2, then the two trees that are possible are

   (2)            (1)
  /       and       \
(1)                  (2)
Example Three
{
"n": 3
}
Output:

5
Suppose the values are 1, 2, 3 then the possible trees are

       (3)
      /
    (2)
   /
(1)

   (3)
  /
(1)
   \
   (2)

(1)
   \
    (2)
      \
       (3)

(1)
   \
    (3)
   /
(2)

   (2)
  /   \
(1)    (3)
Notes
Constraints:

1 <= n <= 16
'''
def how_many_bsts(n):
    """
    Args:
    n(int32)
    Returns:
    int64
    """
    # Write your code here.
    mem = {}
    def helper(no_nodes):
        if no_nodes in mem:
            return mem[no_nodes]
        
        if no_nodes == 0 or no_nodes == 1:
            return 1
        
        if no_nodes == 2:
            return 2
            
        total_sum = 0
        for i in range(1, no_nodes+1):
            total_sum += ( helper(i-1) * helper(no_nodes-i) )
    
        mem[no_nodes] = total_sum
        return total_sum
        
    return helper(n)