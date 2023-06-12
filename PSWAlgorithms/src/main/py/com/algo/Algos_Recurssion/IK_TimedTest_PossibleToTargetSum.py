'''
Given a set of integers and a target value k, find whether there is a non-empty subset that sums up to k.

Example One
{
"arr": [2, 4, 8],
"k": 6
}
Output:

1
Because 2 + 4 = 6.

Example Two
{
"arr": [2, 4, 6],
"k": 5
}
Output:

0
Because no subset of numbers from the input sums up to 5.

Notes
Constraints:

1 <= size of the input array <= 18
-1012 <= elements of the array, k <= 1012

{
        "arr": [8, -11],
        "k": 8
        }

        {
        "arr": [-3, 3, -3, -2, -3, -4, -1, 1, -3, -2, -4, 0, 4, 3, -2, 3, -2, -1],
        "k": 31
        }
        sorted = [-4, -4, -3, -3, -3, -3, -2, -2, -2, -2, -1, -1, 0, 1, 3, 3, 3, 4]
'''

class Solution:
    def check_if_sum_possible(arr, k):
        """
        Args:
         arr(list_int64)
         k(int64)
        Returns:
         bool
        """
        # Write your code here.
        if not arr:
            return False

        def helper(curr_sum, curr_arr):
            # print(curr_sum, curr_arr)
            if curr_sum == 0 and len(curr_arr) != len(arr):
                return True

            if not curr_arr:
                return False

            for index in range(len(curr_arr)):
                if helper(curr_sum - curr_arr[index], curr_arr[index + 1:]):
                    return True

            return False

        arr = sorted(arr)
        if helper(k, arr):
            return True

        return False

    def check_if_sum_possible_TLE(self, arr, k):
        # if len(arr) == 0:
        #     return False
        #
        #
        # def helper(curr_arr, curr_sum):
        #     if curr_sum == k:
        #         return True
        #     else:
        #         for index in range(len(curr_arr)):
        #             curr_sum += curr_arr[index]
        #             if curr_sum <= k:
        #                 res = helper(curr_arr[:index] + curr_arr[index + 1:], curr_sum)
        #                 if res:
        #                     return True
        #
        #         return False
        #
        #
        # arr = sorted(arr)
        # return helper(arr, 0)

        # earlier Failed for test case if k=0
        # then Failed for test case k=0, arr=[0]
        if len(arr) == 0 or (k == 0 and len(arr) == 0):
            return False

            # result = set()

        def helper(i, curr_sum):

            print("index: ", i, "sum: ", curr_sum)
            if curr_sum == k and i != 0:
                # result.add(1)
                return True

            if i >= len(arr):
                return False
            else:
                for index in range(i, len(arr)):
                    curr_sum += arr[index]
                    if curr_sum <= k:
                        res = helper(i + 1, curr_sum)
                        if res:
                            return True
                    curr_sum -= arr[index]

            return False

        arr = sorted(arr)

        return helper(0, 0)


'''
arr.sort()
    count=0

    def fill_blanks(i,sum_slate,size):
        nonlocal count
        if sum_slate==k:
            if size>0:
                count+=1
                return

        for j in range(i,len(arr)):
            if j>i and arr[j]==arr[j-1]:
                continue
            fill_blanks(j+1, sum_slate+arr[j], size+1)

    fill_blanks(0,0,0)
    if count==0:
        return False
    return True

'''