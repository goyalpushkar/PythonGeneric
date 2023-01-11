'''
Given an array of positive integers and a target value, return true if there is a subarray of consecutive elements that
sum up to this target value.

Input: Array of integers, target value
Output: Boolean

Input: [6,12,1,7,5,2,3], 14      	=>	Output: true (7+5+2)
Input: [8,3,7,9,10,1,13], 50		=>	Output: false

Time Complexity: O(N)
Auxiliary Space Complexity: O(1)
'''

class Solution:

    def consecutive_subarray_sum(self, arr, s):
        sum = 0 # arr[0]
        start = 0

        for elem in range(len(arr)):
            print(f"start_elem: {arr[start]}, curr_elem: {arr[elem]}\t"
                  f"start: {start}, elem: {elem}, sum: {sum}")
            sum += arr[elem]

            while sum > s and start < elem:
                sum -= arr[start]
                start += 1

            if sum == s:
                return True, start+1, elem+1
        # # If sum is still greater thn required s then keep decreasing start
        # while sum > s and start < len(arr):
        #     sum -= arr[start]
        #     start += 1
        #
        #     if sum == s:
        #         return True, start+1, elem+1

        return False, -1


if __name__ == '__main__':
    no_of_tests = int(input("No of tests: "))
    # Input: [6, 12, 1, 7, 5, 2, 3], 14 = > Output: true(7 + 5 + 2)
    # Input: [8, 3, 7, 9, 10, 1, 13], 50 = > Output: false
    for i in range(no_of_tests):
        input_array = []
        arr_elem = input("Enter Array Elements as a list: ")
        input_array = list(map(int, arr_elem.split()))

        # no_array_elem = int(input("Enter No of elements in Array: "))
        # for elem in range(no_array_elem):
        #     arr_elem = int(input("Enter Array Element: "))
        #     input_array.append(arr_elem)

        value = int(input("Enter Required Value: "))
        solution = Solution()
        result = solution.consecutive_subarray_sum(input_array, value)
        # longest_palindrome(input_string)
        print(f"result: {result}")