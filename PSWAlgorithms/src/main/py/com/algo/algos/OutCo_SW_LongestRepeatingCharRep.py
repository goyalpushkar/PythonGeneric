'''
Given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Input:  String, Integer
        s ~ input string
        k ~ Number of operations

Output: Integer

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

N ~ length of input string
k ~ Number of operations

Time Complexity: O(N)
Auxiliary Space Complexity: O(k)
'''

# 29/37 timelimit exceeded
# class Solution(object):
#     def characterReplacement(self, s, k):
#         """
#         :type s: str
#         :type k: int
#         :rtype: int
#         """
#         def initialize(start, k):
#             traverse_idx = start + 1
#             check_char = s[start]
#             cur_len = 1
#             replace_left = k
#
#             return check_char, cur_len, traverse_idx, replace_left
#
#         def catchup_phase(s, max_length, start, cur_len, check_char, replace_left):
#             allowed_limit = start
#
#             # In case replacements are still left then check the characters to replace before start of the cur_char
#             while replace_left > 0:
#                 if allowed_limit > 0:
#                     cur_len += 1
#                     allowed_limit -= 1
#                 replace_left -= 1
#
#             if cur_len > max_length:
#                 max_length = cur_len
#
#             if start < len(s)-1:
#                 start += 1
#             while (start < len(s)-1) and (s[start] == check_char):
#                 start += 1
#
#             print(f"max_length: {max_length}\tstart: {start}\n\n")
#             return max_length, start
#
#         def hunting_phase(s, max_length, start, check_char, cur_len, traverse_idx, replace_left):
#             print(f"Start-- len(s):{len(s)}\tmax_length:{max_length}\tcheck_char:{check_char}\t"
#                   f"start:{start}\ttraverse_idx:{traverse_idx}\n"
#                   f"replace_left: {replace_left}\tcur_len:{cur_len}\n")
#             while traverse_idx < len(s):
#                 print(
#                     f"traversing-- len(s):{len(s)}\tmax_length:{max_length}\tcheck_char:{check_char}\t"
#                     f"start:{start}\ttraverse_idx:{traverse_idx}\n"
#                     f"replace_left: {replace_left}\tcur_len:{cur_len}\ts[traverse_idx]:{s[traverse_idx]}")
#                 if s[traverse_idx] == check_char:
#                     cur_len += 1
#                 else:
#                     if replace_left > 0:
#                         cur_len += 1
#                         replace_left -= 1
#                     else:
#                         max_length, start = catchup_phase(s, max_length, start, cur_len, check_char, replace_left)
#                         print(f"temp check replace_left: {replace_left}\n")
#                         check_char, cur_len, traverse_idx, replace_left = initialize(start, k)
#                         traverse_idx -= 1
#
#                 # if replace_left <= 0 and s[traverse_idx] != check_char:
#                 #     max_length, start = catchup_phase(s, max_length, start, cur_len, check_char)
#                 #     check_char, cur_len, traverse_idx, replace_left = initialize(start, k)
#                 # else:
#                 traverse_idx += 1
#
#             max_length, start = catchup_phase(s, max_length, start, cur_len, check_char, replace_left)
#             return max_length
#
#         max_length = 0
#         start = 0
#         check_char, cur_len, traverse_idx, replace_left = initialize(start, k)
#         # traverse_idx = start + 1
#         # check_char = s[start]
#         # cur_len = 1
#         # replace_left = k
#
#         result = hunting_phase(s, max_length, start, check_char, cur_len, traverse_idx, replace_left)
#         return result

# Accepted but performs unnecessarily binary search for length
# class Solution(object):
#     def characterReplacement(self, s, k):
#         # Check for different length substrings, if they make a valid length subsequence with repeating characters,
#         # using binary search. Take mid (length) substring if it a valid substring then we try new subsequence
#         # on the higher end half of the string else we try new subsequence on the lower end half of the string
#         low = 0
#         high = len(s)+1
#         while low + 1 < high:
#             mid = low + (high-low) // 2
#             # print(f"low:{low}\thigh:{high}\tmid:{mid}")
#             if self.check_valid_subsequence(s, mid, k):
#                 low = mid
#             else:
#                 high = mid
#
#         return low
#
#     def check_valid_subsequence(self, s, mid, k):
#         # take a window of length `substring_length` on the given
#         # string, and move it from left to right. If this window
#         # satisfies the condition of a valid string, then we return
#         # true
#         freq_map = {}
#         start = 0
#         max_frequency = 0
#         for end in range(len(s)):
#             freq_map[s[end]] = freq_map.get(s[end], 0) + 1
#             max_frequency = max(max_frequency, freq_map[s[end]])
#
#             print(f"max_frequency:{max_frequency}\n"
#                   f"freq_map: {freq_map}\n"
#                   f"start: {start}\tend:{end}")
#             # if window size is achieved check if we get a valid subsequence
#             if end-start+1 == mid:
#                 if mid - max_frequency <= k:
#                     # print(f"\n\n")
#                     return True
#                 else:
#                     freq_map[s[start]] = freq_map.get(s[start], 0) - 1
#                     start += 1
#
#         # print(f"\n\n")
#         return False

class Solution(object):
    def characterReplacement(self, s, k):
        start = 0
        max_frequency = 0
        result = 0
        freq_map = {}
        for end in range(len(s)):
            freq_map[s[end]] = freq_map.get(s[end], 0) + 1
            max_frequency = max(max_frequency, freq_map[s[end]])

            if end-start+1 - max_frequency > k:
                freq_map[s[start]] = freq_map.get(s[start], 0) - 1
                start += 1

            result = max(result, end-start+1)

        return result

if __name__ == '__main__':
    no_of_tests = int(input("No of tests: "))
    # PUSHKKRKPDGGGDGG, 1 - 6
    # ABBB, 2 - 4
    # AABABBA, 1 - 4
    # ABAB, 2 - 4
    for i in range(no_of_tests):
        input_string = input("Enter String: ")
        replace_left = int(input("Enter Allowed replacements: "))
        solution = Solution()
        result = solution.characterReplacement(input_string,replace_left)
        # longest_palindrome(input_string)
        print(f"result: {result}")