'''
Given a string s, return the longest
palindromic

substring
 in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

'''
import math
class Solution:
    def check_palindrome(self, s, start, end):
        while start <= end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False

        return True

    def checkpalindrome(self, s, start, end, max_length, result):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            if end-start+1 > max_length:
                max_length = end-start+1
                result = s[start:end+1]

            start -= 1
            end += 1

        return max_length, result


    def longestPalindrome(self, s):
        # another way to check palindrome is to expand outside starting from the middle
        # babad  - start from b -> b, start from a -> bab,
        # start from b -> aba, babad, start from a -> bad, start from d -> ad
        # Edge case is when string is even length
        # cbbd -
        max_length = 0
        result = ""
        for i in range(len(s)):
            # odd length
            start, end = i, i
            max_length, result = self.checkpalindrome(s, start, end, max_length, result)
            print(f"max_length: {max_length} result: {result}")

            # even length
            start, end = i, i+1
            max_length, result = self.checkpalindrome(s, start, end, max_length, result)
            print(f"max_length: {max_length} result: {result}")

        return result


    # 80/141 passed rest Time limit Exceeded
    def longest_palindrome_rec(self, s):

        cache = {}
        max_val = -math.inf
        start_val = 0
        end_val = 0

        def helper(start, end):
            nonlocal max_val
            nonlocal start_val
            nonlocal end_val

            print(f"start: {start} end: {end}")
            key = s[start:end+1]
            if start >= len(s) or end < 0 or start > end:
                return

            if key in cache:
                return

            if self.check_palindrome(s, start, end):
                # print(f"max_val: {max_val} start_val: {start_val} end_val: {end_val}")
                if end-start+1 > max_val:
                    start_val = start
                    end_val = end
                max_val = max(max_val, end-start+1)
                cache[key] = max_val
                # max_val = max_length
                print(f"max_val: {max_val} start_val: {start_val} end_val: {end_val}\n"
                      f"start: {start} end: {end}\n\n")

            helper(start+1, end)
            helper(start, end-1)

            cache[key] = max_val

            return

        if self.check_palindrome(s, 0, len(s)-1):
            max_length = len(s)
            max_val = max_length
            start_val = 0
            end_val = len(s) - 1

        helper(0, len(s)-1)
        print(f"max_val: {max_val} start_val: {start_val} end_val: {end_val}")

        return s[start_val: end_val+1]

    # Passes all test cases
    def longest_palindrome(self, s):

        max_length = 0
        start_index = -1
        end_index = -1

        if len(s) == 0 or len(s) == 1:
            return s

        for index in range(len(s)):
            end = len(s) - 1
            print(f"max_length: {max_length}\n"
                  f"start_index: {start_index} -- end_index: {end_index}\n")
            while end >= index:
                print(f"index: {index} - end: {end}")
                # start_palin = index
                # end_palin = end
                if self.check_palindrome(s, index, end):
                    print(f"Result: True")
                    length = end-index
                    if length > max_length:
                        max_length = length
                        start_index = index
                        end_index = end
                    break
                else:
                    print(f"Result: False")
                    end -= 1
                    # print(f"end: {end} - index: {index}")


        if start_index >= 0:
            return s[start_index:end_index+1]
        else:
            return s[0]


if __name__ == '__main__':
    passed_string = input("Enter String: ")
    sol = Solution()
    final_result = sol.longest_palindrome(passed_string)

    print(f"final_result: {final_result}")
