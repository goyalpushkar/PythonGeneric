'''
Given two integers n and k, find all the possible unique combinations of k numbers in range 1 to n.

Example One
{
"n": 5,
"k": 2
}

Output:
[
[1, 2],
[1, 3],
[1, 4],
[1, 5],
[2, 3],
[2, 4],
[2, 5],
[3, 4],
[3, 5],
[4, 5]
]

Example Two
{
"n": 6,
"k": 6
}

Output:
[
[1, 2, 3, 4, 5, 6]
]
Notes
The answer can be returned in any order.

Constraints:
1 <= n <= 20
1 <= k <= n
'''

class Solution:
    def find_combinations(n, k):
        """
        Args:
         n(int32)
         k(int32)
        Returns:
         list_list_int32
        """
        # Write your code here.
        '''
                                                n, k
                      (not selected)  n-1, k                 n-1, k-1 (selected)
              n-2, k                        n-2, k-1     n-2, k-1          n-2, k-2 

                                                     4,2 
                                       3,2                                    3,1 
                            2,2               2,1                       2,1                   2,0 
                     1,2         1,1         1,1        1,0        1,1       1,0         1,0        1,-1(X)
                 0,2    0,1    0,1  0,0   0,1   0,0   0,0  0,-1  0,1  0,0 0,0   0,-1  0,0   0,-1  


               [0,2], [0,1], [0,0], [1,2], [1,1], [1,0], [2,2], [2,1], [2,0], [3,2], [3,1], [4,2]
            '''
        final_sol = []

        # both option1 and 2 are using same memory for output
        # as in option 1 while appending to final_sol we are creating a copy
        # while processing option is better
        # option 1 - Space is N*k as same array is passed in each loop
        def helper(arr, sol, level):
            # print(arr, sol, level, final_sol)
            if level == k:
                final_sol.append(sol.copy())
                # final_sol = final_sol + sol
                return

            else:
                for elem in range(len(arr)):
                    sol.append(arr[elem])
                    helper(arr[elem + 1:], sol, level + 1)
                    # sol = sol[:-1]
                    sol.pop()

        # option 2 - Space is N^2*k as new array is getting created in each loop
        def helper_2(arr, sol, level):
            print(arr, sol, level, final_sol)
            if level == k:
                final_sol.append(sol)
                return
            else:
                for elem in range(len(arr)):
                    # sol.append(arr[elem])
                    helper(arr[elem + 1:], sol + [arr[elem]], level + 1)
                    # sol = sol[:-1]
                    # sol.pop()

                # return
                # sol = sol[:-1]

            # return

        arr = [i + 1 for i in range(n)]
        helper(arr, [], 0)
        return final_sol
