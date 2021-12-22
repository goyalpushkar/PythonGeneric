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