'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false


Constraints:

s consists only of printable ASCII characters.
'''


class Solution:
    from collections import deque
    def isPalindrome(self, s: str) -> bool:

        if len(s) == 0:
            return True

        charDeque = deque()
        for elem in s:
            if elem.isalnum():
                charDeque.append(elem.lower())

        while len(charDeque) > 1:
            front = charDeque.popleft()
            rear = charDeque.pop()

            if front != rear:
                return False

        return True

    def isPalindrome(self, s: str) -> bool:
        #alphanum = set('abcdefghijklmnopqrstuvwxyz0123456789')
        s = [x for x in s.lower() if x.isalnum()]
        return s == s[::-1]

    def isPalindrome(self, s: str) -> bool:

        if len(s) == 0:
            return True

        start = 0
        end = len(s) - 1

        while start <= end:
            while start < len(s) - 1 and not s[start].isalnum():
                start += 1

            while end >= 0 and not s[end].isalnum():
                end -= 1

            if s[start].lower() == s[end].lower():
                start += 1
                end -= 1
            else:
                return False

        return True

