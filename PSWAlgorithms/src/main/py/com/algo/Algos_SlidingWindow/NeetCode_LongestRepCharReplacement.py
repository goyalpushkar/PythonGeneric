'''
Given a string s, find the length of the longest
substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''
class Solution:
    def characterReplacement(self, k, s):
        dict_found = {}
        l = 0
        r = 0

        max_frequency = 0
        max_letter = ""
        curr_len = 0
        return_result = 0

        while l <= r and r < len(s):
            if s[r] in dict_found:
                dict_found[s[r]] += 1
            else:
                dict_found[s[r]] = 1

            # if max_frequency <= dict_found[s[r]]:
            #     max_letter = s[r]
            max_frequency = max(max_frequency, dict_found[s[r]])

            curr_len += 1
            r += 1

            if k >= curr_len - max_frequency:
                return_result = curr_len
            else:
                # catchup_phase
                # while l < len(s) - 1 and s[l] == s[l + 1]:
                dict_found[s[l]] -= 1
                l += 1
                curr_len -= 1
                    # if max_letter == s[l]:
                    #     max_frequency -= 1
                # l += 1
                # r = l + 1

            print(f"l: {l} r: {r} \t curr_len: {curr_len} \t max_frequency: {max_frequency} \t max_letter: {max_letter}\n"
                  f"return_result: {return_result}\n"
                  f"dict_found: {dict_found}")

        return return_result
