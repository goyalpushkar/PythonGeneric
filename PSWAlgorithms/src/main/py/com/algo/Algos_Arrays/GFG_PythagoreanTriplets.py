'''
Given an array of integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a2 + b2 = c2.

Input:
The first line contains T, denoting the number of testcases. Then follows description of testcases. Each case begins with a single positive integer N denoting the size of array. The second line contains the N space separated positive integers denoting the elements of array A.

Output:
For each testcase, print "Yes" or  "No" whether it is Pythagorean Triplet or not (without quotes).

Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= A[i] <= 1000

Example:
Input:
1
5
3 2 4 6 5

Output:
Yes

Explanation:
Testcase 1: a=3, b=4, and c=5 forms a pythagorean triplet, so we print "Yes"
'''
import math
from collections import Set
def check_pythagorean(arr):
    dict_arr = set()
    for elem in arr:
        dict_arr.add(int(math.pow(elem, 2)))

    sorted_arr = sorted(arr)

    for index in range(len(sorted_arr)):
        for next_index in range(index + 1, len(sorted_arr)):
            hypotenuse = int(math.pow(sorted_arr[index], 2)) + int(math.pow(sorted_arr[next_index], 2))
            if hypotenuse in dict_arr:
                return "Yes"

    return "No"


if __name__ == '__main__':
    test_cases = int(input())
    for index in range(test_cases):
        arr_size = int(input())
        arr = list(map(int, input().rstrip().split()))

        return_elem = check_pythagorean(arr)

        print(return_elem)