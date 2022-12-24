'''
Given a string of lowercase characters (a-z), return the length of the longest palindromic subsequence.

Subsequence: a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

For example, the sequence ⟨A, B, D⟩ is a subsequence of ⟨A, B, C, D, E, F⟩ obtained after removal of elements C, E, and F.

https://en.m.wikipedia.org/wiki/Subsequence

Input: {String}
Output: {Integer}
Example
Input:  "vtvvv"
Output: 4

Longest palindromic subsequence here is "vvvv"


Input:  "pwnnb"
Output: 2

Longest palindromic subsequence here is "nn"


Input:  "ttbtctcbt"
Output: 7

Longest palindromic subsequence here is "tbtctbt"
Constraints
Time Complexity:			        O(N^2)
Auxiliary Space Complexity: 		O(N^2)
'''

# 5/30 passed, others failed due to time constraint
# def longest_palindrome(input_string):
#
#     height = len(input_string)
#     final_result = []
#     def check_palindrome(value):
#         start = 0
#         end = len(value)-1
#         while start <= end:
#             if value[start] == value[end]:
#                 start += 1
#                 end -= 1
#             else:
#                 return False
#
#         return True
#
#     def create_all_strings(build, level, result):
#         if level == height:
#             if build not in result:
#                 result.append(build)
#             return result
#
#         # left call
#         result = create_all_strings(build, level+1, result)
#
#         # right call
#         result = create_all_strings(build+input_string[level], level+1, result)
#
#         return result
#
#     final_result = create_all_strings("", 0, final_result)
#
#     print(final_result)
#     max_length = 0
#     max_value = ""
#     for elem in final_result:
#         if check_palindrome(elem):
#             if len(elem) > max_length:
#                 max_length = len(elem)
#                 max_value = elem
#
#     print(f"max_length: {max_length}\tmax_value: {max_value}")
#     return max_length
class Solution:

    def longestPalinSubseq(self, S):



        return 0

if __name__ == '__main__':
    input_string = input("Enter String: ")
    solution = Solution()
    result = solution.longestPalinSubseq(input_string)
    # longest_palindrome(input_string)
    print(f"result: {result}")
