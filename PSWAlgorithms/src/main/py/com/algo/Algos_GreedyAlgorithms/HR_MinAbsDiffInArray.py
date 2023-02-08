'''
The absolute difference is the positive difference between two values a and b, is written |a-b| or |b-a|
 and they are equal. If a=3 and b=2, |3-2| or|2-3| = 1. Given an array of integers,
 find the minimum absolute difference between any two elements in the array.

Example. arr = [-2,2,4]

There are 3 pairs of numbers: [-2,2], [2,4] and .[-2,4] The absolute differences for these pairs are |-2-2| =4,
|2-4| = 2 and |-2-4|=6. The minimum absolute difference is 2.

Function Description

Complete the minimumAbsoluteDifference function in the editor below. It should return an integer that represents
the minimum absolute difference between any pair of elements.

minimumAbsoluteDifference has the following parameter(s):
int arr[n]: an array of integers

Returns
int: the minimum absolute difference found

Input Format
The first line contains a single integer n, the size of arr.
The second line contains n space-separated integers, arr[i].

Constraints
2 <= n <= 10^5
-10^9 <= arr[i] <= 10^9

Sample Input 0
3
3 -7 0
Sample Output 0
3


Explanation 0

The first line of input is the number of array elements. The array, arr [3,-7,0] There are three pairs to test:
 |3--7| =10, |-7-0|=7, and |3-0|=3.

Remember that the order of values in the subtraction does not influence the result.
The smallest of these absolute differences is 3.

Sample Input 1
10
-59 -36 -13 1 -53 -92 -2 -96 -54 75

Sample Output 1
1

Explanation 1
The smallest absolute difference is |-54- -53| = 1.

Sample Input 2
5
1 -3 71 68 17

Sample Output 2
3

Explanation 2
The minimum absolute difference is |71-68| = 3

'''
import math

class Solution:
    def minimumAbsoluteDifference(self, arr):
        # Write your code here
        sorted_arr = sorted(arr)
        min_diff = math.inf
        for elem in range(len(arr) - 1):
            min_diff = min(min_diff, abs(sorted_arr[elem] - sorted_arr[elem + 1]))

        return min_diff
