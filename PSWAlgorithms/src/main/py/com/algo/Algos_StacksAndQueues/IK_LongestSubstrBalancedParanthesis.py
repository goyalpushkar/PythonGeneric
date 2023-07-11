'''
Given a string brackets that only contains characters '(' and ')', find the length of the longest substring
that has "balanced parentheses".

Example One
{
"brackets": "((((())(((()"
}
Output:
4
Because "(())" is the longest substring with balanced parentheses.

Example Two
{
"balanced": "()()()"
}
Output:
6
The entire string "()()()" has parentheses balanced.

Notes
A string is defined as having balanced parentheses if and only if it has an equal number of '(' and ')'
and its every prefix has at least as many '('s as ')'s.

Constraints:
1 <= length of brackets <= 105
'''
# T - O(N) , S - O(1)
def find_max_length_of_matching_parentheses(brackets):
    """
    Args:
     brackets(str)
    Returns:
     int32
    """
    n = len(brackets)
    max_length = 0

    # Scan from left to right.
    left_count = right_count = 0
    for index in range(n):
        if brackets[index] == '(':
            left_count += 1
        else:
            right_count += 1

        if right_count > left_count:
            left_count = right_count = 0
        elif left_count == right_count:
            max_length = max(max_length, 2*left_count)

    """
    Consider '(((()))'.

    First 'left_count' becomes 4, then 'right_count' becomes 3. The "balance" of left_count==right_count
    is never reached, so answer is not found. A scan in the opposite direction is needed.
    """

    # Scan from right to left.
    left_count = right_count = 0
    for index in range(n - 1, -1, -1):
        if brackets[index] == '(':
            left_count += 1
        else:
            right_count += 1

        if right_count < left_count:
            left_count = right_count = 0
        elif left_count == right_count:
            max_length = max(max_length, 2 * left_count)

    return max_length

# T - O(N) , S - O(N)
def find_max_length_of_matching_parentheses(brackets):
    """
    Args:
     brackets(str)
    Returns:
     int32
    """
    max_length = 0
    valid_from = 0
    stack_deq = deque()
    for index in range(len(brackets)):
        if brackets[index] == "(":
            stack_deq.append(index)
        else:
            if len(stack_deq) == 0:
                valid_from = index+1
            else:
                stack_deq.pop()
                substr_start = valid_from-1 if not stack_deq else stack_deq[-1]
                substr_length = index - substr_start
                max_length = max(max_length, substr_length)

    return max_length

# 28/30 passed
def find_max_length_of_matching_parentheses_wrong(brackets):
    """
    Args:
     brackets(str)
    Returns:
     int32
    """
    # Write your code here.
    stack_deq = deque()
    final_string = ""
    final_len = 0
    new_string = ""
    new_len = 0
    prev_elem = ""
    for elem in brackets:
        if elem == "(":

            if prev_elem == ')':
                new_len = len(stack_deq)
                # (new_len, new_string, final_string, final_len)
                if new_len == final_len:
                    final_string += new_string
                else:
                    if len(final_string) < len(new_string):
                        final_string = new_string

                final_len = len(stack_deq)
                new_string = ""

            stack_deq.append(elem)
            prev_elem = elem

        else:
            top_elem = stack_deq[-1] if len(stack_deq) > 0 else ""
            prev_elem = elem
            if top_elem != '(':
                continue
            else:
                new_string = stack_deq.pop() + new_string + elem
                # final_string = new_string

    if prev_elem == ')':
        new_len = len(stack_deq)
        if new_len == final_len:
            final_string += new_string
        else:
            if len(final_string) < len(new_string):
                final_string = new_string

        final_len = len(stack_deq)
        new_string = ""

    return len(final_string)