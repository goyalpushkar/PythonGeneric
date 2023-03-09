'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
 non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


Constraints:
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''
class Solution:
    def isPalindrome(self, s):
        # processed_str = re.sub(r'[\W_]+', '', s).lower()
        # s = re.sub('[^0-9A-Za-z]','',s)

        # s = s.replace(" ", "")
        # s = ''.join(filter(str.isalnum, s)).lower()
        # return s == s[::-1]

        if len(s) == 0:
            return True

        start = 0
        end = len(s)-1
        while start <= end:
            while start < len(s)-1 and not s[start].isalnum():
                start += 1

            while end >= 0 and not s[end].isalnum():
                end -= 1

            if s[start].lower() == s[end].lower():
                start += 1
                end -= 1
            else:
                return False

        return True