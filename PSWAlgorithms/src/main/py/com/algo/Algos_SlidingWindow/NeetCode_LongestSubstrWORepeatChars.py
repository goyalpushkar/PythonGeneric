'''
Given a string s, find the length of the longest substring without
repeating characters.

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

    # Beats 27.36%
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0

        left, right = 0, 1
        duplicate_char = 0
        curr_length = 1
        max_length = 1

        key_val = {}
        key_val[s[left]] = 1

        while left <= len(s) - 1 and right <= len(s) - 1:
            # print(f"left: {s[left]} right: {s[right]} curr_length: {curr_length}")
            if key_val.get(s[right], 0) > 0:
                duplicate_char += 1
            else:
                curr_length += 1

            key_val[s[right]] = key_val.get(s[right], 0) + 1
            max_length = max(max_length, curr_length)

            while duplicate_char > 0:
                if s[left] == s[right]:
                    duplicate_char -= 1
                    curr_length += 1

                key_val[s[left]] -= 1
                curr_length -= 1

                left += 1

            right += 1

        return max_length

    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(set(s)) == len(s):
            return len(s)

        substring = ''
        maxLen = 1

        for i in s:
            if i not in substring:
                substring = substring + i
                maxLen = max(maxLen, len(substring))

            else:
                substring = substring.split(i)[1] + i

        return maxLen

