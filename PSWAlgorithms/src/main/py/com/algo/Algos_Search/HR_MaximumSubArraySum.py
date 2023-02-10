'''
We define the following:

A subarray of array a of length n is a contiguous segment from a[i] through a[j] where 0 <= i < j < n.
The sum of an array is the sum of its elements.
Given an n element array of integers,a, and an integer, m, determine the maximum value of the sum of any of its
subarrays modulo m. For example,
Assume a = [1,2,3] and
m = 2.

The following table lists all subarrays and their moduli:

		   sum	%2
[1]		    1	1
[2]		    2	0
[3]		    3	1
[1,2]		3	1
[2,3]		5	1
[1,2,3]		6	0
The maximum modulus is 1.

Function Description
Complete the maximumSum function in the editor below.
It should return a long integer that represents the maximum value of .

maximumSum has the following parameter(s):
a: an array of long integers, the array to analyze
m: a long integer, the modulo divisor

Returns
- long: the maximum (subarray sum modulo m)

Input Format
The first line contains an integer q, the number of queries to perform.

The next q pairs of lines are as follows:
The first line contains two space-separated integers n and (long)m, the length of a and the modulo divisor.
The second line contains n space-separated long integers a[i].

Constraints
2 <= n <= 10^5
1 <= m <= 10^14
1 <= a[i] <= 10^18
2 <= sum of n over all test cases <= 5 * 10^5

Output Format
For each query, return the maximum value of  as a long integer.

Sample Input
STDIN           Function
1               q=1
5 7             a[] size n = 5, m = 7
3 3 9 9 5
Sample Output
6

Explanation
The subarrays of array a[3,3,9,9,5] and their respective sums modulo m=7 are ranked in order of length and
sum in the following list:
1. [9] => 9 % 7 = 2 and [9] -> 9 % 7 = 2
   [3] => 3 % 7 = 3 and [3] -> 3 % 7 = 3
   [5] => 5 % 7 = 5

2. [9,5] => 14 % 7 = 0
   [9,9] => 18 % 7 = 4
   [3,9] => 12 % 7 = 5
   [3,3] => 6 % 7 = 6

3. [3,9,9] => 21 % 7 = 0
   [3,3,9] => 15 % 7 = 1
   [9,9,5] => 23 % 7 = 2

4. [3,3,9,9] => 24 % 7 = 3
   [3,9,9,5] => 26 % 7 = 5

5. [3,3,9,9,5] => 29 % 7 = 1

The maximum value for subarray sum % 7 for any subarray is 6.
'''


'''
Editorial

1.....j.....i

We define sum[i][j] = (prefix_sum[i] - prefix_sum[j-1]) % m where j <= 1.
Here, sum[i][j] denotes the sum of all the elements from j to i, and prefix_sum[i] denotes the sum of all the elements 
from 1 to i.

The Challenge
We must find the maximum value of sum[i][j] for all i >= j. The solution to this problem is quite similar to solving
 the problem of finding the maximum sum in a subarray.

For a particular index i, we must find the maximum possible value of sum[i][j] for some j.
Let pre[i] = prefix_sum[i] % m. Now, we want to find the value of pre[j] such that j < i and (pre[i]-pre[j])%m
 is maximized.

Note: sum[i][j] = (pre[i]-pre[j])%m
pre[i] is constant for a given i, so only 2 cases are formed.

Case 1: pre[j] <= pre[i]
Find a pre[j] such that pre[j] is minimal (which is 0 when you don't choose any element).

Reason: If pre[i] > pre[j], then the difference is positive and is < m. So we need to find the smallest pre[j]
(the minimum value when no element is chosen is 0).
Remember, we want to maximize (pre[i]-pre[j]) %m at position i.

Case 2: pre[j] > pre[i]
Now the minimum value for pre[i]-pre[j] is -(m-1), and the maximum value is -1.

Reason: pre[i] < pre[j] and m > pre[i], pre[j] >= 0 
Find pre[j], which is strictly > pre[j] .

Reason: The modulo answer will be m + pre[i] - pre[j] where m and pre[i] are constant so we just need to find the 
minimum value of pre[j] which is just greater than pre[i] to maximize our answer.

Note: For finding the j in the second case, we'll need a balanced binary search tree.
We take the maximum of both the cases and thus find the maximum of the (pre[i] - pre[j]) for all j <= i in O(log N) time.

Hack
The correct the syntax for using lower_bound in C++ is set_object.lower_bound(value). 
If you use lower_bound(set_object.begin(), set_object.end(), value), then you'll end up exceeding the time limit.


'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumSum function below.
class Solution:
    # 5/19 passed rest failed in Timeout error using modulo_so_far as set()\
    # All test cases passed after using bisect()
    def maximumSum(self, a, m):
        import heapq
        import bisect
        curr_max = a[0] % m if a[0] > 0 else a[0] + m
        modulo_sofar = []  # bisect # set()
        # heapq.heappush(modulo_sofar, curr_max)
        # modulo_sofar.add(curr_max)
        bisect.insort_left(modulo_sofar, curr_max)
        global_max = curr_max

        for index in range(1, len(a)):
            # current max can be current element modulo only or sum of all prev element modulo
            # curr_max = max(a[index] % m, (curr_max + a[index]) % m)
            curr_max = (curr_max + a[index]) % m
            global_max = max(global_max, curr_max)

            # for elem in modulo_sofar:
            #     # curr_max = max(curr_max, (curr_max - elem + m) % m)
            #     global_max = max(global_max, (curr_max - elem + m) % m)

            index = bisect.bisect_left(modulo_sofar, curr_max)
            if index != len(modulo_sofar):
                global_max = max(global_max, (curr_max - modulo_sofar[index] + m) % m)
            # global_max = max(global_max, (curr_max - heapq.heappop(modulo_sofar) + m) % m)

            # heapq.heappush(modulo_sofar, curr_max)
            # modulo_sofar.add(curr_max)
            bisect.insort_left(modulo_sofar, curr_max)
            print(f"{index}: {a[index]}\n"
                  f"modulo_sofar: {modulo_sofar}\n"
                  f"curr_max: {curr_max}\tglobal_max: {global_max}")

        return global_max


    # only 3/19 passed rest failed wrong answer
    def maximumSum_exp(self, a, m):
        from collections import deque
        max_value = -math.inf
        sum_dict = {}

        def get_modulo(sum_value, m, max_value):
            if sum_value in sum_dict:
                modul = sum_dict[sum_value]
            else:
                modul = sum_value % m
                sum_dict[sum_value] = modul

            max_value = max(max_value, modul)

            return max_value

        arrays = deque()
        arrays.append(a[1:])
        arrays.append(a[:-1])

        while len(arrays) > 0:
            list_val = arrays.popleft()
            sum_val = 0
            for index in range(len(list_val)):
                sum_val += list_val[index]

            max_value = get_modulo(sum_val, m, max_value)

            if len(list_val[1:]) > 0:
                arrays.append(list_val[1:])

            if len(list_val[:-1]) > 0:
                arrays.append(list_val[:-1])

        return max_value


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())

    for q_itr in range(q):
        nm = input().split()
        n = int(nm[0])
        m = int(nm[1])

        a = list(map(int, input().rstrip().split()))
        sol = Solution()
        result = sol.maximumSum(a, m)

        print(str(result) + '\n')
        #fptr.write(str(result) + '\n')

    #fptr.close()