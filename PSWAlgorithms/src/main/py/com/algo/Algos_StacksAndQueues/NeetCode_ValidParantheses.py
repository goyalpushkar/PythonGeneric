'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input
string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''
from collections import deque
class Solution:
    # Beats 87.47% 28ms
    def isValid(self, s):
        open_brackets = set(['(', '[', '{'])
        close_brackets = set([')', ']', '}'])
        open_close_map = {')': '(', '}': '{', ']': '['}

        if not s:
            return True

        open_stack = deque()
        for chr in s:
            if chr in open_brackets:
                open_stack.append(chr)

            if chr in close_brackets:
                if len(open_stack) == 0:
                    return False

                popped_chr = open_stack.pop()
                if open_close_map[chr] != popped_chr:
                    return False
                else:
                    continue

        return True if len(open_stack) == 0 else False

    def isValid(self, s):
        stack = []
        guide = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in guide:
                if stack and stack[-1] == guide[c]:  # stack[-1] is the top/last one in the stack
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False