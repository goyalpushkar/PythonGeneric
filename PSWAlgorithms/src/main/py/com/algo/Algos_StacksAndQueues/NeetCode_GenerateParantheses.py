'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8
'''

# each time there will be a decision whethter to add open, close or both open and close parantheses
# if close count is less than open then close can be added otherwise cannot be added
# if open count is less than total count then open parantheses can be added
# if no of open and close is same then they can be added to the result set
'''
                        n=1
                        ()
                        n=2  (left open, right close)
                              (
                ((                         ()
                   (()                 ()(
                      (())               ()()
                        n=3
                                    (
                ((                                                       ()
(((                       (()                                ()(
    ((()          (()(          (())               ()((              ()()
      ((())         (()()    (())(                   ()(()        ()()(
          ((()))      (()())     (())()                ()(())          ()()()
'''

# import Stack
from collections import deque
class Solution:

    # Beats 94.7% Recursive DFS
    def generateParenthesis(self, n):
        final_result = set()

        def helper(value, open, closed):
            if open == n and closed == n:
                final_result.add(value)
                return

            if open < n:
                helper(value + "(", open + 1, closed)

            if closed < open:
                helper(value + ")", open, closed + 1)

            return

        helper("(", 1, 0)

        return final_result

    #Beats 73.14%
    def generateParenthesis_dfs(self, n):
        final_result = []
        stack = []
        def helper(open, closed):
            if open == n and closed == n:
                sol = "".join(stack)
                final_result.append(sol)
                return

            if open < n:
                stack.append("(")
                helper(open+1, closed)
                stack.pop()

            if closed < open:
                stack.append(")")
                helper(open, closed+1)
                stack.pop()

        helper(0, 0)

        return final_result

    # Beats 30%
    def generateParenthesis_bfs(self, n):

        track_queue = deque()
        final_result = set()
        if n >= 1:
            track_queue.append(("(", 1, 0))

        while len(track_queue) > 0:
            elem = track_queue.popleft()
            print(f"elem: {elem} \n"
                  f"track_queue: {track_queue}")

            # check if set is completed
            if elem[1] == n and elem[2] == n:
                final_result.add(elem[0])

            # check if open bracket can be appended
            if elem[1] < n:
                track_queue.append((elem[0] +"(", elem[1]+1, elem[2]))

            # check if close bracket can be appended
            if elem[2] < elem[1]:
                track_queue.append((elem[0] + ")", elem[1], elem[2]+1))

        print(final_result)
        return final_result

    # not right approach
    # def generateParenthesis(self, n):
    #
    #     cache = {}
    #     final_value = set()
    #     # visited_arr = Stack()
    #     def helper(value, level):
    #         print(f"{'*'*level} value: {value} at level: {level}\n"
    #               f"cache: {cache}\n")
    #         if value in cache:
    #             return # cache[value]
    #
    #         if level == n:
    #             print(f"Reached at final level\n\n")
    #             final_value.add(value)
    #             # final_value.append(value)
    #             return
    #             # return visited_arr[-1]
    #
    #         # visited_arr.push(value)
    #         helper("()"+value, level+1)
    #         cache["()" + value] = "()" + value
    #
    #         helper("("+value+")", level+1)
    #         cache["(" + value + ")"] = "(" + value + ")"
    #
    #         helper(value+"()", level+1)
    #         cache[value+"()"] = value+"()"
    #         # visited_arr.pop()
    #
    #         return
    #
    #     helper("()", 1)
    #     print(final_value)
    #
    #     return final_value   # set(final_value)