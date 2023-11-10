'''
Given daily prices of a stock, what is the maximum possible profit one can generate by first buying
 one share of that stock on a certain day and then selling that share at least one day later?

Example
{
"arr": [2, 3, 10, 6, 4, 8, 1]
}
Output:

8
For a maximum possible profit of 8, one can buy a share on day 0 at the price of 2 and then sell it
 on day 2 at the price of 10. Note that one isn’t allowed to first sell (“sell short”) for 10 and 
 then buy (“buy to cover”) later for 1, which could have generated a higher profit.

Notes
The function has one argument: An integer array with daily prices.
Return an integer, the maximum possible total profit from buying and then selling a share.
If no profit can be generated, return -1.
Constraints:

2 <= number of elements in the input array <= 105
1 <= any element in the input array <= 109
'''
def find_maximum_profit(arr):
    """
    Args:
    arr(list_int32)
    Returns:
    int32
    """
    # Write your code here.
    # Approach 2 - O(N)
    # in first loop get min so far
    # reverse loop to get max so far
    # profit in the final loop
    # or 
    # check max_profit so far and min_so_far in the same loop. min_So_far will be set after max_profit
    # as it cannot be used for the same day
    
    n = len(arr)
    min_so_far = arr[0]
    profit_so_far = -1  # [0 for i in range(n)]
    for i in range(1, n):
        profit_so_far = max(profit_so_far, arr[i]-min_so_far) 
        min_so_far = min(min_so_far, arr[i])
    
    # if no profit is generated i.e. 0 then return -1
    return profit_so_far if profit_so_far > 0 else -1
    
    # O  (N^2)  10/13 passed - rest failed with timeout
    # ret_val = [-1 for i in range(len(arr))]
    
    # for i, row_val in enumerate(arr):
    #     if i>0 and arr[i] > arr[i-1]:
    #         continue
        
    #     for c in range(i+1, len(arr)):
    #         ret_val[c] = max( arr[c]-row_val, ret_val[c], ret_val[c-1] )
            
    #     # print(f"ret_val:{ret_val}")
    
    # return ret_val[len(arr)-1]